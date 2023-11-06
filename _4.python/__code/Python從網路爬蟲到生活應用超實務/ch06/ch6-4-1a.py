import pandas as pd

df = pd.read_csv("titanic_test.csv")
print(df["Age"].isnull().sum())
df2 = df.dropna(subset=["Age"])
print(len(df2))

