import pandas as pd

df = pd.read_csv("titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].mode())
print(s.mode())
