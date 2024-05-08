# 新進測試01

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

plt.figure(
    num="新進測試 01",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

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


# 第二張圖
plt.subplot(232)

d01 = [10 for y in range(1, 9)]  # data1線條之y值
d02 = [20 for y in range(1, 9)]  # data2線條之y值
d03 = [30 for y in range(1, 9)]  # data3線條之y值
d04 = [40 for y in range(1, 9)]  # data4線條之y值
d05 = [50 for y in range(1, 9)]  # data5線條之y值
d06 = [60 for y in range(1, 9)]  # data6線條之y值
d07 = [70 for y in range(1, 9)]  # data7線條之y值
d08 = [80 for y in range(1, 9)]  # data8線條之y值
d09 = [90 for y in range(1, 9)]  # data9線條之y值
d10 = [100 for y in range(1, 9)]  # data10線條之y值
d11 = [110 for y in range(1, 9)]  # data11線條之y值
d12 = [120 for y in range(1, 9)]  # data12線條之y值

x = [1, 2, 3, 4, 5, 6, 7, 8]
plt.plot(x, d01, "-1")
plt.plot(x, d02, "-2")
plt.plot(x, d03, "-3")
plt.plot(x, d04, "-4")
plt.plot(x, d05, "-s")
plt.plot(x, d06, "-p")
plt.plot(x, d07, "-*")
plt.plot(x, d08, "-+")
plt.plot(x, d09, "-D")
plt.plot(x, d10, "-d")
plt.plot(x, d11, "-H")
plt.plot(x, d12, "-h")
plt.title("標記符號")


# 第三張圖
plt.subplot(233)

x1 = np.linspace(0.1, 10, 99)  # 建立含30個元素的陣列
x2 = np.linspace(0.1, 10, 99)  # 建立含30個元素的陣列
y1 = [math.log2(x) for x in x1]
y2 = [math.log(x, 0.5) for x in x2]

plt.plot(x1, y1, label="基底 = 2")
plt.plot(x2, y2, label="基底 = 0.5")

plt.axis([0, 10, -5, 5])
plt.legend(loc="best")  # 建立圖例


# 第四張圖
plt.subplot(234)


# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)

plt.show()

print("------------------------------------------------------------")  # 60個

print(
    "matplotlib 01 ------------------------------------------------------------"
)  # 60個

"""
python用mpl_finance中的candlestick_ohlc畫分時圖

matplotlib.finance獨立出來成爲mpl_finance，而mpl_finance中的candlestick_ochl和candlestick_ohlc一般用來畫股票的K線圖。我需要分析分時圖，也就是一分鐘的行情，這個時候就不能直接用candlestick_ochl函數，因爲candlestick_ochl中x軸最小的單位是日期，不是分鐘。

經過對mpl_finance的源代碼進行分析，問題在於matplotlib的date2num將日期轉換爲浮點數，浮點數的整數部分表示日期，小數部分代表小時和分鐘。比如下面4個時間段是連續的分鐘。
時間 	date2num之後 	乘以1440
2018/09/17-21:34 	736954.8986 	1061215054
2018/09/17-21:35 	736954.8993 	1061215055
2018/09/17-21:36 	736954.9000 	1061215056
2018/09/17-21:37 	736954.9007 	1061215057

可以看出date2num函數計算之後，4個時間的整數部分都是736954，導致在X軸上這4個時間段都重疊在一起，無法區分了。要達到的效果是每一個分鐘也能成爲一個整數，這樣就可以顯示出來了。那麼一天是24小時，每小時60分鐘，那麼一天就是1440分鐘，將date2num計算的浮點數乘以1440就可以將每一分鐘轉爲整數，那麼就可以在x軸上。

最後還需要對x軸格式化，因爲自己對x軸進行了處理（乘以1440），採用默認的格式化是亂碼。需要自定義x軸的格式化函數。

pip install mpl_finance
pip install --upgrade mplfinance

"""

from pandas import DataFrame
import matplotlib.dates as dates
import mplfinance as mpf
from matplotlib.ticker import Formatter
from mplfinance.original_flavor import candlestick_ohlc

dfcvs = DataFrame(
    [
        #    時間            開盤, 最高 ,最低, 收盤
        ["2018/09/17-21:34", 3646, 3650, 3644, 3650],
        ["2018/09/17-21:35", 3650, 3650, 3648, 3648],
        ["2018/09/17-21:36", 3650, 3650, 3648, 3650],
        ["2018/09/17-21:37", 3652, 3654, 3648, 3652],
    ]
)

dfcvs.columns = ["時間", "開盤", "最高", "最低", "收盤"]
dfcvs["時間"] = pd.to_datetime(dfcvs["時間"], format="%Y/%m/%d-%H:%M")

# matplotlib的date2num將日期轉換爲浮點數，整數部分區分日期，小數區分小時和分鐘
# 因爲小數太小了，需要將小時和分鐘變成整數，需要乘以24（小時）×60（分鐘）= 1440，這樣小時和分鐘也能成爲整數
# 這樣就可以一分鐘就佔一個位置

dfcvs["時間"] = dfcvs["時間"].apply(lambda x: dates.date2num(x) * 1440)
data_mat = dfcvs.values

fig, ax = plt.subplots(figsize=(10, 6))

fig.subplots_adjust(bottom=0.1)
candlestick_ohlc(
    ax, data_mat, colordown="#53c156", colorup="#ff1717", width=0.2, alpha=1
)


# 將x軸的浮點數格式化成日期小時分鐘
# 默認的x軸格式化是日期被dates.date2num之後的浮點數，因爲在上面乘以了1440，所以默認是錯誤的
# 只能自己將浮點數格式化爲日期時間分鐘
# 參考https://matplotlib.org/examples/pylab_examples/date_index_formatter.html
class MyFormatter(Formatter):
    def __init__(self, dates, fmt="%Y%m%d %H:%M"):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        "Return the label for time x at position pos"
        ind = int(np.round(x))
        # ind就是x軸的刻度數值，不是日期的下標

        return dates.num2date(ind / 1440).strftime(self.fmt)


formatter = MyFormatter(data_mat[:, 0])
ax.xaxis.set_major_formatter(formatter)

for label in ax.get_xticklabels():
    label.set_rotation(90)
    label.set_horizontalalignment("right")

plt.show()

print(
    "matplotlib 02 ------------------------------------------------------------"
)  # 60個

# 加載取數與繪圖所需的函數包
import datetime
from hs_udata import set_token, stock_quote_daily
import matplotlib as mpl
import matplotlib.dates as mdates

# from mplfinance import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc

data_price = [1, 2, 3, 4, 5]

# 繪製圖片
fig = plt.figure(
    num="matplotlib 02",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

grid = plt.GridSpec(12, 10, wspace=0.5, hspace=0.5)

ax1 = fig.add_subplot(grid[0:8, 0:12])  # 設置K線圖的尺寸

# candlestick_ohlc(ax1, ohlc.values.tolist(), width = 0.7, colorup = 'red', colordown = 'green')

# （2）繪制均線
# ax1.plot(range(len(data_price)), data_price, color = 'red', lw = 2, label = 'MA (5)')

# 設置標注
plt.title("test", fontsize=14)  # 設置圖片標題
plt.ylabel("價 格（元）", fontsize=14)  # 設置縱軸標題
# plt.legend(loc = 'best')                    # 繪制圖例
ax1.set_xticks([])  # 日期標注在成交量中，故清空此處x軸刻度
ax1.set_xticklabels([])  # 日期標注在成交量中，故清空此處x軸

# （3）繪制成交量
# 成交量數據

data_volume = [3, 2, 1, 4, 6]
# 繪制成交量
ax2 = fig.add_subplot(grid[8:10, 0:12])  # 設置成交量圖形尺寸
# ax2.bar(data_volume, color = 'r')                    # 繪制紅色柱狀圖
# ax2.bar(data_volume, color = 'g')                    # 繪制綠色柱狀圖
plt.xticks(rotation=30)
plt.xlabel("日 期", fontsize=14)  # 設置橫軸標題
# 修改橫軸日期標注
date_list = [1, 2, 3, 4, 5]  # ohlc.index.tolist()           # 獲取日期列表
xticks_len = round(len(date_list) / (len(ax2.get_xticks()) - 1))  # 獲取默認橫軸標注的間隔
xticks_num = range(0, len(date_list), xticks_len)  # 生成橫軸標注位置列表
xticks_str = list(map(lambda x: date_list[int(x)], xticks_num))  # 生成正在標注日期列表
ax2.set_xticks(xticks_num)  # 設置橫軸標注位置
ax2.set_xticklabels(xticks_str)  # 設置橫軸標注日期

plt.show()

print(
    "matplotlib 03 ------------------------------------------------------------"
)  # 60個

foldername = "C:/_git/vcs/_1.data/______test_files1"

"""
import glob
import cv2

files = glob.glob(foldername + "/*.jpg")  #建立測試資料
test_feature=[]
for file in files:
    print(file)
    img = cv2.imread(file)	#讀取本機圖片
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #灰階    
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV) #轉為反相黑白 
    test_feature.append(img)

print(test_feature)

print('畫多張圖')


plt.gcf().set_size_inches(12, 14)

num=25

if num>25: num=25
for i in range(num):
    ax=plt.subplot(5,5, i+1)
    #ax.imshow(images[start_id], cmap='binary')  #顯示黑白圖片
    title = 'label = ' + str(i)
    ax.set_title(title,fontsize=12)  # X,Y軸不顯示刻度
    ax.set_xticks([]);ax.set_yticks([])        
plt.show()


"""

print(
    "matplotlib 04 ------------------------------------------------------------"
)  # 60個

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

plt.show()

print(
    "matplotlib 05 ------------------------------------------------------------"
)  # 60個

# 建立一個新的 figure
# fig1 = plt.figure()

# 增新一個axes（座標軸），以供繪圖和放置資訊:
# axs = fig1.add_subplot(1,1,1) # 1x1的座標軸

# 增新很多個axes，以供繪圖和放置資訊:
# fig1.delaxes( fig1.gca() ) # 順便示範，把剛剛1x1的座標軸刪掉

fig2 = plt.figure(
    num="matplotlib 05",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 一般的情況下，axes是"hold on"的, 也就是資料不會被覆蓋掉。
# hold on: 好處是一次要輸出一堆函數，可以把圖疊加上去。
# hold off: 可以更新圖的內容，可是全部的資訊會被洗掉（title, legend等）
# 如果要保留這些資訊，可以單獨抓出圖的內容，直接修改：
x = np.linspace(0, 6.28, 100)
y = np.sin(x)

axes = fig2.add_subplot(1, 3, 1)
axes.set_title("y = sin(x)")
(line,) = axes.plot(x, y)  # 這裡回傳的line就是畫在圖上的資料
# 當發現畫錯想修改，可以對line修改：
line.set_ydata(np.cos(x))

axes = fig2.add_subplot(1, 3, 2)
axes.set_title("y = sin(x)")
(line,) = axes.plot(x, y)  # 這裡回傳的line就是畫在圖上的資料
# 當發現畫錯想修改，可以對line修改：
line.set_ydata(np.cos(x))

axes = fig2.add_subplot(1, 3, 3)
axes.set_title("y = sin(x)")
(line,) = axes.plot(x, y)  # 這裡回傳的line就是畫在圖上的資料
# 當發現畫錯想修改，可以對line修改：
line.set_ydata(np.cos(x))

plt.show()

print(
    "matplotlib 06 ------------------------------------------------------------"
)  # 60個

from matplotlib import pyplot as plt

x = np.linspace(-np.pi, np.pi, 200, endpoint=True)
s, c = np.sin(x), np.cos(x)

# 移動坐標軸邊線
# 坐標軸總共有四個連線，我們通過設置透明色隱藏上方和右方的邊線
# 通過 set_position() 移動左側和下側的邊線
# 通過 set_ticks_position() 設置坐標軸的刻度線的顯示位置
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.spines["bottom"].set_position(("data", 0))
ax.yaxis.set_ticks_position("left")
ax.spines["left"].set_position(("data", 0))
# 設置坐標刻度的字體大小，增加半透明背景
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.65))

# 設置坐標軸的長度
plt.xlim(x.min() * 1.1, x.max() * 1.1)
plt.ylim(c.min() * 1.1, c.max() * 1.1)

# 設置坐標軸的刻度和標簽
plt.xticks(
    (-np.pi, -np.pi / 2, np.pi / 2, np.pi),
    label=(r"$-\pi$", r"$-\pi/2$", r"$+\pi/2$", r"$+\pi$"),
)
plt.yticks([-1, -0.5, 0, 0.5, 1])

# 畫出正弦曲線，并設置線條顏色，寬度，樣式
plt.plot(x, s, color="red", linewidth=2.0, linestyle="-")
# 畫出余弦曲線，并設置線條顏色，寬度，樣式
plt.plot(x, c, color="blue", linewidth=2.0, linestyle="-")

# 在左上角添加銘牌
# plt.legend(loc='upper left')

# 在坐標軸上標示相應的點
t = 2 * np.pi / 3
# 畫出 cos(t) 所在的點在 X 軸上的位置，即畫出 (t, 0) -> (t, cos(t)) 線段，使用虛線
plt.plot([t, t], [0, np.cos(t)], color="blue", linewidth=1.5, linestyle="--")
# 畫出標示的坐標點，即在 (t, cos(t)) 處畫一個大小為 50 的藍色點
plt.scatter(
    [
        t,
    ],
    [
        np.cos(t),
    ],
    50,
    color="blue",
)
# 畫出標示點的值，即 cos(t) 的值
plt.annotate(
    r"$cos(\frac{2\pi}{3})=-\frac{1}{2}$",
    xy=(t, np.cos(t)),
    xycoords="data",
    xytext=(-90, -50),
    textcoords="offset points",
    fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
# 畫出 sin(t) 所在的點在 X 軸上的位置，即畫出 (t, 0) -> (t, sin(t)) 線段，使用虛線
plt.plot([t, t], [0, np.sin(t)], color="red", linewidth=1.5, linestyle="--")
# 畫出標示的坐標點，即在 (t, sin(t)) 處畫一個大小為 50 的紅色點
plt.scatter(
    [
        t,
    ],
    [
        np.sin(t),
    ],
    50,
    color="red",
)
# 畫出標示點的值，即 sin(t) 的值
plt.annotate(
    r"$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$",
    xy=(t, np.sin(t)),
    xycoords="data",
    xytext=(+10, +30),
    textcoords="offset points",
    fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.show()

print(
    "matplotlib 07 ------------------------------------------------------------"
)  # 60個


def tickline():
    plt.xlim(0, 10), plt.ylim(-1, 1), plt.yticks([])
    ax = plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["left"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.xaxis.set_ticks_position("bottom")
    ax.spines["bottom"].set_position(("data", 0))
    ax.yaxis.set_ticks_position("none")
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
    ax.plot(np.arange(11), np.zeros(11))
    return ax


locators = [
    "plt.NullLocator()",
    "plt.MultipleLocator(base=1.0)",
    "plt.FixedLocator(locs=[0, 2, 8, 9, 10])",
    "plt.IndexLocator(base=3, offset=1)",
    "plt.LinearLocator(numticks=5)",
    "plt.LogLocator(base=2, subs=[1.0])",
    "plt.MaxNLocator(nbins=3, steps=[1, 3, 5, 7, 9, 10])",
    "plt.AutoLocator()",
]

n_locators = len(locators)

size = 1024, 60 * n_locators
dpi = 100.0

figsize = size[0] / float(dpi), size[1] / float(dpi)

fig = plt.figure(
    num="matplotlib 07",
    figsize=figsize,
    dpi=dpi,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

fig.patch.set_alpha(0)


for i, locator in enumerate(locators):
    plt.subplot(n_locators, 1, i + 1)
    ax = tickline()
    ax.xaxis.set_major_locator(eval(locator))
    plt.text(5, 0.3, locator[3:], ha="center", size=16)

plt.subplots_adjust(bottom=0.01, top=0.99, left=0.01, right=0.99)
plt.show()

print(
    "matplotlib 08 ------------------------------------------------------------"
)  # 60個


def plt_bar():
    n = 12
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

    plt.subplot(1, 2, 1)
    plt.bar(X, +Y1, facecolor="#9999ff", edgecolor="white")
    plt.bar(X, -Y2, facecolor="#ff9999", edgecolor="white")

    for x, y in zip(X, Y1):
        plt.text(x + 0.4, y + 0.05, "%.2f" % y, ha="center", va="bottom")

    for x, y in zip(X, Y2):
        plt.text(x + 0.4, -y - 0.05, "%.2f" % y, ha="center", va="top")

    plt.xlim(-0.5, n)
    plt.xticks(())
    plt.ylim(-1.25, 1.25)
    plt.yticks(())


def plt_contour():
    def f(x, y):
        return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2) - y**2)

    n = 256
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X, Y = np.meshgrid(x, y)

    plt.subplot(1, 2, 2)

    plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)
    C = plt.contour(X, Y, f(X, Y), 8, colors="black")
    plt.clabel(C, inline=1, fontsize=10)

    plt.xticks(())
    plt.yticks(())


plt.figure(
    num="matplotlib 08",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt_bar()
plt_contour()

plt.show()

print(
    "matplotlib 09 ------------------------------------------------------------"
)  # 60個


def plt_grid():
    ax = plt.subplot(1, 2, 1)

    ax.set_xlim(0, 4)
    ax.set_ylim(0, 3)
    ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
    ax.grid(which="major", axis="x", linewidth=0.75, linestyle="-", color="0.75")
    ax.grid(which="minor", axis="x", linewidth=0.25, linestyle="-", color="0.75")
    ax.grid(which="major", axis="y", linewidth=0.75, linestyle="-", color="0.75")
    ax.grid(which="minor", axis="y", linewidth=0.25, linestyle="-", color="0.75")
    ax.set_xticklabels([])
    ax.set_yticklabels([])


def plt_polar():
    ax = plt.subplot(1, 2, 2, polar=True)

    N = 20
    theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
    radii = 10 * np.random.rand(N)
    width = np.pi / 4 * np.random.rand(N)
    bars = plt.bar(theta, radii, width=width, bottom=0.0)

    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet(r / 10.0))
        bar.set_alpha(0.5)

    ax.set_xticklabels([])
    ax.set_yticklabels([])


plt.figure(
    num="matplotlib 09",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt_grid()
plt_polar()

plt.show()

print(
    "matplotlib 10 ------------------------------------------------------------"
)  # 60個

x = np.linspace(0, 2 * np.pi, 300)
y = np.sin(x)

fig = plt.figure(
    num="matplotlib 10",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

ax1 = fig.add_subplot(121, projection="polar")
ax1.plot(x, y)
ax1.set_title("極座標 Sin 圖", fontsize=12)

ax2 = fig.add_subplot(122)
ax2.plot(x, y)
ax2.set_title("一般座標 Sin 圖", fontsize=12)
ax2.set_aspect(2)

plt.show()

print(
    "matplotlib 11 ------------------------------------------------------------"
)  # 60個

import numpy as np
from matplotlib import pyplot as plt

ax = np.linspace(0, 20, 100)
ay = ax * 0.15
by = np.sin(ax)

# 產生子圖表，第一個數值為縱軸要有幾張圖，第二個數值為橫軸，第三個數值為排在哪裡
# label 可以設定圖例標籤
#  '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.plot(ax, ay, color="red", linewidth=8.0, linestyle="dotted", label="x0.5")
plt.plot(ax, by, color="blue", linewidth=2.0, linestyle="-", label="sin")
plt.ylim((-3, 3))  # y 軸上下最大和最小區間
plt.xlim((0, 20))  # y 軸上下最大和最小區間
plt.yticks([-3, 0, 3], ["min(-3)", "0", "max(3)"])  # 可以設置座標軸上特定文字

xx = plt.gca()
xx.spines["right"].set_color("none")  # 設置邊框樣式
xx.spines["top"].set_color("none")
xx.spines["bottom"].set_position(("data", 0))  # 設置邊框位置

plt.show()

print(
    "matplotlib 15 ------------------------------------------------------------"
)  # 60個

import numpy as np
from matplotlib import pyplot as plt

ax = np.linspace(-20, 20, 100)
ay = ax * 0.5
by = np.sin(ax)
cx = 10
cy = cx * 0.5

plt.plot(ax, ay, color="red", linewidth=3.0, linestyle="dashed", label="x0.5", zorder=2)
plt.plot(ax, by, color="blue", linewidth=2.0, linestyle="solid", label="sin", zorder=2)
# 繪製垂直虛線
plt.plot(
    [
        cx,
        cx,
    ],
    [
        cy,
        0,
    ],
    color="black",
    linewidth=1.0,
    linestyle="dashed",
    zorder=1,
    alpha=0.5,
)

# 加上單一圓點
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html
plt.scatter(cx, cy, s=100, color="red", zorder=2)

# 繪製 annotate
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.annotate.html
plt.annotate(
    "test",
    xy=(cx + 0.5, cy - 0.2),
    xycoords="data",
    xytext=(+36, -36),
    textcoords="offset points",
    fontsize=12,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.ylim((-10, 10))  # 設定 x 和 y 的邊界值
plt.xlim((-20, 20))

xx = plt.gca()  # 設定座標軸位置
xx.spines["right"].set_color("none")
xx.spines["top"].set_color("none")
xx.spines["bottom"].set_position(("data", 0))
xx.spines["left"].set_position(("data", 0))

plt.show()

print(
    "matplotlib 16 ------------------------------------------------------------"
)  # 60個

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

print(
    "matplotlib 17 ------------------------------------------------------------"
)  # 60個

# 相同斜率平行移動

x = [x for x in range(0, 11)]
y1 = [2 * y for y in x]
y2 = [(2 * y - 2) for y in x]
y3 = [(2 * y + 2) for y in x]
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

# plt.show()

print(x)


print(
    "matplotlib 18 ------------------------------------------------------------"
)  # 60個

print(
    "matplotlib 19 ------------------------------------------------------------"
)  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
