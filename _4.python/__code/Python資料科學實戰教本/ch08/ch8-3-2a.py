import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df[(df.population > 350000) & (df.population < 500000)])
df[(df.population > 350000) & (df.population < 500000)].to_html("ch8-3-2a-01.html")
print("---------------------------")
print(df[df["city"].str.startswith("台")])
df[df["city"].str.startswith("台")].to_html("ch8-3-2a-02.html")
