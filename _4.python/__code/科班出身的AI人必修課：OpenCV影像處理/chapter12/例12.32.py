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
ellipse = cv2.fitEllipse(contours[0])
retval=cv2.fitEllipse(contours[0])
print("单个返回值形式：")
print("retval=\n",retval)
(x,y),(MA,ma),angle = cv2.fitEllipse(contours[0])
print("三个返回值形式：")
print("(x,y)=(",x,y,")")
print("(MA,ma)=(",MA,ma,")")
print("angle=",angle)
cv2.ellipse(o,ellipse,(0,0,255),2)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()