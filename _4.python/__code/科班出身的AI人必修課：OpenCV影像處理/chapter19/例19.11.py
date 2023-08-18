# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 13:17:55 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
import numpy as np
thickness=-1
mode=1
d=400
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        a=np.random.randint(1,d-50)
        r=np.random.randint(1,d/5)
        angle = np.random.randint(0,361)
        color = np.random.randint(0,high = 256,size = (3,)).tolist()
        if mode==1:
            cv2.rectangle(img,(x,y),(a,a),color,thickness)
        elif mode==2:
            cv2.circle(img,(x,y),r,color,thickness)
        elif mode==3:
            cv2.line(img,(a,a),(x,y),color,3)  
        elif mode==4:
            cv2.ellipse(img, (x,y), (100,150), angle, 0, 360,color,thickness)                  
        elif mode==5:
            cv2.putText(img,'OpenCV',(0,round(d/2)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2,color,5)    
img=np.ones((d,d,3),np.uint8)*255
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==ord('r'):
        mode=1
    elif k==ord('c'):
        mode=2
    elif k==ord('l'):
        mode=3
    elif k==ord('e'):
        mode=4
    elif k==ord('t'):
        mode=5
    elif k==ord('f'):
        thickness=-1
    elif k==ord('u'):
        thickness=3
    elif k==27:
        break   
cv2.destroyAllWindows()
