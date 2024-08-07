# plot 集合 subplot的另一種寫法

"""
# plot 集合 子圖

Matplotlib 多圖顯示(subplot/subplot2grid/Subplots)

以下紀錄三種方法:

    plt.subplot()
    plt.subplot2grid()
    plt.subplots()
"""

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
'''
#          編號                                     圖像大小[英吋]      解析度    背景色                      邊框顏色                      邊框有無
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
plt.axes([x_st+dx*0, y_st+dy*0, w, h])
plt.plot(x, y, "r-s")

print("第1圖")
plt.axes([x_st+dx*1, y_st+dy*1, w, h])
plt.plot(x, y, "g--o")

print("第2圖")
plt.axes([x_st+dx*2, y_st+dy*2, w, h])
plt.plot(x, y, "b-s")

print("第3圖")
plt.axes([x_st+dx*3, y_st+dy*3, w, h])
plt.plot(x, y, "y--o")

plt.show()

print("------------------------------------------------------------")  # 60個

plt.suptitle("subplot 搭配 gridspec")

import matplotlib.gridspec as gridspec

x = np.linspace(-np.pi, np.pi, num=100, endpoint=True)
c, s, t = np.cos(x), np.sin(x), np.tan(x)

# 建立 3x3 的 GridSpec
gs = gridspec.GridSpec(3, 3)

# 第0列 第0張
plt.subplot(gs[0, 0])
plt.plot(x, c)

# 第0列 第1張
plt.subplot(gs[0, 1])
plt.plot(x, c)

# 第0列 第2張
plt.subplot(gs[0, 2])
plt.plot(x, c)

# 第1列，index 從 0 開始，也可用 [1,0:3] 表示
plt.subplot(gs[1, :])
plt.plot(x, c)

# 第2列 第0張
plt.subplot(gs[2, 0])
plt.plot(x, c)

# 第2列 第1張
plt.subplot(gs[2, 1])
plt.plot(x, c)

# 第2列 第2張
plt.subplot(gs[2, 2])
plt.plot(x, s)

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/__pic/imagedata/2.jpg"

import cv2

# imshow 集合

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"

import matplotlib.image as img

plt.gcf().set_size_inches(12, 14)  # 設定圖框大小

# usage
# ax=plt.subplot(5,5, i+1)
# ax.imshow(images[start_id], cmap='binary')  #顯示黑白圖片

image = cv2.imread(filename)  # 讀取本機圖片
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 灰階
_, image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY_INV)  # 轉為反相黑白

# 第1張子圖
ax1 = plt.subplot(2, 2, 1)
ax1.imshow(image, cmap="binary")  # 顯示黑白圖片
title = "apple"
ax1.set_title(title, fontsize=12)
# X,Y軸不顯示刻度
ax1.set_xticks([])
ax1.set_yticks([])

# 第2張子圖
ax2 = plt.subplot(2, 2, 2)
ax2.imshow(image, cmap="binary")  # 顯示黑白圖片
title = "banana"
ax2.set_title(title, fontsize=12)
# X,Y軸不顯示刻度
ax2.set_xticks([])
ax2.set_yticks([])

# 第3張子圖
ax3 = plt.subplot(2, 2, 3)
ax3.imshow(image, cmap="binary")  # 顯示黑白圖片
title = "cat"
ax3.set_title(title, fontsize=12)
# X,Y軸不顯示刻度
ax3.set_xticks([])
ax3.set_yticks([])

# 第4張子圖
ax4 = plt.subplot(2, 2, 4)
ax4.imshow(image, cmap="binary")  # 顯示黑白圖片
title = "dog"
ax4.set_title(title, fontsize=12)
# X,Y軸不顯示刻度
ax4.set_xticks([])
ax4.set_yticks([])

plt.show()

print("------------------------------------------------------------")  # 60個

foldername = "C:/_git/vcs/_1.data/______test_files1/__pic/imagedata/"

import cv2
import glob

def show_images_labels_predictions(images, labels, start_id, num=10):
    plt.gcf().set_size_inches(12, 14)
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

# 橫條圖
def diagram_1(s, x):
    plt.barh(x, s)


# 圓餅圖
def diagram_2(s, x):
    plt.pie(s, labels=x, autopct="%.2f%%")


# 折線圖+長條圖


def diagram_4(s, x):
    plt.plot(x, s, marker=".")
    plt.bar(x, s, alpha=0.5)


# 長條圖
def diagram_3(s, x):
    plt.bar(x, s)


# 要繪圖的數據
x = ["高雄", "台中", "宜蘭", "花蓮"]
s = [89, 58, 63, 50]

# 設定子圖
plt.figure(1, figsize=(8, 8), clear=True)

plt.subplots_adjust(left=0.1, right=0.95)

plt.subplot(221)
diagram_1(s, x)

plt.subplot(222)
diagram_2(s, x)

plt.subplot(223)
diagram_3(s, x)

plt.subplot(2, 2, 4)
diagram_4(s, x)

plt.show()

print("------------------------------------------------------------")  # 60個

# 1. plt.subplot()

# 1.1 均勻做圖
"""
plt.subplot(2,2,1): 表示把窗口分成2行2列， 並指定位置於位置1
plt.subplot(2,2,1): 表示把窗口分成2行2列， 並指定位置於位置2
"""
plt.subplot(2, 2, 1)
plt.plot([0, 1], [0, 2])

plt.subplot(2, 2, 2)
plt.plot([0, 1], [0, 4])

plt.subplot(2, 2, 3)
plt.plot([0, 1], [0, 5])

plt.subplot(2, 2, 4)
plt.plot([0, 1], [0, 6])

plt.suptitle("均勻做圖")
plt.show()

# 1.2 不均勻做圖(大小不同)
"""
plt.subplot(3,5,(1,2)): 表示把窗口分成3行5列， 並指定位置於位置1~2
plt.subplot(3,5,(3,5)): 表示把窗口分成3行5列， 並指定位置於位置3~5

plt.subplot(3,4,6): 表示把窗口重新分成3行4列， 並指定位置於位置6(會用新的窗口重新計算位置)
plt.subplot(3,4,(7,8)): 表示把窗口重新分成3行4列， 並指定位置於位置7~8(會用新的窗口重新計算位置)
"""
plt.subplot(3, 5, (1, 2))
plt.subplot(3, 5, (3, 5))
plt.tight_layout()

plt.subplot(3, 4, 6)
plt.subplot(3, 4, (7, 8))
plt.tight_layout()

plt.suptitle("不均勻做圖")
plt.show()

# 2. plt.subplot2grid()
"""
plt.subplot2grid((3,3),(0,0), colspan = 3)

    使用plt.subplot2grid()做圖
    (3,3): 表示把窗口分成3行3列
    (0,0): 表示從未置(0,0)開始做圖
    colspan: column範圍
    rowspan: row範圍
"""
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=1)
ax3 = plt.subplot2grid((3, 3), (1, 2), colspan=1, rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0), colspan=1, rowspan=1)

ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel("ax4_x")
ax4.set_ylabel("ax4_y")

ax5 = plt.subplot2grid((3, 3), (2, 1), colspan=1, rowspan=1)
plt.tight_layout()
plt.show()

# 3. plt.subplots()

"""
    使用plt.subplot2s()做圖
    (2,2): 表示把窗口分成2行2列
    ax1, ax2 代表第一行由左至右的兩個位置(座標(1,1), (1,2))
    ax3, ax4 代表第二行由左至右的兩個位置(座標(2,1), (2,2))
    sharex: 是否共享座標軸X (使用相同座標軸)
    sharey: 是否共享座標軸 (使用相同座標軸)
"""
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(
    2, 2, sharex=False, sharey=False, figsize=(10, 6)
)
data = np.arange(1, 10, 0.5)

df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data**2)
df3 = pd.DataFrame(data**3)
df4 = pd.DataFrame(data**4)

ax1.plot(df1)
ax2.plot(df2)
ax3.plot(df3)
ax4.plot(df4)

plt.show()

print("------------------------------------------------------------")  # 60個

t1 = [1, 2, 3, 4]
t2 = [2, 4, 6, 8]

plt.subplot(2, 1, 1, facecolor="y")
# plt.subplot(211,facecolor='y')
plt.plot(t1, t2, "ro")

plt.subplot(2, 2, 3, facecolor="k")
# plt.subplot(223,facecolor='k')
plt.plot(t2, t2, "g--")

plt.subplot(2, 2, 4)
# plt.subplot(224)
plt.plot(t2, t2, "b|")

plt.show()

print("------------------------------------------------------------")  # 60個

print("3圖比較")

x = np.linspace(-2 * np.pi, 2 * np.pi, 51)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

fig, ax = plt.subplots(1, 3, figsize=(20, 15))

ax[0].plot(x,y0, label="sin")
ax[1].plot(x,y1, label="cos")
ax[2].plot(x,y2, label="tan")
ax[0].legend()
ax[1].legend()
ax[2].legend()

plt.show()

print("------------------------------------------------------------")  # 60個

# 16 - grid subplot

import matplotlib.gridspec as gridspec

# method 1: subplot2grid
##########################
plt.figure(figsize=(12, 8))

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)  # stands for axes
ax1.plot([1, 2], [1, 2])
ax1.set_title("ax1_title")
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel("ax4_x")
ax4.set_ylabel("ax4_y")
ax5 = plt.subplot2grid((3, 3), (2, 1))

plt.show()

'''
print("------------------------------------------------------------")  # 60個

