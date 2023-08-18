# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 17:46:33 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
import cv2
cap = cv2.VideoCapture(0)
fourcc = -1
out = cv2.VideoWriter('output.avi',fourcc, 20, (640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

