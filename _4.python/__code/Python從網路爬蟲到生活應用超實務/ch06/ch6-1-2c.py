import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': [2,4,4,6] } 
df = pd.DataFrame(data) 
labels = ["A","B","E","D"]
df.columns = ["Types", "Count", "Wheels"]
labels[2] = "C"
df.index = labels
print(df)