
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]

file_path = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "olist_orders_dataset.csv"
)

if not file_path.exists():
    raise FileNotFoundError(
        f"Dataset not found: {file_path}"
    )

df = pd.read_csv(file_path)

print("=== DATASET OVERVIEW ===")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\n=== COLUMN NAMES ===")
print(df.columns.tolist())

print("\n=== FIRST FIVE ROWS ===")
print(df.head())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== DUPLICATE ORDER IDS ===")
print(df["order_id"].duplicated().sum())

print("\n=== ORDER STATUS COUNTS ===")
print(df["order_status"].value_counts(dropna=False))
