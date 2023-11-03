import pandas as pd

df = pd.read_csv("test.csv")
# 刪除所有 NaN 的記錄
df1 = df.dropna()
print(df1)
df1.to_html("ch13-3-1b-01.html")
print("---------------------------")
df2 = df.dropna(how="any")
print(df2)
df2.to_html("ch13-3-1b-02.html")
print("---------------------------")
df3 = df.dropna(how="all")
print(df3)
df3.to_html("ch13-3-1b-03.html")
print("---------------------------")
df4 = df.dropna(subset=["B", "C"])
print(df4)
df4.to_html("ch13-3-1b-04.html")