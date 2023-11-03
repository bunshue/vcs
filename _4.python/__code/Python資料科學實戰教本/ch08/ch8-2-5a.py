import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")

df2 = df.set_index(["city", "name"])
df2.sort_index(ascending=False, inplace=True)
print(df2)
df2.to_html("ch8-2-5a.html")