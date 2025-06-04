"""
color space 色彩空間轉換
cv2.split
cv2.merge
"""

import cv2

filename1 = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

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

img = cv2.imread(filename1)  # BGR讀取
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

img = cv2.imread(filename1)  # BGR讀取
cv2.imshow("BGR Color Space", img)

print("BGR 轉 HSV")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR轉HSV
cv2.imshow("HSV Color Space", img_hsv)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

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

image = cv2.imread(filename1)
blue, green, red = cv2.split(image)
bgr_image = cv2.merge([blue, green, red])  # 依據 B G R 順序合併
cv2.imshow("B -> G -> R ", bgr_image)

rgb_image = cv2.merge([red, green, blue])  # 依據 R G B 順序合併
cv2.imshow("R -> G -> B ", rgb_image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

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

show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
