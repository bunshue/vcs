"""

ImageEnhance

亮度
"Brightness", ImageEnhance.Brightness

對比
"Contrast", ImageEnhance.Contrast

銳利度
"Sharpness", ImageEnhance.Sharpness

色彩
"Color", ImageEnhance.Color

"""


print("------------------------------------------------------------")  # 60個

filename = "D:/_git/vcs/_1.data/______test_files1/elephant.jpg"

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageEnhance

img = Image.open(filename)  # 開啟影像
brightness = ImageEnhance.Brightness(img)  # 設定 img 要加強亮度

factor = 1.5  # 調整亮度，factor 為一個浮點數值, 提高亮度
output = brightness.enhance(factor)
output.save("tmp_elephant1.5.jpg")  # 存檔

factor = 0.5  # 調整亮度，factor 為一個浮點數值, 降低亮度
output = brightness.enhance(factor)
output.save("tmp_elephant0.5.jpg")  # 存檔

# 調整後的數值 = 原始數值 x factor

print("------------------------------------------------------------")  # 60個

# sharpness
from PIL import Image, ImageEnhance

with Image.open(filename) as image:
    image2 = ImageEnhance.Contrast(image).enhance(0.3)
    image2.save("tmp_pic32_contrast.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageEnhance

with Image.open(filename) as image:
    image_new = ImageEnhance.Brightness(image).enhance(2.5)
    image_new.save("tmp_pic_brightness.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageEnhance

with Image.open(filename) as image:
    image_new = ImageEnhance.Brightness(image).enhance(2.5)
    image_new.save("tmp_pic_brightness.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageEnhance

with Image.open(filename) as image:
    image_new = ImageEnhance.Contrast(image).enhance(0.3)
    image_new.save("tmp_pic_contrast.jpg")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageEnhance

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="imshow 集合 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

image1 = Image.open(filename)  # 開啟圖片
enhancer = ImageEnhance.Brightness(image1)  # 建立調整亮度的方法

# 第一張圖
plt.subplot(231)

# 顯示原圖
plt.imshow(image1)  # 在子圖表中繪製圖片

# 第二張圖
plt.subplot(232)


# 顯示亮度 x0.5 的圖片
image2 = enhancer.enhance(0.5)  # 顯示亮度 x0.5 的圖片
plt.imshow(image2)  # 在子圖表中繪製圖片

# 第三張圖
plt.subplot(233)

image3 = enhancer.enhance(1.5)  # 顯示亮度 x1.5 的圖片
plt.imshow(image3)  # 在子圖表中繪製圖片

# 第四張圖
plt.subplot(234)

image4 = enhancer.enhance(3)  # 顯示亮度 x3 的圖片
plt.imshow(image4)  # 在子圖表中繪製圖片

# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance

filename = "D:/_git/vcs/_1.data/______test_files1/picture1.jpg"

img = Image.open(filename)
brightness = ImageEnhance.Brightness(img)  # 調整亮度
contrast = ImageEnhance.Contrast(img)  # 調整對比
color = ImageEnhance.Color(img)  # 調整飽和度
sharpness = ImageEnhance.Sharpness(img)  # 調整銳利度

output_b5 = brightness.enhance(5)  # 提高亮度
output_b05 = brightness.enhance(0.5)  # 降低亮度
output_c5 = contrast.enhance(5)  # 提高對比
output_c05 = contrast.enhance(0.5)  # 降低對比
output_color5 = color.enhance(5)  # 提高飽和度
output_color01 = color.enhance(0.1)  # 降低飽和度
output_s15 = sharpness.enhance(15)  # 提高銳利度
output_s0 = sharpness.enhance(0)  # 降低銳利度

plt.figure(figsize=(15, 10))  # 改變圖表尺寸
plt.subplot(241)  # 建立 4x2 子圖表的上方從左數來第一個圖表
plt.imshow(output_b5)
plt.title("brightness:5")
plt.subplot(242)  # 建立 4x2 子圖表的上方從左數來第二個圖表
plt.imshow(output_b05)
plt.title("brightness:0.5")
plt.subplot(243)  # 建立 4x2 子圖表的上方從左數來第三個圖表
plt.imshow(output_c5)
plt.title("contrast:5")
plt.subplot(244)  # 建立 4x2 子圖表的上方從左數來第四個圖表
plt.imshow(output_c05)
plt.title("contrast:0.5")
plt.subplot(245)  # 建立 4x2 子圖表的下方從左數來第一個圖表
plt.imshow(output_color5)
plt.title("color:5")
plt.subplot(246)  # 建立 4x2 子圖表的下方從左數來第二個圖表
plt.imshow(output_color01)
plt.title("color:0.1")
plt.subplot(247)  # 建立 4x2 子圖表的下方從左數來第三個圖表
plt.imshow(output_s15)
plt.title("sharpness:15")
plt.subplot(248)  # 建立 4x2 子圖表的下方從左數來第四個圖表
plt.imshow(output_s0)
plt.title("sharpness:0")

plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
