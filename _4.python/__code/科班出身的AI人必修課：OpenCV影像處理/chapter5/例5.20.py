# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:31:22 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img=cv2.imread("lena.bmp")
rows,cols=img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        if 0.25*cols< i <0.75*cols and 0.25*rows< j <0.75*rows:
                mapx.itemset((i,j),2*( j - cols*0.25 ) + 0.5)
                mapy.itemset((i,j),2*( i - rows*0.25 ) + 0.5)
        else:     
                mapx.itemset((i,j),0)
                mapy.itemset((i,j),0)
rst=cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
cv2.imshow("original",img)
cv2.imshow("result",rst)
cv2.waitKey()
cv2.destroyAllWindows()
