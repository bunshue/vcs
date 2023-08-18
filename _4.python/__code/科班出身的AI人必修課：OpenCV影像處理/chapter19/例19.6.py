# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 08:49:07 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""
import numpy as np
import cv2
d = 400
img = np.ones((d,d,3),dtype="uint8")*255
#生成白色背景
pts=np.array([[200,50],[300,200],[200,350],[100,200]], np.int32)
#生成各个顶点,注意数据类型为int32
pts=pts.reshape((-1,1,2))
#第1个参数为-1, 表明这一维的长度是根据后面的维度的计算出来的。
cv2.polylines(img,[pts],True,(0,255,0),8)
#调用函数polylines完成多边形绘图，注意第3个参数控制多边形封闭
# cv2.polylines(img,[pts],False,(0,255,0),8)  #不闭合的的多边形
cv2.imshow("demo19.6",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
