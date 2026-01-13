8️⃣ Why token signing is asymmetric (important)
Asymmetric signing means:
signing key is protected
verification is public
services scale infinitely
no shared secrets
If symmetric signing were used:
every service would need the secret
compromise = catastrophic
 
1️⃣ First: what “signing” actually means
Signing ≠ encrypting
Signing means:
“I attach a cryptographic proof that this message came from me and wasn’t changed.”
The message remains readable.
2️⃣ Symmetric signing (shared secret)
🔑 What it is
One secret key
Same key is used to:
sign the message
verify the signature
Everyone who can verify can also forge.
🔐 Real-world analogy
A shared password
If you know the password, you can:
verify messages
impersonate the sender
 
🚨 Why symmetric signing is dangerous at scale
Imagine Azure had 1,000 services:
Service AService BService C
...
Service Z
Each one needs the secret key
If any one service is compromised:
attacker gets the key
attacker can forge tokens
entire ecosystem compromised
This is unacceptable.
❌ Symmetric signing in Azure tokens?
No. Never.
It is only used in:
internal systems
tightly controlled microservices
legacy APIs
 
3️⃣ Asymmetric signing (public/private key)
🔑 What it is
Two keys
Private key → sign
Public key → verify
Public key cannot sign
 
🚨 Why asymmetric signing scales
Only issuer can sign
Everyone can verify
Compromise of verifier ≠ compromise of issuer
This is critical for cloud platforms.
 
 
It does these steps:
Split the JWT into header, payload, signature
Decode header to get alg (RS256) and kid (key ID)
Fetch the public key corresponding to kid (from Azure AD / JWKS endpoint)
Compute the hash of header + "." + payload using SHA-256
Decrypt the signature with the public key
Compare hashes:
If hash from signature matches hash of message → ✅ valid
Else → ❌ invalid (tampered or wrong issuer)
 
json headers + payloads -> base64 encoding -> unsigned message -> compute hash of message (32 bytes/256 bits)-> pad the hash (2048 bits/256 bytes for RSA key size)-> sign with private key (256 bytes/2048 bits) (raw binary data)-> base64 encoding -> final JWT to be sent
 
split JWT -> decode signature (to bytes) -> recompute hash of message (without signature) -> verify signature with public key (performs reverse mathmatical operations to check if it matches with required signature structure, e.g., prefix / padding) -> remove padding (output is hash_from_signature) -> compare hashes (hash_from_signature == hash_of_message)
 
 
public key must be from a trusted source, 🚨 If the public key is fetched from an untrusted source, security is already broken.
 
Why headers & payload are NOT hashed
 
These are:
routing info
identity claims
authorization context
➡️ Every service that receives the token must be able to read them
Hashing would destroy that.
 
First: what the signature REALLY is (important correction)
The signature is NOT:
“encrypted hash”
It IS:
a mathematical proof that the signer knew the private key and signed this exact hash.
That distinction matters.
 
What RSA signing ACTUALLY does (conceptual, no math formulas)
With RSA:
The private key applies a mathematical transformation to the hash
The public key applies the inverse mathematical transformation
This pair has ONE special property:
Only the public key corresponding to the private key can validate that transformation.
That’s it.
This is not encryption for secrecy.

It’s authentication for proof.
 
 
Now the most important question you asked
“Can anyone extract the hash from a true signature?”
Short answer
Yes — but only if they have the correct public key.
Long answer (important nuance)
The signature does contain the hash
But it is not readable
You must apply the correct public key to recover it
Without the correct public key → meaningless output


 
for symmetric JWT (HS256/HMAC) workflow - Step-by-step with input/output format:
 
| Step | Input                                                          | Operation            | Output                              |
| ---- | -------------------------------------------------------------- | -------------------- | ----------------------------------- |
| 1    | JSON header (text)                                             | base64url encode     | base64url(header)                   |
| 2    | JSON payload (text)                                            | base64url encode     | base64url(payload)                  |
| 3    | Header + Payload                                               | Concatenate with `.` | unsigned_message = "header.payload" |
| 4    | unsigned_message + secret_key                                  | HMAC_SHA256          | signature_bytes (32 bytes)          |
| 5    | signature_bytes                                                | base64url encode     | signature (text, safe for JWT)      |
| 6    | base64url(header) + "." + base64url(payload) + "." + signature | Concatenate          | final JWT string to send            |

 
 
 
| Step | Input                                                          | Operation                                                | Output                                                      |
| ---- | -------------------------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------- |
| 1    | Received JWT string                                            | Split by `.`                                             | base64url(header), base64url(payload), base64url(signature) |
| 2    | base64url(header), base64url(payload)                          | base64url decode                                         | JSON header (text), JSON payload (text)                     |
| 3    | JSON header + payload                                          | Concatenate base64url(header) + "." + base64url(payload) | unsigned_message                                            |
| 4    | unsigned_message + shared secret key                           | HMAC_SHA256                                              | computed_signature_bytes (32 bytes)                         |
| 5    | base64url(signature) from JWT                                  | base64url decode                                         | received_signature_bytes (32 bytes)                         |
| 6    | Compare: computed_signature_bytes == received_signature_bytes? | Byte-by-byte comparison                                  | ✅ True → valid, ❌ False → invalid/tampered                  |

 
 
1️⃣ Byte vs Hash
Hash is the result of a hashing function, like SHA-256.
SHA-256 outputs 32 bytes, which is a sequence of 32 binary numbers (0–255).
These bytes are often represented as hex strings (b9f...) or Base64, but underneath they are still just bytes.
So when we say “compare hashes”, it literally means compare the 32 bytes that the hash function produced.
✅ In other words, hash = bytes; the “hash” is just a name for the bytes generated by a hash function.



| Aspect       | Asymmetric (RS256)                        | Symmetric (HS256)                                                          |
| ------------ | ----------------------------------------- | -------------------------------------------------------------------------- |
| Key usage    | Private key signs, public key verifies    | Shared secret key both signs & verifies                                    |
| Hash         | Recovered from signature using public key | Computed independently via HMAC + secret                                   |
| Verification | Can detect tampering and prove sender     | Can detect tampering but cannot prove sender identity beyond secret holder |
| Signature    | 256 bytes (RSA-2048)                      | 32 bytes (HMAC-SHA256)                                                     |
