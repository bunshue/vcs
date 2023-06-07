
window_name = 'Show Picture'

import cv2

'''
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

image = cv2.imread(filename, 1)	  #讀取本機圖片, 0: 黑白圖片 1: 原色圖片
cv2.imshow(window_name, image)

cv2.imwrite('aaaaaaa.pgm', image) #無效????


print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件
'''

'''
print('使用matplotlib顯示圖片')
import matplotlib.pyplot as plt

image = cv2.imread(filename, 1)	  #讀取本機圖片, 0: 黑白圖片 1: 原色圖片

plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([])  #隱藏x座標
plt.yticks([])  #隱藏y座標
plt.show()

'''


import cv2

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2a = 'C:/_git/vcs/_1.data/______test_files2/picture1a.jpg'
filename2b = 'C:/_git/vcs/_1.data/______test_files2/picture1b.jpg'

cv2.namedWindow("ShowImage1")
cv2.namedWindow("ShowImage2")

image1 = cv2.imread(filename1)	#讀取本機圖片
#image1 = cv2.imread(filename1, 1)
image2 = cv2.imread(filename1, 0)   #讀取本機圖片, 0: 黑白圖片 1: 原色圖片

cv2.imshow("ShowImage1", image1) 
cv2.imshow("ShowImage2", image2)


cv2.waitKey(0)
#cv2.waitKey(10000)
cv2.destroyAllWindows()



