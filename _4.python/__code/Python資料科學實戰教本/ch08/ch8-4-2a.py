import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head())
print("---------------------------")
# 刪除記錄
df2 = df.drop(["second", "fourth"])    # 2,4 筆
print(df2.head())
df2.head().to_html("ch8-4-2a-01.html")
print("---------------------------")
df.drop(df.index[[2,3]], inplace=True) # 3,4 筆
print(df.head())
df.head().to_html("ch8-4-2a-02.html")