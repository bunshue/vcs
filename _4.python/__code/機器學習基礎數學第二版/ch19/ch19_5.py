# ch19_5.py
import numpy as np

x1 = np.array([0, 1, 1, 3, 2, 1])
# 因為 x1 元素最大值是 3, 所以 bin 是 4
print(f'np.bincount = {np.bincount(x1)}')       

x2 = np.array([0, 1, 1, 7, 2, 1])
# 因為 x2 元素最大值是 7, 所以 bin 是 8
print(f'np.bincount = {np.bincount(x2)}') 

