# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:00:44 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
img=cv2.imread("lena.bmp",0)
#测试读取、修改单个像素值
print("读取像素点img.item(3,2)=",img.item(3,2))
img.itemset((3,2),255)
print("修改后像素点img.item(3,2)=",img.item(3,2))
#测试修改一个区域的像素值
cv2.imshow("before",img)
for i in range(10,100):
    for j in range(80,100):
        img.itemset((i,j),255)
cv2.imshow("after",img)
cv2.waitKey()
cv2.destroyAllWindows()
