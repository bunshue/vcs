import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.tail(3))
print("---------------------------")
# 新增記錄
df.loc["third-1"] = ["士林區", 288340, "台北市"]
print(df.tail(3))
df.tail(3).to_html("ch8-4-3-01.html")
print("---------------------------")
s = pd.Series({"city":"新北市","name":"中和區","population":413291})
df2 = df.append(s, ignore_index=True)
print(df2.tail(3))
df2.tail(3).to_html("ch8-4-3-02.html")