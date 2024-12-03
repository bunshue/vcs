"""

cv2.add
cv2.addWeighted
cv2.subtract


"""

import cv2

ESC = 27

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

filename1 = "C:/_git/vcs/_4.python/_data/picture_add1.bmp"
filename2 = "C:/_git/vcs/_4.python/_data/picture_add2.bmp"

# 檔案 => cv2影像
image1 = cv2.imread(filename1)

# 檔案 => cv2影像
image2 = cv2.imread(filename2)

print("兩圖直接相加")
result1 = image1 + image2

print("兩圖用cv相加")
result2 = cv2.add(image1, image2)

print("兩圖做比例疊加 左1.0 右1.0")
result3 = cv2.addWeighted(image1, 1.0, image2, 1.0, 0)  # 0 為墊高值

plt.figure(
    num="相加",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(231)
plt.title("原圖1")
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title("原圖2")
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(234)
plt.title("兩圖直接相加")
plt.imshow(cv2.cvtColor(result1, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title("兩圖用cv相加")
plt.imshow(cv2.cvtColor(result2, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title("兩圖做比例疊加 左1.0 右1.0")
plt.imshow(cv2.cvtColor(result3, cv2.COLOR_BGR2RGB))

plt.tight_layout()  # 緊密排列，並填滿原圖大小
show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/dollar.bmp"

# 檔案 => cv2影像
lena = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/boat.bmp"

# 檔案 => cv2影像
dollar = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure(
    num="疊加",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(131)
plt.title("原圖1")
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("原圖2")
plt.imshow(cv2.cvtColor(dollar, cv2.COLOR_BGR2RGB))

print("兩圖擷取某塊做alpha疊加, 再貼回原圖, 並顯示之")
face1 = lena[220:400, 250:350]
face2 = dollar[160:340, 200:300]
add = cv2.addWeighted(face1, 0.6, face2, 0.4, 0)
dollar[160:340, 200:300] = add

plt.subplot(133)
plt.title("兩圖擷取某塊做alpha疊加, 再貼回原圖")
plt.imshow(cv2.cvtColor(dollar, cv2.COLOR_BGR2RGB))

plt.tight_layout()  # 緊密排列，並填滿原圖大小
show()

print("------------------------------------------------------------")  # 60個

print("OpenCV_12 addWeighted 要一樣大的圖")

filename1 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
filename2 = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"

# 檔案 => cv2影像
image1 = cv2.imread(filename1)

# 檔案 => cv2影像
image2 = cv2.imread(filename2)

output = cv2.addWeighted(image1, 1.0, image2, 1.0, 100)  # 整體墊高100

cvshow("image", output)

print("------------------------------------------------------------")  # 60個

print("測試 淡入淡出 效果")
print("按 ESC 離開")

# 檔案 => cv2影像
image = cv2.imread(filename)  # 開啟圖片
image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA ( 因為需要 alpha 色版 )
w = image.shape[1]  # 取得寬度
h = image.shape[0]  # 取得高度
white = 255 - np.zeros((h, w, 4), dtype="uint8")  # 建立白色圖
a = 1  # 一開始 a 為 1

while True:
    a = a - 0.001  # a 不斷減少 0.001
    if a < 0:
        a = 0  # a最小為0
    output = cv2.addWeighted(white, a, image, 1 - a, 0)  # 根據 a 套用權重
    cv2.imshow("image", output)  # 顯示圖片
    k = cv2.waitKey(1)
    if k == ESC:
        break

cvshow("image", image)

print("------------------------------------------------------------")  # 60個

print("兩圖相減")

filename1 = "data/_compare/compare1.jpg"
filename2 = "data/_compare/compare2.jpg"
# filename1 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
# filename2 = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"

# 檔案 => cv2影像
image1 = cv2.imread(filename1)

# 檔案 => cv2影像
image2 = cv2.imread(filename2)

# image3 = math.fabs(image1-image2)
image3 = image1 - image2

image4 = cv2.subtract(image1, image2)  # 相減

fig = plt.figure(
    num="兩圖相減1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(221)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(223)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("兩圖相減1")

plt.subplot(224)
plt.imshow(cv2.cvtColor(image4, cv2.COLOR_BGR2RGB))
plt.title("兩圖相減2")

show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
