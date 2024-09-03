"""
scatter 集合
散布圖 Scatter Chart
散點圖

matplotlib.pyplot.scatter(x, 
    y, 
    s=20, 
    c='b', 
    marker='o', 
    cmap=None, 
    norm=None, 
    vmin=None, 
    vmax=None, 
    alpha=None, 
    linewidths=None, 
    verts=None, 
    hold=None, 
    **kwargs)

參數：
    x，y：表示的是shape大小為(n,)的數組，也就是我們即將繪制散點圖的數據點，輸入數據。
    s：表示的是大小，是一個標量或者是一個shape大小為(n,)的數組，可選，默認20。
    c：表示的是色彩或顏色序列，可選，默認藍色’b’。但是c不應該是一個單一的RGB數字，也不應該是一個RGBA的序列，因為不便區分。c可以是一個RGB或RGBA二維行數組。
     
    marker：MarkerStyle，表示的是標記的樣式，可選，默認’o’。
    cmap：Colormap，標量或者是一個colormap的名字，cmap僅僅當c是一個浮點數數組的時候才使用。如果沒有申明就是image.cmap，可選，默認None。
    norm：Normalize，數據亮度在0-1之間，也是只有c是一個浮點數的數組的時候才使用。如果沒有申明，就是默認None。
    vmin，vmax：標量，當norm存在的時候忽略。用來進行亮度數據的歸一化，可選，默認None。
    alpha：標量，0-1之間，可選，默認None。
    linewidths：也就是標記點的長度，默認None。

matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, 
vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, hold=None, data=None, **kwargs)

基本參數講解

x, y → 散點的坐標
s → 散點的面積
c → 散點的顏色（默認值為藍色，'b'，其余顏色同plt.plot( )）
marker → 散點樣式（默認值為實心圓，'o'，其余樣式同plt.plot( )）
alpha → 散點透明度（[0, 1]之間的數，0表示完全透明，1則表示完全不透明）
linewidths →散點的邊緣線寬
edgecolors → 散點的邊緣顏色

高級參數講解

cmap → 指的是matplotlib.colors.Colormap，相當于多個調色盤的合集
norm、vmin、vmax → 散點顏色亮度設置


matplotlib.pyplot.scatter(x, y, s=None, 
                            c=None, marker=None, 
                            cmap=None, norm=None, 
                            vmin=None, vmax=None, 
                            alpha=None, linewidths=None, 
                            verts=None, edgecolors=None, 
                            **kwargs)

x，y：輸入數據的x，y軸
s：標量或數組，可選參數，散點圖點的大小
c：顏色或顏色序列，可選參數，默認為藍色
marker：散點圖中點的形狀，默認為圓點
cmap：色圖，僅在c是浮點數組的情況下使用
norm：設置數據亮度，用于將亮度數據縮放到0~1之間。僅當c是浮點數組的情況下使用
vmin，vmax：亮度設置，與norm類似，只是設置縮放的范圍，當使用了norm參數，則該參數無效
alpha：透明度設置，0（透明）~1（不透明）之間
linewidths：設置散點邊界線的寬度
verts：如果marker參數為空，則用（x，y）序列來構造marker，中心的點被置為（0，0），其他點被s重新縮放
edgecolors：設置散點邊界線的顏色

"""

