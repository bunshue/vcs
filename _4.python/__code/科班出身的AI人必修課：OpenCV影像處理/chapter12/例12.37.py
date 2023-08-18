# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:59:57 2018
@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import numpy as np
o = cv2.imread('ct.png')  
cv2.imshow("original",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
cnt=contours[2]   #coutours[0]、coutours[1]是左侧字母R
#--------使用掩膜获取感兴趣区域的最值-----------------
#需要注意minMaxLoc处理的对象为灰度图像，本例中处理对象为灰度图像gray
#如果希望获取彩色图像的，需要提取各个通道，将每个通道独立计算最值
mask = np.zeros(gray.shape,np.uint8)
mask=cv2.drawContours(mask,[cnt],-1,255,-1)   
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gray,mask = mask)
print("minVal=",minVal)
print("maxVal=",maxVal)
print("minLoc=",minLoc)
print("maxLoc=",maxLoc)
#--------使用掩膜获取感兴趣区域并显示-----------------
masko = np.zeros(o.shape,np.uint8)
masko=cv2.drawContours(masko,[cnt],-1,(255,255,255),-1)
loc=cv2.bitwise_and(o,masko) 
cv2.imshow("mask",loc)
#显示灰度结果
#loc=cv2.bitwise_and(gray,mask) 
#cv2.imshow("mask",loc)
#--------释放窗口-----------------
cv2.waitKey()
cv2.destroyAllWindows()