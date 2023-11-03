import pandas as pd

df = pd.read_csv("test.csv")
# 建立布林遮罩
df1 = pd.isnull(df)
print(df1)
df1.to_html("ch13-3-1d.html")