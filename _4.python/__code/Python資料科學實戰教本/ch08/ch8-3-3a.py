import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head())
df.head().to_html("ch8-3-3a-01.html")
print("---------------------------")
df2 = df.sort_values("population", ascending=False)
print(df2.head())
df2.head().to_html("ch8-3-3a-02.html")
print("---------------------------")
df.sort_values(["city","population"], inplace=True)
print(df.head())
df.head().to_html("ch8-3-3a-03.html")