N = 500

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
'''
print("------------------------------------------------------------")  # 60個

plt.figure(
    num="scatter 集合 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個
plt.subplot(231)


print("------------------------------------------------------------")  # 60個
plt.subplot(232)

N = 30
degrees = np.arange(0, 360, N)
x = np.cos(np.radians(degrees))
y = np.sin(np.radians(degrees))

size = 300
plt.scatter(x, y, s=size)
plt.plot(x, y, "r")


print("------------------------------------------------------------")  # 60個
plt.subplot(233)

R = 10
degrees = [x * 15 for x in range(0, 25)]
print(degrees)
x = [R * math.cos(math.radians(d)) for d in degrees]
y = [R * math.sin(math.radians(d)) for d in degrees]
size = 300
plt.scatter(x, y, s=size)


print("------------------------------------------------------------")  # 60個
plt.subplot(234)

N = 1024
X = np.random.normal(0, 1, N)
Y = np.random.normal(0, 1, N)
T = np.arctan2(Y, X)

plt.scatter(X, Y, s=75, c=T, alpha=0.5)

plt.xlim(-3.5, 3.5)
plt.ylim(-3.5, 3.5)

print("------------------------------------------------------------")  # 60個
plt.subplot(235)

X = []
Y = []
for i in range(1000):
    x = random.randint(0, 10) + random.random()
    y = random.randint(0, 10) + random.random()
    if ((x - 5) ** 2 + (y - 5) ** 2) > 25:
        continue
    else:
        X.append(x)
        Y.append(y)
# print(len(X))

plt.scatter(X, Y)

plt.axis([0, 10, 0, 10])
plt.axis("equal")
plt.title("蒙地卡羅模擬")


print("------------------------------------------------------------")  # 60個
plt.subplot(236)


# 試著做三群的數據。
N = 500  # 每一群都是 N 個點

cx0 = 0
cy0 = 0
x0 = np.random.randn(N) + cx0
y0 = np.random.randn(N) + cy0

cx1 = -3
cy1 = 3
x1 = np.random.randn(N) + cx1
y1 = np.random.randn(N) + cy1

cx2 = 3
cy2 = 3

x2 = np.random.randn(N) + cx2
y2 = np.random.randn(N) + cy2

# 合併三群的點到 x, y 之中。
x = np.concatenate((x0, x1, x2))
y = np.concatenate((y0, y1, y2))

# 現在第一群的點是第 0 類, 第二群是第 1 類, 第三群是第 2 類，所以我們要做個像這樣
# [0, 0, ..., 0, 1, 1, ..., 1, 2, 2, ..., 2] 的標記。

c = np.repeat([0, 1, 2], N)

plt.scatter(x, y, c=c, cmap="Set1")
plt.scatter([cx0, cx1, cx2], [cy0, cy1, cy2], [200, 200, 200], ["r", "g", "b"])

plt.title("三群數據")


plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="scatter 集合 2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個
plt.subplot(231)

# 額外設定 s、c 和 cmap，就能根據資料點的數據，對應出指定的顏色，
# 假設資料的範圍是 0～100，顏色地圖是紅橙黃綠藍，
# 則 0～20 對應紅色，21～40 對應橙色，
# 41～60 對應黃色，61～80 對應綠色，81～100 對應藍色。

x = range(1, 11)  # 1 2 3 ... 10
y = range(1, 11)  # 1 2 3 ... 10
X, Y = np.meshgrid(x, y)

size = [i * 80 for i in Y]  # 放大資料點數據 N 倍，比較容易觀察尺寸

plt.scatter(X, Y, s=size, c=size, cmap="Set1")  # 使用 Set1 的 colormap

"""
# 加上 vmin 和 vmax 的設定，能設定顏色的最大值與最小值
# 當數值小於 vmin 時，只會顯示紅色，當數值大於 vmax 時，只會顯示灰色。
plt.scatter(X, Y, s=size, c=size, cmap="Set1", vmin=200, vmax=650)
# plt.colorbar()
"""

# plt.colorbar()

print("------------------------------------------------------------")  # 60個
plt.subplot(232)


def loc(index):
    # 處理座標的移動
    x_mov = random.choice([-3, -2, -1, 1, 2, 3])  # 隨機x軸移動值
    xloc = x[index - 1] + x_mov  # 計算x軸新位置
    y_mov = random.choice([-5, -3, -1, 1, 3, 5])  # 隨機y軸移動值
    yloc = y[index - 1] + y_mov  # 計算y軸新位置
    x.append(xloc)  # x軸新位置加入串列
    y.append(yloc)  # y軸新位置加入串列


N = 10000  # 設定隨機點的數量
x = [0]  # 設定第一次執行x座標
y = [0]  # 設定第一次執行y座標

for i in range(1, N):  # 建立點的座標
    loc(i)
t = x  # 色彩隨x軸變化
plt.scatter(x, y, s=2, c=t, cmap="brg")

print("------------------------------------------------------------")  # 60個
plt.subplot(233)

N = 50  # 散點的數量
r = 0.5  # 邊界線boundary半徑
x = np.random.rand(N)  # 隨機的 x 座標點
y = np.random.rand(N)  # 隨機的 y 座標點

size = []
for i in range(N):  # 建立散點區域陣列
    size.append(30)

colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
colors = []
for i in range(N):  # 隨機設定 N 個顏色
    colors.append(np.random.choice(colorused))

size1 = np.ma.masked_where(x < r, size)  # 邊界線 0.5 內區域遮罩
size2 = np.ma.masked_where(x >= r, size)  # 邊界線 0.5 (含)外區域遮罩

# 大於或等於 0.5 繪製星形, 小於 0.5 繪製圓形
plt.scatter(x, y, s=size1, marker="*", c=colors)
plt.scatter(x, y, s=size2, marker="o", c=colors)

# 繪製邊界線
plt.plot((0.5, 0.5), (0, 1.0))  # 繪製邊界線

print("------------------------------------------------------------")  # 60個
plt.subplot(234)

N = 50  # 散點的數量
r = 0.5  # 邊界線boundary半徑
x = np.random.rand(N)  # 隨機的 x 座標點
y = np.random.rand(N)  # 隨機的 y 座標點

size = np.random.randint(20, 100, N)  # 散點大小
colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
colors = []
for i in range(N):  # 隨機設定 N 個顏色
    colors.append(np.random.choice(colorused))

r1 = np.sqrt(x**2 + y**2)  # 計算距離
size1 = np.ma.masked_where(r1 < r, size)  # 邊界線 0.5 內區域遮罩
size2 = np.ma.masked_where(r1 >= r, size)  # 邊界線 0.5 (含)外區域遮罩

# 大於或等於 0.5 繪製星形, 小於 0.5 繪製圓形
plt.scatter(x, y, s=size1, marker="*", c=colors)
plt.scatter(x, y, s=size2, marker="o", c=colors)

# 計算 0.5Pi 之弧度, 依據弧度產生的座標點繪製邊界線
radian = np.arange(0, np.pi / 2, 0.01)
plt.plot(r * np.cos(radian), r * np.sin(radian))  # 繪製邊界線

print("------------------------------------------------------------")  # 60個
plt.subplot(235)


print("------------------------------------------------------------")  # 60個
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="scatter 集合 3",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個
plt.subplot(231)

N = 10
x = np.random.rand(N)
y = np.random.rand(N)

colors = np.random.rand(N)  # 色彩數列
size = 300

# 把linewidths參數改成數組。
lines = np.zeros(N) + 5
print(lines)

# 修改其中的linewidth參數的大小，但是沒什么不同，**注意：**只有marker為封閉的圖案的時候，這個參數才有效。
# plt.scatter(x, y, s=size, c=colors, alpha=0.5, marker="x", linewidths=lines) # NG
plt.scatter(x, y, s=size, c=colors, alpha=0.5, linewidths=lines)

print("------------------------------------------------------------")  # 60個
plt.subplot(232)

"""
搭配 NumPy 繪製散布圖
由於 matplotlib 能完美的和 NumPy 整合，
所以能透過 NumPy 強大的處理或產生數據能力，快速產生許多繪圖用的數據，
下方的例子，使用 NumPy 產生每組 10 個共三組 100～2000 隨機數字 y 和 size，
使用 matplotlib 繪製出散布圖 ( 如果不指定顏色，每組數據會自動套用不同的顏色 )。
"""

x = range(0, 10)
y = np.random.randint(100, 2000, size=(3, 10))  # 產生 3x10 陣列，內容為 100～2000 隨機數字
size = 300
for i in range(0, 3):
    plt.scatter(x, y[i], s=size, alpha=0.5)

print("------------------------------------------------------------")  # 60個
plt.subplot(233)

# np.random.randint(0, 3, 10)
x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
X, Y = np.meshgrid(x, y)
size = 300

plt.scatter(
    X.ravel(),
    Y.ravel(),
    s=size,
    c=[0, 1, 2, 1, 1, 2, 1, 1, 0, 1, 1, 0, 0, 0, 2, 1],
    cmap="Paired",
)

print("------------------------------------------------------------")  # 60個
plt.subplot(234)

N = 20

x = np.random.randn(N)
y = np.random.randn(N)
size = 300

colors = np.random.rand(N)  # 色彩數列

plt.scatter(x, y, c=colors, s=size, alpha=0.3, cmap="viridis")
# plt.colorbar()

# 這里從cmap中選取了一個叫做'viridis'的調色盤，
# 其作用是，將參數c中獲取到的數值，映射到“色盤”中已經對應好的顏色上
# 并且上圖中從“色盤”viridis中獲取到的顏色，
# 可以通過plt.colorbar( )顯示為顏色條（與熱力圖同理）。

print("------------------------------------------------------------")  # 60個
plt.subplot(235)

N = 20

x = np.random.randint(1, 11, N)
y = np.random.randint(1, 11, N)

size = 300

colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
colors = []  # 建立色彩數列
for i in range(N):  # 隨機設定顏色
    colors.append(np.random.choice(colorused))

plt.scatter(x, y, s=size, c=colors)  # 繪製散點

print("------------------------------------------------------------")  # 60個
plt.subplot(236)

from matplotlib import colors  # 為了調整“色盤”，需要導入colors

N = 20

x = np.random.randn(N)
y = np.random.randn(N)

size = 300

color = np.random.rand(N)  # 色彩數列

changecolor = colors.Normalize(vmin=0.4, vmax=0.8)

plt.scatter(x, y, c=color, s=size, alpha=0.3, cmap="viridis", norm=changecolor)
# plt.colorbar()

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("scatter參數大合集")

plt.figure(figsize=(12, 8))

N = 1000
A = 10  # 震幅

# 使用隨機陣列產生圖像
x = A * np.random.rand(N)  # 0~A取N個數出來
y = A * np.random.rand(N)  # 0~A取N個數出來

colors = np.random.rand(N)  # 色彩數列
size = 300

# plt.scatter(x, y)

# plt.scatter(x, y, s=size, c=colors, alpha=0.5)
plt.scatter(x, y, c=y, cmap="hsv")  # 色彩依 y 軸值變化
# plt.scatter(x, y, s=size, c=colors, alpha=0.5, marker="x")#使用marker
# plt.scatter(x, y, s=size, c=colors, marker="*")#使用marker 方塊
# plt.scatter(x, y, s=size, c=colors, marker="s")#使用marker 星形
# plt.scatter(x, y, color="red", marker="^") # 指名marker和顏色
# plt.scatter(x, y, s=size, c="r")  # 指定顏色與大小

# plt.colorbar()

""" 各種scatter的語法
# 給散佈圖的點套上不同深淺顏色
# c = np.random.choice(np.arange(100), 100)
# plt.scatter(x, y, s=c, c=c, cmap="viridis")

plt.scatter(x, y, alpha=0.5)
plt.scatter(x, y, alpha=0.5, s=100)

plt.scatter(x, y, alpha=0.5, s=100, color="red")
plt.scatter(x, y, alpha=0.5, s=100, color="blue")

print("color：顏色串列， color=['r','g','b','c','m'], 若有多組數據 依序顯示顏色")
print("alpha : 透明度")

"""

plt.title("scatter參數大合集")
plt.xlabel("")
plt.ylabel("")

plt.show()

print("------------------------------------------------------------")  # 60個

print("散佈圖")

x = np.arange(6)
y = x/3 - 1
t = x/3  # 色彩隨 x 軸值變化

plt.scatter(x, y, c=t, s=500, cmap="rainbow")
plt.scatter(x, y, c=x, s=500, cmap="rainbow", marker="*")  # 繪製 sin
plt.scatter(x, y, c=x, s=500, cmap="rainbow", marker="s")  # 繪製 cos
plt.scatter(x, y, c=y, s=500, cmap="rainbow", marker="*")  # 繪製 sin
plt.scatter(x, y, c=y, s=500, cmap="rainbow", marker="s")  # 繪製 cos
plt.scatter(x, y, c=t, s=100, cmap="brg")
plt.scatter(x, y, c="blue", marker=".")
plt.scatter(x, y, color="lightgreen", edgecolor="b", s=80)
plt.scatter(x, y, c=y, cmap="rainbow")
plt.scatter(x, y, s=300, c=y, cmap="hsv")  # 色彩隨y軸值變化
plt.scatter(x, y, s = 100, c = 'b', alpha = 0.5)   # 設定透明度為 0.5
plt.scatter(x, y, s = 100, c = 'r', alpha = 0.5)   # 設定透明度為 0.5

N = 50
x = np.linspace(0, 6.2, N)  # 建立含 N 個元素的陣列
y = np.sin(x)  # y陣列的變化
lwidths = (1 + x) ** 2  # 寬度陣列

plt.scatter(x, y, s=lwidths, c=x, cmap="hsv")  # hsv色彩映射圖

plt.show()
'''
print("------------------------------------------------------------")  # 60個

