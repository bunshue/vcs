import pandas as pd

df = pd.read_csv("test2.csv")
print(df)
df.to_html("ch13-3-2.html")
