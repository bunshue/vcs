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

import pylab as pl
import scipy  # SciPy-數值計算庫
from scipy import constants  # 常數
from scipy import stats
from scipy import optimize
from scipy import linalg  # 線性代數-linalg, 解線性方程式群組
from scipy import integrate
from scipy import interpolate  # 插值-interpolate
from scipy import spatial  # 空間算法庫-spatial
from scipy import signal  # 訊號處理-signal
from scipy import sparse  # 稀疏矩陣-sparse
from scipy.sparse import csgraph
from scipy.integrate import odeint
from scipy.integrate import ode

import scipy.special


def show():
    #plt.show()
    pass

print("------------------------------------------------------------")  # 60個

print("常量和特殊函數")
print(constants.c) # 真空中的光速
print(constants.h) # 普朗克常量

print("一個電子的質量")
cc = constants.physical_constants["electron mass"]
print(cc)

print("一英里 = ? 公尺\t", constants.mile)
print("一英吋 = ? 公尺\t", constants.inch)
print("一公克 = ? 公斤\t", constants.gram)
print("一英鎊 = ? 公斤\t", constants.pound)

print('Gamma函數')
print(scipy.special.gamma(4))
print(scipy.special.gamma(0.5))
print(scipy.special.gamma(1+1j)) # gamma函數支援複數
print(scipy.special.gamma(1000))
print(scipy.special.gammaln(1000))

print(1 + 1e-20)
print(np.log(1+1e-20))
print(scipy.special.log1p(1e-20))

m = np.linspace(0.1, 0.9, 4)
u = np.linspace(-10, 10, 200)
results = scipy.special.ellipj(u[:, None], m[None, :])

print([y.shape for y in results])

# 使用廣播計算得到的`ellipj()`傳回值
fig, axes = pl.subplots(2, 2, figsize=(12, 4))
labels = ["$sn$", "$cn$", "$dn$", "$\phi$"]
for ax, y, label in zip(axes.ravel(), results, labels):
    ax.plot(u, y)
    ax.set_ylabel(label)
    ax.margins(0, 0.1)
    
axes[1, 1].legend(["$m={:g}$".format(m_) for m_ in m], loc="best", ncol=2)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#擬合與改善-optimize
#非線性方程式群組求解

def f(x):
    x0, x1, x2 = x.tolist() #❷
    return [
        5*x1+3,
        4*x0*x0 - 2*math.sin(x1*x2),
        x1*x2 - 1.5
    ]

# f計算方程式群組的誤差，[1,1,1]是不詳數的初值
result = optimize.fsolve(f, [1,1,1]) #❸
print(result)
print(f(result))


def j(x):
    x0, x1, x2 = x.tolist()
    return [
        [0, 5, 0],
        [8*x0, -2*x2*math.cos(x1*x2), -2*x1*math.cos(x1*x2)],
        [0, x2, x1]
    ]
 
result = optimize.fsolve(f, [1,1,1], fprime=j) #❷
print(result)
print(f(result))

#最小二乘擬合

X = np.array([ 8.19,  2.72,  6.39,  8.71,  4.7 ,  2.66,  3.78])
Y = np.array([ 7.01,  2.78,  6.47,  6.71,  4.1 ,  4.23,  4.05])

def residuals(p):
    "計算以p為參數的直線和原始資料之間的誤差"
    k, b = p
    return Y - (k*X + b)

# leastsq使得residuals()的輸出陣列的平方和最小，參數的初值為[1,0]
r = optimize.leastsq(residuals, [1, 0]) #❷
k, b = r[0]
print("k =",k, "b =",b)

#k = 0.613495349193 b = 1.79409254326

# 最小化正方形面積之和（左），誤差曲面（右）
scale_k = 1.0
scale_b = 10.0
scale_error = 1000.0

def S(k, b):
    "計算直線y=k*x+b和原始資料X、Y的誤差的平方和"
    error = np.zeros(k.shape)
    for x, y in zip(X, Y):
        error += (y - (k * x + b)) ** 2
    return error

ks, bs = np.mgrid[k - scale_k:k + scale_k:40j, b - scale_b:b + scale_b:40j]
error = S(ks, bs) / scale_error

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle

fig = pl.figure(figsize=(12, 5))

ax1 = pl.subplot(121)

ax1.plot(X, Y, "o")
X0 = np.linspace(2, 10, 3)
Y0 = k*X0 + b
ax1.plot(X0, Y0)

for x, y in zip(X, Y):
    y2 = k*x+b
    rect = Rectangle((x,y), abs(y-y2), y2-y, facecolor="red", alpha=0.2)
    ax1.add_patch(rect)

ax1.set_aspect("equal")


ax2 = fig.add_subplot(122, projection='3d')

ax2.plot_surface(
    ks, bs / scale_b, error, rstride=3, cstride=3, cmap="jet", alpha=0.5)
ax2.scatter([k], [b / scale_b], [S(k, b) / scale_error], c="r", s=20)
ax2.set_xlabel("$k$")
ax2.set_ylabel("$b$")
ax2.set_zlabel("$error$");

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 帶噪聲的正弦波擬合
def func(x, p):
    """
    資料擬合所用的函數: A*sin(2*pi*k*x + theta)
    """
    A, k, theta = p
    return A*np.sin(2*np.pi*k*x+theta)   

def residuals(p, y, x): #❷
    """
    實驗資料x, y和擬合函數之間的差，p為擬合需要找到的系數
    """
    return y - func(x, p)

x = np.linspace(0, 2*np.pi, 100)
A, k, theta = 10, 0.34, np.pi/6 # 真實資料的函數參數
y0 = func(x, [A, k, theta]) # 真實資料

# 加入噪聲之後的實驗資料
y1 = y0 + 2 * np.random.randn(len(x)) #❸

p0 = [7, 0.40, 0] # 第一次猜測的函數擬合參數

# 呼叫leastsq進行資料擬合
# residuals為計算誤差的函數
# p0為擬合參數的初值
# args為需要擬合的實驗資料
plsq = optimize.leastsq(residuals, p0, args=(y1, x)) #❹

print(u"真實際參數數:", [A, k, theta]) 
print(u"擬合參數", plsq[0]) # 實驗資料擬合後的參數

plt.plot(x, y1, "o", label=u"帶噪聲的實驗資料")
plt.plot(x, y0, label=u"真實資料")
plt.plot(x, func(x, plsq[0]), label=u"擬合資料")
plt.legend(loc="best");

show()


def func2(x, A, k, theta):
    return A*np.sin(2*np.pi*k*x+theta)   

popt, _ = optimize.curve_fit(func2, x, y1, p0=p0)
print(popt)

popt, _ = optimize.curve_fit(func2, x, y1, p0=[10, 1, 0])
print(u"真實際參數數:", [A, k, theta])
print(u"擬合參數", popt)


#計算函數局域最小值

def target_function(x, y):
    return (1-x)**2 + 100*(y-x**2)**2    

class TargetFunction(object):
    
    def __init__(self):
        self.f_points = []
        self.fprime_points = []
        self.fhess_points = []
        
    def f(self, p):
        x, y = p.tolist()
        z = target_function(x, y)
        self.f_points.append((x, y))
        return z
        
    def fprime(self, p):
        x, y = p.tolist()
        self.fprime_points.append((x, y))
        dx = -2 + 2*x - 400*x*(y - x**2)
        dy = 200*y - 200*x**2
        return np.array([dx, dy])
    
    def fhess(self, p):
        x, y = p.tolist()
        self.fhess_points.append((x, y))
        return np.array([[2*(600*x**2 - 200*y + 1), -400*x],
                         [-400*x, 200]])
 
def fmin_demo(method):
    target = TargetFunction()
    init_point =(-1, -1)
    res = optimize.minimize(target.f, init_point, 
                      method=method,
                      jac=target.fprime,
                      hess=target.fhess)
    return res, [np.array(points) for points in 
                (target.f_points, target.fprime_points, target.fhess_points)]

methods = ("Nelder-Mead", "Powell", "CG", "BFGS", "Newton-CG", "L-BFGS-B")
for method in methods:
    res, (f_points, fprime_points, fhess_points) = fmin_demo(method)
    print("{:12s}: min={:12g}, f count={:3d}, fprime count={:3d}, fhess count={:3d}".format(
        method, float(res["fun"]), len(f_points), len(fprime_points), len(fhess_points)))


# 各種改善算法的搜尋路徑
def draw_fmin_demo(f_points, fprime_points, ax):
    xmin, xmax = -3, 3
    ymin, ymax = -3, 3
    Y, X = np.ogrid[ymin:ymax:500j,xmin:xmax:500j]
    Z = np.log10(target_function(X, Y))
    zmin, zmax = np.min(Z), np.max(Z)
    ax.imshow(Z, extent=(xmin,xmax,ymin,ymax), origin="bottom", aspect="auto", cmap="gray")
    ax.plot(f_points[:,0], f_points[:,1], lw=1)
    ax.scatter(f_points[:,0], f_points[:,1], c=range(len(f_points)), s=50, linewidths=0)
    if len(fprime_points):
        ax.scatter(fprime_points[:, 0], fprime_points[:, 1], marker="x", color="w", alpha=0.5)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

