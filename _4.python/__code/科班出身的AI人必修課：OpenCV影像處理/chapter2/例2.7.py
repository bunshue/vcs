# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:00:44 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import numpy as np
img=np.random.randint(10,99,size=[5,5],dtype=np.uint8)
print("img=\n",img)
print("读取像素点img.item(3,2)=",img.item(3,2))
img.itemset((3,2),255)
print("修改后img=\n",img)
print("修改后像素点img.item(3,2)=",img.item(3,2))
