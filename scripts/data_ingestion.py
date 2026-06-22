import pandas as pd
import os

folder = "../data/raw"

files = [f for f in os.listdir(folder) if f.endswith(".csv")]

for file in files:
    print("\n" + "="*50)
    print("FILE:", file)

    path = os.path.join(folder, file)

    df = pd.read_csv(path)

    print("Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())