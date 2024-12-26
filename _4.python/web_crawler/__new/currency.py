import requests

API_KEY = "fca_live_QiRD4yaE7K1aJQIAfVLojfu8J2KPxSXPYkDxxTzc"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]


def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid currency.")
        return None


print("轉換匯率")

base = "USD"

data = convert_currency(base)

del data[base]
for ticker, value in data.items():
    print(f"{ticker}: {value}")
