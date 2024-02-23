import numpy as np

# 一維
a = np.array([1, 2, 3])
print(a)

# 二維
b = np.array([[1, 2, 3], [5, 6, 7]])
print(b)

# 二維，使用 dtype 定義數據類型
bb = np.array([[1, 2, 3], [5, 6, 7]], dtype=float)
print(bb)

# 最小維度
c = np.array([1,2,3], ndmin = 3)
print(c)

