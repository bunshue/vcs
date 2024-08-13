"""
scatter 集合
散布圖 Scatter Chart
散點圖

"""

N = 500

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

plt.figure(
    num="scatter 集合 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

R = 10
degrees = [x * 15 for x in range(0, 25)]
print(degrees)
x = [R * math.cos(math.radians(d)) for d in degrees]
y = [R * math.sin(math.radians(d)) for d in degrees]
plt.scatter(x, y)


# 第二張圖
plt.subplot(232)

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
#print(len(X))

plt.scatter(X, Y)

plt.axis([0, 10, 0, 10])
plt.axis("equal")
plt.title('蒙地卡羅模擬')

# 第三張圖
plt.subplot(233)

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

"""
現在第一群的點是第 0 類, 第二群是第 1 類, 第三群是第 2 類，所以我們要做個像這樣
[0, 0, ..., 0, 1, 1, ..., 1, 2, 2, ..., 2] 的標記。
"""

c = np.repeat([0, 1, 2], N)

plt.scatter(x, y, c=c, cmap="Set1")
plt.scatter([cx0, cx1, cx2], [cy0, cy1, cy2], [200, 200, 200], ["r", "g", "b"])

plt.title("三群數據")

# 第四張圖
plt.subplot(234)

N = 30
degrees = np.arange(0, 360, N)
x = np.cos(np.radians(degrees))
y = np.sin(np.radians(degrees))

#plt.plot(x, y)
plt.scatter(x, y)



# 第五張圖
plt.subplot(235)

N = 20
x = np.random.randint(1, 11, N)  # 建立 x
y = np.random.randint(1, 11, N)  # 建立 y
colors = np.random.rand(N)  # 色彩數列
size = (30 * np.random.rand(N)) ** 2  # 散點大小數列

plt.scatter(x, y, s=size, c=colors)
plt.xticks(np.arange(0, 12, step=1.0))
plt.yticks(np.arange(0, 12, step=1.0))


# 第六張圖
plt.subplot(236)

N = 30
colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
colors = []  # 建立色彩數列
for i in range(N):  # 隨機設定顏色
    colors.append(np.random.choice(colorused))

x = np.random.randint(1, 11, N)  # 建立 x
y = np.random.randint(1, 11, N)  # 建立 y
size = (N * np.random.rand(N)) ** 2  # 散點大小數列
plt.scatter(x, y, s=size, c=colors)  # 繪製散點

plt.xticks(np.arange(0, 12, step=1.0))  # x 軸刻度
plt.yticks(np.arange(0, 12, step=1.0))  # y 軸刻度


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

# 第一張圖
plt.subplot(231)

# 使用隨機陣列產生圖像
x = np.random.rand(10000)  # N個0~1之間的亂數
y = np.random.rand(10000)
plt.scatter(x, y, c=y, cmap="hsv")  # 色彩依 y 軸值變化
#plt.colorbar()

# 第二張圖
plt.subplot(232)


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

# 第三張圖
plt.subplot(233)


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


# 第四張圖
plt.subplot(234)

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
xticks(range(1630, 1930, 50))
xlabel("Year launched")
ylabel("Tonnage (BOM)")
grid(True, ls="-", c="#a0a0a0")


# 第五張圖
plt.subplot(235)

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
#plt.colorbar()


# 第六張圖
plt.subplot(236)

# 加上 vmin 和 vmax 的設定，能設定顏色的最大值與最小值
# 當數值小於 vmin 時，只會顯示紅色，當數值大於 vmax 時，只會顯示灰色。

x = range(1, 11)  # 1 2 3 ... 10
y = range(1, 11)  # 1 2 3 ... 10
X, Y = np.meshgrid(x, y)

size = [i * 80 for i in Y]  # 放大資料點數據 N 倍，比較容易觀察尺寸

plt.scatter(X, Y, s=size, c=size, cmap="Set1", vmin=200, vmax=650)
#plt.colorbar()

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

# 第一張圖
plt.subplot(231)

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
plt.xticks(np.arange(0, 1.1, step=0.1))
plt.yticks(np.arange(0, 1.1, step=0.1))

# 第二張圖
plt.subplot(232)

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
plt.xticks(np.arange(0, 1.1, step=0.1))
plt.yticks(np.arange(0, 1.1, step=0.1))

# 第三張圖
plt.subplot(233)


# 第四張圖
plt.subplot(234)

x = np.random.rand(20)
y = np.random.rand(20)
size = (50 * np.random.rand(20)) ** 2
plt.scatter(x, y, s=size, alpha=0.5)


# 第五張圖
plt.subplot(235)

# 把c參數改成隨機數組。
x = np.random.rand(20)
y = np.random.rand(20)

colors = np.random.rand(20)
size = (50 * np.random.rand(20)) ** 2

plt.scatter(x, y, s=size, c=colors, alpha=0.5)

# 第六張圖
plt.subplot(236)

# 把s參數改成200。
x = np.random.rand(20)
y = np.random.rand(20)

colors = np.random.rand(20)
plt.scatter(x, y, s=200, c=colors, alpha=0.5)


plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="scatter 集合 4",
    figsize=(12, 8),
    dpi=100,
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

# 把maker參數改成x的樣本。
x = np.random.rand(20)
y = np.random.rand(20)

colors = np.random.rand(20)
size = (50 * np.random.rand(20)) ** 2

# plt.scatter(x, y, s=size, c=colors, alpha=0.5, marker="x")
plt.scatter(x, y, s=size, c=colors, alpha=0.5)


# 第二張圖
plt.subplot(232)

# 修改其中的linewidth參數的大小，但是沒什么不同，**注意：**只有marker為封閉的圖案的時候，這個參數才有效。
x = np.random.rand(20)
y = np.random.rand(20)

colors = np.random.rand(20)
size = (50 * np.random.rand(20)) ** 2

lines = np.zeros(220) + 5

# plt.scatter(x, y, s=size, c=colors, alpha=0.5, marker="x", linewidths=lines)
plt.scatter(x, y, s=size, c=colors, alpha=0.5, linewidths=lines)


# 第三張圖
plt.subplot(233)

# 把linewidths參數改成數組。
x = np.random.rand(20)
y = np.random.rand(20)

lines = np.zeros(220) + 5
plt.scatter(x, y, s=200, c="b", alpha=0.5, linewidths=lines)
# 再把alpha改成1


# 第四張圖
plt.subplot(234)

# np.random.randint(0, 3, 10)
x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
X, Y = np.meshgrid(x, y)

plt.scatter(
    X.ravel(),
    Y.ravel(),
    c=[0, 1, 2, 1, 1, 2, 1, 1, 0, 1, 1, 0, 0, 0, 2, 1],
    cmap="Paired",
)


# 第五張圖
plt.subplot(235)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)  # 點的顏色
size = (30 * np.random.rand(N)) ** 2  # 點的半徑
plt.scatter(x, y, s=size, c=colors, alpha=0.5)  # 由於點可能疊加，設置透明度爲0.5

