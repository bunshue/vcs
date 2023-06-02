filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/imagedata/2.jpg'

import numpy as np
import matplotlib.pyplot as plt
import cv2

plt.gcf().set_size_inches(12, 14)
#ax=plt.subplot(5,5, i+1)
#ax.imshow(images[start_id], cmap='binary')  #顯示黑白圖片

image = cv2.imread(filename)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #灰階
_, image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY_INV) #轉為反相黑白

ax=plt.subplot(2, 2, 1)
ax.imshow(image, cmap='binary')  #顯示黑白圖片

title = 'lion'
ax.set_title(title,fontsize=12)  #X,Y軸不顯示刻度
ax.set_xticks([]);ax.set_yticks([])        

plt.show()


