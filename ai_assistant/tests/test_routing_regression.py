import pytest
from ai_assistant.semantic.router import choose_metric

@pytest.mark.parametrize("question, expected", [
    ("How much GMV did we generate from delivered orders?", "delivered_gmv"),
    ("What is our delivered GMV?", "delivered_gmv"),
    ("How many delivered orders do we have?", "delivered_orders"),
    ("What is the average order value?", "delivered_aov"),
    ("What is our total GMV?", "total_gmv"),
    ("What is the late delivery rate?", "late_delivery_rate"),
    ("Tell me a joke", None),
])
def test_intent_selection(question, expected, monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert choose_metric(question) == expected
