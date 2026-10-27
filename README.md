# CommerceIQ

## Enterprise AI Analytics & KPI Intelligence Platform


**End-to-End Data Analytics | Advanced SQL | Data Engineering | Business Intelligence | AI-Powered Analytics**

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![SQL](https://img.shields.io/badge/SQL-Advanced_Analytics-orange)
![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811)
![dbt](https://img.shields.io/badge/dbt-Transformation-FF694B)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![Docker](https://img.shields.io/badge/Docker-Planned-2496ED)
![Status](https://img.shields.io/badge/Status-In_Development-yellow)

---

## 1. Project Overview

CommerceIQ 360 is an enterprise analytics and AI-powered business intelligence platform designed to transform raw e-commerce data into actionable business insights.

The platform combines relational data modeling, advanced SQL, Python-based data processing, data quality validation, dimensional modeling, interactive dashboards, and planned AI-powered natural-language analytics.

The project demonstrates how modern organizations can build scalable, reliable, and business-focused analytics systems.

### Project Objectives

- Design a centralized analytical data warehouse.
- Process and validate real-world transactional datasets.
- Develop advanced SQL queries for business analytics.
- Build fact and dimension tables using dimensional modeling.
- Define and calculate standardized business KPIs.
- Analyze revenue, customers, products, sellers, and delivery performance.
- Implement automated data quality checks.
- Develop interactive Power BI dashboards.
- Integrate an AI-powered analytics assistant.
- Introduce production-oriented testing, CI/CD, and deployment practices.

**Project Status:** Active development — foundational database design, profiling scripts, SQL models, and KPI specifications have been prepared. Execution, validation, dashboard development, and deployment are ongoing.

---

## 2. Business Problem

E-commerce companies generate large amounts of transactional data across multiple operational systems.

These systems may include:

- Order management systems
- Customer databases
- Product catalogs
- Payment processing systems
- Seller management systems
- Shipping and delivery platforms
- Customer review systems

When business data is fragmented, organizations struggle to obtain consistent and reliable insights.

### Key Business Challenges

1. Inconsistent reporting across departments.
2. Limited visibility into sales and order performance.
3. Difficulty identifying high-value customers.
4. Lack of standardized KPI definitions.
5. Manual reporting and repetitive SQL analysis.
6. Challenges measuring seller and delivery performance.
7. Poor data quality and inconsistent relationships.
8. Limited access to self-service analytics.

### Proposed Solution

CommerceIQ 360 addresses these challenges through a centralized analytics platform that:

- Integrates transactional data into PostgreSQL.
- Standardizes data using structured transformation layers.
- Implements reusable business metrics.
- Supports analytical SQL queries.
- Provides interactive business dashboards.
- Introduces a governed AI analytics interface.

---

## 3. Dataset

**Primary Dataset:** Brazilian E-Commerce Public Dataset by Olist

**Source:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The dataset contains approximately 100,000 historical orders and related customer, product, payment, seller, delivery, and review information.

It provides a realistic relational dataset for implementing enterprise-style analytics.

### Dataset Tables

| Dataset | PostgreSQL Table | Description |
|---|---|---|
| olist_customers_dataset.csv | raw.customers | Customer identities and locations |
| olist_orders_dataset.csv | raw.orders | Order lifecycle and timestamps |
| olist_order_items_dataset.csv | raw.order_items | Products sold within orders |
| olist_products_dataset.csv | raw.products | Product attributes and categories |
| olist_sellers_dataset.csv | raw.sellers | Seller information |
| olist_order_payments_dataset.csv | raw.payments | Payment transactions |
| olist_order_reviews_dataset.csv | raw.reviews | Customer ratings and reviews |
| olist_geolocation_dataset.csv | raw.geolocation | Geographic coordinates |
| product_category_name_translation.csv | raw.category_translation | Portuguese-to-English category names |

### Data Considerations

The dataset represents historical Brazilian e-commerce activity.

All monetary values are interpreted in Brazilian real (BRL).

The dataset does not provide complete information for certain business metrics, including:

- Gross profit margin
- Customer acquisition cost
- Advertising return on spend
- Website conversion rate
- True accounting net revenue

These metrics will not be presented as verified business results without appropriate supporting data.

---

## 4. Technology Stack

| Category | Technology | Purpose |
|---|---|---|
| Programming | Python | Data processing and automation |
| Query Language | SQL | Data analysis and transformation |
| Database | PostgreSQL | Relational data warehouse |
| Database IDE | DBeaver | Database development |
| Data Processing | Pandas, NumPy | Data inspection and manipulation |
| Transformation | dbt (planned) | Tested analytical transformations |

| Visualization | Power BI Desktop | Six completed interactive dashboards |
| BI Calculations | DAX | KPI measures, percentages, time-based reporting |
| Data Modeling | Power BI Data Model | Relationships and shared Date dimension |

| Backend | FastAPI (planned) | Analytics APIs |
| AI Integration | LLM API (planned) | Natural-language analytics |
| Containerization | Docker (planned) | Reproducible environments |
| Version Control | Git and GitHub | Source management |
| Testing | Pytest, SQL checks | Automated validation |
| CI/CD | GitHub Actions (planned) | Testing and deployment automation |

---

## 5. System Architecture

The platform follows a layered analytical architecture.

```text
                  DATA SOURCES
                       |
       +---------------+---------------+
       |               |               |
     Orders         Customers        Products
       |               |               |
       +---------------+---------------+
                       |
                PYTHON INGESTION
                       |
                       v
               POSTGRESQL DATABASE
                       |
               +-------+-------+
               |               |
           RAW SCHEMA      DATA VALIDATION
               |
               v
          STAGING SCHEMA
               |
               v
       ANALYTICAL TRANSFORMATIONS
               |
               v
          ANALYTICS SCHEMA
               |
       +-------+--------+
       |                |
   FACT TABLES     DIMENSION TABLES
       |                |
       +-------+--------+
               |
          KPI / METRIC LAYER
               |
       +-------+--------+
       |                |
       v                v
   POWER BI        AI ANALYTICS
   DASHBOARDS       ASSISTANT
                        |
                 FASTAPI + LLM
                        |
                  STREAMLIT UI
```

### Architectural Layers

**Raw Layer**

Preserves source data and supports ingestion validation.

**Staging Layer**

Standardizes data types, naming conventions, missing values, and business rules.

**Analytics Layer**

Contains fact tables, dimension tables, and reusable analytical models.

**Presentation Layer**

Exposes governed business metrics through dashboards and AI-powered interfaces.

---

## 6. Project Directory Structure

```text
commerceiq-360/
|
|-- data/
|   |-- raw/
|   |-- processed/
|
|-- docs/
|   |-- diagrams/
|   |-- kpi_dictionary.md
|
|-- sql/
|   |-- schemas/
|   |   |-- 01_create_raw_tables.sql
|   |   |-- 02_create_remaining_raw_tables.sql
|   |
|   |-- analytics/
|       |-- 01_data_quality_checks.sql
|       |-- 02_create_dimensions.sql
|       |-- 03_create_facts.sql
|
|-- src/
|   |-- inspect_data.py
|   |-- profile_data.py
|
|-- tests/
|
|-- dashboards/
|
|-- .gitignore
|-- requirements.txt
|-- README.md
```

Additional folders will be introduced for dbt, backend services, AI functionality, and deployment.

---

## 7. Data Profiling and Quality Assessment

Data profiling is used to examine the completeness, uniqueness, validity, consistency, and relationships of source data.

### Profiling Workflow

1. Load source CSV files using Pandas.
2. Inspect dataset dimensions.
3. Identify column data types.
4. Calculate missing-value percentages.
5. Analyze unique values.
6. Check candidate primary keys.
7. Examine business timestamps.
8. Identify possible data quality issues.
9. Generate a profiling report.

### Python Example

```python
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"

for file in RAW_DIR.glob("*.csv"):
    df = pd.read_csv(file, low_memory=False)

    print(f"Dataset: {file.name}")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(df.isnull().sum())
```

The extended profiling script generates:

```text
data/processed/data_profile.csv
```

### Data Quality Dimensions

| Dimension | Validation |
|---|---|
| Completeness | Missing values and required fields |
| Uniqueness | Duplicate business identifiers |
| Validity | Invalid prices, dates, and ratings |
| Consistency | Chronological and business-rule checks |
| Referential Integrity | Missing parent records |
| Reconciliation | Source and analytical total comparisons |

---

## 8. PostgreSQL Database Design

The database is organized into three logical schemas.

```sql
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS analytics;
```

### Raw Tables

```text
raw.customers
raw.orders
raw.order_items
raw.products
raw.sellers
raw.payments
raw.reviews
raw.geolocation
raw.category_translation
```

### Example: Orders Table

```sql
CREATE TABLE IF NOT EXISTS raw.orders (
    order_id VARCHAR(32) PRIMARY KEY,
    customer_id VARCHAR(32),
    order_status TEXT,
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP
);
```

### Example: Order Items Table

```sql
CREATE TABLE IF NOT EXISTS raw.order_items (
    order_id VARCHAR(32) NOT NULL,
    order_item_id INTEGER NOT NULL,
    product_id VARCHAR(32),
    seller_id VARCHAR(32),
    shipping_limit_date TIMESTAMP,
    price NUMERIC(12,2),
    freight_value NUMERIC(12,2),
    PRIMARY KEY (order_id, order_item_id)
);
```

### Relational Modeling Concepts

The project applies:

- Primary keys
- Composite primary keys
- Foreign-key relationship analysis
- One-to-many relationships
- Data normalization
- Referential-integrity validation
- SQL indexing
- Query optimization principles

---

## 9. Dimensional Modeling — Star Schema

CommerceIQ 360 uses dimensional modeling to organize analytical data into fact and dimension tables.

### Dimension Tables

| Dimension | Grain | Description |
|---|---|---|
| dim_customer | One unique customer | Customer identity and representative location |
| dim_product | One product | Product details and category |
| dim_seller | One seller | Seller information |
| dim_date | One calendar day | Date attributes for reporting |

### Fact Tables

| Fact | Grain | Measures |
|---|---|---|
| fact_order_items | One order-item row | Merchandise value, freight, unit count |
| fact_orders | One order | Delivery timing, order status |
| fact_payments (planned) | One payment record | Payment amount |
| fact_reviews (planned) | One review record | Review score |

### Star Schema Overview

```text
               dim_customer
                     |
                     |
dim_product ---- fact_order_items ---- dim_seller
                     |
                     |
                  dim_date


Additional analytical facts:

fact_orders
fact_payments
fact_reviews
```

### Why a Star Schema?

- Simplifies analytical queries.
- Improves reporting consistency.
- Supports reusable business metrics.
- Separates descriptive attributes from measurable events.
- Reduces complexity in BI tools.
- Makes table grain explicit.

---

## 10. Business KPI Framework

The platform defines standardized business metrics across sales, customers, products, and operations.

### Sales KPIs

| KPI | Calculation |
|---|---|
| Delivered GMV | Sum of item prices for delivered orders |
| Total Orders | Count of distinct orders |
| Average Order Value | Delivered GMV / delivered orders |
| Monthly GMV Growth | Percentage change from previous month |
| Units Sold | Count of qualifying order-item records |

### Customer KPIs

| KPI | Calculation |
|---|---|
| Active Customers | Distinct purchasing customers |
| Repeat Purchase Rate | Customers with 2+ purchases / purchasing customers |
| Customer Retention | Returning customers / prior cohort customers |
| Customer Purchase Frequency | Orders / purchasing customers |
| Customer Value | Cumulative merchandise value per customer |

### Operational KPIs

| KPI | Calculation |
|---|---|
| On-Time Delivery Rate | On-time deliveries / eligible deliveries |
| Average Transit Time | Average elapsed time from carrier handoff to delivery |
| Average Review Score | Average valid customer rating |
| Seller GMV | Merchandise value by seller |
| Product Category GMV | Merchandise value by category |

### KPI Governance

Every metric should have:

- A business definition
- A mathematical formula
- Source tables
- Reporting grain
- Reporting date
- Filters and exclusions
- Null-handling rules
- Validation checks

---

## 11. Advanced SQL Analytics

The project develops practical SQL solutions for business reporting and analytical decision-making.

### 11.1 Monthly GMV and Growth

```sql
WITH monthly_sales AS (
    SELECT
        DATE_TRUNC('month', purchase_date)::date
            AS sales_month,
        SUM(merchandise_value) AS gmv
    FROM analytics.fact_order_items
    WHERE order_status = 'delivered'
    GROUP BY 1
),
growth AS (
    SELECT
        sales_month,
        gmv,
        LAG(gmv) OVER (
            ORDER BY sales_month
        ) AS previous_gmv
    FROM monthly_sales
)
SELECT
    sales_month,
    ROUND(gmv, 2) AS gmv,
    ROUND(
        100.0 * (gmv - previous_gmv)
        / NULLIF(previous_gmv, 0),
        2
    ) AS growth_percentage
FROM growth
ORDER BY sales_month;
```

**SQL Concepts:** CTEs, aggregations, window functions, LAG, date grouping.

### 11.2 Top Product Categories

```sql
SELECT
    p.category_english,
    ROUND(
        SUM(f.merchandise_value), 2
    ) AS total_gmv,
    SUM(f.unit_count) AS units_sold,
    COUNT(DISTINCT f.order_id) AS orders
FROM analytics.fact_order_items f
LEFT JOIN analytics.dim_product p
    ON f.product_id = p.product_id
WHERE f.order_status = 'delivered'
GROUP BY p.category_english
ORDER BY total_gmv DESC
LIMIT 10;
```

**SQL Concepts:** Joins, grouping, sorting, aggregation.

### 11.3 Repeat Purchase Rate

```sql
WITH customer_orders AS (
    SELECT
        customer_unique_id,
        COUNT(DISTINCT order_id) AS orders
    FROM analytics.fact_orders
    WHERE order_status = 'delivered'
      AND customer_unique_id IS NOT NULL
    GROUP BY customer_unique_id
)
SELECT
    COUNT(*) AS purchasing_customers,
    COUNT(*) FILTER (
        WHERE orders >= 2
    ) AS repeat_customers,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE orders >= 2
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS repeat_purchase_rate
FROM customer_orders;
```

**SQL Concepts:** CTEs, conditional aggregation, DISTINCT counts.

### 11.4 On-Time Delivery Performance

```sql
SELECT
    COUNT(*) FILTER (
        WHERE is_on_time IS NOT NULL
    ) AS eligible_deliveries,
    COUNT(*) FILTER (
        WHERE is_on_time = TRUE
    ) AS on_time_deliveries,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE is_on_time = TRUE
        ) / NULLIF(
            COUNT(*) FILTER (
                WHERE is_on_time IS NOT NULL
            ), 0
        ),
        2
    ) AS on_time_rate
FROM analytics.fact_orders
WHERE order_status = 'delivered';
```

**SQL Concepts:** Conditional aggregation, boolean metrics, null handling.

---

## 12. Data Quality and Reconciliation

Data quality validation is a key part of the platform.

### Example: Referential Integrity

```sql
SELECT
    COUNT(*) AS orphan_order_items
FROM raw.order_items i
LEFT JOIN raw.orders o
    ON i.order_id = o.order_id
WHERE o.order_id IS NULL;
```

### Example: Invalid Monetary Values

```sql
SELECT *
FROM raw.order_items
WHERE price IS NULL
   OR price < 0
   OR freight_value IS NULL
   OR freight_value < 0;
```

### Example: Source-to-Analytics Reconciliation

```sql
WITH raw_gmv AS (
    SELECT SUM(i.price) AS amount
    FROM raw.order_items i
    JOIN raw.orders o USING (order_id)
    WHERE o.order_status = 'delivered'
),
analytics_gmv AS (
    SELECT SUM(merchandise_value) AS amount
    FROM analytics.fact_order_items
    WHERE order_status = 'delivered'
)
SELECT
    r.amount AS raw_gmv,
    a.amount AS analytics_gmv,
    r.amount - a.amount AS difference
FROM raw_gmv r
CROSS JOIN analytics_gmv a;
```

### Validation Goals

- Source and fact-table row counts reconcile.
- Primary-key constraints are satisfied.
- Invalid monetary values are investigated.
- Unmatched references are identified.
- KPI calculations reconcile between raw and analytical layers.
- Missing values are handled explicitly.

Validation results will be documented after execution.

---

## 13. Planned Power BI Dashboard

The Power BI reporting layer will contain multiple business-focused dashboards.

### Executive Dashboard

- Delivered GMV
- Total orders
- Average order value
- Monthly growth
- Active customers
- Sales trends

### Sales Performance Dashboard

- Monthly and quarterly GMV
- Product category performance
- Seller performance
- Geographic sales distribution
- Order-status breakdown

### Customer Analytics Dashboard

- Repeat purchase rate
- Customer segmentation
- Purchase frequency
- RFM analysis
- Cohort retention

### Operations Dashboard

- On-time delivery rate
- Average transit time
- Delivery performance by geography
- Seller fulfillment performance
- Customer review scores

---

## 14. Planned AI Analytics Assistant

The AI component will allow business users to ask questions in natural language.

### Example Questions

- What was the delivered GMV last month?
- Which product categories performed best?
- Why did GMV decrease compared with the previous month?
- Which customers have the highest purchase frequency?
- Which sellers have the weakest delivery performance?

### Proposed Workflow

```text
Business User
     |
     v
Natural Language Question
     |
     v
AI Analytics Assistant
     |
     v
Metric and Schema Retrieval
     |
     v
Controlled SQL Generation
     |
     v
SQL Validation and Authorization
     |
     v
Read-Only PostgreSQL Execution
     |
     v
Result Verification
     |
     v
Business Explanation
```

### AI Reliability Requirements

- Read-only database access
- Approved schemas and metrics
- SQL validation
- Query execution limits
- Protection against unsafe queries
- Transparent metric definitions
- Error handling and logging
- Clear distinction between facts and inferred explanations

This component is planned and has not yet been implemented.

---

## 15. Local Setup

### Prerequisites

- Python 3.11 or newer
- PostgreSQL
- DBeaver
- Git
- Visual Studio Code

### Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd commerceiq-360
```

Replace the placeholder with your actual GitHub repository URL.

### Create a Virtual Environment

Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download the Dataset

Download the Olist dataset from Kaggle:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Extract the CSV files into:

```text
data/raw/
```

### Create PostgreSQL Database

```sql
CREATE DATABASE commerceiq360;
```

Connect to the database and execute:

```sql
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS analytics;
```

### Create and Load Raw Tables

Run the SQL files in order:

```text
sql/schemas/01_create_raw_tables.sql
sql/schemas/02_create_remaining_raw_tables.sql
```

Import the corresponding CSV files into PostgreSQL using DBeaver.

### Run Data Profiling

```bash
python src/inspect_data.py
python src/profile_data.py
```

### Build Analytics Models

After loading and validating source data, execute:

```text
sql/analytics/02_create_dimensions.sql
sql/analytics/03_create_facts.sql
```

### Validate the Warehouse

Execute:

```text
sql/analytics/01_data_quality_checks.sql
```

Review the output and investigate any failed checks before relying on analytical results.

---

## 16. Development Roadmap

| Stage | Deliverables | Status |
|---|---|---|
| Stage 1 | Business case, PostgreSQL schemas, data profiling | Implemented |
| Stage 2 | Advanced SQL, RFM, cohort analysis | Implemented |
| Stage 3 | Python ETL/ELT and dbt transformations | Partially implemented / planned |
| Stage 4 | Six Power BI dashboards and DAX KPIs | Completed |
| Stage 5 | AI-powered KPI Intelligence Assistant | Next phase |
| Stage 6 | Backend APIs and application integration | Planned |
| Stage 7 | Automated testing, Docker, CI/CD | Planned |
| Stage 8 | Deployment, documentation, portfolio demo | In progress |


## 17. Skills Demonstrated

This project is designed to demonstrate practical skills relevant to:

**Data Analyst**
- Advanced SQL
- KPI development
- Data profiling
- Business reporting
- Customer and sales analytics

**Analytics Engineer**
- Dimensional modeling
- Fact and dimension tables
- Data transformation
- Metric standardization
- Data quality and reconciliation

**Data Engineer**
- Python data processing
- PostgreSQL database design
- ETL/ELT architecture
- Data validation
- Pipeline automation

**AI / Analytics Engineer**
- LLM-based analytics
- Natural-language interfaces
- Governed SQL execution
- API integration
- AI reliability and testing

---

## 18. Key Engineering Principles

CommerceIQ 360 follows several important engineering practices:

1. **Data accuracy before visualization:** Business metrics must be validated before they are presented in dashboards.
2. **Explicit grain:** Every analytical table must have a clearly defined row-level meaning.
3. **No fan-out errors:** Measures from different relational grains must not be combined through unsafe joins.
4. **Reusable business logic:** KPI definitions should be standardized across reports.
5. **Source preservation:** Raw data should remain available for reconciliation.
6. **Reproducibility:** Data models and validation checks should be version-controlled.
7. **Transparent limitations:** Unsupported KPIs must not be presented as real results.
8. **Safe AI integration:** AI-generated analytics must operate through authorized and validated database access.

---

## 19. Future Enhancements

Planned improvements include:

- Automated ingestion and incremental data loading
- dbt-based transformation pipelines
- Data quality dashboards
- Customer RFM segmentation
- Cohort retention analysis
- Advanced SQL performance tuning
- AI-generated business summaries
- Natural-language analytics
- Automated anomaly detection
- Containerized application deployment
- CI/CD pipelines
- Query monitoring and observability

---

## 20. Project Purpose

CommerceIQ 360 is a portfolio-driven, enterprise-style analytics engineering project.

Its purpose is to demonstrate the ability to design and develop an analytical solution from raw data through business reporting and AI-assisted decision support.

The project emphasizes:

**Business Understanding → Data Engineering → Advanced SQL → Data Modeling → KPI Governance → Business Intelligence → AI Analytics → Production Engineering**

---

## License and Data Attribution

The transactional dataset is provided by Olist through Kaggle.

Dataset source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Review the dataset's licensing terms before redistributing source files.

This project is an independent educational and portfolio implementation and is not affiliated with Olist.

---

**CommerceIQ 360 — Transforming E-Commerce Data into Reliable Business Intelligence.**

## 📊 Power BI — Business Intelligence Dashboards

Developed four interactive Power BI dashboards for **CommerceIQ 360**, transforming PostgreSQL analytical data into actionable business insights using Power BI, DAX measures, and interactive visualizations.

### 1. Executive Sales Overview

Designed an executive-level dashboard to monitor overall sales performance, revenue growth, and key business metrics.

**Key Features:**
- Delivered Gross Merchandise Value (GMV)
- Total Delivered Orders
- Average Order Value (AOV)
- Latest Month-over-Month (MoM) Growth
- Monthly GMV vs. Three-Month Rolling Average
- Monthly GMV Growth (%) Analysis
- Detailed Monthly Sales Performance Table

**Dashboard Preview:**

![Executive Sales Overview](https://github.com/user-attachments/assets/8944bfed-7d21-49bd-ab7c-81b42b61cf38)

---

### 2. Customer Intelligence Dashboard

Developed a comprehensive customer analytics dashboard to understand purchasing behavior, customer segmentation, spending patterns, and customer retention.

**Key Features:**
- Total Customers
- Average Customer Spend
- Customer Cohort Retention Rate
- Repeat Purchase Rate
- Average Order Value (AOV)
- Customer RFM Segmentation
- Average Customer Spend by Segment
- Customer Purchase Frequency Analysis
- Customer Distribution by State
- Monthly Customer Cohort Retention Heatmap

**Dashboard Preview:**

![Customer Intelligence Dashboard](https://github.com/user-attachments/assets/41e8f794-4441-4708-b40d-aee82ce12787)

---

### 3. Sales & Revenue Analytics Dashboard

Built an interactive sales analytics dashboard to evaluate revenue trends, order performance, product contributions, and seller-level sales performance.

**Key Features:**
- Total Gross Merchandise Value (GMV)
- Total Orders
- Average Order Value (AOV)
- Latest Month-over-Month Growth
- Total Items Sold
- Average Items per Order
- Monthly GMV Trend Analysis
- Monthly GMV vs. Total Orders Comparison
- Revenue Contribution by Product
- Revenue Contribution by Seller
- Monthly Revenue Growth (%)
- Interactive Year and Order Status Filters

**Dashboard Preview:**

![Sales and Revenue Analytics Dashboard](https://github.com/user-attachments/assets/947f5d0e-27e1-45e7-abdc-937b66e06b60)

---

### 4. Product & Seller Performance Dashboard

Developed a product and seller analytics dashboard to evaluate product-level sales, seller contributions, and overall marketplace performance.

**Key Features:**
- Product-Level Revenue Analysis
- Seller-Level Revenue Contribution
- Top-Performing Products
- Top-Performing Sellers
- Product Sales Distribution
- Seller Performance Comparison
- GMV Contribution Analysis
- Product and Seller Ranking Analysis

**Dashboard Preview:**

![Product and Seller Performance Dashboard](https://github.com/user-attachments/assets/02db9789-6a49-429c-bb36-432088d5bf8d")

---

### 🛠️ Technologies Used

- **Power BI Desktop** — Interactive dashboards and business reporting
- **DAX** — Business KPI calculations and dynamic measures
- **Power Query** — Data preparation and transformation
- **PostgreSQL** — Analytical data source
- **SQL** — Data modeling, aggregation, and analytical queries
- **Data Visualization** — KPI cards, line charts, bar charts, tables, and cohort retention heatmaps


### ✅ Power BI Development Status

| Dashboard | Status |
|-----------|--------|
| Executive Sales Overview | ✅ Completed |
| Customer Intelligence | ✅ Completed |
| Sales & Revenue Analytics | ✅ Completed |
| Product & Seller Performance | ✅ Completed |
