"""
其他

新進

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
x = np.arange(1, 11)
ax1 = fig.add_subplot(2, 2, 1)  # 建立子圖表 1
ax1.plot(x, x)
ax1.set_title("子圖 221")
ax1 = fig.add_subplot(2, 2, 3)  # 建立子圖表 3
ax1.plot(x, x, "g")
ax1.set_title("子圖 223")
ax1 = fig.add_subplot(1, 2, 2)  # 建立子圖表 2
ax1.plot(x, x, "m")
ax1.set_title("子圖 122")

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
gs = fig.add_gridspec(2)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
gs = fig.add_gridspec(2, 2)
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_title("gs[0,0]")
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_title("gs[0,1]")
ax3 = fig.add_subplot(gs[1, 0])
ax3.set_title("gs[1,0]")
ax4 = fig.add_subplot(gs[1, 1])
ax4.set_title("gs[1,1]")

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
gs = fig.add_gridspec(2, 2)
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_title("gs[0,0]")
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_title("gs[0,1]")
ax3 = fig.add_subplot(gs[1, :])
ax3.set_title("gs[1,:]")

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi, 300)
y = np.sin(x**2)
fig = plt.figure()
gs = fig.add_gridspec(3, hspace=0)
ax = gs.subplots(sharex=True, sharey=True)
fig.suptitle("共享 x 和 y 軸", fontsize=18)
ax[0].plot(x, y**2, "b--")
ax[1].plot(x, 0.5 * y, "go")
ax[2].plot(x, y, "m+")
# 隱藏內側的刻度標記與標籤
for a in ax.flat:
    a.label_outer()
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi, 300)
y = np.sin(x**2)
fig = plt.figure()
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
(ax1, ax2), (ax3, ax4) = gs.subplots(sharex="col", sharey="row")
fig.suptitle("共享 x(column) 和 y(row) 軸", fontsize=18)
ax1.plot(x, y, "b")
ax2.plot(x, y**2, "g")
ax3.plot(x + 1, y, "m")
ax4.plot(x + 2, y**2, "r")

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
gs = fig.add_gridspec(2, 2)  # 建立 2 x 2 網格

x = np.linspace(0, 2 * np.pi, 300)
y = np.sin(x**2)
gs_ax1 = fig.add_subplot(gs[0, 0])  # 用網格物件索引0,0指定子圖
gs_ax1.plot(x, y, "b")
gs_ax1.set_title("子圖[0, 0]")
gs_ax2 = fig.add_subplot(gs[0, 1])  # 用網格物件索引0,1指定子圖
gs_ax2.plot(x, y, "g")
gs_ax2.set_title("子圖[0, 1]")
gs_ax3 = fig.add_subplot(gs[1, 0])  # 用網格物件索引1,0指定子圖
gs_ax3.plot(x, y, "m")
gs_ax3.set_title("子圖[1, 0]")
gs_ax4 = fig.add_subplot(gs[1, 1])  # 用網格物件索引1,1指定子圖
gs_ax4.plot(x, y, "r")
gs_ax4.set_title("子圖[1, 1]")

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["figure.facecolor"] = "lightyellow"

fig = plt.figure()
gs = fig.add_gridspec(3, 3)  # 建立 3 x 3 子圖
x = np.arange(1, 11)
gs_ax1 = fig.add_subplot(gs[0, :])  # 使用切片觀念
gs_ax1.plot(x, x)
gs_ax1.set_title("gs[0,:]")
gs_ax2 = fig.add_subplot(gs[1, :-1])  # 使用切片觀念
gs_ax2.plot(x, x)
gs_ax2.set_title("gs[1,:-1]")
gs_ax3 = fig.add_subplot(gs[1:, -1])  # 使用切片觀念
gs_ax3.plot(x, x)
gs_ax3.set_title("gs[1:,-1]")
gs_ax4 = fig.add_subplot(gs[-1, 0])  # 使用切片觀念
gs_ax4.plot(x, x)
gs_ax4.set_title("gs[-1,0]")
gs_ax5 = fig.add_subplot(gs[-1, -2])  # 使用切片觀念
gs_ax5.plot(x, x)
gs_ax5.set_title("gs[-1,-2]")

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["figure.facecolor"] = "lightyellow"

fig = plt.figure()
# 子圖 0 列和 1 列的高度比是 2:1
# 子圖 0 列和 1 列的寬度比是 2:1
gs = fig.add_gridspec(nrows=2, ncols=2, height_ratios=[2, 1], width_ratios=[2, 1])
# 建立子圖物件
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, :])
# x 軸資料
x = np.linspace(0, 2 * np.pi, 500)
# 繪製子圖
ax1.plot(x, np.sin(x))
ax2.plot(x, np.sin(x) ** 2, "g")
ax3.plot(x, np.sin(x) + np.cos(x), "m")
# 建立軸標籤
ax1.set_ylabel("y")
ax3.set_xlabel("x")
ax3.set_ylabel("y")

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()

x = np.arange(1, 11)
plt.plot(x, x)
plt.title("外圖表")
# 新增子區域位置和大小
left, bottom, width, height = 0.2, 0.6, 0.2, 0.2
# 設定子座標物件
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(x, x, "g")
ax2.set_title("內圖表")

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
