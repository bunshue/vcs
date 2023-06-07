#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(filename)	#讀取本機圖片

#實例化8位圖
image_empty = np.zeros(image.shape, np.uint8)
image_copy = image.copy()
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #圖片轉為灰階

#顯示圖片
#cv2.imshow("image_empty", image_empty) #空圖, 全黑
#cv2.imshow("image_copy", image_copy)   #原圖拷貝
#cv2.imshow("image_gray", image_gray)   #原圖黑白
cv2.imshow("image", image)              #原圖

#cv2.namedWindow("image")
#cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

