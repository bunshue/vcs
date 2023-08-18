# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:59:57 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
o = cv2.imread('cc.bmp')  
cv2.imshow("original",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
x,y,w,h = cv2.boundingRect(contours[0])
cv2.drawContours(o,contours[0],-1,(0,0,255),3) 
cv2.rectangle(o,(x,y),(x+w,y+h),(255,0,0),3)
rectArea=w*h
cntArea=cv2.contourArea(contours[0])
extend=float(cntArea)/rectArea
print(extend)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()