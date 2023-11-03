import numpy as np
import pandas as pd

fruits = ["蘋果", "橘子", "梨子", "櫻桃"]
s = pd.Series([15, 33, 45, 55], index=fruits) 
print("橘子=", s["橘子"])
print("---------------------------")
print(s[["橘子","梨子","櫻桃"]])
print("---------------------------")
print((s+2)*3)
print("---------------------------")
print(s.apply(np.sin))
 