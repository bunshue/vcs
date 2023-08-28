# ch16_0.py
import numpy as np

x = [9, 12, 30, 31, 31, 32, 33, 33, 35, 35,
     38, 38, 41, 42, 43, 46, 46, 48, 52, 70]
rtn = np.percentile(x,np.arange(0,100,25))
Q1 = rtn[1]
mean = rtn[2]
Q3 = rtn[3]
IQR = Q3 - Q1
print(f"回傳值 = {rtn}")
print(f"最小值 = {Q1-1.5*IQR}")
print(f"  Q1   = {Q1}")
print(f" mean  = {mean}")
print(f"  Q3   = {Q3}")
print(f"最大值 = {Q3+1.5*IQR}")





      
