#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import numpy as np
x = np.array([1, 2])  #numpy自動設定
print(x.dtype)         # 輸出 "int64"
x = np.array([1.0, 2.0])  #numpy自動設定
print(x.dtype)             # 輸出 "float64"
x = np.array([1, 2], dtype=np.int64)  #設定為int64
print(x.dtype)                         # 輸出 "int64"

