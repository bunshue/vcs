# ch12_15.py
import numpy as np

x1 = [1,2,3]
y1 = [4,5,6,7,8]
z1 = np.add.outer(x1, y1)
print(f"z1 = \n{z1}")

x2 = range(8)
y2 = range(8)
z2 = np.add.outer(x2, y2)
print(f"z2 = \n{z2}")



      
