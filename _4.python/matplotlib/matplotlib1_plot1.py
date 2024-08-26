"""
plot 集合 1
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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="plot 集合 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

x = np.linspace(0, 10, 101)

def random_walk(xy0=(0.0, 0.0), nsteps=100, std=1.0):
    xy = np.zeros((nsteps + 1, 2))
    xy[0, :] = xy0
    deltas = np.random.normal(loc=0.0, scale=std, size=(nsteps, 2))
    xy[1:, :] = xy[0, :] + np.cumsum(deltas, axis=0)
    return xy


for cnt in range(3):
    traj = random_walk()
    plt.plot(traj[:, 0], traj[:, 1], label="Traj. {c}".format(c=cnt))

plt.title("Random Walk")

# 第二張圖
plt.subplot(232)

N = 20
x = np.linspace(0, 6.4, N)  # x是numpy.ndarray格式

A = 0.8  # 雜訊的振幅
y = np.sin(x) + np.random.rand(1, len(x)) * A - A / 2  # 加入雜訊的點集    # y是numpy.ndarray格式

y = y.tolist()[0]  # y 由 numpy.ndarray格式 轉成list格式, 畫圖要用list格式

plt.plot(x, np.sin(x), "black")  # 無雜訊
plt.plot(x, y, "r")  # 有雜訊
plt.grid()

plt.title("畫雜訊範例 " + str(N) + "點")

# 第三張圖
plt.subplot(233)

filename = "_data/python_ReadWrite_CSV6_temperature.csv"

# 讀入氣溫資料
dat = pd.read_csv(filename, encoding="UTF-8")

n = len(dat)  # 資料筆數
x = range(1, n + 1)  #  x軸的值（1～資料筆數）

# 氣溫
y = dat["平均氣溫"]  # y軸的值（平均氣溫）
plt.plot(x, y)  # 繪圖

# 區間大小:9 的移動平均
v = np.ones(9) / 9.0
y2 = np.convolve(y, v, mode="same")  # 計算移動平均
plt.plot(x[4 : n - 4], y2[4 : n - 4])  # 繪圖
plt.title("繪製移動平均圖")

# 第四張圖
plt.subplot(234)

# 描點畫圓
# 角度
th = np.arange(0, 360)

# 圓周上的點P座標
x = np.cos(np.radians(th))
y = np.sin(np.radians(th))

plt.plot(x, y, "red")
plt.axis("equal")  # 軸比例

# 第五張圖
plt.subplot(235)

# 繪製半徑300的圓（y >= 0）

# 圓的方程式
r = 300  # 半徑
x = np.arange(-r, r + 1)  # x: -300～300
y = np.sqrt(r**2 - x**2)  # y

plt.plot(x, y)
plt.axis("equal")  # 軸比例

# 第六張圖
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="plot 集合 2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)


def f1(x):
    return int(float(bp[x]) / float(school[x]))


def f2(x):
    return float(float(school[x]) / float(bp[x]))


filename = "_data/school.txt"
with open(filename, "r") as fp:
    schools = fp.readlines()

school = list()
for s in schools:
    school.append(int(s.split()[1]))

# 共取得??筆資料 list的用法

filename = "_data/yrborn.txt"
with open(filename, "r") as fp:
    populations = fp.readlines()

yrborn = dict()

for p in populations:
    yr, tl, boy, girl = p.split()
    yrborn[yr] = {"boy": int(boy), "girl": int(girl)}

# 共取得??筆資料 dict的用法

yrlist = sorted(list(yrborn.keys()))
bp = list()
for yr in yrlist:
    boys = yrborn[yr]["boy"]
    girls = yrborn[yr]["girl"]
    bp.append(boys + girls)
yr = range(1986, 2016)
ind = np.arange(len(bp))

# 第一張圖
plt.subplot(231)

plt.plot(yr, bp, lw=2)
plt.xlim(1986, 2015)
plt.title("1986 - 2015 (Total)")

# 第二張圖
plt.subplot(232)

plt.plot(yr, school, lw=2)
plt.xlim(1986, 2015)
plt.title("1986 - 2015 School Numbers")

# 第三張圖
plt.subplot(233)

plt.plot(yr, list(map(f1, ind)), lw=2)
plt.xlim(1986, 2015)
plt.title("Person/School")

# 第四張圖
plt.subplot(234)

plt.plot(yr, list(map(f2, ind)), lw=2, color="r")
plt.xlim(1986, 2015)
plt.title("School/Person")

# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="plot 集合 3",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第1~2張圖
filename = "_data/yrborn.txt"

with open(filename, "r") as fp:
    populations = fp.readlines()

yrborn = dict()

for p in populations:
    yr, tl, boy, girl = p.split()
    yrborn[yr] = {"boy": int(boy), "girl": int(girl)}

ind = np.arange(len(yrborn))
yrlist = sorted(list(yrborn.keys()))
bp = list()
bp_b = list()
bp_g = list()
for yr in yrlist:
    boys = yrborn[yr]["boy"]
    girls = yrborn[yr]["girl"]
    bp.append(boys + girls)
    bp_b.append(boys)
    bp_g.append(girls)

# 第一張圖
plt.subplot(231)

plt.plot(bp)
plt.xlim(0, len(bp) - 1)
plt.title("1986 - 2015 (Total)")

# 第二張圖
plt.subplot(232)

plt.plot(bp_b)
plt.plot(bp_g)
plt.xlim(0, len(bp_b) - 1)
plt.title("1986 - 2015 (Boy:Girl)")


# 第3~4張圖

filename = "_data/yrborn.txt"

with open(filename, "r") as fp:
    populations = fp.readlines()

yrborn = dict()

for p in populations:
    yr, tl, boy, girl = p.split()
    yrborn[yr] = {"boy": int(boy), "girl": int(girl)}

ind = np.arange(1986, 2016)
yrlist = sorted(list(yrborn.keys()))
bp = list()
bp_b = list()
bp_g = list()
for yr in yrlist:
    boys = yrborn[yr]["boy"]
    girls = yrborn[yr]["girl"]
    bp.append(boys + girls)
    bp_b.append(boys)
    bp_g.append(girls)

width = 0.35

# 第三張圖
plt.subplot(233)

plt.plot(ind, bp)
plt.xlim(1986, 2015)
plt.title("1986 - 2015 (Total)")

# 第四張圖
plt.subplot(234)
plt.bar(ind, bp_b, width, color="b")
plt.bar(ind + 0.35, bp_g, width, color="r")
plt.xlim(1986, 2015)
plt.title("1986 - 2015 (Boy:Girl)")

# 第五張圖
plt.subplot(235)

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sinc(x)
plt.plot(x, y)
plt.margins(0.2, 0.2)
plt.title("有 margins設定 ")


# 第六張圖
plt.subplot(236)

# 畫個函數, 標出正的部份!
# 把這個函數大於 0 的地方標示出來。

N = 30 + 1
x = np.linspace(-5, 5, N)  # 含頭尾 分成N個
y = np.sinc(x)

# print(x)
# print(y)

plt.plot(x, y, "black")
plt.plot(x[y > 0], y[y > 0], "ro")
# plt.scatter(x[y>0], y[y>0], c='r')
# print(plt.axis())
plt.title("只標出正的部分")

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="plot 集合 4",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)


# 第二張圖
plt.subplot(232)


# 第三張圖
plt.subplot(233)

# 第四張圖
plt.subplot(234)


# 第五張圖
plt.subplot(235)

print("畫出年收入圖")

# 讀入csv檔
filename = "_data/python_ReadWrite_CSV7_salary.csv"
dat = pd.read_csv(filename, encoding="UTF-8")

# 設定資料
x = dat["年齡"]
y = dat["年收入"]

# 繪圖
plt.plot(x, y)

# 第六張圖
plt.subplot(236)

print("描繪差額圖")
# 資料筆數
cnt = len(dat)

# 取差額
diff_y = []
for i in range(0, cnt - 1):
    diff_y.append(y[i + 1] - y[i])

# 繪圖
plt.plot(x[1:], diff_y)


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
print("作業完成")
print("------------------------------------------------------------")  # 60個


#把字典畫出來
animals = {
    "鼠": 3,
    "牛": 48,
    "虎": 33,
    "兔": 8,
    "龍": 38,
}

plt.plot(range(len(animals.values())), animals.values())
plt.xticks(range(len(animals.values())), animals.keys(), rotation=45)

plt.show()

sys.exit()

