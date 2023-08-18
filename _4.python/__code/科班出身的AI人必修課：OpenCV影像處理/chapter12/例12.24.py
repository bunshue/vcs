# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 18:24:31 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
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
#----------------内部点A的距离-------------------------
distA = cv2.pointPolygonTest(hull, (300, 150), True)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'A',(300,150), font, 1,(0,255,0),3)
print("distA=",distA) 
#----------------外部点B的距离-------------------------
distB = cv2.pointPolygonTest(hull, (300, 250), True)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'B',(300,250), font, 1,(0,255,0),3)
print("distB=",distB) 
#------------正好处于边缘上的点C的距离-----------------
distC = cv2.pointPolygonTest(hull, (423, 112), True)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'C',(423,112), font, 1,(0,255,0),3)
print("distC=",distC) 
#print(hull)   #测试边缘到底在哪里，然后再使用确定位置的
#----------------显示-------------------------
cv2.imshow("result",image)
cv2.waitKey()
cv2.destroyAllWindows()