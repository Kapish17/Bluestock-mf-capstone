import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("../bluestock_mf.db")

# Read required columns
query = """
SELECT
    scheme_name,
    fund_house,
    sharpe_ratio,
    risk_grade
FROM fact_performance
"""

performance = pd.read_sql(query, conn)

# User input
risk = input("Enter Risk Appetite (Low/Moderate/High): ").strip()

# Filter funds
result = performance[
    performance["risk_grade"].str.lower() == risk.lower()
]

# Sort by Sharpe Ratio
result = result.sort_values(
    "sharpe_ratio",
    ascending=False
)

# Show Top 3
print("\nTop 3 Recommended Funds:\n")
print(
    result[
        ["scheme_name", "fund_house", "sharpe_ratio"]
    ].head(3)
)

conn.close()