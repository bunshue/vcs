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
'''
# 分段线性拟合

import pylab as pl

def make_test_data(seg_count, point_count):
    x = np.random.uniform(2, 10, seg_count)
    x = np.cumsum(x)
    x *= 10 / x.max()
    y = np.cumsum(np.random.uniform(-1, 1, seg_count))
    X = np.random.uniform(0, 10, point_count)
    Y = np.interp(X, x, y) + np.random.normal(0, 0.05, point_count)
    return X, Y

from scipy import optimize

def segments_fit(X, Y, count):
    xmin = X.min()
    xmax = X.max()

    seg = np.full(count - 1, (xmax - xmin) / count)

    px_init = np.r_[np.r_[xmin, seg].cumsum(), xmax]
    py_init = np.array([Y[np.abs(X - x) < (xmax - xmin) * 0.01].mean() for x in px_init])

    def func(p):
        seg = p[:count - 1]
        py = p[count - 1:]
        px = np.r_[np.r_[xmin, seg].cumsum(), xmax]
        return px, py

    def err(p):
        px, py = func(p)
        Y2 = np.interp(X, px, py)
        return np.mean((Y - Y2)**2)

    r = optimize.minimize(err, x0=np.r_[seg, py_init], method='Nelder-Mead')
    return func(r.x)

X, Y = make_test_data(10, 2000)
px, py = segments_fit(X, Y, 8)

pl.plot(X, Y, ".")
pl.plot(px, py, "-or")
show()

X = np.random.uniform(0, 10, 2000)
Y = np.sin(X) + np.random.normal(0, 0.05, X.shape)
px, py = segments_fit(X, Y, 8)
pl.plot(X, Y, ".")
pl.plot(px, py, "-or")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# B样条曲线与Bezier曲线

import pylab as pl

# B样条曲线是B样条基曲线的线性组合

from collections import OrderedDict

def spline_basis(t, npoints, kmax):
    B = OrderedDict()
    x = np.linspace(t[0], t[-1], npoints)

    for i in range(len(t)-1):
        B[i, 0] = ((x > t[i]) & (x < t[i+1])).astype(float)

    for k in range(1, kmax+1):
        for i in range(len(t)-k-1):
            k1 = (x - t[i]) / (t[i+k] - t[i]) if t[i+k] > t[i] else 0
            k2 = (t[i+k+1] - x) / (t[i+k+1] - t[i+1]) if t[i+k+1] > t[i+1] else 0
            B[i, k] = k1 * B[i, k-1] + k2 * B[i+1, k-1]
    return x, B

def plot_basis(x, B, shape, figsize):
    fig, axes = pl.subplots(*shape, figsize=figsize)
    axes = axes.ravel()
    for n, ax in enumerate(axes):
        for i, k in B:
            if k == n:
                ax.plot(x, B[i, k])

# 下面是0到3次B样条基的曲线图。

t = np.r_[0, 0, 0, np.linspace(0, 1, 9), 1, 1, 1]
x, B = spline_basis(t, 200, 3)
plot_basis(x, B, (1, 4), figsize=(15, 3))
show()

# 上面B样条基的节点t的数值如下：

print(t)

# 计算B样条基与控制点p的乘积和得到B样条曲线。三次B样条曲线的控制点数比节点数少4个元素。

def spline_curve(B, k, p):
    return np.dot(np.column_stack([B[i, k] for i, _k in B if _k == k]), p)

p = np.array([[0, 0], [1, 0], [2, 1], [1, 1.5], [0, 2], [-1, 2], [-1.5, 2.5], [-2, 2], [-2, 1], [-1, 0], [0, 0]])
p2 = spline_curve(B, 3, p)
pl.plot(p[:, 0], p[:, 1], "-o")
pl.plot(p2[:, 0], p2[:, 1], "r", lw=2)
pl.margins(0.1, 0.1)
show()

# B样条插值

from scipy import interpolate

def plot_bspline(t, x, y, ax=None):
    line = interpolate.BSpline(t, np.c_[x, y], 3)
    if ax is None:
        fig, ax = pl.subplots()
    x, y = line(np.linspace(0, 1, 200)).T
    ax.plot(x, y)

line = interpolate.BSpline(t, p, 3)
x, y = line(np.linspace(0, 1, 200)).T
pl.plot(p2[:, 0], p2[:, 1], "r", lw=2)
pl.plot(x, y)
show()


def plot_interp_bspline(x, y, ax=None, **kw):
    line = interpolate.make_interp_spline(np.linspace(0, 1, len(x)), np.c_[x, y])
    x2, y2 = line(np.linspace(0, 1, 1000)).T
    if ax is None:
        fig, ax = pl.subplots()
    ax.plot(x, y, "x")
    ax.plot(x2, y2, **kw)
    xc, yc = line.c.T
    ax.plot(xc, yc, "o", alpha=0.5)
    return line

# 下面绘制B样条曲线，其中叉点为插值点，圆点为B样条曲线的控制点。

x = np.linspace(0, 2*np.pi, 8)
y = np.cos(x)
plot_interp_bspline(x, y)
show()

# 下面是通过参数方程计算的插值点及与其对应的插值曲线。

r = np.linspace(0, 2*np.pi, 8)
x = np.sin(2 * r)
y = np.cos(r)
plot_interp_bspline(x, y)
show()

"""
Bezier曲线

Bezier曲线是一种参数曲线，三次Bezier曲线由四个点P0、P1、P2、P3决定。
曲线起始于P0走向P1，并从P2的方向来到P3。

大多数的绘图软件都使用它描绘曲线轮廓。
"""
from matplotlib.path import Path
from matplotlib.patches import PathPatch

def plot_bezier_path(x, y, ax=None, **kw):
    points = np.c_[x, y]
    p = Path(points, [Path.MOVETO] + [Path.CURVE4] * (len(points) - 1))
    patch = PathPatch(p, **kw)
    if ax is None:
        fig, ax = pl.subplots()        
    ax.add_patch(patch)
    ax.autoscale_view()
    
fig, ax = pl.subplots()
x = [0, 0, 1, 1]
y = [0, 1, 1, 0]
plot_bezier_path(x, y, ax=ax, fill=False, lw=4, color="red")
plot_bspline([0, 0, 0, 0, 1, 1, 1, 1], x, y, ax=ax)
ax.plot(x, y, 'o')
show()

# 将BSpline转换为多段Bezier曲线

def bspline_to_bezier(line):
    new_line = line
    for t in line.t[4:-4]:
        new_line = interpolate.insert(t, new_line, m=3)
    points = new_line.c
    points = np.delete(points, np.arange(4, len(points), 4), axis=0)
    path = Path(points, [Path.MOVETO] + [Path.CURVE4] * (len(points) - 1))
    return path

# 下面先计算插值B样条曲线，然后将该曲线转换为Path对象。并使用PathPatch绘制填充部分。

r = np.linspace(0, 2*np.pi, 8)
x = np.sin(2 * r)
y = np.cos(r)

fig, ax = pl.subplots()

line = plot_interp_bspline(x, y, ax=ax, color="red")
path = bspline_to_bezier(line)
patch = PathPatch(path, fill=True, linewidth=0, alpha=0.5)
ax.add_patch(patch)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用LowLevelCallable提高回调函数的运行速度

# quad()计算积分

import scipy
from scipy import integrate

def normal_pdf(x, μ, σ):
    d = math.sqrt(2 * math.pi * σ**2)
    return math.exp(-(x - μ)**2 / (2 * σ**2)) / d

cc = integrate.quad(normal_pdf, -100, 100, args=(0, 1))
print(cc)

# (1.0000000000000002, 1.0347170600110818e-12)

from numba import cfunc
from numba import types as T
from scipy import LowLevelCallable

@cfunc(T.double(T.int32, T.CPointer(T.double)), nopython=True)
def normal_pdf_fast(n, data):
    x, μ, σ = data[0], data[1], data[2]
    d = math.sqrt(2 * math.pi * σ**2)
    return math.exp(-(x - μ)**2 / (2 * σ**2)) / d    

from scipy import LowLevelCallable

llc = LowLevelCallable(normal_pdf_fast.ctypes)
cc = integrate.quad(llc, -100, 100, args=(0, 1))
print(cc)
# (1.0000000000000002, 1.0347170600110818e-12)

cc = integrate.quad(normal_pdf, -0.5, 0.5, args=(0, 1))
print(cc)

cc = integrate.quad(llc, -0.5, 0.5, args=(0, 1))
print(cc)

#58.4 µs ± 2.31 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
# 4.43 µs ± 40.9 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

# geometric_transform()对图像进行几何变形

# ndimage.geometric_transform()将图像上每点的坐标传递给回调函数，得到几何变换之后的坐标。下面使用它实现图像的旋转。

from scipy import ndimage
from PIL import Image
import ctypes

#img = ndimage.imread("flower.jpg")# 廢棄
import imageio
img = np.array(imageio.imread("flower.jpg"))


def trans_func_py(pos, h, w):
    r, c, d = pos
    x, y = c - w / 2, r - h / 2
    dist = math.hypot(x, y)
    angle = math.atan2(y, x) + math.radians(30)
    x, y = dist * math.cos(angle), dist * math.sin(angle)
    return y + h / 2, x + w / 2, d

new_img = ndimage.geometric_transform(img, trans_func_py, order=1, extra_arguments=img.shape[0:2])

# Wall time: 520 ms

# LowLevelCallable对象在调用时，会使用其signature属性判断函数的参数类型是否正确。由于numba创建的ctypes函数的调用参数类型的字符串与geometric_transform()所需的类型字符串不匹配，因此这里在创建LowLevelCallable对象时直接设置其signature属性。

@cfunc(T.int_(T.CPointer(T.intp), T.CPointer(T.double), T.int_, T.int_, T.CPointer(T.int_)))
def trans_func_nb(out_coord, in_coord, out_rank, in_rank, data):
    h = data[0]
    w = data[1]
    r = out_coord[0]
    c = out_coord[1]
    d = out_coord[2]
    x = c - w / 2
    y = r - h / 2
    dist = math.hypot(x, y)
    angle = math.atan2(y, x) + math.radians(30)
    x, y = dist * math.cos(angle), dist * math.sin(angle)
    in_coord[0] = y + h / 2
    in_coord[1] = x + w / 2
    in_coord[2] = d
    return 1

data = (ctypes.c_int32 * 2)(img.shape[0], img.shape[1])
llc = LowLevelCallable(trans_func_nb.ctypes, 
                       signature='int (long long *, double *, int, int, void *)',
                       user_data=ctypes.cast(data, ctypes.c_void_p))
new_img2 = ndimage.geometric_transform(img, llc, order=1)

#Image.fromarray(new_img2)

#Wall time: 69 ms

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 冲激响应与频率响应

import pylab as pl
import matplotlib
from scipy import signal

# 线性时不变系统可以使用其冲激响应或者频率响应描述。

b = [0.1, -0.1]
a = [1, 2, 3]

period = 0.001
t = np.arange(0, 10, period)
_, ir = signal.impulse((b, a), T=t)
pl.plot(t, ir, label="impulse")
pl.grid()
show()

# 下面的impulse_to_frequency_response()通过FFT将冲激响应转换为频率响应，并与signal.freqs()计算的理论频率响应值比较：

def impulse_to_frequency_response(t, ir, length=None):
    if length is None:
        length = len(ir)
    period = t[1] - t[0]
    omega = np.fft.rfftfreq(length, period) * 2 * np.pi
    fr = np.fft.rfft(ir, n=length) * period
    return omega, fr

def db(h):
    return 20 * np.log10(np.abs(h))

def compare_frequency_response(omegas, hs, labels):
    fig, axes = pl.subplots(2, 1, sharex=True, figsize=(8, 7))
    for omega, h, label in zip(omegas, hs, labels):
        axes[0].semilogx(omega, db(h), label=label)
        axes[1].semilogx(omega, np.angle(h), label=label)
    for ax in axes:
        ax.grid()
        ax.legend()
        
omega1 = np.logspace(-1, 3, 1000)
_, h1 = signal.freqs(b, a, omega1)

omega2, h2 = impulse_to_frequency_response(t, ir)
compare_frequency_response([omega1, omega2], [h1, h2], ["freqs", "impulse"])

show()

# 可以观察到二者在高频段的相位逐渐出现偏差,而低频段impulse的数据不足。对于数据不足可以通过在冲激响应之后添补0，即增加FFT的长度解决。

omega3, h3 = impulse_to_frequency_response(t, ir, length=100000)
show()

compare_frequency_response([omega1, omega3], [h1, h3], ["freqs", "impulse"])
show()

# 而高频的相位误差可以通过增加取样频率解决：

period = 0.0001
t4 = np.arange(0, 10, period)
_, ir4 = signal.impulse((b, a), T=t4)
omega4, h4 = impulse_to_frequency_response(t4, ir4)
compare_frequency_response([omega1, omega4], [h1, h4], ["freqs", "impulse"])

show()

#在频域进行系统识别

#如果通过实验测得系统的一组频率响应，可以使用scipy.optimize.minimize()计算出系统的传递函数系数。下面通过8点频率响应值计算出级数不同的3个传递函数的系数：

from scipy import optimize

def get_ba(p):
    return np.r_[0, p[:len(p)//2]], np.r_[1, p[len(p)//2:]]

def plot_response(res, omega):
    fig, axes = pl.subplots(figsize=(12, 6))
    for p in res:
        b, a = get_ba(p)
        _, resp = signal.freqs(b, a, omega)
        axes.loglog(omega, np.abs(resp))
    
def error(p, omegas, responses):
    b, a = get_ba(p)
    _, resp = signal.freqs(b, a, omegas)
    return (np.abs(resp - responses)**2).mean()

omega = np.logspace(-1, 3, 8)
_, h = signal.freqs(b, a, omega)
args = omega, h

r1 = optimize.minimize(error, [1, 1], args=args)
r2 = optimize.minimize(error, [1, 1, 1, 1], args=args)
r3 = optimize.minimize(error, [1, 1, 1, 1, 1, 1], args=args)

omega2 = np.logspace(-1, 3, 500)
b1, a1 = get_ba(r1.x)
b2, a2 = get_ba(r2.x)
b3, a3 = get_ba(r3.x)
_, h1 = signal.freqs(b1, a1, omega2)
_, h2 = signal.freqs(b2, a2, omega2)
_, h3 = signal.freqs(b3, a3, omega2)

compare_frequency_response([omega2] * 3, [h1, h2, h3], ["order1", "order2", "order3"])

show()

print(b2, a2)

"""
(array([ 0.        ,  0.09991928, -0.10001922]),
 array([ 1.        ,  1.99959954,  2.99970942]))
"""

# 在时域进行系统识别

# 在频域测量系统的响应需要输入不同频率的正弦波，并计算输入和输入之间的振幅比和相位差，测量起来比较麻烦，而系统的脉冲响应则无法直接测得。此时我们可以测量系统的阶跃响应。下面使用signal.step()计算阶跃响应，并添加一定的测量噪声。

t = np.arange(0, 10, 0.01)
_, sr = signal.step((b, a), T=t)
sr += np.random.normal(0, 0.001, len(t))
pl.plot(t, sr)
pl.grid()
show()

#然后使用优化库找到最符合上面的阶跃响应的系统的系数。

def plot_step_response(res, t):
    fig, axes = pl.subplots(figsize=(12, 6))
    for p in res:
        b, a = get_ba(p)
        _, resp = signal.step((b, a), T=t)
        axes.plot(t, resp)
    return axes
    
def error_step_response(p, t, response):
    b, a = np.r_[0, p[:len(p)//2]], np.r_[1, p[len(p)//2:]]
    _, resp = signal.step((b, a), T=t)
    return ((resp - response)**2).mean()

args = t, sr

tr1 = optimize.minimize(error_step_response, [1, 1], args=args)
tr2 = optimize.minimize(error_step_response, [1, 1, 1, 1], args=args, tol=1e-10)
tr3 = optimize.minimize(error_step_response, [1, 1, 1, 1, 1, 1], args=args)
get_ba(tr2.x)

"""
(array([ 0.        ,  0.10031599, -0.1003608 ]),
 array([ 1.        ,  2.01585575,  3.00359599]))
"""

omega2 = np.logspace(-1, 3, 500)
b1, a1 = get_ba(tr1.x)
b2, a2 = get_ba(tr2.x)
b3, a3 = get_ba(tr3.x)
_, h1 = signal.freqs(b1, a1, omega2)
_, h2 = signal.freqs(b2, a2, omega2)
_, h3 = signal.freqs(b3, a3, omega2)

compare_frequency_response([omega2] * 3, [h1, h2, h3], ["order1", "order2", "order3"])
show()

# 比较二阶拟合的拟合结果与真实的系统响应：

omega2 = np.logspace(-1, 3, 500)
_, h = signal.freqs(b, a, omega2)
compare_frequency_response([omega2] * 2, [h, h2], ["system", "estimated"])
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# 最小覆盖圆与最大空圆

# 对于平面上一群给定的点，覆盖所点的最小圆称为最小覆盖圆，以及圆心在点的凸包区域之内，并且圆内没有任何点的最大圆。

import pylab as pl
import matplotlib

"""
最小覆盖圆

首先需要找到这群点的凸包，所谓凸包是指N维空间中的一个区域，该区域中任意两点之间的线段都完全被包含在该区域之中，二维平面上的凸多边形就是典型的凸包。然后只需找到覆盖凸包的最小圆即可。最小圆有两种情况：

    以凸包上的两点为直径的圆
    过凸包上三点的圆
"""

def orientation(p,q,r):
    # Return positive if p-q-r are clockwise, neg if ccw, zero if colinear.
    return (q[1]-p[1])*(r[0]-p[0]) - (q[0]-p[0])*(r[1]-p[1])

def hulls(Points):
    # Graham scan to find upper and lower convex hulls of a set of 2d points.
    U = []
    L = []
    Points.sort()
    for p in Points:
        while len(U) > 1 and orientation(U[-2],U[-1],p) <= 0: U.pop()
        while len(L) > 1 and orientation(L[-2],L[-1],p) >= 0: L.pop()
        U.append(p)
        L.append(p)
    return U, L

def rotatingCalipers(U, L):
    i = 0
    j = len(L) - 1
    while i < len(U) - 1 or j > 0:
        yield U[i],L[j]
        
        # if all the way through one side of hull, advance the other side
        if i == len(U) - 1: j -= 1
        elif j == 0: i += 1
        
        # still points left on both lists, compare slopes of next hull edges
        # being careful to avoid divide-by-zero in slope calculation
        elif (U[i+1][1]-U[i][1])*(L[j][0]-L[j-1][0]) > \
                (L[j][1]-L[j-1][1])*(U[i+1][0]-U[i][0]):
            i += 1
        else: j -= 1
            
def diameter(Points):
    U, L = hulls(Points)
    diam, pair = max([((p[0]-q[0])**2 + (p[1]-q[1])**2, (p,q))
                     for p,q in rotatingCalipers(U, L)])
    return diam**0.5, pair            

# 下面创建随机100个点，并绘制它们的凸包以及候选的最远点对。

from matplotlib.collections import LineCollection

np.random.seed(42)
points = np.random.randn(100, 2)
u, l = hulls(points.tolist())
ua, la = map(np.array, [u, l])

fig, ax = pl.subplots()
ax.set_aspect(True)
ax.scatter(*points.T, marker="x")
ax.plot(ua[:, 0], ua[:, 1])
ax.plot(la[:, 0], la[:, 1])

lines = [[p1, p2] for p1, p2 in rotatingCalipers(u, l)]
line_collection = LineCollection(lines, colors="black", alpha=0.3)
ax.add_collection(line_collection)
ax.axis("off")
show()

# SciPy中提供了计算凸包的类：scipy.spatial.ConvexHull()。它的vertices属性保存凸包上点的序号。为了调用rotatingCalipers()，下面的convex_hull_ul()把凸包分为上半部分和下半部分。min_2points_circle()找到凸包上以两点为直径的最大的圆：

from scipy import spatial

def convex_hull_ul(points):
    hull = spatial.ConvexHull(points)
    verts = hull.vertices
    verts = np.roll(verts, -np.argmin(points[verts, 0]))
    sep = np.argmax(points[verts, 0])
    verts_l, verts_u = verts[:sep+1], np.r_[verts[sep:], verts[0]]
    return points[verts_u[::-1]], points[verts_l]

def min_2points_circle(points):
    d, (p1, p2) = diameter(points.tolist())
    return ((p1[0] + p2[0]) * 0.5, (p1[1] + p2[1]) * 0.5), d * 0.5

# 由下面的结果可知，不存在以两点为直径覆盖所有点的圆。

fig, ax = pl.subplots()
ax.set_aspect(True)
u, l = convex_hull_ul(points)
pl.plot(*u.T)
pl.plot(*l.T)
lines = [[p1, p2] for p1, p2 in rotatingCalipers(u.tolist(), l.tolist())]
line_collection = LineCollection(lines, colors="black", alpha=0.3)
center, r = min_2points_circle(points)
circle = pl.Circle(center, r, fill=False, color="red")
ax.add_collection(line_collection)
ax.add_artist(circle)
ax.margins(0.1)
ax.axis("off")
show()

# 经过凸包上3点的圆可以使用最远点沃罗诺伊图计算。最远点沃罗诺伊图(Voronoi Diagram)是一种空间分割算法，它根据指定的N个胞点将空间分割为N个区域，每个区域中的所有坐标点都与该区域对应的胞点最远。

# scipy.spatial.Voronoi()计算沃罗诺伊图，当furthest_site参数为True时计算最远点沃罗诺伊图。下面计算以points为胞点的最远点沃罗诺伊图，并显示构成各个区域的顶点(vertices)。

from scipy.spatial.distance import cdist

v = spatial.Voronoi(points, furthest_site=True)
print(v.vertices)


# 下面遍历v.point_region找到与每个胞点对应的区域，然后遍历区域找到构成每个区域的顶点。将与顶点对应的胞点添加进vertice_points字典中。胞点与顶点之间的相关信息也可以通过v.ridge_dict获得。

def calc_vertice_points_map(v):
    from collections import defaultdict

    vertice_points = defaultdict(list)

    for point_id, region_id in enumerate(v.point_region):
        region = v.regions[region_id]
        if region:
            for vertice_id in region:
                if vertice_id != -1:
                    vertice_points[vertice_id].append(point_id)
    return vertice_points

vertice_points = calc_vertice_points_map(v)
print(vertice_points)

"""
defaultdict(list,
            {0: [37, 39, 61],
             1: [37, 61, 89],
             2: [18, 39, 61],
             3: [37, 39, 73],
             4: [62, 78, 89],
             5: [53, 61, 78],
             6: [61, 78, 89],
             7: [62, 78, 83]})
"""
# 对于每个顶点找到与之最远的胞点距离，然后找到所有顶点中该距离最小的顶点。该顶点就是最小覆盖原圆的圆心，而该距离就是最小圆的半径。

def distance(vid, pids):
    return np.max(np.sum((v.vertices[vid] - v.points[pids])**2, axis=-1)**0.5)

min((distance(vid, pid), v.vertices[vid]) for vid, pid in vertice_points.items())

# (2.4011794636311912, array([-0.27182   ,  0.31900039]))

# 下面是完整的函数：

def min_3points_circle(points):
    v = spatial.Voronoi(points, furthest_site=True)   
    vertice_points = calc_vertice_points_map(v)
                    
    def distance(vid, pids):
        return np.max(np.sum((v.vertices[vid] - v.points[pids])**2, axis=-1)**0.5)

    r, center = min((distance(vid, pid), v.vertices[vid]) for vid, pid in vertice_points.items())
    return center, r

fig, ax = pl.subplots()
ax.set_aspect(True)
ax.scatter(*points.T, marker="x")
center, radius = min_3points_circle(points)
circle = pl.Circle(center, radius, fill=False, color="red")
ax.add_artist(circle)
circle_points = points[(radius - np.sum((points - center)**2, axis=1)**0.5) < 1e-12]
ax.scatter(*circle_points.T, marker="o", alpha=0.4)
ax.autoscale_view()
ax.margins(0.1)
ax.axis("off")
show()

# 最大空圆

# 使用最近点沃罗诺伊图可以解决最大空圆问题：找到一个半径最大的圆，使得其圆心在一组点的凸包区域之内，并且圆内没有任何点。最大空圆是以为顶点圆心，以与之最近的胞点的距离为半径的圆中的某一个。

n = 50
np.random.seed(42)
points2d = np.random.rand(n, 2)
vo = spatial.Voronoi(points2d)
ch = spatial.ConvexHull(points2d)
poly = pl.Polygon(points2d[ch.vertices])
vs = vo.vertices

vertice_points = {k:v for k, v in calc_vertice_points_map(vo).items() if poly.contains_point(vs[k])}

def dist(p1, p2):
    return ((p1-p2)**2).sum()**0.5

max_cicle = max((dist(points2d[pidxs[0]], vs[vidx]), vs[vidx])
                for vidx, pidxs in vertice_points.items())
r, center = max_cicle
print("r = ", r, ", center = ", center)

ax = pl.subplot(111, aspect="equal")
ax.plot(points2d[:, 0], points2d[:, 1], ".")

c = pl.Circle(center, r, fill=True, color="red", alpha=0.5)
ax.add_artist(c)
ax.axis("off")
show()

# r =  0.174278456762 , center =  [ 0.46973363  0.59356531]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
sys.exit()
# 用Kmeans算法计算图像的调色板

import pylab as pl
import matplotlib

# k-平均算法把n个点划分到k个聚类中，使得每个点都属于离他最近的均值对应的聚类，以之作为聚类的标准。下面使用sklearn.datasets.make_blob()创建3个聚类，它们的中心分别为(0, 0), (5, 0), (0, 5)。

from sklearn.datasets import make_blobs

points, labels = make_blobs(centers=[[0, 0], [5, 0], [0, 5]],
                            n_samples=1000, cluster_std=1.0, random_state=8)
pl.scatter(points[:, 0], points[:, 1], c=labels, s=2)
show()

# 下面调用scipy.cluster.vq.kmeans2()将points中的点分为3个聚类。它返回每个聚类的中心和每个点所属的聚类。

from scipy.cluster import vq

centers, labels = vq.kmeans2(points, 3, iter=20)
pl.scatter(points[:, 0], points[:, 1], c=labels, s=2)
pl.plot(centers[:, 0], centers[:, 1], "ro")
show()

# k-平均算法是一种迭代算法，下面的程序调用kmeans2()时设置iter参数为1，即每次调用进行一次迭代。并将前次计算所得的聚类中心作为下次调用的聚类中心初始值。最后使用holoviews显示计算结果。

""" NG
import holoviews as hv

hv.notebook_extension()
"""

"""
C:\Anaconda3\lib\site-packages\matplotlib\cbook.py:136: MatplotlibDeprecationWarning: The spectral and spectral_r colormap was deprecated in version 2.0. Use nipy_spectral and nipy_spectral_r instead.
  warnings.warn(message, mplDeprecation, stacklevel=1)

HoloViewsJS successfully loaded in this cell.
"""
""" NG
np.random.seed(2)
centers = points[np.random.choice(np.arange(len(points)), 3, replace=False), :]
hm_centers = hv.HoloMap(kdims=["iter"])
hm_labels = hv.HoloMap(kdims=["iter"])
for i in range(1, 11):
    centers, labels = vq.kmeans2(points, centers, iter=1)
    table1 = hv.Table(np.column_stack([centers, np.arange(len(centers))]), kdims=["x", "y", "label"])
    hm_centers[i] = table1.to.scatter(kdims=["x"], vdims=["y"]).overlay()
    table2 = hv.Table(np.column_stack([points, labels]), kdims=["x", "y", "label"])
    hm_labels[i] = table2.to.points(kdims=["x", "y"]).overlay()
    
pl.scatter(points[:, 0], points[:, 1], c=labels, s=2)
pl.plot(centers[:, 0], centers[:, 1], "ro")
show()
"""

"""
%%opts Overlay [fig_inches=(6, 6)] Points (s=10 alpha=0.6) Scatter (s=40 edgecolor="black")
hm_labels * hm_centers
"""

# 提取图片中的色彩

# 彩色图像中的每个像素使用红绿蓝三个分量表示，可以将之看作三维空间中的点。使用k-平均算法可以找到该空间中的聚类，即可图像的主要颜色成分。

from PIL import Image

img = Image.open("flower.jpg")
img_arr = np.asarray(img)[:, :, :3]
arr = img_arr.reshape(-1, 3).astype(np.float32)
img

# 下面计算图像颜色的10个聚类。注意k-平均算法只能收敛于一个局部最优解，因此有可能有些聚类对应的点数为0，此时会出现One of the clusters is empty的警告信息。下面的程序使用numpy.bincount()统计每个聚类对应的点数，并丢弃点数为0的聚类。

code, labels = vq.kmeans2(arr, 10)
code = code.astype(np.uint8)
colors = code[np.bincount(labels) > 0]

def display_colors(colors):
    from IPython.display import display_html
    colors = colors[np.argsort(colors.sum(1))]
    pattern = '<span style="padding:20px;background-color:#{:02x}{:02x}{:02x}"></span>'
    display_html("".join(pattern.format(*row) for row in colors), raw=True)

display_colors(colors)

"""
C:\Anaconda3\lib\site-packages\scipy\cluster\vq.py:660: UserWarning: One of the clusters is empty. Re-run kmean with a different initialization.
  warnings.warn("One of the clusters is empty. "
C:\Anaconda3\lib\site-packages\ipykernel\__main__.py:3: VisibleDeprecationWarning: boolean index did not match indexed array along dimension 0; dimension is 10 but corresponding boolean dimension is 9
  app.launch_new_instance()
"""

# 使用code[labels]可以得到以聚类中心表示每个点的图像，即只使用7种颜色（有几个聚类的点数为0）表示的图像。

Image.fromarray(code[labels].reshape(img_arr.shape))

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

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
