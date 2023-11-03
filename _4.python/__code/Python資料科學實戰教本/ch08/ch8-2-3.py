import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")

print(df.head())
df.head().to_html("ch8-2-3-01.html")
print("---------------------------")
print(df.head(3))
df.head(3).to_html("ch8-2-3-02.html")