N = 50  # 色彩數列的點數

x = np.linspace(0.0, 2 * np.pi, N)  # 建立 50 個點
y = np.sin(x)

colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
colors = []  # 建立色彩數列
for i in range(N):  # 隨機設定顏色
    colors.append(np.random.choice(colorused))

plt.scatter(x, y, c=colors, marker="*")  # 繪製 sin

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


"""
#多組數據的散布圖
#如果有多組數據需要同時呈現，可以獨立繪製每組散布圖，完成後再使用 show() 的方式顯示散布圖。

x = [1,2,3,4,5,6,7,8,9,10]

y1 = [11,8,26,16,9,17,23,4,14,10]   # 第一組的 Y 軸數據
s1 = [i*100 for i in y1]            # 將第一組的 Y 軸數據放大 100 倍作為園點尺寸

y2 = [19,29,15,12,21,6,7,8,18,2]    # 第二組的 Y 軸數據
s2 = [i*100 for i in y2]            # 將第二組的 Y 軸數據放大 100 倍作為園點尺寸

----
#連接2點的直線

# 資料
x = np.arange(1, 5.1, 0.1)
y = 1/2*x + (1/2)

# 繪圖
plt.scatter(x, y)
plt.grid(color='0.8')

----

#畫不同顏色的scatter
cl = np.random.randint(1, 4, 100)
plt.scatter(x, y, s=100, c=cl, alpha=0.6, cmap="Paired")

----


"""


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


