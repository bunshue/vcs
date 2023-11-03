import pandas as pd
import numpy as np

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df)
print("---------------------------")
# 取得與更新整個欄位
print(df.loc[:, "population"])
print("---------------------------")
df.loc[:, "population"] = np.random.randint(34000, 700000, size=len(df))
print(df.head())
df.head().to_html("ch8-4-1b.html")
