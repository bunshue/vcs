# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:43:14 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img=np.random.randint(-256,256,size=[4,5],dtype=np.int16)
rst=cv2.convertScaleAbs(img)
print("img=\n",img)
print("rst=\n",rst)
