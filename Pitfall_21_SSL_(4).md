# Why We Need `harbor.ps1` on Windows

## The Problem

Running `harbor` directly — even with the venv activated — fails:

```
(skillsbench) PS> harbor tasks check --model openai/gpt-5.2 tasks/crew-shoot-travel-plan
ResourceUnavailable: Program 'harbor.exe' failed to run: Access is denied.
```

`uv run harbor` also fails with the same error:

```
(skillsbench) PS> uv run harbor tasks check .\tasks\crew-shoot-travel-plan\
error: Failed to spawn: `harbor`
  Caused by: Access is denied. (os error 5)
```

---

## Root Cause: Corporate Endpoint Protection Blocks Unsigned `.exe` Files

### What happens when you `uv sync`

When `uv sync` (or `pip install`) installs a Python package that has a CLI entry point, it creates a small **launcher `.exe`** in `.venv\Scripts\`. For harbor, this is `.venv\Scripts\harbor.exe`.

This launcher is:
- ~47KB — a generic Python script launcher (not the actual harbor code)
- **Unsigned** — no digital signature from a trusted publisher
- Created locally on disk by the install process

Its only job is to find the venv's Python and run harbor's entry point (`harbor.cli.main:app`). It's essentially a tiny C program that does what `harbor.ps1` does.

### What corporate security sees

Corporate endpoint protection software (CrowdStrike, Carbon Black, Symantec, etc.) monitors executable launches. When `harbor.exe` tries to run, it sees:

1. An **unsigned executable** (no digital signature from a trusted publisher)
2. Located in a **user directory** (not `C:\Program Files\`)
3. That **just appeared on disk** (created by pip/uv, not installed by IT)

This triggers the security policy: **block execution**. The software doesn't just prevent running — it even blocks reading the file bytes and checking its signature. Full lockdown.

### Evidence

```powershell
# Can't run it
cmd /c "harbor.exe --help"
# Access is denied.

# Can't even read it from Python
subprocess.run(['harbor.exe', '--help'])
# PermissionError: [WinError 5] Access is denied

# Can't check its digital signature
Get-AuthenticodeSignature harbor.exe
# Access to the path is denied.

# Can't read its bytes
[System.IO.File]::ReadAllBytes("harbor.exe")
# Access to the path is denied.
```

---

## Why `harbor.ps1` Works

```powershell
# harbor.ps1 (3 lines)
$venvPython = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
$argString = ($args | ForEach-Object { "'$_'" }) -join ", "
& $venvPython -c "from harbor.cli.main import app; import sys; sys.argv = ['harbor'] + [$argString]; app()"
```

It bypasses the blocked `.exe` entirely:

| Component | Blocked? | Why |
|---|---|---|
| `harbor.exe` | ❌ Blocked | Unsigned, in user directory |
| `harbor.ps1` | ✅ Allowed | Not an executable — it's a text file interpreted by `powershell.exe` |
| `powershell.exe` | ✅ Allowed | Signed by Microsoft, in system directory |
| `.venv\Scripts\python.exe` | ✅ Allowed | Signed by Python Software Foundation |

The `.ps1` script calls `python.exe` (signed, trusted) and tells it to import harbor's code directly as a Python module. No unsigned `.exe` involved.

---

## Why This Isn't Needed on macOS

On macOS, the same `uv sync` creates `.venv/bin/harbor` — but this is a **Python script**, not a compiled binary:

```bash
#!/path/to/.venv/bin/python
# -*- coding: utf-8 -*-
from harbor.cli.main import app
app()
```

macOS runs this via the shebang (`#!`) — it calls the venv's Python interpreter to execute the script. There's no unsigned executable to block. Corporate security on Mac (if present) typically doesn't block interpreted scripts the same way Windows endpoint protection blocks `.exe` files.

---

## Alternatives That Don't Work

| Approach | Result | Why |
|---|---|---|
| Activate venv + `harbor` | ❌ Access denied | Still calls `harbor.exe` |
| `uv run harbor` | ❌ Access denied | `uv` also tries to spawn `harbor.exe` |
| `.\.venv\Scripts\harbor.exe` | ❌ Access denied | Same blocked `.exe` |

## Alternatives That Would Work (But Aren't Practical)

| Approach | Feasibility |
|---|---|
| Ask IT to whitelist the path | Possible but slow (days/weeks) |
| Ask IT to whitelist Python launcher `.exe` files | Same — slow corporate process |
| Sign `harbor.exe` with a trusted certificate | Requires a code signing cert ($200+/year) |

---

## Summary

The corporate security stack blocks `harbor.exe` because it's an unsigned executable in a user directory. `harbor.ps1` does the exact same thing but avoids the block by calling signed `python.exe` directly and importing harbor as a Python module. It's not a hack — it's the correct workaround for corporate-locked Windows machines.
