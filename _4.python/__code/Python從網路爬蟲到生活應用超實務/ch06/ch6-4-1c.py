import pandas as pd

df = pd.read_csv("titanic_test.csv")
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df["Age"].isnull().sum())


