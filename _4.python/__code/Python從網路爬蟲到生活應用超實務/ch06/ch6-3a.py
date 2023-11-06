import pandas as pd

df = pd.read_csv("2330.TW.csv")
print(df["Volume"].pct_change())
