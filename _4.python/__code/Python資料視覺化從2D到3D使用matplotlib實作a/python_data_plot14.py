"""
# plot 集合


第14章：直方圖


"""

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

x = [4, 3, 3, 2, 5, 4, 5, 6, 9, 4, 5, 5, 3, 0, 1, 7, 8, 7, 5, 6, 4]
"""
plt.hist(x)
plt.hist(x, color="g")
h = plt.hist(x, color="g")
print(f"bins的 y 軸 = {h[0]}")
print(f"bins的 x 軸 = {h[1]}")
"""
plt.hist(x, color="g", rwidth=0.8)  # 寬度設定 80%
#plt.hist(x, bins=5, color="g", cumulative=True, rwidth=0.8)

plt.title("直方圖")
plt.xlabel("值")
plt.ylabel("頻率")
plt.show()

print("------------------------------------------------------------")  # 60個

sides = 6
# 建立 10000 個 1-6(含) 的整數隨機數
dice = np.random.randint(1, sides + 1, size=10000)  # 建立隨機數
# 設定 bins = sides = 6
h = plt.hist(dice, sides)  # 繪製hist圖
print("骰子出現次數 : ", h[0])
plt.ylabel("次數")
plt.xlabel("骰子點數")
plt.title("測試 10000 次")
plt.show()

print("------------------------------------------------------------")  # 60個

# 平均值 = 0.0, 標準差 = 1 的隨機數
s = np.random.randn(10000)  # 隨機數
bins = 30
plt.hist(s, bins, density=True)  # 直方圖
plt.show()

print("------------------------------------------------------------")  # 60個

# 平均值 = 0.0, 標準差 = 1 的隨機數
s = np.random.randn(10000)  # 隨機數
bins = 300
plt.hist(s, bins, density=True)  # 直方圖
plt.show()

print("------------------------------------------------------------")  # 60個

mu = 0  # 均值
sigma = 1  # 標準差
s = np.random.normal(mu, sigma, 10000)  # 隨機數
bins = 30
plt.hist(s, bins, density=True)  # 直方圖
plt.show()

print("------------------------------------------------------------")  # 60個

mu = 100  # 均值
sigma = 15  # 標準差
s = np.random.normal(mu, sigma, 10000)  # 隨機數
bins = 30
plt.hist(s, bins, density=True)  # 直方圖

plt.xlabel("智商指數", color="b")
plt.ylabel("機率", color="b")
plt.title("智商IQ指標直方圖", color="m")
plt.text(120, 0.02, r"$\mu=100,\ \sigma=15$", color="b")
plt.grid(True)
plt.show()

print("------------------------------------------------------------")  # 60個

x1 = np.random.normal(50, 5, 10000)
x2 = np.random.normal(60, 5, 50000)
plt.hist(x1, range=(30, 80), bins=20, color="g", alpha=0.8)
plt.hist(x2, range=(30, 80), bins=20, color="m", alpha=0.8)
plt.show()

print("------------------------------------------------------------")  # 60個

x1 = np.random.normal(50, 5, 10000)
x2 = np.random.normal(60, 5, 50000)
plt.hist(x1, range=(30, 80), bins=20, color="g", alpha=0.8, density=True)
plt.hist(x2, range=(30, 80), bins=20, color="m", alpha=0.8, density=True)
plt.show()

print("------------------------------------------------------------")  # 60個

left = -2
peak = 8  # mode尖峰值
right = 10
bins = 200
s = np.random.triangular(left, peak, right, 10000)
plt.hist(s, bins, density=True)
plt.show()

print("------------------------------------------------------------")  # 60個

left = -2
peak = 8  # mode尖峰值
right = 10
bins = 200
s = np.random.triangular(left, peak, right, 10000)
plt.hist(s, bins, density=True)
plt.show()

print("------------------------------------------------------------")  # 60個

mu = 0  # 平均值
sigma = 1  # 標準差
s = np.random.randn(10000)  # 隨機數
bins = 30
count, bins, ignored = plt.hist(s, bins, density=True)  # 直方圖
# 繪製折線圖
plt.plot(
    bins,
    1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((bins - mu) ** 2) / (2 * sigma**2)),
    linewidth=2,
    color="r",
)
plt.title("常態分布 " + r"$\mu=0, \sigma=1$", fontsize=16)
plt.show()

