import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head(3))
print("---------------------------")
# 刪除欄位
df2 = df.drop(["population"], axis=1)
print(df2.head(3))
df2.head(3).to_html("ch8-4-2b.html")