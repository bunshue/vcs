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
img = cv2.imread('chess.jpg',0)
imgo=cv2.imread('chess.jpg',-1)
o=cv2.cvtColor(imgo,cv2.COLOR_BGR2RGB)
oshow=o.copy()
img = cv2.medianBlur(img,5)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,300,param1=50,param2=30,minRadius=100,maxRadius=200)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
  cv2.circle(o,(i[0],i[1]),i[2],(255,0,0),12)
  cv2.circle(o,(i[0],i[1]),2,(255,0,0),12)
plt.subplot(121)
plt.imshow(oshow)
plt.axis('off')
plt.subplot(122)
plt.imshow(o)
plt.axis('off')

