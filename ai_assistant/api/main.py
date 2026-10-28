import logging
import psycopg
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from ..semantic.metrics import METRICS
from ..semantic.router import choose_metric
from ..semantic.service import get_metric_result

logger = logging.getLogger(__name__)
app = FastAPI(title="CommerceIQ 360 KPI Intelligence API", version="1.2.0")


class Question(BaseModel):
    question: str = Field(min_length=3, max_length=500)


@app.get("/")
def home():
    return {"project": "CommerceIQ 360", "status": "running"}


@app.get("/health")
def health():
    return {"status": "healthy"}  # liveness, not DB readiness


@app.get("/api/v1/kpis")
def list_kpis():
    return {"metrics": [{"name": m.name, "description": m.description,
                          "unit": m.unit, "source": m.source} for m in METRICS.values()]}


@app.get("/api/v1/kpis/{metric_name}")
def get_kpi(metric_name: str):
    if metric_name not in METRICS:
        raise HTTPException(status_code=404, detail="Unknown KPI")
    try:
        return get_metric_result(metric_name)
    except psycopg.Error:
        logger.exception("KPI query failed for %s", metric_name)
        raise HTTPException(status_code=503, detail="KPI database temporarily unavailable")


@app.post("/api/v1/ask")
def ask(body: Question):
    try:
        metric_name = choose_metric(body.question)
    except Exception:
        logger.exception("Question classification failed")
        raise HTTPException(status_code=503, detail="Question interpretation temporarily unavailable")
    if metric_name is None:
        return {"status": "unsupported", "answer":
                "I can only answer registered KPIs. Try: How many delivered orders do we have?",
                "metric": None, "evidence": None}
    try:
        evidence = get_metric_result(metric_name)
    except psycopg.Error:
        logger.exception("Query failed for %s", metric_name)
        raise HTTPException(status_code=503, detail="KPI database temporarily unavailable")
    value = evidence["value"]
    formatted = f"{value:,}" if isinstance(value, int) else str(value)
    answer = (f"{evidence['description']}: {formatted} {evidence['unit']}. "
              f"Source: {evidence['source']}.")
    return {"status": "success", "answer": answer,
            "metric": metric_name, "evidence": evidence}
