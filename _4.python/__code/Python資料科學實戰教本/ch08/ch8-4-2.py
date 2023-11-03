import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head(3))
print("---------------------------")
# 刪除純量值
print(df.loc[ordinals[0], "population"])
df.loc[ordinals[0], "population"] = None
print(df.iloc[1,1])
df.iloc[1,1] = None
print(df.head(3))
df.head(3).to_html("ch8-4-2.html")