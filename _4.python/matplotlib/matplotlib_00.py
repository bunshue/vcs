'''
matplotlib 基本使用

顯示圖片

'''


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

'''
print('使用 matplotlib 顯示一圖')
import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread(filename)

plt.imshow(image)	#顯示圖片, 兩行都要
plt.show()              #顯示圖片, 兩行都要
'''

import matplotlib.pyplot as plt
import cv2

image = cv2.imread(filename)	#讀取本機圖片

#plt.imshow(image)#直接顯示 影像錯誤 因為opencv的imread讀出來是BGR排列
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))#先轉換成RGB再顯示


plt.show()
