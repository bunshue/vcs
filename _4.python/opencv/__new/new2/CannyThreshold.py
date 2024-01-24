import cv2
import numpy as np
 
def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0) #執行高斯模糊化
    detected_edges = cv2.Canny(detected_edges,
                               lowThreshold,
                               lowThreshold*ratio,
                               apertureSize = kernel_size)
    dst = cv2.bitwise_and(img,img,mask = detected_edges)  # 只需在原始图像的边缘添加一些颜色
    cv2.imshow('canny demo', dst)

lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3 
img = cv2.imread('data/lena.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
cv2.namedWindow('canny demo') 
cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)
 
CannyThreshold(0)  # 初始化
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
