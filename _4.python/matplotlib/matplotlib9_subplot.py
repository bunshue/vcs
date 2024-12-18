"""
Matplotlib 多圖顯示(subplot()/subplot2grid()/subplots())

plt.subplot()

"""
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

# 共同參數
N = 50  # 樣本數
x = np.linspace(0, 2 * np.pi, N)
y = np.sin(x)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

print("------------------------------------------------------------")  # 60個
'''
plt.figure(
    num="標準 subplot",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個
plt.subplot(231)

plt.plot(x, y)

print("------------------------------------------------------------")  # 60個
plt.subplot(232)

plt.plot(x, y)

print("------------------------------------------------------------")  # 60個
plt.subplot(233)

plt.plot(x, y)

print("------------------------------------------------------------")  # 60個
plt.subplot(212)

plt.plot(x, y)

print("------------------------------------------------------------")  # 60個
plt.suptitle("標準 subplot")
plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

print("subplot 36張圖")

plt.figure(figsize=(12, 8))

N = 36
for i in range(N):
    plt.subplot(6, N // 6, i + 1)
    plt.plot(x,y)
    plt.xticks(())
    plt.yticks(())

plt.show()

print("------------------------------------------------------------")  # 60個


plt.figure(figsize=(12, 8))

"""
plt.subplot(3,5,(1,2)): 表示把窗口分成3行5列， 並指定位置於位置1~2
plt.subplot(3,5,(3,5)): 表示把窗口分成3行5列， 並指定位置於位置3~5

plt.subplot(3,4,9): 表示把窗口重新分成3行4列， 並指定位置於位置9(會用新的窗口重新計算位置)
plt.subplot(3,4,(10,12)): 表示把窗口重新分成3行4列， 並指定位置於位置10~12(會用新的窗口重新計算位置)
"""
plt.subplot(3, 5, (1, 2))
plt.plot(x, y)
plt.title("畫面切3X5, 佔1~2")

plt.subplot(3, 5, (3, 5))
plt.title("畫面切3X5, 佔3~5")
plt.plot(x, y)

plt.subplot(3, 4, 9)
plt.title("畫面切3X4, 佔9")
plt.plot(x, y)

plt.subplot(3, 4, (10, 12))
plt.title("畫面切3X4, 佔10~12")
plt.plot(x, y)

plt.suptitle("不均勻做圖(大小不同)")
plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1, facecolor="y")
plt.plot(x, y, "ro")

plt.subplot(2, 2, 3, facecolor="k")
plt.plot(x, y, "g--")

plt.subplot(2, 2, 4)
plt.plot(x, y, "b|")

plt.suptitle("不均勻做圖(大小不同)")
plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(12, 8))

import matplotlib.gridspec as gridspec

# 建立 3x3 的 GridSpec
gs = gridspec.GridSpec(3, 3)

# 第0列 第0張
plt.subplot(gs[0, 0])
plt.plot(x, y)

# 第0列 第1張
plt.subplot(gs[0, 1])
plt.plot(x, y)

# 第0列 第2張
plt.subplot(gs[0, 2])
plt.plot(x, y)

# 第1列，index 從 0 開始，也可用 [1,0:3] 表示
plt.subplot(gs[1, :])
plt.plot(x, y)

# 第2列 第0張
plt.subplot(gs[2, 0])
plt.plot(x, y)

# 第2列 第1張
plt.subplot(gs[2, 1])
plt.plot(x, y)

# 第2列 第2張
plt.subplot(gs[2, 2])
plt.plot(x, y)

plt.suptitle("subplot 搭配 gridspec")
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.gridspec as gridspec

plt.figure(figsize=(12, 8))

gs = gridspec.GridSpec(3, 3)

# use index from 0
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, -2])

plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.gridspec as gridspec

plt.figure(figsize=(12, 8))

G = gridspec.GridSpec(3, 3)

axes_1 = plt.subplot(G[0, :])
plt.plot(x, y)

axes_2 = plt.subplot(G[1:, 0])
plt.plot(x, y)

axes_3 = plt.subplot(G[1:, -1])
plt.plot(x, y)

axes_4 = plt.subplot(G[1, -2])
plt.plot(x, y)

axes_5 = plt.subplot(G[-1, -2])
plt.plot(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個

foldername = "C:/_git/vcs/_1.data/______test_files1/__pic/imagedata/"

import cv2
import glob

def show_images_labels_predictions(images, labels, start_id, num=10):
    plt.gcf().set_size_inches(12, 8)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, i + 1)
        ax.imshow(images[start_id], cmap="binary")  # 顯示黑白圖片
        title = "label = " + str(labels[start_id])
        ax.set_title(title, fontsize=12)
        # X,Y軸不顯示刻度
        ax.set_xticks([])
        ax.set_yticks([])
        start_id += 1
    plt.show()


files = glob.glob(foldername + "*.jpg")  # 建立測試資料
test_feature = []
test_label = []
for file in files:
    img = cv2.imread(file)  # 讀取本機圖片
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰階
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)  # 轉為反相黑白
    test_feature.append(img)
    label = file[54:55]  # "imagedata\1.jpg"第10個字元1為label
    test_label.append(int(label))

print(test_label)
show_images_labels_predictions(test_feature, test_label, 0, len(test_feature))

print("------------------------------------------------------------")  # 60個

# plot in plot

fig = plt.figure(figsize=(12, 8))

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

# below are all percentage
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])  # main axes
ax1.plot(x, y, "r")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title("title")

ax2 = fig.add_axes([0.2, 0.6, 0.25, 0.25])  # inside axes
ax2.plot(y, x, "b")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_title("title inside 1")

plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, "g")
plt.xlabel("x")
plt.ylabel("y")
plt.title("title inside 2")

plt.show()

print("------------------------------------------------------------")  # 60個

# 共同參數
N = 50  # 樣本數
x = np.linspace(0, 2 * np.pi, N)
y = np.sin(x)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=[12, 8])

# 所佔比例 0~1, 以左下為原點
x_st = 0.1
y_st = 0.1
w = 0.8
h = 0.8
plt.axes([x_st, y_st, w, h])
plt.title(label="第一張圖")
plt.plot(x, y)

x_st = 0.6
y_st = 0.5
w = 0.25
h = 0.3
plt.axes([x_st, y_st, w, h])
plt.title(label="第二張圖")
plt.plot(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個

# 共同參數
N = 50  # 樣本數
x = np.linspace(0, 2 * np.pi, N)
y = np.sin(x)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(12, 8))

plt.axes([0.1, 0.1, 0.8, 0.8])
plt.plot(x, y)

plt.axes([0.5, 0.5, 0.3, 0.3])
plt.plot(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個

# 建立一個新的 figure
# fig1 = plt.figure(figsize=(12, 8))

# 增新一個axes（座標軸），以供繪圖和放置資訊:
# axs = fig1.add_subplot(1,1,1) # 1x1的座標軸

# 增新很多個axes，以供繪圖和放置資訊:
# fig1.delaxes( fig1.gca() ) # 順便示範，把剛剛1x1的座標軸刪掉

fig2 = plt.figure(
    num="matplotlib 05",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 一般的情況下，axes是"hold on"的, 也就是資料不會被覆蓋掉。
# hold on: 好處是一次要輸出一堆函數，可以把圖疊加上去。
# hold off: 可以更新圖的內容，可是全部的資訊會被洗掉（title, legend等）
# 如果要保留這些資訊，可以單獨抓出圖的內容，直接修改：
x = np.linspace(0, 6.28, 100)
y = np.sin(x)

axes = fig2.add_subplot(1, 3, 1)
axes.set_title("y = sin(x)")
(line,) = axes.plot(x, y)  # 這裡回傳的line就是畫在圖上的資料
# 當發現畫錯想修改，可以對line修改：
line.set_ydata(np.cos(x))

axes = fig2.add_subplot(1, 3, 2)
axes.set_title("y = sin(x)")
(line,) = axes.plot(x, y)  # 這裡回傳的line就是畫在圖上的資料
# 當發現畫錯想修改，可以對line修改：
line.set_ydata(np.cos(x))

axes = fig2.add_subplot(1, 3, 3)
axes.set_title("y = sin(x)")
(line,) = axes.plot(x, y)  # 這裡回傳的line就是畫在圖上的資料
# 當發現畫錯想修改，可以對line修改：
line.set_ydata(np.cos(x))

plt.show()

print("------------------------------------------------------------")  # 60個

N = 50  # 樣本數
x1 = np.linspace(0, 1 * np.pi, N)
x2 = np.linspace(0, 2 * np.pi, N)
y1 = np.sin(x1)
y2 = np.sin(x2)

ax1 = plt.subplot(211)
ax1.plot(x1, y1)
ax1.tick_params("x", labelbottom=False)  # 取消顯示刻度標籤

ax2 = plt.subplot(212, sharex=ax1)  # 共享 x 軸
ax2.plot(x2, y2)

plt.suptitle('各子圖使用同樣的x軸')
plt.show()

print("------------------------------------------------------------")  # 60個

N = 50  # 樣本數
x = np.linspace(0, 2 * np.pi, N)
y1 = np.sin(x)
y2 = np.sin(x) + 1

ax1 = plt.subplot(121)
ax1.plot(x, y1, "b")

ax2 = plt.subplot(122, sharey=ax1)  # 共享 y 軸
ax2.plot(x, y2, "g--")
ax2.tick_params("y", labelleft=False)  # 取消顯示刻度標籤

plt.suptitle('各子圖使用同樣的y軸')
plt.show()

print("------------------------------------------------------------")  # 60個

# 建立子圖 1
x1 = np.linspace(0, 2 * np.pi, 300)
ax1 = plt.subplot(221)
ax1.plot(x1, np.sin(2 * np.pi * x1))

# 建立子圖 2
x2 = np.linspace(0, 3 * np.pi, 300)
ax2 = plt.subplot(222, sharex=ax1, sharey=ax1)  # 共享x和y軸
ax2.plot(x2, np.sin(4 * np.pi * x2))

# 建立子圖 3
x3 = np.linspace(0, 2 * np.pi, 300)
ax3 = plt.subplot(223, sharex=ax1, sharey=ax1)  # 共享x和y軸
ax3.plot(x3, np.sin(x3**2), "b")

# 建立子圖 4
ax4 = plt.subplot(224, sharex=ax1, sharey=ax1)  # 共享x和y軸
ax4.plot(x3, 1 + np.sin(x3**2), "g--")

plt.suptitle('各子圖使用同樣的 x軸 和 y軸')
plt.show()

print("------------------------------------------------------------")  # 60個

# 建立子圖 1
x1 = np.linspace(0, 2 * np.pi, 300)
ax1 = plt.subplot(221)
ax1.plot(x1, np.sin(2 * np.pi * x1))
ax1.tick_params("x", labelbottom=False)  # 取消顯示x軸刻度標籤

# 建立子圖 2
x2 = np.linspace(0, 3 * np.pi, 300)
ax2 = plt.subplot(222, sharex=ax1, sharey=ax1)  # 共享x和y軸
ax2.plot(x2, np.sin(4 * np.pi * x2))
ax2.tick_params("x", labelbottom=False)  # 取消顯示x軸刻度標籤
ax2.tick_params("y", labelleft=False)  # 取消顯示y軸刻度標籤

# 建立子圖 3
x3 = np.linspace(0, 2 * np.pi, 300)
ax3 = plt.subplot(223, sharex=ax1, sharey=ax1)  # 共享x和y軸
ax3.plot(x3, np.sin(x3**2), "b")

# 建立子圖 4
ax4 = plt.subplot(224, sharex=ax1, sharey=ax1)  # 共享x和y軸
ax4.plot(x3, 1 + np.sin(x3**2), "g--")
ax4.tick_params("y", labelleft=False)  # 取消顯示y軸刻度標籤

plt.suptitle('各子圖使用同樣的 x軸 和 y軸')
plt.show()
'''
print("------------------------------------------------------------")  # 60個


