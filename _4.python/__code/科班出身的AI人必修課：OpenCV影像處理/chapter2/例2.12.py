# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:00:44 2018
@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
img=cv2.imread("lenacolor.png")
cv2.imshow("before",img)
print("访问img.item(0,0,0)=",img.item(0,0,0))
print("访问img.item(0,0,1)=",img.item(0,0,1))
print("访问img.item(0,0,2)=",img.item(0,0,2))
for i in range(0,50):
    for j in range(0,100):
        for k in range(0,3):
            img.itemset((i,j,k),255)     #白色
cv2.imshow("after",img)
print("修改后img.item(0,0,0)=",img.item(0,0,0))
print("修改后img.item(0,0,1)=",img.item(0,0,1))
print("修改后img.item(0,0,2)=",img.item(0,0,2))
cv2.waitKey()
cv2.destroyAllWindows()

