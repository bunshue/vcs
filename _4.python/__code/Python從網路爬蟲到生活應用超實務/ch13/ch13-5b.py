import pandas as pd

df = pd.read_csv("monthlysales.csv", index_col=0)
df.index = pd.to_datetime(df.index)
tsmc = df["2330"]
print(tsmc/tsmc.shift()-1)
(tsmc/tsmc.shift()-1).plot(kind="line", title="台積電營收成長率")