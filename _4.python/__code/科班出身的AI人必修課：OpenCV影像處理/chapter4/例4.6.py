# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 16:18:25 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
#=========测试下OpenCV中蓝色的HSV模式值=============
imgBlue=np.zeros([1,1,3],dtype=np.uint8)
imgBlue[0,0,0]=255
Blue=imgBlue
BlueHSV=cv2.cvtColor(Blue,cv2.COLOR_BGR2HSV)
print("Blue=\n",Blue)
print("BlueHSV=\n",BlueHSV)
#=========测试下OpenCV中绿色的HSV模式值=============
imgGreen=np.zeros([1,1,3],dtype=np.uint8)
imgGreen[0,0,1]=255
Green=imgGreen
GreenHSV=cv2.cvtColor(Green,cv2.COLOR_BGR2HSV)
print("Green=\n",Green)
print("GreenHSV=\n",GreenHSV)
#=========测试下OpenCV中红色的HSV模式值=============
imgRed=np.zeros([1,1,3],dtype=np.uint8)
imgRed[0,0,2]=255
Red=imgRed
RedHSV=cv2.cvtColor(Red,cv2.COLOR_BGR2HSV)
print("Red=\n",Red)
print("RedHSV=\n",RedHSV)