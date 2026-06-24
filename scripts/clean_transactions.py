import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Date conversion
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.upper()
)

mapping = {
    "SIP": "SIP",
    "LUMPSUM": "Lumpsum",
    "REDEMPTION": "Redemption"
}

df["transaction_type"] = (
    df["transaction_type"]
    .replace(mapping)
)

# Amount validation
df = df[df["amount_inr"] > 0]

# KYC values
valid_kyc = ["YES", "NO", "PENDING"]

df["kyc_status"] = (
    df["kyc_status"]
    .str.upper()
)

invalid = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print("Invalid KYC rows:", len(invalid))

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned.")