filename = 'C:/______test_files/_emgu/lena.jpg'
#filename = 'C:/______test_files/ims01.bmp'

#import numpy as np
#import matplotlib.pyplot as plt

'''

#Python 與 OpenCV 裁切圖片教學
#OpenCV 裁切圖片

import cv2	#導入 OpenCV 模組

filename = 'C:/______test_files/_emgu/lena.jpg'
img = cv2.imread(filename)	# 讀取本機圖片

#這裡用 OpenCV 讀取進來的圖片 img 其實就是 NumPy 的陣列，如果想要對圖片進行裁切，就用索引的方式，將指定的區域取出即可：

# 裁切區域的 x 與 y 座標（左上角）
x = 100
y = 100

# 裁切區域的長度與寬度
w = 250
h = 150

# 裁切圖片
crop_img = img[y:y+h, x:x+w]

#接著使用 OpenCV 的 imshow 顯示裁切的結果：

# 顯示圖片
cv2.imshow("cropped", crop_img)

# 若要將裁切的圖片儲存下來，可使用 imwrite 函數：
# 寫入圖檔
cv2.imwrite('crop.jpg', crop_img)


cv2.waitKey(0)

'''



#Python 與 OpenCV 基本讀取、顯示與儲存圖片教學
#首先引入 NumPy 與 OpenCV 的 Python 模組：

import numpy as np
import cv2

# 讀取圖檔
img = cv2.imread(filename)

#以 cv2.imread 讀進來的資料，會儲存成一個 NumPy 的陣列，我們可以用 type 檢查一下：

'''
# 查看資料型態
type(img)

<class 'numpy.ndarray'>

此 NumPy 陣列的前兩個維度分別是圖片的高度與寬度，第三個維度則是圖片的 channel（RGB 彩色圖片的 channel 是 3，灰階圖片則為 1）。

以這個子來說，我們的原始圖片是一張 1920×1080 的彩色圖片，我們可以檢查一下這個 NumPy 陣列的大小：

img.shape

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

# 以灰階的方式讀取圖檔
img_gray = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 顯示圖片
cv2.imshow('My Image', img)

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
這裡 cv2.waitKey 函數是用來等待與讀取使用者按下的按鍵，而其參數是等待時間（單位為毫秒），若設定為 0 就表示持續等待至使用者按下按鍵為止，這樣當我們按下任意按鍵之後，就會呼叫 cv2.destroyAllWindows 關閉所有 OpenCV 的視窗。

如果在程式中有許多的 OpenCV 視窗，而我們只要關閉特定的視窗時，可以改用 cv2.destroyWindow 加上視窗名稱，關閉指定的視窗：

# 關閉 'My Image' 視窗
cv2.destroyWindow('My Image')

在預設的狀況下，以 cv2.imshow 所開啟的視窗會依據圖片來自動調整大小，但若是圖片太大、佔滿整個螢幕時，我們會希望可以自由縮放視窗的大小，這時候就可以使用 cv2.namedWindow 將視窗設定為 cv2.WINDOW_NORMAL：

# 讓視窗可以自由縮放大小
cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

使用 OpenCV 開啟的圖形視窗會類似這樣：

OpenCV 顯示圖片視窗

灰階的圖片也可以顯示，用法都相同：
'''

'''
OpenCV 顯示圖片視窗
寫入圖片檔案

若要將 NumPy 陣列中儲存的圖片寫入檔案，可以使用 OpenCV 的 cv2.imwrite：
'''
# 寫入圖檔
cv2.imwrite('output.jpg', img)

#cv2.imwrite 可透過圖片的副檔名來指定輸出的圖檔格式：

# 寫入不同圖檔格式
cv2.imwrite('output.png', img)
cv2.imwrite('output.tiff', img)

#輸出圖片檔案時，也可以調整圖片的品質或壓縮率：

# 設定 JPEG 圖片品質為 90（可用值為 0 ~ 100）
cv2.imwrite('output.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])

# 設定 PNG 壓縮層級為 5（可用值為 0 ~ 9）
cv2.imwrite('output.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 5])





import numpy as np
import cv2
from matplotlib import pyplot as plt

# 使用 OpenCV 讀取圖檔
img_bgr = cv2.imread(filename)

# 將 BGR 圖片轉為 RGB 圖片
img_rgb = img_bgr[:,:,::-1]

# 或是這樣亦可
# img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 使用 Matplotlib 顯示圖片
plt.imshow(img_rgb)
plt.show()


# 如果想要以黑白的方式呈現灰階圖片，可以自己設定 colormap：

# 使用 OpenCV 讀取灰階圖檔
img_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 使用 Matplotlib 顯示圖片
plt.imshow(img_gray, cmap = 'gray')
plt.show()



