import pandas as pd
data = pd.read_csv("out.csv",encoding="utf-8-sig",index_col=0)

print(data)