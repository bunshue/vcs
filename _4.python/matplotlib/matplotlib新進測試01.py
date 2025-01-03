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

import ssl

ssl._create_default_https_context = ssl._create_stdlib_context


def show():
    plt.show()
    pass


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

print("------------------------------")  # 30個
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

print("------------------------------")  # 30個
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


print("------------------------------")  # 30個
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

print("------------------------------")  # 30個
plt.subplot(234)

y, x = np.mgrid[-3:3:300j, -6:6:600j]
z = np.sin(x**2 + 2 * y**2 + x * y)
plt.imshow(z, cmap="Blues", vmin=-2, vmax=2)

# plt.colorbar(shrink=0.92)

print("------------------------------")  # 30個
plt.subplot(235)

# 畫  (x^2 + y^2 -1)^3 - x^2*y^3 = 0
# %fig=matplotlib繪制心形隱函數曲線
x, y = np.mgrid[-2:2:500j, -2:2:500j]
z = (x**2 + y**2 - 1) ** 3 - x**2 * y**3
plt.contourf(x, y, z, levels=[-1, 0], colors=["red"])
plt.gca().set_aspect("equal")

print("------------------------------")  # 30個
plt.subplot(236)


plt.tight_layout()

show()

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

print("------------------------------")  # 30個
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

print("------------------------------")  # 30個
plt.subplot(232)


print("------------------------------")  # 30個
plt.subplot(233)


print("------------------------------")  # 30個
plt.subplot(234)


print("------------------------------")  # 30個
plt.subplot(235)


print("------------------------------")  # 30個
plt.subplot(236)


plt.tight_layout()

show()

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

show()

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

show()

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

show()

print("------------------------------------------------------------")  # 60個

# 資訊圖表的視覺化手法

from PIL import Image, ImageOps

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

image = Image.open(filename)
print(image.size)

plt.imshow(image)

show()


# resize 寬度一半 高度三成 => 變胖
resize_image = image.resize((int(image.size[0] * 0.5), int(image.size[1] * 0.3)))

plt.imshow(resize_image)

show()

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

show()

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

show()

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageOps

image = Image.open("_data2/woman.png")

plt.imshow(image)

show()

print("------------------------------")  # 30個


def fill(image, percentage=100):
    start = int(image.size[1] / 100 * percentage)
    for y in range(image.size[1] - start, image.size[1]):
        for x in range(image.size[0]):
            if image.getpixel((x, y))[3] != 0:
                image.putpixel((x, y), (255, 200, 200))


fill(image, 90)

plt.imshow(image)

show()

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

show()

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

show()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
z = np.cos(x)

# Create Plot
fig, axes = plt.subplots(2, 3)

# Plot Data
axes[0, 0].plot(x, y)
axes[0, 1].plot(x, y)
axes[0, 2].plot(x, y)
axes[1, 0].plot(x, y)
axes[1, 1].plot(x, y)
axes[1, 2].plot(x, y)


axes[0, 0].set_xlabel("x")
axes[0, 0].set_ylabel("y")
axes[0, 0].set_title("第一張圖")
axes[0, 0].grid(True)

show()

print("------------------------------------------------------------")  # 60個

Z = np.random.uniform(0, 1, (8, 8))
plt.imshow(Z)

show()

print("------------------------------------------------------------")  # 60個

Z = np.random.uniform(0, 1, (8, 8))
plt.contourf(Z)

show()

print("------------------------------------------------------------")  # 60個

Z = np.random.normal(0, 1, 100)
plt.hist(Z)

show()

print("------------------------------------------------------------")  # 60個

# Create an error bar plot
X = np.arange(5)
Y = np.random.uniform(0, 1, 5)
plt.errorbar(X, Y, Y / 4)

show()

print("------------------------------------------------------------")  # 60個

# Create a box plot
Z = np.random.normal(0, 1, (100, 3))
plt.boxplot(Z)

show()

print("------------------------------------------------------------")  # 60個

# Create a figure with two subplots (vertically stacked)
X = np.linspace(0, 10, 100)
Y1, Y2 = np.sin(X), np.cos(X)
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(X, Y1, color="C1")
ax2.plot(X, Y2, color="C0")

show()

print("------------------------------------------------------------")  # 60個

