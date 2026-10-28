import os
import re
from ai_assistant.semantic.metrics import METRICS
from ai_assistant.semantic.router import choose_metric


def test_all_queries_are_approved_selects():
    for metric in METRICS.values():
        sql = metric.sql.strip()
        assert sql.upper().startswith("SELECT ")
        assert not re.search(r";|\b(INSERT|UPDATE|DELETE|DROP|ALTER|TRUNCATE|CREATE)\b", sql, re.I)


def test_routing_without_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert choose_metric("How many delivered orders do we have?") == "delivered_orders"
    assert choose_metric("What is our delivered GMV?") == "delivered_gmv"
    assert choose_metric("What is our total GMV?") == "total_gmv"
    assert choose_metric("What is the average order value?") == "delivered_aov"
    assert choose_metric("What percentage of orders were late deliveries?") == "late_delivery_rate"
    assert choose_metric("Tell me a joke") is None
