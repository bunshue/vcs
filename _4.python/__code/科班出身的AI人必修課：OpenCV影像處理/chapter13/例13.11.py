# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 20:41:08 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
#-----------导入使用的模块---------------
import cv2
import matplotlib.pyplot as plt
#-----------读取原始图像---------------
img = cv2.imread('image\\equ.bmp',cv2.IMREAD_GRAYSCALE)
#-----------直方图均衡化处理---------------
equ = cv2.equalizeHist(img)
#-----------显示均衡化前后的直方图---------------
cv2.imshow("original",img)
cv2.imshow("result",equ)
#-----------显示均衡化前后的直方图---------------
plt.figure("原始图像直方图")  #构建窗口
plt.hist(img.ravel(),256)
plt.figure("均衡化结果直方图")  #构建新窗口
plt.hist(equ.ravel(),256)
#----------等待释放窗口---------------------
cv2.waitKey()
cv2.destroyAllWindows()