# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 20:42:34 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""


import numpy as np
import cv2
cap = cv2.VideoCapture('viptrain.avi')
while(cap.isOpened()):
    ret, frame = cap.read()
    frame=cv2.Canny(frame,100,200)
    cv2.imshow('frame',frame)
    c = cv2.waitKey(1)
    if c==27:   #ESC键
        break
cap.release()
cv2.destroyAllWindows()