import pandas as pd

df = pd.read_csv("titanic_test.csv")
df["Age"] = df["Age"].fillna(value=20)
print(df["Age"].isnull().sum())


