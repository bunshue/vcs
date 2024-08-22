# plot 集合

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

x = np.arange(6)
y = x
t = x  # 色彩隨 y 軸值變化
plt.scatter(x, y, c=t, cmap="rainbow")
plt.scatter(x, y, c=x, cmap="rainbow", marker="*")  # 繪製 sin
plt.scatter(x, y, c=x, cmap="rainbow", marker="s")  # 繪製 cos
plt.scatter(x, y, c=y, cmap="rainbow", marker="*")  # 繪製 sin
plt.scatter(x, y, c=y, cmap="rainbow", marker="s")  # 繪製 cos

xpt = np.linspace(0, 5, 500)  # 建立含500個元素的陣列
ypt = 1 - 0.5 * np.abs(xpt - 2)  # y陣列的變化
lwidths = (1 + xpt) ** 2  # 寬度陣列
plt.scatter(xpt, ypt, s=lwidths, c=xpt, cmap="hsv")  # hsv色彩映射圖

xpt = np.linspace(0, 5, 500)  # 建立含500個元素的陣列
ypt = 1 - 0.5 * np.abs(xpt - 2)  # y陣列的變化
lwidths = (1 + xpt) ** 2  # 寬度陣列
plt.scatter(xpt, ypt, s=lwidths, c=ypt, cmap="hsv")  # hsv色彩映射圖

plt.show()

print("------------------------------------------------------------")  # 60個


def plot_color_gradients(cmap_list, cmap_name):
    # 建立圖表, 調整圖表高度
    nrows = len(cmap_name)
    width = 6.5  # 定義圖表寬度
    height = (nrows + 1) * 0.28  # 定義圖表高度
    fig, axs = plt.subplots(nrows=nrows, figsize=(width, height))
    fig.subplots_adjust(left=0.2, right=0.95, top=0.75, bottom=0.1)
    axs[0].set_title(cmap_list + " colormaps", fontsize=14)
    # 繪製彩色映射圖和此圖的名稱
    for ax, cmap_name in zip(axs, cmap_name):
        ax.imshow(colorbar, aspect="auto", cmap=cmap_name)
        # 更改坐標軸為 ax, 文字因為是靠右對齊, 所以文字從 -0.02開始
        # 同時文字垂直置中對齊
        ax.text(
            -0.02,
            0.5,
            cmap_name,
            va="center",
            ha="right",
            fontsize=10,
            transform=ax.transAxes,
        )
    # 關閉軸標記
    for ax in axs:
        ax.set_axis_off()


# 主程式開始
cmaps = [
    (
        "Sequential",
        [
            "Greys",
            "Purples",
            "Blues",
            "Greens",
            "Oranges",
            "Reds",
            "YlOrBr",
            "YlOrRd",
            "OrRd",
            "PuRd",
            "RdPu",
            "BuPu",
            "GnBu",
            "PuBu",
            "YlGnBu",
            "PuBuGn",
            "BuGn",
            "YlGn",
        ],
    ),
    (
        "Sequential (2)",
        [
            "binary",
            "gist_yarg",
            "gist_gray",
            "gray",
            "bone",
            "pink",
            "spring",
            "summer",
            "autumn",
            "winter",
            "cool",
            "Wistia",
            "hot",
            "afmhot",
            "gist_heat",
            "copper",
        ],
    ),
    (
        "Perceptually Uniform Sequential",
        ["viridis", "plasma", "inferno", "magma", "cividis"],
    ),
    (
        "Diverging",
        [
            "PiYG",
            "PRGn",
            "BrBG",
            "PuOr",
            "RdGy",
            "RdBu",
            "RdYlBu",
            "RdYlGn",
            "Spectral",
            "coolwarm",
            "bwr",
            "seismic",
        ],
    ),
    ("Cyclic", ["twilight", "twilight_shifted", "hsv"]),
    (
        "Qualitative",
        [
            "Pastel1",
            "Pastel2",
            "Paired",
            "Accent",
            "Dark2",
            "Set1",
            "Set2",
            "Set3",
            "tab10",
            "tab20",
            "tab20b",
            "tab20c",
        ],
    ),
    (
        "Miscellaneous",
        [
            "flag",
            "prism",
            "ocean",
            "gist_earth",
            "terrain",
            "gist_stern",
            "gnuplot",
            "gnuplot2",
            "CMRmap",
            "cubehelix",
            "brg",
            "gist_rainbow",
            "rainbow",
            "jet",
            "turbo",
            "nipy_spectral",
            "gist_ncar",
        ],
    ),
]
colorbar = np.linspace(0, 1, 256)  # 建立0 - 1之間有256元素陣列
colorbar = np.vstack((colorbar, colorbar))  # 擴充陣列為矩陣
# cmap_list是色彩分類名稱, cmap_name是類別內的名稱
for cmap_list, cmap_name in cmaps:
    plot_color_gradients(cmap_list, cmap_name)

