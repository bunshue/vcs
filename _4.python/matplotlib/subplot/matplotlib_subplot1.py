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

plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"
plt.rcParams["font.size"] = 12


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
import pandas as pd

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

import matplotlib.pyplot as plt

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


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



def plot_function_name(text, x=0, y=0):
    #半透明畫字
    print(x, y)
    plt.text(x, y, text, alpha=0.3, size=25, ha="center", va="center")

