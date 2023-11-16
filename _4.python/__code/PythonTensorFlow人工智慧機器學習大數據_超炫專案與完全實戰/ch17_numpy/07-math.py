#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
v = np.array([9, 10], dtype=np.float64)

# 加法
print(x + y)        # 輸出 [[ 6.0  8.0] [10.0 12.0]]
print(np.add(x, y)) # 輸出 [[ 6.0  8.0] [10.0 12.0]]
print(x + 10)       # 輸出 [[11. 12.] [13. 14.]]
# 減法
print(x - y)        # 輸出 [[-4.0 -4.0] [-4.0 -4.0]]
print(np.subtract(x, y)) # 輸出 [[-4.0 -4.0] [-4.0 -4.0]]
print(x -[1,2])     # 輸出 [[0. 0.]  [2. 2.]]
# 乘法
print(x * y)
print(np.multiply(x, y)) # 輸出  [[ 5.0 12.0][21.0 32.0]]
# 除法
print(x / y)
print(np.divide(x, y))# 輸出 [[ 0.2  0.33333333] [ 0.42857143  0.5]]
# 平方
print(x **2)
print(np.sqrt(x))# 輸出[[ 1. 1.41421356] [ 1.73205081  2.]]

#矩陣乘法，兩個數組的點積 Dot product
print(x.dot(y))# 輸出         [[19. 22.] [43. 50.]]
print(np.dot(x, y))   # [[5+14 , 6+16] []]