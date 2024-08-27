# 新進測試01

# 先做成 2X3 子圖, 以利搬出

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
    num="新進測試 01",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個
plt.subplot(231)

# image data
a = np.array(
    [
        0.313660827978,
        0.365348418405,
        0.423733120134,
        0.365348418405,
        0.439599930621,
        0.525083754405,
        0.423733120134,
        0.525083754405,
        0.651536351379,
    ]
).reshape(3, 3)

"""
for the value of "interpolation", check this:
http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
for the value of "origin"= ['upper', 'lower'], check this:
http://matplotlib.org/examples/pylab_examples/image_origin.html
"""
plt.imshow(a, interpolation="nearest", cmap="bone", origin="lower")
plt.colorbar(shrink=0.92)

plt.xticks(())
plt.yticks(())


print("------------------------------------------------------------")  # 60個
plt.subplot(232)


print("------------------------------------------------------------")  # 60個
plt.subplot(233)


print("------------------------------------------------------------")  # 60個
plt.subplot(234)

y, x = np.mgrid[-3:3:300j, -6:6:600j]
z = np.sin(x**2 + 2 * y**2 + x * y)
plt.imshow(z, cmap="Blues", vmin=-2, vmax=2)

# plt.colorbar(shrink=0.92)

plt.xticks(())
plt.yticks(())


print("------------------------------------------------------------")  # 60個
plt.subplot(235)

# 畫  (x^2 + y^2 -1)^3 - x^2*y^3 = 0
# %fig=matplotlib繪制心形隱函數曲線
x, y = np.mgrid[-2:2:500j, -2:2:500j]
z = (x**2 + y**2 - 1) ** 3 - x**2 * y**3
plt.contourf(x, y, z, levels=[-1, 0], colors=["red"])
plt.gca().set_aspect("equal")


print("------------------------------------------------------------")  # 60個
plt.subplot(236)

n = 1024  # data size
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)  # for color later on

plt.scatter(X, Y, s=75, c=T, alpha=0.5)

plt.xlim(-1.5, 1.5)
plt.xticks(())  # ignore xticks

plt.ylim(-1.5, 1.5)
plt.yticks(())  # ignore yticks

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="新進測試 02",
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


print("------------------------------------------------------------")  # 60個
plt.subplot(233)


print("------------------------------------------------------------")  # 60個
plt.subplot(234)


print("------------------------------------------------------------")  # 60個
plt.subplot(235)


print("------------------------------------------------------------")  # 60個
plt.subplot(236)


plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個


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

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個


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

print("------------------------------------------------------------")  # 60個

ax = plt.subplot(1, 1, 1)

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

plt.show()

print("------------------------------------------------------------")  # 60個

#!wget -O taipei_sans_tc_beta.ttf https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download
#!mv taipei_sans_tc_beta.ttf /usr/local/lib/python3.7/dist-packages/matplotlib/mpl-data/fonts/ttf
import matplotlib
from matplotlib.font_manager import fontManager

# 新增字體
# fontManager.addfont('/usr/local/lib/python3.7/dist-packages/matplotlib/mpl-data/fonts/ttf/taipei_sans_tc_beta.ttf')
# 將 font-family 設為 Taipei Sans TC Beta
# 設定完後，之後的圖表都可以顯示中文了
SMALL_SIZE = 8
MEDIUM_SIZE = 14
BIGGER_SIZE = 18
# 設定字型
# matplotlib.rc('font', family='Taipei Sans TC Beta')
# matplotlib.rc('font', size=SMALL_SIZE)
# 預設字體大小
plt.rc("font", size=SMALL_SIZE)
# 軸標題字體大小
plt.rc("axes", titlesize=BIGGER_SIZE)
# 軸標籤字體大小
plt.rc("axes", labelsize=MEDIUM_SIZE)
# X軸刻度字體大小
plt.rc("xtick", labelsize=SMALL_SIZE)
# Y軸刻度字體大小
plt.rc("ytick", labelsize=SMALL_SIZE)
# 圖例字體大小
plt.rc("legend", fontsize=SMALL_SIZE)
# 圖形標題字體大小
plt.rc("figure", titlesize=BIGGER_SIZE)

