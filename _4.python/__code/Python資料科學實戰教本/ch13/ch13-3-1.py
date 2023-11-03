import pandas as pd

df = pd.read_csv("test.csv")
print(df)
df.to_html("ch13-3-1.html")