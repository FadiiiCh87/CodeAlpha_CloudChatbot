# Multilingual FAQ Chatbot — CodeAlpha

## Features
- Cloud-hosted Flask chatbot with keyword and approximate string retrieval.
- English, Roman Urdu and Arabic sample keywords, suggested topic buttons, confidence score, safe fallback.
- Curated FAQ responses with no fabricated contact email. JSON API and responsive website.

## API
GET /health; GET /api/topics; POST /api/chat JSON: {"message":"What is pricing?"}.

## Run and test
`pip install -r requirements.txt`; `gunicorn app:app`; `python -m pytest -q`. GitHub Actions tests pushes and pull requests.

## Limitations
This is **not an LLM or document-based RAG chatbot**. It is an explainable, low-cost FAQ retrieval prototype. Responses and multilingual keywords are illustrative; configure verified business content before use. Production deployment should add distributed rate limiting and monitoring.
