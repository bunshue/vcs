# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 13:45:25 2018

@author: 天津拨云咨询服务有限公司  

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('image\\boat.bmp',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
ishift = np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)
#print(iimg)
iimg = np.abs(iimg)
#print(iimg)
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('original'),plt.axis('off')
plt.subplot(122),plt.imshow(iimg, cmap = 'gray')
plt.title('iimg'),plt.axis('off')
plt.show()