# 第六張圖
plt.subplot(236)

N = 30
x = np.random.randint(1, 11, N)  # 建立 x
y = np.random.randint(1, 11, N)  # 建立 y
colors = np.random.rand(N)  # 色彩數列

plt.scatter(x, y, c=colors)
plt.xticks(np.arange(0, 11, step=1.0))
plt.yticks(np.arange(0, 11, step=1.0))

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="scatter 集合 5",
    figsize=(12, 8),
    dpi=100,
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


# 第二張圖
plt.subplot(232)

rng = np.random.RandomState(0)

x = rng.randn(50)  # 隨機產生50個X軸坐標
y = rng.randn(50)  # 隨機產生50個Y軸坐標

colors = rng.rand(50)  # 隨機產生50個用于顏色映射的數值
sizes = 700 * rng.rand(50)  # 隨機產生50個用于改變散點面積的數值

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap="viridis")
#plt.colorbar()

# 第三張圖
plt.subplot(233)

from matplotlib import colors  # 為了調整“色盤”，需要導入colors

rng = np.random.RandomState(0)
x = rng.randn(50)
y = rng.randn(50)
color = rng.rand(50)
sizes = 700 * rng.rand(50)

changecolor = colors.Normalize(vmin=0.4, vmax=0.8)

plt.scatter(x, y, c=color, s=sizes, alpha=0.3, cmap="viridis", norm=changecolor)
#plt.colorbar()

# 第四張圖
plt.subplot(234)

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

# 第五張圖
plt.subplot(235)

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


# 第六張圖
plt.subplot(236)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
plt.scatter(x, y, s=300, c=colors, alpha=0.5)


plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("scatter參數大合集")

plt.figure(figsize=(12, 8))

x = np.random.randn(N)
y = np.random.randn(N)

plt.scatter(x, y)
# plt.scatter(x, y, marker="^", color="red") # 指名marker和顏色
# plt.scatter(x, y, s=30)# 設定資料點的大小
plt.scatter(x, y, c="r", s=100)  # 指定顏色與大小

# 給散佈圖的點套上不同深淺顏色
# c = np.random.choice(np.arange(100), 100)
# plt.scatter(x, y, s=c, c=c, cmap="viridis")

