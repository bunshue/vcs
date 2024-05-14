
print('cornerHarris')

import cv2
import numpy as np

filename = 'C:/_git/vcs/_4.python/_data/bear.jpg'

img = cv2.imread(filename)
cv2.imshow('raw_img', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)                 # cornerHarris函数图像格式为 float32

J = (0.05,0.01,0.005)
for j in J:    # 遍历设置阈值：j * dst.max()
    dst = cv2.cornerHarris(src=gray, blockSize=5, ksize=7, k=0.04)
    a = dst>j * dst.max()
    img[a] = [0, 0, 255]
    cv2.imshow('corners_'+ str(j), img)
    cv2.waitKey(0)           # 按 任意鍵 查看下一张

cv2.waitKey(0)
cv2.destroyAllWindows()




import cv2
import numpy as np
img = cv2.imread('chair.jpg')
cv2.imshow('raw_img', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)                 # cornerHarris函数图像格式为 float32

J = (0.05,0.01,0.005)
for j in J:    # 遍历设置阈值：j * dst.max()
    dst = cv2.cornerHarris(src=gray, blockSize=5, ksize=7, k=0.04)
    a = dst>j * dst.max()
    img[a] = [0, 0, 255]
    cv2.imshow('corners_'+ str(j), img)
    cv2.waitKey(0)           # 按Esc查看下一张

cv2.waitKey(0)
cv2.destroyAllWindows()