plt.show()

print("------------------------------------------------------------")  # 60個

num = 100

x = np.random.random(100)  # 可以產生num個0.0至1.0之間的數字
y = np.random.random(100)
t = x  # 色彩隨x軸變化
plt.scatter(x, y, s=100, c=t, cmap="brg")

plt.show()

print("------------------------------------------------------------")  # 60個


def loc(index):
    """處理座標的移動"""
    x_mov = np.random.choice([-3, 3])  # 隨機x軸移動值
    xloc = x[index - 1] + x_mov  # 計算x軸新位置
    y_mov = np.random.choice([-5, -1, 1, 5])  # 隨機y軸移動值
    yloc = y[index - 1] + y_mov  # 計算y軸新位置
    x.append(xloc)  # x軸新位置加入串列
    y.append(yloc)  # y軸新位置加入串列


num = 10000  # 設定隨機點的數量
x = [0]  # 設定第一次執行x座標
y = [0]  # 設定第一次執行y座標
while True:
    for i in range(1, num):  # 建立點的座標
        loc(i)
    t = x  # 色彩隨x軸變化
    plt.scatter(x, y, s=2, c=t, cmap="brg")
    plt.axis("off")  # 隱藏座標
    plt.show()
    yORn = input("是否繼續 ?(y/n) ")  # 詢問是否繼續
    if yORn == "n" or yORn == "N":  # 輸入n或N則程式結束
        break
    else:
        x[0] = x[num - 1]  # 上次結束x座標成新的起點x座標
        y[0] = y[num - 1]  # 上次結束y座標成新的起點y座標
        del x[1:]  # 刪除舊串列x座標元素
        del y[1:]  # 刪除舊串列y座標元素

print("------------------------------------------------------------")  # 60個


N = 1000  # 數據數量
np.random.seed(10)  # 設定隨機數種子值
x = np.random.normal(0, 1, N)  # 均值是 0, 標準差是 1
y = np.random.normal(0, 1, N)  # 均值是 0, 標準差是 1
color = x + y  # 設定顏色串列是 x + y 數列結果
norm = plt.Normalize(vmin=-3, vmax=3)
plt.scatter(x, y, s=60, c=color, cmap="Greens", norm=norm)
plt.xlim(-3, 3)
plt.xticks(())  # 不顯示 x 刻度
plt.ylim(-3, 3)
plt.yticks(())  # 不顯示 y 刻度

plt.show()

print("------------------------------------------------------------")  # 60個


N = 1000  # 數據數量
np.random.seed(10)  # 設定隨機數種子值
x = np.random.normal(0, 1, N)  # 均值是 0, 標準差是 1
y = np.random.normal(0, 1, N)  # 均值是 0, 標準差是 1
color = x + y  # 設定顏色串列是 x + y 數列結果
norm = plt.Normalize(vmin=-3, vmax=3)
plt.scatter(x, y, s=60, alpha=0.5, c=color, cmap="Greens", norm=norm)
plt.xlim(-3, 3)
plt.xticks(())  # 不顯示 x 刻度
plt.ylim(-3, 3)
plt.yticks(())  # 不顯示 y 刻度

plt.show()

print("------------------------------------------------------------")  # 60個

N = 1000  # 數據數量
np.random.seed(10)  # 設定隨機數種子值
x = np.random.normal(0, 1, N)  # 均值是 0, 標準差是 1
y = np.random.normal(0, 1, N)  # 均值是 0, 標準差是 1
color = x + y  # 設定顏色串列是 x + y 數列結果
norm = plt.Normalize(vmin=-3, vmax=3)
plt.scatter(x, y, s=60, alpha=0.5, c=color, cmap="jet", norm=norm)
plt.xlim(-3, 3)
plt.xticks(())  # 不顯示 x 刻度
plt.ylim(-3, 3)
plt.yticks(())  # 不顯示 y 刻度

plt.show()

print("------------------------------------------------------------")  # 60個

fig, axs = plt.subplots(nrows=2, ncols=2)
x = np.linspace(0, 2 * np.pi, 200)
N = 20
for i in range(N):
    axs[0, 0].plot(x, i * np.sin(x), color=plt.cm.hsv(i / N))
    axs[0, 1].plot(x, i * np.sin(x), color=plt.cm.rainbow(i / N))
    axs[1, 0].plot(x, i * np.sin(x), color=plt.cm.cool(i / N))
    axs[1, 1].plot(x, i * np.sin(x), color=plt.cm.hot(i / N))

axs[0, 0].set_title("hsv")
axs[0, 1].set_title("rainbow")
axs[1, 0].set_title("cool")
axs[1, 1].set_title("hot")

plt.tight_layout()

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
