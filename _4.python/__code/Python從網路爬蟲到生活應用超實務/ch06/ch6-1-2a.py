import pandas as pd

s1 = pd.Series(["Bike","Bus","Car","Truck"])
s2 = pd.Series([3,4,6,2])
s3 = pd.Series([2,4,4,6])
data = {'種類': s1, '數量': s2, '輪數': s3 } 
df = pd.DataFrame(data) 
print(df)