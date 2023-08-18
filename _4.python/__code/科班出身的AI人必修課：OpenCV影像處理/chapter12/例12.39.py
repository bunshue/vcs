# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:59:57 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import numpy as np
o = cv2.imread('cs.bmp')  
#--------获取并绘制轮廓-----------------
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  
mask = np.zeros(gray.shape,np.uint8)
cnt=contours[0] 
cv2.drawContours(mask,[cnt],0,255,-1)
#--------计算极值----------------- 
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
#--------计算极值----------------- 
print("leftmost=",leftmost)
print("rightmost=",rightmost)
print("topmost=",topmost)
print("bottommost=",bottommost)
#--------绘制说明文字----------------- 
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o,'A',leftmost, font, 1,(0,0,255),2)
cv2.putText(o,'B',rightmost, font, 1,(0,0,255),2)
cv2.putText(o,'C',topmost, font, 1,(0,0,255),2)
cv2.putText(o,'D',bottommost, font, 1,(0,0,255),2)
#--------绘制图像----------------- 
cv2.imshow("result",o)
#--------释放窗口----------------- 
cv2.waitKey()
cv2.destroyAllWindows()