import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': [2,4,4,6] } 
df = pd.DataFrame(data) 
s = pd.Series({'種類':"Bicycle",'數量':5,'輪數':2}) 
df2 = df.append(s, ignore_index=True)
print(df2.tail())

df["載客數"] = [1, 20, 4, 2]
print(df)