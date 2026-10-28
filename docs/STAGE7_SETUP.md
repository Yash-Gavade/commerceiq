# CommerceIQ 360 — Stage 7 implementation

## Merge with your existing repository (do not delete existing files)

Copy `ai_assistant/` to the existing `commerceiq/ai_assistant/`, adding/replacing **only the specific stage-7 files** listed in this package. Back up existing `ai_assistant/api/main.py` before replacement. Copy `docs/inspect_analytics_schema.sql` to your existing `docs/` folder. Keep existing `sql/`, `src/`, `dashboards/`, `PowerBi/`, and root requirements unchanged.

## Configuration

Existing root `.venv` is reused. From the root of `commerceiq` in Windows CMD:

```cmd
.venv\Scripts\activate.bat
python -m pip install -r ai_assistant\requirements-stage7.txt
copy ai_assistant\.env.example ai_assistant\.env
```

Update only the DB_PASSWORD in `.env` and ensure `.gitignore` includes `.env`, `.env.*`, `!.env.example`, `.venv/` (avoid accidentally committing credentials). A new `.env` is not needed if you already have one; **do not overwrite your working `.env`**.

## Terminal 1 — FastAPI

```cmd
python -m uvicorn ai_assistant.api.main:app --reload --port 8000
```

Open `http://127.0.0.1:8000/docs`, test GET `/api/v1/kpis/delivered_orders` and POST `/api/v1/ask` with body `{"question":"How many delivered orders do we have?"}`.

## Terminal 2 — Streamlit

```cmd
.venv\Scripts\activate.bat
python -m streamlit run ai_assistant\app\streamlit_app.py
```

## Tests

```cmd
python -m pytest ai_assistant\tests -q
```

These are unit tests with a mocked KPI result; they do not prove production data fidelity. Validate database KPI results separately against DBeaver and Power BI.

## Optional LLM classifier

Set `OPENAI_API_KEY` in your local `.env` only if you want the OpenAI Responses API to classify questions. LLM never writes SQL or computes a KPI. With no key, recognized alias questions still work locally. The classifier chooses only a registered metric or returns unsupported. OpenAI API usage may be billed separately from ChatGPT.

## IMPORTANT: GMV is not enabled yet

Run `docs/inspect_analytics_schema.sql` in DBeaver. Cross-check exact GMV definition with your SQL models and Power BI: whether delivered-only, whether price excludes freight, whether order-item joins multiply rows, and which date/status are used. Only then register a `delivered_gmv` entry in `semantic/metrics.py`. Likewise, do not add AOV, monthly growth, retention, logistics, or seller metrics until verified.

## Production hardening still required

This is a local demo, **not a publicly deployable production service**. Add API authentication, rate limiting, TLS, secret management, network-restricted DB permissions, robust DB readiness and audit/monitoring before a public deployment. Restrict exposure of raw business questions/data to external LLM providers and comply with organizational privacy rules. Add metric-specific contract tests comparing API/SQL/Power BI results.
