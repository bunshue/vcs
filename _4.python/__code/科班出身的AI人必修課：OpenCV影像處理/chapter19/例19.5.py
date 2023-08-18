# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 15:30:55 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
import cv2
d = 400
img = np.ones((d,d,3),dtype="uint8")*255
#生成白色背景
center=(round(d/2),round(d/2))
#注意数值类型，center=(d/2,d/2)不可以
size=(100,200)
#轴的长度
for i in range(0,10):
    angle = np.random.randint(0,361)
    #偏移角度    
    color = np.random.randint(0,high = 256,size = (3,)).tolist()
    #生成随机颜色，3个[0,256)的随机数    
    thickness = np.random.randint(1,9)
    cv2.ellipse(img, center, size, angle, 0, 360, color,thickness)
cv2.imshow("demo19.5",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
