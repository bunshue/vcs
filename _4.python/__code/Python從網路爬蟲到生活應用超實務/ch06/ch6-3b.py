import pandas as pd

df = pd.read_csv("2330.TW.csv")
print(df["Close"].unique())
print(df["Close"].nunique())
print(df["Close"].value_counts())