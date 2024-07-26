# scatter 集合
# 散布圖 Scatter Chart

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

def loc(index):
    # 處理座標的移動
    x_mov = random.choice([-3, 3])  # 隨機x軸移動值
    xloc = x[index - 1] + x_mov  # 計算x軸新位置
    y_mov = random.choice([-5, -1, 1, 5])  # 隨機y軸移動值
    yloc = y[index - 1] + y_mov  # 計算y軸新位置
    x.append(xloc)  # x軸新位置加入串列
    y.append(yloc)  # y軸新位置加入串列


num = 10000  # 設定隨機點的數量
x = [0]  # 設定第一次執行x座標
y = [0]  # 設定第一次執行y座標

for i in range(1, num):  # 建立點的座標
    loc(i)
t = x  # 色彩隨x軸變化
plt.scatter(x, y, s=2, c=t, cmap="brg")
plt.show()

print("------------------------------------------------------------")  # 60個


def loc(index):
    # 處理座標的移動
    x_mov = random.choice([-3, 3])  # 隨機x軸移動值
    xloc = x[index - 1] + x_mov  # 計算x軸新位置
    y_mov = random.choice([-5, -1, 1, 5])  # 隨機y軸移動值
    yloc = y[index - 1] + y_mov  # 計算y軸新位置
    x.append(xloc)  # x軸新位置加入串列
    y.append(yloc)  # y軸新位置加入串列


num = 10000  # 設定隨機點的數量
x = [0]  # 設定第一次執行x座標
y = [0]  # 設定第一次執行y座標

for i in range(1, num):  # 建立點的座標
    loc(i)
t = x  # 色彩隨x軸變化
plt.scatter(x, y, s=2, c=t, cmap="brg")
# plt.axes().get_xaxis().set_visible(False)   # 隱藏x軸座標
# plt.axes().get_yaxis().set_visible(False)   # 隱藏y軸座標

plt.show()

print("------------------------------------------------------------")  # 60個

print("散佈圖")

fig, ax = plt.subplots()

N = 50
x = np.random.randint(30, size=N)
y = np.random.randint(30, size=N)
c = np.random.randint(30, size=N)
size = np.exp(np.random.randint(10, size=N) * 200)
sc = ax.scatter(x=x, y=y, c=c, s=c, alpha=0.5, label="scatter plot")

ax.set_xlabel("X軸", loc="left")
ax.set_ylabel("Y軸", loc="top")
ax.legend(loc=1)
cbar = fig.colorbar(sc)
cbar.set_label("Z軸", loc="center")