# Create a figure with two subplots (horizontally aligned)
X = np.linspace(0, 10, 100)
Y1, Y2 = np.sin(X), np.cos(X)
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(Y1, X, color="C1")
ax2.plot(Y2, X, color="C0")

show()

print("------------------------------------------------------------")  # 60個

# Figure, axes & spines

# Create a 3x3 grid of subplots
fig, axs = plt.subplots(3, 3)

# Set face colors for specific subplots
axs[0, 0].set_facecolor("#ddddff")
axs[2, 2].set_facecolor("#ffffdd")

# Create a 3x3 grid of subplots
fig, axs = plt.subplots(3, 3)

# Add a grid specification and set face color for a specific subplot
gs = fig.add_gridspec(3, 3)
ax = fig.add_subplot(gs[0, :])
ax.set_facecolor("#ddddff")

# Create a figure with a single subplot
fig, ax = plt.subplots()

# Remove top and right spines from the subplot
ax.spines["top"].set_color("None")
ax.spines["right"].set_color("None")

show()

print("------------------------------------------------------------")  # 60個

# Ticks & labels

from matplotlib.ticker import MultipleLocator as ML
from matplotlib.ticker import ScalarFormatter as SF

# Create a figure with a single subplot
fig, ax = plt.subplots()

# Set minor tick locations and formatter for the x-axis
ax.xaxis.set_minor_locator(ML(0.2))
ax.xaxis.set_minor_formatter(SF())

# Rotate minor tick labels on the x-axis
ax.tick_params(axis="x", which="minor", rotation=90)

show()

print("------------------------------------------------------------")  # 60個

# Lines & markers

# Generate data and create a plot
X = np.linspace(0.1, 10 * np.pi, 1000)
Y = np.sin(X)
plt.plot(X, Y, "C1o:", markevery=25, mec="1.0")

show()

print("------------------------------------------------------------")  # 60個

# Scales & projections

# Create a figure with a single subplot
fig, ax = plt.subplots()

# Set x-axis scale to logarithmic
ax.set_xscale("log")

# Plot data with specified formatting
ax.plot(X, Y, "C1o-", markevery=25, mec="1.0")

show()

print("------------------------------------------------------------")  # 60個

# Text & ornaments

# Create a figure with a single subplot
fig, ax = plt.subplots()

# Fill the area between horizontal lines with a curve
ax.fill_betweenx([-1, 1], [0], [2 * np.pi])

# Add a text annotation to the plot
ax.text(0, -1, r" Period $\Phi$")

show()

print("------------------------------------------------------------")  # 60個

# Legend

# Create a figure with a single subplot
fig, ax = plt.subplots()

# Plot sine and cosine curves with specified colors and labels
ax.plot(X, np.sin(X), "C0", label="Sine")
ax.plot(X, np.cos(X), "C1", label="Cosine")

# Add a legend with customized positioning and formatting
ax.legend(bbox_to_anchor=(0, 1, 1, 0.1), ncol=2, mode="expand", loc="lower left")

show()

print("------------------------------------------------------------")  # 60個

# Annotation

# Create a figure with a single subplot
fig, ax = plt.subplots()

ax.plot(X, Y, "C1o:", markevery=25, mec="1.0")

# Add an annotation "A" with an arrow
ax.annotate(
    "A",
    (X[250], Y[250]),
    (X[250], -1),
    ha="center",
    va="center",
    arrowprops={"arrowstyle": "->", "color": "C1"},
)

show()

print("------------------------------------------------------------")  # 60個

# Colors

from matplotlib.patches import Rectangle
import matplotlib.colors as mcolors


def plot_colortable(colors, *, ncols=4, sort_colors=True):
    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12

    # Sort colors by hue, saturation, value and name.
    if sort_colors is True:
        names = sorted(
            colors, key=lambda c: tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(c)))
        )
    else:
        names = list(colors)

    n = len(names)
    nrows = math.ceil(n / ncols)

    width = cell_width * 4 + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(
        margin / width,
        margin / height,
        (width - margin) / width,
        (height - margin) / height,
    )
    ax.set_xlim(0, cell_width * 4)
    ax.set_ylim(cell_height * (nrows - 0.5), -cell_height / 2.0)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(
            text_pos_x,
            y,
            name,
            fontsize=14,
            horizontalalignment="left",
            verticalalignment="center",
        )

        ax.add_patch(
            Rectangle(
                xy=(swatch_start_x, y - 9),
                width=swatch_width,
                height=18,
                facecolor=colors[name],
                edgecolor="0.7",
            )
        )

    return fig


