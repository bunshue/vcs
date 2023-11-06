import pandas as pd

df = pd.read_csv("sales.csv")
df1 = df.drop_duplicates("Country")
print(df1)



