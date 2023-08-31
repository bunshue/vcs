import cv2
import numpy as np

import sys

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("img",img)

t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("rst",rst)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("img",img)


t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("rst",rst)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("img",img)

t,rst=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
cv2.imshow("rst",rst)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("img",img)

t,rst=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("rst",rst)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("img",img)

t,rst=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
cv2.imshow("rst",rst)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

img=cv2.imread("computer.jpg",0)
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

img=cv2.imread("tiffany.bmp",0)
print('顯示原圖')
cv2.imshow("img",img)

t1,thd=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
t2,otsu=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("thd",thd)
cv2.imshow("otus",otsu)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個