import matplotlib.gridspec as gridspec

# method 2: gridspec
#########################
plt.figure(figsize=(12, 8))

gs = gridspec.GridSpec(3, 3)
# use index from 0
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, -2])

# method 3: easy to define structure
####################################
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1, 2], [1, 2])

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

# 17 - plot in plot

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


# different method to add axes
####################################
plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, "g")
plt.xlabel("x")
plt.ylabel("y")
plt.title("title inside 2")

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("subplot 100張圖")

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

import matplotlib.image as img

# print('使用 matplotlib 顯示一圖')
image = img.imread(filename)

N = 100
for i in range(N):
    plt.subplot(10, N // 10, i + 1)
    plt.imshow(image)

plt.show()

print("------------------------------------------------------------")  # 60個

# 繪圖區域

fig = plt.figure(figsize=(8, 6))  # 8x6英寸
fig.suptitle("Title 1")  # 主標題
ax1 = plt.subplot(221)  # 整體爲兩行兩列，創建其中的第一個子圖
ax1.set_title("Title 2", fontsize=12, color="y")  # 子標題
ax1.plot([1, 2, 3, 4, 5])
ax2 = plt.subplot(222)
ax2.plot([5, 4, 3, 2, 1])
ax3 = plt.subplot(223)
ax3.plot([1, 2, 3, 3, 3])
ax4 = plt.subplot(224)
ax4.plot([5, 4, 3, 3, 3])

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure(figsize=(9, 6))
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
ax2 = plt.subplot2grid((3, 3), (0, 2), rowspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (1, 1))  # rowspan/colspan默認爲1
ax5 = plt.subplot2grid((3, 3), (2, 1), colspan=2)
ax5.plot([1, 2, 3, 4, 1])

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=[8, 4])