N = 50  # 樣本數
x = np.linspace(0, 2 * np.pi, N)
y = np.sin(x)

ax1 = plt.subplot(2, 2, 1)  # 建立圖表
ax1.plot(x, y)

ax2 = plt.subplot(2, 2, 2)  # 建立圖表
ax2.plot(x, y)

ax3 = plt.subplot(2, 2, 3)  # 建立圖表
ax3.plot(x, y)

ax4 = plt.subplot(2, 2, 4)  # 建立圖表
ax4.plot(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個

ax1 = plt.subplot(2, 2, 1)  # 建立圖表
ax1.plot(x, y)

ax2 = plt.subplot(2, 2, 3)  # 建立圖表
ax2.plot(x, y)

ax3 = plt.subplot(1, 2, 2)  # 建立圖表
ax3.plot(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="不使用subplot畫多圖",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.suptitle("在圖表的指定地方畫圖, 不用subplot")

x = np.linspace(0, 2 * np.pi, num=100, endpoint=True)
y = np.sin(x)

x_st = 0.1
y_st = 0.1
w = 0.2
h = 0.2
dx = 0.2
dy = 0.2

print("第0圖")
plt.axes([x_st + dx * 0, y_st + dy * 0, w, h])
plt.plot(x, y, "r-s")

print("第1圖")
plt.axes([x_st + dx * 1, y_st + dy * 1, w, h])
plt.plot(x, y, "g--o")

print("第2圖")
plt.axes([x_st + dx * 2, y_st + dy * 2, w, h])
plt.plot(x, y, "b-s")

print("第3圖")
plt.axes([x_st + dx * 3, y_st + dy * 3, w, h])
plt.plot(x, y, "y--o")

plt.show()

print("------------------------------------------------------------")  # 60個

print("設定背景色")

for idx, color in enumerate("rgbyck"):
    print(idx, color)
    plt.subplot(321 + idx, facecolor=color)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.subplot(221)  # 第一行的左圖
plt.subplot(222)  # 第一行的右圖
plt.subplot(212)  # 第二整行

plt.show()

print("------------------------------------------------------------")  # 60個

# 使用subplot2grid()建立表格佈局

fig = plt.figure(figsize=(6, 6))
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
ax2 = plt.subplot2grid((3, 3), (0, 2), rowspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 1), colspan=2)
ax5 = plt.subplot2grid((3, 3), (1, 1))

for idx, ax in enumerate(fig.axes, 1):
    ax.text(0.5, 0.5, "ax{}".format(idx), ha="center", va="center", fontsize=16)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
