# CiteDesk

Cited answers, checklists, and draft form fields for students abroad. This local MVP uses a small allowlisted corpus of **demo paraphrases**, not live scraped text or verbatim quotations. Source dates are review dates, not publication dates. Rules and applicability can change; check the linked official pages and responsible offices before acting.

## Run locally

Requires Python 3.10 or newer. From this folder in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000 and follow [DEMO.md](DEMO.md). Stop the server with Ctrl+C. On macOS/Linux, use `python3 -m venv .venv`, `.venv/bin/python -m pip install -r requirements.txt`, and `.venv/bin/python -m uvicorn app:app --host 127.0.0.1 --port 8000`.

## How it works and limits

Keyword matching selects local summaries in `data/corpus.json`. Each displayed passage is explicitly a paraphrase with its official source, country, publisher and review date. The output is templated, with no external AI service. Dates are suggested planning dates, never calculated legal deadlines. Matching does not establish personal eligibility, and KA131 guidance may not apply to every exchange. Check with IGI and both universities. The residence form labels are a small manually selected subset of the linked IGI form, not a complete extraction. Explicitly labelled lines in the situation can fill those fields; other values remain blank and editable. No data is saved by the app. Optional URLs are not fetched; pasted text is displayed separately as unverified and is not used as evidence. Do not paste sensitive personal data into shared deployments. No application is submitted.

## Verification

```powershell
python -m unittest discover -s tests -v
```

See [STATUS.md](STATUS.md) for the verified environment and outstanding work. This is a prototype, not legal advice or production-ready software.

## License

MIT License. See [LICENSE](LICENSE).
