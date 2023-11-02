import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("img",img)

print('顯示二值化圖')
#        cv2.threshold(img, 閥值, 最大灰度值, 使用的二值化方法)
t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
#t, rst = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
#t, rst = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
#t, rst = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)

cv2.imshow("rst",rst)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/computer.jpg'
img=cv2.imread(filename, 0)
print('顯示原圖')
cv2.imshow("img",img)

t1,thd=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
athdMEAN=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
athdGAUS=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,5)
cv2.imshow("thd",thd)
cv2.imshow("athdMEAN",athdMEAN)
cv2.imshow("athdGAUS",athdGAUS)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/tiffany.bmp'
img=cv2.imread(filename, 0)
print('顯示原圖')
cv2.imshow("img",img)

t1,thd=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
t2,otsu=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("thd",thd)
cv2.imshow("otus",otsu)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個