# CSS Colors
plot_colortable(mcolors.CSS4_COLORS)

show()

print("------------------------------------------------------------")  # 60個

# Get a list of named colors
named_colors = plt.colormaps()
print("Colors:", named_colors)

print("------------------------------------------------------------")  # 60個

# 存檔

plt.savefig("tmp_aaa.png")

# Save the figure as a PNG file with higher resolution (300 dpi)
fig.savefig("tmp_bbb.png", dpi=300)

# Save the figure as a PDF file
fig.savefig("tmp_ccc.pdf")

print("------------------------------------------------------------")  # 60個

"""
Matplotlib 多邊形繪製

對於繪圖而言，多邊形繪製是個常見需求，
想在 Matplotlib 繪製多邊形，
可以透過 matplotlib.collections 的 PolyCollection 收集多邊形頂點
"""

from matplotlib.collections import PolyCollection

ax = plt.gca()

ax.add_collection(
    PolyCollection(
        [
            [[0, 0], [10, 0], [0, 10]],  # 三角形
            [[0, 20], [20, 20], [20, 40], [0, 40]],  # 長方形
        ]
    )
)

ax.add_collection(
    PolyCollection(
        [[[25, 15], [45, 20], [45, 40], [40, 45], [30, 40]]],  # 五邊形
        linewidth=0.1,
        facecolor="red",
        edgecolor="black",
    )
)

ax.set_xlim([0, 50])
ax.set_ylim([0, 50])
show()

print("------------------------------------------------------------")  # 60個

"""
Matplotlib 多邊形繪製

來運用多邊形繪製來產生〈NumPy 陣列資料型態〉中的謝爾賓斯基三角形：
"""

from matplotlib.collections import PolyCollection


