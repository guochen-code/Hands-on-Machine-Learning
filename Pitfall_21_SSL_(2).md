# SSL Connection Error: Troubleshooting & Fix

## The Issue

Running `harbor tasks check` or `harbor run` fails with:

```
❌ Error: litellm.InternalServerError: InternalServerError: OpenAIException - Connection error.
```

The underlying error is:

```
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)
```

This affects any Python HTTP call to `api.openai.com`, including the OpenAI SDK and LiteLLM.

---

## Root Cause

### Corporate SSL Interception

The corporate network runs a **man-in-the-middle proxy** (e.g., Zscaler, Palo Alto) that intercepts all HTTPS traffic:

```
Without interception:
  Python ──TLS──► api.openai.com
  (OpenAI cert, signed by DigiCert ✅)

With corporate interception:
  Python ──TLS──► Corporate Firewall ──TLS──► api.openai.com
  (Fake cert, signed by Corp CA ❌)    (Real cert, signed by DigiCert ✅)
  Python only sees the left side.
```

1. Python opens a connection to `api.openai.com:443`.
2. The corporate firewall **intercepts** the connection before it reaches OpenAI.
3. The firewall connects to OpenAI on your behalf with a real TLS session.
4. The firewall presents **its own certificate** for `api.openai.com` back to your machine, signed by the **corporate root CA** (not DigiCert).
5. Python's `httpx` library checks the certificate chain against its trusted CA bundle (the `certifi` package).
6. The corporate root CA is **not** in `certifi`'s bundle → verification fails.

### Why PowerShell works but Python doesn't

- IT installs the corporate root CA into the **Windows certificate store** (via Group Policy).
- PowerShell's `Invoke-RestMethod` uses the Windows certificate store → finds the corporate CA → works.
- Python uses its own bundled CA list (`certifi` package) → corporate CA is missing → fails.

---

## Troubleshooting Steps

### Step 1: Confirmed the error is SSL-related

Ran harbor and got `Connection error`. Enabled LiteLLM debug logging and saw `CERTIFICATE_VERIFY_FAILED`. This pointed to SSL certificate verification, not a network connectivity issue.

### Step 2: Tried environment variables (❌ Did Not Work)

```powershell
$env:SSL_CERT_FILE = ""
$env:CURL_CA_BUNDLE = ""
$env:PYTHONHTTPSVERIFY = "0"
```

These env vars seemed to work in one VS Code terminal but **not in another**, even with the same Python binary, same venv, and same working directory. This was confusing.

**Why these don't actually work:**

| Variable | What it affects | Why it doesn't help |
|---|---|---|
| `PYTHONHTTPSVERIFY=0` | Python's `urllib` module only | LiteLLM uses `httpx`, not `urllib` |
| `SSL_CERT_FILE=""` | Python's default `ssl` context | `httpx` explicitly loads `certifi`'s CA bundle, ignoring this |
| `CURL_CA_BUNDLE=""` | `curl` and `requests` library | `httpx` doesn't check this variable |

**Key insight**: `httpx` ignores all of these env vars. It hardcodes `certifi.where()` as its CA bundle. These env vars only help libraries that use Python's default SSL context (like `urllib` or `requests`), not `httpx`.

The earlier "success" in one terminal was likely due to `truststore` being imported in that session's state (after we installed it and tested interactively).

### Step 3: Tested `httpx.Client(verify=False)` (✅ Worked, But Not Practical)

Created a test script using `httpx.Client(verify=False)`:

```python
import httpx
client = httpx.Client(verify=False)
r = client.get("https://api.openai.com/v1/models")
print("Status:", r.status_code)  # 401 — SSL worked, just no API key
```

This confirmed the problem was purely SSL verification. But we can't modify `httpx` calls inside LiteLLM — it's a third-party library.

### Step 4: Installed `truststore` (❌ Installed But Not Enough)

```powershell
.\.venv\Scripts\pip.exe install truststore
```

`truststore` makes Python's `ssl` module use the OS certificate store instead of `certifi`'s bundle. However, simply installing it does nothing — it must be **activated** by calling `truststore.inject_into_ssl()` before any HTTP calls are made. There was no place to call this in LiteLLM/harbor's code.

### Step 5: Verified both terminals use same Python

```powershell
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable); print(sys.version)"
# Both terminals: Python 3.12.10 from the same venv
```

Same Python, same version, same cwd — ruled out environment differences.

### Step 6: Direct httpx test in the failing terminal

```powershell
.\.venv\Scripts\python.exe -c "import os; print('SSL_CERT_FILE:', repr(os.environ.get('SSL_CERT_FILE'))); import httpx; r = httpx.get('https://api.openai.com/v1/models'); print('Status:', r.status_code)"
```

