import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")

df.columns = ["區", "人口", "直轄市"]
print(df.index)
print("---------------------------")
print(df.columns)
print("---------------------------")
print(df.values)