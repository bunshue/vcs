import pandas as pd

df = pd.read_csv("batchSales.csv")
print(df)
df2 = df.groupby("BatchNo").mean()
print(df2)