# x，y，大小，顏色
plt.scatter([1, 2, 3, 4], [2, 4, 6, 8], [10, 20, 30, 400], ["r", "b", "y", "k"])
plt.scatter([1, 2, 3, 4], [9, 8, 7, 6], s=10, c="b", marker="v")

s = plt.scatter([1, 2, 3], [4, 5, 6])


# plt.colorbar()

# 由平均 0, 標準差 1 的分布中取 20 個數
# np.random.randn(20)

# 試取 100 個, 算平均、標準差

x = np.arange(N)
g = np.random.randn(N)
g.mean()
g.std()

# 不同的平均值和標準差
# 比如我們想要平均值變成 70, 標準差 10 怎麼做呢?
# g2 = g*10 + 70

print(g)
# g.sort()
print(g)


x = [x for x in range(1, 16)]
y = [(y * y) for y in x]


# Map each onto a scatterplot we'll create with Matplotlib
plt.scatter(x=x, y=y, c=scale, s=np.abs(scale) * 800)


theta = 2 * random.random() * math.pi
r = random.random() * 5
x = math.cos(theta) * r + 5
y = math.sin(theta) * r + 5


plt.legend(loc="best")  # 添加圖例

N = 20
x = np.linspace(0, 5, N)  # 含N個元素的陣列

