import pandas as pd
data = pd.read_excel("out.xlsx",encoding="utf-8-sig",index_col=0)

print(data)