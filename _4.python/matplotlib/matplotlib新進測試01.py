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

print("------------------------------------------------------------")  # 60個
plt.subplot(232)

N = 12
X = np.arange(N)

# 生成 N 組介於 0 與 1 之間均勻分配隨機變數
Y1 = np.random.uniform(size=N)
Y2 = np.random.uniform(size=N)

# 生成 N 組介於 ST 與 SP 之間均勻分配隨機變數
ST, SP = 0.5, 1.0
Y1 = np.random.uniform(ST, SP, size=N)
Y2 = np.random.uniform(ST, SP, size=N)

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

plt.xlim(-0.5, N)
plt.ylim(-1.25, 1.25)


print("------------------------------------------------------------")  # 60個
plt.subplot(233)

# nodelist = ["city1","city2","city3","city4","city5","city6","city7","city8"]
dist = np.mat(
    [
        [0.1, 0.1],
        [0.9, 0.5],
        [0.9, 0.1],
        [0.45, 0.9],
        [0.9, 0.8],
        [0.7, 0.9],
        [0.1, 0.45],
        [0.45, 0.1],
    ]
)
m, n = np.shape(dist)

for point in dist.tolist():
    plt.annotate(
        "(" + str(point[0]) + ", " + str(point[1]) + ")", xy=(point[0], point[1])
    )
xlist = []
ylist = []
for px, py in zip(dist.T.tolist()[0], dist.T.tolist()[1]):
    xlist.append([px])
    ylist.append([py])

plt.plot(xlist, ylist, "r")

print("------------------------------------------------------------")  # 60個
plt.subplot(234)

y, x = np.mgrid[-3:3:300j, -6:6:600j]
z = np.sin(x**2 + 2 * y**2 + x * y)
plt.imshow(z, cmap="Blues", vmin=-2, vmax=2)

# plt.colorbar(shrink=0.92)

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
plt.ylim(-1.5, 1.5)

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

x = [x for x in range(0, 11)]
y = [7.5 * y - 3.33 for y in x]
voucher = 25  # unit = 100
ans_x = (25 + 3.33) / 7.5
print("拜訪次數 = {}".format(int(ans_x * 100)))
plt.axis([0, 4, 0, 30])
plt.plot(x, y)
plt.plot(1, 5, "-x")
plt.plot(2, 10, "-x")
plt.plot(3, 20, "-x")
plt.plot(ans_x, 25, "-o")
plt.text(ans_x - 0.6, 25 + 0.2, "(" + str(int(ans_x * 100)) + "," + str(2500) + ")")
plt.xlabel("Times:unit=100")
plt.ylabel("Voucher:unit=100")
plt.grid()  # 加格線

print("------------------------------------------------------------")  # 60個
plt.subplot(232)

x = np.linspace(1, 10, 10)  # 建立 x
y = np.random.random((7, 10))  # 建立 y 7 X 10 的隨機陣列

print(y.shape)
print(y)

for yy in y:
    plt.scatter(x, yy, c="r", marker="*")

plt.xticks(np.arange(0, 11, step=1.0))

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

print("畫格線")
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

# 資訊圖表的視覺化手法

from PIL import Image, ImageOps

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

image = Image.open(filename)
print(image.size)

plt.imshow(image)

plt.show()


# resize 寬度一半 高度三成 => 變胖
resize_image = image.resize((int(image.size[0] * 0.5), int(image.size[1] * 0.3)))

plt.imshow(resize_image)

plt.show()

print(resize_image.size)

# 要排列的圖示個數
N = 10

# 圖片之間的邊界
margin = 5

# 載入圖片
image = Image.open("_data2/human.png")
image_width, image_height = image.size

# 將圖片入作為畫布使用的Image
canvas = Image.new("RGBA", ((image_width + margin) * N, image_height))
for i in range(N):
    canvas.paste(image, ((image_width + margin) * i, 0))

plt.imshow(canvas)

plt.show()

print("------------------------------------------------------------")  # 60個

# 圖片並列個數
N = 15

# 換行位置
wrap_num = 10

# 圖片之間的邊界
margin_h = 5
margin_v = 5

# 載入圖片
image = Image.open("_data2/human.png")
image_width, image_height = image.size

