"""
極座標系 繪圖


"""

import matplotlib

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
'''
plt.figure(
    num="plot 集合 1 函數曲線",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

r = 3
t = np.linspace(-2 * np.pi, 2 * np.pi, 200)
x = r * np.cos(t)
y = r * np.sin(t)


ax = plt.gca()
ax.set_aspect("equal")

plt.plot(x, y, lw=3)


# 第二張圖
plt.subplot(232)

r = np.sin(5 * t)
x = r * np.cos(t)
y = r * np.sin(t)

ax = plt.gca()
ax.set_aspect("equal")

plt.plot(x, y, lw=3)


# 第三張圖
plt.subplot(233)


pi = 3.14159
r = 3
t = np.linspace(-1 * pi, 1 * pi, 50)

x = r * np.cos(t)
y = r * np.sin(t)


r = 3 * (1 - np.sin(t))
x = r * np.cos(t)
y = r * np.sin(t)

plt.plot(x, y, lw=3)


# 第四張圖
plt.subplot(234)


# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)


plt.show()


print("------------------------------------------------------------")  # 60個

ax = plt.subplot(projection="polar")
r = np.arange(0, 1, 0.001)
theta = 2 * 2 * np.pi * r
ax.plot(theta, r, "m", lw=3)
plt.title("極座標圖表", fontsize=16)

plt.show()

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
np.random.seed(10)  # 設定種子值
N = 100
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 150 * r**2
colors = theta
plt.subplot(projection="polar")
plt.scatter(theta, r, c=colors, s=area, cmap="rainbow", alpha=0.8)

plt.show()

print("------------------------------------------------------------")  # 60個

# 散點圖

N = 150
# 產生 150 個 0~2 之間的隨機半徑
r = 2 * np.random.rand(N)
# 產生 150 個 0~2pi 之間的隨機弧度
theta = 2 * np.pi * np.random.rand(N)
# 區域大小與半徑成正比
area = 50 * r**2
# 顏色由弧度決定
colors = theta

ax = plt.subplot(211)
c = ax.scatter(theta, r, c=colors, s=area, cmap="hsv", alpha=0.75)

# 畫出極座標圖，此時的 x 為弧度，y 為半徑
ax = plt.subplot(212, projection="polar")
c = ax.scatter(theta, r, c=colors, s=area, cmap="hsv", alpha=0.75)

plt.show()

print("------------------------------------------------------------")  # 60個

ax = plt.subplot(1, 1, 1, polar=True)

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

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = fig.add_subplot(projection="polar")
r = np.linspace(0, 1, 1000)
theta = 2 * 2 * np.pi * r
ax.plot(theta, r, color="g", lw=3)

i = 500
radius, thistheta = r[i], theta[i]
ax.plot([thistheta], [radius], "o")  # 指定位置繪點
ax.annotate(
    "極座標文字註解",
    xy=(thistheta, radius),  # theta, radius
    xytext=(0.8, 0.2),  # 百分比
    color="b",  # 藍色
    textcoords="figure fraction",  # 座標格式是百分比
    arrowprops=dict(arrowstyle="->", color="m"),
    horizontalalignment="left",
    verticalalignment="bottom",
)

plt.show()

print("------------------------------------------------------------")  # 60個

N = 20  # 長條個數
theta = np.linspace(0.0, 2 * np.pi, N)  # 角度個數
radius = 10 * np.random.rand(N)  # 半徑個數
width = np.pi / 4 * np.random.rand(N)  # 寬度個數
colors = plt.cm.hsv(radius / 10)  # 色彩個數

ax = plt.subplot(projection="polar")  # 建立子圖

print(theta)
print(radius)
print(width)

# 繪製極座標長條圖
ax.bar(theta, radius, width, bottom=0.0, alpha=0.8, color=colors)

plt.show()

print("------------------------------------------------------------")  # 60個

ax = plt.subplot(projection="polar")
r = np.arange(0, 1, 0.001)
theta = 2 * 2 * np.pi * r
ax.plot(theta, r, "m", lw=3)
plt.title("極座標圖表", fontsize=16)
plt.tight_layout()  # 圖表標題可以緊縮佈局

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi, 300)
y = np.sin(x)
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection="polar"))
ax1.plot(x, y)
ax1.set_title("極座標 Sin 圖", fontsize=12)
ax2.plot(x, y**2)
ax2.set_title("極座標 Sin 平方圖", fontsize=12)
plt.tight_layout()  # 緊縮佈局
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

pts = 12
theta = np.linspace(0, 2 * np.pi, pts, endpoint=False)
r = 50 * np.random.rand(pts)
"""
plt.polar(theta,r)
plt.polar(theta,r,'-',marker='*',color='g')
plt.polar(theta,r,'--',marker='D',color='m')
"""
plt.polar(theta, r, "*", color="b", markersize=10)

plt.show()

print("------------------------------------------------------------")  # 60個

a = 6  # 主軸半徑
b = 3  # 次軸半徑

radian = np.arange(0, (2 * np.pi), 0.01)
for rad in radian:
    r = (a * b) / np.sqrt((a * np.sin(rad)) ** 2 + (b * np.cos(rad)) ** 2)
    plt.polar(rad, r, "b.")
plt.show()

print("------------------------------------------------------------")  # 60個

radian = np.arange(0, (2 * np.pi), 0.01)
for r in range(1, 3):
    for rad in radian:
        plt.polar(rad, r, "b.")
plt.show()

print("------------------------------------------------------------")  # 60個

radian = np.arange(0, (6 * np.pi), 0.01)
for rad in radian:
    r = rad
    plt.polar(rad, r, "b.")
plt.show()

print("------------------------------------------------------------")  # 60個

a = 1
radian = np.arange(0, (6 * np.pi), 0.01)
for rad in radian:
    r = a + (a * np.cos(rad))
    # r =  a - (a*np.sin(rad))
    plt.polar(rad, r, "r.")
plt.show()

print("------------------------------------------------------------")  # 60個

print("螺旋圖")

plt.figure(figsize=(6, 6))  # 圖像大小[英吋]

ax = plt.axes([0.1, 0.1, 0.8, 0.8], polar=True)

t = np.arange(-4 * np.pi, 4 * np.pi, 0.1)
plt.polar(t, 1.19**t, linewidth=2)

xt, yt = plt.xticks()[0], plt.yticks()[0]

plt.xticks(xt, ["" for q in range(len(xt))])
plt.yticks(yt, ["" for q in range(len(yt))])

plt.show()
'''
print("------------------------------------------------------------")  # 60個

# 極座標圖

# 極座標中的圓、螺旋線和玫瑰線
theta = np.arange(0, 2 * np.pi, 0.02)

plt.subplot(121, polar=True)
plt.plot(theta, 1.6 * np.ones_like(theta), linewidth=2)
plt.plot(3 * theta, theta / 3, "--", linewidth=2)

plt.subplot(122, polar=True)
plt.plot(theta, 1.4 * np.cos(5 * theta), "--", linewidth=2)
plt.plot(theta, 1.8 * np.cos(4 * theta), linewidth=2)
plt.rgrids(np.arange(0.5, 2, 0.5), angle=45)
plt.thetagrids([0, 45])

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
