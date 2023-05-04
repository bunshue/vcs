

'''

https://blog.gtwang.org/programming/python-opencv-matplotlib-plot-histogram-tutorial/
https://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html

'''

#filename = 'C:/______test_files1/_emgu/lena.jpg'
filename = 'C:/______test_files1/ims01.bmp'


#import numpy as np

import cv2
import numpy as np
import matplotlib.pyplot as plt



'''


# 讀取圖檔
img = cv2.imread(filename)

# 轉為灰階圖片
# 轉為灰階圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 計算直方圖每個 bin 的數值
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# 畫出直方圖
#plt.bar(range(1,255), hist)

# 畫出分佈圖
plt.plot(hist)

# 使用 ravel 將所有的像素資料轉為一維的陣列，以下是一個簡單的範例：
# 畫出直方圖
#plt.hist(gray.ravel(), 256, [0, 256])

plt.show()


#對於彩色的圖片，
#可以用 OpenCV 的 calcHist 函數分別計算統計值，
#並畫出 RGB 三種顏色的分佈圖：

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(filename)

# 畫出 RGB 三種顏色的分佈圖
color = ('b','g','r')
for i, col in enumerate(color):
  histr = cv2.calcHist([img],[i],None,[256],[0, 256])
  plt.plot(histr, color = col)
  plt.xlim([0, 256])
plt.show()
'''


#配合圖形遮罩計算直方圖

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 讀取圖檔
img = cv2.imread(filename)

# 轉為灰階圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 建立圖形遮罩
mask = np.zeros(gray.shape, np.uint8)
#mask[300:780, 300:1620] = 255
W = 640
H = 480
x_st = int(W / 4)
y_st = int(H / 4)
w = int(W / 2)
h = int(H / 2)

mask[y_st:y_st+h, x_st:x_st+w] = 255    #先h 後 w
#mask[0:240, 0:320] = 255

# 計算套用遮罩後的圖形
masked_gray = cv2.bitwise_and(gray, gray, mask = mask)

# 以原圖計算直方圖
hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])

# 以套用遮罩後的圖計算直方圖
hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])

# 繪製結果
plt.subplot(221), plt.imshow(gray, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_gray, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()


