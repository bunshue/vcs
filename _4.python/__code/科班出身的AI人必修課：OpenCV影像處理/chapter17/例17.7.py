# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 13:35:29 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
o = cv2.imread('lenacolor.png')
orgb=cv2.cvtColor(o,cv2.COLOR_BGR2RGB)
mask = np.zeros(o.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,50,400,400)
cv2.grabCut(o,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
ogc = o*mask2[:,:,np.newaxis]
ogc=cv2.cvtColor(ogc,cv2.COLOR_BGR2RGB)
plt.subplot(121)
plt.imshow(orgb)
plt.axis('off')
plt.subplot(122)
plt.imshow(ogc)
plt.axis('off')