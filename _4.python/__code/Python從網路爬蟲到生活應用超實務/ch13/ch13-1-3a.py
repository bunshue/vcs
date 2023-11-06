import pandas as pd

csvfile = "USxrt.csv"
df = pd.read_csv(csvfile)
df.drop_duplicates(keep=False, inplace=True)
df.to_csv('USxrt2.csv',index=False,encoding="utf8")
print(df.head(5))
