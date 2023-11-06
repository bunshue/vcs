import pandas as pd

dates_d = pd.date_range("20170109", periods=5, freq="D")
print(dates_d)
df = pd.read_csv("2330.TW.csv")
df["Date"] = dates_d
print(df)
