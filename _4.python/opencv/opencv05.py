
window_name = 'Show Picture'

import cv2

'''
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
img = cv2.imread(filename, 1)   #0: 黑白圖片 1: 原色圖片
cv2.imshow(window_name, img)

cv2.imwrite('aaaaaaa.pgm', img) #無效????


print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件
'''

'''
print('使用matplotlib顯示圖片')
import matplotlib.pyplot as plt
img = cv2.imread(filename, 1)   #0: 黑白圖片 1: 原色圖片
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([])  #隱藏x座標
plt.yticks([])  #隱藏y座標
plt.show()

'''
