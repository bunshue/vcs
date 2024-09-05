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

print("------------------------------------------------------------")  # 60個

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
    plt.plot(traj[:, 0], traj[:, 1], label="軌跡 : {c}".format(c=cnt))

plt.legend()
plt.title("Random Walk")

print("------------------------------------------------------------")  # 60個
plt.subplot(232)

N = 20
x = np.linspace(0, 6.4, N)

A = 0.8  # 雜訊的振幅
y = np.sin(x) + np.random.rand(1, len(x)) * A - A / 2  # 加入雜訊的點集    # y是numpy.ndarray格式

y = y.tolist()[0]  # y 由 numpy.ndarray格式 轉成list格式, 畫圖要用list格式

plt.plot(x, np.sin(x), "black")  # 無雜訊
plt.plot(x, y, "r")  # 有雜訊
plt.grid()

plt.title("畫雜訊範例 " + str(N) + " 點")

print("------------------------------------------------------------")  # 60個
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

print("------------------------------------------------------------")  # 60個
plt.subplot(234)

# 描點畫圓
# 角度
th = np.arange(0, 360)

# 圓周上的點P座標
x = np.cos(np.radians(th))
y = np.sin(np.radians(th))

plt.plot(x, y, "red")
plt.axis("equal")  # 軸比例

print("------------------------------------------------------------")  # 60個
plt.subplot(235)

# 繪製半徑300的圓（y >= 0）

# 圓的方程式
r = 300  # 半徑
x = np.arange(-r, r + 1)  # x: -300～300
y = np.sqrt(r**2 - x**2)  # y

plt.plot(x, y)
plt.axis("equal")  # 軸比例

print("------------------------------------------------------------")  # 60個
plt.subplot(236)

print("畫點")
plt.plot(0, 0, "-o")  # 在 (0, 1) 上 畫一點
plt.plot(1.5, 1.5, "r-o")
plt.plot(2, -2, "g-o")
plt.plot(-2, -2, "b-o")

radius = 5
degrees = np.arange(0, 360)
x = radius * np.cos(np.radians(degrees))
y = radius * np.sin(np.radians(degrees))

plt.plot(x, y)
plt.axis("equal")
plt.title("畫點 畫圓")

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

print("------------------------------------------------------------")  # 60個
plt.subplot(231)

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sinc(x)
plt.plot(x, y)
plt.margins(0.2, 0.2)
plt.title("有 margins設定 ")

print("------------------------------------------------------------")  # 60個
plt.subplot(232)

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

print("------------------------------------------------------------")  # 60個
plt.subplot(233)

# 畫出y=a^x的函數圖形 0<=x<=10
x = np.linspace(0, 10, 50)
y1 = 2**x
y2 = 2.5**x
y3 = 3**x
y4 = 3.5**x

# 加上圖表標題, 字體大小12, 靠右對齊
plt.title("y=a^x", fontsize=12, loc="right")
# 加上X軸標題(靠右對齊x=1.0為X軸最右)
# horizontalalignment,verticalalignment只是調整與x=1.0之相對位置)
plt.xlabel(
    "x", fontsize=20, horizontalalignment="right", verticalalignment="top", x=1.0
)
# 加上X軸刻度範圍0~10(如果大小顛倒，圖形會左右鏡射)
plt.xlim(0, 10)
# 加上X軸刻度標示 0,1,...,10(只有整數),字體大小16
plt.xticks(list(range(0, 11, 1)), fontsize=16)
# 加上Y軸標題(靠上對齊y=1.0為Y軸最上)
# horizontalalignment,verticalalignment只是調整與y=1.0之相對位置)
plt.ylabel(
    "y", fontsize=20, horizontalalignment="right", verticalalignment="bottom", y=1.0
)
# 加上Y軸刻度範圍0~1200(如果大小顛倒，圖形會上下鏡射)
plt.ylim(0, 1200)
# 加上Y軸刻度標示 0,100,200,...,1200(只有100的倍數),字體大小16
plt.yticks(list(range(0, 1201, 100)), fontsize=16)
# 設定曲線顏色、線條類型、寬度
# 設定顏色1:blue、green、red、cyan、magenta、yellow、black、white
# 設定顏色2:(R, G, B), 0<=R,G,B<=1
# 設定顏色3:#000000~#FFFFFF, RGB各二個十六進位 00~FF
# 設定線條型態:-、--、-.、:
# 設定線條寬度:1~20
# 設定點的形狀:.,ov^<>1234sp*hH+xDd|_
# 設定點的形狀:1~10
plt.plot(x, y1, color="cyan", marker="2", markersize=10)
plt.plot(x, y2, color=(0, 0, 1), linestyle=":", linewidth=2, marker="x", markersize=10)
plt.plot(x, y3, color="#FF0000", linestyle="-.", linewidth=3)
# 設定散佈圖顏色、形狀、大小
# 設定散佈圖點的形狀:.,ov^<>1234sp*hH+xDd|_
# 設定散佈圖點的大小
plt.scatter(x, y4, color="black", marker="x", s=10)

