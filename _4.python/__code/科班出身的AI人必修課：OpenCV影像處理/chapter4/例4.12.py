# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 18:38:53 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
img=np.random.randint(0,256,size=[2,3,3],dtype=np.uint8)
bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
print("img=\n",img)
print("bgra=\n",bgra)
b,g,r,a=cv2.split(bgra)
print("a=\n",a)
a[:,:]=125
bgra=cv2.merge([b,g,r,a])
print("bgra=\n",bgra)
