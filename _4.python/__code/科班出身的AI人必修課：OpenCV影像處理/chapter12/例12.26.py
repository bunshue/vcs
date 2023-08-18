# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:33:20 2018

@author: 李立宗  lilizong@gmail.com
"""

import cv2
#-----------原始图像o1边缘--------------------
o1 = cv2.imread('cs.bmp')
cv2.imshow("original1",o1)
gray1 = cv2.cvtColor(o1,cv2.COLOR_BGR2GRAY) 
ret, binary1 = cv2.threshold(gray1,127,255,cv2.THRESH_BINARY) 
image,contours1, hierarchy = cv2.findContours(binary1,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE) 
cnt1 = contours1[0]
#-----------原始图像o2边缘--------------------
o2 = cv2.imread('cs3.bmp') 
cv2.imshow("original2",o2) 
gray2 = cv2.cvtColor(o2,cv2.COLOR_BGR2GRAY) 
ret, binary2 = cv2.threshold(gray2,127,255,cv2.THRESH_BINARY) 
image,contours2, hierarchy = cv2.findContours(binary2,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)  
cnt2 = contours2[0]
#-----------原始图像o3边缘--------------------
o3 = cv2.imread('hand.bmp') 
cv2.imshow("original3",o3) 
gray3 = cv2.cvtColor(o3,cv2.COLOR_BGR2GRAY) 
ret, binary3 = cv2.threshold(gray3,127,255,cv2.THRESH_BINARY) 
image,contours3, hierarchy = cv2.findContours(binary3,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)  
cnt3 = contours3[0]
#-----------构造距离提取算子--------------------
sd = cv2.createShapeContextDistanceExtractor()
#-----------计算距离--------------------
d1 = sd.computeDistance(cnt1,cnt1)
print("自身距离d1=", d1)
d2 = sd.computeDistance(cnt1,cnt2)
print("旋转缩放后距离d2=", d2)
d3 = sd.computeDistance(cnt1,cnt3)
print("不相似对象距离d3=", d3)
#-----------显示距离--------------------
cv2.waitKey()
cv2.destroyAllWindows()