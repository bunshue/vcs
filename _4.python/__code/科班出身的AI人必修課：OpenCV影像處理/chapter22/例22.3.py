import numpy as np
import cv2
import matplotlib.pyplot as plt

#读取待处理图像
img = cv2.imread('lena.bmp')
#使用reshape将一个RGB像素点值的三个值作为一个单元
data = img.reshape((-1,3))
#转换为kmeans可以处理的类型
data = np.float32(data)
#调用kmeans模块
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K =2
ret,label,center=cv2.kmeans(data,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# 转换为uint8数据类型，将每个像素点值都赋值为当前组的中心点值
#将center的值转换为uint8
center = np.uint8(center)
#使用center内的值替换原有像素点值
res1 = center[label.flatten()]
#使用reshape调整替换后图像
res2 = res1.reshape((img.shape))
#显示处理结果
plt.subplot(121)
plt.imshow(img)
plt.axis('off')
plt.subplot(122)
plt.imshow(res2)
plt.axis('off')

