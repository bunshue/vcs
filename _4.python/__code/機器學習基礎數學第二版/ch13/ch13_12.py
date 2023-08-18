# ch13_12.py
import numpy as np

# 一維陣列
arr1 = np.arange(9)
print("一維陣列")
print(arr1)
np.random.shuffle(arr1)         # 重新排列
print("重新排列")
print(arr1)

# 二維陣列
arr2 = np.arange(9).reshape((3,3))
print("二維陣列")
print(arr2)
np.random.shuffle(arr2)         # 重新排列
print("重新排列")
print(arr2)
    