x = np.linspace(0, 2 * np.pi)
y = np.sin(x)

# 所佔比例 0~1, 以左下為原點
x_st = 0.1
y_st = 0.1
w = 0.8
h = 0.8
plt.axes([x_st, y_st, w, h])
plt.title(label="第一張圖")
plt.plot(x, y, "r:o")

x_st = 0.6
y_st = 0.5
w = 0.25
h = 0.3
plt.axes([x_st, y_st, w, h])
plt.title(label="第二張圖")
plt.plot(x, y, "g--o")

plt.show()

print("------------------------------------------------------------")  # 60個

# 在畫布切出子圖區 , 並繪製內容–add_subplot()

x = np.linspace(0, 2 * np.pi)
y = np.sin(x)

fig = plt.figure(figsize=(8, 6))  # 整個圖表大小為 8 x 6 英吋
fig.subplots_adjust(wspace=0.5, hspace=0.75)  # 調整子圖間距

ax1 = fig.add_subplot(2, 3, 1)  # ←編號 1 的子圖
ax1.plot(x, y)

ax3 = fig.add_subplot(2, 3, 3)  # ← 編號 3 的子圖
# 沒畫

ax5 = fig.add_subplot(2, 3, 5)  # ←編號 5 的子圖
ax5.plot(x, y)

