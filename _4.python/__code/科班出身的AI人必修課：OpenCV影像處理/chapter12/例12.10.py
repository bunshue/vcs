# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 22:08:28 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""

import cv2
#--------------读取3幅原始图像--------------------
o1 = cv2.imread('cs1.bmp')
o2 = cv2.imread('cs2.bmp')
o3 = cv2.imread('cc.bmp') 
#----------打印3幅原始图像的shape属性值-------------
print("o1.shape=",o1.shape)
print("o2.shape=",o2.shape)
print("o3.shape=",o3.shape)
#--------------色彩空间转换-------------------- 
gray1 = cv2.cvtColor(o1,cv2.COLOR_BGR2GRAY) 
gray2 = cv2.cvtColor(o2,cv2.COLOR_BGR2GRAY) 
gray3 = cv2.cvtColor(o3,cv2.COLOR_BGR2GRAY) 
#-------------进行Hu矩匹配--------------------
ret0 = cv2.matchShapes(gray1,gray1,1,0.0)
ret1 = cv2.matchShapes(gray1,gray2,1,0.0)
ret2 = cv2.matchShapes(gray1,gray3,1,0.0)
#--------------打印差值--------------------
print("相同图像的matchShape=",ret0)
print("相似图像的matchShape=",ret1)
print("不相似图像的matchShape=",ret2)
#--------------显示3幅原始图像--------------------
cv2.imshow("original1",o1)
cv2.imshow("original2",o2)
cv2.imshow("original3",o3)
cv2.waitKey()
cv2.destroyAllWindows()