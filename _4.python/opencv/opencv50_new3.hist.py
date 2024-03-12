"""

cv2


"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

#用hist()和cv2.calcHist()函数绘制直方图

filename = 'C:/_git/vcs/_4.python/_data/ims01.bmp'

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(filename)   #img.shape返回(576, 720, 3)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#---------使用hist()函数绘图---注意：用这个函数画图像直方图时一定要用灰度图像，如果非用彩图，那得按通道画，不然没有什么意义----------------
plt.figure(figsize=(16,8))
plt.subplot(131), plt.imshow(img[:,:,::-1])   #原图
plt.subplot(132), plt.hist(img_gray.ravel(), 256)  #将灰度级划分为256个等级
plt.subplot(133), plt.hist(img_gray.ravel(), 16, color='red')   #将灰度级划分为16个等级

#---------使用cv2.calcHist()函数绘图----这个函数可以传入彩图，因为它还有一个channel参数，就把通道分开了---------------------
hist_b = cv2.calcHist([img], [0], None, [256], [0, 256])  
hist_g = cv2.calcHist([img], [1], None, [256], [0, 256])  
hist_r = cv2.calcHist([img], [2], None, [256], [0, 256])  
hist_gray1 = cv2.calcHist([img_gray], [0], None, [256], [0, 256])  
hist_gray2 = cv2.calcHist([img_gray], [0], None, [16], [0, 256])  

plt.figure(figsize=(16,8))
plt.subplot(131), plt.plot(hist_b, color='b'), plt.plot(hist_g, color='g'), plt.plot(hist_r, color='r')
plt.subplot(132), plt.plot(hist_gray1, color='gray') 
plt.subplot(133), plt.plot(hist_gray2, color='gray') 
plt.show()



print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'
filename = 'C:/_git/vcs/_4.python/_data/ims01.bmp'

#例13.2 使用掩膜绘制直方图  
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(filename)

# 做一個一樣大小的mask
mask = np.zeros(img.shape, np.uint8)

#修改mask
mask[200:400, 200:400]=255
img_mask = cv2.bitwise_and(img, mask)

hist_img = cv2.calcHist([img], [0], None, [256], [0,256])
hist_img_mask = cv2.calcHist([img], [0], mask[:,:,0], [256], [0,256])
hist_mask = cv2.calcHist([img_mask[200:400, 200:400]], [0], None, [256], [0,256])

#可视化
plt.figure(figsize=(16,8))
plt.subplot(231), plt.imshow(img[:,:,::-1])
plt.subplot(232), plt.imshow(img_mask[:,:,::-1]) 
plt.subplot(234), plt.plot(hist_img), plt.plot(hist_img_mask) #无掩膜和有掩膜的直方图画到一起
plt.subplot(235), plt.plot(hist_img_mask)   #单独划出有掩膜的直方图
plt.subplot(236), plt.plot(hist_mask)     #单独把mask部分图像的直方图画出来，和上面的一模一样

plt.show()


print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'
filename = 'C:/_git/vcs/_4.python/_data/ims01.bmp'

#例13.3 实现图像均衡化处理    
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(filename)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#-----------------------图像均衡化处理----------------
equ = cv2.equalizeHist(img_gray)            

plt.figure(figsize=(16,8))
plt.subplot(221), plt.imshow(img[:,:,::-1])
plt.subplot(222), plt.imshow(img_gray, cmap='gray') 
plt.subplot(223), plt.imshow(equ, cmap='gray') 
plt.subplot(224), plt.imshow(equ, cmap='gray_r'),plt.axis('off') #cmap和axis小知识点

plt.show()

#----------------------直方图对比----------------
print('aaaa')
hist_img_gray = cv2.calcHist([img_gray], [0], None, [256], [0,256])  #生成灰度图像的直方图
hist_equ = cv2.calcHist([equ], [0], None, [256], [0,256])   #生成均衡化后的图像的直方图

plt.figure(figsize=(16,12))
plt.subplot(221), plt.plot(hist_img_gray)
plt.subplot(222), plt.plot(hist_equ) 
plt.subplot(223), plt.hist(img_gray.ravel(), 256) 
plt.subplot(224), plt.hist(equ.ravel(), 256) 
plt.show()




print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