def sierpinski(n):
    def quotientAndRemainderZero(elem, n):
        quotient = elem // n
        remainder = elem % n
        return quotient & remainder == 0

    quotientAndRemainderZero = np.frompyfunc(quotientAndRemainderZero, 2, 1)

    nums = np.arange(n**2)
    nums = nums[np.where(quotientAndRemainderZero(nums, n))]
    return (nums % n, nums // n)


# 在每個 x, y 建立一個三角形
def tri(x, y):
    return [[x, y], [x + 1, y], [x, y + 1]]


tri = np.frompyfunc(tri, 2, 1)

n = 32
x, y = sierpinski(n)

ax = plt.gca()
ax.add_collection(PolyCollection(tri(x, y)))
ax.set_xlim([0, n])
ax.set_ylim([0, n])
show()

print("------------------------------------------------------------")  # 60個

"""
Matplotlib 多邊形繪製

若要在三維空間繪製多邊形，
可以透過 mpl_toolkits.mplot3d.art3d 的 Poly3DCollection，
例如在〈Matplotlib 三角曲面〉透過六次呼叫 plot_surface 來繪製立方體的範例
"""

from mpl_toolkits.mplot3d.art3d import Poly3DCollection

width = 30
depth = 40
height = 50


def box(width, depth, height):
    faces = Poly3DCollection(
        [
            [[0, 0, 0], [width, 0, 0], [width, depth, 0], [0, depth, 0]],
            [
                [0, 0, height],
                [width, 0, height],
                [width, depth, height],
                [0, depth, height],
            ],
            [[0, 0, 0], [width, 0, 0], [width, 0, height], [0, 0, height]],
            [
                [0, depth, 0],
                [width, depth, 0],
                [width, depth, height],
                [0, depth, height],
            ],
            [[0, 0, 0], [0, depth, 0], [0, depth, height], [0, 0, height]],
            [
                [width, 0, 0],
                [width, depth, 0],
                [width, depth, height],
                [width, 0, height],
            ],
        ]
    )
    faces.set_edgecolor("black")

    ax = plt.axes(projection="3d")
    ax.add_collection3d(faces)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    lim = max(width, depth, height)
    ax.set_xlim([0, lim])
    ax.set_ylim([0, lim])
    ax.set_zlim([0, lim])

    show()


box(width, depth, height)

print("------------------------------------------------------------")  # 60個
"""
Matplotlib 多邊形繪製
既然如此，要用 Poly3DCollection 來繪製正四面體也是可以的：
"""

from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def tetrahedron(width):
    n = width / (2**0.5) * 0.5

    xs = np.array([n, -n, n, -n])
    ys = np.array([n, n, -n, -n])
    zs = np.array([n, -n, -n, n])

    coord = np.dstack((xs, ys, zs))[0]

    faces = Poly3DCollection(
        [coord[[0, 1, 2]], coord[[1, 2, 3]], coord[[2, 3, 0]], coord[[3, 0, 1]]]
    )
    faces.set_edgecolor("black")

    ax = plt.axes(projection="3d")
    ax.add_collection3d(faces)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.set_xlim([-n, n])
    ax.set_ylim([-n, n])
    ax.set_zlim([-n, n])

    show()


width = 30
tetrahedron(width)

print("------------------------------------------------------------")  # 60個

plt.fill("time", "signal", "g", data={"time": [0, 1, 2, 3], "signal": [0, 1, 1, 0]})
plt.xlabel("Time")
plt.ylabel("Signal")
show()


print("------------------------------------------------------------")  # 60個

# plt畫圖
from matplotlib import patches
from PIL import Image

# 在圖上作畫

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => PIL影像
im = Image.open(filename)
im_w, im_h = im.size
W = im_w
H = im_h

pic = plt.imshow(im, alpha=0.8)  # 使用 alpha

x_st = 20
y_st = 20
w = W - 40
h = H - 40

# 畫出矩形
patch = patches.Rectangle((x_st, y_st), w, h, fill=False, linewidth=2, color="r")
pic.axes.add_patch(patch)

# 畫多邊形
vertices = []
vertices.append((0, 0))
vertices.append((100, 0))
vertices.append((100, 100))
vertices.append((50, 150))
vertices.append((0, 100))
vertices.append((0, 0))
patch = patches.Polygon(vertices, closed=True, fill=False, linewidth=2, color="g")
pic.axes.add_patch(patch)

show()

print("------------------------------------------------------------")  # 60個

plt.plot([9, 9.2, 9.6, 9.2, 6.7, 7, 7.6], [9.0, 9.2, 9.2, 9.2, 7.1, 7.4, 7.5], "yx")
plt.plot(
    [7.2, 7.3, 7.2, 7.3, 7.2, 7.3, 7.3], [10.3, 10.5, 9.2, 10.2, 9.7, 10.1, 10.1], "g."
)
plt.plot([7], [9], "r^")

circle1 = plt.Circle((7, 9), 1.2, color="#aaaaaa")
plt.gcf().gca().add_artist(circle1)
plt.axis([6, 11, 6, 11])

plt.xlabel("W cm")
plt.ylabel("H cm")
plt.legend(("Orange", "Lemons"), loc="upper right")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

class1 = np.array([[1, 1], [1, 3], [2, 1], [1, 2], [2, 2]])
class2 = np.array([[4, 4], [5, 5], [5, 4], [5, 3], [4, 5], [6, 4]])

plt.title("畫圖範例1")

ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(class1[:, 0], class1[:, 1], marker="o")
plt.scatter(class2[:, 0], class2[:, 1], marker="s")

plt.plot([1, 5], [5, 1], "r-")
plt.arrow(4, 4, -1, -1, shape="full", color="r")

plt.plot([3, 3], [0.5, 6], "b--")
plt.arrow(4, 4, -1, 0, shape="full", color="b", linestyle="--")

plt.annotate(
    r"margin 1",
    xy=(3.5, 4),
    xycoords="data",
    xytext=(3.1, 4.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.annotate(
    r"margin 2",
    xy=(3.5, 3.5),
    xycoords="data",
    xytext=(4, 3.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.annotate(
    r"support vector",
    xy=(4, 4),
    xycoords="data",
    xytext=(5, 4.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.annotate(
    r"support vector",
    xy=(2, 2),
    xycoords="data",
    xytext=(0.5, 1.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

show()

print("------------------------------")  # 30個

plt.title("畫圖範例2")

ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(class1[:, 0], class1[:, 1], marker="o")
plt.scatter(class2[:, 0], class2[:, 1], marker="s")

plt.plot([1, 5], [5, 1], "-r")
plt.plot([0, 4], [4, 0], "--b", [2, 6], [6, 2], "--b")

plt.arrow(4, 4, -1, -1, shape="full", color="b")

plt.annotate(
    r"$w^T x + b = 0$",
    xy=(5, 1),
    xycoords="data",
    xytext=(6, 1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.annotate(
    r"$w^T x + b = 1$",
    xy=(6, 2),
    xycoords="data",
    xytext=(7, 2),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.annotate(
    r"$w^T x + b = -1$",
    xy=(3.5, 0.5),
    xycoords="data",
    xytext=(4.5, 0.2),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.annotate(
    r"d",
    xy=(3.5, 3.5),
    xycoords="data",
    xytext=(2, 4.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.annotate(
    r"A",
    xy=(4, 4),
    xycoords="data",
    xytext=(5, 4.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs  # 集群資料集

plt.suptitle("畫圖範例3")

plt.subplot(121)

X, y = make_blobs(
    n_samples=100,
    n_features=2,
    centers=[(1, 1), (2, 2)],
    random_state=9487,
    shuffle=False,
    cluster_std=0.4,
)

ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], marker="o")
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], marker="s")
plt.plot([0.5, 2.5], [2.5, 0.5], "-r")

plt.subplot(122)

class1 = np.array([[1, 1], [1, 3], [2, 1], [1, 2], [2, 2], [1.5, 1.5], [1.2, 1.7]])
class2 = np.array(
    [[4, 4], [5, 5], [5, 4], [5, 3], [4, 5], [6, 4], [5.5, 3.5], [4.5, 4.5], [2, 1.5]]
)

ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(class1[:, 0], class1[:, 1], marker="o")
plt.scatter(class2[:, 0], class2[:, 1], marker="s")
plt.plot([1, 5], [5, 1], "-r")
plt.plot([0, 4], [4, 0], "--b", [2, 6], [6, 2], "--b")
plt.arrow(2, 1.5, 2.25, 2.25, shape="full", color="b")
plt.annotate(
    r"violate margin rule.",
    xy=(2, 1.5),
    xycoords="data",
    xytext=(0.2, 0.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"normal sample. $\epsilon = 0$",
    xy=(4, 5),
    xycoords="data",
    xytext=(4.5, 5.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"$\epsilon > 0$",
    xy=(3, 2.5),
    xycoords="data",
    xytext=(3, 1.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.title("畫圖範例4")

plt.xlabel("$y^{(i)} (w^T x^{(i)} + b)$")
plt.ylabel("Cost")

ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.plot([0, 1], [1.5, 0], "-r")
plt.plot([1, 3], [0.015, 0.015], "-r")
plt.annotate(
    r"$J_i = R \epsilon_i$ for $y^{(i)} (w^T x^{(i)} + b) \geq 1 - \epsilon_i$",
    xy=(0.7, 0.5),
    xycoords="data",
    xytext=(1, 1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"$J_i = 0$ for $y^{(i)} (w^T x^{(i)} + b) \geq 1$",
    xy=(1.5, 0),
    xycoords="data",
    xytext=(1.8, 0.2),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

class1 = np.array([[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [3, 2], [4, 1], [5, 1]])
class2 = np.array(
    [[2.2, 4], [1.5, 5], [1.8, 4.6], [2.4, 5], [3.2, 5], [3.7, 4], [4.5, 4.5], [5.4, 3]]
)

plt.subplot(121)

plt.yticks(())
plt.xlabel("X1")
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")

plt.scatter(class1[:, 0], np.zeros(class1[:, 0].shape[0]) + 0.05, marker="o")
plt.scatter(class2[:, 0], np.zeros(class2[:, 0].shape[0]) + 0.05, marker="s")

plt.subplot(122)

plt.xlabel("X1")
plt.ylabel("X2")
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(class1[:, 0], class1[:, 1], marker="o")
plt.scatter(class2[:, 0], class2[:, 1], marker="s")
plt.plot([1, 5], [3.8, 2], "-r")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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

# plt.title("標題在特定位置", size="x-large", y=-0.1)

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
