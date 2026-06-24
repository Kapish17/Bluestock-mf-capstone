import pandas as pd

nav = pd.read_csv("data/raw/02_nav_history.csv")
print("\nNAV HISTORY")
print(nav.columns)

perf = pd.read_csv("data/raw/07_scheme_performance.csv")
print("\nSCHEME PERFORMANCE")
print(perf.columns)

trans = pd.read_csv("data/raw/08_investor_transactions.csv")
print("\nINVESTOR TRANSACTIONS")
print(trans.columns)