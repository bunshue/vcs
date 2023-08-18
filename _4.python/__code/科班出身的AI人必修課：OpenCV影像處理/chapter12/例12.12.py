# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:59:57 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import numpy as np
#---------------读取并显示原始图像------------------ 
o = cv2.imread('cc.bmp')  
cv2.imshow("original",o)
#---------------提取图像轮廓------------------ 
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE) 
#---------------构造矩形边界------------------ 
x,y,w,h = cv2.boundingRect(contours[0])
brcnt = np.array([[[x, y]], [[x+w, y]], [[x+w, y+h]], [[x, y+h]]])
cv2.drawContours(o, [brcnt], -1, (255, 255,255), 2)
#---------------显示矩形边界------------------
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()