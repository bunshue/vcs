"""
OpenCV 基本使用

顯示圖片

使用 cv2 顯示圖片

vs

使用 matplotlib 顯示圖片

讀取圖片 存圖


以 cv2.imread 讀進來的資料，會儲存成一個 NumPy 的陣列
查看資料型態
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

cv2.IMREAD_COLOR     彩色 + 無透明度 (預設)
cv2.IMREAD_GRAYSCALE 灰階
cv2.IMREAD_UNCHANGED 彩色 + 有透明度


"""

import cv2

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
# filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
# filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
'''
print('讀取圖片 並顯示')
image = cv2.imread(filename, 1)	  #讀取本機圖片, 0: 黑白圖片 1: 原色圖片
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap = 'gray', interpolation = 'bicubic')
plt.show()

print('------------------------------------------------------------')	#60個

""" OK
print('使用 cv2 顯示圖片')

# 檔案 => cv2影像
image = cv2.imread(filename)

cv2.imshow('Image', image)  #顯示圖片, 標題不支持中文

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()
"""
print('------------------------------------------------------------')	#60個

print('取得 OpenCV 版本')

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

print(cv2.__version__)
print(major_ver)
print(minor_ver)
print(subminor_ver)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'

print('開啟檔案成灰階影像')
# 檔案 => cv2影像 灰階
image = cv2.imread(filename, 0)
print("灰階 圖像屬性：")
print("image.shape=",image.shape)
print("image.size=",image.size)
print("image.dtype=",image.dtype)

print('開啟檔案成彩色影像')
# 檔案 => cv2影像 彩色
image = cv2.imread(filename)
#image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)	# -1 讀取本機圖片, 不改變顏色通道
#image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#  0 讀取本機圖片, 直接變成灰階
#image = cv2.imread(filename, cv2.IMREAD_COLOR)         #  1 讀取本機圖片, 改為BGR三通道(預設)

#print('cv2.IMREAD_UNCHANGED =', cv2.IMREAD_UNCHANGED)   # -1
#print('cv2.IMREAD_GRAYSCALE =', cv2.IMREAD_GRAYSCALE)   #  0
#print('cv2.IMREAD_COLOR =', cv2.IMREAD_COLOR)           #  1(預設)

print("彩色 圖像屬性：")
print("image.shape=",image.shape)
print("image.size=",image.size)
print("image.dtype=",image.dtype)

print('image.shape格式 :', type(image.shape))
print('image.shape內容 :', image.shape)

h = image.shape[0]    #高
w = image.shape[1]    #寬
d = image.shape[2]    #深
h, w, d = image.shape   #d為dimension d=3 全彩, d=1 灰階
print("寬 = ", w, ", 高 = ", h, ", D = ", d)

plt.subplot(121)
plt.title('顯示圖片 要轉RGB')

# plt.imshow(image)#直接顯示 影像錯誤 因為opencv的imread讀出來是BGR排列
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #圖片轉為灰階
plt.subplot(122)
plt.title('先轉灰階 再轉RGB')
plt.imshow(cv2.cvtColor(image_gray, cv2.COLOR_BGR2RGB))     #顯示圖片   #原圖轉黑白

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'

print('------------------------------------------------------------')	#60個

# 檔案 => cv2影像
image = cv2.imread(filename)

# 檔案 => cv2影像
image_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

print('------------------------------------------------------------')	#60個

# 檔案 => cv2影像
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

# 檔案 => cv2影像
image_bgr = cv2.imread(filename)

# 將 OpenCV 讀入的 BGR 格式轉為 Matplotlib 用的 RGB 格式，再交給 Matplotlib 顯示
image_rgb = image_bgr[:,:,::-1]     # 將 BGR 圖片轉為 RGB 圖片

# 或是這樣亦可
# image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# 使用 Matplotlib 顯示圖片
plt.imshow(image_rgb)
plt.show()

# 檔案 => cv2影像
image_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉為灰階

# 使用 Matplotlib 顯示圖片
plt.imshow(image_gray, cmap = 'gray')
plt.show()

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

# 檔案 => cv2影像
image_bgr = cv2.imread(filename)
image_rgb = image_bgr[:,:,::-1]     # 將 BGR 圖片轉為 RGB 圖片

# 或是這樣亦可
# image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.show()

print("------------------------------------------------------------")  # 60個

# 用 OpenCV 讀取並顯示圖片

# 等同於 plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) #BGR轉RGB再交由matplotlib顯示之
def aidemy_imshow(name, image):
    b, g, r = cv2.split(image)
    image = cv2.merge([r, g, b])
    plt.title(name)
    plt.imshow(image)
    plt.show()

cv2.imshow = aidemy_imshow

cv2.waitKey()
cv2.destroyAllWindows()

print('-----------------------------')

print("並列一圖")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
image1 = cv2.imread(filename)
image2 = cv2.hconcat([image1, image1, image1, image1, image1, image1])

plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('並列一圖')

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.show()

#三個影像橫向拼接 np.hstack
image_hstack = np.hstack((image, image, image))

#二個影像縱向拼接 np.vstack
image_vstack = np.vstack((image_hstack, image_hstack))

plt.imshow(cv2.cvtColor(image_vstack, cv2.COLOR_BGR2RGB))

plt.show()
'''
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/green_300X300.bmp"

