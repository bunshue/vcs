import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")

df.columns = ["區", "人口", "直轄市"]
print(df.head(4)) 
df.head(4).to_html("ch8-2-3b.html")