ax6 = fig.add_subplot(2, 3, 6)  # ←編號 6 的子圖
ax6.plot(x, y)
# 設定子圖的座標範圍、座標說明文字與子圖標題
ax6.set_xlim(0, 3.14 / 2)
ax6.set_ylim(-0.1, 1.1)
ax6.set_xlabel("x-axis")
ax6.set_ylabel("y-axis")
ax6.set_title("y = sin(x)")
ax6.plot(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個

"""
Matplotlib 繪圖
    Matplotlib有很多種畫法，不同指令也可以達到相同效果 但較好也較全面的姿勢應該是先釐清fig,ax的關係
    step1:設定好fig,ax和subplots數目及figsize
    step2:個別指定每個ax的畫圖種類，例如line plot, bar chart or hist chart…
    step3:個別指定每個ax的屬性，例如label, xlabel, ylabel,xlim,ylim, legend, xticklabels等等
"""

x = np.linspace(0, 6.28, 50)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axs = plt.subplots(2, 2, figsize=(10, 10), sharex=True, sharey=True)

axs[0][0].plot(x, y1, label="Sin(x)")
axs[0][1].plot(x, y1, label="Sin(x)", linewidth=4, color="black")
axs[1][0].plot(x, y1, label="Sin(x)")
axs[1][1].plot(x, y1, label="Sin(x)")
axs[0][0].set_title("(0, 0)")
axs[0][1].set_title("(0, 1)")
axs[1][0].set_title("(1, 0)")
axs[1][1].set_title("(1, 1)")
axs[0][0].set_xlabel("x_label0")
axs[0][1].set_xlabel("x_label1")
axs[1][0].set_xlabel("x_label2")
axs[1][1].set_xlabel("x_label3")
axs[0][0].set_ylabel("y_label0")
axs[0][1].set_ylabel("y_label1")
axs[1][0].set_ylabel("y_label2")
axs[1][1].set_ylabel("y_label3")
# axs[1][0].set_xticklabels(labels = x, rotation = 45)
# axs[1][1].set_xticklabels(labels = x, rotation = 45)
axs[0][0].grid(True)
# axs[0][0].legend(['legend'], loc = 2)
axs[0][0].plot(x, y2, label="Cos(x)", marker="x", markersize=5, color="r")
axs[0][0].legend(loc=3)
axs[0][0].set_ylim(-1.2, 1.2)

fig.suptitle("Suptitle")

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(18, 4))
plt.subplot(2, 2, 1)
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, "subplot(2,2,1)", ha="center", va="center", size=20, alpha=0.5)

plt.subplot(2, 2, 2)
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, "subplot(2,2,2)", ha="center", va="center", size=20, alpha=0.5)

plt.subplot(2, 2, 3)
plt.xticks(())
plt.yticks(())

plt.text(0.5, 0.5, "subplot(2,2,3)", ha="center", va="center", size=20, alpha=0.5)

plt.subplot(2, 2, 4)
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, "subplot(2,2,4)", ha="center", va="center", size=20, alpha=0.5)

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.gridspec as gridspec

plt.figure(figsize=(18, 4))
G = gridspec.GridSpec(3, 3)

axes_1 = plt.subplot(G[0, :])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, "Axes 1", ha="center", va="center", size=24, alpha=0.5)

axes_2 = plt.subplot(G[1:, 0])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, "Axes 2", ha="center", va="center", size=24, alpha=0.5)

axes_3 = plt.subplot(G[1:, -1])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, "Axes 3", ha="center", va="center", size=24, alpha=0.5)

axes_4 = plt.subplot(G[1, -2])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, "Axes 4", ha="center", va="center", size=24, alpha=0.5)

axes_5 = plt.subplot(G[-1, -2])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, "Axes 5", ha="center", va="center", size=24, alpha=0.5)

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(18, 4))

plt.axes([0.1, 0.1, 0.8, 0.8])
plt.xticks(())
plt.yticks(())
plt.text(
    0.2, 0.5, "axes([0.1, 0.1, .8, .8])", ha="center", va="center", size=20, alpha=0.5
)

plt.axes([0.5, 0.5, 0.3, 0.3])
plt.xticks(())
plt.yticks(())
plt.text(
    0.5, 0.5, "axes([.5, .5, .3, .3])", ha="center", va="center", size=16, alpha=0.5
)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


# 折線圖
def lineChart(s, x):
    plt.xlabel("城市名稱")
    plt.ylabel("民調原分比")
    plt.title("各種城市喜好度比較")
    plt.plot(x, s, marker=".")


# 長條圖
def barChart(s, x):
    plt.xlabel("城市名稱")
    plt.ylabel("民調原分比")
    plt.title("各種城市喜好度比較")
    plt.bar(x, s)


