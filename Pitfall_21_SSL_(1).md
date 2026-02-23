Below are incorrect:

# SSL Connection Error Fix for Harbor / LiteLLM

## Issue

Running `harbor tasks check` or `harbor run` fails with:

```
❌ Error: litellm.InternalServerError: InternalServerError: OpenAIException - Connection error.
```

## Root Cause

The corporate network intercepts HTTPS traffic with its own SSL certificate (SSL inspection / man-in-the-middle proxy). Python's `httpx` library rejects the corporate certificate because it is not in Python's trusted CA bundle, causing:

```
SSL: CERTIFICATE_VERIFY_FAILED - unable to get local issuer certificate
```

This affects any Python HTTP call to `api.openai.com`, including the OpenAI SDK and LiteLLM.

## Fix

Set the following environment variables before running any harbor command:

```powershell
$env:SSL_CERT_FILE = ""
$env:CURL_CA_BUNDLE = ""
$env:PYTHONHTTPSVERIFY = "0"
```

`SSL_CERT_FILE=""` is the most important — it makes Python fall back to the Windows certificate store (which has the corporate CA) instead of the `certifi` bundle (which doesn't). The other two are extra safety.

### Example

```powershell
$env:SSL_CERT_FILE = ""; $env:CURL_CA_BUNDLE = ""; $env:PYTHONHTTPSVERIFY = "0"
.\harbor.ps1 tasks check --model openai/gpt-5.2 tasks/crew-shoot-travel-plan
.\harbor.ps1 run -a codex -m gpt-5.2 -p tasks-no-skills/crew-shoot-travel-plan-3.1
```

### Make it persistent for the session

Add to your PowerShell profile or run once per terminal session:

```powershell
$env:SSL_CERT_FILE = ""
$env:CURL_CA_BUNDLE = ""
$env:PYTHONHTTPSVERIFY = "0"
```

**Note:** `PYTHONHTTPSVERIFY` alone is NOT enough — it only affects Python's `urllib`, not `httpx` (which litellm uses). You need `SSL_CERT_FILE=""` as well.

## Notes

- This disables SSL certificate verification for all Python processes in the session.
- Only needed on networks with SSL inspection (corporate firewalls, Zscaler, etc.).
- `Invoke-RestMethod` (PowerShell native) is unaffected because it uses the Windows certificate store, not Python's CA bundle.

## What Actually Happens (Step by Step)

### Normal HTTPS (no corporate interception)

1. Python opens a TCP connection to `api.openai.com:443`.
2. OpenAI's server presents its SSL certificate, signed by a public CA (e.g., Let's Encrypt or DigiCert).
3. Python's `httpx` checks the certificate chain: OpenAI cert → intermediate CA → root CA.
4. The root CA exists in Python's trusted CA bundle (`certifi` package), so the chain is valid.
5. TLS handshake completes. All traffic is encrypted end-to-end between Python and OpenAI.

### With corporate SSL interception

1. Python opens a TCP connection to `api.openai.com:443`.
2. The corporate firewall (e.g., Zscaler, Palo Alto) **intercepts** this connection before it reaches OpenAI.
3. The firewall makes its own separate HTTPS connection to `api.openai.com` on your behalf, receives OpenAI's real certificate, and establishes a real TLS session with OpenAI.
4. The firewall then presents **its own fake certificate** for `api.openai.com` back to your machine. This certificate is signed by the **corporate root CA**, not by DigiCert or Let's Encrypt.
5. Python's `httpx` checks the certificate chain: fake OpenAI cert → **corporate root CA**.
6. Python looks for the corporate root CA in its trusted CA bundle (`certifi`). **It's not there.** The `certifi` package only contains public CAs, not your company's private CA.
7. Certificate verification fails → `SSL: CERTIFICATE_VERIFY_FAILED`.

### Why PowerShell works but Python doesn't

- Your IT department installs the corporate root CA into the **Windows certificate store** (via Group Policy).
- PowerShell's `Invoke-RestMethod` uses the Windows certificate store → finds the corporate CA → trusts it → works.
- Python uses its own bundled CA list (`certifi` package) → corporate CA is not in it → fails.

### What `PYTHONHTTPSVERIFY=0` does

