import pandas as pd

fruits = ["蘋果", "橘子", "梨子", "櫻桃"]
quantities = [15, 33, 45, 55]
s = pd.Series(quantities, index=fruits) 
print(s)
print("---------------------------")
print(s.index)
print("---------------------------")
print(s.values)  