# 橫條圖
def barhChart(s, x):
    plt.barh(x, s)


# 圓餅圖
def pieChart(s, x):
    plt.pie(s, labels=x, autopct="%.2f%%")


# 要繪圖的數據
x = ["第一季", "第二季", "第三季", "第四季"]
s = [13.2, 20.1, 11.9, 14.2]

# 定義子圖
plt.figure(1, figsize=(8, 6), clear=True)
plt.subplots_adjust(left=0.1, right=0.95)

plt.subplot(2, 2, 1)
pieChart(s, x)

x = ["程式設計概論", "多媒體概論", "計算機概論", "網路概論"]
s = [3560, 4000, 4356, 1800]
plt.subplot(2, 2, 2)
barhChart(s, x)

x = ["新北市", "台北市", "高雄市", "台南市", "桃園市", "台中市"]
s = [0.2, 0.3, 0.15, 0.23, 0.19, 0.27]
plt.subplot(223)
lineChart(s, x)

plt.subplot(224)
barChart(s, x)

plt.show()

print("------------------------------------------------------------")  # 60個

data1 = [1, 2, 3, 4, 5, 6, 7, 8]  # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]  # data2線條
data3 = [1, 3, 6, 10, 15, 21, 28, 36]  # data3線條
data4 = [1, 7, 15, 26, 40, 57, 77, 100]  # data4線條

seq = [1, 2, 3, 4, 5, 6, 7, 8]

plt.subplot(2, 2, 1)
plt.plot(seq, data1, "-*")

plt.subplot(2, 2, 2)
plt.plot(seq, data2, "-o")

plt.subplot(2, 2, 3)
plt.plot(seq, data3, "-^")

plt.subplot(2, 2, 4)
plt.plot(seq, data4, "-s")

plt.show()


print("------------------------------------------------------------")  # 60個

# 建立衰減數列.
x1 = np.linspace(0.0, 5.0, 50)
y1 = np.cos(3 * np.pi * x1) * np.exp(-x1)
# 建立非衰減數列
x2 = np.linspace(0.0, 2.0, 50)
y2 = np.cos(3 * np.pi * x2)

plt.subplot(2, 1, 1)
plt.title("衰減數列")
plt.plot(x1, y1, "go-")
plt.ylabel("衰減值")

plt.subplot(2, 1, 2)
plt.plot(x2, y2, "m.-")
plt.xlabel("時間(秒)")
plt.ylabel("非衰減值")

plt.show()

print("------------------------------------------------------------")  # 60個

data1 = [1, 2, 3, 4, 5, 6, 7, 8]  # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]  # data2線條
seq = [1, 2, 3, 4, 5, 6, 7, 8]
plt.subplot(1, 2, 1)  # 子圖1
plt.plot(seq, data1, "-*")
plt.subplot(1, 2, 2)  # 子圖2
plt.plot(seq, data2, "m-o")

plt.show()

print("------------------------------------------------------------")  # 60個


def f(t):
    return np.exp(-t) * np.sin(2 * np.pi * t)


x = np.linspace(0.0, np.pi, 100)
plt.subplot(2, 2, 1)  # 子圖 1
plt.plot(x, f(x))
plt.title("子圖 1")
plt.subplot(2, 2, 2)  # 子圖 2
plt.plot(x, f(x))
plt.title("子圖 2")
plt.subplot(2, 2, 3)  # 子圖 3
plt.plot(x, f(x))
plt.title("子圖 3")

plt.show()

print("------------------------------------------------------------")  # 60個


def f(t):
    return np.exp(-t) * np.sin(2 * np.pi * t)


x = np.linspace(0.0, np.pi, 100)
plt.subplot(221)  # 子圖 1
plt.plot(x, f(x))
plt.title("子圖 1")
plt.subplot(222)  # 子圖 2
plt.plot(x, f(x))
plt.title("子圖 2")
plt.subplot(223)  # 子圖 3
plt.plot(x, f(x))
plt.title("子圖 3")

plt.show()

print("------------------------------------------------------------")  # 60個


def f(t):
    return np.exp(-t) * np.sin(2 * np.pi * t)


x = np.linspace(0.0, np.pi, 100)
plt.subplot(2, 2, 1)  # 子圖 1
plt.plot(x, f(x))
plt.title("子圖 1")
plt.subplot(2, 2, 2)  # 子圖 2
plt.plot(x, f(x))
plt.title("子圖 2")
plt.subplot(2, 1, 2)  # 子圖 3
plt.plot(x, f(x))
plt.title("子圖 3")