print("------------------------------------------------------------")  # 60個

import seaborn as sns

mu = 0  # 平均值
sigma = 1  # 標準差
s = np.random.randn(10000)  # 隨機數
bins = 30
count, bins, ignored = plt.hist(s, bins, density=True)  # 直方圖
sns.kdeplot(s)  # 核密度估計圖
plt.title("使用kdeplot()函數繪製常態分布 " + r"$\mu=0, \sigma=1$", fontsize=16)
plt.show()

print("------------------------------------------------------------")  # 60個

import seaborn as sns

s = np.random.uniform(size=10000)  # 隨機數
plt.hist(s, 30, density=True)  # 直方圖
sns.kdeplot(s)  # 核密度估計圖
plt.show()

print("------------------------------------------------------------")  # 60個

math = [
    60,
    10,
    40,
    80,
    80,
    30,
    80,
    60,
    70,
    90,
    50,
    50,
    50,
    70,
    60,
    80,
    80,
    50,
    60,
    70,
    70,
    40,
    30,
    70,
    60,
    80,
    20,
    80,
    70,
    50,
    90,
    80,
    40,
    40,
    70,
    60,
    80,
    30,
    20,
    70,
]
chem = [
    50,
    10,
    60,
    80,
    70,
    30,
    80,
    60,
    30,
    90,
    50,
    50,
    90,
    70,
    60,
    50,
    80,
    50,
    60,
    70,
    60,
    50,
    30,
    70,
    70,
    80,
    10,
    80,
    70,
    50,
    90,
    80,
    40,
    50,
    70,
    60,
    80,
    40,
    20,
    70,
]

plt.rcParams["font.family"] = "Microsoft JhengHei"
bins = 9
labels = ["數學", "化學"]
plt.hist([math, chem], bins, label=labels)
plt.ylabel("學生人數")
plt.xlabel("分數")
plt.title("成績表", fontsize=16)
plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個

bins = 20
x = np.random.randn(10000, 3)
colors = ["red", "green", "blue"]
plt.hist(x, bins, density=True, color=colors, label=colors)
plt.legend()
plt.title("3 組數據的常態分佈隨機數", fontsize=16)
plt.show()

print("------------------------------------------------------------")  # 60個

import cv2

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
plt.subplot(121)  # 建立子圖 1
plt.imshow(src, "gray")  # 灰度顯示第1張圖
plt.subplot(122)  # 建立子圖 2
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

arr = np.arange(6).reshape(2, 3)  # 陣列轉成 2 x 3
print(arr)
print(arr.ravel())

print("------------------------------------------------------------")  # 60個

import cv2

src = cv2.imread("springfield.jpg", cv2.IMREAD_GRAYSCALE)
plt.subplot(121)  # 建立子圖 1
plt.imshow(src, "gray")  # 灰階顯示第1張圖
plt.subplot(122)  # 建立子圖 2
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

mu = 0  # 平均值
sigma1 = 25  # x1 資料標準差
x1 = np.random.normal(mu, sigma1, size=100)  # 建立 x1 資料

sigma2 = 10  # x2 資料標準差
x2 = np.random.normal(mu, sigma2, size=100)  # 建立 x1 資料

fig, axs = plt.subplots(nrows=2, ncols=2)  # 建立 2 x 2 子圖
# 建立 [0,0]子圖
axs[0, 0].hist(x1, 15, density=True, histtype="step")
axs[0, 0].set_title("histtype = 'step'")
# 建立 [0,1]子圖
axs[0, 1].hist(x1, 15, density=True, histtype="stepfilled", color="m", alpha=0.8)
axs[0, 1].set_title("histtype = 'stepfilled'")
# 建立 [1,0]子圖
axs[1, 0].hist(x1, density=True, histtype="barstacked", rwidth=0.8)
axs[1, 0].hist(x2, density=True, histtype="barstacked", rwidth=0.8)
axs[1, 0].set_title("histtype = 'barstacked'")
# 建立 [1,1]子圖, 寬度不相等
bins = [-60, -50, -20, -10, 30, 50]
axs[1, 1].hist(x1, bins, density=True, histtype="bar", rwidth=0.8, color="g")
axs[1, 1].set_title("histtype = 'bar' 不相等寬度的 bins")
fig.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


