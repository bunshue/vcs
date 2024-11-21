"""
新進測試

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
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

import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

print("------------------------------------------------------------")  # 60個

# 柱狀圖參數調整

# 數據
categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 25]

# 設定圖形大小和分辨率
plt.figure(figsize=(10, 5), dpi=100)

# 繪製柱狀圖並自定義參數
plt.bar(
    categories,
    values,
    color="skyblue",
    edgecolor="black",
    linewidth=1.5,
    hatch="/",
    width=0.5,
    label="數據1",
)

# 設定標題和標籤
plt.title("22柱狀圖示例")
plt.xlabel("類別")
plt.ylabel("值")

# 設定刻度標籤
plt.xticks(categories)
plt.yticks([0, 5, 10, 15, 20, 25])

# 顯示網格線
plt.grid(True)

# 顯示圖例
plt.legend()

# 顯示圖形
plt.show()

print("------------------------------------------------------------")  # 60個

"""
參數說明
顏色和樣式
color：設定柱子的顏色，可以是一個顏色或一個顏色列表。
edgecolor：設定柱子邊框的顏色。
linewidth：設定柱子邊框的寬度。
hatch：設定柱子的圖案填充，例如 '/'（斜線），'\\'（反斜線），'|'（垂直線），'-'（水平線）。
柱子的寬度
width：設定柱子的寬度。
刻度和網格
plt.xticks() 和 plt.yticks()：設定刻度標籤。
plt.grid()：顯示或隱藏網格線。
圖形大小和分辨率
plt.figure(figsize=(width, height), dpi=dpi)：設定圖形大小和分辨率。
"""

print("------------------------------------------------------------")  # 60個

# 散點圖參數調整

# 數據
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
sizes = [50, 100, 150, 200, 250]
colors = [1, 2, 3, 4, 5]

# 設定圖形大小和分辨率
plt.figure(figsize=(10, 5), dpi=100)

# 繪製散點圖並自定義參數
plt.scatter(
    x, y, s=sizes, c=colors, alpha=0.6, edgecolor="black", linewidth=1.5, label="數據1"
)

# 設定標題和標籤
plt.title("44散點圖示例")
plt.xlabel("X軸")
plt.ylabel("Y軸")

# 設定刻度標籤
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([2, 3, 5, 7, 11])

# 顯示網格線
plt.grid(True)

# 顯示圖例
plt.legend()

# 顯示圖形
plt.colorbar()  # 顯示顏色條
plt.show()

print("------------------------------------------------------------")  # 60個

"""
參數說明
顏色和樣式
color：設定點的顏色，可以是一個顏色或一個顏色列表。
c：設定點的顏色，可以使用單一顏色或一個數值序列來根據數值著色。
marker：設定標記樣式，例如 'o'（圓點），'s'（正方形），'^'（三角形）。
大小
s：設定點的大小，可以是一個數值或一個數值列表。
透明度
alpha：設定點的透明度，範圍從0（完全透明）到1（完全不透明）。
邊框
edgecolor：設定點的邊框顏色。
linewidth：設定點的邊框寬度。
刻度和網格
plt.xticks() 和 plt.yticks()：設定刻度標籤。
plt.grid()：顯示或隱藏網格線。
圖形大小和分辨率
plt.figure(figsize=(width, height), dpi=dpi)：設定圖形大小和分辨率。
"""

print("------------------------------------------------------------")  # 60個

# 繪製餅圖
# plt.pie(sizes, labels=labels, autopct='%1.1f%%')

print("------------------------------------------------------------")  # 60個

"""
autopct='%1.1f%%' 的解釋

autopct 參數用來控制餅圖上顯示的自動百分比標籤。這個參數接受一個字符串格式或一個函數，用來指定如何顯示每個餅圖部分的百分比。

%1.1f：這是一個格式化字符串，用來指定浮點數的格式。