plt.show()

print("------------------------------------------------------------")  # 60個

plt.subplot(1, 2, 1)  # 建立子圖表 1,2,1
plt.text(0.15, 0.5, "subplot(1,2,1)", fontsize="16", c="b")
plt.subplot(2, 2, 2)  # 建立子圖表 2,2,2
plt.text(0.15, 0.5, "subplot(2,2,2)", fontsize="16", c="m")
plt.subplot(2, 2, 4)  # 建立子圖表 2,2,4
plt.text(0.15, 0.5, "subplot(2,2,4)", fontsize="16", c="m")

plt.show()

print("------------------------------------------------------------")  # 60個


N = 50  # 色彩數列的點數
colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
colors = []  # 建立色彩數列
for i in range(N):  # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.linspace(0.0, 2 * np.pi, N)  # 建立 50 個點
y = np.sin(x)
fig = plt.figure()  # 建立畫布物件
ax = fig.add_subplot()  # 建立子圖(或稱軸物件)ax
ax.scatter(x, y, c=colors, marker="*")  # 繪製 sin
ax.set_title("建立畫布與軸物件,使用OO API繪圖", fontsize=16)

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(2, 2)  # 建立4個子圖
x = np.linspace(0, 2 * np.pi, 300)
y = np.sin(x**2)
ax[0, 0].plot(x, y, "b")  # 子圖索引 0,0
ax[0, 0].set_title("子圖[0, 0]")
ax[0, 1].plot(x, y, "g")  # 子圖索引 0,1
ax[0, 1].set_title("子圖[0, 1]")
ax[1, 0].plot(x, y, "m")  # 子圖索引 1,0
ax[1, 0].set_title("子圖[1, 0]")
ax[1, 1].plot(x, y, "r")  # 子圖索引 1,1
ax[1, 1].set_title("子圖[1, 1]")
fig.suptitle("4個子圖的實作", fontsize=16)  # 圖表主標題
plt.tight_layout()  # 緊縮佈局

plt.show()

print("------------------------------------------------------------")  # 60個

# 繪製半徑 5 的圓
angle = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots(2, 2)  # 建立 2 x 2 子圖

ax[0, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 0].set_title("繪圓形, 看起來像橢圓")
ax[0, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 1].axis("equal")
ax[0, 1].set_title("寬高比相同, 是圓形")
ax[1, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 0].axis("equal")
ax[1, 0].set(xlim=(-5, 5), ylim=(-5, 5))
ax[1, 0].set_title("設定寬和高相同區間")
ax[1, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 1].set_aspect("equal", "box")
ax[1, 1].set_title("設定寬高比相同")
fig.tight_layout()

plt.show()

print("------------------------------------------------------------")  # 60個

# 繪製半徑 5 的圓
angle = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots(2, 2)  # 建立 2 x 2 子圖

ax[0, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 0].set_title("繪圓形, 看起來像橢圓")
ax[0, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 1].axis("equal")
ax[0, 1].set_title("寬高比相同, 是圓形")
ax[1, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 0].axis("equal")
ax[1, 0].set(xlim=(-5, 5), ylim=(-5, 5))
ax[1, 0].set_title("設定寬和高相同區間")
ax[1, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 1].set_aspect(2)
ax[1, 1].set_title("設定寬高比是2")
fig.tight_layout()

plt.show()

print("------------------------------------------------------------")  # 60個

ax = plt.subplot(projection="polar")
r = np.arange(0, 1, 0.001)
theta = 2 * 2 * np.pi * r
ax.plot(theta, r, "m", lw=3)
plt.title("極座標圖表", fontsize=16)
plt.tight_layout()  # 圖表標題可以緊縮佈局

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

x = np.linspace(0, 2 * np.pi, 300)
y = np.sin(x)

fig = plt.figure(
    num="matplotlib 10",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

ax1 = fig.add_subplot(121, projection="polar")
ax1.plot(x, y)
ax1.set_title("極座標 Sin 圖", fontsize=12)

ax2 = fig.add_subplot(122)
ax2.plot(x, y)
ax2.set_title("一般座標 Sin 圖", fontsize=12)
ax2.set_aspect(2)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
