"""
OpenCV 基本使用

顯示圖片

使用 cv2 顯示圖片

vs

使用 matplotlib 顯示圖片

"""

import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'

print('------------------------------------------------------------')	#60個

print('取得 OpenCV 版本')

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

print(cv2.__version__)
print(major_ver)
print(minor_ver)
print(subminor_ver)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
gray = cv2.imread(filename, 0)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
color = cv2.imread(filename)

print("圖像gray屬性：")
print("gray.shape=",gray.shape)
print("gray.size=",gray.size)
print("gray.dtype=",gray.dtype)
print("圖像color屬性：")
print("color.shape=",color.shape)
print("color.size=",color.size)
print("color.dtype=",color.dtype)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'

image = cv2.imread(filename)	#讀取本機圖片
#image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)	# -1 讀取本機圖片, 不改變顏色通道
#image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#  0 讀取本機圖片, 直接變成灰階
#image = cv2.imread(filename, cv2.IMREAD_COLOR)         #  1 讀取本機圖片, 改為BGR三通道(預設)

print('cv2.IMREAD_UNCHANGED =', cv2.IMREAD_UNCHANGED)   # -1
print('cv2.IMREAD_GRAYSCALE =', cv2.IMREAD_GRAYSCALE)   #  0
print('cv2.IMREAD_COLOR =', cv2.IMREAD_COLOR)           #  1(預設)

print('image.shape格式 :', type(image.shape))
print('image.shape內容 :', image.shape)

h = image.shape[0]    #高
w = image.shape[1]    #寬
d = image.shape[2]    #深
h, w, d = image.shape   #d為dimension d=3 全彩, d=1 灰階
print("寬 = ", w, ", 高 = ", h, ", D = ", d)

cv2.imshow('Picture Viewer', image) #顯示圖片

#cv2.namedWindow('Picture Viewer')
window_name = 'Show Picture'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)


#實例化8位圖
image_empty = np.zeros(image.shape, dtype = np.uint8)   #依照原圖大小建立一個圖像的二維陣列
cv2.imshow("empty", image_empty)    #顯示圖片   #空圖, 全黑

image_copy = image.copy()
cv2.imshow("copy", image_copy)      #顯示圖片   #原圖拷貝

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #圖片轉為灰階
cv2.imshow("gray", image_gray)      #顯示圖片   #原圖轉黑白

#cv2.waitKey()
cv2.waitKey(0)
cv2.destroyAllWindows() #銷毀建立的物件

print('------------------------------------------------------------')	#60個

print('使用 cv2 顯示圖片')

image = cv2.imread(filename)	#讀取本機圖片

cv2.imshow('Peony', image)  #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

"""
cv2.imshow('視窗標題 不支持中文', image) #顯示圖片

cv2.waitKey(0)  #待user輸入內容
cv2.destroyAllWindows() #關閉視窗

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()
"""

print('------------------------------------------------------------')	#60個

print('使用 matplotlib 顯示圖片, 需先BGR轉RGB')

plt.title('使用 matplotlib 顯示圖片, 需先BGR轉RGB')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

image = cv2.imread(filename, 1)	  #讀取本機圖片, 0: 黑白圖片 1: 原色圖片
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap = 'gray', interpolation = 'bicubic')
plt.show()


print('------------------------------------------------------------')	#60個

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2a = 'C:/_git/vcs/_1.data/______test_files2/picture1a.jpg'
filename2b = 'C:/_git/vcs/_1.data/______test_files2/picture1b.jpg'

image1 = cv2.imread(filename1)	#讀取本機圖片
#image1 = cv2.imread(filename1, 1)
image2 = cv2.imread(filename1, 0)   #讀取本機圖片, 0: 黑白圖片 1: 原色圖片

image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
plt.imshow(image1)
#plt.title('xxxx')
plt.show()

image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
plt.imshow(image2)
#plt.title('xxxx')
plt.show()

print('------------------------------------------------------------')	#60個

"""
image = cv2.imread(filename, 1)	  #讀取本機圖片, 0: 黑白圖片 1: 原色圖片
cv2.imshow(window_name, image)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('xxxx')
plt.show()
"""

print('------------------------------------------------------------')	#60個

"""
print('------------------------------------------------------------')	#60個

#儲存檔案
image = cv2.imread(filename)	#讀取本機圖片

#寫入圖片檔案
#若要將 NumPy 陣列中儲存的圖片寫入檔案，可以使用 OpenCV 的 cv2.imwrite：
#cv2.imwrite 可透過圖片的副檔名來指定輸出的圖檔格式
# 寫入不同圖檔格式
cv2.imwrite('output.jpg', image)
cv2.imwrite('output.png', image)
cv2.imwrite('output.tiff', image)

#輸出圖片檔案時，也可以調整圖片的品質或壓縮率：

# 設定 JPEG 圖片品質為 90（可用值為 0 ~ 100）
cv2.imwrite('output.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 90])

# 設定 PNG 壓縮層級為 5（可用值為 0 ~ 9）
cv2.imwrite('output.png', image, [cv2.IMWRITE_PNG_COMPRESSION, 5])

print('------------------------------------------------------------')	#60個

#保存圖片 質量為5 和 100
print('存圖, 質量為5')
cv2.imwrite("./1.jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
print('存圖, 質量為100')
cv2.imwrite("./2.jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
#png壓縮大小
print('存圖, 壓縮為0')
cv2.imwrite("./3.png", image, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
print('存圖, 壓縮為9')
cv2.imwrite("./4.png", image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

#cv2.imwrite(filename2a, image1)
#cv2.imwrite(filename2b, image2, [int(cv2.IMWRITE_JPEG_QUALITY), 50])

#保存检测结果
#cv2.imwrite("re.jpg",image)

print('------------------------------------------------------------')	#60個


"""


print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'

print('------------------------------------------------------------')	#60個

image = cv2.imread(filename)	#讀取本機圖片

image_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

#以 cv2.imread 讀進來的資料，會儲存成一個 NumPy 的陣列

"""
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
"""

print('------------------------------------------------------------')	#60個

image_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉為灰階

image_gray = cv2.cvtColor(image_gray, cv2.COLOR_BGR2RGB)
plt.imshow(image_gray)
plt.show()


"""
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
"""

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


#cv2.imwrite('aaaaaaa.pgm', image) #無效????

