# Status

Built a local FastAPI and browser MVP with a three-record official-source demo corpus, source-linked paraphrases, suggested dated actions, limited manually mapped IGI form fields, explicit evidence gaps, and unverified user material kept separate. README.md, DEMO.md and SUBMISSION_DRAFT.md describe setup, the walkthrough and the submission concept.

Run with the virtual-environment commands in README.md. The preinstalled compatible environment can also run it on this machine:

```powershell
& 'C:\Users\ariba\anaconda3\envs\cuda\python.exe' -m uvicorn app:app --host 127.0.0.1 --port 8000
```

## Verification on 2026-11-15

```powershell
& 'C:\Users\ariba\anaconda3\envs\cuda\python.exe' -m unittest discover -s tests -v
& 'C:\Users\ariba\anaconda3\envs\cuda\python.exe' -m compileall -q app.py tests
node --check static/app.js
ruff check app.py tests
```

All three tests passed; compilation, JavaScript syntax and Ruff checks passed. A temporary Uvicorn server on 127.0.0.1:18765 returned HTTP 200 and the demo API returned sources R1, L1 and H1, three checklist items and three form fields; the server was stopped afterward. The globally available base Python FastAPI installation failed because its Starlette version is incompatible. A local venv was created, but dependency installation could not complete because package index DNS resolution failed. The existing cuda environment has compatible dependencies and was used without modifying it. A fresh install requires working package-index access. No browser screenshot or recording was captured.

## Remaining gaps and decisions

This is a demonstration, not a live legal knowledge system: check all official sources and eligibility, applicable rules, actual deadlines and form requirements with IGI and the universities. Checklist dates are suggestions. Retrieval is keyword-based; the optional source URL is not fetched and pasted text is not used as evidence. Form fields are only a manually mapped subset, not full extraction. There is no persistence, authentication, automated submission or production security review. The no-evidence behavior is intentionally conservative but topic matching cannot detect every unanswered question. Public repo, Vultr deployment, recorded demo on Vultr, public URL and final submission require Kağan's decisions and remain undone. No deployment, submission or paid service was used.