print("------------------------------------------------------------")  # 60個

# 準備描點x,y資料
x = np.arange(-10, 10, 0.1)
y1 = x**3
y2 = x**2
# 指定 寬6.4inches, 高4.8inches, 160dpi
# 將圖分成一個子圖
fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=160)
# 畫出y=x**3曲線
ax.plot(x, y1)
# 畫出y=x**2曲線
ax.plot(x, y2)
# 加上X軸刻度範圍-10~10(如果大小顛倒，圖形會左右鏡射)
ax.set_xlim(-10, 10)
# 加上Y軸刻度範圍-1000~1000(如果大小顛倒，圖形會左右鏡射)
ax.set_ylim(-1000, 1000)
# 加上X軸刻度標示 -10,-9,-8,...,10(只有整數),字體大小為預設
ax.set_xticks(np.arange(-10, 11, 1))
# 加上Y軸刻度標示 -1000,-900,...,1000(只有100的倍數),字體大小為預設
ax.set_yticks(np.arange(-1000, 1000, 100))
# 加上X軸標題(靠右對齊x=1.0為X軸最右)
ax.set_xlabel("X軸", horizontalalignment="right", verticalalignment="top", x=1.0)
# 加上Y軸標題(靠上對齊y=1.0為Y軸最上)
ax.set_ylabel("Y軸", horizontalalignment="right", verticalalignment="bottom", y=1.0)
# ax.set(xlabel='X軸', ylabel='Y軸')

ax.grid()  # 加上格線

# 子圖標題
ax.set_title("子圖標題", loc="right")

# figure標題
fig.suptitle("y=x**3&y=x**2")

# 儲存檔案名為test.png
# fig.savefig("tmp_test.png")

# 圖例說明
ax.legend(["y=x**3", "y=x**2"])

plt.show()

print("------------------------------------------------------------")  # 60個

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor="#9999ff", edgecolor="white")
plt.bar(X, -Y2, facecolor="#ff9999", edgecolor="white")

for x, y in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, y + 0.05, "%.2f" % y, ha="center", va="bottom")

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, -y - 0.05, "%.2f" % y, ha="center", va="top")

plt.xlim(-0.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()

print("------------------------------------------------------------")  # 60個


def f(x, y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2) - y**2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

# use plt.contourf to filling contours
# X, Y and value for (X,Y) point
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)

# use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors="black", linewidth=0.5)
# adding label
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())

plt.show()

print("------------------------------------------------------------")  # 60個


""" 久
# 繪制心形隱函數曲面
# pip install mayavi

from mayavi import mlab

x, y, z = np.mgrid[-3:3:100j, -1:1:100j, -3:3:100j]
f = (x**2 + 9.0/4*y**2 + z**2 - 1)**3 - x**2 * z**3 - 9.0/80 * y**2 * z**3
contour = mlab.contour3d(x, y, z, f, contours=[0], color=(1, 0, 0))
"""

print("------------------------------------------------------------")  # 60個

# 新增圖表 並 設定屬性
plt.figure(
    figsize=[12, 8],
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)
plt.plot([1, 2, 3])

plt.axis("off")  # 隱藏坐標軸
_ = plt.title("image file", size="x-large", y=-0.1)  # 顯示圖片描述

plt.axis("off")
plt.title("Picture Title", size=30, x=0.0, y=0.0)

plt.show()

print("------------------------------------------------------------")  # 60個

N = 50  # 色彩數列的點數
colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
colors = []  # 建立色彩數列
for i in range(N):  # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.linspace(0.0, 2 * np.pi, N)  # 建立 50 個點
y = np.sin(x)
fig = plt.figure()  # 建立畫布物件
ax = fig.add_subplot()  # 建立子圖(或稱軸物件)ax
ax.scatter(x, y, c=colors, marker="*")  # 繪製 sin
ax.set_title("建立畫布與軸物件,使用OO API繪圖", fontsize=16)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
