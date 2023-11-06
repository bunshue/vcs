import pandas as pd

df = pd.read_csv("drinks.csv")
print(df)
df.set_index("Type", inplace=True)
df.plot(kind="bar")

df.plot(kind="barh")

