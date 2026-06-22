import requests
import pandas as pd

schemes = {
    "HDFC":125497,
    "SBI":119551,
    "ICICI":120503,
    "Nippon":118632,
    "Axis":119092,
    "Kotak":120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    df.to_csv(
        f"../data/raw/{name}.csv",
        index=False
    )

    print(name, "saved")