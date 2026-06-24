import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "expense_ratio_pct"
]

for col in columns:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Expense ratio validation
anomalies = df[
    ~df["expense_ratio_pct"]
    .between(0.1, 2.5)
]

print("Expense anomalies:")
print(anomalies)

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned.")