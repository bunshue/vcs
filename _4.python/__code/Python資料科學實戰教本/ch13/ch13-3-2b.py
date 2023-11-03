import pandas as pd

df = pd.read_csv("test2.csv")

df1 = df.drop_duplicates()
print(df1)
df1.to_html("ch13-3-2b.html") 
