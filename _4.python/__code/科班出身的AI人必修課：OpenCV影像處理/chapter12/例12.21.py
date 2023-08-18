# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:59:57 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
# --------------读取并绘制原始图像------------------
o = cv2.imread('hand.bmp')  
cv2.imshow("original",o)
# --------------提取轮廓------------------
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
# --------------寻找凸包，得到凸包的角点------------------
hull = cv2.convexHull(contours[0])
# --------------绘制凸包------------------
cv2.polylines(o, [hull], True, (0, 255, 0), 2)
# --------------显示凸包------------------
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()