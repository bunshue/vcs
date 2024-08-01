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
print("作業完成")
print("------------------------------------------------------------")  # 60個

