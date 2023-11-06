import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': ["2","4","4","6"] } 
df = pd.DataFrame(data, index=["A","B","C","D"]) 
df.to_csv("vehicles.csv",index=False,encoding="big5")

df.to_json("vehicles.json")