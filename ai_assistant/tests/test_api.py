from fastapi.testclient import TestClient
from ai_assistant.api.main import app
from ai_assistant.semantic.router import choose_metric

client = TestClient(app)


def test_health():
    assert client.get("/health").json()["status"] == "healthy"


def test_registry():
    result = client.get("/api/v1/kpis")
    assert result.status_code == 200
    assert any(m["name"] == "delivered_orders" for m in result.json()["metrics"])


def test_unknown_metric_is_rejected():
    assert client.get("/api/v1/kpis/not_real").status_code == 404


def test_question_routing():
    assert choose_metric("How many delivered orders do we have?") == "delivered_orders"


def test_question_response(monkeypatch):
    from ai_assistant.api import main
    monkeypatch.setattr(main, "get_metric_result", lambda name: {
        "metric": name, "value": 96478, "unit": "orders",
        "description": "Distinct orders with delivered status",
        "source": "analytics.fact_orders", "status": "success"})
    response = client.post("/api/v1/ask", json={"question": "How many delivered orders do we have?"})
    assert response.status_code == 200
    assert response.json()["evidence"]["value"] == 96478
