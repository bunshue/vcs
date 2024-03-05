# scatter 集合
# 散布圖 Scatter Chart

import sys
import numpy as np
import matplotlib.pyplot as plt
import random
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

np.random.randint(0, 3, 10)
x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
X, Y = np.meshgrid(x, y)
plt.scatter(
    X.ravel(),
    Y.ravel(),
    c=[0, 1, 2, 1, 1, 2, 1, 1, 0, 1, 1, 0, 0, 0, 2, 1],
    cmap="Paired",
)

plt.show()

print("------------------------------------------------------------")  # 60個

x0 = np.arange(0, 5, 1)
y0 = np.arange(0, 5, 1)
x, y = np.meshgrid(x0, y0)
z = np.c_[x.ravel(), y.ravel()]

print(len(x))
print(x.shape)
print(x)
print(len(y))
print(y.shape)
print(y)
print(len(z))
print(z.shape)
print(z)

# ravel 拉平法
print("x.ravel() = ", x.ravel())
print("y.ravel() = ", y.ravel())

plt.scatter(z[:, 0], z[:, 1], s=100)
plt.show()

print("------------------------------------------------------------")  # 60個

x, y = np.meshgrid(np.linspace(0, 4, 5), np.linspace(0, 4, 5))

# ravel 拉平法
X = x.ravel()
Y = y.ravel()
plt.scatter(X, Y, s=100)

plt.show()

print("------------------------------------------------------------")  # 60個

X = np.random.rand(6)
Y = np.random.rand(6)


def myplot(n=1):
    plt.scatter(X, Y, c="r", s=100)
    x = np.linspace(0, 1, 1000)
    y = 0.5 * np.sin(n * x) + 0.5
    plt.plot(x, y)


myplot(10)

plt.show()


print("------------------------------------------------------------")  # 60個

# 氣泡圖
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)  # 點的顏色
area = (30 * np.random.rand(N)) ** 2  # 點的半徑
plt.scatter(x, y, s=area, c=colors, alpha=0.5)  # 由於點可能疊加，設置透明度爲0.5
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


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

print("------------------------------------------------------------")  # 60個

from matplotlib import pyplot as plt


def plt_scatter():
    n = 1024
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)

    plt.subplot(1, 2, 1)
    plt.scatter(X, Y, s=75, c=T, alpha=0.5)

    plt.xlim(-1.5, 1.5)
    plt.xticks(())
    plt.ylim(-1.5, 1.5)
    plt.yticks(())


def plt_fill_between():
    n = 256
    X = np.linspace(-np.pi, np.pi, n, endpoint=True)
    Y = np.sin(2 * X)

    plt.subplot(1, 2, 2)

    plt.plot(X, Y + 1, color="blue", alpha=1.00)
    plt.fill_between(X, 1, Y + 1, color="blue", alpha=0.25)

    plt.plot(X, Y - 1, color="blue", alpha=1.00)
    plt.fill_between(X, -1, Y - 1, (Y - 1) > -1, color="blue", alpha=0.25)
    plt.fill_between(X, -1, Y - 1, (Y - 1) < -1, color="red", alpha=0.25)

    plt.xlim(-np.pi, np.pi)
    plt.xticks(())
    plt.ylim(-2.5, 2.5)
    plt.yticks(())


plt.figure(figsize=(16, 6))
plt_scatter()
plt_fill_between()
plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

x = [x for x in range(1, 6)]
y = [(y * y) for y in x]
plt.scatter(x, y, color="lightgreen", edgecolor="b", s=60)
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0.0, 2 * np.pi, 50)  # 建立 35 個點
y1 = np.sin(x)
plt.scatter(x, y1, c="b", marker="x")  # 繪製 sine wave
y2 = np.cos(x)
plt.scatter(x, y2, c="g", marker="X")  # 繪製 cos wave

plt.show()

print("------------------------------------------------------------")  # 60個

colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
x = np.linspace(0.0, 2 * np.pi, 50)  # 建立 50 個點
y1 = np.sin(x)
colors = []
for i in range(50):  # 隨機設定顏色
    colors.append(np.random.choice(colorused))
