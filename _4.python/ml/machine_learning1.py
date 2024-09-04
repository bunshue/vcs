"""
無 scikit-learn(sklearn)的

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import time
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

# 統率, 武力, 智力, 政治, 魅力
main_features = [87, 86, 82, 78, 100]  # 劉備 特徵值
people_names = [  # 比較人物人名
    "諸葛亮",
    "關羽",
    "張飛",
    "趙雲",
    "曹操",
    "司馬懿",
    "孫權",
    "周瑜",
    "呂布",
]

people_features = [  # 比較人物特徵值
    [99, 42, 100, 100, 92],
    [92, 100, 74, 51, 83],
    [86, 99, 78, 36, 57],
    [79, 94, 77, 82, 91],
    [100, 85, 93, 96, 95],
    [95, 62, 98, 95, 84],
    [72, 84, 76, 85, 93],
    [93, 71, 94, 81, 92],
    [84, 98, 61, 12, 55],
]

dist = []  # 儲存人物相似度值
for feature in people_features:
    distances = 0
    for i in range(len(feature)):
        distances += (main_features[i] - feature[i]) ** 2
    dist.append(math.sqrt(distances))

min_ = min(dist)  # 求最小值
min_index = dist.index(min_)  # 最小值的索引

print(f"與 劉備 最相似的人物 : {people_names[min_index]}")
print(f"相似度值 : {dist[min_index]}")
for i in range(len(dist)):
    print(f"人物 : {people_names[i]}, 相似度 : {dist[i]:6.2f}")

print("------------------------------------------------------------")  # 60個

# numpy cumsum()函數簡介
# 函數作用：求數組的所有元素的累計和，可通過參數axis指定求某個軸向的統計值。

a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])

print(a)

print("累計和")
cc = a.cumsum()
print(cc)
# array([ 1,  3,  6, 10, 15, 21], dtype=int32)

print("累計和, axis=0")
cc = np.cumsum(a, axis=0)
print(cc)

print("累計和, axis=1")
cc = np.cumsum(a, axis=1)
print(cc)

# 隨機漫步算法

n_person = 2000
n_times = 500

t = np.arange(n_times)
steps = 2 * np.random.randint(2, size=(n_person, n_times)) - 1

amount = np.cumsum(steps, axis=1)
sd_amount = amount**2
mean_sd_amount = sd_amount.mean(axis=0)

plt.figure(figsize=(8, 6))

plt.xlabel(r"$t$")
plt.ylabel(r"$\sqrt{\langle (\delta x)^2 \rangle}$")

plt.plot(t, np.sqrt(mean_sd_amount), "g.")
plt.plot(t, np.sqrt(t), "r-")

plt.title("隨機漫步算法")

plt.show()

print("------------------------------------------------------------")  # 60個

# 多項式擬合

N = 10
n_order = 3  # 3階

x = np.linspace(0, 1, N)
y = x + 0.4 * (np.random.rand(N) - 0.5)
p = np.poly1d(np.polyfit(x, y, n_order))
print(p.coeffs)

t = np.linspace(0, 1, 100)

plt.plot(x, x, "r-", label="理論")
plt.plot(x, y, "go", label="實驗")
plt.plot(t, p(t), "b-", label="擬合")
plt.legend()

plt.title("多項式擬合, " + str(n_order) + " 階")

plt.show()

print("------------------------------------------------------------")  # 60個

N = 20

x = np.linspace(0, 1, N)  # [0, 1] 之間創建 20 個點
y = x + 0.2 * np.random.rand(N) - 0.1


def plot_polynomial_fit(x, y, n_order):
    p = np.poly1d(np.polyfit(x, y, n_order))

    # 畫出擬合出來的多項式所表達的曲線以及原始的點
    t = np.linspace(0, 1, 200)
    plt.plot(x, x, "r-", label="理論")
    plt.plot(x, y, "go", label="實驗")
    plt.plot(t, p(t), "b-", label="擬合")
    return p


plt.figure(figsize=(18, 6))
titles = ["Under Fitting", "Fitting", "Over Fitting"]
models = [None, None, None]

n_order = 1
plt.subplot(131)
models[0] = plot_polynomial_fit(x, y, n_order)
plt.title(titles[0] + ", " + str(n_order) + " 階")

n_order = 3
plt.subplot(132)
models[1] = plot_polynomial_fit(x, y, n_order)
plt.title(titles[1] + ", " + str(n_order) + " 階")

n_order = 10
plt.subplot(133)
models[2] = plot_polynomial_fit(x, y, n_order)
plt.title(titles[2] + ", " + str(n_order) + " 階")

plt.legend()
plt.show()

print("------------------------------")  # 30個

for m in models:
    print("model coeffs: {0}".format(m.coeffs))

print("------------------------------")  # 30個

# 針對一階多項式的模型，不同的參數擬合出來的直線和訓練樣本對應的位置關系
coeffs_1d = [0.2, 0.6]

plt.figure(figsize=(9, 6))
t = np.linspace(0, 1, 200)

plt.plot(x, y, "ro", t, models[0](t), "-", t, np.poly1d(coeffs_1d)(t), "r-")

plt.annotate(
    r"L1: $y = {1} + {0}x$".format(coeffs_1d[0], coeffs_1d[1]),
    xy=(0.8, np.poly1d(coeffs_1d)(0.8)),
    xycoords="data",
    xytext=(-90, -50),
    textcoords="offset points",
    fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.annotate(
    r"L2: $y = {1} + {0}x$".format(models[0].coeffs[0], models[0].coeffs[1]),
    xy=(0.3, models[0](0.3)),
    xycoords="data",
    xytext=(-90, -50),
    textcoords="offset points",
    fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.show()

print("------------------------------------------------------------")  # 60個

# 邏輯回歸模型成本函數


def f_1(x):
    return -np.log(x)


def f_0(x):
    return -np.log(1 - x)


X = np.linspace(0.01, 0.99, 100)
f = [f_1, f_0]
titles = ["y=1: $-log(h_\\theta(x))$", "y=0: $-log(1 - h_\\theta(x))$"]

plt.figure(figsize=(12, 6))

for i in range(len(f)):
    plt.subplot(1, 2, i + 1)
    plt.title(titles[i])
    plt.xlabel("$h_\\theta(x)$")
    plt.ylabel("$Cost(h_\\theta(x), y)$")
    plt.plot(X, f[i](X), "r-")

plt.suptitle("邏輯回歸模型成本函數")

plt.show()

print("------------------------------------------------------------")  # 60個

print("L1/L2 範數")


def L1(x):
    return 1 - np.abs(x)


def L2(x):
    return np.sqrt(1 - np.power(x, 2))


def contour(v, x):
    return 5 - np.sqrt(v - np.power(x + 2, 2))  # 4x1^2 + 9x2^2 = v


def format_spines(title):
    ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
    ax.spines["right"].set_color("none")  # 隱藏坐標軸
    ax.spines["top"].set_color("none")
    ax.xaxis.set_ticks_position("bottom")  # 設置刻度顯示位置
    ax.spines["bottom"].set_position(("data", 0))  # 設置下方坐標軸位置
    ax.yaxis.set_ticks_position("left")
    ax.spines["left"].set_position(("data", 0))  # 設置左側坐標軸位置

    plt.title(title)
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)


plt.figure(figsize=(8.4, 4), dpi=144)

x = np.linspace(-1, 1, 100)
cx = np.linspace(-3, 1, 100)

plt.subplot(1, 2, 1)
format_spines("L1 norm")
plt.plot(x, L1(x), "r-", x, -L1(x), "r-")
plt.plot(
    cx, contour(20, cx), "r--", cx, contour(15, cx), "r--", cx, contour(10, cx), "r--"
)

plt.subplot(1, 2, 2)
format_spines("L2 norm")
plt.plot(x, L2(x), "b-", x, -L2(x), "b-")
plt.plot(
    cx, contour(19, cx), "b--", cx, contour(15, cx), "b--", cx, contour(10, cx), "b--"
)

plt.show()

print("------------------------------------------------------------")  # 60個


def entropy(px):
    return -(px * np.log2(px))


x = np.linspace(0.01, 1, 100)

plt.figure(figsize=(8, 6))
plt.title("$Entropy(x) = - P(x) * log_2(P(x))$")
plt.xlim(0, 1)
plt.ylim(0, 0.6)
plt.xlabel("P(x)")
plt.ylabel("Entropy")
plt.plot(x, entropy(x), "r-")

plt.show()

print("------------------------------------------------------------")  # 60個


def gini_impurity(px):
    return px * (1 - px)


x = np.linspace(0.01, 1, 100)

plt.figure(figsize=(8, 6))
plt.title("$Gini(x) = P(x) (1 - P(x))$")
plt.xlim(0, 1)
plt.ylim(0, 0.6)
plt.xlabel("P(x)")
plt.ylabel("Gini Impurity")
plt.plot(x, entropy(x), "r-")

plt.show()

print("------------------------------------------------------------")  # 60個


def gaussian_kernel(x, mean, sigma):
    return np.exp(-((x - mean) ** 2) / (2 * sigma**2))


x = np.linspace(0, 6, 500)
mean = 1
sigma1 = 0.1
sigma2 = 0.3

plt.figure(figsize=(12, 6))

# sub plot 1
plt.subplot(1, 2, 1)
plt.title("Gaussian for $\sigma={0}$".format(sigma1))

plt.xlim(0, 2)
plt.ylim(0, 1.1)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.plot(x, gaussian_kernel(x, mean, sigma1), "r-")

# sub plot 2
plt.subplot(1, 2, 2)
plt.title("Gaussian for $\sigma={0}$".format(sigma2))

plt.xlim(0, 2)
plt.ylim(0, 1.1)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.plot(x, gaussian_kernel(x, mean, sigma2), "r-")

plt.show()

print("------------------------------------------------------------")  # 60個


def normal_distribution(x, mean, sigma):
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(
        -((x - mean) ** 2) / (2 * sigma**2)
    )


x = np.linspace(0, 6, 500)
mean1 = 1
mean2 = 1
sigma1 = 0.1
sigma2 = 0.3

plt.figure(figsize=(12, 6))

# sub plot 1
plt.subplot(1, 2, 1)
plt.title("Gaussian Distribution for $\mu={0}, \sigma={1}$".format(mean1, sigma1))

plt.xlim(0, 2)
plt.ylim(0, 5)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.plot(x, normal_distribution(x, mean1, sigma1), "r-")

# sub plot 2
plt.subplot(1, 2, 2)
plt.title("Gaussian Distribution for $\mu={0}, \sigma={1}$".format(mean2, sigma2))

plt.xlim(0, 2)
plt.ylim(0, 5)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.plot(x, normal_distribution(x, mean2, sigma2), "r-")

plt.show()

print(normal_distribution(6, 5.855, np.sqrt(3.5033e-02)))

print("------------------------------------------------------------")  # 60個

dots = np.array([[1, 1.5], [2, 1.5], [3, 3.6], [4, 3.2], [5, 5.5]])


def cross_point(x0, y0):
    """
    1. line1: y = x
    2. line2: y = -x + b => x = b/2
    3. [x0, y0] is in line2 => b = x0 + y0

    => x1 = b/2 = (x0 + y0) / 2
    => y1 = x1
    """
    x1 = (x0 + y0) / 2
    return x1, x1


plt.figure(figsize=(8, 6))
plt.title("2-dimension to 1-dimension")

plt.xlim(0, 8)
plt.ylim(0, 6)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(dots[:, 0], dots[:, 1], marker="s", c="b")

plt.plot([0.5, 6], [0.5, 6], "-r")

for d in dots:
    x1, y1 = cross_point(d[0], d[1])
    plt.plot([d[0], x1], [d[1], y1], "--b")
    plt.scatter(x1, y1, marker="o", c="r")

plt.annotate(
    r"projection point",
    xy=(x1, y1),
    xycoords="data",
    xytext=(x1 + 0.5, y1 - 0.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.annotate(
    r"vector $u^{(1)}$",
    xy=(4.5, 4.5),
    xycoords="data",
    xytext=(5, 4),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
