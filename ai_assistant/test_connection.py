
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

try:
    with psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        connect_timeout=5,
    ) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT current_database(), current_user")
            print("Connected:", cur.fetchone())

            cur.execute("""
                SELECT COUNT(DISTINCT order_id)
                FROM analytics.fact_orders
                WHERE order_status = 'delivered'
            """)

            print("Delivered orders:", cur.fetchone()[0])

except psycopg.Error as error:
    print("Database error:", error)
