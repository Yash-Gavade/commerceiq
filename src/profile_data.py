
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
OUTPUT_DIR = ROOT / "data" / "processed"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

reports = []

for file in sorted(RAW_DIR.glob("*.csv")):
    df = pd.read_csv(file, low_memory=False)

    for column in df.columns:
        reports.append({
            "file": file.name,
            "column": column,
            "data_type": str(df[column].dtype),
            "row_count": len(df),
            "null_count": int(df[column].isna().sum()),
            "null_percentage": round(
                df[column].isna().mean() * 100, 2
            ),
            "unique_values": int(df[column].nunique()),
            "duplicate_values": int(
                len(df) - df[column].nunique(dropna=False)
            )
        })

report = pd.DataFrame(reports)

output = OUTPUT_DIR / "data_profile.csv"
report.to_csv(output, index=False)

print(report.to_string(index=False))
print(f"\nSaved profile to: {output}")
