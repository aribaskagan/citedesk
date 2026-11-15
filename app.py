from datetime import date, timedelta
import json
import re
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent
CORPUS = json.loads((ROOT / 'data/corpus.json').read_text(encoding='utf-8-sig'))
app = FastAPI(title='CiteDesk')
app.mount('/static', StaticFiles(directory=ROOT / 'static'), name='static')

class Query(BaseModel):
    situation: str = Field(min_length=1, max_length=10000)
    official_text: str = Field(default='', max_length=10000)
    source_url: str = Field(default='', max_length=2000)

@app.get('/')
def index():
    return FileResponse(ROOT / 'static/index.html')

@app.post('/api/answer')
def answer(query: Query):
    text = query.situation.lower()
    words = set(re.findall(r"[a-z]+", text))
    hits = [doc for doc in CORPUS if words.intersection(doc['keywords'])]
    today = date.today()
    checklist = [{'date': (today + timedelta(days=i)).isoformat(), 'action': doc['action'], 'source': doc['id']} for i, doc in enumerate(hits)]
    # Values are accepted only from explicit labelled lines, never inferred.
    supplied = {}
    for line in query.situation.splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            if key.strip().lower() in {'residence', 'date of last entry in romania', 'study grade'}:
                supplied[key.strip().lower()] = value.strip()[:200]
    fields = [{'label': label, 'value': supplied.get(label.lower(), ''), 'source': doc['id'], 'form_url': doc['form_url']} for doc in hits for label in doc['fields']]
    return {'sources': hits, 'checklist': checklist, 'fields': fields,
            'warning': 'Demo summaries, not live source text or legal advice. Confirm applicability, deadlines and current requirements with the relevant office. Suggested dates are planning dates, not official deadlines.',
            'missing': 'We cannot verify your personal eligibility, exact deadline, insurance proof or institution-specific form requirements from this corpus. Check with the territorial IGI office and your sending and receiving universities.',
            'user_material': {'text': query.official_text[:2000], 'url': query.source_url} if query.official_text or query.source_url else None}
