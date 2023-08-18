# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:50:56 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy  as np
a=np.random.randint(0,255,(5,5),dtype=np.uint8)
b=np.zeros((5,5),dtype=np.uint8)
b[0:3,0:3]=255
b[4,4]=255
c=cv2.bitwise_and(a,b)
print("a=\n",a)
print("b=\n",b)
print("c=\n",c)