# 檔案 => cv2影像
image = cv2.imread(filename)  # cv2讀取圖片, 自動轉成array

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 轉換為RGB
plt.subplot(121)
plt.imshow(rgb)
plt.title("cv影像轉RGB")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # 轉換為HSV
plt.subplot(122)
plt.imshow(hsv)
plt.title("cv影像轉HSV")

plt.show()

print("coordinate")
coordinate = rgb[131, 81]  # 輸入要取得顏色的指定座標
print(coordinate)

# print('取得cv影像陣列中的資料')
# print(array([255, 219,  79], dtype=uint8))

print("------------------------------------------------------------")  # 60個

print("測試CV視窗 : 全螢幕顯示一圖")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
filename = "C:/_git/vcs/_4.python/_data/bear.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)

window_name = "Full-screen"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cv2.imshow(window_name, image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("測試CV視窗 : 設定視窗大小並依視窗縮放影像")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
# filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'

# 檔案 => cv2影像
image = cv2.imread(filename)

window_name = window_name
cv2.namedWindow(window_name, 0)
cv2.resizeWindow(window_name, 640, 480)

# 設定視窗位置
x_st, y_st = 300, 100
cv2.moveWindow(window_name, x_st, y_st)

# 顯示圖片
cv2.imshow(window_name, image)

cv2.waitKey()
cv2.destroyAllWindows()

# 設定視窗參數, 若不設定, 即是 圖片滿框、不可調整大小
# 預設 flags == WINDOW_AUTOSIZE | WINDOW_KEEPRATIO |WINDOW_GUI_EXPANDED

# 可調整大小
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# WINDOW_FREERATIO 不 保持比例
# WINDOW_KEEPRATIO    保持比例

# 可調整大小 並 保持比例
# cv2.namedWindow('image', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)

print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
image = cv2.imread(filename)
b, g, r = cv2.split(image)
# print(b)
# print(g)
# print(r)

print("------------------------------------------------------------")  # 60個

print("OpenCV_03")

# 檔案 => cv2影像
image_r = cv2.imread(filename)
image_g = cv2.imread(filename)
image_b = cv2.imread(filename)

image_r[:, :, 0] = 0  # 將藍色設為 0
image_r[:, :, 1] = 0  # 將綠色設為 0

image_g[:, :, 0] = 0  # 將藍色設為 0
image_g[:, :, 2] = 0  # 將紅色設為 0

image_b[:, :, 1] = 0  # 將綠色設為 0
image_b[:, :, 2] = 0  # 將紅色設為 0

plt.subplot(131)
plt.imshow(cv2.cvtColor(image_r, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.imshow(cv2.cvtColor(image_g, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.imshow(cv2.cvtColor(image_b, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"

# 檔案 => cv2影像
image = cv2.imread(filename)

print("原圖 彩色 轉 灰階1通道")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # cv2影像 轉 灰階

print("灰階 轉 BGR3通道")
rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
print("rgb.shape=", rgb.shape)

plt.figure(
    num="new32 影像處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(131)
plt.title("原圖 彩色")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("灰階1通道")
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("BGR3通道")
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
# 檔案 => cv2影像
image = cv2.imread(filename)

print("原圖 BGR 轉 RGB")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(
    num="new33 影像處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121)
plt.title("原圖 B-G-R OK")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("原圖 BGR 轉 RGB NG")
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
# 檔案 => cv2影像
image = cv2.imread(filename)

bgra = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
b, g, r, a = cv2.split(bgra)
a[:, :] = 125
bgra125 = cv2.merge([b, g, r, a])
a[:, :] = 0
bgra0 = cv2.merge([b, g, r, a])

plt.figure(
    num="new36 影像處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("bgra")
plt.imshow(cv2.cvtColor(bgra, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("bgra125")
plt.imshow(cv2.cvtColor(bgra125, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("bgra0")
plt.imshow(cv2.cvtColor(bgra0, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
# 檔案 => cv2影像
image = cv2.imread(filename, 0)

plt.figure(
    num="new37 修改一部份資料",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

print("修改一部份資料 1")
for i in range(20, 60):  # y
    for j in range(20, 100):  # x
        image[i, j] = 255

print("修改一部份資料 2")
# 測試讀取、修改單個像素值
print("讀取像素點image.item(3,2)=", image.item(3, 2))
image.itemset((3, 2), 255)
print("修改後像素點image.item(3,2)=", image.item(3, 2))
# 測試修改一個區域的像素值
for i in range(100, 200):  # y
    for j in range(20, 60):  # x
        image.itemset((i, j), 220)

plt.subplot(222)
plt.title("修改後的圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

print("------------------------------")  # 30個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
# 檔案 => cv2影像
image = cv2.imread(filename)

plt.subplot(223)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

print("讀取image[0,0]=", image[0, 0])
print("讀取image[0,0,0]=", image[0, 0, 0])
print("讀取image[0,0,1]=", image[0, 0, 1])
print("讀取image[0,0,2]=", image[0, 0, 2])
print("讀取image[50,0]=", image[50, 0])
print("讀取image[100,0]=", image[100, 0])
# 區域1
for i in range(0, 50):
    for j in range(0, 100):
        for k in range(0, 3):
            image[i, j, k] = 255  # 白色
# 區域2
for i in range(50, 100):
    for j in range(0, 100):
        image[i, j] = [128, 128, 128]  # 灰色
# 區域3
for i in range(100, 150):
    for j in range(0, 100):
        image[i, j] = 0  # 黑色
# 區域4
print("讀取image.item(0, 0, 0) = ", image.item(0, 0, 0))
print("讀取image.item(0, 0, 1) = ", image.item(0, 0, 1))
print("讀取image.item(0, 0, 2) = ", image.item(0, 0, 2))
for i in range(200, 250):
    for j in range(0, 100):
        for k in range(0, 3):
            image.itemset((i, j, k), 255)  # 白色

print("修改後image.item(0, 0, 0) = ", image.item(0, 0, 0))
print("修改後image.item(0, 0, 1) = ", image.item(0, 0, 1))
print("修改後image.item(0, 0, 2) = ", image.item(0, 0, 2))
print("修改後image[0, 0] = ", image[0, 0])
print("修改後image[0, 0, 0] = ", image[0, 0, 0])
print("修改後image[0, 0, 1] = ", image[0, 0, 1])
print("修改後image[0, 0, 2] = ", image[0, 0, 2])
print("修改後image[50, 0] = ", image[50, 0])
print("修改後image[100, 0] = ", image[100, 0])

plt.subplot(224)
plt.title("修改後的圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
# 檔案 => cv2影像
a = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure(
    num="new38 擷取一塊處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(231)
plt.title("原圖")
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

print("擷取一塊出來, 並顯示之")
face = a[200:400, 200:380]  # h, w

plt.subplot(232)
plt.title("擷取一塊出來")
plt.imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))

print("將其中一塊亂碼化, 並顯示之")
x_st = 50
y_st = 50
w = 100
h = 180
face = np.random.randint(0, 256, (h, w, 3))
a[y_st : y_st + h, x_st : x_st + w] = face

plt.subplot(233)
plt.title("將其中一塊亂碼化")
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

print("------------------------------------------------------------")  # 60個

# A圖
filename1 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray2.bmp"
# 檔案 => cv2影像
lena = cv2.imread(filename1, cv2.IMREAD_UNCHANGED)

# A圖抓一塊貼到B圖上
plt.subplot(234)
plt.title("原圖")
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

# B圖
filename2 = "C:/_git/vcs/_4.python/_data/picture1.jpg"
# 檔案 => cv2影像
peony = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)

plt.subplot(235)
plt.title("原圖")
plt.imshow(cv2.cvtColor(peony, cv2.COLOR_BGR2RGB))

print("A圖抓一塊貼到B圖上")
face = lena[220:400, 250:350]
peony[160:340, 200:300] = face

plt.subplot(236)
plt.title("顯示修改後的圖")
plt.imshow(cv2.cvtColor(peony, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------")  # 30個

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)

x_st, y_st, w, h = 200, 50, 150, 200
image_cut = image[y_st : y_st + h, x_st : x_st + w]
print(image_cut.shape)

plt.imshow(cv2.cvtColor(image_cut, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

print("圖片翻轉 原圖")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
# 檔案 => cv2影像
image = cv2.imread(filename)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
image_flip = cv2.flip(image, -999)
image_flip2 = cv2.flip(image, -88)

plt.imshow(cv2.cvtColor(image_flip, cv2.COLOR_BGR2RGB))
plt.title("圖片翻轉")

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
