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
img = cv2.imread(filename1)  # 讀取影像
cv2.imshow("Peony", img)  # 顯示影像
cv2.imshow("Peony", img)  # 顯示影像
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
img = cv2.imread(filename1)  # 讀取影像
cv2.imshow("Peony", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch1_6.py

cv2.namedWindow("Peony1")  # 使用預設
cv2.namedWindow("Peony2", cv2.WINDOW_NORMAL)  # 可以調整大小
img1 = cv2.imread(filename1)  # 彩色讀取
img2 = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
cv2.imshow("Peony1", img1)  # 顯示影像img1
cv2.imshow("Peony2", img2)  # 顯示影像img2

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch1_6_1.py

cv2.namedWindow("Peony1")  # 使用預設
cv2.namedWindow("Peony2", cv2.WINDOW_NORMAL)  # 可以調整大小
img1 = cv2.imread(filename1)  # 彩色讀取
img2 = cv2.imread(filename1, 0)  # 灰色讀取
cv2.imshow("Peony1", img1)  # 顯示影像img1
cv2.imshow("Peony2", img2)  # 顯示影像img2

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
print(x)

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
print(x1)

x2 = np.ones((2, 3), dtype=np.uint8)
print(x2)

print("------------------------------------------------------------")  # 60個

# ch3_6.py

x1 = np.empty(3)
print(x1)

x2 = np.empty((2, 3), dtype=np.uint8)
print(x2)

print("------------------------------------------------------------")  # 60個

# ch3_7.py

x1 = np.random.randint(10, 20)
print("回傳值是10(含)至20(不含)的單一隨機數")
print(x1)

print("回傳一維陣列10個元素, 值是1(含)至5(不含)的隨機數")
x2 = np.random.randint(1, 5, 10)
print(x2)

print("回傳單3*5陣列, 值是0(含)至10(不含)的隨機數")
x3 = np.random.randint(10, size=(3, 5))
print(x3)

print("------------------------------------------------------------")  # 60個

# ch3_7_3.py

x = np.arange(16)
print(x)
print(np.reshape(x, (4, -1)))


print("------------------------------------------------------------")  # 60個

# ch3_7_4.py

x = np.arange(16)
print(x)
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

x1 = np.array([0, 1, 2, 3, 4, 5])
x2 = np.array(x1, copy=True)
print(x1)
print(x2)

x2[0] = 9
print(x1)
print(x2)

print("------------------------------------------------------------")  # 60個

# ch3_10.py

x1 = np.array([0, 1, 2, 3, 4, 5])
x2 = x1.copy()
print(x1)
print(x2)

x2[0] = 9
print(x1)
print(x2)

print("------------------------------------------------------------")  # 60個

# ch3_11.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
print(x4)

print("------------------------------------------------------------")  # 60個

# ch3_12.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
x5 = np.array([x4, x4])
print(x5)

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
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

# 建立GRAY影像陣列, 白色
image = np.zeros((height, width), np.uint8)
image.fill(255)  # 元素內容改為白色 255
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

# 建立GRAY影像陣列, 白色
image = np.ones((height, width), np.uint8) * 255
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_4.py

width, height = 640, 480  # 影像寬, 影像高

# 建立GRAY影像陣列, 黑色
image = np.zeros((height, width), np.uint8)

# 某塊塗為白色
image[40:120, 70:210] = 255  # 高在40至120之間,寬在70至210之間,設為255

cv2.imshow("image", image)  # 顯示影像

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
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_6.py

width, height = 640, 480  # 影像寬, 影像高

# 使用random.randint()建立GRAY影像陣列
image = np.random.randint(256, size=[height, width], dtype=np.uint8)
cv2.imshow("image", image)  # 顯示影像

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
cv2.imshow("image", image)  # 顯示影像

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
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_10.py

width, height = 640, 480  # 影像寬, 影像高

image = np.zeros((height, width, 3), np.uint8)
image[0:50, :, 0] = 255  # blue
image[50:100, :, 1] = 255  # green
image[100:150, :, 2] = 255  # red
cv2.imshow("image", image)  # 顯示影像

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
cv2.imshow("Peony", img)  # 顯示影像
face = img[70:220, 90:240]  # ROI, 先高後寬
cv2.imshow("Face", face)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch6_14.py

img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Peony", img)  # 顯示影像
# ROI大小區塊建立馬賽克
face = np.random.randint(0, 256, size=(190, 170, 3))  # 馬賽克效果
img[30:220, 80:250] = face  # ROI, 先高後寬
cv2.imshow("Face", img)  # 顯示影像

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

cv2.imshow("Image", lena)  # 顯示影像

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
res = cv2.add(img, img)
cv2.imshow("Peony1", img)  # 顯示影像img
cv2.imshow("Peony2", res)  # 顯示影像res

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch8_3.py

img = cv2.imread(filename1)  # 彩色讀取
res = cv2.add(img, img)  # 調整亮度結果
cv2.imshow("Peony1", img)  # 顯示影像img
cv2.imshow("Peony2", res)  # 顯示影像res

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch8_3_1.py

value = 20  # 亮度調整值
img = cv2.imread(filename1)  # 彩色讀取
coff = np.ones(img.shape, dtype=np.uint8) * value

res = cv2.add(img, coff)  # 調整亮度結果
cv2.imshow("Peony1", img)  # 顯示影像img
cv2.imshow("Peony2", res)  # 顯示影像res

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
res1 = cv2.add(img, img)
res2 = img + img
cv2.imshow("Peony1", img)  # 顯示影像img
cv2.imshow("Peony2", res1)  # 顯示影像res1
cv2.imshow("Peony3", res2)  # 顯示影像res2

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch8_6.py

img = cv2.imread(filename1)  # 彩色讀取
res1 = cv2.add(img, img)
res2 = img + img
cv2.imshow("Peony1", img)  # 顯示影像img
cv2.imshow("Peony2", res1)  # 顯示影像res1
cv2.imshow("Peony3", res2)  # 顯示影像res2

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
cv2.imshow("B channel", b)  # 顯示影像b
cv2.imshow("G channel", g)  # 顯示影像g
cv2.imshow("R channel", r)  # 顯示影像r

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
cv2.imshow("img1", img1)  # 顯示影像img1

img2 = np.zeros((height, width, 3), np.uint8)  # 建立img2影像
img2[:, :, 2] = 255
cv2.imshow("img2", img2)  # 顯示影像img2

m = np.zeros((height, width, 1), np.uint8)  # 建立mask(m)影像
m[50:150, 100:200, :] = 255  # 建立 ROI
cv2.imshow("mask", m)  # 顯示影像m

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

# ch8_11.py

src1 = np.random.randint(0, 255, (3, 5), dtype=np.uint8)

src2 = np.zeros((3, 5), dtype=np.uint8)
src2[0:2, 0:2] = 255  # 設定mask, 先高後寬

dst = cv2.bitwise_and(src1, src2)

print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {dst}")

print("------------------------------------------------------------")  # 60個

# ch8_12.py

# 灰階 mask 運算

src1 = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 讀取影像

src2 = np.zeros(src1.shape, dtype=np.uint8)  # 建立mask
src2[50:520, 150:360] = 255  # 設定mask, 先高後寬

dst = cv2.bitwise_and(src1, src2)  # 執行and運算

cv2.imshow("Before", src1)
cv2.imshow("Mask", src2)
cv2.imshow("After", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch8_13.py

# 彩色 mask 運算

src1 = cv2.imread(filename2)  # 讀取影像

src2 = np.zeros(src1.shape, dtype=np.uint8)  # 建立mask
src2[50:520, 150:360, :] = 255  # 設定mask, 先高後寬  # 這是3維陣列

dst = cv2.bitwise_and(src1, src2)  # 執行and運算

cv2.imshow("Before", src1)
cv2.imshow("Mask", src2)
cv2.imshow("After", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch8_14.py

src1 = np.random.randint(0, 255, (3, 5), dtype=np.uint8)

src2 = np.zeros((3, 5), dtype=np.uint8)
src2[0:2, 0:2] = 255  # 設定mask, 先高後寬

dst = cv2.bitwise_or(src1, src2)

print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {dst}")

print("------------------------------------------------------------")  # 60個

# ch8_15.py

src1 = cv2.imread(filename2)  # 讀取影像

src2 = np.zeros(src1.shape, dtype=np.uint8)  # 建立mask
src2[50:520, 150:360, :] = 255  # 設定mask, 先高後寬  # 這是3維陣列

dst = cv2.bitwise_or(src1, src2)  # 執行or運算

cv2.imshow("Before", src1)
cv2.imshow("Mask", src2)
cv2.imshow("After", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch8_16.py

src = cv2.imread(filename1)  # 讀取影像

dst = cv2.bitwise_not(src)  # 執行or運算

cv2.imshow("Before", src)
cv2.imshow("After", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch8_17.py

src1 = cv2.imread(filename1)  # 讀取影像

src2 = np.zeros(src1.shape, np.uint8)
src2[:, 140:280, :] = 255  # 設定mask, 先高後寬  # 建立mask白色區塊

dst = cv2.bitwise_xor(src1, src2)  # 執行xor運算

cv2.imshow("Before", src1)
cv2.imshow("Mask", src2)
cv2.imshow("After", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch8_18.py

src = cv2.imread(filename1)  # 讀取影像
key = np.random.randint(0, 256, src.shape, np.uint8)  # 密鑰影像
print(src.shape)

cv2.imshow("Before", src)  # 原始影像
cv2.imshow("key", key)  # 密鑰影像

img_encryp = cv2.bitwise_xor(src, key)  # 加密結果的影像
cv2.imshow("encryption", img_encryp)  # 加密結果影像

img_decryp = cv2.bitwise_xor(key, img_encryp)  # 解密結果的影像
cv2.imshow("decryption", img_decryp)  # 解密結果影像

cv2.waitKey()
cv2.destroyAllWindows()

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
cv2.imshow("src", src)  # 顯示原始影像
cv2.imshow("THRESH_BINARY", dst)  # 顯示二值化處理影像
cv2.imshow("ADAPTIVE_THRESH_MEAN_C", dst_mean)  # 顯示自適應閾值結果
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", dst_gauss)  # 顯示自適應閾值結果

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_22.py

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("JK Hung", img)

row, column = img.shape
x = np.zeros((row, column, 8), dtype=np.uint8)

for i in range(8):
    x[:, :, i] = 2**i  # 填上權重

result = np.zeros((row, column, 8), dtype=np.uint8)

for i in range(8):
    result[:, :, i] = cv2.bitwise_and(img, x[:, :, i])
    mask = result[:, :, i] > 0  # 影像邏輯值
    result[mask] = 255  # True的位置填255
    cv2.imshow(str(i), result[:, :, i])  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_23.py

jk = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("JK Hung", jk)  # 顯示原始影像

row, column = jk.shape  # 取得列高和欄寬

h7 = np.ones((row, column), dtype=np.uint8) * 254  # 建立像素值是254的影像
cv2.imshow("254", h7)  # 顯示像素值是254的影像

new_jk = cv2.bitwise_and(jk, h7)  # 原始影像最低有效位元是 0
cv2.imshow("New JK", new_jk)  # 顯示新影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_24.py

jk = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("JK Hung", jk)  # 顯示原始影像

row, column = jk.shape  # 取得列高和欄寬

h7 = np.ones((row, column), dtype=np.uint8) * 254  # 建立像素值是254的影像
tmp_jk = cv2.bitwise_and(jk, h7)  # 原始影像最低有效位元是 0
watermark = cv2.imread("copyright.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Copy Right", watermark)  # 顯示浮水印影像

ret, wm = cv2.threshold(watermark, 0, 1, cv2.THRESH_BINARY)
# 浮水印影像嵌入最低有效位元是 0的原始影像
new_jk = cv2.bitwise_or(tmp_jk, wm)
cv2.imshow("New JK", new_jk)  # 顯示新影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_25.py

jk = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("JK Hung", jk)  # 顯示原始影像

row, column = jk.shape  # 取得列高和欄寬
h7 = np.ones((row, column), dtype=np.uint8) * 254  # 建立像素值是254的影像
tmp_jk = cv2.bitwise_and(jk, h7)  # 原始影像最低有效位元是 0
watermark = cv2.imread("copyright.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("original watermark", watermark)  # 顯示浮水印影像

ret, wm = cv2.threshold(watermark, 0, 1, cv2.THRESH_BINARY)

new_jk = cv2.bitwise_or(tmp_jk, wm)  # 浮水印影像嵌入原始影像
cv2.imshow("New JK", new_jk)  # 顯示新影像

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

# ch10_1.py

src = cv2.imread(filename1)  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像
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

# ch10_3.py

print("原圖")
src = cv2.imread(filename1)  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像

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

# ch10_4.py

src = cv2.imread("rural.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像

height, width = src.shape[0:2]  # 獲得影像大小
dsize = (width, height)  # 建立未來影像大小
x = 50  # 平移 x = 50
y = 100  # 平移 y = 100
M = np.float32([[1, 0, x], [0, 1, y]])  # 建立 M 矩陣
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst", dst)  # 顯示平移結果影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_5.py
print("旋轉")

src = cv2.imread("rural.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像

height, width = src.shape[0:2]  # 獲得影像大小

print("逆時鐘轉 30 度")
M = cv2.getRotationMatrix2D((width / 2, height / 2), 30, 1)  # 建立 M 矩陣
dsize = (width, height)  # 建立未來影像大小
dst1 = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst - counterclockwise", dst1)  # 顯示逆時鐘影像

print("順時鐘轉 30 度")
M = cv2.getRotationMatrix2D((width / 2, height / 2), -30, 1)  # 建立 M 矩陣
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst clockwise", dst)  # 顯示順時鐘影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_6.py

src = cv2.imread("rural.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像

height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])  # src的A,B,C三個點
dstp = np.float32([[30, 0], [width - 1, 0], [0, height - 1]])  # dst的A,B,C三個點
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst", dst)  # 顯示傾斜影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_7.py

src = cv2.imread("rural.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像

height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])  # src的A,B,C三個點
dstp = np.float32([[0, 0], [width - 1 - 30, 0], [30, height - 1]])  # dst的A,B,C三個點
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst", dst)  # 顯示傾斜影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_8.py

src = cv2.imread("rural.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像

height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
a = [0, height * 0.2]  # A
b = [width * 0.8, height * 0.2]  # B
c = [width * 0.1, height * 0.9]  # C
dstp = np.float32([a, b, c])  # dst的 A, B, C
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst", dst)  # 顯示傾斜影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_9.py

src = cv2.imread("rural.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像

height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
a = [0, height * 0.4]  # A
b = [width * 0.8, height * 0.2]  # B
c = [width * 0.1, height * 0.9]  # C
dstp = np.float32([a, b, c])  # dst的 A, B, C
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst", dst)  # 顯示傾斜影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_10.py

src = cv2.imread("tunnel.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像

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
# OpenCV_11_刪除影像雜訊_濾波
print("------------------------------------------------------------")  # 60個

# ch11_1.py
print("使用 均值濾波器.blur()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

dst1 = cv2.blur(src, (3, 3))  # 使用 3x3 濾波核
dst2 = cv2.blur(src, (5, 5))  # 使用 5x5 濾波核
dst3 = cv2.blur(src, (7, 7))  # 使用 7x7 濾波核
dst4 = cv2.blur(src, (29, 29))  # 使用 29x29 濾波核

cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 5 x 5", dst2)
cv2.imshow("dst 7 x 7", dst3)
cv2.imshow("dst 29 x 29", dst4)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 方框濾波器.boxFilter()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

dst1 = cv2.boxFilter(src, -1, (2, 2), normalize=0)  # ksize是 2x2 的濾波核
dst2 = cv2.boxFilter(src, -1, (3, 3), normalize=0)  # ksize是 3x3 的濾波核
dst3 = cv2.boxFilter(src, -1, (5, 5), normalize=0)  # ksize是 5x5 的濾波核

cv2.imshow("dst 2 x 2", dst1)
cv2.imshow("dst 3 x 3", dst2)
cv2.imshow("dst 5 x 5", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 中值濾波器.medianBlur()")

src = np.ones((3, 3), np.float32) * 150
src[1, 1] = 20
print(f"原陣列 src = \n {src}")

dst = cv2.medianBlur(src, 3)
print(f"中值濾波後 dst = \n {dst}")

print("------------------------------------------------------------")  # 60個

print("使用 中值濾波器.medianBlur()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

dst1 = cv2.medianBlur(src, 3)  # 使用邊長是 3 的濾波核
dst2 = cv2.medianBlur(src, 5)  # 使用邊長是 5 的濾波核
dst3 = cv2.medianBlur(src, 7)  # 使用邊長是 7 的濾波核
cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 5 x 5", dst2)
cv2.imshow("dst 7 x 7", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 高斯濾波器.GaussianBlur()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

dst1 = cv2.GaussianBlur(src, (3, 3), 0, 0)  # 使用 3 x 3 的濾波核
dst2 = cv2.GaussianBlur(src, (5, 5), 0, 0)  # 使用 5 x 5 的濾波核
dst3 = cv2.GaussianBlur(src, (29, 29), 0, 0)  # 使用 29 x 29 的濾波核
cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 5 x 5", dst2)
cv2.imshow("dst 15 x 15", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 均值濾波器.blur() / 高斯濾波器.GaussianBlur()")

src = cv2.imread("border.jpg")

dst1 = cv2.blur(src, (3, 3))  # 均值濾波器 - 3x3 濾波核
dst2 = cv2.blur(src, (7, 7))  # 均值濾波器 - 7x7 濾波核

dst3 = cv2.GaussianBlur(src, (3, 3), 0, 0)  # 高斯濾波器 - 3x3 的濾波核
dst4 = cv2.GaussianBlur(src, (7, 7), 0, 0)  # 高斯濾波器 - 7x7 的濾波核

cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 7 x 7", dst2)
cv2.imshow("Gauss dst 3 x 3", dst3)
cv2.imshow("Gauss dst 7 x 7", dst4)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 均值濾波器.blur() / 高斯濾波器.GaussianBlur() / 雙邊濾波器.bilateralFilter()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

dst1 = cv2.blur(src, (15, 15))  # 均值濾波器
dst2 = cv2.GaussianBlur(src, (15, 15), 0, 0)  # 高斯濾波器
dst2 = cv2.bilateralFilter(src, 15, 100, 100)  # 雙邊濾波器

cv2.imshow("blur", dst1)
cv2.imshow("GaussianBlur", dst1)
cv2.imshow("bilateralFilter", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 2D濾波核.filter2D()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

kernel = np.ones((11, 11), np.float32) / 121  # 自訂卷積核
dst = cv2.filter2D(src, -1, kernel)  # 自定義濾波器
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

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

src = cv2.imread("macau.jpg")  # 讀取影像
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

src = cv2.imread("macau_small.jpg")  # 讀取影像

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

src = cv2.imread("pengiun.jpg")  # 讀取影像
cv2.imshow("src", src)

dst1 = src + src  # 影像相加
dst2 = src - src  # 影像相減

cv2.imshow("dst1 - add", dst1)
cv2.imshow("dst2 - subtraction", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("pengiun.jpg")  # 讀取影像
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

src = cv2.imread("pengiun.jpg")  # 讀取影像
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

src = cv2.imread("pengiun.jpg")  # 讀取影像

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

src = cv2.imread("pengiun.jpg")  # 讀取影像
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


# ch2_2.py

img = cv2.imread("jk.jpg")  # 彩色讀取

# 影像的屬性

print(f"shape = {img.shape}")
print(f"size  = {img.size}")
print(f"dtype = {img.dtype}")

print("------------------------------------------------------------")  # 60個

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取


print("------------------------------------------------------------")  # 60個
