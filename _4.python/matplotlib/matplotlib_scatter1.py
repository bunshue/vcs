# scatter 集合
# 散布圖 Scatter Chart
# 散點圖

import sys
import numpy as np
import matplotlib.pyplot as plt
import math
import random
import pandas as pd

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

#          編號                  圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="scatter 集合 1a random",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

N = 500


"""
#一般random
x = np.random.rand(N) #N個0~1之間的亂數
y = np.random.rand(N)
plt.scatter(x, y)
plt.scatter(x, y, c=y, cmap = 'hsv')  # 色彩依 y 軸值變化
plt.scatter(x, y, s=100, c='r', marker='*',alpha=0.65)
plt.colorbar()

"""

"""
#常態分佈
#常態random

x = np.random.randn(N)
y = np.random.randn(N)
#plt.scatter(x, y)
plt.scatter(x, y, c = 'r', s = 100)
"""

# Generate 100 random data points along 3 dimensions
x, y, scale = np.random.randn(3, 100)
# Map each onto a scatterplot we'll create with Matplotlib
plt.scatter(x=x, y=y, c=scale, s=np.abs(scale) * 500)


# 第二張圖
plt.subplot(232)

plt.xlim(-3, 3)
plt.ylim(-3, 3)
x1 = np.random.normal(0, 1, 1024)
y1 = np.random.normal(0, 1, 1024)
plt.scatter(x1, y1, alpha=0.3)

# 第三張圖
plt.subplot(233)

# 使用 NumPy 隨機數的「常態分佈」產生 N 個數據點，再透過 matplotlib 畫出散布圖。
N = 500
x = np.random.normal(5, 50, N)
y = np.random.normal(5, 50, N)
plt.scatter(x, y, alpha=0.5, s=100)

# 第四張圖
plt.subplot(234)

"""
搭配 NumPy 繪製散布圖

由於 matplotlib 能完美的和 NumPy 整合，
所以能透過 NumPy 強大的處理或產生數據能力，快速產生許多繪圖用的數據，
下方的例子，使用 NumPy 產生每組 10 個共三組 100～2000 隨機數字 y 和 size，
使用 matplotlib 繪製出散布圖 ( 如果不指定顏色，每組數據會自動套用不同的顏色 )。
"""

x = range(0, 10)
y = np.random.randint(100, 2000, size=(3, 10))  # 產生 3x10 陣列，內容為 100～2000 隨機數字
size = np.random.randint(100, 2000, size=(3, 10))  # 產生 3x10 陣列，內容為 100～2000 隨機數字
for i in range(0, 3):
    plt.scatter(x, y[i], s=size[i], alpha=0.5)

# 第五張圖
plt.subplot(235)

np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y)

# 第六張圖
plt.subplot(236)

np.random.seed(0)

x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y, marker="^", color="red")

plt.show()

print("------------------------------------------------------------")  # 60個

#          編號                      圖像大小[英吋]     解析度    背景色                    邊框顏色                         邊框有無
plt.figure(
    num="scatter 集合 1b random",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

X = []
Y = []
for i in range(1000):
    theta = 2 * random.random() * math.pi
    r = random.random() * 5
    x = math.cos(theta) * r + 5
    y = math.sin(theta) * r + 5
    X.append(x)
    Y.append(y)

plt.scatter(X, Y)
print(len(X))
plt.axis([0, 10, 0, 10])
plt.axis("equal")  # 軸比例

# 第二張圖
plt.subplot(232)

X = []
Y = []
for i in range(1000):
    x = random.randint(0, 10) + random.random()
    y = random.randint(0, 10) + random.random()
    if ((x - 5) ** 2 + (y - 5) ** 2) > 25:
        # print('Reject ({0}, {1})'.format(x, y))
        continue
    else:
        X.append(x)
        Y.append(y)
print(len(X))

plt.scatter(X, Y)
print(len(X))
plt.axis([0, 10, 0, 10])
plt.axis("equal")  # 軸比例

# 第三張圖
plt.subplot(233)

# Fixing random state for reproducibility
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N)) ** 2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)

# 第四張圖
plt.subplot(234)


import numpy as np
from matplotlib import pyplot as plt