fig, axes = plt.subplots(2, 3, figsize=(9, 6))
methods = ("Nelder-Mead", "Powell", "CG", "BFGS", "Newton-CG", "L-BFGS-B")
for ax, method in zip(axes.ravel(), methods):
    res, (f_points, fprime_points, fhess_points) = fmin_demo(method)
    # NG draw_fmin_demo(f_points, fprime_points, ax)
    ax.set_aspect("equal")
    ax.set_title(method)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("計算全域最小值")

def func(x, p):
    A, k, theta = p
    return A*np.sin(2*np.pi*k*x+theta)

def func_error(p, y, x):
    return np.sum((y - func(x, p))**2)   

x = np.linspace(0, 2*np.pi, 100)
A, k, theta = 10, 0.34, np.pi/6 
y0 = func(x, [A, k, theta])

y1 = y0 + 2 * np.random.randn(len(x))

result = optimize.basinhopping(func_error, (1, 1, 1),
                      niter = 10,
                      minimizer_kwargs={"method":"L-BFGS-B",
                                        "args":(y1, x)})
print(result.x)

# 用`basinhopping()`擬合正弦波
plt.plot(x, y1, "o", label=u"帶噪聲的實驗資料")
plt.plot(x, y0, label=u"真實資料")
plt.plot(x, func(x, result.x), label=u"擬合資料")
plt.legend(loc="best")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("線性代數-linalg, 解線性方程式群組")

m, n = 500, 50
A = np.random.rand(m, m)
B = np.random.rand(m, n)
X1 = linalg.solve(A, B)
X2 = np.dot(linalg.inv(A), B)
print(np.allclose(X1, X2))
cc = linalg.solve(A, B)
print(cc)
cc = np.dot(linalg.inv(A), B)
print(cc)

luf = linalg.lu_factor(A)
X3 = linalg.lu_solve(luf, B)
cc = np.allclose(X1, X3)
print(cc)

M, N = 1000, 100
A = np.random.rand(M, M)
B = np.random.rand(M, N)
Ai = linalg.inv(A)
luf = linalg.lu_factor(A)   
cc = linalg.inv(A)
print(cc)
cc = np.dot(Ai, B)
print(cc)
cc = linalg.lu_factor(A)
print(cc)
cc = linalg.lu_solve(luf, B)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
#最小二乘解

from numpy.lib.stride_tricks import as_strided

def make_data(m, n, noise_scale):
    x = np.random.standard_normal(m) 
    h = np.random.standard_normal(n) 
    y = np.convolve(x, h) 
    yn = y + np.random.standard_normal(len(y)) * noise_scale * np.max(y)
    return x, yn, h
    
def solve_h(x, y, n):      #❷
    X = as_strided(x, shape=(len(x)-n+1, n), strides=(x.itemsize, x.itemsize)) #❸
    Y = y[n-1:len(x)]      #❹
    h = linalg.lstsq(X, Y) #❺
    return h[0][::-1]      #❻

x, yn, h = make_data(1000, 100, 0.4)   
H1 = solve_h(x, yn, 120)
H2 = solve_h(x, yn, 80)

print("Average error of H1:", np.mean(np.abs(H1[:100] - h)))
print("Average error of H2:", np.mean(np.abs(h[:80] - H2)))

#Average error of H1: 0.301548854044
#Average error of H2: 0.295842215834

# 實際的系統參數與最小二乘解的比較
fig, (ax1, ax2) = pl.subplots(2, 1, figsize=(6, 4))
ax1.plot(h, linewidth=2, label=u"實際的系統參數")
ax1.plot(H1, linewidth=2, label=u"最小二乘解H1", alpha=0.7)
ax1.legend(loc="best", ncol=2)
ax1.set_xlim(0, len(H1))

ax2.plot(h, linewidth=2, label=u"實際的系統參數")
ax2.plot(H2, linewidth=2, label=u"最小二乘解H2", alpha=0.7)
ax2.legend(loc="best", ncol=2)
ax2.set_xlim(0, len(H2));

show()
"""
print("------------------------------------------------------------")  # 60個

"""
print("特徵值 和 特徵向量")

A = np.array([[1, -0.3], [-0.1, 0.9]])
evalues, evectors = linalg.eig(A)
print(evalues)
print(evectors)

# 線性變換將藍色箭頭變換為紅色箭頭
points = np.array([[0, 1.0], [1.0, 0], [1, 1]])

def draw_arrows(points, **kw):
    props = dict(color="blue", arrowstyle="->")
    props.update(kw)
    for x, y in points:
        pl.annotate("",
                    xy=(x, y), xycoords='data',
                    xytext=(0, 0), textcoords='data',
                    arrowprops=props)

draw_arrows(points)
draw_arrows(np.dot(A, points.T).T, color="red")    
draw_arrows(evectors.T, alpha=0.7, linewidth=2)
draw_arrows(np.dot(A, evectors).T, color="red", alpha=0.7, linewidth=2)    

ax = pl.gca()
ax.set_aspect("equal")
ax.set_xlim(-0.5, 1.1)
ax.set_ylim(-0.5, 1.1);