plt.show()
'''
print("------------------------------------------------------------")  # 60個

from matplotlib import pyplot as plt


n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

plt.scatter(X, Y, s=75, c=T, alpha=0.5)

plt.xlim(-1.5, 1.5)
plt.xticks(())
plt.ylim(-1.5, 1.5)
plt.yticks(())

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.random.rand(10)
y = np.random.rand(10)
colors = np.array(["b", "c", "g", "k", "m", "r", "y", "pink", "purple", "orange"])
# 建立 1 x 3 的子圖
fig, axs = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True)
# 建立多邊形標記
axs[0].scatter(x, y, s=75, c=colors, marker=(5, 0))
axs[0].set_title("多邊形marker=(5, 0)")
axs[0].axis("square")  # 建立矩形子圖
# 建立星形標記
axs[1].scatter(x, y, s=75, c=colors, marker=(5, 1))
axs[1].set_title("星狀形marker=(5, 1)")
axs[1].axis("square")  # 建立矩形子圖
# 建立鑽石標記
axs[2].scatter(x, y, s=75, c=colors, marker=(5, 2))
axs[2].set_title("鑽石形marker=(5, 2)")
axs[2].axis("square")  # 建立矩形子圖
plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.random.rand(10)
y = np.random.rand(10)
colors = np.array(["b", "c", "g", "k", "m", "r", "y", "pink", "purple", "orange"])
# 建立 2 x 3 的子圖
fig, axs = plt.subplots(nrows=2, ncols=3, sharex=True, sharey=True)
# 建立 aplha 標記
axs[0, 0].scatter(x, y, s=100, c=colors, marker=r"$\alpha$")
axs[0, 0].set_title(r"${alpha=}\alpha$" + "標記", c="b")
axs[0, 0].axis("square")  # 建立矩形子圖
# 建立 beta 標記
axs[0, 1].scatter(x, y, s=100, c=colors, marker=r"$\beta$")
axs[0, 1].set_title(r"${beta=}\beta$" + "標記", c="b")
axs[0, 1].axis("square")  # 建立矩形子圖
# 建立 gamma 標記
axs[0, 2].scatter(x, y, s=100, c=colors, marker=r"$\gamma$")
axs[0, 2].set_title(r"${gamma=}\gamma$" + "標記", c="b")
axs[0, 2].axis("square")  # 建立矩形子圖
# 建立 clubsuit 標記
axs[1, 0].scatter(x, y, s=100, c=colors, marker=r"$\clubsuit$")
axs[1, 0].set_title(r"${clubsuit=}\clubsuit$" + "標記", c="b")
axs[1, 0].axis("square")  # 建立矩形子圖
# 建立 spadesuit 標記
axs[1, 1].scatter(x, y, s=100, c=colors, marker=r"$\spadesuit$")
axs[1, 1].set_title(r"${spadesuit=}\spadesuit$" + "標記", c="b")
axs[1, 1].axis("square")  # 建立矩形子圖
# 建立 heartsuit 標記
axs[1, 2].scatter(x, y, s=100, c=colors, marker=r"$\heartsuit$")
axs[1, 2].set_title(r"${heartsuit=}\heartsuit$" + "標記", c="b")
axs[1, 2].axis("square")  # 建立矩形子圖
plt.tight_layout()

plt.show()

print("------------------------------------------------------------")  # 60個

N = 50  # 色彩數列的點數
colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
colors = []  # 建立色彩數列
for i in range(N):  # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.linspace(0.0, 2 * np.pi, N)  # 建立 50 個點
y1 = np.sin(x)
plt.scatter(x, y1, c=colors, marker="*")  # 繪製 sine
y2 = np.cos(x)
plt.scatter(x, y2, c=colors, marker="s")  # 繪製 cos
plt.show()

print("------------------------------------------------------------")  # 60個

points = 30
colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
colors = []  # 建立色彩數列
for i in range(points):  # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.random.randint(1, 11, points)  # 建立 x
y = np.random.randint(1, 11, points)  # 建立 y
size = (points * np.random.rand(points)) ** 2  # 散點大小數列
plt.scatter(x, y, s=size, c=colors)  # 繪製散點
plt.xticks(np.arange(0, 12, step=1.0))  # x 軸刻度
plt.yticks(np.arange(0, 12, step=1.0))  # y 軸刻度
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 5, 500)  # 含500個元素的陣列
y = 1 - 0.5 * np.abs(x - 2)  # y陣列的變化
plt.scatter(x, y, s=50, c=x, cmap="rainbow")  # 色彩隨 x 軸值變化
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 5, 500)  # 含500個元素的陣列
y = 1 - 0.5 * np.abs(x - 2)  # y陣列的變化
plt.scatter(x, y, s=50, c=y, cmap="rainbow")  # 色彩隨 y 軸值變化
plt.colorbar()  # 色彩條
plt.show()

print("------------------------------------------------------------")  # 60個

N = 100
x = np.random.random(N)  # 建立x軸100個隨機數字
y = np.random.random(N)  # 建立y軸100個隨機數字
plt.scatter(x, y, s=N, c=x, cmap="brg")  # 繪製散點圖
plt.show()

print("------------------------------------------------------------")  # 60個


def loc(index):
    # 處理座標的移動
    x_mov = random.choice([-3, 3])  # 隨機x軸移動值
    xloc = x[index - 1] + x_mov  # 計算x軸新位置
    y_mov = random.choice([-5, -1, 1, 5])  # 隨機y軸移動值
    yloc = y[index - 1] + y_mov  # 計算y軸新位置
    x.append(xloc)  # x軸新位置加入串列
    y.append(yloc)  # y軸新位置加入串列


num = 10000  # 設定隨機點的數量
x = [0]  # 設定第一次執行x座標
y = [0]  # 設定第一次執行y座標

for i in range(1, num):  # 建立點的座標
    loc(i)
t = x  # 色彩隨x軸變化
plt.scatter(x, y, s=2, c=t, cmap="brg")
plt.axis("off")  # 隱藏座標
plt.show()

print("------------------------------------------------------------")  # 60個


""" fail
#zip 高級組合法

xx = [1, 2, 3, 4]
yy = [5, 6, 7, 8]
list(zip(xx, yy))

Z = list(zip(X, Y))
print(Z)

plt.scatter(X, Y, s = 50, c = Z)
plt.show()
"""

print("------------------------------------------------------------")  # 60個

degrees = [x * 15 for x in range(0, 25)]
x = [math.cos(math.radians(d)) for d in degrees]
y = [math.sin(math.radians(d)) for d in degrees]

plt.scatter(x, y)
plt.show()


degrees = np.arange(0, 360)
x = np.cos(np.radians(degrees))
y = np.sin(np.radians(degrees))

plt.plot(x, y)
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


