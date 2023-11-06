import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': ["2","4","4","6"] } 
df = pd.DataFrame(data, index=["A","B","C","D"]) 
print(df["種類"])

print(df[["數量", "輪數"]].head(3))