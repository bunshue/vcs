import pandas as pd

df1 = pd.read_csv("vehicles.csv", encoding="big5")
df2 = pd.read_json("vehicles.json")
print(df1)
print(df2)
