# plot 集合

import matplotlib

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

left = -2 * np.pi
right = 2 * np.pi

x = np.linspace(left, right, 100)
y = np.sin(x)

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="plot 集合 fill_between 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

# 使用fill
plt.plot(x, y)
plt.fill(x, y, color="y", alpha=0.3)  # 黃色填充
plt.title("使用fill")

# 第二張圖
plt.subplot(232)

# 使用fill_between
plt.plot(x, y)
plt.fill_between(x, 0, y, color="y", alpha=0.3)
plt.title("與x軸之間填充")

# 第三張圖
plt.subplot(233)

plt.plot(x, y)
plt.fill_between(x, -1, y, color="y", alpha=0.3)
plt.title("x之下填充到底")

# 第四張圖 和 第五張圖 比較
plt.subplot(234)

plt.plot(x, y)
plt.fill_between(x, 1, y, color="y", alpha=0.3)
plt.title("x之上填充到頂")

# 第五張圖
plt.subplot(235)

t = np.linspace(-np.pi * 1.5, np.pi * 1.5, 100)
c = np.sinc(t)

plt.plot(t, c)
plt.fill(t, c)

# 第六張圖
plt.subplot(236)

x = [0, 4, 6, 4, 0]
y = [0, 0, 2, 4, 4]
plt.fill(x, y, "r")

x = [0, 1, 3, 2]
y = [2, 5, 6, 0]
x2 = [7, 8, 9]
y2 = [0, 3, 0]
plt.fill(x, y, "g", x2, y2, "b")

plt.show()

print("------------------------------------------------------------")  # 60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="plot 集合 fill_between 2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

# 函數f(x)的係數
a1 = 1
c1 = -2
x = np.linspace(-2, 3, 1000)
y1 = a1 * x**2 + c1
plt.plot(x, y1, color="b")  # 藍色是 f(x)

# 函數g(x)的係數
a2 = -1
b2 = 2
c2 = 2
x = np.linspace(-2, 3, 1000)
y2 = a2 * x**2 + b2 * x + c2
plt.plot(x, y2, color="g")  # 綠色是 g(x)

# 繪製區間
plt.fill_between(x, y1=y1, y2=y2, where=(x >= -1) & (x <= 2), facecolor="yellow")

plt.grid()


# 第二張圖
plt.subplot(232)

x = np.arange(0, 13.3, 0.01)

y1 = 17.5 - 2.5 * x
y2 = 8 - 0.6 * x
y3 = np.minimum(y1, y2)  # 取較低值

plt.plot(x, y1, color="blue", label="17.5 - 2.5x")
plt.plot(x, y2, color="green", label="8 - 0.6x")
plt.ylim(0, 10)
plt.fill_between(x, 0, y3, color="yellow")
plt.legend()


# 第三張圖
plt.subplot(233)

x = np.arange(0, 13.3, 0.01)
y = 3 - x
y1 = 17.5 - 2.5 * x
y2 = 8 - 0.6 * x
y3 = np.minimum(y1, y2)  # 取較低值

plt.plot(x, y, color="r", label="3 - x")
plt.plot(x, y1, color="blue", label="17.5 - 2.5x")
plt.plot(x, y2, color="green", label="8 - 0.6x")
plt.ylim(0, 10)
plt.fill_between(x, y, y3, color="yellow")
plt.legend()


# 第四張圖
plt.subplot(234)

# 函數的係數
a = -1
b = 2
# 繪製區間圖形
x = np.linspace(-2, 4, 1000)
y = a * x**2 + b * x
plt.plot(x, y, color="b")
plt.fill_between(x, y1=y, y2=0, where=(x >= -2) & (x <= 5), facecolor="lightgreen")


# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