n = 300
ax = np.random.normal(0, 1, n)
ay = np.random.normal(0, 1, n)
bx = np.random.normal(0, 1, n)
by = np.random.normal(0, 1, n)

plt.scatter(ax, ay, alpha=0.5, s=100, color="red")
plt.scatter(bx, by, alpha=0.5, s=100, color="blue")
plt.xlim = (0, 1)
plt.ylim = (0, 1)


# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)

# 試著做三群的數據。

cx0 = 0
cy0 = 0

cx1 = -3
cy1 = 3

cx2 = 3
cy2 = 3

# 每一群都是 500 個點

x0 = np.random.randn(500) + cx0
y0 = np.random.randn(500) + cy0

x1 = np.random.randn(500) + cx1
y1 = np.random.randn(500) + cy1

x2 = np.random.randn(500) + cx2
y2 = np.random.randn(500) + cy2

# 合併三群的點到 x, y 之中。
x = np.concatenate((x0, x1, x2))
y = np.concatenate((y0, y1, y2))

"""
現在第一群的點是第 0 類, 第二群是第 1 類, 第三群是第 2 類，所以我們要做個像這樣
[0, 0, ..., 0, 1, 1, ..., 1, 2, 2, ..., 2]
的標記。
"""

c = np.repeat([0, 1, 2], 500)

plt.scatter(x, y, c=c, cmap="Set1")

plt.show()

print("------------------------------------------------------------")  # 60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="scatter 集合 2",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

# Hyperlinks

s = plt.scatter([1, 2, 3], [4, 5, 6])
s.set_urls(["https://www.bbc.com/news", "https://www.google.com/", None])


# 第二張圖
plt.subplot(232)


N = 50  # 色彩數列的點數
colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
colors = []  # 建立色彩數列
for i in range(N):  # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.random.randint(1, 11, N)  # 建立 x
y = np.random.randint(1, 11, N)  # 建立 y
size = (30 * np.random.rand(N)) ** 2  # 散點大小數列
plt.scatter(x, y, s=size, c=colors)  # 繪製散點
plt.xticks(np.arange(0, 12, step=1.0))  # x 軸刻度
plt.yticks(np.arange(0, 12, step=1.0))  # y 軸刻度


# 第三張圖
plt.subplot(233)

POINTS = 10
# 由平均 0, 標準差 1 的分布中取 20 個數
# np.random.randn(20)

# 試取 100 個, 算平均、標準差

x = np.arange(POINTS)
g = np.random.randn(POINTS)
g.mean()
g.std()

# 不同的平均值和標準差
# 比如我們想要平均值變成 70, 標準差 10 怎麼做呢?
# g2 = g*10 + 70

print(g)
# g.sort()
print(g)

plt.scatter(x, g, c="blue", marker=".")


# 第四張圖
plt.subplot(234)

# 設定資料點的大小
np.random.seed(0)

x = np.random.randn(100)
y = np.random.randn(100)

size = np.random.choice(np.arange(100), 100)

plt.scatter(x, y, s=30)
plt.tight_layout()

# 第五張圖
plt.subplot(235)


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


# 第六張圖
plt.subplot(236)


def loc(index):
    # 處理座標的移動
    x_mov = random.choice([-3, -2, -1, 1, 2, 3])  # 隨機x軸移動值
    xloc = x[index - 1] + x_mov  # 計算x軸新位置
    y_mov = random.choice([-5, -3, -1, 1, 3, 5])  # 隨機y軸移動值
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
# plt.axis('off')

plt.show()

print("------------------------------------------------------------")  # 60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="scatter 集合 3 雜訊",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

N = 200

# 曲線資料加入雜訊
# y = sin(x)
x = np.linspace(0, 10, N)

y1 = np.sin(x)
y1n = y1 + 0.3 * np.random.randn(N)  # 加上noise
plt.scatter(x, y1n, c="red")

y2 = np.sin(x)
y2n = y1 + np.random.rand(1, len(y2)) * 1.5
plt.scatter(x, y2n, c="blue", marker=".")

plt.plot(x, y1, "lime")
plt.plot(x, y2 + 0.75, "green")
plt.title("曲線資料加入雜訊")

# 第二張圖
plt.subplot(232)

