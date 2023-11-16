#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"
import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b= a[0:2,1:3]         # 定義b為a 的部分資料
#b= a[0:2,1:3].copy() # 複製b為a 的部分資料
print(b)              #輸出[[2 3], [6 7]]
b[0, 0] = 99          # 修改b的局部資料
print(b)              #輸出[[99  3], [ 6  7]]
print(a)              # 輸出[[ 1 99  3  4],[ 5  6  7  8],[ 9 10 11 12]]