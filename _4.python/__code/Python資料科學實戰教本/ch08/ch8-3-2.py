import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df[df.population > 350000])
df[df.population > 350000].to_html("ch8-3-2-01.html")
print("---------------------------")
print(df[df["city"].isin(["台北市","高雄市"])])
df[df["city"].isin(["台北市","高雄市"])].to_html("ch8-3-2-02.html")
