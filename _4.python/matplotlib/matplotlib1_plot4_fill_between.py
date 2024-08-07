# plot 集合

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

plt.figure(
    num="plot 集合 fill_between 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)

print("------------------------------------------------------------")  # 60個

plt.subplot(231)

plt.plot(x, y)
plt.fill(x, y, color="y", alpha=0.3)  # 黃色填充
plt.title("使用fill (預設)")

print("------------------------------------------------------------")  # 60個
plt.subplot(232)

plt.plot(x, y)
plt.fill_between(x, 0, y, color="y", alpha=0.3)
plt.title("使用fill_between 0\n與x軸之間填充 (預設)")

print("------------------------------------------------------------")  # 60個
plt.subplot(233)

plt.plot(x, y)
plt.fill_between(x, -1, y, color="y", alpha=0.3)
plt.title("使用fill_between -1\nx之下填充到底")

print("------------------------------------------------------------")  # 60個
plt.subplot(234)

plt.plot(x, y)
plt.fill_between(x, 1, y, color="y", alpha=0.3)
plt.title("使用fill_between 1\nx之上填充到頂")

print("------------------------------------------------------------")  # 60個
plt.subplot(235)

t = np.linspace(-np.pi * 1.5, np.pi * 1.5, 100)
c = np.sinc(t)

plt.plot(t, c)
plt.fill(t, c)

print("------------------------------------------------------------")  # 60個
plt.subplot(236)

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

plt.plot(X, Y + 1, color="blue", alpha=1.00)
plt.fill_between(X, 1, Y + 1, color="blue", alpha=0.25)

plt.plot(X, Y - 1, color="blue", alpha=1.00)
plt.fill_between(X, -1, Y - 1, (Y - 1) > -1, color="blue", alpha=0.25)
plt.fill_between(X, -1, Y - 1, (Y - 1) < -1, color="red", alpha=0.25)

plt.xlim(-np.pi, np.pi)
plt.xticks(())
plt.ylim(-2.5, 2.5)
plt.yticks(())

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="plot 集合 fill_between 2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個
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

print("------------------------------------------------------------")  # 60個
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

print("------------------------------------------------------------")  # 60個
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

print("------------------------------------------------------------")  # 60個
plt.subplot(234)

# 函數的係數
a = -1
b = 2
# 繪製區間圖形
x = np.linspace(-2, 4, 1000)
y = a * x**2 + b * x
plt.plot(x, y, color="b")
plt.fill_between(x, y1=y, y2=0, where=(x >= -2) & (x <= 5), facecolor="lightgreen")

print("------------------------------------------------------------")  # 60個
plt.subplot(235)

x = [0, 4, 6, 4, 0]
y = [0, 0, 2, 4, 4]
plt.fill(x, y, "r")

x = [0, 1, 3, 2]
y = [2, 5, 6, 0]
x2 = [7, 8, 9]
y2 = [0, 3, 0]
plt.fill(x, y, "g", x2, y2, "b")

print("------------------------------------------------------------")  # 60個
plt.subplot(236)

import datetime

dates = [
    datetime.datetime(2025, 1, 1, 0, 0),
    datetime.datetime(2025, 1, 2, 0, 0),
    datetime.datetime(2025, 1, 3, 0, 0),
    datetime.datetime(2025, 1, 4, 0, 0),
    datetime.datetime(2025, 1, 5, 0, 0),
    datetime.datetime(2025, 1, 6, 0, 0),
    datetime.datetime(2025, 1, 7, 0, 0),
    datetime.datetime(2025, 1, 8, 0, 0),
    datetime.datetime(2025, 1, 9, 0, 0),
    datetime.datetime(2025, 1, 10, 0, 0),
    datetime.datetime(2025, 1, 11, 0, 0),
    datetime.datetime(2025, 1, 12, 0, 0),
    datetime.datetime(2025, 1, 13, 0, 0),
    datetime.datetime(2025, 1, 14, 0, 0),
    datetime.datetime(2025, 1, 15, 0, 0),
    datetime.datetime(2025, 1, 16, 0, 0),
    datetime.datetime(2025, 1, 17, 0, 0),
    datetime.datetime(2025, 1, 18, 0, 0),
    datetime.datetime(2025, 1, 19, 0, 0),
    datetime.datetime(2025, 1, 20, 0, 0),
    datetime.datetime(2025, 1, 21, 0, 0),
    datetime.datetime(2025, 1, 22, 0, 0),
    datetime.datetime(2025, 1, 23, 0, 0),
    datetime.datetime(2025, 1, 24, 0, 0),
    datetime.datetime(2025, 1, 25, 0, 0),
    datetime.datetime(2025, 1, 26, 0, 0),
    datetime.datetime(2025, 1, 27, 0, 0),
    datetime.datetime(2025, 1, 28, 0, 0),
    datetime.datetime(2025, 1, 29, 0, 0),
    datetime.datetime(2025, 1, 30, 0, 0),
    datetime.datetime(2025, 1, 31, 0, 0),
]
highTemps = [
    26,
    25,
    22,
    27,
    25,
    25,
    26,
    22,
    18,
    20,
    21,
    22,
    18,
    15,
    15,
    16,
    23,
    23,
    22,
    18,
    15,
    17,
    16,
    17,
    18,
    19,
    24,
    26,
    25,
    27,
    18,
]
lowTemps = [
    20,
    18,
    19,
    20,
    19,
    20,
    20,
    18,
    16,
    16,
    18,
    18,
    14,
    12,
    13,
    13,
    16,
    18,
    18,
    12,
    12,
    12,
    13,
    14,
    13,
    13,
    13,
    16,
    17,
    14,
    14,
]

plt.plot(dates, highTemps)  # 繪製最高溫
plt.plot(dates, lowTemps)  # 繪製最低溫
plt.fill_between(dates, highTemps, lowTemps, color="pink", alpha=0.2)  # 填滿
# fig.autofmt_xdate()  # 日期旋轉
plt.title("2025年1月臺北天氣報告", fontsize=12)
plt.ylabel(r"溫度 $C^{o}$", fontsize=12)

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
