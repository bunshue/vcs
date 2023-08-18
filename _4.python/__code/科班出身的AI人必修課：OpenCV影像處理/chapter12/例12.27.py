# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:33:20 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""

import cv2
#-----------读取原始图像--------------------
o1 = cv2.imread('cs.bmp')
o2 = cv2.imread('cs3.bmp') 
o3 = cv2.imread('hand.bmp') 
cv2.imshow("original1",o1)
cv2.imshow("original2",o2) 
cv2.imshow("original3",o3) 
#-----------色彩转换--------------------
gray1 = cv2.cvtColor(o1,cv2.COLOR_BGR2GRAY) 
gray2 = cv2.cvtColor(o2,cv2.COLOR_BGR2GRAY) 
gray3 = cv2.cvtColor(o3,cv2.COLOR_BGR2GRAY) 
#-----------阈值处理--------------------
ret, binary1 = cv2.threshold(gray1,127,255,cv2.THRESH_BINARY) 
ret, binary2 = cv2.threshold(gray2,127,255,cv2.THRESH_BINARY) 
ret, binary3 = cv2.threshold(gray3,127,255,cv2.THRESH_BINARY) 
#-----------提取轮廓--------------------
image,contours1, hierarchy = cv2.findContours(binary1,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)  
image,contours2, hierarchy = cv2.findContours(binary2,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)  
image,contours3, hierarchy = cv2.findContours(binary3,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)  
cnt1 = contours1[0]
cnt2 = contours2[0]
cnt3 = contours3[0]
#-----------构造距离提取算子--------------------
hd = cv2.createHausdorffDistanceExtractor()
#-----------计算距离--------------------
d1 = hd.computeDistance(cnt1,cnt1)
print("自身Hausdorff距离d1=", d1)
d2 = hd.computeDistance(cnt1,cnt2)
print("旋转缩放后Hausdorff距离d2=", d2)
d3 = hd.computeDistance(cnt1,cnt3)
print("不相似对象Hausdorff距离d3=", d3)
#-----------显示距离--------------------
cv2.waitKey()
cv2.destroyAllWindows()