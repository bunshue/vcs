import pandas as pd

df = pd.read_csv("test.csv")
# 填補遺失資料
df1 = df.fillna(value=1)
print(df1)
df1.to_html("ch13-3-1c-01.html")
print("---------------------------")
df["B"] = df["B"].fillna(df["B"].mean())
print(df)
df.to_html("ch13-3-1c-02.html")
print("---------------------------")
df["C"] = df["C"].fillna(df["C"].median())
print(df)
df.to_html("ch13-3-1c-03.html")