""" 各種scatter的語法
plt.scatter(x, y, alpha=0.3)
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

""" TBD
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
"""
print("------------------------------------------------------------")  # 60個


""" TBD
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
"""
print("------------------------------------------------------------")  # 60個

print("散佈圖")

fig, ax = plt.subplots()

N = 50
x = np.random.randint(30, size=N)
y = np.random.randint(30, size=N)
c = np.random.randint(30, size=N)
size = np.random.randint(10, size=N) * 400

sc = ax.scatter(x=x, y=y, c=c, s=c, alpha=0.5, label="scatter plot")

ax.set_xlabel("X軸", loc="left")
ax.set_ylabel("Y軸", loc="top")
ax.legend(loc=1)
cbar = fig.colorbar(sc)
cbar.set_label("Z軸", loc="center")

plt.show()

print("------------------------------------------------------------")  # 60個

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

plt.scatter(X, Y, s=75, c=T, alpha=0.5)

plt.xlim(-3.5, 3.5)
plt.ylim(-3.5, 3.5)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

""" TBD
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
"""
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

plt.scatter(x, y1, s = s1, c = 'b', alpha = 0.5)   # 設定透明度為 0.5
plt.scatter(x, y2, s = s2, c = 'r', alpha = 0.5)   # 設定透明度為 0.5



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

np.random.seed(10)  # 固定隨機數


"""


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

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


# x，y，大小，顏色
plt.scatter([1, 2, 3, 4], [2, 4, 6, 8], [10, 20, 30, 400], ["r", "b", "y", "k"])
plt.scatter([1, 2, 3, 4], [9, 8, 7, 6], s=10, c="b", marker="v")

s = plt.scatter([1, 2, 3], [4, 5, 6])

plt.scatter(x, g, c="blue", marker=".")
plt.scatter(x, y, color="lightgreen", edgecolor="b", s=60)

plt.scatter(x, y, c=y, cmap="rainbow")
plt.scatter(x, y, s=50, c=y, cmap="hsv")  # 色彩隨y軸值變化
#plt.colorbar()

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


x = np.linspace(0, 5, 50)  # 含50個元素的陣列

plt.scatter(x, y, s=50, c=y, cmap="rainbow")  # 色彩隨 y 軸值變化
#plt.colorbar()

print("------------------------------------------------------------")  # 60個

plt.scatter(x, y, s=N, c=x, cmap="brg")  # 繪製散點圖


colors = np.array(["b", "c", "g", "k", "m", "r", "y", "pink", "purple", "orange"])
plt.scatter(x, y1, c=colors, label="圓形標記")
plt.scatter(x, y2, c=colors, marker="*", label="星形標記")
plt.xticks(np.arange(0, 11, step=1.0))
plt.yticks(np.arange(0, 11, step=1.0))


N = 50  # 色彩數列的點數

colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色

colors = []  # 建立色彩數列
for i in range(N):  # 隨機設定顏色
    colors.append(np.random.choice(colorused))

plt.scatter(x, y1, c=colors, marker="*")  # 繪製 sine
plt.scatter(x, y2, c=colors, marker="s")  # 繪製 cos


plt.scatter(x, y1, c="b", marker="x")  # 繪製 sine wave
plt.scatter(x, y2, c="g", marker="X")  # 繪製 cos wave

plt.scatter(x, y1, c=colors, marker="*")  # 繪製 sine
plt.scatter(x, y2, c=colors, marker="s")  # 繪製 cos

colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
x = np.linspace(0.0, 2 * np.pi, 50)  # 建立 50 個點


colors = []
for i in range(50):  # 隨機設定顏色
    colors.append(np.random.choice(colorused))


x = np.linspace(0, 1, 1000)
y = 0.5 * np.sin(n * x) + 0.5

plt.scatter(listx, listy, c="r", s=scale, marker="o", alpha=0.5)

plt.axis("off")  # 隱藏座標
plt.axis("off")  # 隱藏座標


N = 50  # 色彩數列的點數
colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
colors = []  # 建立色彩數列
for i in range(N):  # 隨機設定顏色
    colors.append(np.random.choice(colorused))

x = np.linspace(0.0, 2 * np.pi, N)  # 建立 50 個點

#方塊
plt.scatter(x, y1, c=colors, marker="*")  # 繪製 sine
#星形
plt.scatter(x, y2, c=colors, marker="s")  # 繪製 cos


x = np.linspace(0, 5, 500)  # 含500個元素的陣列
y = np.linspace(0, 5, 500)  # 含500個元素的陣列

plt.scatter(x, y, s=50, c=x, cmap="rainbow")  # 色彩隨 x 軸值變化
plt.scatter(x, y, s=50, c=y, cmap="rainbow")  # 色彩隨 y 軸值變化

#plt.colorbar()
plt.show()


x = np.random.rand(10)
y = np.random.rand(10)
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

