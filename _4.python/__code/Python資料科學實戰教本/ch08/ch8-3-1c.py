import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.iloc[3])          # 第 4 筆
print("---------------------------")
print(df.iloc[3:5, 1:3])   # 切割
df.iloc[3:5, 1:3].to_html("ch8-3-1c-01.html")
print("---------------------------")
print(df.iloc[1:3, :])     # 切割列
df.iloc[1:3, :].to_html("ch8-3-1c-02.html")
print("---------------------------")
print(df.iloc[:, 1:3])     # 切割欄
df.iloc[:, 1:3].to_html("ch8-3-1c-03.html")
print("---------------------------")
print(df.iloc[[1,2,4], [0,2]])   # 索引清單
df.iloc[[1,2,4], [0,2]].to_html("ch8-3-1c-04.html")
print("---------------------------")
# 取得單一純量值
print(df.iloc[1,1])
print(df.iat[1,1])
