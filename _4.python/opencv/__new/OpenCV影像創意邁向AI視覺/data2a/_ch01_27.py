"""
OpenCV影像創意邁向AI視覺王者歸來

"""

print("------------------------------------------------------------")  # 60個

import cv2

filename1 = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"
filename3 = "C:/_git/vcs/_4.python/opencv/data/lena.jpg"
filename4 = "C:/_git/vcs/_1.data/______test_files1/ims01.bmp"

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

"""
img = cv2.imread(filename1)
cv2.imshow("Peony", img)
cv2.destroyWindow("Peony")  # 關閉視窗

ret_value = cv2.waitKey(0)  # 無限等待
cv2.destroyWindow("Peony")  # 關閉視窗

ret_value = cv2.waitKey(5000)  # 等待 5 秒
cv2.destroyWindow("Peony")  # 關閉視窗

ret_value = cv2.waitKey(0)  # 無限等待
if ret_value == ord("Q") or ret_value == ord("q"):
    cv2.destroyWindow("Peony")  # 關閉視窗

print("------------------------------------------------------------")  # 60個
"""
img = cv2.imread(filename1)
cv2.imshow("Peony", img)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch1_6.py

cv2.namedWindow("Peony1")  # 使用預設
cv2.namedWindow("Peony2", cv2.WINDOW_NORMAL)  # 可以調整大小
img1 = cv2.imread(filename1)  # 彩色讀取
img2 = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
cv2.imshow("Peony1", img1)
cv2.imshow("Peony2", img2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch1_6_1.py

cv2.namedWindow("Peony1")  # 使用預設
cv2.namedWindow("Peony2", cv2.WINDOW_NORMAL)  # 可以調整大小
img1 = cv2.imread(filename1)  # 彩色讀取
img2 = cv2.imread(filename1, 0)  # 灰色讀取
cv2.imshow("Peony1", img1)
cv2.imshow("Peony2", img2)

cv2.waitKey()
cv2.destroyWindow("Peony1")  # 刪除Peony1
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 讀取某點的灰階/RGB值

pt_y = 169
pt_x = 118

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
px = img[pt_y, pt_x]  # 讀px點

print(type(px))
print(f"BGR = {px}")

img = cv2.imread(filename1)  # 彩色讀取
px = img[pt_y, pt_x]  # 讀px點
print(type(px))
print(f"BGR = {px}")

pt_y = 169
pt_x = 118
img = cv2.imread(filename1)  # 彩色讀取
blue = img[pt_y, pt_x, 0]  # 讀 B 通道值
green = img[pt_y, pt_x, 1]  # 讀 G 通道值
red = img[pt_y, pt_x, 2]  # 讀 R 通道值
print(f"BGR = {blue}, {green}, {red}")

print("------------------------------------------------------------")  # 60個

# 修改影像的RGB值

pt_y = 169
pt_x = 118
img = cv2.imread(filename1)  # 彩色讀取
px = img[pt_y, pt_x]  # 讀取 px 點
print(f"更改前BGR = {px}")
px = [255, 255, 255]  # 修改 px 點
print(f"更改後BGR = {px}")

print("------------------------------------------------------------")  # 60個

# ch2_7.py

print("把影像的一塊改成藍色")

img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Before", img)
for y in range(img.shape[0] - 100, img.shape[0]):
    for x in range(img.shape[1] - 100, img.shape[1]):
        img[y, x] = [255, 0, 0]
cv2.imshow("After", img)

cv2.waitKey()
cv2.destroyAllWindows()

print("-------------------- ----------------------------------------")  # 60個
# OpenCV_03_Numpy影像
print("------------------------------------------------------------")  # 60個

# ch3_1.py

row1 = [1, 2, 3]
arr1 = np.array(row1, ndmin=2)
print(f"陣列維度 = {arr1.ndim}")
print(f"陣列外型 = {arr1.shape}")
print(f"陣列大小 = {arr1.size}")
print("陣列內容")
print(arr1)

row2 = [4, 5, 6]
arr2 = np.array([row1, row2], ndmin=2)
print(f"陣列維度 = {arr2.ndim}")
print(f"陣列外型 = {arr2.shape}")
print(f"陣列大小 = {arr2.size}")
print("陣列內容")
print(arr2)

print("------------------------------------------------------------")  # 60個

# ch3_2.py

x = np.array([[1, 2, 3], [4, 5, 6]])
print(f"陣列維度 = {x.ndim}")
print(f"陣列外型 = {x.shape}")
print(f"陣列大小 = {x.size}")
print("陣列內容")
print("x :", x)

print("------------------------------------------------------------")  # 60個

# ch3_3.py

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x[0][2])
print(x[1][2])
# 或是
print(x[0, 2])
print(x[1, 2])

print("------------------------------------------------------------")  # 60個

# 建立 640 X 480 之黑圖
fig = np.zeros((480, 640), dtype=np.uint8)
print(fig)
cv2.imshow("fig", fig)

cv2.waitKey()
cv2.destroyAllWindows()

# 建立 640 X 480 之白圖
fig = np.ones((480, 640), dtype=np.uint8) * 255
print(fig)
cv2.imshow("fig", fig)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch3_5.py

x1 = np.ones(3)
print("x1 :", x1)

x2 = np.ones((2, 3), dtype=np.uint8)
print("x2 :", x2)

print("------------------------------------------------------------")  # 60個

# ch3_6.py

x1 = np.empty(3)
print("x1 :", x1)

x2 = np.empty((2, 3), dtype=np.uint8)
print("x2 :", x2)

print("------------------------------------------------------------")  # 60個

# ch3_7.py

x1 = np.random.randint(10, 20)
print("回傳值是10(含)至20(不含)的單一隨機數")
print("x1 :", x1)

print("回傳一維陣列10個元素, 值是1(含)至5(不含)的隨機數")
x2 = np.random.randint(1, 5, 10)
print("x2 :", x2)

print("回傳單3*5陣列, 值是0(含)至10(不含)的隨機數")
x3 = np.random.randint(10, size=(3, 5))
print("x3 :", x3)

print("------------------------------------------------------------")  # 60個

# ch3_7_3.py

x = np.arange(16)
print("x :", x)
print(np.reshape(x, (4, -1)))

print("------------------------------------------------------------")  # 60個

# ch3_7_4.py

x = np.arange(16)
print("x :", x)
print(np.reshape(x, (-1, 8)))

print("------------------------------------------------------------")  # 60個

# ch3_8.py

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"陣列元素如下 : {x} ")
print(f"x[2:]       = {x[2:]}")
print(f"x[:2]       = {x[:3]}")
print(f"x[0:3]      = {x[0:3]}")
print(f"x[1:4]      = {x[1:4]}")
print(f"x[0:9:2]    = {x[0:9:2]}")
print(f"x[-1]       = {x[-1]}")
print(f"x[::2]      = {x[::2]}")
print(f"x[2::3]     = {x[2::3]}")
print(f"x[:]        = {x[:]}")
print(f"x[::]       = {x[::]}")
print(f"x[-3:-7:-1] = {x[-3:-7:-1]}")

print("------------------------------------------------------------")  # 60個

# ch3_9.py

print("測試 copy=True/False")

print("測試 copy=True, 完全複製, 不連動")
x1 = np.array([0, 1, 2, 3, 4, 5])
x2 = np.array(x1, copy=True)

print("x1 :", x1)
print("x2 :", x2)
x2[0] = 9
print("x1 :", x1)
print("x2 :", x2)

print("測試 copy=False, 會連動")
x1 = np.array([0, 1, 2, 3, 4, 5])
x2 = np.array(x1, copy=False)

print("x1 :", x1)
print("x2 :", x2)
x2[0] = 9
print("x1 :", x1)
print("x2 :", x2)

print("預設, 無copy=True/False, 就是True, 完全複製, 不連動")
x1 = np.array([0, 1, 2, 3, 4, 5])
x2 = np.array(x1)

print("x1 :", x1)
print("x2 :", x2)
x2[0] = 9
print("x1 :", x1)
print("x2 :", x2)

print("------------------------------------------------------------")  # 60個

# ch3_10.py

x1 = np.array([0, 1, 2, 3, 4, 5])
x2 = x1.copy()

print("x1 :", x1)
print("x2 :", x2)
x2[0] = 9
print("x1 :", x1)
print("x2 :", x2)

print("------------------------------------------------------------")  # 60個

# ch3_11.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
print("x4 :", x4)

print("------------------------------------------------------------")  # 60個

# ch3_12.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
x5 = np.array([x4, x4])
print("x5 :", x5)

print("------------------------------------------------------------")  # 60個

# ch3_13.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
print(f"x4[2][1] = {x4[2][1]}")
print(f"x4[1][3] = {x4[1][3]}")

print("------------------------------------------------------------")  # 60個

# ch3_13_1.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
print(f"x4[2,1] = {x4[2,1]}")
print(f"x4[1,3] = {x4[1,3]}")

print("------------------------------------------------------------")  # 60個

# ch3_14.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
x5 = np.array([x4, x4])
print(f"x5[0][2][1] = {x5[0][2][1]}")
print(f"x5[0][1][3] = {x5[0][1][3]}")
print(f"x5[1][0][1] = {x5[1][0][1]}")
print(f"x5[1][1][4] = {x5[1][1][4]}")

print("------------------------------------------------------------")  # 60個

# ch3_14_1.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
x5 = np.array([x4, x4])
print(f"x5[0,2,1] = {x5[0,2,1]}")
print(f"x5[0,1,3] = {x5[0,1,3]}")
print(f"x5[1,0,1] = {x5[1,0,1]}")
print(f"x5[1,1,4] = {x5[1,1,4]}")

print("------------------------------------------------------------")  # 60個

# ch3_15.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x = np.array([x1, x2, x3])
print("x[:,:]   = 結果是二維陣列")  # 結果是二維陣列
print(x[:, :])

print("x[2,:4]  = 結果是一維陣列")  # 結果是一維陣列
print(x[2, :4])

print("x[:2,:1] = 結果是二維陣列")  # 結果是二維陣列
print(x[:2, :1])

print("x[:,4:]  =  結果是二維陣列")  # 結果是二維陣列
print(x[:, 4:])

print("x[:,4]   =  結果是一維陣列")  # 結果是一維陣列
print(x[:, 4])

print("------------------------------------------------------------")  # 60個

# ch3_16.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x = np.array([x1, x2, x3])
print("x[:2,4]  = 結果是一維陣列")  # 結果是一維陣列
print(x[:2, 4])

print("------------------------------------------------------------")  # 60個

# ch3_17.py

x1 = np.arange(4).reshape(2, 2)
print(f"陣列 1 \n{x1}")
x2 = np.arange(4, 8).reshape(2, 2)
print(f"陣列 2 \n{x2}")
x = np.vstack((x1, x2))
print(f"合併結果 \n{x}")

print("------------------------------------------------------------")  # 60個

# ch3_18.py

x1 = np.arange(4).reshape(2, 2)
print(f"陣列 1 \n{x1}")
x2 = np.arange(4, 8).reshape(2, 2)
print(f"陣列 2 \n{x2}")
x = np.hstack((x1, x2))
print(f"合併結果 \n{x}")

print("------------------------------------------------------------")  # 60個
# OpenCV_04_色彩空間
print("------------------------------------------------------------")  # 60個

# ch4_1.py

img = cv2.imread("view.jpg")  # BGR讀取
cv2.imshow("BGR Color Space", img)

print("BGR 轉 RGB")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR 轉 RGB
cv2.imshow("RGB Color Space", img_rgb)

print("RGB 轉 BGR")
img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)  # RGB 轉 BGR
cv2.imshow("BGR Color Space", img_bgr)

print("BGR 轉 GRAY")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # BGR轉GRAY
cv2.imshow("GRAY Color Space", img_gray)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_5.py

pt_x = 169
pt_y = 118
img = cv2.imread(filename1)  # BGR讀取

print("BGR 轉 GRAY")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY Color Space", img_gray)
px = img_gray[pt_x, pt_y]
print(f"Gray Color 通道值 = {px}")

