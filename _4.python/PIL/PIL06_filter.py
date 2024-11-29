"""

濾鏡效果

使用 PIL 之 ImageFilter 的各種效果


"""

filename = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"

from PIL import Image
from PIL import ImageFilter

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

print("測試 濾鏡 filter")

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

# 檔案 => PIL影像
image = Image.open(filename)

#          編號                  圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="測試 濾鏡 filter",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(3, 4, 1)

print("ImageFilter.BLUR 模糊")
image2 = image.filter(ImageFilter.BLUR)
plt.imshow(image2)
plt.title("BLUR")

plt.subplot(3, 4, 2)

print("ImageFilter.CONTOUR 輪廓")
image2 = image.filter(ImageFilter.CONTOUR)
plt.imshow(image2)
plt.title("CONTOUR")

plt.subplot(3, 4, 3)

print("ImageFilter.DETAIL")
image2 = image.filter(ImageFilter.DETAIL)
plt.imshow(image2)
plt.title("DETAIL")

plt.subplot(3, 4, 4)

print("ImageFilter.EDGE_ENHANCE")
image2 = image.filter(ImageFilter.EDGE_ENHANCE)
plt.imshow(image2)
plt.title("EDGE_ENHANCE")

plt.subplot(3, 4, 5)

print("ImageFilter.EDGE_ENHANCE_MORE")
image2 = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
plt.imshow(image2)
plt.title("EDGE_ENHANCE_MORE")

plt.subplot(3, 4, 6)

print("ImageFilter.EMBOSS 浮雕")
image2 = image.filter(ImageFilter.EMBOSS)
plt.imshow(image2)
plt.title("EMBOSS")

plt.subplot(3, 4, 7)

print("ImageFilter.FIND_EDGES")
image2 = image.filter(ImageFilter.FIND_EDGES)
plt.imshow(image2)
plt.title("FIND_EDGES")

plt.subplot(3, 4, 8)

print("ImageFilter.SMOOTH")
image2 = image.filter(ImageFilter.SMOOTH)
plt.imshow(image2)
plt.title("SMOOTH")

plt.subplot(3, 4, 9)

print("ImageFilter.SMOOTH_MORE")
image2 = image.filter(ImageFilter.SMOOTH_MORE)
plt.imshow(image2)
plt.title("SMOOTH_MORE")

plt.subplot(3, 4, 10)

print("ImageFilter.SHARPEN 銳化")
image2 = image.filter(ImageFilter.SHARPEN)
plt.imshow(image2)
plt.title("SHARPEN")

plt.show()

print("------------------------------------------------------------")  # 60個

print("測試 濾鏡 filter")

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

# 檔案 => PIL影像
image = Image.open(filename)

#          編號                  圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="測試 濾鏡 filter",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(2, 2, 1)
image2 = image.filter(ImageFilter.BoxBlur(5))  # 套用 BoxBlur，設定模糊半徑為 5
plt.imshow(image2)
plt.title("SHARPEN")

plt.subplot(2, 2, 2)
image2 = image.filter(ImageFilter.GaussianBlur(5))  # 套用 GaussianBlur，設定模糊半徑為 5
plt.imshow(image2)
plt.title("SHARPEN")

plt.subplot(2, 2, 3)
# 套用 UnsharpMask
image2 = image.filter(ImageFilter.UnsharpMask(radius=5, percent=-100, threshold=3))
plt.imshow(image2)
plt.title("SHARPEN")

plt.subplot(2, 2, 4)
# 套用 UnsharpMask
image2 = image.filter(ImageFilter.UnsharpMask(radius=5, percent=100, threshold=10))
plt.imshow(image2)
plt.title("SHARPEN")

plt.show()

print("------------------------------------------------------------")  # 60個

""" new

print('PIL模糊處理 GaussianBlur')
image = Image.open(open(filename, 'rb'))
image2 = image.filter(ImageFilter.GaussianBlur)
image2.save(open('tmp_elephant_blur.jpg', 'wb'))

"""


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
