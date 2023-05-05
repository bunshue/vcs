filename = 'C:/_git/vcs/_1.data/______test_files1/_emgu/lena.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'

import cv2

print('使用 OpenCV 顯示一圖')
image = cv2.imread(filename)	#讀取本機圖片

cv2.imshow('Show Picture', image) #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()


'''
print('使用 matplotlib 顯示一圖')
import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread(filename)

plt.imshow(image)	#顯示圖片, 兩行都要
plt.show()              #顯示圖片, 兩行都要
'''
