# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 22:02:16 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import numpy as np
img=np.random.randint(0,256,size=[2,4,3],dtype=np.uint8)
rst=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print("img=\n",img)
print("rst=\n",rst)
print("像素点(1,0)直接计算得到的值=",
      img[1,0,0]*0.114+img[1,0,1]*0.587+img[1,0,2]*0.299)
print("像素点(1,0)使用公式cv2.cvtColor()转换值=",rst[1,0])
'''
print(img[1,0,0])
print(img[1,0,1])
print(img[1,0,2])
'''