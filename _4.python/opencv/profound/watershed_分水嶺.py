"""
watershed 分水嶺

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
print("------------------------------------------------------------")  # 60個

# 圖形分割
# Mean-Shift法

# %fig=使用pyrMeanShiftFiltering()進行圖形分割，從左到右參數sr分別為20, 40, 80
fig, axes = plt.subplots(1, 3, figsize=(9, 3))

img = cv2.imread("data/fruits.jpg")

srs = [20, 40, 80]
for ax, sr in zip(axes, srs):
    img2 = cv2.pyrMeanShiftFiltering(img, sp=20, sr=sr, maxLevel=1)
    ax.imshow(img2[:, :, ::-1])
    ax.set_axis_off()
    ax.set_title("sr = {}".format(sr))

fig.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 分水嶺算法

img = cv2.imread("data/pills.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.blur(img_gray, (15, 15))
_, img_binary = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
peaks = img_gray == cv2.dilate(img_gray, np.ones((7, 7)), 1)

# NG peaks &= img_binary
peaks[1, 1] = True

from scipy.ndimage import label

markers, count = label(peaks)
cv2.watershed(img, markers)

"""
scpy2.opencv.watershed_demo：分水嶺算法的示範程式。
用滑鼠在圖形上繪制起始區域，起始區域將使用“目前標簽”填充，
按滑鼠右鍵切換到下一個標簽。每次繪制起始區域之後，將顯示分割的結果。
"""
print("------------------------------")  # 30個

# %figonly=使用watershed分割藥丸
fig, axes = plt.subplots(1, 2, figsize=(10, 3))
axes[0].imshow(img[:, :, ::-1])
peaks_img = np.zeros(img.shape[:2] + (4,), np.uint8)
peaks_img[peaks, 2] = 255
peaks_img[peaks, -1] = 255
axes[0].imshow(peaks_img)

colors = np.random.randint(64, 200, (count + 2, 3)).astype(np.uint8)
colors[markers[1, 1]] = 255, 255, 255
colors[-1] = 0
axes[1].imshow(colors[markers])
for ax in axes:
    ax.axis("off")
fig.subplots_adjust(0, 0, 1, 1, 0, 0)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def watershed_demo(img):
    print(img.shape)
    # 去噪声
    blurred = cv2.pyrMeanShiftFiltering(img, 10, 100)
    # 灰度/二值图像
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow("thresh", thresh)
    # 有很多的黑点，所以我们去黑点噪声
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    cv2.imshow("opening ", opening)
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    cv2.imshow("mor-opt", sure_bg)
    # 距离变换
    dist = cv2.distanceTransform(opening, cv2.DIST_L2, 3)
    dist_output = cv2.normalize(dist, 0, 1.0, cv2.NORM_MINMAX)
    cv2.imshow("distance-t", dist_output * 50)
    ret, surface = cv2.threshold(dist, dist.max() * 0.6, 255, cv2.THRESH_BINARY)
    cv2.imshow("surface", surface)
    # 发现未知的区域
    surface_fg = np.uint8(surface)
    cv2.imshow("surface_bin", surface_fg)
    unknown = cv2.subtract(sure_bg, surface_fg)
    # 标记标签
    ret, markers = cv2.connectedComponents(surface_fg)
    # 添加一个标签到所有标签，这样确保背景不是0，而是1
    markers = markers + 1
    # 令未知区域为零
    markers[unknown == 255] = 0
    markers = cv2.watershed(img, markers)
    img[markers == -1] = [255, 0, 0]
    cv2.imshow("result", img)


filename = "C:/_git/vcs/_1.data/______test_files1/ims01.24.bmp"
filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_egd/pic04a.jpg"

img = cv2.imread(filename)
cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Original", img)

watershed_demo(img)

cv2.waitKey(0)
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