It tells Python: "Skip step 6 entirely — don't verify the certificate chain at all, just accept whatever certificate is presented." The TLS connection is still encrypted, but Python no longer checks *who* it's encrypted with. The firewall's fake certificate is accepted without question.

### Diagram

```
Without interception:
  Python ──TLS──► api.openai.com
  (OpenAI cert, signed by DigiCert ✅)

With corporate interception:
  Python ──TLS──► Corporate Firewall ──TLS──► api.openai.com
  (Fake cert, signed by Corp CA ❌)    (Real cert, signed by DigiCert ✅)
  Python only sees the left side.
```

---

## Deep Dive: How Certificate Verification Actually Works

### What's in the `.pem` file?

The `certifi` package ships a file called `cacert.pem`. It does **not** contain website certificates. It contains **~130 root CA public keys** — organizations like DigiCert, Let's Encrypt, and GlobalSign. These root CAs have certificates that last **20–30 years**. They almost never change. That's why a bundled file works.

### The verification is pure math, not a server call

Python does **not** contact any authorization server to verify a certificate. It's all public key cryptography:

1. **When OpenAI buys a certificate**, DigiCert (the CA) uses its **private key** (secret, locked in a vault) to **sign** it:
   `signature = encrypt(hash(openai_cert), digicert_private_key)`

2. **When Python receives OpenAI's cert**, it does the reverse using DigiCert's **public key** (from the `.pem` file):
   `hash = decrypt(signature, digicert_public_key)`

3. If the decrypted hash matches the cert's actual hash → the cert is genuine. If not → rejected.

This is pure math. No network call needed. The `.pem` file has the public key, that's all you need.

### What about certificates that change frequently?

Website certs (like OpenAI's) rotate every 90 days to 1 year. But **the root CA that signs them stays the same**:

- OpenAI cert 2025 → signed by DigiCert → ✅ DigiCert public key in `.pem`
- OpenAI cert 2026 → signed by DigiCert → ✅ same DigiCert public key in `.pem`
- OpenAI cert 2027 → signed by DigiCert → ✅ still works

The `.pem` file doesn't need to know about every website cert. It only needs the ~130 root CA keys, which rarely change.

### Is there any live server call?

There is one optional network call: **OCSP** (Online Certificate Status Protocol). This checks if a certificate was **revoked** (e.g., stolen private key). But it's separate from trust verification:

| What | How | Network call? |
|---|---|---|
| **Is this cert signed by a trusted CA?** | Math (public key in `.pem`) | ❌ No |
| **Has this cert been revoked?** | OCSP query to CA server | ✅ Yes (optional) |
| **Has this cert expired?** | Compare date | ❌ No |

### Why does corporate interception break this?

The firewall generates a **fake certificate** for `api.openai.com` on the fly, signed by the **corporate CA**. Python does the math:

- Try DigiCert's public key → `decrypt(signature, digicert_key)` → **doesn't match**
- Try Let's Encrypt's key → **doesn't match**
- Try all ~130 CAs in `.pem` → **none match**
- The corporate CA isn't in the list → **verification fails**

It's like someone showing you an ID card with the right name on it, but stamped by an office you've never heard of.

---

## Why Does the Company Do This?

The whole point of SSL interception is that the firewall can **decrypt and read all your HTTPS traffic**. Without interception, HTTPS is end-to-end encrypted — the firewall only sees that you connected to `api.openai.com` but can't see **what** you sent.

With interception, the firewall decrypts your traffic, inspects it, then re-encrypts it to forward to OpenAI. This enables:

1. **Data Loss Prevention (DLP)** — detect if someone is uploading confidential files, source code, or customer data to external services (Dropbox, Gmail, ChatGPT, etc.)
2. **Malware scanning** — inspect downloaded files and responses for viruses/exploits before they reach your machine, even over HTTPS
3. **Compliance / Audit** — log what employees send to external APIs (e.g., your OpenAI API calls — they can see the prompts and responses)
4. **Block prohibited content** — enforce policies on what sites/services can be accessed and what data can leave the network

**In short**: your API calls, prompts, and OpenAI's responses are all visible to the corporate firewall. That's the entire purpose of SSL interception.
