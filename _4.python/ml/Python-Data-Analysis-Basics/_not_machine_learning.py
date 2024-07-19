"""

不是機器學習的


"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("------------------------------------------------------------")  # 60個

# 過度擬合 (overfitting)

# 拉格朗日 (Lagrange) 插值法

x = np.linspace(0, 1, 200)
y = -((x - 1) ** 2) + 1
plt.plot(x, y, "lime")

X = np.linspace(0, 1, 20)
Y = -((X - 1) ** 2) + 1 + 0.08 * np.random.randn(20)
plt.scatter(X, Y, c="b", s=50)

z = np.polyfit(X, Y, 19)
p = np.poly1d(z)
plt.plot(x, p(x), "r")

xmin, xmax, ymin, ymax = 0, 1, 0, 1.5
plt.axis([xmin, xmax, ymin, ymax])  # 設定各軸顯示範圍

plt.show()

print("------------------------------------------------------------")  # 60個

"""
#【秘技】分列 X, Y 的變成點座標

等一下我們會大量的把資料變換形式, 現在我們先熱身。在畫圖時常常用到把 x, y 座標分列。現在我們要合成點要怎麼做呢? 也就是說
X1 <-- [1,2,3,4]
Y1 <-- [5,6,7,8]
希望變成
[[1,5], [2,6], [3,7], [4,8]]
"""

X1 = np.array([1, 2, 3, 4])
Y1 = np.array([5, 6, 7, 8])

# NumPy 有個神奇的方式會幫我們做!

ccc = np.c_[X1, Y1]
print(ccc)

"""
【重要插播】meshgrid 用法

為了用 contourf (填充型的等高線) 呈現我們成果, 我們要介紹一個初學有點難理解、meshgrid 的概念。

meshgrid 是產生格點的方式, 通常是我們要畫 3D 曲面啦、或是等高線的時候要先為我們在 xy 平面上「佈點」, 然後算出每點的高度 Z。

我們要做的是給定 x 方向座標, y 方向座標, 然後就產生格點, 如圖示。
"""


# 於是我們再度用我們的 X1, Y1 示範。

X1 = np.array([1, 2, 3, 4])

Y1 = np.array([5, 6, 7, 8])

# 因為 matplotlib 很愛 x, y-座標分開, 經 meshgrid 後也是分開的! 所以我們用 Xm 和 Ym 來接。

Xm, Ym = np.meshgrid(X1, Y1)

# 看一下內容...

print(Xm)
print(Ym)

# 等等, 這什麼啊? 原來 meshgrid 存網格的 x 座標是一列一列存的。
# 同理我們可以理解 Ym 的內容為什麼是這樣了...

print("------------------------------------------------------------")  # 60個

# 01 numpy 的 filter

egg = np.array([3, -5, 10, 23, -5, 11])
idx = egg >= 0
print(idx)
# array([ True, False,  True,  True, False,  True])

print(egg[idx])
# array([ 3, 10, 23, 11])

print(egg[egg >= 0])
# array([ 3, 10, 23, 11])

x = np.linspace(-10, 10, 1000)
y = np.sin(x)
plt.plot(x, y)
plt.scatter(x[y > 0], y[y > 0], c="r")
plt.show()

# 02 Overfitting
Px = np.random.rand(6)
Py = np.random.rand(6)
plt.scatter(Px, Py, c="r", s=50)
plt.show()

x = np.linspace(0, 1, 1000)
y = 0.5 * np.sin(x) + 0.5
plt.scatter(Px, Py, c="r", s=50)
plt.plot(x, y)
plt.show()


def myplot(n=1):
    y = 0.5 * np.sin(n * x) + 0.5
    plt.scatter(Px, Py, c="r", s=50)
    plt.plot(x, y)


myplot(3)
plt.show()


print("------------------------------------------------------------")  # 60個


# 要平均值 μ, 標準差 σ 的時候呢?

μ = 87

σ = 2.5

eggs = np.random.randn(100) * σ + μ

# 我們來檢查這樣生出的平均值、標準差是不是我們想的那樣。

print("平均值 :", eggs.mean())

# 87.3032349761459

print("標準差 :", eggs.std())

# 2.411544933383249

import seaborn as sns

sns.distplot(eggs)
plt.show()


print("------------------------------------------------------------")  # 60個


# lambda: 臨時要使用的函數
currency = 32.1357851  # 1美元 = 32.13台幣    台灣銀行 現金賣出價

price = [100, 500, 1000]  # 美元

ll = list(map(lambda x: currency * x, price))
print("換算成台幣 :", ll)

usb2twd = lambda x: currency * x

print(usb2twd(1000))


# print(f"1 美元合台幣 {c:.2f} 元。")
# print(f"1 美元合台幣 {c:10.2f} 元。")

print("------------------------------------------------------------")  # 60個


class Card:
    SUITS = ["♣", "♦", "♥", "♠"]
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, s, r):
        self.suit = s
        self.rank = r

    def show(self):
        print(self.SUITS[self.suit] + self.RANKS[self.rank])


card01 = Card(2, 3)
card01.show()

print("------------------------------------------------------------")  # 60個

"""
import matplotlib as mpl
import matplotlib.font_manager as fm

for f in mpl.font_manager.fontManager.ttflist:
    print(f.name)

#[f.name for f in mpl.font_manager.fontManager.ttflist]

print('matplotlib 真的「看到的」字型')
for f in fm.fontManager.ttflist:
    print(f.name)
"""


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("作業完成")
