# 使用 Python 與 OpenCV 處理影像圖檔

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'

import numpy as np
import cv2

image = cv2.imread(filename)	#讀取本機圖片

image_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

#以 cv2.imread 讀進來的資料，會儲存成一個 NumPy 的陣列

'''
# 查看資料型態
print(type(image))
print(type(image_gray))

#此 NumPy 陣列的前兩個維度分別是圖片的高度與寬度
#第三個維度則是圖片的 channel（RGB 彩色圖片的 channel 是 3，灰階圖片則為 1）

h ,w, d = image.shape
print("Image Size: %d x %d, channel = %d" % (w, h, d))

h ,w = image_gray.shape
#print("Image Size: %d x %d, channel = %d" % (w, h, d))

cv2.imshow('Picture Viewer', image) #顯示圖片

'''
# cv2.imwrite 可透過圖片的副檔名來指定輸出的圖檔格式
# 寫入不同圖檔格式
cv2.imwrite('output.jpg', image)
cv2.imwrite('output.png', image)
cv2.imwrite('output.tiff', image)

# 輸出圖片檔案時，也可以調整圖片的品質或壓縮率：

# 設定 JPEG 圖片品質為 90（可用值為 0 ~ 100）
cv2.imwrite('output.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 90])

# 設定 PNG 壓縮層級為 5（可用值為 0 ~ 9）
cv2.imwrite('output.png', image, [cv2.IMWRITE_PNG_COMPRESSION, 5])
'''

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)  # 0 : 持續等待至使用者按下按鍵為止
cv2.destroyAllWindows() # 關閉所有 OpenCV 的視窗

# 關閉 'My Image' 視窗
# cv2.destroyWindow('My Image') 指名關閉某視窗


print('用matplotlib顯示圖片')

import numpy as np
import cv2
from matplotlib import pyplot as plt

image_bgr = cv2.imread(filename)	#讀取本機圖片

# 將 OpenCV 讀入的 BGR 格式轉為 Matplotlib 用的 RGB 格式，再交給 Matplotlib 顯示

image_rgb = image_bgr[:,:,::-1]     # 將 BGR 圖片轉為 RGB 圖片
# 或是這樣亦可
# image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# 使用 Matplotlib 顯示圖片
plt.imshow(image_rgb)
plt.show()

image_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉為灰階

# 使用 Matplotlib 顯示圖片
plt.imshow(image_gray, cmap = 'gray')
plt.show()
'''

