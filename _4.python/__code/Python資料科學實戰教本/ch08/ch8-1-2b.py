import pandas as pd

fruits = ["蘋果", "橘子", "梨子", "櫻桃"]
quantities = [15, 33, 45, 55]
s = pd.Series(quantities, index=fruits) 
p = pd.Series([11, 16, 21, 32], index=fruits) 
print(s + p)
print("---------------------------")
print("總計=", sum(s + p))
 