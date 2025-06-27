"""


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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from mpl_toolkits import mplot3d
from matplotlib import cm
import matplotlib	

feature_x = np.linspace(-5.0, 5.0, 1000)
feature_y = np.linspace(-5.0, 5.0, 1000)
  
# Creating 2-D grid of features
[X, Y] = np.meshgrid(feature_x, feature_y)
z=(X+Y*1j)
  
fig, ax = plt.subplots(1, 1)
Z = np.sqrt(X ** 2 + Y ** 2)
ax.set_aspect('equal', adjustable='box')

# plots filled contour plot

ax.pcolormesh(X, Y, Z, cmap="hsv", vmin=-(np.pi), vmax=(np.pi))
ax.pcolormesh(X, Y, Z, cmap="viridis", norm=matplotlib.colors.LogNorm())

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

def binary_step(x):
    return 0 if x < 0 else 1


def logistic(x):
    return 1 / (1 + math.exp(-x))


def tanh(x):
    return math.tanh(x)


def relu(x):
    return 0 if x < 0 else x


x = np.linspace(-5, 5, 100)

bs = [binary_step(x_) for x_ in x]
lf = [logistic(x_) for x_ in x]
th = [tanh(x_) for x_ in x]
re = [relu(x_) for x_ in x]

_, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))

ax1.set_title("Binary step")
ax2.set_title("TanH")
ax3.set_title("Logistic")
ax4.set_title("ReLU")

ax1.plot(x, bs)
ax2.plot(x, lf)
ax3.plot(x, th)
ax4.plot(x, re)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# AND, OR vs XOR

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y_and = [0, 0, 0, 1]
Y_or = [0, 1, 1, 1]
Y_xor = [0, 1, 1, 0]

titles = ("AND", "OR", "XOR")

for i, Y in enumerate([Y_and, Y_or, Y_xor]):
    ax = plt.subplot(131 + i)

    ax.set_xlim([-0.5, 1.5])
    ax.set_ylim([-0.5, 1.5])

    ax.set_aspect("equal")

    plt.title(titles[i])
    plt.scatter(*zip(*X), c=Y)

    if i == 0:
        plt.plot([0, 1.5], [1.5, 0])
    elif i == 1:
        plt.plot([-0.5, 1], [1, -0.5])
    else:
        plt.text(0.5, 0.5, s="?", ha="center", va="center")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

def dice_roll():
    v = random.randint(1, 6)
    return v

num_of_trials = range(100, 10000, 10)
avgs = []
for num_of_trial in num_of_trials:  
    trials = []    
    for trial in range(num_of_trial):
        trials.append(dice_roll())
    avgs.append(sum(trials)/float(num_of_trial))

plt.plot(num_of_trials, avgs)
plt.xlabel("試驗次數")
plt.ylabel("平均")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def normal_pdf(x, mu, sigma):
    pi = 3.1415926
    e = 2.718281
    f = (1./np.sqrt(2*pi*sigma**2))*e**(-(x-mu)**2/(2.*sigma**2))
    return f

ax = np.linspace(-5, 5, 100)
ay = [normal_pdf(x, 0, 1) for x in ax]  
plt.plot(ax, ay)
show()

print("------------------------------------------------------------")  # 60個

x = range(1, 11)  # 1 2 3 ... 10
y = range(1, 11)  # 1 2 3 ... 10
X, Y = np.meshgrid(x, y)

size = [i * 80 for i in Y]  # 放大資料點數據 N 倍，比較容易觀察尺寸
plt.scatter(X, Y, s=size, c=size, cmap="Set1")  # 使用 Set1 的 colormap
show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots()
ax.plot(np.linspace(0, 2 * np.pi, 10), np.sin(np.linspace(0, 2 * np.pi, 10)))
show()

print("------------------------------------------------------------")  # 60個

# Momentum

# Online learning may help to escape local minima

x = np.linspace(-2, 2, 100)
y1 = x**2
y2 = np.array([a**2 + np.sin(5 * a) for a in x])

plt.subplot(121)
plt.plot(x, y1)
plt.scatter([-1.5], [3], c="k", s=300)

plt.subplot(122)
plt.plot(x, y2)
plt.scatter([-1.45], [1.75], c="k", s=300)
show()

print("------------------------------------------------------------")  # 60個

N = 50
A = 100
spread = np.random.rand(N) * A  # 放大 A 倍 原本0~1 後來 0~1*A
print(spread)

print()
center = np.ones(N//2) * N
print(center)

flier_high = np.random.rand(N//5) * A + A
flier_low = np.random.rand(N//5) * -A
data = np.concatenate((spread, center, flier_high, flier_low), 0)

plt.boxplot(data)
#plt.hist(data)

show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
