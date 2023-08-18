# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 11:26:41 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
import numpy as np
def Demo(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("单击了鼠标左键")
    elif event==cv2.EVENT_RBUTTONDOWN :
        print("单击了鼠标右键")
    elif flags==cv2.EVENT_FLAG_LBUTTON:
        print("按住左键拖动了鼠标")
    elif event==cv2.EVENT_MBUTTONDOWN :
        print("单击了中间键")
#创建名称为Demo的响应（回调）函数OnMouseAction
#将回调函数Demo与窗口“Demo19.9”建立连接
img = np.ones((300,300,3),np.uint8)*255
cv2.namedWindow('Demo19.9')
cv2.setMouseCallback('Demo19.9',Demo)     
cv2.imshow('Demo19.9',img)
cv2.waitKey()
cv2.destroyAllWindows()