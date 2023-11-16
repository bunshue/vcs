#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"


import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
bool_idx =  ((a % 2)==0)
print(bool_idx)
print(a[bool_idx])
print(a[a > 10])
print(a[a%2==1]*10)
