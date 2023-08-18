# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:41:47 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
Type=0  #阈值处理类型值
Value=0 #使用的阈值
def onType(a):
    Type= cv2.getTrackbarPos(tType, windowName)
    Value= cv2.getTrackbarPos(tValue, windowName)
    ret, dst = cv2.threshold(o, Value,255, Type) 
    cv2.imshow(windowName,dst)
 
def onValue(a):
    Type= cv2.getTrackbarPos(tType, windowName)
    Value= cv2.getTrackbarPos(tValue, windowName)
    ret, dst = cv2.threshold(o, Value, 255, Type) 
    cv2.imshow(windowName,dst)

o = cv2.imread("lena512.bmp",0)
windowName = "Demo19.13"  #窗体名
cv2.namedWindow(windowName)
cv2.imshow(windowName,o)
#创建两个滑动条
tType = "Type"  #用来选取阈值处理类型的滚动条
tValue = "Value"    #用来选取阈值的滚动条
cv2.createTrackbar(tType, windowName, 0, 4, onType)
cv2.createTrackbar(tValue, windowName,0, 255, onValue) 
if cv2.waitKey(0) == 27:  
    cv2.destroyAllWindows()