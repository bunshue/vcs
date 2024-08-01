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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

