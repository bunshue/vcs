import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': ["2","4","4","6"] } 
df = pd.DataFrame(data, index=["A","B","C","D"]) 
print(df.loc["A", "數量"])
print(df.loc[["C","D"], ["數量","輪數"]])

print(df.loc[:, ["數量","輪數"]])
print(df.loc["B":"C", "種類":"數量"])

print(df.iloc[3])
print(df.iloc[2:4, 1:3])
