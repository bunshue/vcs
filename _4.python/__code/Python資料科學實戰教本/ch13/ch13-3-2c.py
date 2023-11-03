import pandas as pd

df = pd.read_csv("test2.csv")

df1 = df.drop_duplicates("B")
print(df1)
df1.to_html("ch13-3-2c-01.html") 
print("---------------------------")
df2 = df.drop_duplicates("B", keep="last")
print(df2)
df2.to_html("ch13-3-2c-02.html") 
print("---------------------------")
df3 = df.drop_duplicates("B", keep=False)
print(df3)
df3.to_html("ch13-3-2c-03.html") 