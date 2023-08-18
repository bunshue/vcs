# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 22:11:44 2018
@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""

import cv2
gray=cv2.imread("lena.bmp",0)
color=cv2.imread("lenacolor.png")
print("图像gray属性：")
print("gray.shape=",gray.shape)
print("gray.size=",gray.size)
print("gray.dtype=",gray.dtype)
print("图像color属性：")
print("color.shape=",color.shape)
print("color.size=",color.size)
print("color.dtype=",color.dtype)
