# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:00:44 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import numpy as np
img1=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
img2=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
print("img1=\n",img1)
print("img2=\n",img2)
print("img1+img2=\n",img1+img2)
