# Retrieval-Based Website Chatbot

CodeAlpha Cloud Computing Internship project.

Flask FAQ chatbot with predefined intent patterns, browser chat interface, JSON API and fallback responses.

## Local setup

```bash
python -m venv .venv
# Activate the virtual environment
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000.

## Tests

```bash
python -m pytest -q
```

## Configuration

No API key required.

## Files

- `app.py`: Flask backend
- `templates/index.html`: frontend
- `static/style.css`: UI
- `tests/test_app.py`: tests
- `requirements.txt`: dependencies
- `Procfile`: Gunicorn startup

## Scope

Educational prototype. Deployment and production security review have not been completed.