plt.scatter(x, y, s=300, c=y, cmap="rainbow")  # 色彩隨 y 軸值變化
# plt.colorbar()

print("------------------------------------------------------------")  # 60個

plt.scatter(x, y, s=N, c=x, cmap="brg")  # 繪製散點圖


colors = np.array(["b", "c", "g", "k", "m", "r", "y", "pink", "purple", "orange"])
plt.scatter(x, y1, c=colors, label="圓形標記")
plt.scatter(x, y2, c=colors, marker="*", label="星形標記")
plt.scatter(x, y1, c=colors, marker="*")  # 繪製 sine
plt.scatter(x, y2, c=colors, marker="s")  # 繪製 cos
plt.scatter(x, y1, c="b", marker="x")  # 繪製 sine wave
plt.scatter(x, y2, c="g", marker="X")  # 繪製 cos wave
plt.scatter(x, y1, c=colors, marker="*")  # 繪製 sine
plt.scatter(x, y2, c=colors, marker="s")  # 繪製 cos

x = np.linspace(0, 1, 1000)
y = 0.5 * np.sin(n * x) + 0.5

plt.scatter(listx, listy, c="r", s=scale, marker="o", alpha=0.5)

plt.axis("off")  # 隱藏座標
plt.axis("off")  # 隱藏座標

N = 20
x = np.linspace(0, 5, N)  # 含N個元素的陣列
y = np.linspace(0, 5, N)  # 含N個元素的陣列

plt.scatter(x, y, s=300, c=x, cmap="rainbow")  # 色彩隨 x 軸值變化
plt.scatter(x, y, s=300, c=y, cmap="rainbow")  # 色彩隨 y 軸值變化

