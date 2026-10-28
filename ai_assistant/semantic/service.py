from decimal import Decimal
from ..api.database import get_db_connection
from .metrics import get_metric


def get_metric_result(metric_name: str) -> dict:
    metric = get_metric(metric_name)
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(metric.sql)
            record = cur.fetchone()
    value = record[0] if record else None
    if isinstance(value, Decimal):
        value = str(value)  # financial precision preserved
    return {"metric": metric.name, "value": value, "unit": metric.unit,
            "description": metric.description, "source": metric.source,
            "status": "success"}
