# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 09:13:52 2018

@author:  天津职业技术师范大学  
@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('computer.jpg',-1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize =3)
orgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
oShow=orgb.copy()
lines = cv2.HoughLinesP(edges,1,np.pi/180,160,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(orgb,(x1,y1),(x2,y2),(255,255,255),2)
plt.subplot(121)
plt.imshow(oShow)
plt.axis('off')
plt.subplot(122)
plt.imshow(orgb)
plt.axis('off')