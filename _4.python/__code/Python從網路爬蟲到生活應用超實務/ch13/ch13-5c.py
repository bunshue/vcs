import pandas as pd

df = pd.read_csv("monthlysales.csv", index_col=0)
df.index = pd.to_datetime(df.index)

df1 = df.iloc[-3:].mean() > df.iloc[-12:].mean()
print(df1[df1 == True].index)
print("------------------------------")
df2 = df.rolling(window=3, min_periods=2).mean()
df2 = (df2 > df2.shift()).iloc[-6:].sum()
print(df2[df2 == 6].head())
print("------------------------------")
df3 = df.iloc[-1] == df.iloc[-12:].max()
print(df3[df3 == True].index)
print("------------------------------")