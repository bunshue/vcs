"""


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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

x = np.linspace(0.0, np.pi, 500)
y = np.cos(2 * np.pi * x)
plt.plot(x, y, "m", lw=2)
plt.annotate(
    "局部極大值",
    xy=(2, 1),
    xytext=(2.5, 1.2),
    arrowprops=dict(arrowstyle="->", facecolor="black"),
)
plt.annotate(
    "局部極小值", xy=(1.5, -1), xytext=(2.0, -1.25), arrowprops=dict(arrowstyle="-")
)
plt.text(0.8, 1.2, "Annotate的應用", fontsize=20, color="b")
plt.ylim(-1.5, 1.5)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0.0, np.pi, 500)
y = np.cos(2 * np.pi * x)
plt.plot(x, y, "m", lw=2)
plt.annotate(
    "局部極大值",
    xy=(2, 1),
    xytext=(2.5, 1.2),
    arrowprops=dict(facecolor="black", shrink=0.05),
)
plt.ylim(-1.5, 1.5)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0.0, np.pi, 500)
y = np.cos(2 * np.pi * x)
plt.plot(x, y, "m", lw=2)
plt.annotate(
    "局部極大值", xy=(2, 1), xytext=(2.5, 1.2), arrowprops=dict(facecolor="y", shrink=0.05)
)
plt.ylim(-1.5, 1.5)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0.0, np.pi, 500)
y = np.cos(2 * np.pi * x)
plt.plot(x, y, "m", lw=2)
plt.annotate("局部極大值", xy=(2, 1), xytext=(2.5, 1.2), arrowprops=dict(shrink=0.05))
plt.ylim(-1.5, 1.5)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0.0, np.pi, 500)
y = np.cos(2 * np.pi * x)
plt.plot(x, y, "m", lw=2)
plt.annotate(
    "局部極大值", xy=(2, 1), xytext=(2.5, 1.2), arrowprops=dict(ec="g", fc="g", shrink=0.05)
)
# arrowprops = dict(color = 'g', shrink = 0.05))
plt.ylim(-1.5, 1.5)

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(figsize=(4, 4))
ax.annotate(
    "Annotate",
    xy=(0.2, 0.2),
    xytext=(0.7, 0.8),
    arrowprops=dict(arrowstyle="->", connectionstyle="arc"),
)

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(figsize=(4, 4))
ax.annotate(
    "Annotate",
    xy=(0.2, 0.2),
    xytext=(0.7, 0.8),
    arrowprops=dict(arrowstyle="->", connectionstyle="angle"),
)

plt.show()

print("------------------------------------------------------------")  # 60個


def demo(ax, connectionstyle):
    # 繪製子圖與箭頭樣式說明
    x1, y1 = 0.3, 0.2
    x2, y2 = 0.8, 0.6
    ax.plot([x1, x2], [y1, y2], "g.")
    ax.annotate(
        "",
        xy=(x1, y1),
        xytext=(x2, y2),
        arrowprops=dict(
            arrowstyle="->",
            color="m",
            shrinkA=5,
            shrinkB=5,
            connectionstyle=connectionstyle,
        ),
    )
    ax.text(
        0.1,
        0.96,
        connectionstyle.replace(",", ",\n"),
        transform=ax.transAxes,
        ha="left",
        va="top",
        c="b",
    )


# 主程式開始
fig, axs = plt.subplots(3, 5, figsize=(7, 6.2))
demo(axs[0, 0], "angle3,angleA=90,angleB=0")
demo(axs[1, 0], "angle3,angleA=0,angleB=90")
demo(axs[0, 1], "angle,angleA=-90,angleB=180,rad=0")
demo(axs[1, 1], "angle,angleA=-90,angleB=180,rad=5")
demo(axs[2, 1], "angle,angleA=-90,angleB=10,rad=5")
demo(axs[0, 2], "arc3,rad=0.")
demo(axs[1, 2], "arc3,rad=0.3")
demo(axs[2, 2], "arc3,rad=-0.3")
demo(axs[0, 3], "arc,angleA=-90,angleB=0,armA=30,armB=30,rad=0")
demo(axs[1, 3], "arc,angleA=-90,angleB=0,armA=30,armB=30,rad=5")
demo(axs[2, 3], "arc,angleA=-90,angleB=0,armA=0,armB=40,rad=0")
demo(axs[0, 4], "bar,fraction=0.3")
demo(axs[1, 4], "bar,fraction=-0.3")
demo(axs[2, 4], "bar,angle=180,fraction=-0.3")
# 取消刻度標記與標籤
for ax in axs.flat:
    ax.set(xlim=(0, 1), ylim=(0, 1.25), xticks=[], yticks=[])
plt.tight_layout()  # 緊縮佈局

plt.show()

print("------------------------------------------------------------")  # 60個

plt.subplots(figsize=(4, 4))
plt.annotate(
    "Simple",
    xy=(0.2, 0.2),
    xytext=(0.7, 0.8),
    size=20,
    va="center",
    ha="center",
    color="b",
    arrowprops=dict(arrowstyle="simple", color="g", connectionstyle="arc3,rad=-0.3"),
)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.subplots(figsize=(4, 4))
plt.annotate(
    "fancy",
    xy=(0.2, 0.2),
    xytext=(0.7, 0.8),
    size=20,
    va="center",
    ha="center",
    color="b",
    bbox=dict(boxstyle="round4", fc="lightyellow"),
    arrowprops=dict(arrowstyle="fancy", color="g", connectionstyle="arc3,rad=-0.3"),
)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.subplots(figsize=(4, 4))
plt.annotate(
    "wedge",
    xy=(0.2, 0.2),
    xytext=(0.7, 0.8),
    size=20,
    va="center",
    ha="center",
    color="b",
    bbox=dict(boxstyle="round4", fc="lightyellow"),
    arrowprops=dict(arrowstyle="wedge", color="g", connectionstyle="arc3,rad=-0.3"),
)
plt.annotate(
    "wedge",
    xy=(0.2, 0.2),
    xytext=(0.7, 0.8),
    size=20,
    va="center",
    ha="center",
    color="b",
    bbox=dict(boxstyle="round4", fc="lightyellow"),
    arrowprops=dict(arrowstyle="wedge", color="m", connectionstyle="arc3,rad=0.3"),
)

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure(figsize=(6, 4), dpi=100)  # 設置繪製對象大小
plt.style.use("ggplot")  # 設置顯示風格

plt.plot([12, 13, 45, 15, 16], label="label1")  # 繪圖及設置圖例文字
plt.annotate(
    "local max",
    xy=(2, 45),
    xytext=(3, 45),
    arrowprops=dict(facecolor="black", shrink=0.05),
)  # 繪製帶箭頭的標註
x = np.arange(0, 6)
y = x * x
plt.plot(x, y, marker="o", label="label2")  # 繪圖及設置圖例文字
for xy in zip(x, y):
    plt.annotate(
        "(%s,%s)" % xy, xy=xy, xytext=(-20, 10), textcoords="offset points"  # 繪製標註
    )
plt.text(4.5, 10, "Draw text", fontsize=20)  # 在位置0,20繪製文字

plt.legend(loc="upper left")  # 在左上角顯示圖例
plt.xlabel("x value")  # 設置x軸上的標籤
plt.ylabel("y value")  # 設置y軸上的標籤
plt.xlim(-0.5, 7)  # 設置x軸範圍
plt.ylim(-5, 50)  # 設置y軸範圍

plt.show()

# 顯示繪製對象的各個屬性值, many
# import matplotlib
# print(matplotlib.artist.getp(fig.patch))

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
