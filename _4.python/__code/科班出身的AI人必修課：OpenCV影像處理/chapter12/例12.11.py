# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:59:57 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
#---------------读取并显示原始图像------------------ 
o = cv2.imread('cc.bmp')  
#---------------提取图像轮廓------------------ 
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE) 
#---------------返回顶点及边长------------------ 
x,y,w,h = cv2.boundingRect(contours[0])
print("顶点及长宽的点形式:")
print("x=",x)
print("y=",y)
print("w=",w)
print("h=",h)
#---------------仅有一个返回值的情况------------------
rect = cv2.boundingRect(contours[0])
print("\n顶点及长宽的元组（tuple）形式：")
print("rect=",rect)