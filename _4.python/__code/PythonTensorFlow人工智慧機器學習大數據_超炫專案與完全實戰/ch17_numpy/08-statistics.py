#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"


import numpy as np
x = np.array([[-1,2,3],[13,14,15]])
print(x)
print(np.sum(x))       # 輸出46   全部累加
print(np.sum(x, axis=0))  # 輸出"[12 16 18]" =(-1+13),(2+14),(3+15)
print(np.sum(x, axis=1))  # 輸出"[ 4 42]" =(-1+2+3),(13+14+15)
print(np.max(x))       #最大值 輸出15
print(np.min(x))       #最小值 輸出-1
print(np.cumsum(x))    # 累加[-1  1  4 17 31 46]
# 加權平均值
print(np.average(x))   # 輸出7.666
# 平均 mean=sum(x)/len(x)
print(np.mean(x))      # 輸出7.666
# 中間值
print(np.median(x))   # 輸出8.0
# 標準偏差 std = sqrt(mean(abs(x - x.mean())**2))
print(np.std(x))       # 輸出 6.472
# 方差 var = mean(abs(x - x.mean())**2)
print(np.var(x))       # 輸出 41.888
print(x.T)       # 輸出 [[-1 13] [ 2 14] [ 3 15]]
