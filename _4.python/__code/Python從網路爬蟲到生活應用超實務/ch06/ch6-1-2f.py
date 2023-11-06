import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': [2,4,4,6] } 
df = pd.DataFrame(data) 
df.set_index("種類", inplace=True)
print(df)
df2 = df.drop(["Bus", "Truck"])
print(df2)
df3 = df.drop(df.index[[0, 2]])
print(df3)
df4 = df.drop(["輪數"], axis=1)
print(df4)
