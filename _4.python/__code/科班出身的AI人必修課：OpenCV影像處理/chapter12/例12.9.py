# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 21:08:08 2018
@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""

import cv2
#----------------计算图像1的Hu矩-------------------
o1 = cv2.imread('cs1.bmp')  
gray1 = cv2.cvtColor(o1,cv2.COLOR_BGR2GRAY)  
HuM1=cv2.HuMoments(cv2.moments(gray1)).flatten()
#----------------计算图像2的Hu矩-------------------
o2 = cv2.imread('cs3.bmp')  
gray2 = cv2.cvtColor(o2,cv2.COLOR_BGR2GRAY)  
HuM2=cv2.HuMoments(cv2.moments(gray2)).flatten()
#----------------计算图像3的Hu矩-------------------
o3 = cv2.imread('lena.bmp')  
gray3 = cv2.cvtColor(o3,cv2.COLOR_BGR2GRAY)  
HuM3=cv2.HuMoments(cv2.moments(gray3)).flatten()
#---------打印图像1、图像2、图像3的特征值------------
print("o1.shape=",o1.shape)
print("o2.shape=",o2.shape)
print("o3.shape=",o3.shape)
print("cv2.moments(gray1)=\n",cv2.moments(gray1))
print("cv2.moments(gray2)=\n",cv2.moments(gray2))
print("cv2.moments(gray3)=\n",cv2.moments(gray3))
print("\nHuM1=\n",HuM1)
print("\nHuM2=\n",HuM2)
print("\nHuM3=\n",HuM3)
#---------计算图像1与图像2、图像3的Hu矩之差----------------
print("\nHuM1-HuM2=",HuM1-HuM2)
print("\nHuM1-HuM3=",HuM1-HuM3)
#---------显示图像----------------
cv2.imshow("original1",o1)
cv2.imshow("original2",o2)
cv2.imshow("original3",o3)
cv2.waitKey()
cv2.destroyAllWindows()