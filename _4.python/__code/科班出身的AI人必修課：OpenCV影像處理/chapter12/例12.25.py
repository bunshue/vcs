# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 18:38:25 2018

@author: 李立宗  lilizong@gmail.com
"""

import cv2
#----------------原始图像-------------------------
o = cv2.imread('cs.bmp')
cv2.imshow("original",o)
#----------------获取凸包------------------------ 
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
hull = cv2.convexHull(contours[0])
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, (0, 255, 0), 2)
#----------------内部点A与多边形的关系-------------------------
distA = cv2.pointPolygonTest(hull, (300, 150),False)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'A',(300,150), font, 1,(0,255,0),3)
print("distA=",distA) 
#----------------外部点B与多边形的关系-------------------------
distB = cv2.pointPolygonTest(hull, (300, 250), False)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'B',(300,250), font, 1,(0,255,0),3)
print("distB=",distB) 
#----------------边缘线上点C与多边形的关系----------------------
distC = cv2.pointPolygonTest(hull, (423, 112),False)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'C',(423,112), font, 1,(0,255,0),3)
print("distC=",distC) 
#print(hull)   #测试边缘到底在哪里，然后再使用确定位置的
#----------------显示-------------------------
cv2.imshow("result",image)
cv2.waitKey()
cv2.destroyAllWindows()