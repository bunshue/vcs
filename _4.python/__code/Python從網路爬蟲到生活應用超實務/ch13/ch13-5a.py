import pandas as pd

df = pd.read_csv("monthlysales.csv", index_col=0)
df.index = pd.to_datetime(df.index)
print(df["2330"])
df["2330"].plot(kind="line", title="台積電月營收")
