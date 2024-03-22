import cv2

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

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
# filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'

print("測試 01------------------------------------------------------------")  # 60個

# 影像對比與亮度調整
import matplotlib.image as img


# output_image = alpha * imput_image + beta
def modify_contrast_and_brightness(image, alpha=1.0, beta=0.0):
    array_alpha = np.array([alpha])  # 對比度
    array_beta = np.array([beta])  # 亮度
    image = cv2.add(image, array_beta)
    image = cv2.multiply(image, array_alpha)
    image = np.clip(image, 0, 255)
    return image


plt.figure(
    num="影像對比與亮度調整",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)
image = cv2.imread(filename)  # 讀取本機圖片
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

modified_image = modify_contrast_and_brightness(image, 1.5, 10.0)
plt.subplot(122)
plt.imshow(cv2.cvtColor(modified_image, cv2.COLOR_BGR2RGB))
plt.title("影像對比與亮度調整")

plt.show()

print("測試 02------------------------------------------------------------")  # 60個

plt.figure(
    num="將一圖分解成 藍 綠 紅 三通道",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/rgb256X300.bmp'
filename = "C:/_git/vcs/_1.data/______test_files1/_opencv/rgb512.bmp"
image = cv2.imread(filename)

plt.subplot(331)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

"""same
b=image[:,:,0]
g=image[:,:,1]
r=image[:,:,2]
"""

b, g, r = cv2.split(image)

print(image.shape)
# print(image)

print(b.shape)
# print(b)

print(g.shape)
# print(g)

print(r.shape)
# print(r)

print("顯示 ch2 紅 通道 圖")
plt.subplot(334)
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))
plt.title("紅 第2通道")

print("顯示 ch1 綠 通道 圖")
plt.subplot(335)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
plt.title("綠 第1通道")

print("顯示 ch0 藍 通道 圖")
plt.subplot(336)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title("藍  第0通道")

print("設定第2通道為0")
image[:, :, 2] = 0
plt.subplot(337)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("設定第2通道為0")

print("再設定第1通道為0")
image[:, :, 1] = 0
plt.subplot(338)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("再設定第1通道為0")

print("再設定第0通道為0")
image[:, :, 0] = 0
plt.subplot(339)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("再設定第0通道為0")

plt.show()

print("測試 05------------------------------------------------------------")  # 60個

plt.figure(
    num="將一圖分解成 藍 綠 紅 三通道",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
filename = "C:/_git/vcs/_1.data/______test_files1/_opencv/rgb256X300.bmp"
filename = "C:/_git/vcs/_1.data/______test_files1/_opencv/rgb512.bmp"

image = cv2.imread(filename)

b, g, r = cv2.split(image)

bgr = cv2.merge([b, g, r])
rgb = cv2.merge([r, g, b])

plt.subplot(231)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.subplot(232)
plt.imshow(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB))  # 照BGR排列 OK
plt.title("B-G-R OK")
plt.subplot(233)
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))  # 照RGB排列 錯相
plt.title("R-G-B NG")

plt.subplot(234)
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))
plt.title("R分量")
plt.subplot(235)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
plt.title("G分量")
plt.subplot(236)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title("B分量")

plt.show()

print("測試 06------------------------------------------------------------")  # 60個

filename = "images/girl.bmp"
image = cv2.imread(filename)
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(
    num="顯示結果",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖BGR OK")

plt.subplot(122)
plt.imshow(cv2.cvtColor(imageRGB, cv2.COLOR_BGR2RGB))
plt.title("原圖RGB NG")

plt.show()

print("測試 07------------------------------------------------------------")  # 60個

plt.figure(
    num="灰度圖像顯示演示",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

image = cv2.imread("images/8.bmp")
g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.subplot(221)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB), cmap=plt.cm.gray)

plt.subplot(222)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB), cmap=plt.cm.gray_r)

plt.subplot(223)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB), cmap="gray")

plt.subplot(224)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB), cmap="gray_r")

plt.show()

print("測試 08------------------------------------------------------------")  # 60個

plt.figure(
    num="灰度圖像顯示演示",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

filename = "images/girl.bmp"
image = cv2.imread(filename)
g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.figure("灰度圖像顯示演示")
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap=plt.cm.gray)

plt.subplot(223)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB), cmap=plt.cm.gray)

plt.show()

print("測試 09------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
