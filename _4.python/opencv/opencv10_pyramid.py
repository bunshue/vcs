'''
圖像金字塔 (pyrDown,pyrUp)

'''
import cv2
import numpy as np

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'

o=cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('------------------------------------------------------------')	#60個

'''
pyrDown

这里的down是指图像变小，所以原始图像在金字塔的底部。

'''

#连续3次进行pyrDown

print('cv2.__version__:',cv2.__version__)

img = cv2.imread(filename)
img_down = cv2.pyrDown(img,dstsize=(img.shape[1]//2,img.shape[0]//2))
img_down2 = cv2.pyrDown(img_down,dstsize=(img_down.shape[1]//2,img_down.shape[0]//2))
img_down3 = cv2.pyrDown(img_down2,dstsize=(img_down2.shape[1]//2,img_down2.shape[0]//2))
print('img.shape',img.shape)
print('img_down.shape',img_down.shape)
print('img_down2.shape',img_down2.shape)
print('img_down3.shape',img_down3.shape)
cv2.imshow('img',img)
cv2.imshow('img_down',img_down)
cv2.imshow('img_down2',img_down2)
cv2.imshow('img_down3',img_down3)

cv2.waitKey()
cv2.destroyAllWindows()

#pyrUp
#这里的up是指将图像的尺寸变大，所以原始图像位于图像金字塔的顶层。

print('cv2.__version__:',cv2.__version__)

img = cv2.imread(filename)
img = cv2.resize(img,None,fx=0.15,fy=0.15)  #为了观察方便缩小原图
img_up = cv2.pyrUp(img,dstsize=(2*img.shape[1],2*img.shape[0]))
img_up2 = cv2.pyrUp(img_up,dstsize=(2*img_up.shape[1],2*img_up.shape[0]))
img_up3 = cv2.pyrUp(img_up2,dstsize=(2*img_up2.shape[1],2*img_up2.shape[0]))
print('img.shape',img.shape)
print('img_up.shape',img_up.shape)
print('img_up2.shape',img_up2.shape)
print('img_up3.shape',img_up3.shape)
cv2.imshow('img',img)
cv2.imshow('img_up',img_up)
cv2.imshow('img_up2',img_up2)
cv2.imshow('img_up3',img_up3)

cv2.waitKey()
cv2.destroyAllWindows()