# 給散佈圖的點套上不同深淺顏色

np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)
c = np.random.choice(np.arange(100), 100)
plt.scatter(x, y, s=c, c=c, cmap="viridis")

# 第三張圖
plt.subplot(233)


# 第四張圖
plt.subplot(234)


# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)

from pylab import *

rc("xtick.major", pad=8)

data = """
   Sovereign of the Seas   90     1637   1,522                                             2,500             Sail Three-Decker                  Lavery        
   Naseby                  80     1655   1,258                                             2,100             Sail Three-Decker                  Lavery        
   Prince                 100     1670   1,403                                             2,300             Sail Three-Decker                  Lavery        
   Royal James            100     1671   1,416                                             2,300             Sail Three-Decker                  Lavery        
   Royal Charles          100     1673   1,443                                             2,400             Sail Three-Decker                  Lavery        
   Royal James            100     1675   1,422                                             2,400             Sail Three-Decker                  Lavery        
   Royal Prince            92     1663   1,432                                             2,400             Sail Three-Decker                  Lavery        
   Britannia              100     1682   1,739                                             2,900             Sail Three-Decker                  Lavery        
   Royal Sovereign        100     1701   1,883                                             3,100             Sail Three-Decker                  Lavery        
   Royal Anne             100     1703   1,722                                             2,900             Sail Three-Decker                  Lavery        
   London                 100     1706   1,685                                             2,800             Sail Three-Decker                  Lavery        
   Royal George           100     1715   1,801                                             3,000             Sail Three-Decker                  Lavery        
   Britannia              100     1719   1,895                                             3,100             Sail Three-Decker                  Lavery        
   Royal William          100     1719   1,918                                             3,200             Sail Three-Decker                  Lavery        
   Royal Sovereign        100     1728   1,883                                             3,100             Sail Three-Decker                  Lavery        
   Victory                100     1737   1,921                                             3,200             Sail Three-Decker                  Lavery        
   Royal George           100     1756   2,047                                             3,400             Sail Three-Decker                  Lavery        
   Britannia              100     1762   2,116                                             3,500             Sail Three-Decker                  Lavery        
   Victory                100     1765   2,142                                             3,600             Sail Three-Decker                  Lavery        
   Royal Sovereign        100     1786   2,175                                             3,600             Sail Three-Decker                  Lavery        
   Royal George           100     1788   2,286                                             3,800             Sail Three-Decker                  Lavery        
   Caledonia              120     1808   2,616                                             4,300             Sail Three-Decker                  Lavery        
   Ville de Paris         110     1795   2,351                                             3,900             Sail Three-Decker                  Lavery        
   Hibernia               110     1804   2,530                                             4,200             Sail Three-Decker                  Lavery        
   Queen Charlotte        100     1790   2,286                                             3,800             Sail Three-Decker                  Lavery        
   Nelson                 120     1814   2,617                                             4,300             Sail Three-Decker                  Lavery        
   St Vincent             120     1815   2,601                                             4,300             Sail Three-Decker                  Lavery        
   Howe                   120     1815   2,619                                             4,300             Sail Three-Decker                  Lavery        
   Britannia              120     1820   2,616                                             4,300             Sail Three-Decker                  Lavery        
   Prince Regent          120     1823   2,613                                             4,300             Sail Three-Decker                  Lavery        
   Queen Charlotte        104     1810   2,289                                             3,800             Sail Three-Decker                  Lavery        
   Princess Charlotte     104     1825   2,443                                             4,100             Sail Three-Decker                  Lavery        
   Royal Adelaide         104     1828   2,446                                             4,100             Sail Three-Decker                  Lavery        
   Royal George           120     1827   2,616                                             4,300             Sail Three-Decker                  Lavery        
   Neptune                120     1832   2,694                                             4,500             Sail Three-Decker                  Lavery        
   Royal William          120     1833   2,694                                             4,500             Sail Three-Decker                  Lavery        
   Waterloo               120     1833   2,694                                             4,500             Sail Three-Decker                  Lavery        
   St George              120     1840   2,694                                             4,500             Sail Three-Decker                  Lavery        
   Trafalgar              120     1841   2,694                                             4,500             Sail Three-Decker                  Lavery        
   Queen                  110     1839   3,104                                             5,100             Sail Three-Decker                  Lavery        
   Duke of Wellington     131     1852   3,759                                5,829        5,829 Steam Three-Decker (conversion from sail)      Lambert       
   Marlborough            131     1855   3,853                                6,065        6,065 Steam Three-Decker (conversion from sail)      Lambert       
   Royal Sovereign        131     1857   3,853                                6,065        6,065 Steam Three-Decker (conversion from sail)      Lambert       
   Prince of Wales        131     1860   3,853                                6,065        6,065 Steam Three-Decker (conversion from sail)      Lambert       
   Royal Albert           121     1854   3,726                                5,572        5,572 Steam Three-Decker (conversion from sail)      Lambert       
   Windsor Castle         102     1858   3,099                                             5,100 Steam Three-Decker (conversion from sail)      Lambert       
   Victoria               121     1859   4,116                                6,959        6,959             Steam Three-Decker                 Lambert       
   Howe                   121     1860   4,236                                             7,000             Steam Three-Decker                 Lambert       
   Saint Jean d'Acre      101     1853   3,200                                5,499        5,499              Steam Two-Decker                  Lambert       
   Conqueror              101     1855   3,224                                5,720        5,720              Steam Two-Decker                  Lambert       
   Donegal                101     1858   3,224                                5,720        5,720              Steam Two-Decker                  Lambert       
   Duncan                 101     1859   3,715                                5,950        5,950              Steam Two-Decker                  Lambert       
   Gibraltar              101     1860   3,715                                5,950        5,950              Steam Two-Decker                  Lambert       
   Warrior                 40     1860   6,039                                9,180        9,180             Iron-Clad Frigate              Lyon & Winfield   
   Black Prince            40     1861   6,039                                9,180        9,180             Iron-Clad Frigate              Lyon & Winfield   
   Achilles                26     1863   6,121                                9,820        9,820             Iron-Clad Frigate              Lyon & Winfield   
   Minotaur                36     1863   6,643                               10,690       10,690             Iron-Clad Frigate              Lyon & Winfield   
   Agincourt               36     1865   6,638                               10,600       10,600             Iron-Clad Frigate              Lyon & Winfield   
   Northumberland          36     1866   6,631                               10,784       10,784             Iron-Clad Frigate              Lyon & Winfield   
   Lord Clyde              24     1864   4,067                                7,750        7,750    Centre-Battery Iron-Clad Frigate       Lyon & Winfield   
   Lord Warden             16     1865   4,080                                7,842        7,842    Centre-Battery Iron-Clad Frigate       Lyon & Winfield   
   Bellerophon             15     1865   4,720                                7,551        7,551          Centre-Battery Iron-Clad          Lyon & Winfield   
   Hercules                14     1868   5,234                                8,830        8,830          Centre-Battery Iron-Clad          Lyon & Winfield   
   Monarch                  7     1868   5,102                                8,322        8,322             Masted Turret Ship             Lyon & Winfield   
   Captain                  6     1869   4,272                                7,767        7,767             Masted Turret Ship             Lyon & Winfield   
   Sultan                  12     1870   5,234                                9,540        9,540          Centre-Battery Iron-Clad          Lyon & Winfield   
   Devastation              4     1871   4,407                                9,390        9,390            Mastless Turret Ship            Lyon & Winfield   
   Thunderer                4     1872                                        9,390        9,390            Mastless Turret Ship            Lyon & Winfield   
   Alexandra               12     1875                                        9,490        9,490          Centre-Battery Iron-Clad          Lyon & Winfield   
   Dreadnought              4     1875                                       10,820       10,820            Mastless Turret Ship            Lyon & Winfield   
   Temeraire                8     1876                                        8,571        8,571          Centre-Battery Iron-Clad          Lyon & Winfield   
   Inflexible               4     1876                                       11,880       11,880        Central Citadel Turret Ship         Lyon & Winfield   
"""

