import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df[0:3])                # 不含 3
df[0:3].to_html("ch8-3-1a-01.html")
print("---------------------------")
print(df["sixth":"eleventh"]) # 含 "eleventh"
df["sixth":"eleventh"].to_html("ch8-3-1a-02.html")