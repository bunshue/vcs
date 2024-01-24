import cv2
import numpy as np

img = cv2.imread('data/wu_2.png',0)
equ = cv2.equalizeHist(img) #只能传入灰度图
res = np.hstack((img,equ))  #图像列拼接（用于显示）

cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
