filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'

import cv2
import numpy as np


image = cv2.imread(filename)	#讀取本機圖片

image_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

#以 cv2.imread 讀進來的資料，會儲存成一個 NumPy 的陣列

'''
# 查看資料型態
print(type(image))
print(type(image_gray))

<class 'numpy.ndarray'>

#此 NumPy 陣列的前兩個維度分別是圖片的高度與寬度
#第三個維度則是圖片的 channel（RGB 彩色圖片的 channel 是 3，灰階圖片則為 1）

h ,w, d = image.shape
print("Image Size: %d x %d, channel = %d" % (w, h, d))

h ,w = image_gray.shape
#print("Image Size: %d x %d, channel = %d" % (w, h, d))

cv2.imshow('Picture Viewer', image) #顯示圖片


此 NumPy 陣列的前兩個維度分別是圖片的高度與寬度，第三個維度則是圖片的 channel（RGB 彩色圖片的 channel 是 3，灰階圖片則為 1）。

以這個子來說，我們的原始圖片是一張 1920×1080 的彩色圖片，我們可以檢查一下這個 NumPy 陣列的大小：

image.shape

(1080, 1920, 3)

圖檔格式

OpenCV 的 cv2.imread 在讀取圖片時，可以在第二個參數指定圖片的格式，可用的選項有三種：

cv2.IMREAD_COLOR
    此為預設值，這種格式會讀取 RGB 三個 channels 的彩色圖片，而忽略透明度的 channel。
cv2.IMREAD_GRAYSCALE
    以灰階的格式來讀取圖片。
cv2.IMREAD_UNCHANGED
    讀取圖片中所有的 channels，包含透明度的 channel。
'''

image_gray = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉為灰階

# 顯示圖片
cv2.imshow('My Image', image)

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

'''
這裡 cv2.waitKey 函數是用來等待與讀取使用者按下的按鍵，而其參數是等待時間（單位為毫秒），
若設定為 0 就表示持續等待至使用者按下按鍵為止，
這樣當我們按下任意按鍵之後，就會呼叫 cv2.destroyAllWindows 關閉所有 OpenCV 的視窗。

如果在程式中有許多的 OpenCV 視窗，而我們只要關閉特定的視窗時，可以改用 cv2.destroyWindow 加上視窗名稱，關閉指定的視窗：

# 關閉 'My Image' 視窗
cv2.destroyWindow('My Image')

在預設的狀況下，以 cv2.imshow 所開啟的視窗會依據圖片來自動調整大小，但若是圖片太大、佔滿整個螢幕時，我們會希望可以自由縮放視窗的大小，這時候就可以使用 cv2.namedWindow 將視窗設定為 cv2.WINDOW_NORMAL：

# 讓視窗可以自由縮放大小
cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)

cv2.imshow('My Image', image)

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)  # 0 : 持續等待至使用者按下按鍵為止
cv2.destroyAllWindows() # 關閉所有 OpenCV 的視窗

# 關閉 'My Image' 視窗
# cv2.destroyWindow('My Image') 指名關閉某視窗

使用 OpenCV 開啟的圖形視窗會類似這樣：

OpenCV 顯示圖片視窗

灰階的圖片也可以顯示，用法都相同：
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

image_bgr = cv2.imread(filename)  #讀取本機圖片

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