s2x, s2y, s3x, s3y, t3x, t3y, ix, iy, lx, ly = [], [], [], [], [], [], [], [], [], []

for l in data.splitlines():
    if len(l) < 5:
        continue
    n = l[:26].strip()
    y = int(l[33:39])
    try:
        t = int(l[39:47].replace(",", ""))
    except:
        continue
    if "Steam Two-Decker" in l:
        s2x.append(y)
        s2y.append(t)
    elif "Steam Three-Decker" in l:
        s3x.append(y)
        s3y.append(t)
    elif "Sail Three-Decker" in l:
        t3x.append(y)
        t3y.append(t)
    elif "igate" in l:
        ix.append(y)
        iy.append(t)
    else:
        lx.append(y)
        ly.append(t)

ll = 0.7
scatter(t3x, t3y, c="b", marker="o", lw=ll, label="Sail 3-Deckers")
scatter(s3x, s3y, c="orange", marker="o", lw=ll, label="Steam 3-Deckers")
scatter(s2x, s2y, c="r", marker="o", lw=ll, label="Steam 2-Deckers")
scatter(ix, iy, c="g", marker="o", lw=ll, label="Iron-clad Frigates")
scatter(lx, ly, c="cyan", marker="o", lw=ll, label="Later Iron-clads")