show()
"""
print("------------------------------------------------------------")  # 60個

t = np.random.uniform(0, 2 * np.pi, 60)

alpha = 0.4
a = 0.5
b = 1.0
x = 1.0 + a * np.cos(t) * np.cos(alpha) - b * np.sin(t) * np.sin(alpha)
y = 1.0 + a * np.cos(t) * np.sin(alpha) - b * np.sin(t) * np.cos(alpha)
x += np.random.normal(0, 0.05, size=len(x))
y += np.random.normal(0, 0.05, size=len(y))

D = np.c_[x**2, x * y, y**2, x, y, np.ones_like(x)]
A = np.dot(D.T, D)
C = np.zeros((6, 6))
C[[0, 1, 2], [2, 1, 0]] = 2, -1, 2
evalues, evectors = linalg.eig(A, C)
evectors = np.real(evectors)
err = np.mean(np.dot(D, evectors) ** 2, 0)  # ❷
p = evectors[:, np.argmin(err)]  # ❸
print(p)


# 用廣義特征向量計算的擬合橢圓
def ellipse(p, x, y):
    a, b, c, d, e, f = p
    return a * x**2 + b * x * y + c * y**2 + d * x + e * y + f


X, Y = np.mgrid[0:2:100j, 0:2:100j]
Z = ellipse(p, X, Y)
pl.plot(x, y, "ro", alpha=0.5)
pl.contour(X, Y, Z, levels=[0])

show()

print("------------------------------------------------------------")  # 60個

# 奇異值分解-SVD

r, g, b = np.rollaxis(pl.imread("vinci_target.png"), 2).astype(float)
img = 0.2989 * r + 0.5870 * g + 0.1140 * b
print(img.shape)

U, s, Vh = linalg.svd(img)
print(U.shape)
print(s.shape)
print(Vh.shape)


# 按從大到小排序的奇異值
pl.semilogy(s, lw=3)

show()

print("------------------------------------------------------------")  # 60個


def composite(U, s, Vh, n):
    return np.dot(U[:, :n], s[:n, np.newaxis] * Vh[:n, :])


print(np.allclose(img, composite(U, s, Vh, len(s))))

# True

# 原始圖形、使用10、20、50個向量合成的圖形（從左到右）
img10 = composite(U, s, Vh, 10)
img20 = composite(U, s, Vh, 20)
img50 = composite(U, s, Vh, 50)

print("------------------------------------------------------------")  # 60個

# 統計-stats
# 連續機率分佈

cc = [k for k, v in stats.__dict__.items() if isinstance(v, stats.rv_continuous)]
print(cc)

cc = stats.norm.stats()
print(cc)

X = stats.norm(loc=1.0, scale=2.0)
cc = X.stats()
print(cc)

x = X.rvs(size=10000)  # 對隨機變數取10000個值
cc = np.mean(x), np.var(x)  # 期望值和方差
print(cc)

cc = stats.norm.fit(x)  # 得到隨機序列期望值和標准差
print(cc)

pdf, t = np.histogram(x, bins=100, normed=True)  # normed 改成 density
t = (t[:-1] + t[1:]) * 0.5  # ❷
cdf = np.cumsum(pdf) * (t[1] - t[0])  # ❸
p_error = pdf - X.pdf(t)
c_error = cdf - X.cdf(t)
print(
    "max pdf error: {}, max cdf error: {}".format(
        np.abs(p_error).max(), np.abs(c_error).max()
    )
)

# max pdf error: 0.0217211429624, max cdf error: 0.0209887986472

# 正態分佈的機率密度函數（左）和累積分佈函數（右）
fig, (ax1, ax2) = pl.subplots(1, 2, figsize=(7, 2))
ax1.plot(t, pdf, label="統計值")
ax1.plot(t, X.pdf(t), label="理論值", alpha=0.6)
ax1.legend(loc="best")
ax2.plot(t, cdf)
ax2.plot(t, X.cdf(t), alpha=0.6)

show()

print("------------------------------------------------------------")  # 60個

print(stats.gamma.stats(1.0))
print(stats.gamma.stats(2.0))

cc = stats.gamma.stats(2.0, scale=2)
print(cc)

x = stats.gamma.rvs(2, scale=2, size=4)
print(x)

cc = stats.gamma.pdf(x, 2, scale=2)
print(cc)

X = stats.gamma(2, scale=2)
cc = X.pdf(x)
print(cc)

print("------------------------------------------------------------")  # 60個

# 離散機率分佈

x = range(1, 7)
p = (0.4, 0.2, 0.1, 0.1, 0.1, 0.1)

dice = stats.rv_discrete(values=(x, p))
cc = dice.rvs(size=20)
print(cc)

samples = dice.rvs(size=(20000, 50))
samples_mean = np.mean(samples, axis=1)
print(samples_mean)

# 核密度估計

# 核密度估計能更準確地表示隨機變數的機率密度函數
_, bins, step = pl.hist(samples_mean, bins=100, histtype="step", label="直方圖統計")
kde = stats.kde.gaussian_kde(samples_mean)
x = np.linspace(bins[0], bins[-1], 100)
pl.plot(x, kde(x), label="核密度估計")
mean, std = stats.norm.fit(samples_mean)
pl.plot(x, stats.norm(mean, std).pdf(x), alpha=0.8, label="正態分佈擬合")
pl.legend()

show()

print("------------------------------------------------------------")  # 60個

# `bw_method`參數越大核密度估計曲線越平順
for bw in [0.2, 0.3, 0.6, 1.0]:
    kde = stats.gaussian_kde([-1, 0, 1], bw_method=bw)
    x = np.linspace(-5, 5, 1000)
    y = kde(x)
    pl.plot(x, y, lw=2, label="bw={}".format(bw), alpha=0.6)

pl.legend(loc="best")

show()

print("------------------------------------------------------------")  # 60個

# 二項、泊松、伽瑪分佈

cc = stats.binom.pmf(range(6), 5, 1 / 6.0)
print(cc)

# 當n足夠大時二項分佈和泊松分佈近似相等
lambda_ = 10.0
x = np.arange(20)

n1, n2 = 100, 1000

y_binom_n1 = stats.binom.pmf(x, n1, lambda_ / n1)
y_binom_n2 = stats.binom.pmf(x, n2, lambda_ / n2)
y_poisson = stats.poisson.pmf(x, lambda_)
print(np.max(np.abs(y_binom_n1 - y_poisson)))
print(np.max(np.abs(y_binom_n2 - y_poisson)))

fig, (ax1, ax2) = pl.subplots(1, 2, figsize=(7.5, 2.5))

ax1.plot(x, y_binom_n1, label="binom", lw=2)
ax1.plot(x, y_poisson, label="poisson", lw=2, color="red")
ax2.plot(x, y_binom_n2, label="binom", lw=2)
ax2.plot(x, y_poisson, label="poisson", lw=2, color="red")
for n, ax in zip((n1, n2), (ax1, ax2)):
    ax.set_xlabel("次數")
    ax.set_ylabel("機率")
    ax.set_title("n={}".format(n))
    ax.legend()
fig.subplots_adjust(0.1, 0.15, 0.95, 0.90, 0.2, 0.1)

show()

print("------------------------------------------------------------")  # 60個

# 類比泊松分佈


def sim_poisson(lambda_, time):
    t = np.random.uniform(0, time, size=lambda_ * time)
    count, time_edges = np.histogram(t, bins=time, range=(0, time))  # ❷
    dist, count_edges = np.histogram(count, bins=20, range=(0, 20), density=True)  # ❸
    x = count_edges[:-1]
    poisson = stats.poisson.pmf(x, lambda_)
    return x, poisson, dist


lambda_ = 10
times = 1000, 50000
x1, poisson1, dist1 = sim_poisson(lambda_, times[0])
x2, poisson2, dist2 = sim_poisson(lambda_, times[1])
max_error1 = np.max(np.abs(dist1 - poisson1))
max_error2 = np.max(np.abs(dist2 - poisson2))
print("time={}, max_error={}".format(times[0], max_error1))
print("time={}, max_error={}".format(times[1], max_error2))

fig, (ax1, ax2) = pl.subplots(1, 2, figsize=(7.5, 2.5))

ax1.plot(x1, dist1, "-o", lw=2, label="統計結果")
ax1.plot(x1, poisson1, "->", lw=2, label="泊松分佈", color="red", alpha=0.6)
ax2.plot(x2, dist2, "-o", lw=2, label="統計結果")
ax2.plot(x2, poisson2, "->", lw=2, label="泊松分佈", color="red", alpha=0.6)

for ax, time in zip((ax1, ax2), times):
    ax.set_xlabel("次數")
    ax.set_ylabel("機率")
    ax.set_title("time = {}".format(time))
    ax.legend(loc="lower center")

fig.subplots_adjust(0.1, 0.15, 0.95, 0.90, 0.2, 0.1)

show()

print("------------------------------------------------------------")  # 60個


# 類比伽瑪分佈
def sim_gamma(lambda_, time, k):
    t = np.random.uniform(0, time, size=int(lambda_ * time))
    t.sort()  # ❷
    interval = t[k:] - t[:-k]  # ❸
    dist, interval_edges = np.histogram(interval, bins=100, density=True)  # ❹
    x = (interval_edges[1:] + interval_edges[:-1]) / 2  # ❺
    gamma = stats.gamma.pdf(x, k, scale=1.0 / lambda_)  # ❺
    return x, gamma, dist


lambda_ = 10.0
time = 1000
ks = 1, 2
x1, gamma1, dist1 = sim_gamma(lambda_, time, ks[0])
x2, gamma2, dist2 = sim_gamma(lambda_, time, ks[1])

fig, (ax1, ax2) = pl.subplots(1, 2, figsize=(7.5, 2.5))

ax1.plot(x1, dist1, lw=2, label="統計結果")
ax1.plot(x1, gamma1, lw=2, label="伽瑪分佈", color="red", alpha=0.6)
ax2.plot(x2, dist2, lw=2, label="統計結果")
ax2.plot(x2, gamma2, lw=2, label="伽瑪分佈", color="red", alpha=0.6)

for ax, k in zip((ax1, ax2), ks):
    ax.set_xlabel("時間間隔")
    ax.set_ylabel("機率密度")
    ax.set_title("k = {}".format(k))
    ax.legend(loc="upper right")

fig.subplots_adjust(0.1, 0.15, 0.95, 0.90, 0.2, 0.1)

show()

print("------------------------------------------------------------")  # 60個

T = 100000
A_count = T // 5
B_count = T // 10

A_time = np.random.uniform(0, T, A_count)
B_time = np.random.uniform(0, T, B_count)

bus_time = np.concatenate((A_time, B_time))  # ❷
bus_time.sort()

N = 200000
passenger_time = np.random.uniform(bus_time[0], bus_time[-1], N)  # ❸

idx = np.searchsorted(bus_time, passenger_time)  # ❹
cc = np.mean(bus_time[idx] - passenger_time) * 60  # ❺
print(cc)

cc = np.mean(np.diff(bus_time)) * 60
print(cc)

# 觀察者偏差

import matplotlib.gridspec as gridspec

pl.figure(figsize=(7.5, 3))

G = gridspec.GridSpec(10, 1)
ax1 = pl.subplot(G[:2, 0])
ax2 = pl.subplot(G[3:, 0])

ax1.vlines(bus_time[:10], 0, 1, lw=2, color="blue", label="公共汽車車")
ptime = np.random.uniform(bus_time[0], bus_time[9], 100)
ax1.vlines(ptime, 0, 1, lw=1, color="red", alpha=0.2, label="乘客")
ax1.legend()
count, bins = np.histogram(passenger_time, bins=bus_time)
ax2.plot(np.diff(bins), count, ".", alpha=0.3, rasterized=True)
ax2.set_xlabel("公共汽車車的時間間隔")
ax2.set_ylabel("等待人數")

show()

t = 10.0 / 3  # 兩輛公共汽車車之間的平均時間間隔
bus_interval = stats.gamma(1, scale=t)
n, _ = integrate.quad(lambda x: 0.5 * x * x * bus_interval.pdf(x), 0, 1000)
d, _ = integrate.quad(lambda x: x * bus_interval.pdf(x), 0, 1000)
cc = n / d * 60
print(cc)

print("------------------------------------------------------------")  # 60個

# 學生t-分佈與t檢驗

# 類比學生t-分佈
mu = 0.0
n = 10
samples = stats.norm(mu).rvs(size=(100000, n))
t_samples = (
    (np.mean(samples, axis=1) - mu) / np.std(samples, ddof=1, axis=1) * n**0.5
)  # ❷
sample_dist, x = np.histogram(t_samples, bins=100, density=True)  # ❸
x = 0.5 * (x[:-1] + x[1:])
t_dist = stats.t(n - 1).pdf(x)
print("max error:", np.max(np.abs(sample_dist - t_dist)))

pl.plot(x, sample_dist, lw=2, label="樣本分佈")
pl.plot(x, t_dist, lw=2, alpha=0.6, label="t分佈")
pl.xlim(-5, 5)
pl.legend(loc="best")

# max error: 0.00658734287935

show()

print("------------------------------------------------------------")  # 60個


# 當`df`增大，學生t-分佈趨向於正態分佈
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.5, 2.5))
ax1.plot(x, stats.t(6 - 1).pdf(x), label="df=5", lw=2)
ax1.plot(x, stats.t(40 - 1).pdf(x), label="df=39", lw=2, alpha=0.6)
ax1.plot(x, stats.norm.pdf(x), "k--", label="norm")
ax1.legend()

ax2.plot(x, stats.t(6 - 1).sf(x), label="df=5", lw=2)
ax2.plot(x, stats.t(40 - 1).sf(x), label="df=39", lw=2, alpha=0.6)
ax2.plot(x, stats.norm.sf(x), "k--", label="norm")
ax2.legend()

show()

print("------------------------------------------------------------")  # 60個

n = 30
s = stats.norm.rvs(loc=1, scale=0.8, size=n)

t = (np.mean(s) - 0.5) / (np.std(s, ddof=1) / np.sqrt(n))
print(t, stats.ttest_1samp(s, 0.5))

# 2.65858434088 (2.6585843408822241, 0.012637702257091229)

print((np.mean(s) - 1) / (np.std(s, ddof=1) / np.sqrt(n)))
print(stats.ttest_1samp(s, 1), stats.ttest_1samp(s, 0.9))

# -1.14501736704
# (-1.1450173670383303, 0.26156414618801477) (-0.38429702545421962, 0.70356191034252025)

# 紅色部分為`ttest_1samp()`計算的p值
x = np.linspace(-5, 5, 500)
y = stats.t(n - 1).pdf(x)
plt.plot(x, y, lw=2)
t, p = stats.ttest_1samp(s, 0.5)
mask = x > np.abs(t)
plt.fill_between(x[mask], y[mask], color="red", alpha=0.5)
mask = x < -np.abs(t)
plt.fill_between(x[mask], y[mask], color="red", alpha=0.5)
plt.axhline(color="k", lw=0.5)
plt.xlim(-5, 5)

show()

print("------------------------------------------------------------")  # 60個
""" NG
print('積分')
x = np.linspace(-10, 10, 100000)
y = stats.t(n-1).pdf(x)
mask = x >= np.abs(t)
cc = integrate.trapz(y[mask], x[mask])*2
print(cc)
"""

m = 200000
mean = 0.5
r = stats.norm.rvs(loc=mean, scale=0.8, size=(m, n))
ts = (np.mean(s) - mean) / (np.std(s, ddof=1) / np.sqrt(n))
tr = (np.mean(r, axis=1) - mean) / (np.std(r, ddof=1, axis=1) / np.sqrt(n))
cc = np.mean(np.abs(tr) > np.abs(ts))
print(cc)

s1 = stats.norm.rvs(loc=1, scale=1.0, size=20)
s2 = stats.norm.rvs(loc=1.5, scale=0.5, size=20)
s3 = stats.norm.rvs(loc=1.5, scale=0.5, size=25)

print(stats.ttest_ind(s1, s2, equal_var=False))
print(stats.ttest_ind(s2, s3, equal_var=True))  # ❷

print("------------------------------------------------------------")  # 60個

# 卡方分佈和卡方檢驗

# 使用隨機數驗證卡方分佈
a = np.random.normal(size=(300000, 4))
cs = np.sum(a**2, axis=1)

sample_dist, bins = np.histogram(cs, bins=100, range=(0, 20), density=True)
x = 0.5 * (bins[:-1] + bins[1:])
chi2_dist = stats.chi2.pdf(x, 4)
print("max error:", np.max(np.abs(sample_dist - chi2_dist)))

pl.plot(x, sample_dist, lw=2, label="樣本分佈")
pl.plot(x, chi2_dist, lw=2, alpha=0.6, label="$\chi ^{2}$分佈")
pl.legend(loc="best")

# max error: 0.00340194486328

show()

print("------------------------------------------------------------")  # 60個

# 類比卡方分佈
repeat_count = 60000
n, k = 100, 5

ball_ids = np.random.randint(0, k, size=(repeat_count, n))
counts = np.apply_along_axis(np.bincount, 1, ball_ids, minlength=k)  # ❷
cs2 = np.sum((counts - n / k) ** 2.0 / (n / k), axis=1)  # ❸
k = stats.kde.gaussian_kde(cs2)  # ❹
x = np.linspace(0, 10, 200)
pl.plot(x, stats.chi2.pdf(x, 4), lw=2, label="$\chi ^{2}$分佈")
pl.plot(x, k(x), lw=2, color="red", alpha=0.6, label="樣本分佈")
pl.legend(loc="best")
pl.xlim(0, 10)

show()

print("------------------------------------------------------------")  # 60個


def choose_balls(probabilities, size):
    r = stats.rv_discrete(values=(range(len(probabilities)), probabilities))
    s = r.rvs(size=size)
    counts = np.bincount(s)
    return counts


counts1 = choose_balls([0.18, 0.24, 0.25, 0.16, 0.17], 400)
counts2 = choose_balls([0.2] * 5, 400)

print(counts1)
print(counts2)

chi1, p1 = stats.chisquare(counts1)
chi2, p2 = stats.chisquare(counts2)

print("chi1 =", chi1, "p1 =", p1)
print("chi2 =", chi2, "p2 =", p2)

# chi1 = 11.375 p1 = 0.0226576012398
# chi2 = 2.55 p2 = 0.635705452704

# 卡方檢驗計算的機率為陰影部分的面積
x = np.linspace(0, 30, 200)
CHI2 = stats.chi2(4)
pl.plot(x, CHI2.pdf(x), "k", lw=2)
pl.vlines(chi1, 0, CHI2.pdf(chi1))
pl.vlines(chi2, 0, CHI2.pdf(chi2))
pl.fill_between(x[x > chi1], 0, CHI2.pdf(x[x > chi1]), color="red", alpha=1.0)
pl.fill_between(x[x > chi2], 0, CHI2.pdf(x[x > chi2]), color="green", alpha=0.5)
pl.text(chi1, 0.015, r"$\chi^2_1$", fontsize=14)
pl.text(chi2, 0.015, r"$\chi^2_2$", fontsize=14)
pl.ylim(0, 0.2)
pl.xlim(0, 20)

show()

print("------------------------------------------------------------")  # 60個

table = [[43, 9], [44, 4]]
chi2, p, dof, expected = stats.chi2_contingency(table)
print(chi2)
print(p)

cc = stats.fisher_exact(table)
print(cc)

print("------------------------------------------------------------")  # 60個

# 數值積分-integrate
# 球的體積


def half_circle(x):
    return (1 - x**2) ** 0.5


N = 10000
x = np.linspace(-1, 1, N)
dx = x[1] - x[0]
y = half_circle(x)
cc = 2 * dx * np.sum(y)  # 面積的兩倍
print(cc)

cc = np.trapz(y, x) * 2  # 面積的兩倍
print(cc)

pi_half, err = integrate.quad(half_circle, -1, 1)
cc = pi_half * 2
print(cc)


def half_sphere(x, y):
    return (1 - x**2 - y**2) ** 0.5


volume, error = integrate.dblquad(
    half_sphere, -1, 1, lambda x: -half_circle(x), lambda x: half_circle(x)
)

print(volume, error, np.pi * 4 / 3 / 2)

print("------------------------------------------------------------")  # 60個

# 解常微分方程式群組

# 目前畫不出來

# 洛倫茨吸引子：微小的初值差別也會顯著地影響運動軌跡


def lorenz(w, t, p, r, b):
    # 舉出位置向量w，和三個參數p, r, b計算出
    # dx/dt, dy/dt, dz/dt的值
    x, y, z = w.tolist()
    # 直接與lorenz的計算公式對應
    return p * (y - x), x * (r - z) - y, x * y - b * z


t = np.arange(0, 30, 0.02)  # 建立時間點
# 呼叫ode對lorenz進行求解, 用兩個不同的初值
track1 = odeint(lorenz, (0.0, 1.00, 0.0), t, args=(10.0, 28.0, 3.0))  # ❷
track2 = odeint(lorenz, (0.0, 1.01, 0.0), t, args=(10.0, 28.0, 3.0))  # ❸

from mpl_toolkits.mplot3d import Axes3D

fig = pl.figure()
ax = Axes3D(fig)
ax.plot(track1[:, 0], track1[:, 1], track1[:, 2], lw=1)
ax.plot(track2[:, 0], track2[:, 1], track2[:, 2], lw=1)

show()

print("------------------------------------------------------------")  # 60個

# ode類別


def mass_spring_damper(xu, t, m, k, b, F):
    x, u = xu.tolist()
    dx = u
    du = (F - k * x - b * u) / m
    return dx, du


# 滑動區塊的速度和位移曲線
m, b, k, F = 1.0, 10.0, 20.0, 1.0
init_status = 0.0, 0.0
args = m, k, b, F
t = np.arange(0, 2, 0.01)
result = odeint(mass_spring_damper, init_status, t, args)

fig, (ax1, ax2) = pl.subplots(2, 1)
ax1.plot(t, result[:, 0], label="位移")
ax1.legend()
ax2.plot(t, result[:, 1], label="速度")
ax2.legend()

show()

print("------------------------------------------------------------")  # 60個


class MassSpringDamper(object):
    def __init__(self, m, k, b, F):
        self.m, self.k, self.b, self.F = m, k, b, F

    def f(self, t, xu):
        x, u = xu.tolist()
        dx = u
        du = (self.F - self.k * x - self.b * u) / self.m
        return [dx, du]


system = MassSpringDamper(m=m, k=k, b=b, F=F)
init_status = 0.0, 0.0
dt = 0.01

r = ode(system.f)  # ❷
r.set_integrator("vode", method="bdf")
r.set_initial_value(init_status, 0)

t = []
result2 = [init_status]
while r.successful() and r.t + dt < 2:  # ❸
    r.integrate(r.t + dt)
    t.append(r.t)
    result2.append(r.y)

result2 = np.array(result2)
cc = np.allclose(result, result2)
print(cc)

print("------------------------------------------------------------")  # 60個


class PID(object):
    def __init__(self, kp, ki, kd, dt):
        self.kp, self.ki, self.kd, self.dt = kp, ki, kd, dt
        self.last_error = None
        self.status = 0.0

    def update(self, error):
        p = self.kp * error
        i = self.ki * self.status
        if self.last_error is None:
            d = 0.0
        else:
            d = self.kd * (error - self.last_error) / self.dt
        self.status += error * self.dt
        self.last_error = error
        return p + i + d


# 使用PID控制器讓滑動區塊停在位移為1.0處
def pid_control_system(kp, ki, kd, dt, target=1.0):
    system = MassSpringDamper(m=m, k=k, b=b, F=0.0)
    pid = PID(kp, ki, kd, dt)
    init_status = 0.0, 0.0

    r = ode(system.f)
    r.set_integrator("vode", method="bdf")
    r.set_initial_value(init_status, 0)

    t = [0]
    result = [init_status]
    F_arr = [0]

    while r.successful() and r.t + dt < 2.0:
        r.integrate(r.t + dt)
        err = target - r.y[0]
        F = pid.update(err)  # ❷
        system.F = F  # ❸
        t.append(r.t)
        result.append(r.y)
        F_arr.append(F)

    result = np.array(result)
    t = np.array(t)
    F_arr = np.array(F_arr)
    return t, F_arr, result


t, F_arr, result = pid_control_system(50.0, 100.0, 10.0, 0.001)
print("控制力的終值:", F_arr[-1])

fig, (ax1, ax2, ax3) = pl.subplots(3, 1, figsize=(6, 6))
ax1.plot(t, result[:, 0], label="位移")
ax1.legend(loc="best")
ax2.plot(t, result[:, 1], label="速度")
ax2.legend(loc="best")
ax3.plot(t, F_arr, label="控制力")
ax3.legend(loc="best")

# 控制力的終值: 19.9434046839

show()

print("------------------------------------------------------------")  # 60個


def eval_func(k):
    kp, ki, kd = k
    t, F_arr, result = pid_control_system(kp, ki, kd, 0.01)
    return np.sum(np.abs(result[:, 0] - 1.0))


kwargs = {
    "method": "L-BFGS-B",
    "bounds": [(10, 200), (10, 100), (1, 100)],
    "options": {"approx_grad": True},
}

opt_k = optimize.basinhopping(
    eval_func, (10, 10, 10), niter=10, minimizer_kwargs=kwargs
)
print(opt_k.x)

# 改善PID的參數降低控制響應時間
kp, ki, kd = opt_k.x
t, F_arr, result = pid_control_system(kp, ki, kd, 0.01)
idx = np.argmin(np.abs(t - 0.5))
x, u = result[idx]
print("t={}, x={:g}, u={:g}".format(t[idx], x, u))

fig, (ax1, ax2, ax3) = pl.subplots(3, 1, figsize=(6, 6))
ax1.plot(t, result[:, 0], label="位移")
ax1.legend(loc="best")
ax2.plot(t, result[:, 1], label="速度")
ax2.legend(loc="best")
ax3.plot(t, F_arr, label="控制力")
ax3.legend(loc="best")

show()

print("------------------------------------------------------------")  # 60個

# 中值濾波

# 使用中值濾波剔除瞬間噪聲
t = np.arange(0, 20, 0.1)
x = np.sin(t)
x[np.random.randint(0, len(t), 20)] += np.random.standard_normal(20) * 0.6
x2 = signal.medfilt(x, 5)  # ❷
x3 = signal.order_filter(x, np.ones(5), 2)
print(np.all(x2 == x3))
pl.plot(t, x, label="帶噪聲的訊號")
pl.plot(t, x2 + 0.5, alpha=0.6, label="中值濾波之後的訊號")
pl.legend(loc="best")

# True

show()

print("------------------------------------------------------------")  # 60個

# 濾波器設計

sampling_rate = 8000.0

# 設計一個帶通濾波器：
# 通帶為0.2*4000 - 0.5*4000
# 阻帶為<0.1*4000, >0.6*4000
# 通帶增益的最大衰減值為2dB
# 阻帶的最小衰減值為40dB
b, a = signal.iirdesign([0.2, 0.5], [0.1, 0.6], 2, 40)

# 使用freq計算濾波器的頻率響應
w, h = signal.freqz(b, a)  # ❷

# 計算增益
power = 20 * np.log10(np.clip(np.abs(h), 1e-8, 1e100))  # ❸
freq = w / np.pi * sampling_rate / 2

# 用頻率掃描波測量的頻率響應
# 產生2秒鍾的取樣頻率為sampling_rate Hz的頻率掃描訊號
# 開始頻率為0， 結束頻率為sampling_rate/2
t = np.arange(0, 2, 1 / sampling_rate)
sweep = signal.chirp(t, f0=0, t1=2, f1=sampling_rate / 2)  # ❷
# 對頻率掃描訊號進行濾波
out = signal.lfilter(b, a, sweep)  # ❸
# 將波形轉為能量
out = 20 * np.log10(np.abs(out))  # ❹
# 找到所有局部最大值的索引
index = signal.argrelmax(out, order=3)  # ❺
# 繪制濾波之後的波形的增益
pl.figure(figsize=(8, 2.5))
pl.plot(freq, power, label="帶通IIR濾波器的頻率響應")
pl.plot(t[index] / 2.0 * 4000, out[index], label="頻率掃描波測量的頻譜", alpha=0.6)  # ❻
pl.legend(loc="best")

pl.title("頻率掃描波測量的濾波器頻譜")
pl.ylim(-100, 20)
pl.ylabel("增益(dB)")
pl.xlabel("頻率(Hz)")

show()

print("------------------------------------------------------------")  # 60個

# 連續時間線性系統

# 系統的階躍響應和正弦波響應
m, b, k = 1.0, 10, 20

numerator = [1]
denominator = [m, b, k]

plant = signal.lti(numerator, denominator)

t = np.arange(0, 2, 0.01)
_, x_step = plant.step(T=t)  # ❷
_, x_sin, _ = signal.lsim(plant, U=np.sin(np.pi * t), T=t)  # ❸

pl.plot(t, x_step, label="階躍響應")
pl.plot(t, x_sin, label="正弦波響應")
pl.legend(loc="best")
pl.xlabel("時間（秒）")
pl.ylabel("位移（米）")

show()

print("------------------------------------------------------------")  # 60個

""" NG
from numbers import Real

