# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:59:57 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import numpy as np
#--------读取并显示原始图像-----------------
o = cv2.imread('ct.png')  
cv2.imshow("original",o)
#--------获取轮廓-----------------
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
cnt=contours[2] 
#--------使用掩膜获取感兴趣区域的均值----------------- 
mask = np.zeros(gray.shape,np.uint8)#构造mean所使用的掩膜，必须是单通道的
cv2.drawContours(mask,[cnt],0,(255,255,255),-1)
meanVal = cv2.mean(o,mask = mask)  #mask是区域，所以必须是单通道的
print("meanVal=\n",meanVal)
#--------使用掩膜获取感兴趣区域并显示-----------------
masko = np.zeros(o.shape,np.uint8)
cv2.drawContours(masko,[cnt],-1,(255,255,255),-1)
loc=cv2.bitwise_and(o,masko)
cv2.imshow("mask",loc)
#--------释放窗口-----------------
cv2.waitKey()
cv2.destroyAllWindows()