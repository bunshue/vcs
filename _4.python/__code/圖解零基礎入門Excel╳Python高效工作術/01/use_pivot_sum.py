import pandas as pd

df = pd.read_csv("data\ordersList.csv",encoding="utf-8",header = 0)

print(df.pivot_table(index="品名",columns="客戶名稱", values="金額", fill_value=0, margins=True, aggfunc="sum"))

print(df.pivot_table(index="品名",columns="客戶名稱", values="金額", fill_value=0, margins=True ))

