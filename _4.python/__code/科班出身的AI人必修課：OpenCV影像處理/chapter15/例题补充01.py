# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:42:17 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
a=np.array([[3,6,8,77,66],[1,2,88,3,98],[11,2,67,5,2]])
print(a)
b=np.where(a>5)
print(b)