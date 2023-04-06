#filename = 'C:/______test_files/_emgu/lena.jpg'
filename = 'C:/______test_files/ims01.bmp'

import matplotlib.pyplot as plt

#显示图片代码：

import cv2
import numpy as np
#读取图片
img = cv2.imread(filename)
#实例化8位图
emptyImage = np.zeros(img.shape, np.uint8)
emptyImage2 = img.copy()
#灰度图
emptyImage3 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#显示图片
cv2.imshow("emptyImage",emptyImage)
cv2.imshow("emptyImage2",emptyImage2)
cv2.imshow("emptyImage3",emptyImage3)
cv2.imshow("img",img)
#保存图片 质量为5 和 100
cv2.imwrite("./1.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),5])
cv2.imwrite("./2.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),100])
#png压缩大小
cv2.imwrite("./3.png",img,[int(cv2.IMWRITE_PNG_COMPRESSION),0])
cv2.imwrite("./4.png",img,[int(cv2.IMWRITE_PNG_COMPRESSION),9])

#cv2.namedWindow("image")
#cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

