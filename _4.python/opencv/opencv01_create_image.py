"""
OpenCV 基本使用


"""

import cv2

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個


def show():
    # return
    plt.show()
    pass


def cvshow(title, image):
    # return
    cv2.imshow(title, image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    pass


print("------------------------------------------------------------")  # 60個

print("各種建立畫布的方法")

print("建立畫布(黑色)")
W, H = 640, 480
# 快速產生 WxH，每個項目為 [0,0,0] 的三維陣列
image = np.zeros((H, W, 3), dtype="uint8")
# image = np.zeros((H, W,3), np.uint8)
# image = np.ones((H,W,3), np.uint8)*255  # 白色背景

# 白色背景
image = np.ones((H, W, 3), dtype="uint8") * 255

# 黑色背景
image = np.zeros((H, W, 3), dtype=np.uint8)

# 灰色背景
image[:] = (128, 128, 128)


# 用(B, G, R) = (255, 255, 255): 白色填滿畫布
image.fill(255)  # 將這個矩陣全部填入255 => 白色, 128 => 灰色

image[:] = [48, 213, 254]  # 將這個矩陣全部填入指定顏色


print("------------------------------------------------------------")  # 60個

# 實例化8位圖
image_empty = np.zeros((480, 640), dtype=np.uint8)  # 依照原圖大小建立一個圖像的二維陣列
plt.title("空圖, 全黑")
plt.imshow(cv2.cvtColor(image_empty, cv2.COLOR_BGR2RGB))  # 顯示圖片   #空圖, 全黑

plt.show()

print("------------------------------------------------------------")  # 60個

print("用np建立一個隨機影像陣列")
image = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)

H, W = image.shape
print(image.shape)
print("W = ", W)
print("H = ", H)

mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for i in range(H):
    for j in range(W):
        mapx.itemset((i, j), j)
        # mapx.itemset((i, j), W - 1 - j)
        mapy.itemset((i, j), i)
        # mapy.itemset((i, j), H - 1 - i)

rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)

plt.figure("xxxxxx3", figsize=(16, 12))
plt.title("用np建立一個隨機影像陣列")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

print("用np建立一個隨機影像陣列")
image = np.random.randint(0, 256, size=[4, 6], dtype=np.uint8)

H, W = image.shape
print(image.shape)
print("W = ", W)
print("H = ", H)

mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for i in range(H):
    for j in range(W):
        mapx.itemset((i, j), i)
        mapy.itemset((i, j), j)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)

plt.figure("xxxxxxb", figsize=(16, 12))
plt.title("用np建立一個隨機影像陣列")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

img = cv2.imread(filename)
img[0, 0] = [0, 0, 255]
img[10:100, 10:100] = [0, 255, 0]
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("漸層色")

w = 400
h = 400
image = np.zeros([h, w, 3])
for i in range(h):
    for j in range(w):
        image[i, j, 0] = int(256 * (j + i) / (w + h))
        image[i, j, 2] = int(256 * (j + i) / (w + h))

image = image.astype("float32") / 255

cvshow("image", image)

print("------------------------------------------------------------")  # 60個

w = 400
h = 400
image = np.zeros([h, w, 4])  # 第三個值為 4
for i in range(h):
    image[i, :, 3] = int(256 * i / 400)  # 設定第四個值 ( 透明度 )

image = image.astype("float32") / 255

cvshow("image", image)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
