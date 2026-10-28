from dataclasses import dataclass


@dataclass(frozen=True)
class MetricDefinition:
    name: str
    description: str
    sql: str
    unit: str
    source: str
    aliases: tuple[str, ...]


# Approved, read-only SELECT statements. All queries return ONE scalar value.
# Currency metrics represent merchandise only, excluding freight.
# Monthly growth means the most recent available month, not today's month.
METRICS = {
    "delivered_orders": MetricDefinition(
        "delivered_orders", "Distinct delivered orders",
        "SELECT COUNT(DISTINCT order_id) FROM analytics.fact_orders WHERE order_status = 'delivered'",
        "orders", "analytics.fact_orders",
        ("delivered orders", "orders delivered", "how many deliveries", "number of delivered orders"),
    ),
    "delivered_gmv": MetricDefinition(
        "delivered_gmv", "Merchandise GMV from delivered orders (freight excluded)",
        "SELECT COALESCE(SUM(merchandise_value_brl), 0) FROM analytics.fact_orders WHERE order_status = 'delivered'",
        "BRL", "analytics.fact_orders",
        ("delivered gmv", "gmv from delivered", "gmv of delivered", "delivered merchandise", "revenue from delivered orders"),
    ),
    "total_gmv": MetricDefinition(
        "total_gmv", "Merchandise GMV across all order statuses (freight excluded)",
        "SELECT COALESCE(SUM(merchandise_value_brl), 0) FROM analytics.fact_orders",
        "BRL", "analytics.fact_orders",
        ("total gmv", "overall gmv", "all orders gmv", "total merchandise value"),
    ),
    "delivered_aov": MetricDefinition(
        "delivered_aov", "Delivered merchandise GMV per distinct delivered order",
        """SELECT ROUND(SUM(merchandise_value_brl) / NULLIF(COUNT(DISTINCT order_id), 0), 2)
           FROM analytics.fact_orders WHERE order_status = 'delivered'""",
        "BRL/order", "analytics.fact_orders",
        ("average order value", "aov", "average delivered order value"),
    ),
    "distinct_customers": MetricDefinition(
        "distinct_customers", "Distinct customer identities in customer dimension",
        "SELECT COUNT(DISTINCT customer_unique_id) FROM analytics.dim_customers",
        "customers", "analytics.dim_customers",
        ("total customers", "how many customers", "unique customers", "distinct customers"),
    ),
    "repeat_customers": MetricDefinition(
        "repeat_customers", "Customers with at least two orders in purchase summary",
        "SELECT COUNT(*) FROM analytics.customer_purchase_summary WHERE total_orders >= 2",
        "customers", "analytics.customer_purchase_summary",
        ("repeat customers", "returning customers", "customers purchased more than once"),
    ),
    "latest_mom_growth": MetricDefinition(
        "latest_mom_growth", "Month-on-month GMV growth for latest available sales month",
        """SELECT mom_growth_pct FROM analytics.monthly_sales_growth
           WHERE mom_growth_pct IS NOT NULL ORDER BY sales_month DESC LIMIT 1""",
        "percent", "analytics.monthly_sales_growth",
        ("monthly growth", "month over month", "mom growth", "latest sales growth"),
    ),
    "latest_yoy_growth": MetricDefinition(
        "latest_yoy_growth", "Year-on-year GMV growth for latest available comparable month",
        """SELECT yoy_growth_pct FROM analytics.sales_yoy_growth
           WHERE yoy_growth_pct IS NOT NULL ORDER BY sales_month DESC LIMIT 1""",
        "percent", "analytics.sales_yoy_growth",
        ("year over year", "yoy growth", "annual sales growth"),
    ),
    "month_one_retention": MetricDefinition(
        "month_one_retention", "Cohort-size-weighted month-one retention across cohorts",
        """SELECT ROUND(100.0 * SUM(active_customers) / NULLIF(SUM(cohort_size), 0), 2)
           FROM analytics.customer_cohort_retention WHERE month_number = 1""",
        "percent", "analytics.customer_cohort_retention",
        ("month one retention", "month 1 retention", "first month retention", "cohort retention"),
    ),
    "late_delivery_rate": MetricDefinition(
        "late_delivery_rate", "Share of delivery-performance records flagged late",
        """SELECT ROUND(100.0 * SUM(is_late) / NULLIF(COUNT(*), 0), 2)
           FROM analytics.delivery_performance""",
        "percent", "analytics.delivery_performance",
        ("late delivery rate", "percent late", "late deliveries", "delivery delay rate"),
    ),
    "on_time_delivery_rate": MetricDefinition(
        "on_time_delivery_rate", "Share of delivery-performance records flagged on time",
        """SELECT ROUND(100.0 * SUM(is_on_time) / NULLIF(COUNT(*), 0), 2)
           FROM analytics.delivery_performance""",
        "percent", "analytics.delivery_performance",
        ("on time delivery rate", "on-time delivery", "on time percentage", "delivery punctuality"),
    ),
    "products_count": MetricDefinition(
        "products_count", "Products represented in the product performance model",
        "SELECT COUNT(DISTINCT product_id) FROM analytics.product_performance",
        "products", "analytics.product_performance",
        ("number of products", "how many products", "total products"),
    ),
    "sellers_count": MetricDefinition(
        "sellers_count", "Sellers represented in the seller performance model",
        "SELECT COUNT(DISTINCT seller_id) FROM analytics.seller_performance",
        "sellers", "analytics.seller_performance",
        ("number of sellers", "how many sellers", "total sellers"),
    ),
}


def get_metric(name: str) -> MetricDefinition:
    return METRICS[name]
