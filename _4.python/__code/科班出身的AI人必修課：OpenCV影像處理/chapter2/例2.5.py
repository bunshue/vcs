# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:00:44 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import numpy as np
img=np.zeros((2,4,3),dtype=np.uint8)
print("img=\n",img)
print("读取像素点img[0,3]=",img[0,3])
print("读取像素点img[1,2,2]=",img[1,2,2])
img[0,3]=255
img[0,0]=[66,77,88]
img[1,1,1]=3
img[1,2,2]=4
img[0,2,0]=5
print("修改后img\n",img)
print("读取修改后像素点img[1,2,2]=",img[1,2,2])
