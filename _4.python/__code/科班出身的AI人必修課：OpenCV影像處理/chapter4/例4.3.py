# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 22:33:58 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img=np.random.randint(0,256,size=[2,4,3],dtype=np.uint8)
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
bgr=cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR)
print("img=\n",img)
print("rgb=\n",rgb)
print("bgr=\n",bgr)