plt.scatter(x, y1, c=colors, marker="*")  # 繪製 sine
y2 = np.cos(x)
plt.scatter(x, y2, c=colors, marker="s")  # 繪製 cos

plt.show()

print("------------------------------------------------------------")  # 60個

points = 30
x = np.random.randint(1, 11, points)  # 建立 x
y = np.random.randint(1, 11, points)  # 建立 y
colors = np.random.rand(points)  # 色彩數列
plt.scatter(x, y, c=colors)
plt.xticks(np.arange(0, 11, step=1.0))
plt.yticks(np.arange(0, 11, step=1.0))

plt.show()

print("------------------------------------------------------------")  # 60個

points = 30
x = np.random.randint(1, 11, points)  # 建立 x
y = np.random.randint(1, 11, points)  # 建立 y
colors = np.random.rand(points)  # 色彩數列
size = (30 * np.random.rand(points)) ** 2  # 散點大小數列
plt.scatter(x, y, s=size, c=colors)
plt.xticks(np.arange(0, 12, step=1.0))
plt.yticks(np.arange(0, 12, step=1.0))

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
np.random.seed(5)  # 固定隨機數
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

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
np.random.seed(20)  # 固定隨機數
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

points = 10
colors = np.array(["b", "c", "g", "k", "m", "r", "y", "pink", "purple", "orange"])
x = np.random.randint(1, 11, points)  # 建立 x
y1 = np.random.randint(1, 11, points)  # 建立 y1
y2 = np.random.randint(1, 11, points)  # 建立 y2
plt.scatter(x, y1, c=colors, label="Circle")
plt.scatter(x, y2, c=colors, marker="*", label="Star")
plt.xticks(np.arange(0, 11, step=1.0))
plt.yticks(np.arange(0, 11, step=1.0))
plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(10)  # 固定隨機數
N = 50  # 散點的數量
r = 0.5  # 邊界線boundary半徑
x = np.random.rand(N)  # 隨機的 x 座標點
y = np.random.rand(N)  # 隨機的 y 座標點
area = []
for i in range(N):  # 建立散點區域陣列
    area.append(30)
colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
colors = []
for i in range(N):  # 隨機設定 N 個顏色
    colors.append(np.random.choice(colorused))

area1 = np.ma.masked_where(x < r, area)  # 邊界線 0.5 內區域遮罩
area2 = np.ma.masked_where(x >= r, area)  # 邊界線 0.5 (含)外區域遮罩
# 大於或等於 0.5 繪製星形, 小於 0.5 繪製圓形
plt.scatter(x, y, s=area1, marker="*", c=colors)
plt.scatter(x, y, s=area2, marker="o", c=colors)
# 繪製邊界線
plt.plot((0.5, 0.5), (0, 1.0))  # 繪製邊界線
plt.xticks(np.arange(0, 1.1, step=0.1))
plt.yticks(np.arange(0, 1.1, step=0.1))
plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(10)  # 固定隨機數
N = 50  # 散點的數量
r = 0.5  # 邊界線boundary半徑
x = np.random.rand(N)  # 隨機的 x 座標點
y = np.random.rand(N)  # 隨機的 y 座標點
area = np.random.randint(20, 100, N)  # 散點大小
colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
colors = []
for i in range(N):  # 隨機設定 N 個顏色
    colors.append(np.random.choice(colorused))

r1 = np.sqrt(x**2 + y**2)  # 計算距離
area1 = np.ma.masked_where(r1 < r, area)  # 邊界線 0.5 內區域遮罩
area2 = np.ma.masked_where(r1 >= r, area)  # 邊界線 0.5 (含)外區域遮罩
# 大於或等於 0.5 繪製星形, 小於 0.5 繪製圓形
plt.scatter(x, y, s=area1, marker="*", c=colors)
plt.scatter(x, y, s=area2, marker="o", c=colors)
# 計算 0.5Pi 之弧度, 依據弧度產生的座標點繪製邊界線
radian = np.arange(0, np.pi / 2, 0.01)
plt.plot(r * np.cos(radian), r * np.sin(radian))  # 繪製邊界線
plt.xticks(np.arange(0, 1.1, step=0.1))
plt.yticks(np.arange(0, 1.1, step=0.1))
plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
