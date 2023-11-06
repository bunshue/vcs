import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': [2,4,4,6] } 
df = pd.DataFrame(data) 
df.set_index("種類", inplace=True)
print(df)
df.reset_index(inplace=True)
print(df)