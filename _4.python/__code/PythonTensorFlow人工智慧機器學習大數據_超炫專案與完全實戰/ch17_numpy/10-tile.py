#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"
import numpy as np
#方法1
x = np.array([[1,2,3], [4,5,6]])
v = np.array([1, 0, 1])
y = np.empty_like(x)
for i in range(2):
    y[i, :] = x[i, :] + v
print(y)    #輸出[[2 2 4][5 5 7]]

#方法2
v2 = np.tile(v, (2, 1))
print(v2)   #輸出[[1 0 1][1 0 1]]
print(x+v2) #輸出[[2 2 4] [5 5 7]]

#方法3
print(x+v)  #輸出[[2 2 4] [5 5 7]]


