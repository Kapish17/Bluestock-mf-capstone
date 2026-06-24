# Data Dictionary

## 02_nav_history.csv

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Mutual fund code |
| date | Date | NAV date |
| nav | Float | Net asset value |

## 07_scheme_performance.csv

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Fund code |
| scheme_name | Text | Scheme name |
| return_1yr_pct | Float | 1-year return |
| return_3yr_pct | Float | 3-year return |
| return_5yr_pct | Float | 5-year return |
| expense_ratio_pct | Float | Expense ratio |

## 08_investor_transactions.csv

| Column | Data Type | Description |
|--------|-----------|-------------|
| investor_id | Integer | Investor ID |
| transaction_date | Date | Transaction date |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Investment amount |
| kyc_status | Text | KYC verification |