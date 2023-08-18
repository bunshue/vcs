# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:41:47 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
import numpy as np
d=400
global thickness
thickness=-1
def fill(x):
    pass
def draw(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        p1x=x
        p1y=y
        p2x=np.random.randint(1,d-50)
        p2y=np.random.randint(1,d-50)
        color = np.random.randint(0,high = 256,size = (3,)).tolist()
        cv2.rectangle(img,(p1x,p1y),(p2x,p2y),color,thickness)

img=np.ones((d,d,3),np.uint8)*255
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)
cv2.createTrackbar('R','image',0,1,fill)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    g=cv2.getTrackbarPos('R','image')
    if g==0:
        thickness=-1
    else:
        thickness=2        
    if k==27:
        break   
cv2.destroyAllWindows()