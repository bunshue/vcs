# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:00:44 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import numpy as np
img=np.random.randint(10,99,size=[2,4,3],dtype=np.uint8)
print("img=\n",img)
print("读取像素点img[1,2,0]=",img.item(1,2,0))
print("读取像素点img[0,2,1]=",img.item(0,2,1))
print("读取像素点img[1,0,2]=",img.item(1,0,2))
img.itemset((1,2,0),255)
img.itemset((0,2,1),255)
img.itemset((1,0,2),255)
print("修改后img=\n",img)
print("修改后像素点img[1,2,0]=",img.item(1,2,0))
print("修改后像素点img[0,2,1]=",img.item(0,2,1))
print("修改后像素点img[1,0,2]=",img.item(1,0,2))
