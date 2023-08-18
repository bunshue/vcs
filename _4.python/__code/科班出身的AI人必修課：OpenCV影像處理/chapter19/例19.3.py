# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:51:25 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
import cv2
d = 400
img = np.ones((d,d,3),dtype="uint8")*255
(centerX,centerY) = (round(img.shape[1] / 2),round(img.shape[0] / 2))
#将图像的中心作为圆心,实际值为=d/2
red = (0,0,255)#设置白色变量
for r in range(5,round(d/2),12):
    cv2.circle(img,(centerX,centerY),r,red,3)
    #circle(载体图像，圆心，半径，颜色)
cv2.imshow("Demo19.3",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