colors = np.array(["b", "c", "g", "k", "m", "r", "y", "pink", "purple", "orange"])

# 建立多邊形標記
axs[0, 0].scatter(x, y, s=75, c=colors, marker=(5, 0))
axs[0, 0].set_title("多邊形marker=(5, 0)")

# 建立星形標記
axs[0, 1].scatter(x, y, s=75, c=colors, marker=(5, 1))
axs[0, 1].set_title("星狀形marker=(5, 1)")

# 建立鑽石標記
axs[0, 2].scatter(x, y, s=75, c=colors, marker=(5, 2))
axs[0, 2].set_title("鑽石形marker=(5, 2)")

# 建立 aplha 標記
axs[1, 0].scatter(x, y, s=100, c=colors, marker=r"$\alpha$")
axs[1, 0].set_title(r"${alpha=}\alpha$" + "標記", c="b")

# 建立 beta 標記
axs[1, 1].scatter(x, y, s=100, c=colors, marker=r"$\beta$")
axs[1, 1].set_title(r"${beta=}\beta$" + "標記", c="b")

# 建立 gamma 標記
axs[1, 2].scatter(x, y, s=100, c=colors, marker=r"$\gamma$")
axs[1, 2].set_title(r"${gamma=}\gamma$" + "標記", c="b")

# 建立 clubsuit 標記
axs[2, 0].scatter(x, y, s=100, c=colors, marker=r"$\clubsuit$")
axs[2, 0].set_title(r"${clubsuit=}\clubsuit$" + "標記", c="b")

# 建立 spadesuit 標記
axs[2, 1].scatter(x, y, s=100, c=colors, marker=r"$\spadesuit$")
axs[2, 1].set_title(r"${spadesuit=}\spadesuit$" + "標記", c="b")

# 建立 heartsuit 標記
axs[2, 2].scatter(x, y, s=100, c=colors, marker=r"$\heartsuit$")
axs[2, 2].set_title(r"${heartsuit=}\heartsuit$" + "標記", c="b")


""" 搬到pd plot

filename = "_data/python_ReadWrite_CSV6_score.csv"

# 讀入資料
dat = pd.read_csv(filename, encoding="UTF-8")

# 散布圖
plt.scatter(dat["數學"], dat["理科"])
plt.axis([0, 100, 0, 100])
plt.axis("equal")
plt.xlabel("數學")
plt.ylabel("理科")

# 共變異數與相關係數
correlation = np.corrcoef(dat["數學"], dat["理科"])  # 計算相關係數
correlation[0, 1]  # 顯示在畫面

"""

print("建立任意大小陣列")
size = (30 * np.random.rand(N)) ** 2  # 散點大小數列
size = 700 * np.random.rand(N)  # 隨機產生N個用于改變散點面積的數值
size = np.random.randint(100, 2000, size=(3, 10))  # 產生 3x10 陣列，內容為 100～2000 隨機數字

plt.xticks(np.arange(0, 12, step=1.0))  # x 軸刻度
plt.yticks(np.arange(0, 12, step=1.0))  # y 軸刻度
plt.xticks(np.arange(0, 11, step=1.0))
plt.yticks(np.arange(0, 11, step=1.0))

# 由於點可能疊加，設置透明度爲0.5

N = 20
x = np.random.randint(1, 11, N)
y = np.random.randint(1, 11, N)


x = np.random.randn(N)
y = np.random.randn(N)



""" fail
#zip 高級組合法

xx = [1, 2, 3, 4]
yy = [5, 6, 7, 8]
list(zip(xx, yy))

Z = list(zip(X, Y))
print(Z)

plt.scatter(X, Y, s = 300, c = Z)
plt.show()
"""

print("------------------------------------------------------------")  # 60個


plt.xticks(())  # 不顯示 x 刻度
plt.yticks(())  # 不顯示 y 刻度

N = 100
x = np.random.randint(30, size=N)
y = np.random.randint(30, size=N)

plt.scatter(x, y, s=size, c=color, cmap="Greens", norm=norm)
plt.scatter(x, y, s=size, alpha=0.5, c=color, cmap="Greens", norm=norm)
plt.scatter(x, y, s=size, alpha=0.5, c=color, cmap="jet", norm=norm)

