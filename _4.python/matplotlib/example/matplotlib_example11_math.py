"""
matplotlib 範例

數學畫圖

"""

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

print("------------------------------------------------------------")  # 60個


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

print("------------------------------------------------------------")  # 60個


x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure(figsize=(12, 8))

plt.plot(x, y2)
# plot the second curve in this figure with certain parameters
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
# set x limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')

# set new sticks
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
plt.show()

print("------------------------------------------------------------")  # 60個

# 6 - axis setting

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure(figsize=(12, 8))

plt.plot(x, y2)
# plot the second curve in this figure with certain parameters
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
# set x limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# set new ticks
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3],
           ['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])
# to use '$ $' for math text and nice looking, e.g. '$\pi$'

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
# ACCEPTS: [ 'top' | 'bottom' | 'both' | 'default' | 'none' ]

ax.spines['bottom'].set_position(('data', 0))
# the 1st is in 'outward' | 'axes' | 'data'
# axes: percentage of y axis
# data: depend on y data

ax.yaxis.set_ticks_position('left')
# ACCEPTS: [ 'left' | 'right' | 'both' | 'default' | 'none' ]

ax.spines['left'].set_position(('data',0))
plt.show()

print("------------------------------------------------------------")  # 60個

# 7 - legend

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure(figsize=(12, 8))

# set x limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# set new sticks
new_sticks = np.linspace(-1, 2, 5)
plt.xticks(new_sticks)
# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

l1, = plt.plot(x, y2, label='linear line')
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='square line')

# plt.legend(loc='upper right')
plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')
# the "," is very important in here l1, = plt... and l2, = plt... for this step
"""legend( handles=(line1, line2, line3),
           labels=('label1', 'label2', 'label3'),
           'upper right')
    The *loc* location codes are::

          'best' : 0,          (currently not supported for figure legends)
          'upper right'  : 1,
          'upper left'   : 2,
          'lower left'   : 3,
          'lower right'  : 4,
          'right'        : 5,
          'center left'  : 6,
          'center right' : 7,
          'lower center' : 8,
          'upper center' : 9,
          'center'       : 10,"""

plt.show()

print("------------------------------------------------------------")  # 60個

#8_annotation.py

x = np.linspace(-3, 3, 50)
y = 2*x + 1

plt.figure(num=1, figsize=(8, 5),)

plt.plot(x, y,)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2*x0 + 1
plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)
plt.scatter([x0, ], [y0, ], s=50, color='b')

# method 1:
#####################
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

# method 2:
########################
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})

plt.show()

print("------------------------------------------------------------")  # 60個

#9_tick_visibility.py

x = np.linspace(-3, 3, 50)
y = 0.1*x

plt.figure(figsize=(12, 8))

plt.plot(x, y, linewidth=10)
plt.ylim(-2, 2)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))
plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




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

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