Output:
```
SSL_CERT_FILE: ''
httpx.ConnectError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
```

**This proved definitively that `SSL_CERT_FILE=""` does NOT help `httpx`.** The env var was set (confirmed by the print), but httpx still failed. This was the breakthrough moment.

### Step 7: `sitecustomize.py` with `truststore` (✅ The Fix)

Created `.venv\Lib\site-packages\sitecustomize.py` — Python automatically executes this file on every startup, before any user code runs.

---

## The Correct Solution

### The file

`.venv\Lib\site-packages\sitecustomize.py`:

```python
"""Auto-inject truststore to use Windows certificate store for SSL."""
try:
    import truststore
    truststore.inject_into_ssl()
except Exception:
    pass
```

### Prerequisites

```powershell
.\.venv\Scripts\pip.exe install truststore
```

### Why this works

1. **`sitecustomize.py`** is a special Python file. Python automatically imports it during startup, before any other code runs. Placing it in the venv's `site-packages` makes it run every time this venv's Python is used.

2. **`truststore.inject_into_ssl()`** monkey-patches Python's `ssl` module at the lowest level. It replaces the default certificate verification mechanism so that **all** SSL contexts — including those created by `httpx`, `requests`, `urllib`, or any other library — use the **Windows certificate store** instead of `certifi`'s bundled `.pem` file.

3. The **Windows certificate store** already has the corporate root CA (installed by IT via Group Policy). So when `httpx` creates an SSL connection:
   - **Before fix**: `httpx` → `ssl` module → `certifi` bundle → corporate CA missing → ❌
   - **After fix**: `httpx` → `ssl` module (patched by truststore) → Windows cert store → corporate CA found → ✅

### Why this is better than the other approaches

| Approach | Scope | Security | Works with httpx? |
|---|---|---|---|
| `PYTHONHTTPSVERIFY=0` | `urllib` only | Disables ALL verification | ❌ No |
| `SSL_CERT_FILE=""` | Default ssl context | Depends on OS | ❌ No (httpx ignores it) |
| `verify=False` in code | One client only | Disables ALL verification | ✅ But requires code changes |
| **`truststore` + `sitecustomize.py`** | **All libraries** | **Proper verification via OS store** | **✅ Yes** |

The `truststore` approach is the only solution that:
- Works with `httpx` (which LiteLLM uses)
- Requires no code changes to LiteLLM or harbor
- Still performs **proper certificate verification** (just against the OS store instead of `certifi`)
- Applies automatically to every Python process from this venv

---

## Deep Dive: How Certificate Verification Works

### What's in the `.pem` file?

The `certifi` package ships `cacert.pem` — **~130 root CA public keys** (DigiCert, Let's Encrypt, GlobalSign, etc.). These root CAs have certificates lasting 20–30 years. It does NOT contain website certificates.

### Verification is pure math, not a server call

1. **When OpenAI buys a certificate**, DigiCert signs it with its **private key**:
   `signature = encrypt(hash(openai_cert), digicert_private_key)`

2. **When Python receives the cert**, it uses DigiCert's **public key** (from `.pem`) to verify:
   `hash = decrypt(signature, digicert_public_key)`

3. If the decrypted hash matches → cert is genuine. No network call needed.

### Why corporate interception breaks this

The firewall generates a fake certificate signed by the corporate CA. Python tries every key in `certifi` — none match the corporate CA's signature → fails.

It's like someone showing you an ID card stamped by an office you've never heard of.

---

## Why Does the Company Do This?

SSL interception lets the firewall **decrypt and read all HTTPS traffic**. This enables:

1. **Data Loss Prevention** — detect uploads of confidential data to external services
2. **Malware scanning** — inspect downloads for viruses, even over HTTPS
3. **Compliance / Audit** — log API calls (your prompts and responses are visible)
4. **Content blocking** — enforce access policies

---

## Summary

| Step | What We Tried | Result | Why |
|---|---|---|---|
| 1 | Diagnose error | SSL verification failure | Corporate proxy intercepts HTTPS |
| 2 | Env vars (`SSL_CERT_FILE`, etc.) | ❌ Failed | `httpx` ignores these vars |
| 3 | `httpx.Client(verify=False)` | ✅ Works | Confirms SSL is the issue |
| 4 | Install `truststore` | ❌ Not enough | Needs to be activated before imports |
| 5 | Verify same Python in both terminals | ✅ Same | Rules out env differences |
| 6 | Direct httpx test with env vars | ❌ Failed | **Proves** env vars don't help httpx |
| 7 | **`sitecustomize.py` + `truststore`** | **✅ Fixed** | Patches ssl module before any code runs |

**The fix is a single file**: `.venv\Lib\site-packages\sitecustomize.py` — 4 lines of Python.
