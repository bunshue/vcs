#filename = 'C:/_git/vcs/_1.data/______test_files1/_emgu/lena.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'

import cv2
import numpy as np
import matplotlib.pyplot as plt

#讀取圖片
img = cv2.imread(filename)
#實例化8位圖
emptyImage = np.zeros(img.shape, np.uint8)
emptyImage2 = img.copy()
#灰度圖
emptyImage3 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#顯示圖片
cv2.imshow("emptyImage",emptyImage)
cv2.imshow("emptyImage2",emptyImage2)
cv2.imshow("emptyImage3",emptyImage3)
cv2.imshow("img",img)
#保存圖片 質量為5 和 100
cv2.imwrite("./1.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),5])
cv2.imwrite("./2.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),100])
#png壓縮大小
cv2.imwrite("./3.png",img,[int(cv2.IMWRITE_PNG_COMPRESSION),0])
cv2.imwrite("./4.png",img,[int(cv2.IMWRITE_PNG_COMPRESSION),9])

#cv2.namedWindow("image")
#cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