legend(loc="upper left")
ylim(0, 7000)
xlim(1630, 1875)
xticks(range(1630, 1930, 50))
xlabel("Year launched")
ylabel("Tonnage (BOM)")
grid(True, ls="-", c="#a0a0a0")

plt.show()

print("------------------------------------------------------------")  # 60個

#          編號                      圖像大小[英吋]     解析度    背景色                    邊框顏色                         邊框有無
plt.figure(
    num="scatter 集合 4",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)


# 第二張圖
plt.subplot(232)

print("繪製散布圖")

filename = "_data/python_ReadWrite_CSV6_score.csv"

# 讀入資料
dat = pd.read_csv(filename, encoding="UTF-8")

# 散布圖
plt.scatter(dat["數學"], dat["理科"])
plt.axis("equal")


# 共變異數與相關係數
correlation = np.corrcoef(dat["數學"], dat["理科"])  # 計算相關係數
correlation[0, 1]  # 顯示在畫面


# 第三張圖
plt.subplot(233)


# 第四張圖
plt.subplot(234)


# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)


plt.show()


print("------------------------------------------------------------")  # 60個

#          編號                      圖像大小[英吋]     解析度    背景色                    邊框顏色                         邊框有無
plt.figure(
    num="scatter 集合 5",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

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

# 第二張圖
plt.subplot(232)


# 第三張圖
plt.subplot(233)


# 第四張圖
plt.subplot(234)


# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)


plt.show()


print("------------------------------------------------------------")  # 60個

#          編號                      圖像大小[英吋]     解析度    背景色                    邊框顏色                         邊框有無
plt.figure(
    num="scatter 集合 6",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

"""
額外設定 s、c 和 cmap，就能根據資料點的數據，對應出指定的顏色，
假設資料的範圍是 0～100，顏色地圖是紅橙黃綠藍，
則 0～20 對應紅色，21～40 對應橙色，
41～60 對應黃色，61～80 對應綠色，81～100 對應藍色。
"""

x = range(1, 11)  # 1 2 3 ... 10
y = range(1, 11)  # 1 2 3 ... 10
X, Y = np.meshgrid(x, y)
size = [i * 80 for i in Y]  # 放大資料點數據 N 倍，比較容易觀察尺寸
plt.scatter(X, Y, s=size, c=size, cmap="Set1")  # 使用 Set1 的 colormap
plt.colorbar()


# 第二張圖
plt.subplot(232)

# 加上 vmin 和 vmax 的設定，能設定顏色的最大值與最小值
# 當數值小於 vmin 時，只會顯示紅色，當數值大於 vmax 時，只會顯示灰色。

x = range(1, 11)  # 1 2 3 ... 10
y = range(1, 11)  # 1 2 3 ... 10
X, Y = np.meshgrid(x, y)
size = [i * 80 for i in Y]  # 放大資料點數據 N 倍，比較容易觀察尺寸
plt.scatter(X, Y, s=size, c=size, cmap="Set1", vmin=200, vmax=650)
plt.colorbar()


# 第三張圖
plt.subplot(233)


# 第四張圖
plt.subplot(234)

listx = [31, 15, 20, 25, 12, 18, 45, 21, 33, 5, 18, 22, 37, 42, 10]
listy = [68, 20, 61, 32, 45, 56, 10, 18, 70, 64, 43, 66, 19, 77, 21]

scale = [x**3 for x in [5, 4, 2, 6, 7, 1, 8, 9, 2, 3, 2, 4, 5, 7, 2]]

plt.xlim(0, 50)
plt.ylim(0, 80)

plt.scatter(listx, listy, c="r", s=scale, marker="o", alpha=0.5)

# 第五張圖
plt.subplot(235)

x = np.linspace(0, 5, 50)  # 建立含50個元素的陣列
y = x  # y陣列的變化
plt.scatter(x, y, s=50, c=y, cmap="hsv")  # 色彩隨y軸值變化
plt.colorbar()  # 色彩條


# 第六張圖
plt.subplot(236)

x = np.linspace(0, 5, 50)  # 含50個元素的陣列
y = x  # y陣列的變化
plt.scatter(x, y, s=50, c=y, cmap="rainbow")  # 色彩隨 y 軸值變化
plt.colorbar()  # 色彩條

plt.show()

print("------------------------------------------------------------")  # 60個

#          編號                      圖像大小[英吋]     解析度    背景色                    邊框顏色                         邊框有無
plt.figure(
    num="scatter 集合 7",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

x = np.arange(50)
y = np.arange(50)
plt.scatter(x, y, c=y, cmap="rainbow")


# 第二張圖
plt.subplot(232)


# 第三張圖
plt.subplot(233)


# 第四張圖
plt.subplot(234)

# x，y，大小，顏色
plt.scatter([1, 2, 3, 4], [2, 4, 6, 8], [10, 20, 30, 400], ["r", "b", "y", "k"])
plt.scatter([1, 2, 3, 4], [9, 8, 7, 6], s=10, c="b", marker="v")


# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)
radius = 10
degrees = [x * 15 for x in range(0, 25)]
print(degrees)
x = [radius * math.cos(math.radians(d)) for d in degrees]
y = [radius * math.sin(math.radians(d)) for d in degrees]

plt.scatter(x, y)
plt.xlim(-12, 12)
plt.ylim(-12, 12)
# plt.axis('equal')
plt.show()

sys.exit()

print("------------------------------------------------------------")  # 60個

#          編號                      圖像大小[英吋]     解析度    背景色                    邊框顏色                         邊框有無
plt.figure(
    num="scatter 集合 8",
    figsize=(20, 15),
    dpi=84,
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


# 第六張圖
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個

#          編號                      圖像大小[英吋]     解析度    背景色                    邊框顏色                         邊框有無
plt.figure(
    num="scatter 集合 9",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

"""
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
"""

# 第一張圖
plt.subplot(231)

np.random.seed(0)
x = np.random.rand(20)
y = np.random.rand(20)

area = (50 * np.random.rand(20)) ** 2

plt.scatter(x, y, s=area, alpha=0.5)


# 第二張圖
plt.subplot(232)

# 把c參數改成隨機數組。

np.random.seed(0)
x = np.random.rand(20)
y = np.random.rand(20)

colors = np.random.rand(20)
area = (50 * np.random.rand(20)) ** 2

plt.scatter(x, y, s=area, c=colors, alpha=0.5)


# 第三張圖
plt.subplot(233)

# 把maker參數改成x的樣本。

np.random.seed(0)
x = np.random.rand(20)
y = np.random.rand(20)

colors = np.random.rand(20)
area = (50 * np.random.rand(20)) ** 2

plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker="x")


# 第四張圖
plt.subplot(234)

# 修改其中的linewidth參數的大小，但是沒什么不同，**注意：**只有marker為封閉的圖案的時候，這個參數才有效。

np.random.seed(0)
x = np.random.rand(20)
y = np.random.rand(20)

colors = np.random.rand(20)
area = (50 * np.random.rand(20)) ** 2

lines = np.zeros(220) + 5

plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker="x", linewidths=lines)


# 第五張圖
plt.subplot(235)

# 把s參數改成200。

np.random.seed(0)
x = np.random.rand(20)
y = np.random.rand(20)

colors = np.random.rand(20)
plt.scatter(x, y, s=200, c=colors, alpha=0.5)

# 第六張圖
plt.subplot(236)

# 把linewidths參數改成數組。

np.random.seed(0)
x = np.random.rand(20)
y = np.random.rand(20)

lines = np.zeros(220) + 5
plt.scatter(x, y, s=200, c="b", alpha=0.5, linewidths=lines)
# 再把alpha改成1

plt.show()


print("------------------------------------------------------------")  # 60個

#          編號                      圖像大小[英吋]     解析度    背景色                    邊框顏色                         邊框有無
plt.figure(
    num="scatter 集合 10",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

"""
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

"""

# 第一張圖
plt.subplot(231)


plt.scatter(x, y)

# 第二張圖
plt.subplot(232)

# 第三張圖
plt.subplot(233)

# numpy.random.RandomState的用法

rng = np.random.RandomState(0)

x = rng.randn(50)  # 隨機產生50個X軸坐標
y = rng.randn(50)  # 隨機產生50個Y軸坐標

colors = rng.rand(50)  # 隨機產生50個用于顏色映射的數值
sizes = 700 * rng.rand(50)  # 隨機產生50個用于改變散點面積的數值

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap="viridis")


# 這里從cmap中選取了一個叫做'viridis'的調色盤，
# 其作用是，將參數c中獲取到的數值，映射到“色盤”中已經對應好的顏色上

# 并且上圖中從“色盤”viridis中獲取到的顏色，
# 可以通過plt.colorbar( )顯示為顏色條（與熱力圖同理）。

# 第四張圖
plt.subplot(234)

rng = np.random.RandomState(0)

x = rng.randn(50)  # 隨機產生50個X軸坐標
y = rng.randn(50)  # 隨機產生50個Y軸坐標

colors = rng.rand(50)  # 隨機產生50個用于顏色映射的數值
sizes = 700 * rng.rand(50)  # 隨機產生50個用于改變散點面積的數值

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap="viridis")
plt.colorbar()  # 顯示顏色條


# 第五張圖
plt.subplot(235)

from matplotlib import colors  # 注意！為了調整“色盤”，需要導入colors

rng = np.random.RandomState(0)
x = rng.randn(50)
y = rng.randn(50)
color = rng.rand(50)
sizes = 700 * rng.rand(50)

changecolor = colors.Normalize(vmin=0.4, vmax=0.8)

plt.scatter(x, y, c=color, s=sizes, alpha=0.3, cmap="viridis", norm=changecolor)
plt.colorbar()

# 第六張圖
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個

#          編號                      圖像大小[英吋]     解析度    背景色                    邊框顏色                         邊框有無
plt.figure(
    num="scatter 集合 11",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

"""
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

# 第一張圖
plt.subplot(231)

np.random.seed(100)

x = np.arange(0.0, 50.0, 1.0)  # 生成一個0到50的序列
y = x**1.3 + np.random.rand(*x.shape) * 30.0  # y = x ^ 1.3 + 隨機值 * 30

plt.scatter(x, y, alpha=0.9, label="rand")
plt.legend(loc="best")  # 添加圖例


# 第二張圖
plt.subplot(232)

np.random.seed(500)

N = 50  # 數據點總數
x = np.random.rand(N)  # x 軸數據
y = np.random.rand(N)  # y 軸數據
colors = np.random.rand(N)  # 顏色

area = np.pi * (15 * np.random.rand(N)) ** 2  # 每個點對應的面積大小，（即氣泡大小，這里可以放入第3個屬性數據）

plt.scatter(x, y, s=area, c=colors, alpha=0.5)

# 第三張圖
plt.subplot(233)


# 第四張圖
plt.subplot(234)


# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個

#          編號                      圖像大小[英吋]     解析度    背景色                    邊框顏色                         邊框有無
plt.figure(
    num="scatter 集合 12",
    figsize=(20, 15),
    dpi=84,
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


# 第六張圖
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個

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

plt.scatter(x, y1, s = s1, c = 'b', alpha = 0.5)   # 設定透明度為 0.5
plt.scatter(x, y2, s = s2, c = 'r', alpha = 0.5)   # 設定透明度為 0.5



----
#連接2點的直線

import matplotlib.pyplot as plt
import numpy as np

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