# 將圖片入作為畫布使用的Image
canvas = Image.new(
    "RGBA",
    (
        (image_width + margin_h) * wrap_num,
        (image_height + margin_v) * math.ceil(N / wrap_num),
    ),
)
for i in range(N):
    x = (image_width + margin_h) * (i % wrap_num)
    y = (image_height + margin_v) * (i // wrap_num)
    canvas.paste(image, (x, y))

plt.imshow(canvas)

plt.show()

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageOps

image = Image.open("_data2/woman.png")

plt.imshow(image)

plt.show()

print("------------------------------")  # 30個


def fill(image, percentage=100):
    start = int(image.size[1] / 100 * percentage)
    for y in range(image.size[1] - start, image.size[1]):
        for x in range(image.size[0]):
            if image.getpixel((x, y))[3] != 0:
                image.putpixel((x, y), (255, 200, 200))


fill(image, 90)

plt.imshow(image)

plt.show()

print("------------------------------------------------------------")  # 60個

# 圖片並列個數
N = 10

# 圖片之間的邊界
margin = 5


# 以指定的顏色替圖片填色的函數
def fill(image, color=(255, 255, 255)):
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            if image.getpixel((x, y))[3] != 0:
                image.putpixel((x, y), color)


# 載入圖片
image = Image.open("_data2/human.png")
image_width, image_height = image.size

# 將圖片入作為畫布使用的Image
canvas = Image.new("RGBA", ((image_width + margin) * N, image_height))
for i in range(N):
    if i < 7:
        # 到第7張圖片之前的圖片都是藍色
        color = (0, 0, 255)
    else:
        # 第7張圖片之後的圖片都是紅色
        color = (255, 0, 0)

    # 以指定的顏色替圖片填色
    color_image = image.copy()
    fill(color_image, color)

    # 貼入圖片
    canvas.paste(color_image, ((image_width + margin) * i, 0))

plt.imshow(canvas)

plt.show()

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw, ImageFont


class IconGraph:
    # 初始化的內容
    def __init__(
        self,
        data,
        icon_size=(128, 128),
        size=(800, 800),
        back_color=(255, 255, 255),
        label_back_color=(255, 255, 255),
        font="C:\Windows\Fonts\msjh.ttc",
        font_size=24,
        font_color=(0, 0, 0),
    ):
        self.canvas_size = [size[0], size[1]]  # 圖表的整體大小
        self.label_field_height = 100  # 繪製標籤區塊的高度
        # 繪製圖表的範圍大小
        self.graph_size = [
            self.canvas_size[0],
            self.canvas_size[1] - self.label_field_height,
        ]
        self.icon_size = icon_size  # 圖示的大小
        self.back_color = back_color  # 圖表區塊的背景色
        self.label_back_color = label_back_color  # 標籤區塊的背景色

        # 設定標籤資訊
        self.labels = []
        for d in data:
            self.labels.append(d["label"])

        # 取得value的最大值
        value_max = data[0]["value"]
        for d in data:
            if value_max < d["value"]:
                value_max = d["value"]

        # 儲存格的個數
        self.grid_y = value_max  # 儲存格的個數（垂直）
        self.grid_x = len(data)  # 儲存格的個數（水平）

        # 儲存格的大小
        # 單一儲存格可使用的高度
        self.grid_height = self.icon_size[1]
        # 單一儲存格可使用的寬度
        self.grid_width = self.graph_size[0] // self.grid_x

        # 距離儲存格中心點的位移量
        self.grid_med_offset = (self.grid_width // 2, self.grid_height // 2)

        # 假設圖表區塊的高度不夠就自動擴張
        if self.graph_size[1] < self.grid_height * self.grid_y:
            self.graph_size[1] = self.grid_height * self.grid_y
            self.canvas_size[1] = (
                self.grid_height * self.grid_y + self.label_field_height
            )

        # 建立格點
        self.grid = [[None for i in range(self.grid_y)] for j in range(self.grid_x)]

        # 於格點新增圖片
        for x in range(len(data)):
            target = data[x]
            icon = Image.open(target["image"])
            for j in range(target["value"]):
                self.grid[x][j] = icon

        # 設定標籤的字型
        self.font = ImageFont.truetype(font, font_size)
        self.font_color = font_color

        # 繪製圖表
        self._draw()

    # 繪製圖表
    def _draw(self):
        # 建立繪製畫布與圖表的區塊
        self.canvas = Image.new("RGBA", self.canvas_size, self.label_back_color)
        self.graph_field = Image.new("RGBA", self.graph_size, self.back_color)

        # 在圖表區塊繪製圖示
        for x in range(len(self.grid)):
            # 計算繪製位置
            x_offset = x * self.grid_width  # 儲存格左端的座標

            # 繪製標籤
            imd = ImageDraw.Draw(self.canvas)
            # 計算標籤的大小
            label_size = imd.textsize(self.labels[x], self.font)
            # 標籤左端的座標
            label_x = x_offset + self.grid_med_offset[0] - label_size[0] // 2

            imd.text(
                (label_x, self.graph_size[1]),
                self.labels[x],
                font=self.font,
                fill=self.font_color,
            )

            # 繪製圖示
            for y in range(len(self.grid[x])):
                if self.grid[x][y] is None:
                    continue
                c_x = (
                    x_offset + self.grid_med_offset[0] - self.icon_size[0] // 2
                )  # 圖示左端的座標
                c_y = (
                    self.graph_size[1] - (y * self.grid_height) - self.grid_height
                )  # 圖示上緣的座標
                self.graph_field.paste(self.grid[x][y], (c_x, c_y), self.grid[x][y])

        # 將圖表區塊貼入畫布
        self.canvas.paste(self.graph_field)

    # 傳回圖表的圖片
    def get_image(self):
        return self.canvas


print("------------------------------------------------------------")  # 60個

# 繪製以圖片代替長條的長條圖

# 預設圖示的大小一致
# 圖示的大小
icon_size = (128, 128)

# 整張圖表的大小（圖表的高度會自動擴張）
canvas_size = (800, 800)

# 圖表區塊的背景色
graph_back_color = (248, 255, 248)

# 標籤區塊的背景色
label_back_color = (130, 230, 180)

# 定義資料
data = [
    {
        "label": "Dolphin",  # 標籤
        "image": "_data2/dolphin.png",  # 用於堆疊的圖片
        "value": 3,  # 堆疊個數
    },
    {"label": "Penguin", "image": "_data2/penguin.png", "value": 5},
    {"label": "Sunfish", "image": "_data2/sunfish.png", "value": 2},
]

""" NG
ig = IconGraph(data, icon_size, canvas_size, graph_back_color, label_back_color)
ig.get_image()
"""


print("------------------------------------------------------------")  # 60個

print("資料視覺化的調色盤 many")
"""
import seaborn as sns

sns.set()
current_palette = sns.color_palette()
sns.palplot(current_palette)

#02 seaborn的調色盤

#適用於質化變數視覺化手法的調色盤

sns.palplot(sns.color_palette("husl", 8))

sns.palplot(sns.color_palette("Set1", 8))

sns.palplot(sns.color_palette("Set2", 8))

sns.palplot(sns.color_palette("Paired", 8))

#適用於質化變數視覺化手法的調色盤

sns.palplot(sns.color_palette("Blues"))

sns.palplot(sns.color_palette("BuGn_r"))

sns.palplot(sns.color_palette("GnBu_d"))

sns.palplot(sns.color_palette("Reds"))

sns.palplot(sns.color_palette("Reds_r"))

sns.palplot(sns.color_palette("Reds_d"))

#無彩色的調色盤

sns.palplot(sns.color_palette("binary"))

sns.palplot(sns.color_palette("gray"))

sns.palplot(sns.color_palette("gist_gray_r"))

#適用於數值在基準值前後分佈的調色盤

sns.palplot(sns.color_palette("RdBu", 7))

sns.palplot(sns.color_palette("coolwarm", 7))

plt.show()
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

plt.xticks(())  # ignore xticks
plt.yticks(())  # ignore yticks

# plt.axis("off")
# plt.axis("off")  # 隱藏坐標軸

# plt.title("標題在特定位置", size="x-large", y=-0.1)  # 顯示圖片描述

plt.title("標題在特定位置", size=30, x=0.0, y=0.0)


#!wget -O taipei_sans_tc_beta.ttf https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download
#!mv taipei_sans_tc_beta.ttf /usr/local/lib/python3.7/dist-packages/matplotlib/mpl-data/fonts/ttf

# import matplotlib
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