plt.grid()  # 加上格線

# 加上註解
# xy箭頭座標,xytext文字座標, shrink
plt.annotate(
    "y=2^x",
    xy=(9.5, 800),
    xytext=(8, 1100),
    arrowprops=dict(color="cyan", shrink=0.01),
    color="cyan",
)

# 加上圖例說明
plt.legend(["a=2", "a=2.5", "a=3", "a=3.5"], fontsize=20)

print("------------------------------------------------------------")  # 60個
plt.subplot(234)

x1 = np.linspace(0.1, 10, 99)  # 建立含30個元素的陣列
x2 = np.linspace(0.1, 10, 99)  # 建立含30個元素的陣列
y1 = [math.log2(x) for x in x1]
y2 = [math.log(x, 0.5) for x in x2]

plt.plot(x1, y1, label="基底 = 2")
plt.plot(x2, y2, label="基底 = 0.5")

plt.axis([0, 10, -5, 5])
plt.legend(loc="best")  # 建立圖例

print("------------------------------------------------------------")  # 60個
plt.subplot(235)

print("畫出年收入圖")

# 讀入csv檔
filename = "_data/python_ReadWrite_CSV7_salary.csv"
dat = pd.read_csv(filename, encoding="UTF-8")

# 設定資料
x = dat["年齡"]
y = dat["年收入"]

plt.plot(x, y)

print("------------------------------------------------------------")  # 60個
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

plt.figure(
    num="plot 集合 3",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個
plt.subplot(231)

# 時序圖
import matplotlib.dates as mdates

#     2017/0808/2100    2017/0808/2101    2017/0808/2102    2017/0808/2103
x = [
    "20170808210000",
    "20170808210100",
    "20170808210200",
    "20170808210300",
    "20170808210400",
    "20170808210500",
    "20170808210600",
    "20170808210700",
    "20170808210800",
    "20170808210900",
]

x = pd.to_datetime(x)
y = [3900.0, 3903.0, 3891.0, 3888.0, 3893.0, 3899.0, 3906.0, 3914.0, 3911.0, 3912.0]

plt.plot(x, y)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m-%d %H:%M"))  # 設置時間顯示格式
plt.gcf().autofmt_xdate()  # 自動旋轉角度，以避免重疊

print("------------------------------------------------------------")  # 60個
plt.subplot(232)

# 把字典畫出來
animals = {
    "鼠": 3,
    "牛": 48,
    "虎": 33,
    "兔": 8,
    "龍": 38,
}

plt.plot(range(len(animals.values())), animals.values())
plt.xticks(range(len(animals.values())), animals.keys(), rotation=30)

print("------------------------------------------------------------")  # 60個
plt.subplot(233)

print("------------------------------------------------------------")  # 60個
plt.subplot(234)

print("------------------------------------------------------------")  # 60個
plt.subplot(235)

print("------------------------------------------------------------")  # 60個
plt.subplot(236)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi, 200)
N = 20

plt.figure(figsize=(12, 8))

for i in range(N):
    plt.subplot(221)
    plt.plot(x, i * np.sin(x), color=plt.cm.hsv(i / N))
    plt.subplot(222)
    plt.plot(x, i * np.sin(x), color=plt.cm.rainbow(i / N))
    plt.subplot(223)
    plt.plot(x, i * np.sin(x), color=plt.cm.cool(i / N))
    plt.subplot(224)
    plt.plot(x, i * np.sin(x), color=plt.cm.hot(i / N))

plt.subplot(221)
plt.title("hsv")
plt.subplot(222)
plt.title("rainbow")
plt.subplot(223)
plt.title("cool")
plt.subplot(224)
plt.title("hot")

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


plt.plot(seq, data1, "-*")
plt.plot(seq, data2, "m-o")
plt.plot(seq, data2, "-o")
plt.plot(seq, data3, "-^")
plt.plot(seq, data4, "-s")
plt.plot(x1, y1, "go-")
plt.plot(x2, y2, "m.-")