def as_sys(s):
    if isinstance(s, Real):
        return SYS([s], [1])
    return s

class SYS(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den
        
    def feedback(self):
        return self / (self + 1)
        
    def __mul__(self, s):
        s = as_sys(s)
        num = np.polymul(self.num, s.num)
        den = np.polymul(self.den, s.den)
        return SYS(num, den)
    
    def __add__(self, s):
        s = as_sys(s)
        den = np.polymul(self.den, s.den)
        num = np.polyadd(np.polymul(self.num, s.den),
                         np.polymul(s.num, self.den))
        return SYS(num, den)
    
    def __sadd__(self, s):
        return self + s

    def __div__(self, s):
        s = as_sys(s)
        return self * SYS(s.den, s.num)
    
    def __iter__(self): #❷
        return iter((self.num, self.den))    

# 使用PI控制器的控制系統的階躍響應
M, b, k = 1.0, 10, 20
plant = SYS([1], [M, b, k])

pi_settings = [(10, 1e-10), (200, 1e-10),
               (200, 100),  (50, 100)]

fig, ax = pl.subplots(figsize=(8, 3))

for pi_setting in pi_settings:
    pi_ctrl = SYS(pi_setting, [1, 1e-6]) #❷
    feedback = (pi_ctrl * plant).feedback() #❸
    _, x = signal.step(feedback, T=t)    
    label = "$K_p={:d}, K_i={:3.0f}$".format(*pi_setting)
    ax.plot(t, x, label=label)
    
ax.legend(loc="best", ncol=2)
ax.set_xlabel(u"時間（秒）")
ax.set_ylabel(u"位移（米）");

show()

_, f, _ = signal.lsim(pi_ctrl, U=1-x, T=t)

kd, kp, ki = 30, 200, 400
pid_ctrl = SYS([kd, kp, ki], [1, 1e-6])
feedback = (pid_ctrl * plant).feedback()
_, x2 = signal.step(feedback, T=t)

lp = SYS([1], [0.2, 1])
lp_feedback = lp * (pid_ctrl * plant).feedback()
_, x3 = signal.step(lp_feedback, T=t)

pid_out = (pid_ctrl * lp) / (pid_ctrl * plant + 1)
_, f3 = signal.step(pid_out, T=t)

# 滑動區塊的位移以及控制力
fig, (ax1, ax2) = pl.subplots(1, 2, figsize=(10, 3))
ax1.plot(t, x, label=u"PI控制")
ax1.plot(t, x2, label=u"PID控制")
ax1.plot(t, x3, label=u"低通+PID控制")
ax2.plot(t, f, label=u"PI控制")
ax2.plot(t, f3, color="r", label=u"低通+PID控制")
ax1.legend(loc="best")
ax2.legend(loc="best")
ax1.set_title(u"目的系統的位移")
ax2.set_title(u"控制力");

show()
"""
print("------------------------------------------------------------")  # 60個

# 一維插值
# 高次interp1d()插值的運算量很大，因此對於點數較多的資料，
# 建議使用後面介紹的UnivariateSpline()。

# `interp1d`的各階插值

x = np.linspace(0, 10, 11)
y = np.sin(x)

xnew = np.linspace(0, 10, 101)
pl.plot(x, y, "ro")
for kind in ["nearest", "zero", "slinear", "quadratic"]:
    f = interpolate.interp1d(x, y, kind=kind)
    ynew = f(xnew)  # ❷
    pl.plot(xnew, ynew, label=str(kind))

pl.legend(loc="lower right")

show()

print("------------------------------------------------------------")  # 60個

# 外推和Spline擬合

# 使用UnivariateSpline進行插值：外推（上），資料擬合（下）
x1 = np.linspace(0, 10, 20)
y1 = np.sin(x1)
sx1 = np.linspace(0, 12, 100)
sy1 = interpolate.UnivariateSpline(x1, y1, s=0)(sx1)

x2 = np.linspace(0, 20, 200)
y2 = np.sin(x2) + np.random.standard_normal(len(x2)) * 0.2
sx2 = np.linspace(0, 20, 2000)
spline2 = interpolate.UnivariateSpline(x2, y2, s=8)  # ❷
sy2 = spline2(sx2)

pl.figure(figsize=(8, 5))
pl.subplot(211)
pl.plot(x1, y1, ".", label="資料點")
pl.plot(sx1, sy1, label="spline曲線")
pl.legend()

pl.subplot(212)
pl.plot(x2, y2, ".", label="資料點")
pl.plot(sx2, sy2, linewidth=2, label="spline曲線")
pl.plot(x2, np.sin(x2), label="無噪聲曲線")
pl.legend()

show()

print(np.array_str(spline2.roots(), precision=3))
# [  3.288   6.329   9.296  12.578  15.75   18.805]

print("------------------------------------------------------------")  # 60個


# 計算Spline與水平線的交點
def roots_at(self, v):
    coeff = self.get_coeffs()
    coeff -= v
    try:
        root = self.roots()
        return root
    finally:
        coeff += v


interpolate.UnivariateSpline.roots_at = roots_at  # ❷

pl.plot(sx2, sy2, linewidth=2, label="spline曲線")

ax = pl.gca()
for level in [0.5, 0.75, -0.5, -0.75]:
    ax.axhline(level, ls=":", color="k")
    xr = spline2.roots_at(level)  # ❸
    pl.plot(xr, spline2(xr), "ro")

show()

print("------------------------------------------------------------")  # 60個

# 參數插值

# 使用參數插值連線二維平面上的點
x = [
    4.913,
    4.913,
    4.918,
    4.938,
    4.955,
    4.949,
    4.911,
    4.848,
    4.864,
    4.893,
    4.935,
    4.981,
    5.01,
    5.021,
]

y = [
    5.2785,
    5.2875,
    5.291,
    5.289,
    5.28,
    5.26,
    5.245,
    5.245,
    5.2615,
    5.278,
    5.2775,
    5.261,
    5.245,
    5.241,
]

pl.plot(x, y, "o")

for s in (0, 1e-4):
    tck, t = interpolate.splprep([x, y], s=s)
    xi, yi = interpolate.splev(np.linspace(t[0], t[-1], 200), tck)  # ❷
    pl.plot(xi, yi, lw=2, label="s=%g" % s)

pl.legend()

show()

print("------------------------------------------------------------")  # 60個
""" NG
#單調插值

# 單調插值能確保兩個點之間的曲線為單調遞增或遞減
x = [0, 1, 2, 3, 4, 5]
y = [1, 2, 1.5, 2.5, 3, 2.5]
xs = np.linspace(x[0], x[-1], 100)
curve = interpolate.pchip(x, y)
ys = curve(xs)
dys = curve.derivative(xs)
pl.plot(xs, ys, label=u"pchip")
pl.plot(xs, dys, label=u"一階導數")
pl.plot(x, y, "o")
pl.legend(loc="best")
pl.grid()
pl.margins(0.1, 0.1)

show()
"""
print("------------------------------------------------------------")  # 60個

""" interp2d removed
#多維插值

# 使用interp2d類別進行二維插值
def func(x, y):
    return (x+y)*np.exp(-5.0*(x**2 + y**2))

# X-Y軸分為15*15的網格
y, x = np.mgrid[-1:1:15j, -1:1:15j] #❷
fvals = func(x, y) # 計算每個網格點上的函數值

# 二維插值
newfunc = interpolate.interp2d(x, y, fvals, kind='cubic') #❸

# 計算100*100的網格上的插值
xnew = np.linspace(-1,1,100)
ynew = np.linspace(-1,1,100)
fnew = newfunc(xnew, ynew) #❹

pl.subplot(121)
pl.imshow(fvals, extent=[-1,1,-1,1], cmap=pl.cm.jet, interpolation='nearest', origin="lower")
pl.title("fvals")
pl.subplot(122)
pl.imshow(fnew, extent=[-1,1,-1,1], cmap=pl.cm.jet, interpolation='nearest', origin="lower")
pl.title("fnew")
pl.show()

show()
"""
print("------------------------------------------------------------")  # 60個


def func(x, y):
    return (x + y) * np.exp(-5.0 * (x**2 + y**2))


# griddata

# griddata()使用歐幾裡得距離計算插值。
# 若果K維空間中每個維度的取值範圍相差較大，則應先將資料正式化，
# 然後使用griddata()進行插值運算。

# 使用gridata進行二維插值
# 計算隨機N個點的座標，以及這些點對應的函數值
N = 200
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)
z = func(x, y)

yg, xg = np.mgrid[-1:1:100j, -1:1:100j]
xi = np.c_[xg.ravel(), yg.ravel()]

methods = "nearest", "linear", "cubic"

zgs = [
    interpolate.griddata((x, y), z, xi, method=method).reshape(100, 100)
    for method in methods
]

fig, axes = pl.subplots(1, 3, figsize=(11.5, 3.5))

for ax, method, zg in zip(axes, methods, zgs):
    ax.imshow(
        zg,
        extent=[-1, 1, -1, 1],
        cmap=pl.cm.jet,
        interpolation="nearest",
        origin="lower",
    )
    ax.set_xlabel(method)
    ax.scatter(x, y, c=z)

show()

print("------------------------------------------------------------")  # 60個

# 徑向基函數插值

# 一維RBF插值
from scipy.interpolate import Rbf

x1 = np.array([-1, 0, 2.0, 1.0])
y1 = np.array([1.0, 0.3, -0.5, 0.8])

funcs = ["multiquadric", "gaussian", "linear"]
nx = np.linspace(-3, 4, 100)
rbfs = [Rbf(x1, y1, function=fname) for fname in funcs]
rbf_ys = [rbf(nx) for rbf in rbfs]  # ❷

pl.plot(x1, y1, "o")
for fname, ny in zip(funcs, rbf_ys):
    pl.plot(nx, ny, label=fname, lw=2)

pl.ylim(-1.0, 1.5)
pl.legend()

show()

print("------------------------------------------------------------")  # 60個

for fname, rbf in zip(funcs, rbfs):
    print(fname, rbf.nodes)

"""
multiquadric [ -3.79570791   9.82703701   5.08190777 -11.13103777]
gaussian [ 1.78016841 -1.83986382 -1.69565607  2.5266374 ]
linear [-0.26666667  0.6         0.73333333 -0.9       ]
"""

# 二維徑向基函數插值
rbfs = [Rbf(x, y, z, function=fname) for fname in funcs]
rbf_zg = [rbf(xg, yg).reshape(xg.shape) for rbf in rbfs]

fig, axes = pl.subplots(1, 3, figsize=(11.5, 3.5))
for ax, fname, zg in zip(axes, funcs, rbf_zg):
    ax.imshow(
        zg,
        extent=[-1, 1, -1, 1],
        cmap=pl.cm.jet,
        interpolation="nearest",
        origin="lower",
    )
    ax.set_xlabel(fname)
    ax.scatter(x, y, c=z)

show()

print("------------------------------------------------------------")  # 60個

# `epsilon`參數指定徑向基函數中資料點的作用範圍
epsilons = 0.1, 0.15, 0.3
rbfs = [Rbf(x, y, z, function="gaussian", epsilon=eps) for eps in epsilons]
zgs = [rbf(xg, yg).reshape(xg.shape) for rbf in rbfs]

fig, axes = pl.subplots(1, 3, figsize=(11.5, 3.5))
for ax, eps, zg in zip(axes, epsilons, zgs):
    ax.imshow(
        zg,
        extent=[-1, 1, -1, 1],
        cmap=pl.cm.jet,
        interpolation="nearest",
        origin="lower",
    )
    ax.set_xlabel("eps=%g" % eps)
    ax.scatter(x, y, c=z)

show()

print("------------------------------------------------------------")  # 60個

# 稀疏矩陣的儲存形式

a = sparse.dok_matrix((10, 5))
a[2:5, 3] = 1.0, 2.0, 3.0
print(a.keys())
print(a.values())

b = sparse.lil_matrix((10, 5))
b[2, 3] = 1.0
b[3, 4] = 2.0
b[3, 2] = 3.0
print(b.data)
print(b.rows)

row = [2, 3, 3, 2]
col = [3, 4, 2, 3]
data = [1, 2, 3, 10]
c = sparse.coo_matrix((data, (row, col)), shape=(5, 6))
print(c.col, c.row, c.data)
print(c.toarray())


w = sparse.dok_matrix((4, 4))

edges = [(0, 1, 10), (1, 2, 5), (0, 2, 3), (2, 3, 7), (3, 0, 4), (3, 2, 6)]

for i, j, v in edges:
    w[i, j] = v

cc = w.todense()
print(cc)

""" no file
img = pl.imread("maze.png")
sx, sy = (400, 979)
ex, ey = (398,  25)
bimg = np.all(img > 0.81, axis=2)
H, W = bimg.shape

x0, x1 = np.where(bimg[H//2, :]==0)[0][[0, -1]] #❷
bimg[H//2, :x0] = 0
bimg[H//2, x1:] = 0

#上下相鄰白色像素
mask = (bimg[1:, :] & bimg[:-1, :]) 
idx = np.where(mask.ravel())[0]
vedge = np.c_[idx, idx + W]
pl.imsave("tmp.png", mask, cmap="gray")

#左右相鄰白色像素
mask = (bimg[:, 1:] & bimg[:, :-1])
y, x = np.where(mask)
idx = y * W + x
hedge = np.c_[idx, idx + 1]

edges = np.vstack([vedge, hedge])

values = np.ones(edges.shape[0])
w = sparse.coo_matrix((values, (edges[:, 0], edges[:, 1])),  #❷
                      shape=(bimg.size, bimg.size))

startid = sy * W + sx
endid   = ey * W + ex
d, p = csgraph.dijkstra(w, indices=[startid], return_predecessors=True, directed=False)

print(d.shape)
print(p.shape)

cc = np.isinf(d[0]).sum()
print(cc)

path = []
node_id = endid
while True:
    path.append(node_id)
    if node_id == startid or node_id < 0:
        break
    node_id = p[0, node_id]
path = np.array(path)

# 用dijkstra計算最短路徑
x, y = path % W, path // W
img[y, x, :] = 0
fig, axes = pl.subplots(1, 2, figsize=(16, 12))
axes[0].imshow(img)
axes[1].imshow(bimg, cmap="gray")
for ax in axes:
    ax.axis("off")
fig.subplots_adjust(0, 0, 1, 1, 0, 0)

show()
"""
print("------------------------------------------------------------")  # 60個

# 圖形處理-ndimage
# 形態學圖形處理


def expand_image(img, value, out=None, size=10):
    if out is None:
        w, h = img.shape
        out = np.zeros((w * size, h * size), dtype=np.uint8)

    tmp = np.repeat(np.repeat(img, size, 0), size, 1)
    out[:, :] = np.where(tmp, value, out)
    out[::size, :] = 0
    out[:, ::size] = 0
    return out


def show_image(*imgs):
    for idx, img in enumerate(imgs, 1):
        ax = pl.subplot(1, len(imgs), idx)
        pl.imshow(img, cmap="gray")
        ax.set_axis_off()
    pl.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)


# 膨脹和腐蝕

# 四連通和八連通的膨脹運算
from scipy.ndimage import morphology


def dilation_demo(a, structure=None):
    b = morphology.binary_dilation(a, structure)
    img = expand_image(a, 255)
    return expand_image(np.logical_xor(a, b), 150, out=img)


a = pl.imread("scipy_morphology_demo.png")[:, :, 0].astype(np.uint8)
img1 = expand_image(a, 255)

img2 = dilation_demo(a)
img3 = dilation_demo(a, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
show_image(img1, img2, img3)

show()

print("------------------------------------------------------------")  # 60個

# 不同結構元素的膨脹效果
img4 = dilation_demo(a, [[0, 0, 0], [1, 1, 1], [0, 0, 0]])
img5 = dilation_demo(a, [[0, 1, 0], [0, 1, 0], [0, 1, 0]])
img6 = dilation_demo(a, [[0, 1, 0], [0, 1, 0], [0, 0, 0]])
show_image(img4, img5, img6)

show()

print("------------------------------------------------------------")  # 60個


# 四連通和八連通的腐蝕運算
def erosion_demo(a, structure=None):
    b = morphology.binary_erosion(a, structure)
    img = expand_image(a, 255)
    return expand_image(np.logical_xor(a, b), 100, out=img)


img1 = expand_image(a, 255)
img2 = erosion_demo(a)
img3 = erosion_demo(a, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
show_image(img1, img2, img3)

show()

print("------------------------------------------------------------")  # 60個

# Hit和Miss


# Hit和Miss運算
def hitmiss_demo(a, structure1, structure2):
    b = morphology.binary_hit_or_miss(a, structure1, structure2)
    img = expand_image(a, 100)
    return expand_image(b, 255, out=img)


img1 = expand_image(a, 255)

img2 = hitmiss_demo(
    a, [[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
)
img3 = hitmiss_demo(
    a, [[0, 0, 0], [0, 0, 0], [1, 1, 1]], [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
)

show_image(img1, img2, img3)

show()

print("------------------------------------------------------------")  # 60個


# 使用Hit和Miss進行細線化運算
def skeletonize(img):
    h1 = np.array([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
    m1 = np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]])
    h2 = np.array([[0, 0, 0], [1, 1, 0], [0, 1, 0]])
    m2 = np.array([[0, 1, 1], [0, 0, 1], [0, 0, 0]])
    hit_list = []
    miss_list = []
    for k in range(4):  # ❷
        hit_list.append(np.rot90(h1, k))
        hit_list.append(np.rot90(h2, k))
        miss_list.append(np.rot90(m1, k))
        miss_list.append(np.rot90(m2, k))
    img = img.copy()
    while True:
        last = img
        for hit, miss in zip(hit_list, miss_list):
            hm = morphology.binary_hit_or_miss(img, hit, miss)  # ❸
            # 從圖形中移除hit_or_miss所得到的白色點
            img = np.logical_and(img, np.logical_not(hm))  # ❹
        # 若果處理之後的圖形和處理前的圖形相同，則結束處理
        if np.all(img == last):  # ❺
            break
    return img


a = pl.imread("scipy_morphology_demo2.png")[:, :, 0].astype(np.uint8)
b = skeletonize(a)

_, (ax1, ax2) = pl.subplots(1, 2, figsize=(9, 3))
ax1.imshow(a, cmap="gray", interpolation="nearest")
ax2.imshow(b, cmap="gray", interpolation="nearest")
ax1.set_axis_off()
ax2.set_axis_off()
pl.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)

show()

print("------------------------------------------------------------")  # 60個

# 圖形分割

squares = pl.imread("suqares.jpg")
squares = (squares[:, :, 0] < 200).astype(np.uint8)

from scipy.ndimage import morphology

squares_dt = morphology.distance_transform_cdt(squares)
print("各種距離值", np.unique(squares_dt))

squares_core = (squares_dt > 8).astype(np.uint8)

from scipy.ndimage.measurements import label, center_of_mass


def random_palette(labels, count):
    palette = np.random.rand(count + 1, 3)
    palette[0, :] = 0
    return palette[labels]


labels, count = label(squares_core)
h, w = labels.shape
centers = np.array(center_of_mass(labels, labels, index=range(1, count + 1)), np.int)
cores = random_palette(labels, count)

index = morphology.distance_transform_cdt(
    1 - squares_core, return_distances=False, return_indices=True
)
near_labels = labels[index[0], index[1]]  # ❷

mask = (squares - squares_core).astype(bool)
labels2 = labels.copy()
labels2[mask] = near_labels[mask]  # ❸
separated = random_palette(labels2, count)

# 矩形區域分割算法各個步驟的輸出圖形
fig, axes = pl.subplots(
    2,
    3,
    figsize=(7.5, 5.0),
)
fig.delaxes(axes[1, 2])
axes[0, 0].imshow(squares, cmap="gray")
axes[0, 1].imshow(squares_dt)
axes[0, 2].imshow(squares_core, cmap="gray")
ax = axes[1, 0]
ax.imshow(cores)
center_y, center_x = centers.T
ax.plot(center_x, center_y, "o", color="white")
ax.set_xlim(0, w)
ax.set_ylim(h, 0)

axes[1, 1].imshow(separated)

for ax in axes.ravel():
    ax.axis("off")

fig.subplots_adjust(wspace=0.01, hspace=0.01)

show()

print("------------------------------------------------------------")  # 60個

import pylab as pl

# 計算最近旁點

x = np.sort(np.random.rand(100))
idx = np.searchsorted(x, 0.5)
print(x[idx], x[idx - 1])  # 距離0.5最近的數是這兩個數中的一個

# 0.542258714465 0.492205345391

N = 100
points = np.random.uniform(-1, 1, (N, 2))
kd = spatial.cKDTree(points)

targets = np.array([(0, 0), (0.5, 0.5), (-0.5, 0.5), (0.5, -0.5), (-0.5, -0.5)])
dist, idx = kd.query(targets, 3)
print(dist)
print(idx)

r = 0.2
idx2 = kd.query_ball_point(targets, r)
print(idx2)

idx3 = kd.query_pairs(0.1) - kd.query_pairs(0.08)
print(idx3)

# 用cKDTree尋找近旁點
x, y = points.T
colors = "r", "b", "g", "y", "k"

fig, (ax1, ax2, ax3) = pl.subplots(1, 3, figsize=(12, 4))

for ax in ax1, ax2, ax3:
    ax.set_aspect("equal")
    ax.plot(x, y, "o", markersize=4)

for ax in ax1, ax2:
    for i in range(len(targets)):
        c = colors[i]
        tx, ty = targets[i]
        ax.plot([tx], [ty], "*", markersize=10, color=c)

for i in range(len(targets)):
    nx, ny = points[idx[i]].T
    ax1.plot(
        nx,
        ny,
        "o",
        markersize=10,
        markerfacecolor="None",
        markeredgecolor=colors[i],
        markeredgewidth=1,
    )

    nx, ny = points[idx2[i]].T
    ax2.plot(
        nx,
        ny,
        "o",
        markersize=10,
        markerfacecolor="None",
        markeredgecolor=colors[i],
        markeredgewidth=1,
    )

    ax2.add_artist(pl.Circle(targets[i], r, fill=None, linestyle="dashed"))

for pidx1, pidx2 in idx3:
    sx, sy = points[pidx1]
    ex, ey = points[pidx2]
    ax3.plot([sx, ex], [sy, ey], "r", linewidth=2, alpha=0.6)

ax1.set_xlabel("搜尋最近的3個近旁點")
ax2.set_xlabel("搜尋距離在0.2之內的所有近旁點")
ax3.set_xlabel("搜尋所有距離在0.08到0.1之間的點對")

show()

print("------------------------------------------------------------")  # 60個

from scipy.spatial import distance

dist1 = distance.squareform(distance.pdist(points))
dist2 = distance.cdist(points, targets)
print(dist1.shape)
print(dist2.shape)

print(dist[:, 0])  # cKDTree.query()傳回的與targets最近的距離
print(np.min(dist2, axis=0))

dist1[np.diag_indices(len(points))] = np.inf
nearest_pair = np.unravel_index(np.argmin(dist1), dist1.shape)
print(nearest_pair, dist1[nearest_pair])

dist, idx = kd.query(points, 2)
print(idx[np.argmin(dist[:, 1])], np.min(dist[:, 1]))

N = 1000000
start = np.random.uniform(0, 100, N)
span = np.random.uniform(0.01, 1, N)
span = np.clip(span, 2, 100)
end = start + span


def naive_count_at(start, end, time):
    mask = (start < time) & (end > time)
    return np.sum(mask)


# 使用二維K-d樹搜尋指定區間的線上使用者
def _():
    N = 100
    start = np.random.uniform(0, 100, N)
    span = np.random.normal(40, 10, N)
    span = np.clip(span, 2, 100)
    end = start + span

    time = 40

    fig, ax = pl.subplots(figsize=(8, 6))
    ax.scatter(start, end)
    mask = (start < time) & (end > time)
    start2, end2 = start[mask], end[mask]
    ax.scatter(start2, end2, marker="x", color="red")
    rect = pl.Rectangle((-20, 40), 60, 120, alpha=0.3)
    ax.add_patch(rect)
    ax.axhline(time, color="k", ls="--")
    ax.axvline(time, color="k", ls="--")
    ax.set_xlabel("Start")
    ax.set_ylabel("End")
    ax.set_xlim(-20, 120)
    ax.set_ylim(-20, 160)
    ax.plot([0, 120], [0, 120])


_()

show()


class KdSearch(object):
    def __init__(self, start, end, leafsize=10):
        self.tree = spatial.cKDTree(np.c_[start, end], leafsize=leafsize)
        self.max_time = np.max(end)

    def count_at(self, time):
        max_time = self.max_time
        to_search = spatial.cKDTree([[time - max_time, time + max_time]])
        return self.tree.count_neighbors(to_search, max_time, p=np.inf)


cc = naive_count_at(start, end, 40) == KdSearch(start, end).count_at(40)
print(cc)

# 請讀者研究點數N和leafsize參數與建立K-d樹和搜尋時間之間的關系。
""" fail naive_search
ks = KdSearch(start, end, leafsize=100)
cc = naive_search(start, end, 40)
print(cc)
cc = ks.count_at(40)
print(cc)
"""
print("------------------------------------------------------------")  # 60個

# 凸包

points2d = np.random.rand(10, 2)
ch2d = spatial.ConvexHull(points2d)
print(ch2d.simplices)
print(ch2d.vertices)

# 二維平面上的凸包
poly = pl.Polygon(points2d[ch2d.vertices], fill=None, lw=2, color="r", alpha=0.5)
ax = pl.subplot(aspect="equal")
pl.plot(points2d[:, 0], points2d[:, 1], "go")
for i, pos in enumerate(points2d):
    pl.text(pos[0], pos[1], str(i), color="blue")
ax.add_artist(poly)

show()

print("------------------------------------------------------------")  # 60個

points3d = np.random.rand(40, 3)
ch3d = spatial.ConvexHull(points3d)
cc = ch3d.simplices.shape
print(cc)

# 沃羅諾伊圖

points2d = np.array(
    [
        [0.2, 0.1],
        [0.5, 0.5],
        [0.8, 0.1],
        [0.5, 0.8],
        [0.3, 0.6],
        [0.7, 0.6],
        [0.5, 0.35],
    ]
)
vo = spatial.Voronoi(points2d)

print(vo.vertices)
print(vo.regions)
print(vo.ridge_vertices)

bound = np.array([[-100, -100], [-100, 100], [100, 100], [100, -100]])
vo2 = spatial.Voronoi(np.vstack((points2d, bound)))

# 沃羅諾伊圖將空間分割為多個區域
fig, (ax1, ax2) = pl.subplots(1, 2, figsize=(9, 4.5))
ax1.set_aspect("equal")
ax2.set_aspect("equal")
spatial.voronoi_plot_2d(vo, ax=ax1)
for i, v in enumerate(vo.vertices):
    ax1.text(v[0], v[1], str(i), color="red")

for i, p in enumerate(points2d):
    ax1.text(p[0], p[1], str(i), color="blue")

n = len(points2d)
color = pl.cm.rainbow(np.linspace(0, 1, n))
for i in range(n):
    idx = vo2.point_region[i]
    region = vo2.regions[idx]
    poly = pl.Polygon(vo2.vertices[region], facecolor=color[i], alpha=0.5, zorder=0)
    ax2.add_artist(poly)
ax2.scatter(points2d[:, 0], points2d[:, 1], s=40, c=color, linewidths=2, edgecolors="k")
ax2.plot(vo2.vertices[:, 0], vo2.vertices[:, 1], "ro", ms=6)

for ax in ax1, ax2:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

show()

print(vo.point_region)
print(vo.regions[6])

print("------------------------------------------------------------")  # 60個

# 使用沃羅諾伊圖計算最大空圓
from collections import defaultdict

n = 50
points2d = np.random.rand(n, 2)
vo = spatial.Voronoi(points2d)
ch = spatial.ConvexHull(points2d)
poly = pl.Polygon(points2d[ch.vertices])
vs = vo.vertices
convexhull_mask = [poly.contains_point(p, radius=0) for p in vs]  # ❷

vertice_point_map = defaultdict(list)  # ❸
for index_point, index_region in enumerate(vo.point_region):
    region = vo.regions[index_region]
    if -1 in region:
        continue
    for index_vertice in region:
        if convexhull_mask[index_vertice]:
            vertice_point_map[index_vertice].append(index_point)


def dist(p1, p2):
    return ((p1 - p2) ** 2).sum() ** 0.5


""" NG
max_cicle = max((dist(points2d[pidxs[0]], vs[vidx]), vs[vidx]) #❹
                for vidx, pidxs in vertice_point_map.iteritems())
r, center = max_cicle
print("r = ", r, ", center = ", center)

ax = pl.subplot(111, aspect="equal")
ax.plot(points2d[:, 0], points2d[:, 1], ".")

c = pl.Circle(center, r, fill=True, color="red", alpha=0.5)
ax.add_artist(c)

#r =  0.174278456762 , center =  [ 0.46973363  0.59356531]

show()
"""
print("------------------------------------------------------------")  # 60個

# 德勞內三角化

x = np.array(
    [
        46.445,
        263.251,
        174.176,
        280.899,
        280.899,
        189.358,
        135.521,
        29.638,
        101.907,
        226.665,
    ]
)
y = np.array(
    [
        287.865,
        250.891,
        287.865,
        160.975,
        54.252,
        160.975,
        232.404,
        179.187,
        35.765,
        71.361,
    ]
)
points2d = np.c_[x, y]
dy = spatial.Delaunay(points2d)
vo = spatial.Voronoi(points2d)

print(dy.simplices)
print(vo.vertices)

# 德勞內三角形的外接圓與圓心
cx, cy = vo.vertices.T

ax = pl.subplot(aspect="equal")
spatial.delaunay_plot_2d(dy, ax=ax)
ax.plot(cx, cy, "r.")
for i, (cx, cy) in enumerate(vo.vertices):
    px, py = points2d[dy.simplices[i, 0]]
    radius = np.hypot(cx - px, cy - py)
    circle = pl.Circle((cx, cy), radius, fill=False, ls="dotted")
    ax.add_artist(circle)
ax.set_xlim(0, 300)
ax.set_ylim(0, 300)

show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

np.random.seed(42)
