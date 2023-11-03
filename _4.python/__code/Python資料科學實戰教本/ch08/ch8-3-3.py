import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

df2 = df.set_index("population")
print(df2.head())
df2.head().to_html("ch8-3-3-01.html")
print("---------------------------")
df2.sort_index(ascending=False, inplace=True)
print(df2.head())
df2.head().to_html("ch8-3-3-02.html")