# 新進測試01 整理成6個一圖

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

import pandas as pd
import random

print("------------------------------------------------------------")  # 60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="新進測試 01",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

# 正常顯示
x1 = np.linspace(-1.5, 1.5, 31)
y1 = np.cos(x1) ** 2

# 移除 y1 > 0.6 的點
x2 = x1[y1 <= 0.6]
y2 = y1[y1 <= 0.6]

# 遮罩 y1 > 0.7 的點
y3 = np.ma.masked_where(y1 > 0.7, y1)

# 將 y1 > 0.8 的點設為 NaN
y4 = y1.copy()
y4[y4 > 0.8] = np.nan

plt.plot(x1 * 0.1, y1, "o-", label="正常顯示")
plt.plot(x2 * 0.4, y2, "o-", label="移除點")
plt.plot(x1 * 0.7, y3, "o-", label="遮罩點")
plt.plot(x1 * 1.0, y4, "o-", label="將點設為NaN")
plt.legend()
plt.title("Cos函數顯示與遮蔽點的應用")

# 第二張圖
plt.subplot(232)

d1 = [10 for y in range(1, 9)]  # data1線條之y值
d2 = [20 for y in range(1, 9)]  # data2線條之y值
d3 = [30 for y in range(1, 9)]  # data3線條之y值
d4 = [40 for y in range(1, 9)]  # data4線條之y值
d5 = [50 for y in range(1, 9)]  # data5線條之y值
d6 = [60 for y in range(1, 9)]  # data6線條之y值
d7 = [70 for y in range(1, 9)]  # data7線條之y值
d8 = [80 for y in range(1, 9)]  # data8線條之y值
d9 = [90 for y in range(1, 9)]  # data9線條之y值
d10 = [100 for y in range(1, 9)]  # data10線條之y值
d11 = [110 for y in range(1, 9)]  # data11線條之y值
d12 = [120 for y in range(1, 9)]  # data12線條之y值

seq = [1, 2, 3, 4, 5, 6, 7, 8]
plt.plot(
    seq,
    d1,
    "-1",
    seq,
    d2,
    "-2",
    seq,
    d3,
    "-3",
    seq,
    d4,
    "-4",
    seq,
    d5,
    "-s",
    seq,
    d6,
    "-p",
    seq,
    d7,
    "-*",
    seq,
    d8,
    "-+",
    seq,
    d9,
    "-D",
    seq,
    d10,
    "-d",
    seq,
    d11,
    "-H",
    seq,
    d12,
    "-h",
)

# 第三張圖
plt.subplot(233)

print("畫點")
plt.plot(0, 1, "-o")  # 在 (0, 1) 上 畫一點
plt.plot(1, 5, "r-o")
plt.plot(2, 10, "r-o")
plt.plot(3, 20, "r-o")

print("寫字")
#                      H對齊方式       V對齊方式
my_kwargs = dict(ha="center", va="center", fontsize=30, c="b")
my_kwargs = dict(ha="left", va="top", fontsize=30, c="b")
x_st = 0
y_st = 17.5
text = "歡迎來到美國"
plt.text(x_st, y_st, text, **my_kwargs)
plt.plot(x_st, y_st, "r-o")  # 畫基準點

plt.title("畫點 寫字")

# 第四張圖
plt.subplot(234)

radius = 5
degrees = np.arange(0, 360)
x = radius * np.cos(np.radians(degrees))
y = radius * np.sin(np.radians(degrees))

plt.plot(x, y)
plt.axis("equal")
plt.grid()

# 第五張圖
plt.subplot(235)

x1 = np.linspace(0.1, 10, 99)  # 建立含30個元素的陣列
x2 = np.linspace(0.1, 10, 99)  # 建立含30個元素的陣列
y1 = [math.log2(x) for x in x1]
y2 = [math.log(x, 0.5) for x in x2]

plt.plot(x1, y1, label="基底 = 2")
plt.plot(x2, y2, label="基底 = 0.5")

plt.axis([0, 10, -5, 5])
plt.legend(loc="best")  # 建立圖例
plt.grid()

# 第六張圖
plt.subplot(236)

plt.show()

print("------------------------------------------------------------")  # 60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="新進測試 03",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)


# 第二張圖
plt.subplot(232)


# 第三張圖
plt.subplot(233)


# 第四張圖
plt.subplot(234)


# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)


plt.show()


print("------------------------------------------------------------")  # 60個
