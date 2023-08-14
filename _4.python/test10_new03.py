import pandas as pd

fruits = {"蘋果": [4, 3, 1, 0],
          "香蕉": [0, 4, 6, 2],
          "橘子": [1, 5, 2, 4]}
df = pd.DataFrame(fruits)

print(df)

print(df.head(3))   #前3項

print(df.tail(2))   #後2項

'''
df.to_csv("fruits.csv",index=False,encoding="utf8")
df.to_json("fruits.json")

df2 = pd.read_csv("fruits.csv", encoding="utf8")
df2 = pd.read_json("fruits.json")
print(df2)

for index, row in df.iterrows() :
    print(index, row["蘋果"], row["香蕉"],
          row["橘子"])

'''

sales = [11.22,23.50,12.99,15.95,25.75,11.55]
df = pd.DataFrame(sales)
print(df.describe())

print(df.count())
print(df.median())
print(df.mean())
print(df.min())
print(df.max())
print(df.std())

#--------------------------------------



