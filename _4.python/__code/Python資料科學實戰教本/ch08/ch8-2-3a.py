import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")

print(df.tail())
df.tail().to_html("ch8-2-3a-01.html")
print("---------------------------")
print(df.tail(3)) 
df.tail(3).to_html("ch8-2-3a-02.html")
