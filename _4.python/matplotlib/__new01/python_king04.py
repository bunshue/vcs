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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

def show():
    # pass
    plt.tight_layout()  # 緊密排列，並填滿原圖大小
    plt.show()


print("------------------------------------------------------------")  # 60個
'''
x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x)

plt.plot(x, y, color="red")
plt.plot(x, z, "b--")

plt.ylim(-1.2, 1.2)

import io

buf = io.BytesIO()  # 建立一個用來儲存圖形內容的BytesIO物件
plt.savefig(buf, format="png")  # 將圖形以png格式儲存進buf中
cc = buf.getvalue()[:20]  # 顯示圖形內容的前20個位元組
print(cc)

show()

print("------------------------------------------------------------")  # 60個

print("設定線圖的透明度")
x = np.arange(0, 5, 0.1)

line = plt.plot(x, 0.05 * x * x, "r")[0]  # plot傳回一個清單
line.set_alpha(0.3)  # 呼叫Line2D物件的set_*()方法設定屬性值

line = plt.plot(x, 0.08 * x * x, "r")[0]  # plot傳回一個清單
line.set_alpha(0.6)  # 呼叫Line2D物件的set_*()方法設定屬性值

line = plt.plot(x, 0.10 * x * x, "r")[0]  # plot傳回一個清單
line.set_alpha(0.9)  # 呼叫Line2D物件的set_*()方法設定屬性值

show()

print("------------------------------------------------------------")  # 60個

from matplotlib import style

print(style.available)

style.use("ggplot")  # 使用ggplot型態繪圖

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x,y)

show()

print("------------------------------------------------------------")  # 60個

#在圖表中顯示中文

from matplotlib.font_manager import fontManager

cc = fontManager.ttflist[:6]
print(cc)

print(fontManager.ttflist[0].name)
print(fontManager.ttflist[0].fname)

plt.close("all")

# 顯示系統中所有的中文字型名

fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111)
plt.subplots_adjust(0, 0, 1, 1, 0, 0)
plt.xticks([])
plt.yticks([])
x, y = 0.05, 0.05
fonts = [font.name for font in fontManager.ttflist if 
             os.path.exists(font.fname) and os.stat(font.fname).st_size>1e6]
font = set(fonts)
dy = (1.0 - y) / (len(fonts) // 4 + (len(fonts)%4 != 0))

for font in fonts:
    t = ax.text(x, y + dy / 2, u"中文字型", 
                {'fontname':font, 'fontsize':14}, transform=ax.transAxes)
    ax.text(x, y, font, {'fontsize':12}, transform=ax.transAxes)
    x += 0.25
    if x >= 1.0:
        y += dy
        x = 0.05

show()

print("------------------------------------------------------------")  # 60個

from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("時間", fontproperties=font)
plt.ylabel("振幅", fontproperties=font)
plt.title("正弦波", fontproperties=font)

show()

print("------------------------------------------------------------")  # 60個

#Artist物件

fig = plt.figure()

#新增軸, 水平 : 0.15~0.7, 垂直 : 0.1~0.3
ax = fig.add_axes([0.15, 0.1, 0.7, 0.3])

line = ax.plot([1, 2, 3], [1, 2, 1])[0]  # 傳回的是只有一個元素的清單
print(line is ax.lines[0])

ax.set_xlabel("水平軸")
ax.set_ylabel("垂直軸")
print("ax.xaxis:", ax.xaxis)
print('ax.xaxis.label:', ax.xaxis.label)
print('ax.xaxis.label._text :', ax.xaxis.label._text)

cc = ax.get_xaxis().get_label().get_text()
print('x軸 :', cc)
cc = ax.get_yaxis().get_label().get_text()
print('y軸 :', cc)

show()

print("------------------------------------------------------------")  # 60個

#Artist的屬性

fig = plt.figure()
fig.patch.set_color("g") # 設定背景彩色為綠色

line = plt.plot([1, 2, 3, 2, 1], lw=4)[0]
line.set_alpha(0.5)

show()

line.set(alpha=0.5, zorder=2)

show()

cc = plt.getp(fig.patch)
print(cc)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

fig = plt.figure()

ax1 = fig.add_subplot(211)
ax2 = fig.add_axes([0.1, 0.1, 0.7, 0.3])

print(ax1 in fig.axes and ax2 in fig.axes)

show()

for ax in fig.axes:
    ax.grid(True)

from matplotlib.lines import Line2D

fig = plt.figure()
line1 = Line2D(
    [0, 1], [0, 1], transform=fig.transFigure, figure=fig, color="r")
line2 = Line2D(
    [0, 1], [1, 0], transform=fig.transFigure, figure=fig, color="g")
fig.lines.extend([line1, line2])

show()

print("------------------------------------------------------------")  # 60個

#Axes容器

fig = plt.figure()
ax = fig.add_subplot(111)
ax.patch.set_facecolor("green")

x, y = np.random.rand(2, 100)
line = ax.plot(x, y, "-", color="blue", linewidth=2)[0]
cc = line is ax.lines[0]
print(cc)

show()

fig, ax = plt.subplots()
n, bins, rects = ax.hist(np.random.randn(1000), 50, facecolor="blue")
cc = rects[0] is ax.patches[0]
print(cc)

show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots()
rect = plt.Rectangle((1,1), width=5, height=12)

show()

ax.add_patch(rect) # 將rect加入進ax
#cc = rect.get_axes()
#print(cc)

fig, ax = plt.subplots()
t = ax.scatter(np.random.rand(20), np.random.rand(20))
print(t, t in ax.collections)

show()

print("------------------------------------------------------------")  # 60個

#Axis容器

fig, ax = plt.subplots()
axis = ax.xaxis

show()

cc = axis.get_ticklocs()
print(cc)

print(axis.get_ticklabels()) # 獲得刻度標簽清單
print([x.get_text() for x in axis.get_ticklabels()]) # 獲得刻度的文字字串

cc = axis.get_ticklines()
print(cc)

cc = axis.get_ticklines(minor=True) # 獲得副刻度線清單

print(cc)

# 組態X軸的刻度線和刻度文字的型態
for label in axis.get_ticklabels():
    label.set_color("red")
    label.set_rotation(45)
    label.set_fontsize(16)
     
for line in axis.get_ticklines():
    line.set_color("green")
    line.set_markersize(25)
    line.set_markeredgewidth(3)
fig

show()

print(axis.get_minor_locator()) # 計算副刻度位置的物件
print(axis.get_major_locator()) # 計算主刻度位置的物件

print("------------------------------------------------------------")  # 60個

# 組態X軸的刻度線的位置和文字，並開啟副刻度線

from fractions import Fraction
from matplotlib.ticker import MultipleLocator, FuncFormatter

x = np.arange(0, 4*np.pi, 0.01)
fig, ax = plt.subplots(figsize=(8,4))
plt.plot(x, np.sin(x), x, np.cos(x))

def pi_formatter(x, pos):
    frac = Fraction(int(np.round(x / (np.pi/4))), 4)
    d, n = frac.denominator, frac.numerator
    if frac == 0:
        return "0"
    elif frac == 1:
        return "$\pi$"
    elif d == 1:
        return r"${%d} \pi$" % n
    elif n == 1:
        return r"$\frac{\pi}{%d}$" % d
    return r"$\frac{%d \pi}{%d}$" % (n, d)

# 設定兩個座標軸的範圍
plt.ylim(-1.5,1.5)
plt.xlim(0, np.max(x))

# 設定圖的底邊距
plt.subplots_adjust(bottom = 0.15)

# 主刻度為pi/4
ax.xaxis.set_major_locator( MultipleLocator(np.pi/4) )

# 主刻度文字用pi_formatter函數計算
ax.xaxis.set_major_formatter( FuncFormatter( pi_formatter ) )

# 副刻度為pi/20
ax.xaxis.set_minor_locator( MultipleLocator(np.pi/20) )

# 設定刻度文字的大小
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(16)

show()

print("------------------------------------------------------------")  # 60個

# annotate
#座標變換和注解

# 為圖表加入各種注解元素

def func1(x):
    return 0.6*x + 0.3

def func2(x):
    return 0.4*x*x + 0.1*x + 0.2
    
def find_curve_intersects(x, y1, y2):
    d = y1 - y2
    idx = np.where(d[:-1]*d[1:]<=0)[0]
    x1, x2 = x[idx], x[idx+1]
    d1, d2 = d[idx], d[idx+1]
    return -d1*(x2-x1)/(d2-d1) + x1

x = np.linspace(-3,3,100)
f1 = func1(x)
f2 = func2(x)
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(x, f1)
ax.plot(x, f2)

x1, x2 = find_curve_intersects(x, f1, f2)
ax.plot(x1, func1(x1), "o") 
ax.plot(x2, func1(x2), "o")

ax.fill_between(x, f1, f2, where=f1>f2, facecolor="green", alpha=0.5)

from matplotlib import transforms

trans = transforms.blended_transform_factory(ax.transData, ax.transAxes)
ax.fill_between([x1, x2], 0, 1, transform=trans, alpha=0.1)

a = ax.text(0.05, 0.95, u"直線和二次曲線的交點",
    transform=ax.transAxes,
    verticalalignment = "top",
    fontsize = 18,
    bbox={"facecolor":"red","alpha":0.4,"pad":10}
)

arrow = {"arrowstyle":"fancy,tail_width=0.6", 
         "facecolor":"gray", 
         "connectionstyle":"arc3,rad=-0.3"}

ax.annotate(u"交點",
    xy=(x1, func1(x1)), xycoords="data",
    xytext=(0.05, 0.5), textcoords="axes fraction",
    arrowprops = arrow)
                  
ax.annotate(u"交點",
    xy=(x2, func1(x2)), xycoords="data",
    xytext=(0.05, 0.5), textcoords="axes fraction",
    arrowprops = arrow)

xm = (x1+x2)/2
ym = (func1(xm) - func2(xm))/2+func2(xm)
o = ax.annotate(u"直線大於曲線區域",
    xy =(xm, ym), xycoords="data",
    xytext = (30, -30), textcoords="offset points",    
    bbox={"boxstyle":"round", "facecolor":(1.0, 0.7, 0.7), "edgecolor":"none"},
    fontsize=16,
    arrowprops={"arrowstyle":"->"}
)

show()

print("------------------------------------------------------------")  # 60個

#四種座標系

print(type(ax.transData))
ax.transData.transform([(-3,-2), (3,5)])

ax.transAxes.transform([(0,0), (1,1)])

fig.transFigure.transform([(0,0), (1,1)])

inv = ax.transData.inverted()
print(type(inv))
inv.transform((320, 160))

print(ax.set_xlim(-3, 2)) # 設定X軸的範圍為-3到2
print(ax.transData.transform((3, 5))) # 資料座標變換物件已經發生了變化

#使用axvspan()和axhspan()可以快速繪制垂直方向和水平方向上的區間。

#座標變換的管線

cc = fig.dpi_scale_trans == fig.transFigure._boxout._transform
print(cc)

cc = ax.transAxes._boxout._transform == fig.transFigure
print(cc)

cc = ax.get_position()
print(cc)

cc = ax.transAxes._boxout.bounds
print(cc)

print(ax.transLimits.transform((-3, -2)))
print(ax.transLimits.transform((2, 5)))

print(ax.get_xlim()) # 獲得X軸的顯示範圍
print(ax.get_ylim()) # 獲得Y軸的顯示範圍

t = ax.transLimits + ax.transAxes
print(t.transform((0,0)))
print(ax.transData.transform((0,0)))

cc = ax.transScale
print(cc)

#TransformWrapper(BlendedAffine2D(IdentityTransform(),IdentityTransform()))

#由於本例中的X軸的取值範圍是(-3,3)，因此若果將X軸改為對數座標，並且重新繪圖，會產生很多錯誤訊息。

# X軸為對數座標時的transScale物件的內定結構
ax.set_xscale("log") # 將X軸改為對數座標
# dddd %dot GraphvizMPLTransform.graphviz(ax.transScale)
ax.set_xscale("linear") # 將X軸改為線性座標

print("------------------------------------------------------------")  # 60個

#製作陰影效果

from matplotlib import transforms

# 使用座標變換繪制的帶陰影的曲線
fig, ax = plt.subplots()
x = np.arange(0., 2., 0.01)
y = np.sin(2*np.pi*x)

N = 7 # 陰影的條數
for i in range(N, 0, -1):
    offset = transforms.ScaledTranslation(i, -i, transforms.IdentityTransform())
    shadow_trans = plt.gca().transData + offset
    ax.plot(x,y,linewidth=4,color="black", 
        transform=shadow_trans,
        alpha=(N-i)/2.0/N)
    
ax.plot(x,y,linewidth=4,color='black')    
ax.set_ylim((-1.5, 1.5))

show()

cc = offset.transform((0,0)) # 將(0,0)變換為(1,-1)
print(cc)

print(ax.transData.transform((0,0))) # 對(0,0)進行資料座標變換
print(shadow_trans.transform((0,0))) # 對(0,0)進行資料座標變換和偏移變換

print("------------------------------------------------------------")  # 60個

#加入注解

# 三個座標系中的文字
x = np.linspace(-1,1,10)
y = x**2

fig, ax = plt.subplots(figsize=(8,4))
ax.plot(x,y)

for i, (_x, _y) in enumerate(zip(x, y)):
    ax.text(_x, _y, str(i), color="red", fontsize=i+10)

ax.text(0.5, 0.8, u"子圖座標系中的文字", color="blue", ha="center", 
    transform=ax.transAxes)
    
plt.figtext(0.1, 0.92, u"圖表座標系中的文字", color="green")

show()

print("------------------------------------------------------------")  # 60個

from matplotlib import collections as mc

#塊、路徑和集合
#Path與Patch

rect_patch = plt.Rectangle((0, 1), 2, 1)
rect_path = rect_patch.get_path()
print(rect_path.vertices)
print(rect_path.codes)

tran = rect_patch.get_patch_transform()
cc = tran.transform(rect_path.vertices)
print(cc)

ax = plt.gca()

ax.set_aspect("equal")
ax.invert_yaxis()
ax.autoscale()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
X, Y = np.mgrid[-2:2:5j, -2:2:5j]
init_pos = np.c_[X.ravel(), Y.ravel()]
t = np.linspace(0, 5, 50)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5))  # 1X2 子圖
fig.subplots_adjust(0, 0, 1, 1)
ax1.plot(init_pos[:, 0], init_pos[:, 1], "x")
ax2.plot(init_pos[:, 0], init_pos[:, 1], "o")

ax1.autoscale()
ax1.set_aspect("equal")

ax2.autoscale()
ax2.set_aspect("equal")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#多邊形集合(PolyCollection)

# 用PolyCollection繪制大量多邊形
from numpy.random import randint, rand, uniform
from matplotlib import collections as mc

def star_polygon(x, y, r, theta, n, s): 
    angles = np.arange(0, 2*np.pi, 2*np.pi/2/n) + theta
    xs = r * np.cos(angles)
    ys = r * np.sin(angles)
    xs[1::2] *= s
    ys[1::2] *= s
    xs += x
    ys += y
    return np.vstack([xs, ys]).T

stars = []
for i in range(1000):
    star = star_polygon(randint(800), randint(500), 
                        uniform(5, 20), uniform(0, 2*np.pi),
                        randint(3, 9), uniform(0.1, 0.7))
    stars.append(star)

fig, ax = plt.subplots(figsize=(10, 5))
polygons = mc.PolyCollection(stars, alpha=0.5, array=np.random.rand(len(stars)))
ax.add_collection(polygons)# add_collection 只能用 ax
ax.autoscale()
ax.margins(0)
ax.set_aspect("equal")

show()

print("length of facecolors:", len(polygons.get_facecolors()))
print("length of edgecolors:", len(polygons.get_edgecolors()))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#路徑集合(PathCollection)

N = 30
np.random.seed(42)
x = np.random.rand(N)
y = np.random.rand(N)
size = np.random.randint(20, 60, N)
value = np.random.rand(N)

fig, ax = plt.subplots()
pc = ax.scatter(x, y, s=size, c=value)

show()

print(pc.get_transforms().shape)
print(pc.get_transforms()[0]) #索引為0的點對應的縮放矩陣

print(pc.get_offsets()[0]) #索引為0的點對應的中心座標
#計算索引為0的點對應的螢幕座標
print(pc.get_offset_transform().transform(pc.get_offsets())[0])
print(pc.get_offset_transform() is ax.transData)

print(pc.get_transform())

#cc = pc.get_offset_position()
#print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#資料空間中的圓形集合物件

from matplotlib.collections import CircleCollection, Collection
from matplotlib.transforms import Affine2D

class DataCircleCollection(CircleCollection):

    def set_sizes(self, sizes):
        self._sizes = sizes

    def draw(self, render):
        ax = self.axes
        ms = np.zeros((len(self._sizes), 3, 3))
        ms[:, 0, 0] = self._sizes
        ms[:, 1, 1] = self._sizes
        ms[:, 2, 2] = 1
        self._transforms = ms

        m = ax.transData.get_affine().get_matrix().copy()
        m[:2, 2:] = 0
        self.set_transform(Affine2D(m))

        return Collection.draw(self, render)

# 使用DataCircleCollection繪制大量的圓形

data = np.loadtxt("venus-face.csv", delimiter=",", encoding='UTF-8-sig')
offsets = data[:, :2]
sizes = data[:, 2] * 1.05
colors = data[:, 3:] / 256.0

fig, axe = plt.subplots(figsize=(8, 8))
axe.set_rasterized(True)
cc = DataCircleCollection(sizes, facecolors=colors, edgecolors="w", linewidths=0.1,
                          offsets=offsets, transOffset=axe.transData)

axe.add_collection(cc)# add_collection 只能用 ax
axe.axis((0, 512, 512, 0))
axe.axis("off")

show()

print("------------------------------------------------------------")  # 60個

#繪圖函數簡介
#對數座標圖

# 低通濾波器的頻率響應：算術座標（左上）、X軸對數座標（右上）、Y軸對數座標（左下）、雙對數座標（右上） 
w = np.linspace(0.1, 1000, 1000)
p = np.abs(1/(1+0.1j*w)) # 計算低通濾波器的頻率響應

fig, axes = plt.subplots(2, 2)

functions = ("plot", "semilogx", "semilogy", "loglog")

for ax, fname in zip(axes.ravel(), functions):
    func = getattr(ax, fname)
    func(w, p, linewidth=2)
    ax.set_ylim(0, 1.5)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG
#柱狀圖

# 中國男女人口的年齡分佈圖
data = np.loadtxt("china_population.txt", encoding='UTF-8-sig')
width = (data[1,0] - data[0,0])*0.4
c1, c2 = plt.rcParams['axes.color_cycle'][:2]
plt.bar(data[:,0]-width, data[:,1]/1e7, width, color=c1, label=u"男")
plt.bar(data[:,0], data[:,2]/1e7, width, color=c2, label=u"女")
plt.xlim(-width, 100)
plt.xlabel("年齡")
plt.ylabel("人口（千萬）")
plt.legend()

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 四邊形網格

X = np.array([[0, 1, 2], [0, 1, 2]])
Y = np.array([[0, 0.2, 0], [1, 0.8, 1]])
Z = np.array([[0.5, 0.8]])

# 示範pcolormesh()繪制的四邊形以及其填充彩色
plt.plot(X.ravel(), Y.ravel(), "ko")
plt.pcolormesh(X, Y, Z)
plt.margins(0.1)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 使用pcolormesh()繪制復數平面上的座標變換
def make_mesh(n):
    x, y = np.mgrid[-10 : 0 : n * 1j, -5 : 5 : n * 1j]

    s = x + 1j * y
    z = (2 + s) / (2 - s)
    return s, z


fig, axes = plt.subplots(2, 2, figsize=(8, 8))
axes = axes.ravel()
for ax in axes:
    ax.set_aspect("equal")

s1, z1 = make_mesh(10)
s2, z2 = make_mesh(200)
axes[0].pcolormesh(s1.real, s1.imag, np.abs(s1))
axes[1].pcolormesh(z1.real, z1.imag, np.abs(s1))
axes[2].pcolormesh(s2.real, s2.imag, np.abs(s2), rasterized=True)
axes[3].pcolormesh(z2.real, z2.imag, np.abs(s2), rasterized=True)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 使用pcolormesh()繪制極座標中的網格
def func(theta, r):
    y = theta * np.sin(r)
    return np.sqrt(y * y)


T, R = np.mgrid[0 : 2 * np.pi : 360j, 0:10:100j]
Z = func(T, R)

ax = plt.subplot(111, projection="polar", aspect=1.0)
ax.pcolormesh(T, R, Z, rasterized=True)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 箭頭圖


# 用quiver()繪制向量場
def f(x, y):
    return x * np.exp(-(x**2) - y**2)


def vec_field(f, x, y, dx=1e-6, dy=1e-6):
    x2 = x + dx
    y2 = y + dy
    v = f(x, y)
    vx = (f(x2, y) - v) / dx
    vy = (f(x, y2) - v) / dy
    return vx, vy


X, Y = np.mgrid[-2:2:20j, -2:2:20j]
C = f(X, Y)
U, V = vec_field(f, X, Y)
plt.quiver(X, Y, U, V, C)
plt.colorbar()
plt.gca().set_aspect("equal")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
# 使用箭頭表示參數曲線的切線方向
n = 40
arrow_size = 16
t = np.linspace(0, 1, 1000)
x = np.sin(3*2*np.pi*t)
y = np.cos(5*2*np.pi*t)
line, = plt.plot(x, y, lw=1)

lengths = np.cumsum(np.hypot(np.diff(x), np.diff(y)))
length = lengths[-1]
arrow_locations = np.linspace(0, length, n, endpoint=False)
index = np.searchsorted(lengths, arrow_locations)
dx = x[index + 1] - x[index]
dy = y[index + 1] - y[index]
ds = np.hypot(dx, dy)
dx /= ds
dy /= ds
plt.quiver(x[index], y[index], dx, dy, t[index],
          units="dots", scale_units="dots", 
          angles="xy", scale=1.0/arrow_size, pivot="middle",
          edgecolors="black", linewidths=1,
          width=1, headwidth=arrow_size*0.5, 
          headlength=arrow_size, headaxislength=arrow_size, 
          zorder=100)
plt.colorbar()
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
#使用quiver()繪制神經網路結構示意圖
levels = [4, 5, 3, 2]
x = np.linspace(0, 1, len(levels))

for i in range(len(levels) - 1):
    j = i + 1
    n1, n2 = levels[i], levels[j]
    y1, y2 = np.mgrid[0:1:n1*1j, 0:1:n2*1j]
    x1 = np.full_like(y1, x[i])
    x2 = np.full_like(y2, x[j])
    plt.quiver(x1, y1, x2-x1, y2-y1, 
              angles="xy", units="dots", scale_units="xy", 
              scale=1, width=2, headlength=10,
              headaxislength=10, headwidth=4)
    
yp = np.concatenate([np.linspace(0, 1, n) for n in levels])
xp = np.repeat(x, levels)
plt.plot(xp, yp, "o", ms=12)
plt.gca().axis("off")
plt.margins(0.1, 0.1)

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("plt響應滑鼠與鍵碟事件")

# 鍵碟事件

# scpy2.matplotlib.key_event_show_key：顯示觸發鍵碟按鍵事件的按鍵名稱。

fig, ax = plt.subplots()


def on_key_press(event):
    print(event.key)
    sys.stdout.flush()


fig.canvas.mpl_connect("key_press_event", on_key_press)

""" NG
for key, funcs in fig.canvas.callbacks.callbacks.iteritems():
    print(key)
    for cid, wrap in sorted(funcs.items()):
        func = wrap.func
        print("    {0}:{1}.{2}".format(cid, func.__module__, func))
"""
show()

print("------------------------------------------------------------")  # 60個

# scpy2.matplotlib.key_event_change_color：透過按鍵修改曲線的彩色。

fig, ax = plt.subplots()
x = np.linspace(0, 10, 1000)
(line,) = ax.plot(x, np.sin(x))


def on_key_press(event):
    if event.key in "rgbcmyk":
        line.set_color(event.key)
    fig.canvas.draw_idle()


fig.canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)
fig.canvas.mpl_connect("key_press_event", on_key_press)

show()

print("------------------------------------------------------------")  # 60個

# 滑鼠事件

# scpy2.matplotlib.mouse_event_show_info：顯示子圖中的滑鼠事件的各種訊息。

fig, ax = plt.subplots()
text = ax.text(0.5, 0.5, "event", ha="center", va="center", fontdict={"size": 20})


def on_mouse(event):
    global e
    e = event
    info = "{}\nButton:{}\nFig x,y:{}, {}\nData x,y:{:3.2f}, {:3.2f}".format(
        event.name, event.button, event.x, event.y, event.xdata, event.ydata
    )
    text.set_text(info)
    fig.canvas.draw()


fig.canvas.mpl_connect("button_press_event", on_mouse)
fig.canvas.mpl_connect("button_release_event", on_mouse)
fig.canvas.mpl_connect("motion_notify_event", on_mouse)

show()

print("------------------------------------------------------------")  # 60個

# scpy2.matplotlib.mouse_event_move_polygon：示範透過滑鼠搬移Patch物件。

from numpy.random import rand, randint
from matplotlib.patches import RegularPolygon


class PatchMover(object):
    def __init__(self, ax):
        self.ax = ax
        self.selected_patch = None
        self.start_mouse_pos = None
        self.start_patch_pos = None

        fig = ax.figure
        fig.canvas.mpl_connect("button_press_event", self.on_press)
        fig.canvas.mpl_connect("button_release_event", self.on_release)
        fig.canvas.mpl_connect("motion_notify_event", self.on_motion)

    def on_press(self, event):
        patches = self.ax.patches[:]
        patches.sort(key=lambda patch: patch.get_zorder())
        for patch in reversed(patches):
            if patch.contains_point((event.x, event.y)):
                self.selected_patch = patch
                self.start_mouse_pos = np.array([event.xdata, event.ydata])
                self.start_patch_pos = patch.xy
                break

    def on_motion(self, event):
        if self.selected_patch is not None:
            pos = np.array([event.xdata, event.ydata])
            self.selected_patch.xy = self.start_patch_pos + pos - self.start_mouse_pos
            self.ax.figure.canvas.draw_idle()

    def on_release(self, event):
        self.selected_patch = None


fig, ax = plt.subplots()
ax.set_aspect("equal")
for i in range(10):
    poly = RegularPolygon(
        rand(2),
        randint(3, 10),
        rand() * 0.1 + 0.1,
        facecolor=rand(3),
        zorder=randint(10, 100),
    )
    ax.add_patch(poly)
ax.relim()
ax.autoscale()
pm = PatchMover(ax)

show()

print("------------------------------------------------------------")  # 60個

# 點選事件

# scpy2.matplotlib.pick_event_demo：示範繪圖物件的點選事件。


fig, ax = plt.subplots()
rect = plt.Rectangle((np.pi, -0.5), 1, 1, fc=np.random.random(3), picker=True)
ax.add_patch(rect)
x = np.linspace(0, np.pi * 2, 100)
y = np.sin(x)
(line,) = plt.plot(x, y, picker=8.0)


def on_pick(event):
    artist = event.artist
    if isinstance(artist, plt.Line2D):
        lw = artist.get_linewidth()
        artist.set_linewidth(lw % 5 + 1)
    else:
        artist.set_fc(np.random.random(3))
    fig.canvas.draw_idle()


fig.canvas.mpl_connect("pick_event", on_pick)

show()

print("------------------------------------------------------------")  # 60個

# 實時反白顯示曲線

# scpy2.matplotlib.mouse_event_highlight_curve：滑鼠搬移到曲線之上時反白顯示該曲線。


class CurveHighLighter(object):
    def __init__(self, ax, alpha=0.3, linewidth=3):
        self.ax = ax
        self.alpha = alpha
        self.linewidth = 3

        ax.figure.canvas.mpl_connect("motion_notify_event", self.on_move)

    def highlight(self, target):
        need_redraw = False
        if target is None:
            for line in self.ax.lines:
                line.set_alpha(1.0)
                if line.get_linewidth() != 1.0:
                    line.set_linewidth(1.0)
                    need_redraw = True
        else:
            for line in self.ax.lines:
                lw = self.linewidth if line is target else 1
                if line.get_linewidth() != lw:
                    line.set_linewidth(lw)
                    need_redraw = True
                alpha = 1.0 if lw == self.linewidth else self.alpha
                line.set_alpha(alpha)

        if need_redraw:
            self.ax.figure.canvas.draw_idle()

    def on_move(self, evt):
        ax = self.ax
        for line in ax.lines:
            if line.contains(evt)[0]:
                self.highlight(line)
                break
        else:
            self.highlight(None)


fig, ax = plt.subplots()
x = np.linspace(0, 50, 300)

from scipy.special import jn

for i in range(1, 10):
    ax.plot(x, jn(i, x))

ch = CurveHighLighter(ax)
show()

print("------------------------------------------------------------")  # 60個

# 動畫

fig, ax = plt.subplots()
x = np.linspace(0, 10, 1000)
(line,) = ax.plot(x, np.sin(x), lw=2)


def update_data(line):
    x[:] += 0.1
    line.set_ydata(np.sin(x))
    fig.canvas.draw()


timer = fig.canvas.new_timer(interval=50)
timer.add_callback(update_data, line)
timer.start()

print("------------------------------------------------------------")  # 60個

# 使用快取快速重繪圖表

fig, ax = plt.subplots()
x = np.linspace(0, 10, 1000)
(line,) = ax.plot(x, np.sin(x), lw=2, animated=True)

fig.canvas.draw()
background = fig.canvas.copy_from_bbox(ax.bbox)


def update_data(line):
    x[:] += 0.1
    line.set_ydata(np.sin(x))
    fig.canvas.restore_region(background)
    ax.draw_artist(line)
    fig.canvas.blit(ax.bbox)


timer = fig.canvas.new_timer(interval=50)
timer.add_callback(update_data, line)
timer.start()

# animation模組

from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

x = np.linspace(0, 4 * np.pi, 200)
y = np.sin(x)
(line,) = ax.plot(x, y, lw=2, animated=True)


def update_line(i):
    y = np.sin(x + i * 2 * np.pi / 100)
    line.set_ydata(y)
    return [line]


ani = FuncAnimation(fig, update_line, blit=True, interval=25, frames=100)

# matplotlib會使用系統中安裝的視訊壓縮軟體（如ffmpeg.exe）產生視訊檔案。請讀者確認視訊壓縮軟體的可執行檔案的路徑是否在PATH環境變數中。

ani.save("tmp_sin_wave.mp4", fps=25)

# 加入GUI面板

# scpy2.matplotlib.gui_panel：提供了TK與QT界面庫的滑標控制項面板類別TkSliderPanel和QtSliderPanel。tk_panel_demo.py和qt_panel_demo.py為其示範程式。

import matplotlib

matplotlib.use("TkAgg")

import pylab as pl


def exp_sin(x, A, f, z, p):
    return A * np.sin(2 * np.pi * f * x + p) * np.exp(z * x)


fig, ax = pl.subplots()

x = np.linspace(1e-6, 1, 500)
pars = {"A": 1.0, "f": 2, "z": -0.2, "p": 0}
y = exp_sin(x, **pars)

(line,) = pl.plot(x, y)


def update(**kw):
    y = exp_sin(x, **kw)
    line.set_data(x, y)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()


from scpy2.matplotlib.gui_panel import TkSliderPanel

panel = TkSliderPanel(
    fig,
    [("A", 0, 10), ("f", 0, 10), ("z", -3, 0), ("p", 0, 2 * np.pi)],
    update,
    cols=2,
    min_value_width=80,
)
panel.set_parameters(**pars)
fig.show()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""

plt.savefig("test.png", dpi=120)
    TIP
    若果關閉了圖表視窗，則無法使用savefig()儲存圖形。實際上不需要呼叫show()顯示圖表，可以直接用savefig()將圖表儲存成圖形檔案。使用這種方法可以很容易撰寫批次輸出圖表的程式。

print xxxx
print(

b'\n\n\n

show()

print("------------------------------------------------------------")  # 60個

with open(filename, "r", encoding='UTF-8-sig') as f:

"""

plt.close("all")







cx, cy = 100, 100
R = 100
for i in range(5):
    angle = -90 + 72 * i;
    X = int(R * np.cos(angle * np.pi / 180))+cx
    Y = int(R * np.sin(angle * np.pi / 180))+cy
    print(X, Y, end=" ")
print()

cx, cy = 300, 100
R = 100
for i in range(5):
    angle = -90 + 72 * i;
    X = int(R * np.cos(angle * np.pi / 180))+cx
    Y = int(R * np.sin(angle * np.pi / 180))+cy
    print(X, Y, end=" ")
print()

cx, cy = 200, 300
R = 100
for i in range(5):
    angle = -90 + 72 * i;
    X = int(R * np.cos(angle * np.pi / 180))+cx
    Y = int(R * np.sin(angle * np.pi / 180))+cy
    print(X, Y, end=" ")
print()

