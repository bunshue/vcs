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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#绘制带箭头的曲线

import pylab as pl
import matplotlib

t = np.linspace(0, 2*np.pi, 1000)
x = np.sin(2 * t)
y = np.cos(3 * t)

def add_arrows(line, n, arrow_size=7):
    ax = line.axes
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    x, y = line.get_data()

    mask = (xmin < x) & (x < xmax) & (ymin < y) & (y < ymax)

    index = np.nonzero(mask)[0]
    curves = [(x[ind], y[ind]) for ind in np.split(index, np.where(np.diff(index) > 1)[0] + 1)]
    curves_lengths = [np.cumsum(np.hypot(np.diff(xc), np.diff(yc))) for xc, yc in curves]
    total_length = sum([lengths[-1] for lengths in curves_lengths])
    step = total_length / n
    arrows = []

    for (x, y), lengths in zip(curves, curves_lengths):
        count = max(int(lengths[-1] / step), 3)
        location = np.linspace(0, lengths[-1], count)[1:-1]
        index = np.searchsorted(lengths, location)

        dx = x[index + 1] - x[index]
        dy = y[index + 1] - y[index]
        ds = np.hypot(dx, dy)
        dx /= ds
        dy /= ds

        arrows.extend(zip(x[index], y[index], dx, dy))

    x, y, u, v = zip(*arrows)

    return ax.quiver(x, y, u, v,
              units="dots", scale_units="dots", 
              angles="xy", scale=1.0/arrow_size, pivot="middle",
              edgecolors="black", linewidths=1,
              width=1, headwidth=arrow_size*0.5, 
              headlength=arrow_size, headaxislength=arrow_size, 
              zorder=100)

fig, axes = pl.subplots(1, 2, figsize=(12, 4))
line0, = axes[0].plot(x, y)
line1, = axes[1].plot(x, y)

axes[1].set_xlim(-0.8, 0.8)
axes[1].set_ylim(-0.8, 0.8)

add_arrows(line0, 20)
add_arrows(line1, 20)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 绘制超过浮点数范围的对数轴

import sympy

plt.plot([0, 1, 2], [sympy.Float('1e-20'), sympy.Float('1e-100'), sympy.Float('1e-700')])
plt.yscale('log')
show()

from matplotlib.ticker import FuncFormatter, Locator
x = [0, 1, 2]
y = [sympy.Float('1e-20'), sympy.Float('1e-100'), sympy.Float('1e-700')]

def log_formatter(x, pos):
    return "$10^{{{:d}}}$".format(int(x))

class LogMinorLocator(Locator):
    def __call__(self):
        majorlocs = self.axis.get_majorticklocs()
        step = majorlocs[1] - majorlocs[0]
        res = majorlocs[:, None] + np.log10(np.linspace(1, 0.1, 10)) * step
        return res.ravel()

formatter = FuncFormatter(log_formatter)

fig, ax = plt.subplots(figsize=(10, 5))
y2 = list(map(lambda x:sympy.log(x, 10), y))
ax.plot(x, y2)
ax.minorticks_on()
ax.yaxis.set_major_formatter(formatter)
ax.yaxis.set_minor_locator(LogMinorLocator())
ax.grid()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 用matplotlib和OpenCV制作动画视频

# matplotlib.animation中提供了制作动画视频的类，但是这些类都是首先将图表保存为图像文件，然后使用视频工具生成视频。本文介绍使用OpenCV中的VideoWriter直接将图表的绘图内存保存为视频文件。

import pylab as pl
import numpy as np
import cv2
from matplotlib.collections import LineCollection
from scipy.spatial.distance import squareform, pdist

# 建立視訊編碼 fourcc
fourcc = cv2.VideoWriter_fourcc(*"MPEG")
out = None # 建立影像寫入器 out
video_fps = 25

N = 100
x, y = np.random.uniform(-2, 2, (2, N))
vx, vy = np.random.randn(2, N) * 0.01
fig, ax = pl.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
scatter = ax.scatter(x, y, 10, zorder=100)
line_collection = LineCollection([[(0, 0), (1, 1)]])
line_collection.set_cmap("gray")
ax.add_collection(line_collection)
fig.canvas.draw()
ax.axis("off")
canvas_map = np.asarray(fig.canvas.renderer._renderer)[:, :, 2::-1]
arrs = []

# 300張圖 
for i in range(300):
    x += vx
    y += vy
    vx[(x < -2) | (x > 2)] *= -1
    vy[(y < -2) | (y > 2)] *= -1
    scatter.set_offsets(np.c_[x, y])
    
    points = np.c_[x, y]
    dist = squareform(pdist(points))
    i0, i1 = np.where(dist < 0.5)
    mask = i0 != i1
    i0 = i0[mask]
    i1 = i1[mask]
    lines = np.concatenate((points[i0], points[i1]), axis=-1).reshape(-1, 2, 2)
    line_collection.set_segments(lines)
    length = ((lines[:, 1, :] - lines[:, 0, :])**2).sum(axis=-1)**0.5
    line_collection.set_array(length)
    fig.canvas.draw()
    if out is None:
        # 建立影像寫入器 out
        out = cv2.VideoWriter("tmp_matplotlib_movie.avi", fourcc, video_fps, fig.canvas.get_width_height())
    out.write(canvas_map)
    
out.release()

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
