import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head(2))
print("---------------------------")
# 取得與更新單一純量值
print(df.loc[ordinals[0], "population"])
df.loc[ordinals[0], "population"] = 160000
print(df.iloc[1,1])
df.iloc[1,1] = 560000
print(df.head(2))
df.head(2).to_html("ch8-4-1.html")