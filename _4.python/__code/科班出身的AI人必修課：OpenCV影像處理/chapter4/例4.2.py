# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 22:28:45 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img=np.random.randint(0,256,size=[2,4],dtype=np.uint8)
rst=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
print("img=\n",img)
print("rst=\n",rst)