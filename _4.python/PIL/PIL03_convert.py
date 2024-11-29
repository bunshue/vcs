"""
PIL 圖片相關的處理

各種convert

使用函數convert()來進行轉換，它是圖像實例對象的一個方法，接受一個 mode 參數，用以指定一種色彩模式，mode 的取值可以是如下幾種：
· 1 (1-bit pixels, black and white, stored with one pixel per byte)
· L (8-bit pixels, black and white)
· P (8-bit pixels, mapped to any other mode using a colour palette)
· RGB (3x8-bit pixels, true colour)
· RGBA (4x8-bit pixels, true colour with transparency mask)
· CMYK (4x8-bit pixels, colour separation)
· YCbCr (3x8-bit pixels, colour video format)
· I (32-bit signed integer pixels)
· F (32-bit floating point pixels)

"""

from PIL import Image

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

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

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => PIL影像
image = Image.open(filename)

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="各種convert參數",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第1張圖
plt.subplot(251)
plt.title("原圖")
plt.imshow(image)

# 第2張圖
plt.subplot(252)
# L
# 轉為灰度圖像，每個像素用8個bit表示，0表示黑，255表示白，其他數字表示不同的灰度。
# 轉換公式：L = R * 299/1000 + G * 587/1000+ B * 114/1000。
image_L = image.convert("L")  # 轉換成灰階圖像
plt.imshow(image_L)
plt.title("灰階")

# 第3張圖
plt.subplot(253)
plt.title("二值化")
image3 = image.convert("1")  # one, 二值化
plt.imshow(image3)

# 第4張圖
plt.subplot(254)
# P
image_P = image.convert("P")
plt.imshow(image_P)

# 第5張圖
plt.subplot(255)
# RGB
image_RGB = image.convert("RGB")
plt.imshow(image_RGB)

# 第6張圖
plt.subplot(256)
# RGBA
image_RGBA = image.convert("RGBA")
plt.imshow(image_RGBA)

# 第7張圖
plt.subplot(257)
# CMYK
image_CMYK = image.convert("CMYK")
plt.imshow(image_CMYK)

# 第8張圖
plt.subplot(258)
# YCbCr
image_YCbCr = image.convert("YCbCr")
plt.imshow(image_YCbCr)

# 第9張圖
plt.subplot(259)
# I
image_I = image.convert("I")
plt.imshow(image_I)

# 第10張圖
plt.subplot(2, 5, 10)
# F
image_F = image.convert("F")
plt.imshow(image_F)

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => PIL影像
image = Image.open(filename)

plt.gray()  # 不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(121)
plt.title("原圖")
plt.imshow(image)

# 檔案 => PIL影像 => 灰階
image = Image.open(filename).convert("L")

plt.subplot(122)
plt.title("灰度圖")
plt.imshow(image)

plt.show()

print("------------------------------------------------------------")  # 60個

import torchvision.transforms as transforms

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => PIL影像
image = Image.open(filename)  # PIL讀取本機圖片, 讀取的是RGB格式的圖片

plt.imshow(image)
plt.show()

print("RGB圖像的維度：", np.array(image).shape)
image_dim_len = len(np.array(image).shape)
print("The dim of Image: ", image_dim_len)

# RGB轉換成灰階圖像
image_transforms = transforms.Compose([transforms.Grayscale(1)])

image = image_transforms(image)
# 輸出灰度圖像的維度
print("灰度圖像維度： ", np.array(image).shape)
image_dim_len = len(np.array(image).shape)
print("The dim of Image: ", image_dim_len)

# 1
# 轉為二值圖像，非黑即白。每個像素用8個bit表示，0表示黑，255表示白。
image_1 = image.convert("1")  # one 轉換成二值化圖像
plt.imshow(image_1)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
