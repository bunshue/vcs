# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 17:03:50 2018
@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import matplotlib.pyplot as plt
o=cv2.imread("image\\boat.bmp")
plt.hist(o.ravel(),16)