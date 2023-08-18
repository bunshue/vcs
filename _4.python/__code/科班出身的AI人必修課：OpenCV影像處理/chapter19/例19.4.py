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
#生成白色背景
for i in range(0,100):
    centerX = np.random.randint(0,high = d)
    #生成随机圆心X,确保在画布img内
    centerY = np.random.randint(0,high = d)
    #生成随机圆心Y,确保在画布img内
    radius = np.random.randint(5,high = d/5)
    #生成随机半径，值范围：[5,d/5)，最大半径是d/5
    color = np.random.randint(0,high = 256,size = (3,)).tolist()
    #生成随机颜色，3个[0,256)的随机数    
    cv2.circle(img,(centerX,centerY),radius,color,-1)
    #使用上述随机数，在画布img内画圆
cv2.imshow("demo19.4",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