print("GRAY 轉 BGR")
img_color = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
cv2.imshow("BGR Color Space", img_gray)
px = img_color[pt_x, pt_y]
print(f"BGR Color  通道值 = {px}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_6.py

img = cv2.imread(filename1)  # BGR讀取
cv2.imshow("BGR Color Space", img)

print("BGR 轉 HSV")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR轉HSV
cv2.imshow("HSV Color Space", img_hsv)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_7.py

filename = "C:/_git/vcs/_4.python/opencv/data/rgb512.bmp"

image = cv2.imread(filename)
cv2.imshow("bgr", image)

blue, green, red = cv2.split(image)
cv2.imshow("blue", blue)
cv2.imshow("green", green)
cv2.imshow("red", red)

print(f"B通道影像屬性 shape = {blue.shape}")
print("列印B通道內容")
print(blue)

print(f"BGR  影像 : {image.shape}")
print(f"B通道影像 : {blue.shape}")
print(f"G通道影像 : {green.shape}")
print(f"R通道影像 : {red.shape}")

print("B通道內容 : ")
print(blue)
print("G通道內容 : ")
print(green)
print("R通道內容 : ")
print(red)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_9.py

image = cv2.imread(filename1)
cv2.imshow("bgr", image)

print("BGR 轉 HSV")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hue, saturation, value = cv2.split(hsv_image)
cv2.imshow("hsv", hue)
cv2.imshow("saturation", saturation)
cv2.imshow("value", value)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_10.py

image = cv2.imread(filename1)
blue, green, red = cv2.split(image)
bgr_image = cv2.merge([blue, green, red])  # 依據 B G R 順序合併
cv2.imshow("B -> G -> R ", bgr_image)

rgb_image = cv2.merge([red, green, blue])  # 依據 R G B 順序合併
cv2.imshow("R -> G -> B ", rgb_image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_11.py

image = cv2.imread(filename1)

print("BGR 轉 HSV")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(hsv_image)
hsv_image = cv2.merge([hue, saturation, value])  # 依據 H S V 順序合併

cv2.imshow("The Image", image)
cv2.imshow("The Merge Image", hsv_image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_12.py

image = cv2.imread(filename1)

print("BGR 轉 HSV")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv, saturation, value = cv2.split(hsv_image)
hsv[:, :] = 200  # 修訂 hsv 內容
hsv_image = cv2.merge([hsv, saturation, value])  # 依據H S V順序合併

print("HSV 轉 BGR")
new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)  # HSV 轉 BGR

cv2.imshow("The Image", image)
cv2.imshow("The New Image", new_image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_12_1.py

image = cv2.imread(filename1)

print("BGR 轉 HSV")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv, saturation, value = cv2.split(hsv_image)
hsv.fill(200)  # 修訂 hsv 內容
hsv_image = cv2.merge([hsv, saturation, value])  # 依據H S V順序合併

print("HSV 轉 BGR")
new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)  # HSV 轉 BGR

cv2.imshow("The Image", image)
cv2.imshow("The New Image", new_image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_13.py

image = cv2.imread(filename1)

print("BGR 轉 HSV")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv, saturation, value = cv2.split(hsv_image)
saturation.fill(255)  # 修訂 hsv 內容
hsv_image = cv2.merge([hsv, saturation, value])  # 依據H S V順序合併

print("HSV 轉 BGR")
new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)  # HSV 轉 BGR

cv2.imshow("The Image", image)
cv2.imshow("The New Image", new_image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_14.py

image = cv2.imread(filename1)

print("BGR 轉 HSV")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv, saturation, value = cv2.split(hsv_image)
value.fill(255)  # 修訂 value 內容
hsv_image = cv2.merge([hsv, saturation, value])  # 依據H S V順序合併

print("HSV 轉 BGR")
new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)  # HSV 轉 BGR

cv2.imshow("The Image", image)
cv2.imshow("The New Image", new_image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_15.py

image = cv2.imread(filename1)
cv2.imshow("The Image", image)  # 顯示BGR影像

print("BGR 轉 BGRA")
bgra_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

b, g, r, a = cv2.split(bgra_image)
print("列出轉成含A通道影像物件後的alpha值")
print(a)

a[:, :] = 32  # 修訂alpha內容
a32_image = cv2.merge([b, g, r, a])  # alpha=32影像物件
cv2.imshow("The a32 Image", a32_image)  # 顯示alpha=32影像

a.fill(128)  # 修訂alpha內容
a128_image = cv2.merge([b, g, r, a])  # alpha=128影像物件
cv2.imshow("The a128 Image", a128_image)  # 顯示alpha=128影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_05_建立空影像
print("------------------------------------------------------------")  # 60個

width, height = 640, 480  # 影像寬, 影像高

# 建立GRAY影像陣列, 黑色
image = np.zeros((height, width), np.uint8)
cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

# 建立GRAY影像陣列, 白色
image = np.zeros((height, width), np.uint8)
image.fill(255)  # 元素內容改為白色 255
cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

# 建立GRAY影像陣列, 白色
image = np.ones((height, width), np.uint8) * 255
cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_4.py

width, height = 640, 480  # 影像寬, 影像高

# 建立GRAY影像陣列, 黑色
image = np.zeros((height, width), np.uint8)

# 某塊塗為白色
image[40:120, 70:210] = 255  # 高在40至120之間,寬在70至210之間,設為255

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_5.py

width, height = 640, 480  # 影像寬, 影像高

# 建立GRAY影像陣列, 黑色
image = np.zeros((height, width), np.uint8)

print("某些塗為白色")

for y in range(0, height, 20):
    image[y : y + 10, :] = 255  # 白色厚度是10
cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_6.py

width, height = 640, 480  # 影像寬, 影像高

# 使用random.randint()建立GRAY影像陣列
image = np.random.randint(256, size=[height, width], dtype=np.uint8)
cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_7.py

height = 160  # 影像高
width = 280  # 影像寬
width, height = 640, 480  # 影像寬, 影像高

# 建立BGR影像陣列
image = np.zeros((height, width, 3), np.uint8)
image[:, :, 0] = 255  # 建立 B 通道像素值
cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_8.py

height = 160  # 影像高
width = 280  # 影像寬
width, height = 640, 480  # 影像寬, 影像高

# 建立BGR影像陣列
image = np.zeros((height, width, 3), np.uint8)
blue_image = image.copy()
blue_image[:, :, 0] = 255  # 建立 B 通道像素值
cv2.imshow("blue image", blue_image)  # 顯示blue image影像

green_image = image.copy()
green_image[:, :, 1] = 255  # 建立 G 通道像素值
cv2.imshow("green image", green_image)  # 顯示green image影像

red_image = image.copy()
red_image[:, :, 2] = 255  # 建立 R 通道像素值
cv2.imshow("red image", red_image)  # 顯示red image影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_9.py

height = 160  # 影像高
width = 280  # 影像寬
width, height = 640, 480  # 影像寬, 影像高

# 使用random.randint()建立GRAY影像陣列
image = np.random.randint(256, size=[height, width, 3], dtype=np.uint8)
cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_10.py

width, height = 640, 480  # 影像寬, 影像高

image = np.zeros((height, width, 3), np.uint8)
image[0:50, :, 0] = 255  # blue
image[50:100, :, 1] = 255  # green
image[100:150, :, 2] = 255  # red
cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_06_影像處理
print("------------------------------------------------------------")  # 60個

# ch6_1.py

# 建立GRAY影像陣列
image = np.zeros((5, 12), np.uint8)
print(f"修改前 image=\n{image}")  # 顯示修改前GRAY影像
print(f"image[1,4] = {image[1, 4]}")  # 列出特定像素點的內容

image[1, 4] = 255  # 修改像素點的內容
print(f"修改後 image=\n{image}")  # 顯示修改後的GRAY影像
print(f"image[1,4] = {image[1, 4]}")  # 列出特定像素點的內容

print("------------------------------------------------------------")  # 60個

# ch6_2.py

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
cv2.imshow("Before", img)  # 顯示修改前影像img
for y in range(30, 80):  # 修改影像
    for x in range(150, 250):
        img[y, x] = 127
cv2.imshow("After", img)  # 顯示修改後影像img

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch6_3.py

# 建立藍色blue底的彩色影像陣列
blue_img = np.zeros((2, 3, 3), np.uint8)
blue_img[:, :, 0] = 255  # 填滿藍色
print(f"blue image =\n{blue_img}")  # 顯示blue_img影像陣列

# 建立綠色green底的彩色影像陣列
green_img = np.zeros((2, 3, 3), np.uint8)
green_img[:, :, 1] = 255  # 填滿綠色
print(f"green image =\n{green_img}")  # 顯示green_img影像陣列

# 建立紅色red底的彩色影像陣列
red_img = np.zeros((2, 3, 3), np.uint8)
red_img[:, :, 2] = 255  # 填滿紅色
print(f"red image =\n{red_img}")  # 顯示red_img影像陣列

print("------------------------------------------------------------")  # 60個

# ch6_4.py

width, height = 640, 480  # 影像寬, 影像高

# 建立藍色blue底的彩色影像陣列
blue_img = np.zeros((height, width, 3), np.uint8)
blue_img[:, :, 0] = 255  # 填滿藍色
print(f"blue image =\n{blue_img}")  # 顯示blue_img影像陣列
cv2.imshow("Blue Image", blue_img)  # 顯示藍色影像

# 建立綠色green底的彩色影像陣列
green_img = np.zeros((height, width, 3), np.uint8)
green_img[:, :, 1] = 255  # 填滿綠色
print(f"green image =\n{green_img}")  # 顯示green_img影像陣列
cv2.imshow("Green Image", green_img)  # 顯示綠色影像

# 建立紅色red底的彩色影像陣列
red_img = np.zeros((height, width, 3), np.uint8)
red_img[:, :, 2] = 255  # 填滿紅色
print(f"red image =\n{red_img}")  # 顯示red_img影像陣列
cv2.imshow("Red Image", red_img)  # 顯示紅色影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch6_5.py

# 建立藍色blue底的彩色影像陣列
blue = np.zeros((2, 3, 3), np.uint8)
blue[:, :, 0] = 255  # 填滿藍色
print(f"blue =\n{blue}")  # 列印影像陣列
# 列印修訂前的像素點
print(f"blue[0,1] = {blue[0,1]}")

blue[0, 1] = [50, 100, 150]  # 修訂像素點
print("修訂後")
# 列印修訂後的像素點
print(f"blue =\n{blue}")  # 列印影像陣列

print("------------------------------------------------------------")  # 60個

# ch6_6.py

# 建立藍色blue底的彩色影像陣列
blue = np.zeros((2, 3, 3), np.uint8)
blue[:, :, 0] = 255  # 填滿藍色
print(f"blue =\n{blue}")  # 列印影像陣列
# 列印修訂前的像素點
print(f"blue[0,1,2] = {blue[0,1,2]}")

blue[0, 1, 2] = 50  # 修訂像素點的單一通道
print("修訂後")
# 列印修訂後的像素點
print(f"blue =\n{blue}")  # 列印影像陣列
print(f"blue[0,1,2] = {blue[0,1,2]}")

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename1)  # 彩色讀取

print(f"修改前img[115,110] = {img[115,110]}")
print(f"修改前img[125,110] = {img[125,110]}")
print(f"修改前img[135,110] = {img[135,110]}")
# 紫色長條
img[115:125, 110:210] = [255, 0, 255]
# 白色長條
for z in range(125, 135):  # 修改影像:一次一個通道值
    for y in range(110, 210):
        for x in range(0, 3):  # 一次一個通道值
            img[z, y, x] = 255  # 白色取代
# 黃色長條
for y in range(135, 145):  # 修改影像
    for x in range(110, 210):
        img[y, x] = [0, 255, 255]  # 黃色取代
cv2.imshow("After", img)  # 顯示修改後影像img
print(f"修改後img[115,110] = {img[115,110]}")
print(f"修改後img[125,110] = {img[125,110]}")
print(f"修改後img[135,110] = {img[135,110]}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch6_8.py

# 看不出差異

img = cv2.imread("street.png", cv2.IMREAD_UNCHANGED)  # PNG讀取
cv2.imshow("Before", img)  # 顯示修改前影像img
print(f"修改前img[10,50] = {img[10,50]}")
print(f"修改前img[50,99] = {img[50,99]}")

for z in range(0, 200):  # 一次一個修改alpha通道值
    for y in range(0, 200):
        img[z, y, 3] = 128  # 修改alpha通道值

print(f"修改後img[10,50] = {img[10,50]}")
print(f"修改後img[50,99] = {img[50,99]}")

cv2.imshow("After", img)  # 顯示修改前影像img

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch6_8_1.py

img = cv2.imread("street.png", cv2.IMREAD_UNCHANGED)  # PNG讀取
cv2.imshow("Before", img)  # 顯示修改前影像img
print(f"修改前img[10,50] = {img[10,50]}")
print(f"修改前img[50,99] = {img[50,99]}")

img[0:200, 0:200, 3] = 128
print(f"修改後img[10,50] = {img[10,50]}")
print(f"修改後img[50,99] = {img[50,99]}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch6_9.py

image = np.random.randint(0, 200, size=[3, 5], dtype=np.uint8)
print(f"image = \n{image}")
print(f"修改前image.item(1,3) = {image.item(1,3)}")
image.itemset((1, 3), 255)  # 修訂內容為 255

print(f"修改後image =\n{image}")
print(f"修改後image.item(1,3) = {image.item(1,3)}")

print("------------------------------------------------------------")  # 60個

# ch6_10.py

print("灰階讀取, 部分塗成白色")

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
cv2.imshow("Before", img)  # 顯示修改前影像img
for y in range(120, 140):  # 修改影像
    for x in range(110, 210):
        img.itemset((y, x), 255)
cv2.imshow("After", img)  # 顯示修改後影像img

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch6_11.py

# 建立藍色blue底的彩色影像陣列
blue = np.zeros((2, 3, 3), np.uint8)
blue[:, :, 0] = 255  # 填滿藍色
print(f"blue =\n{blue}")  # 列印影像陣列
# 列印修訂前的像素點
print(f"blue[0,1,2] = {blue.item(0,1,2)}")

blue.itemset((0, 1, 2), 50)  # 修訂像素點的單一通道
print("修訂後")
# 列印修訂後的像素點
print(f"blue =\n{blue}")  # 列印影像陣列
print(f"blue[0,1,2] = {blue.item(0,1,2)}")

print("------------------------------------------------------------")  # 60個

# ch6_12.py

img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Before", img)  # 顯示修改前影像img
print(f"修改前img[115,110,1] = {img.item(115,110,1)}")
print(f"修改前img[125,110,1] = {img.item(125,110,1)}")
print(f"修改前img[135,110,1] = {img.item(135,110,1)}")
# 白色長條
for z in range(115, 145):  # 修改影像:一次一個通道值
    for y in range(110, 210):
        for x in range(0, 3):  # 一次一個通道值
            img.itemset((z, y, x), 255)  # 白色取代
cv2.imshow("After", img)  # 顯示修改後影像img
print(f"修改後img[115,110,1] = {img.item(115,110,1)}")
print(f"修改後img[125,110,1] = {img.item(125,110,1)}")
print(f"修改後img[135,110,1] = {img.item(135,110,1)}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch6_13.py
img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Peony", img)

face = img[70:220, 90:240]  # ROI, 先高後寬
cv2.imshow("Face", face)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch6_14.py

img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Peony", img)
# ROI大小區塊建立馬賽克
face = np.random.randint(0, 256, size=(190, 170, 3))  # 馬賽克效果
img[30:220, 80:250] = face  # ROI, 先高後寬
cv2.imshow("Face", img)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch6_15.py

filenamea = "C:/_git/vcs/_4.python/opencv/data/lena.jpg"
filenameb = "C:/_git/vcs/_4.python/opencv/data/contours.bmp"

lena = cv2.imread(filenamea)  # 彩色讀取, 大圖
img = cv2.imread(filenameb)  # 彩色讀取, 小圖

face = img[130:420, 280:550]  # ROI, 先高後寬
lena[130:420, 120:390] = face  # 複製到lena影像

cv2.imshow("Image", lena)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_08_影像計算
print("------------------------------------------------------------")  # 60個

# ch8_1.py

src1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
src2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
res = cv2.add(src1, src2)
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {src1+src2}")

print("------------------------------------------------------------")  # 60個

# ch8_2.py

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
cv2.imshow("Peony1", img)

res = cv2.add(img, img)
cv2.imshow("Peony2", res)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch8_3.py

img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Peony1", img)

res = cv2.add(img, img)  # 調整亮度結果
cv2.imshow("Peony2", res)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch8_3_1.py

value = 20  # 亮度調整值
img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Peony1", img)

coff = np.ones(img.shape, dtype=np.uint8) * value
res = cv2.add(img, coff)  # 調整亮度結果
cv2.imshow("Peony2", res)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch8_4.py

src1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
src2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
res = src1 + src2
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {src1+src2}")

print("------------------------------------------------------------")  # 60個

# ch8_5.py

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
cv2.imshow("Peony1", img)

res1 = cv2.add(img, img)
cv2.imshow("Peony2", res1)

res2 = img + img
cv2.imshow("Peony3", res2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch8_6.py

img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Peony1", img)

res1 = cv2.add(img, img)
cv2.imshow("Peony2", res1)

res2 = img + img
cv2.imshow("Peony3", res2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch8_7.py

width, height = 640, 480  # 影像寬, 影像高

b = np.zeros((height, width, 3), np.uint8)  # b影像
g = np.zeros((height, width, 3), np.uint8)  # g影像
r = np.zeros((height, width, 3), np.uint8)  # r影像
b[:, :, 0] = 255  # 設定藍色
g[:, :, 1] = 255  # 設定綠色
r[:, :, 2] = 255  # 設定紅色
cv2.imshow("B channel", b)
cv2.imshow("G channel", g)
cv2.imshow("R channel", r)

img1 = cv2.add(b, g)  # b + g影像
cv2.imshow("B + G", img1)
img2 = cv2.add(g, r)  # g + r影像
cv2.imshow("G + R", img2)
img3 = cv2.add(img1, r)  # b + g + r影像
cv2.imshow("B + G + R", img3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch8_8.py

img1 = np.ones((4, 5), dtype=np.uint8) * 8
img2 = np.ones((4, 5), dtype=np.uint8) * 9

mask = np.zeros((4, 5), dtype=np.uint8)
mask[1:3, 1:4] = 255  # 設定mask, 先高後寬

dst = np.random.randint(0, 256, (4, 5), np.uint8)

print("img1 = \n", img1)
print("img2 = \n", img2)
print("mask = \n", mask)
print("最初值 dst =\n", dst)
dst = cv2.add(img1, img2, mask=mask)
print("結果值 dst =\n", dst)

print("------------------------------------------------------------")  # 60個

# ch8_8_1.py

width, height = 640, 480  # 影像寬, 影像高

img1 = np.zeros((height, width, 3), np.uint8)  # 建立img1影像
img1[:, :, 1] = 255
cv2.imshow("img1", img1)

img2 = np.zeros((height, width, 3), np.uint8)  # 建立img2影像
img2[:, :, 2] = 255
cv2.imshow("img2", img2)

m = np.zeros((height, width, 1), np.uint8)  # 建立mask(m)影像
m[50:150, 100:200, :] = 255  # 建立 ROI
cv2.imshow("mask", m)

img3 = cv2.add(img1, img2)  # 不含mask的影像相加
cv2.imshow("img1 + img2", img3)

img4 = cv2.add(img1, img2, mask=m)  # 含mask的影像相加
cv2.imshow("img1 + img2 + mask", img4)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch8_9.py

src1 = np.ones((2, 3), dtype=np.uint8) * 10  # 影像 src1
src2 = np.ones((2, 3), dtype=np.uint8) * 50  # 影像 src2
alpha = 1
beta = 0.5
gamma = 5
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)  # 加權和
print(f"dst = \n {dst}")

print("------------------------------------------------------------")  # 60個

""" NG
# ch8_10.py

src1 = cv2.imread("lake.jpg")  # 影像 src1
cv2.imshow("lake", src1)
src2 = cv2.imread("geneva.jpg")  # 影像 src2
cv2.imshow("geneva.jpg", src2)
alpha = 1
beta = 0.2
gamma = 1
dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)  # 加權和
cv2.imshow("lake+geneva", dst)  # 顯示結果

cv2.waitKey()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
# OpenCV_09_閾值處理
print("------------------------------------------------------------")  # 60個

# ch9_1.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch9_2.py

maxval = 255  # 定義像素最大值

src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)
cv2.imshow("Before", src)

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("threshold 127", dst)

thresh = 80  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("threshold 80", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_3.py

maxval = 255  # 定義像素最大值

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
src = cv2.imread(filename2)
cv2.imshow("Src", src)

ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("threshold 127", dst)

thresh = 80  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("threshold 80", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_4.py

maxval = 255  # 二值化的極大值

src = cv2.imread("numbers.jpg")
cv2.imshow("Src", src)

thresh = 127  # 閾值 = 10
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("threshold 127", dst)

thresh = 10  # 更改閾值 = 10
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("threshold 10", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_5.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch9_6.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("Src", src)

cv2.imshow("threshold 127", dst)

thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("threshold 80", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_7.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread(filename2)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("Src", src)

cv2.imshow("threshold 127", dst)

thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("threshold 80", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_8.py

src = cv2.imread("numbers.jpg")
thresh = 127  # 閾值 = 10
maxval = 255  # 二值化的極大值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("Src", src)

cv2.imshow("threshold 127", dst)

thresh = 10  # 更改閾值 = 10
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("threshold 10", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_9.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch9_10.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
cv2.imshow("Src", src)

cv2.imshow("threshold 127", dst)

thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
cv2.imshow("threshold 80", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_11.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread(filename2)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
cv2.imshow("Src", src)
cv2.imshow("threshold 127", dst)

thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
cv2.imshow("threshold 127", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_12.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch9_13.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
cv2.imshow("Src", src)

cv2.imshow("threshold 127", dst)

thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
cv2.imshow("threshold 80", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_14.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread(filename2)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
cv2.imshow("Src", src)

cv2.imshow("threshold 127", dst)

thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
cv2.imshow("threshold 80", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_15.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch9_16.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
cv2.imshow("Src", src)

cv2.imshow("threshold 127", dst)

thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
cv2.imshow("threshold 80", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_17.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread(filename2)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
cv2.imshow("Src", src)

cv2.imshow("threshold 127", dst)

thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
cv2.imshow("threshold 80", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_18.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.ones((3, 4), dtype=np.uint8) * 120  # 設定陣列是 120
src[0:2, 0:2] = 108  # 設定陣列區間為 0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch9_19.py

thresh = 0  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.ones((3, 4), dtype=np.uint8) * 120  # 設定陣列是 120
src[0:2, 0:2] = 108  # 設定陣列區間為 0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch9_20.py

src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
thresh = 127  # 定義閾值 = 127
maxval = 255  # 定義像素最大值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("Src - 127", dst)  # threshold = 127
thresh = 0  # 定義閾值 = 0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Dst - Otsu", dst)  # Otsu
print(f"threshold = {ret}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_21.py

src = cv2.imread("school.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取
thresh = 127  # 閾值
maxval = 255  # 定義像素最大值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
# 自適應閾值計算方法為ADAPTIVE_THRESH_MEAN_C
dst_mean = cv2.adaptiveThreshold(
    src, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5
)
# 自適應閾值計算方法為ADAPTIVE_THRESH_GAUSSIAN_C
dst_gauss = cv2.adaptiveThreshold(
    src, maxval, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5
)
cv2.imshow("src", src)
cv2.imshow("THRESH_BINARY", dst)  # 顯示二值化處理影像
cv2.imshow("ADAPTIVE_THRESH_MEAN_C", dst_mean)  # 顯示自適應閾值結果
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", dst_gauss)  # 顯示自適應閾值結果

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_22.py

img = cv2.imread(filename3, cv2.IMREAD_GRAYSCALE)
cv2.imshow("Lena", img)

row, column = img.shape
x = np.zeros((row, column, 8), dtype=np.uint8)

for i in range(8):
    x[:, :, i] = 2**i  # 填上權重

result = np.zeros((row, column, 8), dtype=np.uint8)

for i in range(8):
    result[:, :, i] = cv2.bitwise_and(img, x[:, :, i])
    mask = result[:, :, i] > 0  # 影像邏輯值
    result[mask] = 255  # True的位置填255
    cv2.imshow(str(i), result[:, :, i])

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_23.py

jk = cv2.imread(filename3, cv2.IMREAD_GRAYSCALE)
cv2.imshow("Lena", jk)

row, column = jk.shape  # 取得列高和欄寬

h7 = np.ones((row, column), dtype=np.uint8) * 254  # 建立像素值是254的影像
cv2.imshow("254", h7)  # 顯示像素值是254的影像

new_jk = cv2.bitwise_and(jk, h7)  # 原始影像最低有效位元是 0
cv2.imshow("New Lena", new_jk)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_24.py

jk = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("JK Hung", jk)

row, column = jk.shape  # 取得列高和欄寬

h7 = np.ones((row, column), dtype=np.uint8) * 254  # 建立像素值是254的影像
tmp_jk = cv2.bitwise_and(jk, h7)  # 原始影像最低有效位元是 0
watermark = cv2.imread("copyright.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Copy Right", watermark)  # 顯示浮水印影像

ret, wm = cv2.threshold(watermark, 0, 1, cv2.THRESH_BINARY)
# 浮水印影像嵌入最低有效位元是 0的原始影像
new_jk = cv2.bitwise_or(tmp_jk, wm)
cv2.imshow("New JK", new_jk)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_25.py

jk = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("JK Hung", jk)

row, column = jk.shape  # 取得列高和欄寬
h7 = np.ones((row, column), dtype=np.uint8) * 254  # 建立像素值是254的影像
tmp_jk = cv2.bitwise_and(jk, h7)  # 原始影像最低有效位元是 0
watermark = cv2.imread("copyright.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("original watermark", watermark)  # 顯示浮水印影像

ret, wm = cv2.threshold(watermark, 0, 1, cv2.THRESH_BINARY)

new_jk = cv2.bitwise_or(tmp_jk, wm)  # 浮水印影像嵌入原始影像
cv2.imshow("New JK", new_jk)

# 擷取浮水印
h0 = np.ones((row, column), dtype=np.uint8)
wm = cv2.bitwise_and(new_jk, h0)
ret, dst = cv2.threshold(wm, 0, 255, cv2.THRESH_BINARY)
cv2.imshow("result Watermark", dst)  # 顯示浮水印

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_10_影像的幾何變換
print("------------------------------------------------------------")  # 60個

print("cv2.resize()")

src = cv2.imread(filename1)
cv2.imshow("Src", src)
print(f"src.shape = {src.shape}")

print("圖片拉成 640 X 480")
width, height = 640, 480  # 影像寬, 影像高
dsize = (width, height)
dst = cv2.resize(src, dsize)  # 重設影像大小
cv2.imshow("Dst1", dst)  # 顯示新的影像
print(f"dst1.shape = {dst.shape}")

print("圖片拉成 寬度2倍，高度一半")
dst = cv2.resize(src, None, fx=2.0, fy=0.5)  # 重設影像大小
cv2.imshow("Dst2", dst)  # 顯示新的影像
print(f"dst2.shape = {dst.shape}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("cv2.flip()")

print("原圖")
src = cv2.imread(filename1)
cv2.imshow("Src", src)

print("上下顛倒")
dst1 = cv2.flip(src, 0)  # 垂直翻轉
cv2.imshow("dst1 - Flip Vertically", dst1)  # 顯示垂直影像

print("左右顛倒")
dst2 = cv2.flip(src, 1)  # 水平翻轉
cv2.imshow("dst2 - Flip Horizontally", dst2)  # 顯示水平影像

print("上下顛倒 + 左右顛倒")
dst3 = cv2.flip(src, -1)  # 水平與垂直翻轉
cv2.imshow("dst3 - Horizontally and Vertically", dst3)  # 顯示水平與垂直影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("cv2.warpAffine() 平移")

src = cv2.imread(filename1)
cv2.imshow("Src", src)

height, width = src.shape[0:2]  # 獲得影像大小
dsize = (width, height)  # 建立未來影像大小
x = 30  # 平移 x = 30
y = 80  # 平移 y = 80
M = np.float32([[1, 0, x], [0, 1, y]])  # 建立 M 矩陣
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst", dst)  # 顯示平移結果影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("旋轉")

src = cv2.imread(filename1)
cv2.imshow("Src", src)

height, width = src.shape[0:2]  # 獲得影像大小

print("逆時鐘 旋轉 30 度")
M = cv2.getRotationMatrix2D((width / 2, height / 2), 30, 1)  # 建立 M 矩陣
dsize = (width, height)  # 建立未來影像大小
dst1 = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("CCW 30", dst1)

print("順時鐘 旋轉 30 度")
M = cv2.getRotationMatrix2D((width / 2, height / 2), -30, 1)  # 建立 M 矩陣
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("CW 30", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("仿射 歪折 折向右")

src = cv2.imread(filename1)
cv2.imshow("Src", src)

height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])  # src的A,B,C三個點
dstp = np.float32([[30, 0], [width - 1, 0], [0, height - 1]])  # dst的A,B,C三個點
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("仿射 歪折 折向左")

src = cv2.imread(filename1)
cv2.imshow("Src", src)

height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])  # src的A,B,C三個點
dstp = np.float32([[0, 0], [width - 1 - 30, 0], [30, height - 1]])  # dst的A,B,C三個點
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("仿射 歪折 轉置")

src = cv2.imread(filename1)
cv2.imshow("Src", src)

height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
a = [0, height * 0.2]  # A
b = [width * 0.8, height * 0.2]  # B
c = [width * 0.1, height * 0.9]  # C
dstp = np.float32([a, b, c])  # dst的 A, B, C
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("仿射 歪折 轉置")

src = cv2.imread(filename1)
cv2.imshow("Src", src)

height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
a = [0, height * 0.4]  # A
b = [width * 0.8, height * 0.2]  # B
c = [width * 0.1, height * 0.9]  # C
dstp = np.float32([a, b, c])  # dst的 A, B, C
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_10.py

src = cv2.imread("tunnel.jpg")
cv2.imshow("Src", src)

height, width = src.shape[0:2]  # 獲得影像大小
a1 = [0, 0]  # 原始影像的 A
b1 = [width, 0]  # 原始影像的 B
c1 = [0, height]  # 原始影像的 C
d1 = [width - 1, height - 1]  # 原始影像的 D
srcp = np.float32([a1, b1, c1, d1])
a2 = [150, 0]  # dst的 A
b2 = [width - 150, 0]  # dst的 B
c2 = [0, height - 1]  # dst的 C
d2 = [width - 1, height - 1]  # dst的 D
dstp = np.float32([a2, b2, c2, d2])
M = cv2.getPerspectiveTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpPerspective(src, M, dsize)  # 執行透視
cv2.imshow("Dst", dst)  # 顯示透視影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_10_1.py

src = np.random.randint(0, 256, size=[3, 4], dtype=np.uint8)
rows, cols = src.shape
mapx = np.ones(src.shape, np.float32) * 3  # 設定 mapx
mapy = np.ones(src.shape, np.float32) * 2  # 設定 mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"src =\n {src}")
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch10_11.py

src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
rows, cols = src.shape
mapx = np.zeros(src.shape, np.float32)
mapy = np.zeros(src.shape, np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"src =\n {src}")
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch10_12.py

src = cv2.imread("huang.jpg")
rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_13.py

src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
rows, cols = src.shape
mapx = np.zeros(src.shape, np.float32)
mapy = np.zeros(src.shape, np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), rows - 1 - r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"src =\n {src}")
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch10_14.py

src = cv2.imread("huang.jpg")
rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), rows - 1 - r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_15.py

src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
rows, cols = src.shape
mapx = np.zeros(src.shape, np.float32)
mapy = np.zeros(src.shape, np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), cols - 1 - c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"src =\n {src}")
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch10_16.py

src = cv2.imread("huang.jpg")
rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), cols - 1 - c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_17.py

src = cv2.imread("tunnel.jpg")
rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        if 0.25 * rows < r < 0.75 * rows and 0.25 * cols < c < 0.75 * cols:
            mapx.itemset((r, c), 2 * (c - cols * 0.25))  # 計算對應的 x
            mapy.itemset((r, c), 2 * (r - rows * 0.25))  # 計算對應的 y
        else:
            mapx.itemset((r, c), 0)  # 取x座標為 0
            mapy.itemset((r, c), 0)  # 取y座標為 0
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_18.py

src = cv2.imread("tunnel.jpg")
rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)
        mapy.itemset((r, c), 2 * r)
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# OpenCV_12_數學形態學
print("------------------------------------------------------------")  # 60個

print("腐蝕(Erosion)")

src = np.zeros((7, 7), np.uint8)
src[1:6, 1:6] = 1  # 建立前景影像
kernel = np.ones((3, 3), np.uint8)  # 建立內核
dst = cv2.erode(src, kernel)  # 腐蝕.erode
print(f"src = \n {src}")
print(f"kernel = \n {kernel}")
print(f"Erosion = \n {dst}")

print("------------------------------------------------------------")  # 60個

# ch12_10.py

src = cv2.imread("night.jpg")
cv2.imshow("src", src)

kernel = np.ones((9, 9), np.uint8)  # 建立9x9內核

dst = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)  # 開運算
cv2.imshow("after Opening 9 x 9", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_11.py

src = cv2.imread("night.jpg")
cv2.imshow("src", src)

kernel = np.ones((9, 9), np.uint8)  # 建立9x9內核

mid = cv2.erode(src, kernel)  # 腐蝕.erode
cv2.imshow("after erosion 9 x 9", mid)

dst = cv2.dilate(mid, kernel)  # 膨脹.dilate
cv2.imshow("after dilation 9 x 9", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_12.py

src = cv2.imread("snowman.jpg")
cv2.imshow("src", src)

kernel = np.ones((11, 11), np.uint8)  # 建立11x11內核

dst = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)  # 閉運算
cv2.imshow("after Closing 11 x 11", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_13.py

src = cv2.imread("snowman1.jpg")
cv2.imshow("src", src)

kernel = np.ones((11, 11), np.uint8)  # 建立11x11內核

dst = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)  # 閉運算
cv2.imshow("after Closing 11 x 11", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_14.py

src = cv2.imread("night.jpg")
cv2.imshow("src", src)

kernel = np.ones((9, 9), np.uint8)  # 建立9x9內核

mid = cv2.dilate(src, kernel)  # 膨脹.dilate
cv2.imshow("after dilation 9 x 9", mid)

dst = cv2.erode(mid, kernel)  # 腐蝕.erode
cv2.imshow("after erosion 9 x 9", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_15.py

src = cv2.imread("k.jpg")
cv2.imshow("src", src)

kernel = np.ones((5, 5), np.uint8)  # 建立5x5內核

dst1 = cv2.dilate(src, kernel)  # 膨脹.dilate
cv2.imshow("after dilation 5 x 5", dst1)

dst2 = cv2.erode(src, kernel)  # 腐蝕.erode
cv2.imshow("after erosion 5 x 5", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_16.py

src = cv2.imread("k.jpg")
cv2.imshow("src", src)

kernel = np.ones((5, 5), np.uint8)  # 建立5x5內核

dst = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel)  # gradient
cv2.imshow("after morpological gradient", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_17.py

src = cv2.imread("hole.jpg")
cv2.imshow("src", src)

kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核

dst = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel)  # gradient
cv2.imshow("after morpological gradient", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_18.py

src = cv2.imread("btree.jpg")
cv2.imshow("src", src)

kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核

dst = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, kernel)  # 禮帽運算(tophat)
cv2.imshow("after tophat", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_19.py

src = cv2.imread("snowman.jpg")
cv2.imshow("src", src)

kernel = np.ones((11, 11), np.uint8)  # 建立11x11內核

dst = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel)  # 黑帽運算(blackhat)
cv2.imshow("after blackhat", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_2.py

src = cv2.imread("bw.jpg")
cv2.imshow("src", src)

kernel = np.ones((5, 5), np.uint8)  # 建立5x5內核

dst1 = cv2.erode(src, kernel)  # 腐蝕.erode
cv2.imshow("after erosion 5 x 5", dst1)

kerne2 = np.ones((11, 11), np.uint8)  # 建立11x11內核

dst2 = cv2.erode(src, kerne2)  # 腐蝕.erode
cv2.imshow("after erosion 11 x 11", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_20.py

src = cv2.imread("excel.jpg")
cv2.imshow("src", src)

kernel = np.ones((11, 11), np.uint8)  # 建立11x11內核

dst = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel)  # 黑帽運算(blackhat)
cv2.imshow("after blackhat", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_21.py

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
print(f"MORPH_RECT \n {kernel}")
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
print(f"MORPH_ELLIPSE \n {kernel}")
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
print(f"MORPH_CROSS \n {kernel}")

print("------------------------------------------------------------")  # 60個

# ch12_22.py

src = cv2.imread("bw_circle.jpg")
cv2.imshow("src", src)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (39, 39))

dst1 = cv2.dilate(src, kernel)  # 膨脹.dilate
cv2.imshow("MORPH_RECT", dst1)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (39, 39))

dst2 = cv2.dilate(src, kernel)  # 膨脹.dilate
cv2.imshow("MORPH_ELLIPSE", dst2)

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (39, 39))

dst3 = cv2.dilate(src, kernel)  # 膨脹.dilate
cv2.imshow("MORPH_CROSS", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_3.py

src = cv2.imread("bw_noise.jpg")
cv2.imshow("src", src)

kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核

dst1 = cv2.erode(src, kernel)  # 腐蝕.erode
cv2.imshow("after erosion 3 x 3", dst1)

kerne2 = np.ones((5, 5), np.uint8)  # 建立5x5內核

dst2 = cv2.erode(src, kerne2)  # 腐蝕.erode
cv2.imshow("after erosion 5 x 5", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_4.py

src = cv2.imread("whilster.jpg")
cv2.imshow("src", src)

kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核

dst1 = cv2.erode(src, kernel)  # 腐蝕.erode
cv2.imshow("after erosion 3 x 3", dst1)

kerne2 = np.ones((5, 5), np.uint8)  # 建立5x5內核

dst2 = cv2.erode(src, kerne2)  # 腐蝕.erode
cv2.imshow("after erosion 5 x 5", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_5.py

src = np.zeros((7, 7), np.uint8)
src[2:5, 2:5] = 1  # 建立前景影像
kernel = np.ones((3, 3), np.uint8)  # 建立內核
dst = cv2.dilate(src, kernel)  # 膨脹.dilate
print(f"src = \n {src}")
print(f"kernel = \n {kernel}")
print(f"Dilation = \n {dst}")

print("------------------------------------------------------------")  # 60個

# ch12_6.py

src = cv2.imread("bw_dilate.jpg")
cv2.imshow("src", src)

kernel = np.ones((5, 5), np.uint8)  # 建立5x5內核

dst1 = cv2.dilate(src, kernel)  # 膨脹.dilate
cv2.imshow("after dilation 5 x 5", dst1)

kerne2 = np.ones((11, 11), np.uint8)  # 建立11x11內核

dst2 = cv2.dilate(src, kerne2)  # 膨脹.dilate
cv2.imshow("after dilation 11 x 11", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_7.py

src = cv2.imread("a.jpg")
cv2.imshow("src", src)

kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核

dst1 = cv2.dilate(src, kernel)  # 膨脹.dilate
cv2.imshow("after dilation 3 x 3", dst1)

kerne2 = np.ones((5, 5), np.uint8)  # 建立5x5內核

dst2 = cv2.dilate(src, kerne2)  # 膨脹.dilate
cv2.imshow("after dilation 5 x 5", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_8.py

src = cv2.imread("whilster.jpg")
cv2.imshow("src", src)

kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核

dst1 = cv2.dilate(src, kernel)  # 膨脹.dilate
cv2.imshow("after dilation 3 x 3", dst1)

kerne2 = np.ones((5, 5), np.uint8)  # 建立5x5內核

dst2 = cv2.dilate(src, kerne2)  # 膨脹.dilate
cv2.imshow("after dilation 5 x 5", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_9.py

src = cv2.imread("btree.jpg")
cv2.imshow("src", src)

kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核

dst = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)  # 開運算
cv2.imshow("after Opening 3 x 3", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_13_影像梯度與邊緣偵測
print("------------------------------------------------------------")  # 60個

# ch13_1.py

src = np.random.randint(-256, 256, size=[3, 5], dtype=np.int16)
print(f"src = \n {src}")
dst = cv2.convertScaleAbs(src)
print(f"dst = \n {dst}")

print("------------------------------------------------------------")  # 60個

print("使用 Sobel()")

src = cv2.imread("map.jpg")
cv2.imshow("Src", src)

dst = cv2.Sobel(src, -1, 1, 0)  # 計算 x 軸影像梯度
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 Sobel()")

src = cv2.imread("map.jpg")
cv2.imshow("Src", src)

dst = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dst = cv2.convertScaleAbs(dst)  # 將負值轉正值
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 Sobel()")

src = cv2.imread("map.jpg")
cv2.imshow("Src", src)

dst = cv2.Sobel(src, -1, 0, 1)  # 計算 y 軸影像梯度
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 Sobel()")

src = cv2.imread("map.jpg")
cv2.imshow("Src", src)

dst = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dst = cv2.convertScaleAbs(dst)  # 將負值轉正值
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 Sobel()")

src = cv2.imread("map.jpg")
cv2.imshow("Src", src)

dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 Sobel()")

src = cv2.imread("lena.jpg")
cv2.imshow("Src", src)

dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合
cv2.imshow("Dstx", dstx)
cv2.imshow("Dsty", dsty)
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 Sobel() / Scharr()")

# Sobel()函數
src = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)  # 黑白讀取
cv2.imshow("Src", src)

dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_sobel = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合

# Scharr()函數
dstx = cv2.Scharr(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Scharr(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_scharr = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合

# 輸出影像梯度
cv2.imshow("Sobel", dst_sobel)
cv2.imshow("Scharr", dst_scharr)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 Sobel() / Scharr()")

# Sobel()函數
src = cv2.imread("lena.jpg")  # 彩色讀取
cv2.imshow("Src", src)

dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_sobel = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合

# Scharr()函數
dstx = cv2.Scharr(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Scharr(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_scharr = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合

# 輸出影像梯度
cv2.imshow("Sobel", dst_sobel)
cv2.imshow("Scharr", dst_scharr)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 Sobel() / Scharr()")

# Sobel()函數
src = cv2.imread("snow.jpg")  # 彩色讀取
cv2.imshow("Src", src)

dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_sobel = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合
# Scharr()函數
dstx = cv2.Scharr(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Scharr(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_scharr = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合

# 輸出影像梯度
cv2.imshow("Scharr X", dstx)
cv2.imshow("Scharr Y", dsty)
cv2.imshow("Sobel", dst_sobel)
cv2.imshow("Scharr", dst_scharr)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 Laplacian()")

src = cv2.imread("laplacian.jpg")
cv2.imshow("Src", src)

dst_tmp = cv2.Laplacian(src, cv2.CV_32F)  # Laplacian邊緣影像
dst = cv2.convertScaleAbs(dst_tmp)  # 轉換為正值
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 Sobel() / Scharr() / Laplacian()")

src = cv2.imread("geneva.jpg", cv2.IMREAD_GRAYSCALE)  # 黑白讀取
cv2.imshow("Src", src)

src = cv2.GaussianBlur(src, (3, 3), 0)  # 降低噪音
cv2.imshow("Src", src)

# Sobel()函數
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_sobel = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合
# Scharr()函數
dstx = cv2.Scharr(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Scharr(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_scharr = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合
# Laplacian()函數
dst_tmp = cv2.Laplacian(src, cv2.CV_32F, ksize=3)  # Laplacian邊緣影像
dst_lap = cv2.convertScaleAbs(dst_tmp)  # 將負值轉正值

# 輸出影像梯度
cv2.imshow("Sobel", dst_sobel)
cv2.imshow("Scharr", dst_scharr)
cv2.imshow("Laplacian", dst_lap)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 Canny()")

src = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

dst1 = cv2.Canny(src, 50, 100)  # minVal=50, maxVal=100
dst2 = cv2.Canny(src, 50, 200)  # minVal=50, maxVal=200
cv2.imshow("Dst1", dst1)
cv2.imshow("Dst2", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 Sobel() / Scharr() / Laplacian() / Canny()")

src = cv2.imread("geneva.jpg", cv2.IMREAD_GRAYSCALE)  # 黑白讀取

src = cv2.GaussianBlur(src, (3, 3), 0)  # 降低噪音

# Sobel()函數
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_sobel = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合

# Scharr()函數
dstx = cv2.Scharr(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Scharr(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_scharr = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合

# Laplacian()函數
dst_tmp = cv2.Laplacian(src, cv2.CV_32F, ksize=3)  # Laplacian邊緣影像
dst_lap = cv2.convertScaleAbs(dst_tmp)  # 將負值轉正值

# Canny()函數
dst_canny = cv2.Canny(src, 50, 100)  # minVal=50, maxVal=100

# 輸出影像梯度
cv2.imshow("Canny", dst_canny)
cv2.imshow("Sobel", dst_sobel)
cv2.imshow("Scharr", dst_scharr)
cv2.imshow("Laplacian", dst_lap)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_14_影像金字塔
print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("macau.jpg")
cv2.imshow("src", src)

dst1 = cv2.pyrDown(src)  # 第 1 次向下採樣
dst2 = cv2.pyrDown(dst1)  # 第 2 次向下採樣
dst3 = cv2.pyrDown(dst2)  # 第 3 次向下採樣
print(f"src.shape = {src.shape}")
print(f"dst1.shape = {dst1.shape}")
print(f"dst2.shape = {dst2.shape}")
print(f"dst3.shape = {dst3.shape}")

cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("macau_small.jpg")

dst1 = cv2.pyrUp(src)  # 第 1 次向下採樣
dst2 = cv2.pyrUp(dst1)  # 第 2 次向下採樣
dst3 = cv2.pyrUp(dst2)  # 第 3 次向下採樣

print(f"src.shape = {src.shape}")
print(f"dst1.shape = {dst1.shape}")
print(f"dst2.shape = {dst2.shape}")
print(f"dst3.shape = {dst3.shape}")
cv2.imshow("drc", src)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch14_3.py

src1 = np.random.randint(256, size=(2, 3), dtype=np.uint8)
src2 = np.random.randint(256, size=(2, 3), dtype=np.uint8)
dst = src1 + src2
print(f"src1 = \n{src1}")
print(f"src2 = \n{src2}")
print(f"dst = \n{dst}")

print("------------------------------------------------------------")  # 60個

# ch14_4.py

src = cv2.imread("pengiun.jpg")
cv2.imshow("src", src)

dst1 = src + src  # 影像相加
dst2 = src - src  # 影像相減

cv2.imshow("dst1 - add", dst1)
cv2.imshow("dst2 - subtraction", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("pengiun.jpg")
cv2.imshow("src", src)

print(f"原始影像大小 = \n{src.shape}")
dst_down = cv2.pyrDown(src)  # 向下採樣
print(f"向下採樣大小 = \n{dst_down.shape}")
dst_up = cv2.pyrUp(dst_down)  # 向上採樣, 復原大小
print(f"向上採樣大小 = \n{dst_up.shape}")
dst = dst_up - src
print(f"結果影像大小 = \n{dst.shape}")

cv2.imshow("dst1 - recovery", dst_up)
cv2.imshow("dst2 - dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("pengiun.jpg")
cv2.imshow("src", src)

print(f"原始影像大小 = \n{src.shape}")
dst_up = cv2.pyrUp(src)  # 向上採樣
print(f"向上採樣大小 = \n{dst_up.shape}")
dst_down = cv2.pyrDown(dst_up)  # 向下採樣, 復原大小
print(f"向下採樣大小 = \n{dst_down.shape}")
dst = dst_down - src
print(f"結果影像大小 = \n{dst.shape}")

cv2.imshow("dst1 - recovery", dst_down)
cv2.imshow("dst2 - dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("pengiun.jpg")

G0 = src
G1 = cv2.pyrDown(G0)  # 第 1 次向下採樣
G2 = cv2.pyrDown(G1)  # 第 2 次向下採樣

L0 = G0 - cv2.pyrUp(G1)  # 建立第 0 層拉普拉斯金字塔
L1 = G1 - cv2.pyrUp(G2)  # 建立第 1 層拉普拉斯金字塔
print(f"L0.shape = \n{L0.shape}")  # 列印第 0 層拉普拉斯金字塔大小
print(f"L1.shape = \n{L1.shape}")  # 列印第 1 層拉普拉斯金字塔大小
cv2.imshow("Laplacian L0", L0)  # 顯示第 0 層拉普拉斯金字塔
cv2.imshow("Laplacian L1", L1)  # 顯示第 1 層拉普拉斯金字塔

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("pengiun.jpg")
cv2.imshow("Src", src)

G0 = src
G1 = cv2.pyrDown(G0)  # 第 1 次向下採樣
L0 = src - cv2.pyrUp(G1)  # 拉普拉斯影像
dst = L0 + cv2.pyrUp(G1)  # 恢復結果影像

print(f"src.shape = \n{src.shape}")  # 列印原始影像大小
print(f"dst.shape = \n{dst.shape}")  # 列印恢復影像大小
cv2.imshow("Dst", dst)  # 顯示恢復影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_15_輪廓的檢測與匹配
print("------------------------------------------------------------")  # 60個

# ch15_1.py

src = cv2.imread("easy.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_1_1.py

src = cv2.imread("easy.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像
cv2.imshow("src1", src)  # 再輸出一次原始影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_2.py

src = cv2.imread("easy.jpg")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
print(f"資料類型      : {type(contours)}")
print(f"輪廓數量      : {len(contours)}")

print("------------------------------------------------------------")  # 60個

# ch15_3.py

src = cv2.imread("easy.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
n = len(contours)  # 回傳輪廓數
imgList = []  # 建立輪廓串列
for i in range(n):  # 依次繪製輪廓
    img = np.zeros(src.shape, np.uint8)  # 建立輪廓影像
    imgList.append(img)  # 將預設黑底影像加入串列
    # 繪製輪廓影像
    imgList[i] = cv2.drawContours(imgList[i], contours, i, (255, 255, 255), 5)
    cv2.imshow("contours" + str(i), imgList[i])  # 顯示輪廓影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_4.py

src = cv2.imread("easy.jpg")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
n = len(contours)  # 回傳輪廓數
for i in range(n):  # 輸出輪廓的屬性
    print(f"編號 = {i}")
    print(f"輪廓點的數量 = {len(contours[i])}")
    print(f"輪廓點的外形 = {contours[i].shape}")

print("------------------------------------------------------------")  # 60個

# ch15_5.py

src = cv2.imread("easy.jpg")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
n = len(contours)  # 回傳輪廓數
print(contours[1])  # 列印編號1的輪廓點

print("------------------------------------------------------------")  # 60個

# ch15_6.py

src = cv2.imread("easy1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_7.py

src = cv2.imread("easy1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_8.py

src = cv2.imread("lake.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("binary", dst_binary)  # 顯示二值化影像
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 2)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_9.py

src = cv2.imread("lake.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("binary", dst_binary)  # 顯示二值化影像
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (255, 255, 255), -1)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_10.py

src = cv2.imread("lake.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("binary", dst_binary)  # 顯示二值化影像
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
mask = np.zeros(src.shape, np.uint8)
dst = cv2.drawContours(mask, contours, -1, (255, 255, 255), -1)  # 繪製圖形輪廓
dst_result = cv2.bitwise_and(src, mask)
cv2.imshow("dst result", dst_result)  # 顯示結果影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_11.py

src = cv2.imread("easy2.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像
print(f"hierarchy 資料類型 : {type(hierarchy)}")
print(f"列印層級 \n {hierarchy}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_12.py

src = cv2.imread("easy2.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像
print(f"hierarchy 資料類型 : {type(hierarchy)}")
print(f"列印層級 \n {hierarchy}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_13.py

src = cv2.imread("easy3.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 3)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像
print(f"hierarchy 資料類型 : {type(hierarchy)}")
print(f"列印層級 \n {hierarchy}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_14.py

src = cv2.imread("easy3.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 3)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像
print(f"列印層級 \n {hierarchy}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_15.py

src = cv2.imread("easy.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
n = len(contours)  # 回傳輪廓數
imgList = []  # 建立輪廓串列
for i in range(n):  # 依次繪製輪廓
    img = np.zeros(src.shape, np.uint8)  # 建立輪廓影像
    imgList.append(img)  # 將預設黑底影像加入串列
    # 繪製輪廓影像
    imgList[i] = cv2.drawContours(imgList[i], contours, i, (255, 255, 255), 5)
    cv2.imshow("contours" + str(i), imgList[i])  # 顯示輪廓影像

for i in range(n):  # 列印輪廓面積
    area = cv2.moments(contours[i])
    print(f"輪廓面積 str(i) = {area['m00']}")

for i in range(n):  # 列印影像矩
    M = cv2.moments(contours[i])
    print(f"列印影像矩 {str(i)} \n {M}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_16.py

src = cv2.imread("easy.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)  # 繪製圖形輪廓

for c in contours:  # 繪製中心點迴圈
    M = cv2.moments(c)  # 影像矩
    Cx = int(M["m10"] / M["m00"])  # 質心 x 座標
    Cy = int(M["m01"] / M["m00"])  # 質心 y 座標
    cv2.circle(dst, (Cx, Cy), 5, (255, 0, 0), -1)  # 繪製中心點
cv2.imshow("result", dst)  # 顯示結果影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_17.py

src = cv2.imread("easy.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
n = len(contours)
for i in range(n):  # 繪製中心點迴圈
    M = cv2.moments(contours[i])  # 影像矩
    area = cv2.contourArea(contours[i])  # 計算輪廓面積
    print(f"輪廓 {i} 面積 = {area}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_18.py

src = cv2.imread("easy.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
n = len(contours)
for i in range(n):  # 繪製中心點迴圈
    M = cv2.moments(contours[i])  # 影像矩
    area = cv2.arcLength(contours[i], True)  # 計算輪廓周長
    print(f"輪廓 {i} 周長 = {area}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_19.py

src = cv2.imread("heart.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
M = cv2.moments(src_gray)  # 影像矩
nu20 = M["nu20"]
print(f"歸一化中心矩 nu20 = {nu20}")
nu02 = M["nu02"]
print(f"歸一化中心矩 nu02 = {nu02}")

Hu = cv2.HuMoments(M)  # Hu矩
print(f"Hu \n {Hu}")  # 列印Hu矩

result = Hu[0][0] - (nu20 + nu02)  # 驗證Hu矩 0, h0
print(f"驗證結果 h0 - nu20 - nu02 = {result}")

print("------------------------------------------------------------")  # 60個

# ch15_20.py

src = cv2.imread("3heart.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

M0 = cv2.moments(contours[0])  # 計算編號 0 影像矩
M1 = cv2.moments(contours[1])  # 計算編號 1 影像矩
M2 = cv2.moments(contours[2])  # 計算編號 2 影像矩
Hu0 = cv2.HuMoments(M0)  # 計算編號 0 Hu矩
Hu1 = cv2.HuMoments(M1)  # 計算編號 1 Hu矩
Hu2 = cv2.HuMoments(M2)  # 計算編號 2 Hu矩
# 列印Hu矩
print(f"h0 = {Hu0[0]}\t\t {Hu1[0]}\t\t {Hu2[0]}")
print(f"h1 = {Hu0[1]}\t\t {Hu1[1]}\t\t {Hu2[1]}")
print(f"h2 = {Hu0[2]}\t\t {Hu1[2]}\t\t {Hu2[2]}")
print(f"h3 = {Hu0[3]}\t\t {Hu1[3]}\t {Hu2[3]}")
print(f"h4 = {Hu0[4]}\t\t {Hu1[4]}\t {Hu2[4]}")
print(f"h5 = {Hu0[5]}\t\t {Hu1[5]}\t {Hu2[5]}")
print(f"h6 = {Hu0[6]}\t\t {Hu1[6]}\t {Hu2[6]}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_21.py

src = cv2.imread("3shapes.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

M0 = cv2.moments(contours[0])  # 計算編號 0 影像矩
M1 = cv2.moments(contours[1])  # 計算編號 1 影像矩
M2 = cv2.moments(contours[2])  # 計算編號 2 影像矩
Hu0 = cv2.HuMoments(M0)  # 計算編號 0 Hu矩
Hu1 = cv2.HuMoments(M1)  # 計算編號 1 Hu矩
Hu2 = cv2.HuMoments(M2)  # 計算編號 2 Hu矩
# 列印Hu矩
print(f"h0 = {Hu0[0]}\t\t {Hu1[0]}\t\t {Hu2[0]}")
print(f"h1 = {Hu0[1]}\t\t {Hu1[1]}\t {Hu2[1]}")
print(f"h2 = {Hu0[2]}\t\t {Hu1[2]}\t {Hu2[2]}")
print(f"h3 = {Hu0[3]}\t\t {Hu1[3]}\t {Hu2[3]}")
print(f"h4 = {Hu0[4]}\t\t {Hu1[4]}\t {Hu2[4]}")
print(f"h5 = {Hu0[5]}\t\t {Hu1[5]}\t {Hu2[5]}")
print(f"h6 = {Hu0[6]}\t\t {Hu1[6]}\t {Hu2[6]}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_22.py

src = cv2.imread("myheart.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

match0 = cv2.matchShapes(contours[0], contours[0], 1, 0)  # 輪廓0和0比較
print(f"輪廓0和0比較 = {match0}")
match1 = cv2.matchShapes(contours[0], contours[1], 1, 0)  # 輪廓0和1比較
print(f"輪廓0和1比較 = {match1}")
match2 = cv2.matchShapes(contours[0], contours[2], 1, 0)  # 輪廓0和2比較
print(f"輪廓0和2比較 = {match2}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_23.py

# 讀取與建立影像 1
src1 = cv2.imread("mycloud1.jpg")
cv2.imshow("mycloud1", src1)

src1_gray = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src1_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt1 = contours[0]
# 讀取與建立影像 2
src2 = cv2.imread("mycloud2.jpg")
cv2.imshow("mycloud2", src2)
src2_gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
ret, dst_binary = cv2.threshold(src2_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt2 = contours[0]
# 讀取與建立影像 3
src3 = cv2.imread("explode1.jpg")
cv2.imshow("explode", src3)
src3_gray = cv2.cvtColor(src3, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
ret, dst_binary = cv2.threshold(src3_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt3 = contours[0]
sd = cv2.createShapeContextDistanceExtractor()  # 建立形狀場景運算子
match0 = sd.computeDistance(cnt1, cnt1)  # 影像1和1比較
print(f"影像1和1比較 = {match0}")
match1 = sd.computeDistance(cnt1, cnt2)  # 影像1和2比較
print(f"影像1和2比較 = {match1}")
match2 = sd.computeDistance(cnt1, cnt3)  # 影像1和3比較
print(f"影像1和3比較 = {match2}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_24.py

# 讀取與建立影像 1
src1 = cv2.imread("mycloud1.jpg")
cv2.imshow("mycloud1", src1)

src1_gray = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src1_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt1 = contours[0]
# 讀取與建立影像 2
src2 = cv2.imread("mycloud2.jpg")
cv2.imshow("mycloud2", src2)
src2_gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
ret, dst_binary = cv2.threshold(src2_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt2 = contours[0]
# 讀取與建立影像 3
src3 = cv2.imread("explode1.jpg")
cv2.imshow("explode", src3)
src3_gray = cv2.cvtColor(src3, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
ret, dst_binary = cv2.threshold(src3_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt3 = contours[0]
hd = cv2.createHausdorffDistanceExtractor()  # 建立Hausdorff
match0 = hd.computeDistance(cnt1, cnt1)  # 影像1和1比較
print(f"影像1和1比較 = {match0}")
match1 = hd.computeDistance(cnt1, cnt2)  # 影像1和2比較
print(f"影像1和2比較 = {match1}")
match2 = hd.computeDistance(cnt1, cnt3)  # 影像1和3比較
print(f"影像1和3比較 = {match2}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# OpenCV_16_輪廓擬合與凸包的相關應用
print("------------------------------------------------------------")  # 60個

# ch16_1.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

# 輸出矩形格式使用元組(tuple)
rect = cv2.boundingRect(contours[0])
print(f"元組 rect = {rect}")
# 輸出矩形格式, 列出所有細項
x, y, w, h = cv2.boundingRect(contours[0])
print(f"左上角 x = {x}, 左上角 y = {y}")
print(f"矩形寬度     = {w}")
print(f"矩形高度     = {h}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_2.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 255), 2)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_3.py

src = cv2.imread("explode2.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 255), 2)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_4.py

src = cv2.imread("explode2.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

box = cv2.minAreaRect(contours[0])  # 建構最小矩形
print(f"轉換前的矩形頂角 = \n {box}")
points = cv2.boxPoints(box)  # 獲取頂點座標
points = np.int0(points)  # 轉為整數
print(f"轉換後的矩形頂角 = \n {points}")
dst = cv2.drawContours(src, [points], 0, (0, 255, 0), 2)  # 繪製輪廓
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_5.py

src = cv2.imread("explode3.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 取得圓中心座標和圓半徑
(x, y), radius = cv2.minEnclosingCircle(contours[0])
center = (int(x), int(y))  # 圓中心座標取整數
radius = int(radius)  # 圓半徑取整數
dst = cv2.circle(src, center, radius, (0, 255, 255), 2)  # 繪圓
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_6.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 取得圓中心座標和圓半徑
(x, y), radius = cv2.minEnclosingCircle(contours[0])
center = (int(x), int(y))  # 圓中心座標取整數
radius = int(radius)  # 圓半徑取整數
dst = cv2.circle(src, center, radius, (0, 255, 255), 2)  # 繪圓
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_7.py

src = cv2.imread("cloud.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 取得圓中心座標和圓半徑
ellipse = cv2.fitEllipse(contours[0])  # 取得最優擬合橢圓數據
print(f"資料類型   = {type(ellipse)}")
print(f"橢圓中心   = {ellipse[0]}")
print(f"長短軸直徑 = {ellipse[1]}")
print(f"旋轉角度   = {ellipse[2]}")
dst = cv2.ellipse(src, ellipse, (0, 255, 0), 2)  # 繪橢圓
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_8.py

src = cv2.imread("heart.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 取得三角形面積與頂點座標
area, triangle = cv2.minEnclosingTriangle(contours[0])
print(f"三角形面積   = {area}")
print(f"三角形頂點座標資料類型 = {type(triangle)}")
print(f"三角頂點座標 = \n{triangle}")
triangle = np.int0(triangle)  # 轉整數
dst = cv2.line(src, tuple(triangle[0][0]), tuple(triangle[1][0]), (0, 255, 0), 2)
dst = cv2.line(src, tuple(triangle[1][0]), tuple(triangle[2][0]), (0, 255, 0), 2)
dst = cv2.line(src, tuple(triangle[0][0]), tuple(triangle[2][0]), (0, 255, 0), 2)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_9.py

src = cv2.imread("multiple.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 近似多邊形包圍
n = len(contours)  # 輪廓數量
src1 = src.copy()  # 複製src影像
src2 = src.copy()  # 複製src影像
for i in range(n):
    approx = cv2.approxPolyDP(contours[i], 3, True)  # epsilon=3
    dst1 = cv2.polylines(src1, [approx], True, (0, 255, 0), 2)  # dst1
    approx = cv2.approxPolyDP(contours[i], 15, True)  # epsilon=15
    dst2 = cv2.polylines(src2, [approx], True, (0, 255, 0), 2)  # dst2
cv2.imshow("dst1 - epsilon = 3", dst1)
cv2.imshow("dst2 - epsilon = 15", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_10.py

src = cv2.imread("unregular.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 擬合一條線
rows, cols = src.shape[:2]  # 輪廓大小
vx, vy, x, y = cv2.fitLine(contours[0], cv2.DIST_L2, 0, 0.01, 0.01)
print(f"共線正規化向量 = {vx}, {vy}")
print(f"直線經過的點   = {x}, {y}")
lefty = int((-x * vy / vx) + y)  # 左邊點的 y 座標
righty = int(((cols - x) * vy / vx) + y)  # 右邊點的 y 座標
dst = cv2.line(src, (0, lefty), (cols - 1, righty), (0, 255, 0), 2)  # 左到右繪線
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_11.py

src = cv2.imread("heart1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_12.py

src = cv2.imread("hand1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_12_1.py

src = cv2.imread("hand1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
cv2.imshow("dst", dst)
convex_area = cv2.contourArea(hull)  # 凸包面積
print(f"凸包面積 = {convex_area}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_13.py

src = cv2.imread("hand2.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
n = len(contours)  # 輪廓數量
for i in range(n):
    hull = cv2.convexHull(contours[i])  # 獲得凸包頂點座標
    dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_14.py

src = cv2.imread("star.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包 -> 凸包缺陷
contour = contours[0]  # 輪廓
hull = cv2.convexHull(contour, returnPoints=False)  # 獲得凸包
defects = cv2.convexityDefects(contour, hull)  # 獲得凸包缺陷
n = defects.shape[0]  # 缺陷數量
print(f"缺陷數量 = {n}")
for i in range(n):
    # s是startPoint, e是endPoint, f是farPoint, d是depth
    s, e, f, d = defects[i, 0]
    start = tuple(contour[s][0])  # 取得startPoint座標
    end = tuple(contour[e][0])  # 取得endPoint座標
    far = tuple(contour[f][0])  # 取得farPoint座標
    dst = cv2.line(src, start, end, [0, 255, 0], 2)  # 凸包連線
    dst = cv2.circle(src, far, 3, [0, 0, 255], -1)  # 繪製farPoint
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_15.py

src = cv2.imread("heart1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
src1 = src.copy()  # 複製src影像
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst1 = cv2.polylines(src1, [hull], True, (0, 255, 0), 2)  # 將凸包連線
cv2.imshow("dst1", dst1)
isConvex = cv2.isContourConvex(hull)  # 是否凸形
print(f"凸包是凸形       = {isConvex}")
# 近似多邊形包圍
src2 = src.copy()  # 複製src影像
approx = cv2.approxPolyDP(contours[0], 10, True)  # epsilon=10
dst2 = cv2.polylines(src2, [approx], True, (0, 255, 0), 2)  # 近似多邊形連線
cv2.imshow("dst2 - epsilon = 10", dst2)
isConvex = cv2.isContourConvex(approx)  # 是否凸形
print(f"近似多邊形是凸形 = {isConvex}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_16.py

src = cv2.imread("heart1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
# print(hull)   可以用這個指令了解凸包座標點
# 點在凸包線上
pointa = (231, 85)  # 點在凸包線上
dist_a = cv2.pointPolygonTest(hull, pointa, True)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_a = (236, 95)  # 文字輸出位置
dst = cv2.circle(src, pointa, 3, [0, 0, 255], -1)  # 用圓標記點 A
cv2.putText(dst, "A", pos_a, font, 1, (0, 255, 255), 2)  # 輸出文字 A
print(f"dist_a = {dist_a}")
# 點在凸包內
pointb = (150, 100)  # 點在凸包線上
dist_b = cv2.pointPolygonTest(hull, pointb, True)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_b = (160, 110)  # 文字輸出位置
dst = cv2.circle(src, pointb, 3, [0, 0, 255], -1)  # 用圓標記點 B
cv2.putText(dst, "B", pos_b, font, 1, (255, 0, 0), 2)  # 輸出文字 B
print(f"dist_b = {dist_b}")
# 點在凸包外
pointc = (80, 85)  # 點在凸包線上
dist_c = cv2.pointPolygonTest(hull, pointc, True)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_c = (50, 95)  # 文字輸出位置
dst = cv2.circle(src, pointc, 3, [0, 0, 255], -1)  # 用圓標記點 C
cv2.putText(dst, "C", pos_c, font, 1, (0, 255, 255), 2)  # 輸出文字 C
print(f"dist_c = {dist_c}")
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_17.py

src = cv2.imread("heart1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
# print(hull)   可以用這個指令了解凸包座標點
# 點在凸包線上
pointa = (231, 85)  # 點在凸包線上
dist_a = cv2.pointPolygonTest(hull, pointa, False)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_a = (236, 95)  # 文字輸出位置
dst = cv2.circle(src, pointa, 3, [0, 0, 255], -1)  # 用圓標記點 A
cv2.putText(dst, "A", pos_a, font, 1, (0, 255, 255), 2)  # 輸出文字 A
print(f"dist_a = {dist_a}")
# 點在凸包內
pointb = (150, 100)  # 點在凸包線上
dist_b = cv2.pointPolygonTest(hull, pointb, False)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_b = (160, 110)  # 文字輸出位置
dst = cv2.circle(src, pointb, 3, [0, 0, 255], -1)  # 用圓標記點 B
cv2.putText(dst, "B", pos_b, font, 1, (255, 0, 0), 2)  # 輸出文字 B
print(f"dist_b = {dist_b}")
# 點在凸包外
pointc = (80, 85)  # 點在凸包線上
dist_c = cv2.pointPolygonTest(hull, pointc, False)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_c = (50, 95)  # 文字輸出位置
dst = cv2.circle(src, pointc, 3, [0, 0, 255], -1)  # 用圓標記點 C
cv2.putText(dst, "C", pos_c, font, 1, (0, 255, 255), 2)  # 輸出文字 C
print(f"dist_c = {dist_c}")
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_17_輪廓的特徵
print("------------------------------------------------------------")  # 60個

# ch17_1.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 255), 2)
cv2.imshow("dst", dst)
aspectratio = w / h  # 計算寬高比
print(f"寬高比 = {aspectratio}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_2.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]  # 建立輪廓變數
print(f"資料格式 = {type(cnt)}")
print(f"資料維度 = {cnt.ndim}")
print(f"資料長度 = {len(cnt)}")
for i in range(3):  # 列印 3 個座標點
    print(cnt[i])

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_3.py

data = np.array([3, 9, 8, 5, 2])
print(f"data = {data}")
max_i = np.argmax(data)
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i]}")
min_i = np.argmin(data)
print(f"最小值索引 = {min_i}")
print(f"最小值     = {data[min_i]}")

print("------------------------------------------------------------")  # 60個

# ch17_4.py

data = np.array([3, 9, 8, 5, 2])
print(f"data = {data}")
max_i = data.argmax()
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i]}")
min_i = data.argmin()
print(f"最小值索引 = {min_i}")
print(f"最小值     = {data[min_i]}")

print("------------------------------------------------------------")  # 60個

# ch17_5.py

data = np.array([[3, 9], [8, 2], [5, 3]])
print(f"data = {data}")
max_i = data[:, 0].argmax()
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i][0]}")
print(f"對應值     = {data[max_i][1]}")
max_val = tuple(data[data[:, 0].argmax()])
print(f"最大值配對 = {max_val}")

print("------------------------------------------------------------")  # 60個

# ch17_6.py

data = np.array([[[186, 39]], [[181, 44]], [[180, 44]]])
print(f"原始資料data = \n{data}")
n = len(data)
print("取3維內的陣列資料")
for i in range(n):  # 列印 3 個座標點
    print(data[i])
print(f"資料維度   = {data.ndim}")  # 維度
max_i = data[:, :, 0].argmax()  # x 最大值索引索引
print(f"x 最大值索引 = {max_i}")  # 列印 x 最大值索引
right = tuple(data[data[:, :, 0].argmax()][0])  # 最大值元組
print(f"最大值元組 = {right}")  # 列印最大值元組
min_i = data[:, :, 0].argmin()  # x 最小值索引索引
print(f"x 最小值索引 = {min_i}")  # 列印 x 最小值索引
left = tuple(data[data[:, :, 0].argmin()][0])  # 最小值元組
print(f"最小值元組 = {left}")  # 列印最小值元組

print("------------------------------------------------------------")  # 60個

# ch17_7.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]  # 建立輪廓變數
left = tuple(cnt[cnt[:, :, 0].argmin()][0])  # left
right = tuple(cnt[cnt[:, :, 0].argmax()][0])  # right
top = tuple(cnt[cnt[:, :, 1].argmin()][0])  # top
bottom = tuple(cnt[cnt[:, :, 1].argmax()][0])  # bottom
print(f"最左點 = {left}")
print(f"最右點 = {right}")
print(f"最上點 = {top}")
print(f"最下點 = {bottom}")
dst = cv2.circle(src, left, 5, [0, 255, 0], -1)
dst = cv2.circle(src, right, 5, [0, 255, 0], -1)
dst = cv2.circle(src, top, 5, [0, 255, 255], -1)
dst = cv2.circle(src, bottom, 5, [0, 255, 255], -1)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_8.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 3)  # 繪製輪廓
con_area = cv2.contourArea(contours[0])  # 輪廓面積
x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 255), 2)
cv2.imshow("dst", dst)
square_area = w * h  # 計算矩形面積
extent = con_area / square_area  # 計算Extent
print(f"Extent = {extent}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_9.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 3)  # 繪製輪廓
con_area = cv2.contourArea(contours[0])  # 輪廓面積
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 255), 2)  # 將凸包連線
cv2.imshow("dst", dst)
convex_area = cv2.contourArea(hull)  # 凸包面積
solidity = con_area / convex_area  # 計算solidity
print(f"Solidity = {solidity}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_10.py

src = cv2.imread("star1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 3)  # 繪製輪廓
con_area = cv2.contourArea(contours[0])  # 輪廓面積
ed = np.sqrt(4 * con_area / np.pi)  # 計算等效面積
print(f"等效面積 = {ed}")
dst = cv2.circle(src, (260, 110), int(ed / 2), (0, 255, 0), 3)  # 繪製圓
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_11.py

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")
nonzero_img = np.nonzero(img)  # 獲得非0元素座標
print(f"非0元素的座標 \n{nonzero_img}")

print("------------------------------------------------------------")  # 60個

# ch17_12.py

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")
nonzero_img = np.nonzero(img)  # 獲得非0元素座標
loc_img = np.transpose(nonzero_img)  # 執行矩陣轉置
print(f"非0元素的座標 \n{loc_img}")

print("------------------------------------------------------------")  # 60個

# ch17_13.py

src = cv2.imread("simple.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]  # 取得輪廓數據
mask1 = np.zeros(src_gray.shape, np.uint8)  # 建立畫布
dst1 = cv2.drawContours(mask1, [cnt], 0, 255, 1)  # 繪製空心輪廓
points1 = np.transpose(np.nonzero(dst1))
mask2 = np.zeros(src_gray.shape, np.uint8)  # 建立畫布
dst2 = cv2.drawContours(mask2, [cnt], 0, 255, -1)  # 繪製實心輪廓
points2 = np.transpose(np.nonzero(dst2))
print(f"空心像素點長度 = {len(points1)},   實心像素點長度 = {len(points2)}")
print("空心像素點")
print(points1)
print("實心像素點")
print(points2)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_14.py

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")
loc_img = cv2.findNonZero(img)  # 獲得非0元素座標
print(f"非0元素的座標 \n{loc_img}")

print("------------------------------------------------------------")  # 60個

# ch17_15.py

src = cv2.imread("simple.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]  # 取得輪廓數據
mask1 = np.zeros(src_gray.shape, np.uint8)  # 建立畫布
dst1 = cv2.drawContours(mask1, [cnt], 0, 255, 1)  # 繪製空心輪廓
points1 = cv2.findNonZero(dst1)
mask2 = np.zeros(src_gray.shape, np.uint8)  # 建立畫布
dst2 = cv2.drawContours(mask2, [cnt], 0, 255, -1)  # 繪製實心輪廓
points2 = cv2.findNonZero(dst2)
print(f"空心像素點長度 = {len(points1)},   實心像素點長度 = {len(points2)}")
print("空心像素點")
print(points1)
print("實心像素點")
print(points2)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_16.py

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(256, size=(height, width))  # 建立矩陣
print(f"矩陣內容 = \n{img}")
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(img)
print(f"最小值 = {minVal},  位置 = {minLoc}")  # 最小值與其位置
print(f"最大值 = {maxVal},  位置 = {maxLoc}")  # 最大值與其位置

print("------------------------------------------------------------")  # 60個

# ch17_17.py

src = cv2.imread("hand.jpg")  # 手上有一黑點與一白點
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(src_gray, 50, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]
mask = np.zeros(src_gray.shape, np.uint8)  # 建立遮罩
mask = cv2.drawContours(mask, [cnt], -1, (255, 255, 255), -1)
cv2.imshow("mask", mask)
# 在src_gray影像的mask遮罩區域找尋最大像素與最小像素值
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(src_gray, mask=mask)
print(f"最小像素值 = {minVal}")
print(f"最小像素值座標 = {minLoc}")
print(f"最大像素值 = {maxVal}")
print(f"最大像素值座標 = {maxLoc}")
cv2.circle(src, minLoc, 20, [0, 255, 0], 3)  # 最小像素值用綠色圓
cv2.circle(src, maxLoc, 20, [0, 0, 255], 3)  # 最大像素值用紅色圓
# 建立遮罩未來可以顯示此感興趣的遮罩區域
mask1 = np.zeros(src.shape, np.uint8)  # 建立遮罩
mask1 = cv2.drawContours(mask1, [cnt], -1, (255, 255, 255), -1)
cv2.imshow("mask1", mask1)
dst = cv2.bitwise_and(src, mask1)  # 顯示感興趣區域
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_18.py

src = cv2.imread("forest.png")
cv2.imshow("src", src)

channels = cv2.mean(src)  # 計算均值
print(channels)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_19.py

src = cv2.imread("hand.jpg")  # 手上有一黑點與一白點
cv2.imshow("src", src)

channels = cv2.mean(src)  # 計算均值
print(channels)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_20.py

src = cv2.imread("hand.jpg")  # 手上有一黑點與一白點
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(src_gray, 50, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]
# 在src_gray影像的mask遮罩區域計算均值
mask = np.zeros(src_gray.shape, np.uint8)  # 建立遮罩
mask = cv2.drawContours(mask, [cnt], -1, (255, 255, 255), -1)
channels = cv2.mean(src, mask=mask)  # 計算遮罩的均值
print(channels)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_21.py

src = cv2.imread("forest.png")
cv2.imshow("src", src)

mean, std = cv2.meanStdDev(src)  # 計算標準差
print(f"均值   = \n{mean}")
print(f"標準差 = \n{std}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_18_從直線檢測到無人駕駛車道檢測
print("------------------------------------------------------------")  # 60個

# ch18_1.py

src = cv2.imread("calendar.jpg", cv2.IMREAD_COLOR)
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉成灰階
edges = cv2.Canny(src_gray, 100, 200)  # 使用Canny邊緣檢測
cv2.imshow("Canny", edges)  # 顯示Canny邊緣線條
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)  # 檢測直線
# 繪製直線
for line in lines:
    rho, theta = line[0]  # lines回傳
    a = np.cos(theta)  # cos(theta)
    b = np.sin(theta)  # sin(theta)
    x0 = rho * a
    y0 = rho * b
    x1 = int(x0 + 1000 * (-b))  # 建立 x1
    y1 = int(y0 + 1000 * (a))  # 建立 y1
    x2 = int(x0 - 1000 * (-b))  # 建立 x2
    y2 = int(y0 - 1000 * (a))  # 建立 y2
    cv2.line(src, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 繪製綠色線條
cv2.imshow("dst", src)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch18_2.py

src = cv2.imread("lane.jpg", cv2.IMREAD_COLOR)
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉成灰階
edges = cv2.Canny(src_gray, 100, 200)  # 使用Canny邊緣檢測
# cv2.imshow("Canny", edges)                         # 顯示Canny邊緣線條
lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)  # 檢測直線
# 繪製直線
for line in lines:
    rho, theta = line[0]  # lines回傳
    a = np.cos(theta)  # cos(theta)
    b = np.sin(theta)  # sin(theta)
    x0 = rho * a
    y0 = rho * b
    x1 = int(x0 + 1000 * (-b))  # 建立 x1
    y1 = int(y0 + 1000 * (a))  # 建立 y1
    x2 = int(x0 - 1000 * (-b))  # 建立 x2
    y2 = int(y0 - 1000 * (a))  # 建立 y2
    cv2.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 繪製紅色線條
cv2.imshow("dst", src)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch18_3.py

src = cv2.imread("roadtest.jpg", cv2.IMREAD_COLOR)
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉成灰階
edges = cv2.Canny(src_gray, 50, 200)  # 使用Canny邊緣檢測
cv2.imshow("Canny", edges)  # 顯示Canny邊緣線條
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=10, maxLineGap=100)
# 繪製檢測到的直線
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(src, (x1, y1), (x2, y2), (255, 0, 0), 3)  # 繪製藍色線條
cv2.imshow("dst", src)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch18_4.py

src = cv2.imread("shapes.jpg")
cv2.imshow("src", src)

image = cv2.medianBlur(src, 5)  # 過濾雜訊

src_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉成灰階
circles = cv2.HoughCircles(
    src_gray,
    cv2.HOUGH_GRADIENT,
    1,
    100,
    param1=50,
    param2=30,
    minRadius=70,
    maxRadius=200,
)
circles = np.uint(np.around(circles))  # 轉成整數
# 繪製檢測到的直線
for c in circles[0]:
    x, y, r = c
    cv2.circle(src, (x, y), r, (0, 255, 0), 3)  # 綠色繪圓外圈
    cv2.circle(src, (x, y), 2, (0, 0, 255), 2)  # 紅色繪圓中心
cv2.imshow("dst", src)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_19_直方圖均衡化—增強影像對比度
print("------------------------------------------------------------")  # 60個

# ch19_1.py

seq = [1, 2, 3, 4, 5]  # 像素值
times = [2, 1, 2, 1, 3]  # 出現次數
plt.plot(seq, times, "-o")  # 繪含標記的圖
plt.axis([0, 6, 0, 4])  # 建立軸大小
plt.xlabel("Pixel Value")  # 像素值
plt.ylabel("Times")  # 出現次數
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_2.py

times = [2, 1, 2, 1, 3]  # 出現次數
N = len(times)  # 計算長度
x = np.arange(N)  # 長條圖x軸座標
width = 0.35  # 長條圖寬度
plt.bar(x, times, width)  # 繪製長條圖

plt.xlabel("Pixel Value")  # 像素值
plt.ylabel("Times")  # 出現次數
plt.xticks(x, ("1", "2", "3", "4", "5"))
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_3.py

seq = [1, 2, 3, 4, 5]  # 像素值
freq = [2 / 9, 1 / 9, 2 / 9, 1 / 9, 3 / 9]  # 出現頻率
plt.plot(seq, freq, "-o")  # 繪含標記的圖
plt.axis([0, 6, 0, 0.5])  # 建立軸大小
plt.xlabel("Pixel Value")  # 像素值
plt.ylabel("Frequency")  # 出現頻率
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_4.py

freq = [2 / 9, 1 / 9, 2 / 9, 1 / 9, 3 / 9]  # 出現頻率
N = len(freq)  # 計算長度
x = np.arange(N)  # 長條圖x軸座標
width = 0.35  # 長條圖寬度
plt.bar(x, freq, width)  # 繪製長條圖

plt.xlabel("Pixel Value")  # 像素值
plt.ylabel("Freqency")  # 出現頻率
plt.xticks(x, ("1", "2", "3", "4", "5"))
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_5.py

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_7.py

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

hist = cv2.calcHist([src], [0], None, [256], [0, 256])  # 直方圖統計資料
print(f"資料類型 = {type(hist)}")
print(f"資料外觀 = {hist.shape}")
print(f"資料大小 = {hist.size}")
print(f"資料內容 \n{hist}")

print("------------------------------------------------------------")  # 60個

# ch19_8.py

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

hist = cv2.calcHist([src], [0], None, [256], [0, 258])  # 直方圖統計資料
plt.plot(hist)  # 用plot()繪直方圖
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_9.py

src = cv2.imread("macau.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Src", src)

b = cv2.calcHist([src], [0], None, [256], [0, 256])  # B 通道統計資料
g = cv2.calcHist([src], [1], None, [256], [0, 256])  # G 通道統計資料
r = cv2.calcHist([src], [2], None, [256], [0, 256])  # R 通道統計資料
plt.plot(b, color="blue", label="B channel")  # 用plot()繪 B 通道
plt.plot(g, color="green", label="G channel")  # 用plot()繪 G 通道
plt.plot(r, color="red", label="R channel")  # 用plot()繪 R 通道
plt.legend(loc="best")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_10.py

src = np.zeros([200, 400], np.uint8)  # 建立影像
src[50:150, 100:300] = 255  # 在影像內建立遮罩
cv2.imshow("Src", src)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_11.py

src = cv2.imread("macau.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

mask = np.zeros(src.shape[:2], np.uint8)  # 建立影像遮罩影像
mask[20:200, 50:400] = 255  # 在遮罩影像內建立遮罩
masked = cv2.bitwise_and(src, src, mask=mask)  # And運算
cv2.imshow("After Mask", masked)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_12.py

src = cv2.imread("macau.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

mask = np.zeros(src.shape[:2], np.uint8)  # 建立影像遮罩影像
mask[20:200, 50:400] = 255  # 在遮罩影像內建立遮罩
hist = cv2.calcHist([src], [0], None, [256], [0, 256])  # 灰階統計資料
hist_mask = cv2.calcHist([src], [0], mask, [256], [0, 256])  # 遮罩統計資料
plt.plot(hist, color="blue", label="Src Image")  # 用plot()繪影像直方圖
plt.plot(hist_mask, color="red", label="Mask")  # 用plot()繪遮罩直方圖
plt.legend(loc="best")
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_13.py

src = cv2.imread("macau.jpg", cv2.IMREAD_GRAYSCALE)
# 建立遮罩
mask = np.zeros(src.shape[:2], np.uint8)  # 建立影像遮罩影像
mask[20:200, 50:400] = 255  # 在遮罩影像內建立遮罩
aftermask = cv2.bitwise_and(src, src, mask=mask)

hist = cv2.calcHist([src], [0], None, [256], [0, 256])  # 灰階統計資料
hist_mask = cv2.calcHist([src], [0], mask, [256], [0, 256])  # 遮罩統計資料
# subplot()第一個 2 是代表垂直有 2 張圖, 第二個 2 是代表左右有 2 張圖
# subplot()第三個參數是代表子圖編號
plt.subplot(221)  # 建立子圖 1
plt.imshow(src, "gray")  # 灰階顯示第1張圖
plt.subplot(222)  # 建立子圖 2
plt.imshow(mask, "gray")  # 灰階顯示第2張圖
plt.subplot(223)  # 建立子圖 3
plt.imshow(aftermask, "gray")  # 灰階顯示第3張圖
plt.subplot(224)  # 建立子圖 4
plt.plot(hist, color="blue", label="Src Image")
plt.plot(hist_mask, color="red", label="Mask")
plt.legend(loc="best")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_14.py

src = cv2.imread("snow1.jpg", cv2.IMREAD_GRAYSCALE)
plt.subplot(221)  # 建立子圖 1
plt.imshow(src, "gray")  # 灰階顯示第1張圖
plt.subplot(222)  # 建立子圖 2
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.subplot(223)  # 建立子圖 3
dst = cv2.equalizeHist(src)  # 均衡化處理
plt.imshow(dst, "gray")  # 顯示執行均衡化的結果影像
plt.subplot(224)  # 建立子圖 4
plt.hist(dst.ravel(), 256)  # 降維再繪製直方圖
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_15.py

src = cv2.imread("springfield.jpg", cv2.IMREAD_GRAYSCALE)
plt.subplot(221)  # 建立子圖 1
plt.imshow(src, "gray")  # 灰階顯示第1張圖
plt.subplot(222)  # 建立子圖 2
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.subplot(223)  # 建立子圖 3
dst = cv2.equalizeHist(src)  # 均衡化處理
plt.imshow(dst, "gray")  # 顯示執行均衡化的結果影像
plt.subplot(224)  # 建立子圖 4
plt.hist(dst.ravel(), 256)  # 降維再繪製直方圖
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_16.py

src = cv2.imread("highway1.png", cv2.IMREAD_GRAYSCALE)
plt.subplot(221)  # 建立子圖 1
plt.imshow(src, "gray")  # 灰階顯示第1張圖
plt.subplot(222)  # 建立子圖 2
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.subplot(223)  # 建立子圖 3
dst = cv2.equalizeHist(src)  # 均衡化處理
plt.imshow(dst, "gray")  # 顯示執行均衡化的結果影像
plt.subplot(224)  # 建立子圖 4
plt.hist(dst.ravel(), 256)  # 降維再繪製直方圖
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_17.py

src = cv2.imread("springfield.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Src", src)

(b, g, r) = cv2.split(src)  # 拆開彩色影像通道
blue = cv2.equalizeHist(b)  # 均衡化 B 通道
green = cv2.equalizeHist(g)  # 均衡化 G 通道
red = cv2.equalizeHist(r)  # 均衡化 R 通道
dst = cv2.merge((blue, green, red))  # 合併通道
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_18.py

src = cv2.imread("office.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

equ = cv2.equalizeHist(src)  # 直方圖均衡化
cv2.imshow("euualizeHist", equ)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_19.py

src = cv2.imread("office.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

# 自適應直方圖均衡化
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
dst = clahe.apply(src)  # 灰度影像與clahe物件關聯
cv2.imshow("CLAHE", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_20_模板匹配 Template Matching
print("------------------------------------------------------------")  # 60個

# ch20_1.py

src = cv2.imread("macau_hotel.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Src", src)

H, W = src.shape[:2]
print(f"原始影像高 H = {H}, 寬 W = {W}")
temp1 = cv2.imread("head.jpg")
cv2.imshow("Temp1", temp1)  # 顯示模板影像
h, w = temp1.shape[:2]
print(f"模板影像高 h = {h}, 寬 w = {w}")
result = cv2.matchTemplate(src, temp1, cv2.TM_SQDIFF)
print(f"result大小 = {result.shape}")
print(f"陣列內容 \n{result}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_2.py

src = cv2.imread("shapes.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Src", src)

temp1 = cv2.imread("heart.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Temp1", temp1)  # 顯示模板影像
height, width = temp1.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_SQDIFF_NORMED執行模板匹配
result = cv2.matchTemplate(src, temp1, cv2.TM_SQDIFF_NORMED)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
upperleft = minLoc  # 左上角座標
lowerright = (minLoc[0] + width, minLoc[1] + height)  # 右下角座標
dst = cv2.rectangle(src, upperleft, lowerright, (0, 255, 0), 3)  # 繪置最相似外框
cv2.imshow("Dst", dst)
print(f"result大小 = {result.shape}")
print(f"陣列內容 \n{result}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_3.py

src = cv2.imread("g5.jpg", cv2.IMREAD_COLOR)
temp1 = cv2.imread("face1.jpg", cv2.IMREAD_COLOR)
height, width = temp1.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_SQDIFF_NORMED執行模板匹配
result = cv2.matchTemplate(src, temp1, cv2.TM_SQDIFF_NORMED)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
upperleft = minLoc  # 左上角座標
lowerright = (minLoc[0] + width, minLoc[1] + height)  # 右下角座標
dst = cv2.rectangle(src, upperleft, lowerright, (0, 255, 0), 3)  # 繪置最相似外框
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_4.py

src = []  # 建立原始影像陣列
src1 = cv2.imread("knight0.jpg", cv2.IMREAD_COLOR)
src.append(src1)  # 加入原始影像串列
src2 = cv2.imread("knight1.jpg", cv2.IMREAD_COLOR)
src.append(src2)  # 加入原始影像串列
temp1 = cv2.imread("knight.jpg", cv2.IMREAD_COLOR)
# 使用cv2.TM_SQDIFF_NORMED執行模板匹配
minValue = 1  # 設定預設的最小值
index = -1  # 設定最小值的索引
# 採用歸一化平方匹配法
for i in range(len(src)):
    result = cv2.matchTemplate(src[i], temp1, cv2.TM_SQDIFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    if minValue > minVal:
        minValue = minVal  # 紀錄目前的最小值
        index = i  # 紀錄目前的索引
seq = "knight" + str(index) + ".jpg"
print(f"{seq} 比較類似")
cv2.imshow("Dst", src[index])

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_5.py

src = cv2.imread("mutishapes.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Src", src)

temp1 = cv2.imread("heart.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Temp1", temp1)  # 顯示模板影像
height, width = temp1.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_CCOEFF_NORMED執行模板匹配
result = cv2.matchTemplate(src, temp1, cv2.TM_CCOEFF_NORMED)
for row in range(len(result)):  # 找尋row
    for col in range(len(result[row])):  # 找尋column
        if result[row][col] > 0.95:  # 值大於0.95就算找到了
            dst = cv2.rectangle(
                src, (col, row), (col + width, row + height), (0, 255, 0), 3
            )
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_6.py

src = cv2.imread("baidu.jpg", cv2.IMREAD_COLOR)
temp1 = cv2.imread("mountain_mark.jpg", cv2.IMREAD_COLOR)
h, w = temp1.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_CCOEFF_NORMED執行模板匹配
result = cv2.matchTemplate(src, temp1, cv2.TM_CCOEFF_NORMED)
for row in range(len(result)):  # 找尋row
    for col in range(len(result[row])):  # 找尋column
        if result[row][col] > 0.95:  # 值大於0.95就算找到了
            dst = cv2.rectangle(src, (col, row), (col + w, row + h), (0, 0, 255), 3)
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_7.py

start_x = 450  # 目前位置 x
start_y = 180  # 目前位置 y
src = cv2.imread("airport.jpg", cv2.IMREAD_COLOR)
temp1 = cv2.imread("airport_mark.jpg", cv2.IMREAD_COLOR)
dst = cv2.circle(src, (start_x, start_y), 10, (255, 0, 0), -1)
h, w = temp1.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_CCOEFF_NORMED執行模板匹配
ul_x = []  # 最佳匹配左上角串列 x
ul_y = []  # 最佳匹配左上較串列 y
result = cv2.matchTemplate(src, temp1, cv2.TM_CCOEFF_NORMED)
for row in range(len(result)):  # 找尋row
    for col in range(len(result[row])):  # 找尋column
        if result[row][col] > 0.9:  # 值大於0.9就算找到了
            dst = cv2.rectangle(src, (col, row), (col + w, row + h), (255, 0, 0), 2)
            ul_x.append(col)  # 加入最佳匹配串列 x
            ul_y.append(row)  # 加入最佳匹配串列 y
# 計算目前位置到台北機場的距離
sub_x = start_x - ul_x[0]  # 計算 x 座標差距
sub_y = start_y - ul_y[0]  # 計算 y 座標差距
start_taipei = math.hypot(sub_x, sub_y)  # 計算距離
print(f"目前位置到台北機場的距離 = {start_taipei:8.2f}")
# 計算目前位置到桃園機場的距離
sub_x = start_x - ul_x[1]  # 計算 x 座標差距
sub_y = start_y - ul_y[1]  # 計算 y 座標差距
start_taoyuan = math.hypot(sub_x, sub_y)  # 計算距離
print(f"目前位置到桃園機場的距離 = {start_taoyuan:8.2f}")
# 計算最短距離
if start_taipei > start_taoyuan:  # 距離比較
    cv2.line(src, (start_x, start_y), (ul_x[0], ul_y[0]), (255, 0, 0), 2)
else:
    cv2.line(src, (start_x, start_y), (ul_x[1], ul_y[1]), (255, 0, 0), 2)
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_8.py


def myMatch(image, tmp):
    """執行匹配"""
    h, w = tmp.shape[0:2]  # 回傳height, width
    result = cv2.matchTemplate(src, tmp, cv2.TM_CCOEFF_NORMED)
    for row in range(len(result)):  # 找尋row
        for col in range(len(result[row])):  # 找尋column
            if result[row][col] > 0.95:  # 值大於0.95就算找到了
                match.append([(col, row), (col + w, row + h)])  # 左上與右下點加入串列
    return


src = cv2.imread("mutishapes1.jpg", cv2.IMREAD_COLOR)  # 讀取原始影像
temps = []
temp1 = cv2.imread("heart1.jpg", cv2.IMREAD_COLOR)  # 讀取匹配影像
temps.append(temp1)  # 加入匹配串列temps
temp2 = cv2.imread("star.jpg", cv2.IMREAD_COLOR)  # 讀取匹配影像
temps.append(temp2)  # 加入匹配串列temps
match = []  # 符合匹配的圖案
for t in temps:
    myMatch(src, t)  # 調用 myMatch
for img in match:
    dst = cv2.rectangle(src, (img[0]), (img[1]), (0, 255, 0), 1)  # 繪外框
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# OpenCV_21_傅立葉變換
print("------------------------------------------------------------")  # 60個

# ch21_1.py

seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # 時間值
water = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 水
sugar = [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]  # 糖
grass = [4, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0]  # 仙草
pearl = [3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0]  # 黑珍珠
plt.plot(seq, water, "-o", label="水")  # 繪含標記的water折線圖
plt.plot(seq, sugar, "-x", label="糖")  # 繪含標記的sugar折線圖
plt.plot(seq, grass, "-s", label="仙草")  # 繪含標記的grass折線圖
plt.plot(seq, pearl, "-p", label="黑珍珠")  # 繪含標記的pearl折線圖
plt.legend(loc="best")
plt.axis([0, 12, 0, 5])  # 建立軸大小
plt.xlabel("時間軸")  # 時間軸
plt.ylabel("份數")  # 份數
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_10.py

src = cv2.imread("shape2.jpg", cv2.IMREAD_GRAYSCALE)
# 轉成頻率域
dft = cv2.dft(np.float32(src), flags=cv2.DFT_COMPLEX_OUTPUT)
dftshift = np.fft.fftshift(dft)  # 0 頻率分量移至中心
# 計算映射到[0,255]的振幅
spectrum = 20 * np.log(cv2.magnitude(dftshift[:, :, 0], dftshift[:, :, 1]))
# 執行逆傅立葉
idftshift = np.fft.ifftshift(dftshift)
tmp = cv2.idft(idftshift)
dst = cv2.magnitude(tmp[:, :, 0], tmp[:, :, 1])

plt.subplot(131)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像shape2.jpg")
plt.axis("off")  # 不顯示座標軸
plt.subplot(132)  # 繪製中間頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.subplot(133)  # 繪製右邊逆傅立葉圖
plt.imshow(dst, cmap="gray")  # 灰階顯示
plt.title("逆傅立葉影像")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_11.py

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
# 傅立葉變換
dft = cv2.dft(np.float32(src), flags=cv2.DFT_COMPLEX_OUTPUT)
dftshift = np.fft.fftshift(dft)  # 0 頻率分量移至中心
# 低通濾波器
rows, cols = src.shape  # 取得影像外形
row, col = rows // 2, cols // 2  # rows, cols的中心
mask = np.zeros((rows, cols, 2), np.uint8)
mask[row - 30 : row + 30, col - 30 : col + 30] = 1  # 設定區塊為低頻率分量是1

fshift = dftshift * mask
ifshift = np.fft.ifftshift(fshift)  # 0 頻率分量移回左上角
src_tmp = cv2.idft(ifshift)  # 逆傅立葉
src_back = cv2.magnitude(src_tmp[:, :, 0], src_tmp[:, :, 1])

plt.subplot(131)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(132)  # 繪製中間圖
plt.imshow(src_back, cmap="gray")  # 灰階顯示
plt.title("低通濾波灰階影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(133)  # 繪製右邊圖
plt.imshow(src_back)  # 顯示
plt.title("低通濾波影像")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_2.py

copies = [1, 2, 4, 3]  # 份數
N = len(copies)
x = np.arange(N)
width = 0.35
plt.bar(x, copies, width)  # 直條圖
plt.xlabel("頻率")  # 頻率
plt.ylabel("份數")  # 份數
plt.xticks(x, ("1", "2", "3", "4"))
plt.grid(axis="y")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_3.py

start = 0
end = 1
x = np.linspace(start, end, 500)  # x 軸區間
y = np.sin(2 * np.pi * 4 * x)  # 建立正弦曲線
plt.plot(x, y)
plt.xlabel("時間(秒)")  # 時間
plt.ylabel("振幅")  # 振幅
plt.title("正弦曲線", fontsize=16)  # 標題
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_4.py

amplitude = [0, 0, 0, 1, 0, 0, 0]
N = len(amplitude)
x = np.arange(N)
width = 0.3
plt.bar(x, amplitude, width)  # 直條圖
plt.xlabel("頻率")  # 頻率
plt.ylabel("振幅")  # 振幅
plt.xticks(x, ("1", "2", "3", "4", "5", "6", "7"))
plt.grid(axis="y")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_5.py

start = 0
# 起始時間
end = 5
# 結束時間
# 兩個正弦波的訊號頻率
freq1 = 5
# 頻率是 5 Hz
freq2 = 8
# 頻率是 8 Hz
# 建立時間軸的Numpy陣列, 用500個點
time = np.linspace(start, end, 500)
# 建立2個正弦波
amplitude1 = np.sin(2 * np.pi * freq1 * time)
amplitude2 = np.sin(2 * np.pi * freq2 * time)
# 建立子圖
figure, axis = plt.subplots(3, 1)
plt.subplots_adjust(hspace=1)
# 時間域的 sin 波 1
axis[0].set_title("頻率是 5 Hz的 sin 波")
axis[0].plot(time, amplitude1)
axis[0].set_xlabel("時間")
axis[0].set_ylabel("振幅")
# 時間域的 sin 波 2
axis[1].set_title("頻率是 8 Hz的 sin 波")
axis[1].plot(time, amplitude2)
axis[1].set_xlabel("時間")
axis[1].set_ylabel("振幅")
# 加總sin波
amplitude = amplitude1 + amplitude2
axis[2].set_title("2個不同頻率正弦波的結果")
axis[2].plot(time, amplitude)
axis[2].set_xlabel("時間")
axis[2].set_ylabel("振幅")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_6.py

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(src)  # 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
spectrum = 20 * np.log(np.abs(fshift))  # 轉成頻譜
plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_6_1.py

src = cv2.imread("shape1.jpg", cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(src)  # 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
spectrum = 20 * np.log(np.abs(fshift))  # 轉成頻譜
plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像shape1.jpg")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_6_2.py

src = cv2.imread("shape2.jpg", cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(src)  # 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
spectrum = 20 * np.log(np.abs(fshift))  # 轉成頻譜
plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像shape2.jpg")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_6_3.py

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(src)  # 轉成頻率域
# fshift = np.fft.fftshift(f)            # 0 頻率分量移至中心
spectrum = 20 * np.log(np.abs(f))  # 轉成頻譜
plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_7.py

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
# 傅立葉變換
f = np.fft.fft2(src)  # 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
# 逆傅立葉變換
ifshift = np.fft.ifftshift(fshift)  # 0 頻率頻率移回左上角
src_tmp = np.fft.ifft2(ifshift)  # 逆傅立葉
src_back = np.abs(src_tmp)  # 取絕對值

plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊逆運算圖
plt.imshow(src_back, cmap="gray")  # 灰階顯示
plt.title("逆變換影像")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_8.py

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
# 傅立葉變換
f = np.fft.fft2(src)  # 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
# 高通濾波器
rows, cols = src.shape  # 取得影像外形
row, col = rows // 2, cols // 2  # rows, cols的中心
fshift[row - 30 : row + 30, col - 30 : col + 30] = 0  # 設定區塊為低頻率分量是0
# 逆傅立葉變換
ifshift = np.fft.ifftshift(fshift)  # 0 頻率分量移回左上角
src_tmp = np.fft.ifft2(ifshift)  # 逆傅立葉
src_back = np.abs(src_tmp)  # 取絕對值

plt.subplot(131)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(132)  # 繪製中間圖
plt.imshow(src_back, cmap="gray")  # 灰階顯示
plt.title("高通濾波灰階影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(133)  # 繪製右邊圖
plt.title("高通濾波影像")
plt.imshow(src_back)  # 顯示影像
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_9.py

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
# 轉成頻率域
dft = cv2.dft(np.float32(src), flags=cv2.DFT_COMPLEX_OUTPUT)
dftshift = np.fft.fftshift(dft)  # 0 頻率分量移至中心
# 計算映射到[0,255]的振幅
spectrum = 20 * np.log(cv2.magnitude(dftshift[:, :, 0], dftshift[:, :, 1]))
plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個
# OpenCV_22_影像分割使用分水嶺演算法
print("------------------------------------------------------------")  # 60個

# ch22_1.py

src = cv2.imread("coin1.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch22_1.py

src = cv2.imread("coin2.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch22_2.py

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(133)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch22_2_1.py

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
# 執行開運算 Opening
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.5 * dst.max(), 255, 0)  # 前景圖案
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(133)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch22_2_2.py

src = cv2.imread("coin1.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
# 執行開運算 Opening
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(133)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch22_3.py

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
plt.subplot(141)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(142)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(143)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.subplot(144)
plt.title("未知區域")
plt.imshow(unknown)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch22_4.py

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# 標記
ret, markers = cv2.connectedComponents(sure_fg)
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("未知區域")
plt.imshow(unknown)
plt.axis("off")
plt.subplot(133)
plt.title("標記區")
plt.imshow(markers)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch22_5.py

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# 標記
ret, markers = cv2.connectedComponents(sure_fg)
# 先複製再標記修訂
sure_fg_copy = sure_fg.copy()
ret, markers_new = cv2.connectedComponents(sure_fg_copy)
markers_new += 1  # 標記修訂
markers_new[unknown == 255] = 0
plt.subplot(131)
plt.title("未知區域")
plt.imshow(unknown)
plt.axis("off")
plt.subplot(132)
plt.title("標記區")
plt.imshow(markers, cmap="jet")
plt.axis("off")
plt.subplot(133)
plt.title("標記修訂區")
plt.imshow(markers_new, cmap="jet")
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch22_6.py

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# 標記
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0
# 正式執行分水嶺函數
dst = rgb_src.copy()
markers = cv2.watershed(dst, markers)
dst[markers == -1] = [255, 0, 0]  # 使用紅色
plt.subplot(121)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(122)
plt.title("分割結果")
plt.imshow(dst)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個
# OpenCV_23_影像擷取
print("------------------------------------------------------------")  # 60個

# ch23_1.py

src = cv2.imread("hung.jpg")  # 讀取影像
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (10, 30, 380, 360)  # 建立ROI區域
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1
# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT
)
# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(121)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(122)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch23_2.py

src = cv2.imread("hung.jpg")  # 讀取影像
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (10, 30, 380, 360)  # 建立ROI區域
# 呼叫grabCut()進行分割
cv2.grabCut(src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT)
maskpict = cv2.imread("hung_mask.jpg")  # 讀取影像
newmask = cv2.imread("hung_mask.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取
mask[newmask == 0] = 0  # 白色內容則確定是前景
mask[newmask == 255] = 1  # 黑色內容則確定是背景
cv2.grabCut(src, mask, None, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_MASK)
mask = np.where((mask == 0) | (mask == 2), 0, 1).astype("uint8")
dst = src * mask[:, :, np.newaxis]  # 計算輸出影像
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
maskpict_rgb = cv2.cvtColor(maskpict, cv2.COLOR_BGR2RGB)
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(131)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(132)
plt.title("遮罩影像")
plt.imshow(maskpict_rgb)
plt.axis("off")
plt.subplot(133)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch23_3.py

src = cv2.imread("lena.jpg")  # 讀取影像
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (30, 30, 280, 280)  # 建立ROI區域
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1
# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT
)
# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(121)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(122)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch23_4.py

src = cv2.imread("lena.jpg")  # 讀取影像
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (30, 30, 280, 280)  # 建立ROI區域
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
mask[30:324, 30:300] = 3
mask[90:200, 90:200] = 1
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1
# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, None, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_MASK
)
# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(121)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(122)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個
# OpenCV_24_影像修復
print("------------------------------------------------------------")  # 60個

# ch24_1.py

# 修復影像 inpaint

lisa = cv2.imread("lisaE1.jpg")
ret, mask = cv2.threshold(lisa, 250, 255, cv2.THRESH_BINARY)
# 遮罩處理, 適度增加要處理的表面
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.dilate(mask, kernal)
dst = cv2.inpaint(lisa, mask[:, :, -1], 5, cv2.INPAINT_NS)
# 輸出執行結果
lisa_rgb = cv2.cvtColor(lisa, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
mask_rgb = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(131)
plt.title("原始影像")
plt.imshow(lisa_rgb)
plt.axis("off")
plt.subplot(132)
plt.title("遮罩影像")
plt.imshow(mask_rgb)
plt.axis("off")
plt.subplot(133)
plt.title("影像修復結果")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch24_2.py

lisa = cv2.imread("lisaE2.jpg")
ret, mask = cv2.threshold(lisa, 250, 255, cv2.THRESH_BINARY)
# 遮罩處理, 適度增加要處理的表面
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.dilate(mask, kernal)
dst = cv2.inpaint(lisa, mask[:, :, -1], 5, cv2.INPAINT_TELEA)
# 輸出執行結果
lisa_rgb = cv2.cvtColor(lisa, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
mask_rgb = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(131)
plt.title("原始影像")
plt.imshow(lisa_rgb)
plt.axis("off")
plt.subplot(132)
plt.title("遮罩影像")
plt.imshow(mask_rgb)
plt.axis("off")
plt.subplot(133)
plt.title("影像修復結果")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個
# OpenCV_25_辨識手寫數字
print("------------------------------------------------------------")  # 60個

# ch25_1.py

data1 = np.random.randint(0, 10, size=5)
print(f"陣列外形 = {data1.shape}")
print(f"輸出陣列 = {data1}")
print(f"data1[0] = {data1[0]}")
data2 = np.random.randint(0, 10, size=(5, 1))
print(f"矩陣外形 = {data2.shape}")
print(f"輸出矩陣 = \n{data2}")
print(f"data2[0] = {data2[0]}")
print(f"data2[0,0] = {data2[0,0]}")

print("------------------------------------------------------------")  # 60個

# ch25_10.py
# np.vsplit() 垂直方向分割數據

data = np.arange(16).reshape(2, 2, 2, 2)
print(f"data = \n {data}")
print(f"data = \n {np.vsplit(data,2)}")

print("------------------------------------------------------------")  # 60個

# ch25_11.py
# np.hsplit() 水平方向分割數據

data = np.arange(16).reshape(4, 4)
print(f"data = \n {data}")
print(f"split = \n{np.hsplit(data,2)}")

print("------------------------------------------------------------")  # 60個

# ch25_11_1.py
# np.repeat() 元素重複

data = np.arange(3)
print(f"data = \n {data}")
x = np.repeat(data, 3)
print(f"After repeat = \n{x}")

print("------------------------------------------------------------")  # 60個

# ch25_11_2.py

data = np.array([[1, 2], [3, 4]])
print(f"data = \n {data}")
x1 = np.repeat(data, 3, axis=1)
print(f"After axis=1 repeat  = \n{x1}")
x2 = np.repeat(data, 3, axis=0)
print(f"After axis=0 repeat = \n{x2}")

print("------------------------------------------------------------")  # 60個

# ch25_11_3.py

data = np.arange(3)
print(f"data = \n {data}")
x = np.repeat(data, 3)[:, np.newaxis]
print(f"After repeat = \n{x}")

print("------------------------------------------------------------")  # 60個

# ch25_12.py

"""
digits.png
手寫數字0~9, 每個數字重複寫500次, 共5000個手寫數字
"""
img = cv2.imread("digits.png")
cv2.imshow("digits", img)

cv2.waitKey()
cv2.destroyAllWindows()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 將digits拆成 5000 張, 20 x 20 的數字影像
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
# 將 cells 轉成 50 x 100 x 20 x 20 的陣列
x = np.array(cells)
# 將數據轉為訓練數據 size=(2500,400)和測試數據 size=(2500,400)
train = x[:, :50].reshape(-1, 400).astype(np.float32)
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)
# 建立訓練數據和測試數據的分類 labels
k = np.arange(10)
train_labels = np.repeat(k, 250)[:, np.newaxis]
test_labels = train_labels.copy()
# 最初化KNN或稱建立KNN物件，訓練數據、使用 k=5 測試KNN演算法
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, k=5)
# 統計辨識結果
matches = result == test_labels  # 執行匹配
correct = np.count_nonzero(matches)  # 正確次數
accuracy = correct * 100.0 / result.size  # 精確度
print(f"測試數據辨識成功率 = {accuracy}")

print("------------------------------------------------------------")  # 60個

# ch25_13.py

img = cv2.imread("digits.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 將digits拆成 5000 張, 20 x 20 的數字影像
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
# 將 cells 轉成 50 x 100 x 20 x 20 的陣列
x = np.array(cells)
# 將數據轉為訓練數據 size=(2500,400)和測試數據 size=(2500,400)
train = x[:, :50].reshape(-1, 400).astype(np.float32)
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)
# 建立訓練數據和測試數據的分類 labels
k = np.arange(10)
train_labels = np.repeat(k, 250)[:, np.newaxis]
test_labels = train_labels.copy()
# 最初化KNN或稱建立KNN物件，訓練數據、使用 k=5 測試KNN演算法
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, k=5)
# 統計辨識結果
matches = result == test_labels  # 執行匹配
correct = np.count_nonzero(matches)  # 正確次數
accuracy = correct * 100.0 / result.size  # 精確度
print(f"測試數據辨識成功率 = {accuracy}")

# 儲存模型
np.savez("tmp_knn_digit.npz", train=train, train_labels=train_labels)

print("------------------------------------------------------------")  # 60個

# ch25_14.py

# 讀取模型
# 下載數據
with np.load("tmp_knn_digit.npz") as data:
    train = data["train"]
    train_labels = data["train_labels"]

# 讀取數字影像
test_img = cv2.imread("8.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("img", test_img)
img = cv2.resize(test_img, (20, 20)).reshape((1, 400))
test_data = img.astype(np.float32)  # 將資料轉成foat32

# 最初化KNN或稱建立KNN物件，訓練數據、使用 k=5 測試KNN演算法
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test_data, k=5)
print(f"識別的數字是 = {int(result[0,0])}")

print("------------------------------------------------------------")  # 60個

# ch25_2.py

np.random.seed(5)
data1 = np.random.randint(0, 10, size=5)
print(f"陣列外形 = {data1.shape}")
print(f"輸出陣列 = {data1}")
print(f"data1[0] = {data1[0]}")
data2 = np.random.randint(0, 10, size=(5, 1))
print(f"矩陣外形 = {data2.shape}")
print(f"輸出矩陣 = \n{data2}")
print(f"data2[0] = {data2[0]}")
print(f"data2[0,0] = {data2[0,0]}")

print("------------------------------------------------------------")  # 60個

# ch25_3.py

data = np.random.randint(0, 10, size=(5, 1))
print(f"輸出二維陣列 = \n{data}")
print(f"轉成一維陣列 = \n{data.ravel()}")

print("------------------------------------------------------------")  # 60個

# ch25_4.py

np.random.seed(1)
trains = np.random.randint(0, 10, size=(5, 2))
print(f"列出二維陣列 \n{trains}")
np.random.seed(5)
# 建立分類, 未來 0 代表 red,  1 代表 blue
labels = np.random.randint(0, 2, (5, 1))
print(f"列出顏色分類陣列 \n{labels}")
# 列出 0 代表的紅色
red = trains[labels.ravel() == 0]
print(f"輸出紅色的二維陣列 \n{red}")
print(f"配對取出 \n{red[:,0], red[:,1]}")
# 列出 1 代表的藍色
blue = trains[labels.ravel() == 1]
print(f"輸出藍色的二維陣列 \n{blue}")
print(f"配對取出 \n{blue[:,0], blue[:,1]}")

print("------------------------------------------------------------")  # 60個

# ch25_5.py

num = 30  # 數據數量
np.random.seed(5)
trains = np.random.randint(0, 100, size=(num, 2))
np.random.seed(1)
# 建立分類, 未來 0 代表 red,  1 代表 blue
labels = np.random.randint(0, 2, (num, 1))
# 列出紅色方塊訓練數據
red = trains[labels.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, "r", "s")  # 50是繪圖點大小
# 列出藍色三角形訓練數據
blue = trains[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, "b", "^")  # 50是繪圖點大小
plt.show()

print("------------------------------------------------------------")  # 60個

# ch25_6.py

num = 30  # 數據數量
np.random.seed(5)
# 建立訓練數據 train, 需轉為 32位元浮點數
trains = np.random.randint(0, 100, size=(num, 2)).astype(np.float32)
np.random.seed(1)
# 建立分類, 未來 0 代表 red,  1 代表 blue
labels = np.random.randint(0, 2, (num, 1)).astype(np.float32)
# 列出紅色方塊訓練數據
red = trains[labels.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, "r", "s")  # 50是繪圖點大小
# 列出藍色三角形訓練數據
blue = trains[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, "b", "^")  # 50是繪圖點大小
# test 為測試數據, 需轉為 32位元浮點數
np.random.seed(10)
test = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(test[:, 0], test[:, 1], 50, "g", "o")  # 50大小的綠色圓
# 建立 KNN 物件
knn = cv2.ml.KNearest_create()
knn.train(trains, cv2.ml.ROW_SAMPLE, labels)  # 訓練數據
# 執行 KNN 分類
ret, results, neighbours, dist = knn.findNearest(test, k=3)
print(f"最後分類              result = {results}")
print(f"最近鄰3個點的分類 neighbours = {neighbours}")
print(f"與最近鄰的距離      distance = {dist}")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch25_7.py

num = 30  # 數據數量
np.random.seed(5)
# 建立 0 - 50 間的訓練數據 train0, 需轉為 32位元浮點數
train0 = np.random.randint(0, 50, (num // 2, 2)).astype(np.float32)
# 建立 50 - 100 間的訓練數據 train1, 需轉為 32位元浮點數
train1 = np.random.randint(50, 100, (num // 2, 2)).astype(np.float32)
trains = np.vstack((train0, train1))  # 合併訓練數據
# 建立分類, 未來 0 代表 red,  1 代表 blue
label0 = np.zeros((num // 2, 1)).astype(np.float32)
label1 = np.ones((num // 2, 1)).astype(np.float32)
labels = np.vstack((label0, label1))
# 列出紅色方塊訓練數據
red = trains[labels.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, "r", "s")  # 50是繪圖點大小
# 列出藍色三角形訓練數據
blue = trains[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, "b", "^")  # 50是繪圖點大小
# test 為測試數據, 需轉為 32位元浮點數
np.random.seed(8)
test = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(test[:, 0], test[:, 1], 50, "g", "o")  # 50大小的綠色圓
# 建立 KNN 物件
knn = cv2.ml.KNearest_create()
knn.train(trains, cv2.ml.ROW_SAMPLE, labels)  # 訓練數據
# 執行 KNN 分類
ret, results, neighbours, dist = knn.findNearest(test, k=3)
print(f"最後分類              result = {results}")
print(f"最近鄰3個點的分類 neighbours = {neighbours}")
print(f"與最近鄰的距離      distance = {dist}")

plt.show()

print("------------------------------------------------------------")  # 60個

# ch25_8.py

data = np.arange(16).reshape(4, 4)
print(f"data = \n {data}")
print(f"split = \n{np.vsplit(data,2)}")

print("------------------------------------------------------------")  # 60個

# ch25_9.py

data = np.arange(8).reshape(2, 2, 2)
print(f"data = \n {data}")
print(f"split = \n{np.vsplit(data,2)}")

print("------------------------------------------------------------")  # 60個
# OpenCV_27_物件偵測
print("------------------------------------------------------------")  # 60個

"""
Haar-like features 哈爾特徵

匈牙利 Afred Haar
"""

# ch27_1.py
# 偵測正面人臉 haarcascade_frontalface_default.xml

pic_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face06.jpg"

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread(pic_filename)  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Found " + str(len(faces)) + " faces",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 偵測上半身 haarcascade_upperbody.xml

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_upperbody.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

# pic_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face06.jpg"

img = cv2.imread("people1.jpg")  # 讀取影像
bodies = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=9, minSize=(20, 20)
)

# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_11.py
# 偵測正面人臉 haarcascade_frontalface_default.xml

# 建立人臉物件
xml_filename1 = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier1 = cv2.CascadeClassifier(xml_filename1)  # 建立辨識檔案物件

# 建立雙眼物件
xml_filename2 = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_eye.xml"
face_cascade_classifier2 = cv2.CascadeClassifier(xml_filename2)  # 建立辨識檔案物件

img = cv2.imread(filename3)  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測人臉
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 偵測雙眼
eyes = face_cascade_classifier2.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
# 將雙眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_12.py
# 偵測正面人臉 haarcascade_frontalface_default.xml

# 建立人臉物件
xml_filename1 = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier1 = cv2.CascadeClassifier(xml_filename1)  # 建立辨識檔案物件

# 建立雙眼物件
xml_filename2 = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_eye.xml"
face_cascade_classifier2 = cv2.CascadeClassifier(xml_filename2)  # 建立辨識檔案物件

img = cv2.imread(filename3)  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 偵測人臉
faces = face_cascade_classifier1.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 偵測雙眼
eyes = face_cascade_classifier2.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=7, minSize=(20, 20)
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

# 將雙眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_13.py
# 偵測正面人臉 haarcascade_frontalface_default.xml

# 建立人臉物件
xml_filename1 = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier1 = cv2.CascadeClassifier(xml_filename1)  # 建立辨識檔案物件

# 建立左眼物件
xml_filename2 = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_lefteye_2splits.xml"
face_cascade_classifier2 = cv2.CascadeClassifier(xml_filename2)  # 建立辨識檔案物件

img = cv2.imread(filename3)  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 偵測人臉
faces = face_cascade_classifier1.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 偵測左眼
eyes = face_cascade_classifier2.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=7, minSize=(20, 20)
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

# 將左眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_14.py
# 偵測正面人臉 haarcascade_frontalface_default.xml

# 建立人臉物件
xml_filename1 = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier1 = cv2.CascadeClassifier(xml_filename1)  # 建立辨識檔案物件

# 建立右眼物件
xml_filename2 = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_righteye_2splits.xml"
face_cascade_classifier2 = cv2.CascadeClassifier(xml_filename2)  # 建立辨識檔案物件

img = cv2.imread(filename3)  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 偵測人臉
faces = face_cascade_classifier1.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 偵測右眼
eyes = face_cascade_classifier2.detectMultiScale(
    img, scaleFactor=1.3, minNeighbors=7, minSize=(20, 20)
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

# 將右眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_15.py

# 正面的貓臉 haarcascade_frontalcatface.xml

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalcatface.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("cat1.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 將貓臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住貓臉

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_16.py
# 正面的貓臉 haarcascade_frontalcatface.xml

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalcatface.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("cat2.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=9, minSize=(20, 20)
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_17.py
# 偵測車牌, 適用於俄羅斯車牌 haarcascade_russian_plate_number.xml

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_russian_plate_number.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("car.jpg")  # 讀取影像
plates = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 將車牌框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住車牌

cv2.imshow("Car Plate", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_18.py
# 偵測車牌, 適用於俄羅斯車牌 haarcascade_russian_plate_number.xml

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_russian_plate_number.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("car1.jpg")  # 讀取影像
plates = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 將車牌框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住車牌

cv2.imshow("Car Plate", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_19.py
# 偵測車牌, 適用於俄羅斯車牌 haarcascade_russian_plate_number.xml

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_russian_plate_number.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("car2.jpg")  # 讀取影像
plates = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 將車牌框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住車牌

cv2.imshow("Car Plate", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_2.py
# 偵測正面人臉 haarcascade_frontalface_default.xml

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("g5.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_3.py
# 偵測正面人臉 haarcascade_frontalface_default.xml

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_3_1.py
# 偵測正面人臉 haarcascade_frontalface_default.xml

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# ch27_4.py

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_alt.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)

# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_4_1.py

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_alt.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20), maxSize=(50, 50)
)

# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)

# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_5.py

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_alt2.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20), maxSize=(50, 50)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_6.py

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_alt_tree.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)

# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_6_1.py

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_alt.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("s_1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.02, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_6_2.py
# 偵測側面的人臉 haarcascade_profileface.xml

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_profileface.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("s_1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.3, minNeighbors=4, minSize=(20, 20)
)

# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)

# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_7.py
# 偵測身形 路人偵測 haarcascade_fullbody.xml

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_fullbody.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("people1.jpg")  # 讀取影像
bodies = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體

cv2.imshow("Body", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_8.py
# 偵測身形 路人偵測 haarcascade_fullbody.xml

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_fullbody.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("people2.jpg")  # 讀取影像
bodies = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體

cv2.imshow("Body", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_9.py

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_lowerbody.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("people1.jpg")  # 讀取影像
bodies = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體

cv2.imshow("Body", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


cv2.waitKey(3000)  # 等待3秒
cv2.destroyWindow("Peony1")  # 刪除Peony1
cv2.waitKey(8000)  # 等待8秒
cv2.destroyAllWindows()

ret = cv2.imwrite("tmp_out1_7_1.tiff", img)  # 將檔案寫入out1_7_1.tiff
ret = cv2.imwrite("tmp_out1_7_2.png", img)  # 將檔案寫入out1_7_2.png
cv2.imwrite("a32.png", a32_image)  # 儲存alpha=32影像

img = cv2.imread("jk.jpg")  # 彩色讀取

# 影像的屬性

print(f"shape = {img.shape}")
print(f"size  = {img.size}")
print(f"dtype = {img.dtype}")

print("------------------------------------------------------------")  # 60個

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取


print("------------------------------------------------------------")  # 60個

"""
陣列垂直合併 vstack()
陣列水平合併 hstack()
"""


img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("JK Hung", img)
