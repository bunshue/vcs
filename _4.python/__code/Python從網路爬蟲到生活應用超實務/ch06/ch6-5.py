import pandas as pd

df = pd.read_csv("2330_2019_9.csv")
data = pd.DataFrame()
data["Date"] = pd.to_datetime(df["Date"])
data["Adj Close"] = df["Adj Close"]
data["High"] = df["High"]
data["Low"] = df["Low"]
data = data.set_index("Date")

data.plot(kind="line")




