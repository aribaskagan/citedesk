# HackGlobal submission draft: CiteDesk

**Entrant:** Kağan Arıbaş
**Team:** kegan (solo)
**Track:** ML/AI, Track 03 Grounded knowledge and RAG; overlaps with Track 01 Agentic and GenAI apps and Track 04 Civic and real-world impact.

## Problem and solution

International students face fragmented rules, unfamiliar procedures and inconsistent advice. CiteDesk turns a situation into source-linked summaries, suggested next steps and draft form fields for review. It serves students navigating mobility and international offices answering recurring questions. The prototype focuses on Romanian student residence, Erasmus+ learning agreements and health coverage.

## System design

```mermaid
flowchart LR
    A[Student situation] --> B[FastAPI keyword retrieval]
    C[Local allowlisted source summaries] --> B
    B --> D[Source-linked paraphrases]
    B --> E[Suggested checklist]
    B --> F[Reviewable form fields]
    G[Optional user text and URL] --> H[Separate unverified display]
```

The local corpus contains manually written demo paraphrases and official links, not a live scrape. Templated output requires no model or paid API. Users verify current rules and review every field. The app never sends forms to an office. Checklist dates are suggestions, not deadlines. The first form mapping is a limited manual subset and the optional text is not used as evidence.

## Implemented

The local prototype includes a web interface, FastAPI endpoint, three source records, keyword matching, citations, checklist, limited form drafts, and explicit evidence gaps. See DEMO.md for the walkthrough and STATUS.md for verification.

Public repository (15 November 2026): https://github.com/aribaskagan/citedesk (MIT License).

A local demo video of the MVP running on http://127.0.0.1:8000 was recorded on 15 November 2026. It is stored only on the build machine at `citedesk-local-demo.mp4` (about 46 seconds, under the 3-minute limit). It has not been uploaded anywhere.

## Still blocked (need Kağan's OK)

- Claiming Vultr credits
- Deploying the backend on a Vultr Compute instance
- Publishing a public product-style demo URL
- Uploading the demo video anywhere public
- Final submission on Vultr Community

Validate official sources, eligibility logic, dates, form coverage, privacy, security and accessibility before real use. Collect user feedback across countries and team or community participation separately; no reach is claimed here.
