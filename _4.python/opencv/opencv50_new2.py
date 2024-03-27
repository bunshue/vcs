"""
opencv 集合

"""

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
'''
filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

image1 = cv2.imread(filename)
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉成灰階

# image2 = cv2.cvtColor(image1, 6)  # 也可以用數字對照 6 表示轉換成灰階
# 套用 medianBlur() 中值模糊
image3 = cv2.medianBlur(image2, 7)                   # 模糊化，去除雜訊 7, 25 彩色黑白皆可
image4 = cv2.Canny(image3, 36, 36)                   # 偵測邊緣

# 套用自適應二值化黑白影像
image5 = cv2.adaptiveThreshold(image3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

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
plt.title("原圖")
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title("轉成灰階")
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(233)
plt.title("模糊化，去除雜訊")
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))

plt.subplot(234)
plt.title("偵測邊緣")
plt.imshow(cv2.cvtColor(image4, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title("自適應二值化黑白影像")
plt.imshow(cv2.cvtColor(image5, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title("")

plt.tight_layout()  # 緊密排列，並填滿原圖大小
plt.show()

print("------------------------------------------------------------")  # 60個

print('Y對稱一張圖片')

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
image1 = cv2.imread(filename)

w = image1.shape[1]
h = image1.shape[0]

D = 20
output = np.zeros((h+D*2,w*2+D*2,3), dtype='uint8')   # 產生 2W x H 的黑色背景

image1 = image1[:h, :w]               # 取出 WxH 的影像 全部 也可只取部分

print("左右翻轉影像")
image12 = cv2.flip(image1, 1)

#左半
output[D:h+D, D:w+D] = image1               # 將 output 左邊內容換成 image1
#右半
output[D:h+D, w+D:w*2+D] = image12           # 將 output 右邊內容換成 img2

plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.show()
'''
print("------------------------------------------------------------")  # 60個

print('XY對稱一張圖片')

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
image1 = cv2.imread(filename)

w = image1.shape[1]
h = image1.shape[0]

output = np.zeros((h*2,w*2,3), dtype='uint8')   # 產生 2W x 2H 的黑色背景

img = image1[:h, :w]               # 取出 WxH 的影像 全部 也可只取部分
img2 = cv2.flip(img, 1)           # 左右翻轉
img3 = cv2.flip(img, 0)           # 上下翻轉
img4 = cv2.flip(img, -1)          # 上下左右翻轉

# 左上
output[:h, :w] = img
# 右上
output[:h, w:w*2] = img2
# 左下
output[h:h*2, :w] = img3
# 右下
output[h:h*2, w:w*2] = img4

plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