%：這是格式化操作的開始標誌。用來指示如何格式化後面的數值。
1：這表示總共顯示至少1個字符（包括小數點和小數位）。
.1：這表示顯示1位小數。
f：這表示以浮點數格式顯示數值。
%%：這表示一個百分號。由於百分號在格式字符串中有特別的意義，所以需要用兩個百分號來表示一個實際的百分號。
"""
print("------------------------------------------------------------")  # 60個

# 圓餅圖參數調整

# 數據
labels = ["A", "B", "C", "D"]
sizes = [15, 30, 45, 10]
colors = ["gold", "yellowgreen", "lightcoral", "lightskyblue"]
explode = (0, 0.1, 0, 0)  # 將第二塊分離出來

# 繪製圓餅圖並自定義參數
plt.figure(figsize=(8, 8))
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90,
    pctdistance=0.85,
    wedgeprops={"edgecolor": "black"},
)

# 設置標題
plt.title("66圓餅圖示例")

# 顯示圖形
plt.show()

print("------------------------------------------------------------")  # 60個

"""
參數說明
顏色
colors：設定各個部分的顏色，可以是一個顏色列表。
起始角度
startangle：設定第一塊的起始角度，以度數為單位。
比例顯示
autopct：設定每塊的比例顯示格式，例如 '%1.1f%%' 表示保留一位小數的百分比。
分離圓餅塊
explode：設定分離圓餅塊的距離，默認為0。如果要將某塊突出顯示，可以設置一個數值列表，其中需要分離的塊設置為大於0的值。
陰影
shadow：設置是否顯示陰影，取值為布林值。
圓餅比例
pctdistance：設定比例文字距離圓心的距離，默認為0.6。
圓形或扁平化
normalize：設置是否將數據標準化，使得總和為1。如果為 False，數據不會被標準化。
圓餅中心空白
wedgeprops：設置圓餅塊的屬性，例如邊框顏色、寬度等。
"""

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

plt.show()

print("------------------------------------------------------------")  # 60個

Z = np.random.uniform(0, 1, (8, 8))
plt.imshow(Z)

plt.show()

print("------------------------------------------------------------")  # 60個

Z = np.random.uniform(0, 1, (8, 8))
plt.contourf(Z)

plt.show()

print("------------------------------------------------------------")  # 60個

Z = np.random.normal(0, 1, 100)
plt.hist(Z)

plt.show()

print("------------------------------------------------------------")  # 60個

# Create an error bar plot
X = np.arange(5)
Y = np.random.uniform(0, 1, 5)
plt.errorbar(X, Y, Y / 4)

plt.show()

print("------------------------------------------------------------")  # 60個

# Create a box plot
Z = np.random.normal(0, 1, (100, 3))
plt.boxplot(Z)

plt.show()

print("------------------------------------------------------------")  # 60個

# Create a figure with two subplots (vertically stacked)
X = np.linspace(0, 10, 100)
Y1, Y2 = np.sin(X), np.cos(X)
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(X, Y1, color="C1")
ax2.plot(X, Y2, color="C0")

plt.show()

print("------------------------------------------------------------")  # 60個

# Create a figure with two subplots (horizontally aligned)
X = np.linspace(0, 10, 100)
Y1, Y2 = np.sin(X), np.cos(X)
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(Y1, X, color="C1")
ax2.plot(Y2, X, color="C0")

plt.show()

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

plt.show()

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

plt.show()

print("------------------------------------------------------------")  # 60個

# Lines & markers

# Generate data and create a plot
X = np.linspace(0.1, 10 * np.pi, 1000)
Y = np.sin(X)
plt.plot(X, Y, "C1o:", markevery=25, mec="1.0")

plt.show()

print("------------------------------------------------------------")  # 60個

# Scales & projections

# Create a figure with a single subplot
fig, ax = plt.subplots()

# Set x-axis scale to logarithmic
ax.set_xscale("log")

# Plot data with specified formatting
ax.plot(X, Y, "C1o-", markevery=25, mec="1.0")

plt.show()

print("------------------------------------------------------------")  # 60個

# Text & ornaments

# Create a figure with a single subplot
fig, ax = plt.subplots()

# Fill the area between horizontal lines with a curve
ax.fill_betweenx([-1, 1], [0], [2 * np.pi])

# Add a text annotation to the plot
ax.text(0, -1, r" Period $\Phi$")

plt.show()

print("------------------------------------------------------------")  # 60個

# Legend

# Create a figure with a single subplot
fig, ax = plt.subplots()

# Plot sine and cosine curves with specified colors and labels
ax.plot(X, np.sin(X), "C0", label="Sine")
ax.plot(X, np.cos(X), "C1", label="Cosine")

# Add a legend with customized positioning and formatting
ax.legend(bbox_to_anchor=(0, 1, 1, 0.1), ncol=2, mode="expand", loc="lower left")

plt.show()

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

plt.show()

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

plt.show()

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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
