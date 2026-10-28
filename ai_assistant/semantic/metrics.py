from dataclasses import dataclass

@dataclass(frozen=True)
class MetricDefinition:
    name: str
    description: str
    sql: str
    unit: str
    source: str
    aliases: tuple[str, ...]

# Register ONLY validated, read-only SQL here.
# Keep delivered GMV out until the exact field/formula agrees with Power BI.
METRICS = {
    "delivered_orders": MetricDefinition(
        name="delivered_orders",
        description="Distinct orders with delivered status",
        sql="""SELECT COUNT(DISTINCT order_id)
               FROM analytics.fact_orders
               WHERE order_status = 'delivered'""",
        unit="orders",
        source="analytics.fact_orders",
        aliases=("delivered orders", "orders delivered", "how many deliveries", "number of delivered orders"),
    ),
}


def get_metric(name: str) -> MetricDefinition:
    return METRICS[name]
