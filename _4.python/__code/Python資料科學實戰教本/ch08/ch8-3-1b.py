import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.loc[ordinals[1]])
print(type(df.loc[ordinals[1]]))
print("---------------------------")
print(df.loc[:,["name","population"]].head(3))
df.loc[:,["name","population"]].head(3).to_html("ch8-3-1b-01.html")
print("---------------------------")
print(df.loc["third":"fifth", ["name","population"]])
print("---------------------------")
print(df.loc["third", ["name","population"]])
df.loc["third":"fifth", ["name","population"]].to_html("ch8-3-1b-02.html")
print("---------------------------")
# 取得單一純量值
print(df.loc[ordinals[0], "name"])
print(type(df.loc[ordinals[0],"name"]))
print("---------------------------")
print(df.loc["first", "population"])
print(type(df.loc["first", "population"]))
