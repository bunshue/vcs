import cv2
import matplotlib.pyplot as plt
import numpy as np  
plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签 
original_img = cv2.imread("lena.png", 0)
#canny(): 边缘检测
img1 = cv2.GaussianBlur(original_img,(3,3),0)
canny = cv2.Canny(img1, 50, 150)

#形态学：边缘检测
_,Thr_img = cv2.threshold(original_img,210,255,cv2.THRESH_BINARY)#设定红色通道阈值210（阈值影响梯度运算效果）
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))         #定义矩形结构元素
gradient = cv2.morphologyEx(Thr_img, cv2.MORPH_GRADIENT, kernel) #梯度
plt.subplot(131)
cv2.imshow("原始图像", original_img) 
plt.subplot(132)
cv2.imshow("梯度", gradient) 
plt.subplot(133)
cv2.imshow('Canny函数', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

