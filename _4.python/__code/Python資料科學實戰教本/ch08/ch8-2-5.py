import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")

df2 = df.set_index("city")
print(df2.head())
df2.head().to_html("ch8-2-5-01.html")
print("---------------------------")
df3 = df2.reset_index()
print(df3.head())
df3.head().to_html("ch8-2-5-02.html")