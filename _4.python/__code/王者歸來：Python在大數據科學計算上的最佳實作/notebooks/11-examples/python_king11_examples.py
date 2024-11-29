"""

python_king11_examples


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

print("------------------------------------------------------------")  # 60個

import pylab as pl
from scipy import integrate
from scipy import optimize
from scipy import signal

def show():
    #plt.show()
    pass

# 各種長度的懸鏈線
def catenary(x, a):
    return a * np.cosh((x - 0.5) / a) - a * np.cosh((-0.5) / a)

print("------------------------------------------------------------")  # 60個
'''
# 使用泊松混合合成圖形
# 泊松混合算法

import cv2

offset_x, offset_y = -36, 42

src = cv2.imread("vinci_src.png", 1)
dst = cv2.imread("vinci_target.png", 1)

mask = cv2.imread("vinci_mask.png", 0)

src_mask = (mask > 128).astype(np.uint8)

src_y, src_x = np.where(src_mask)  # ❶

src_laplacian = cv2.Laplacian(src, cv2.CV_16S, ksize=1)[src_y, src_x, :]  # ❷

dst_mask = np.zeros(dst.shape[:2], np.uint8)
dst_x, dst_y = src_x + offset_x, src_y + offset_y
dst_mask[dst_y, dst_x] = 1  # ❶

kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)
dst_mask2 = cv2.dilate(dst_mask, kernel=kernel)  # ❷

dst_y2, dst_x2 = np.where(dst_mask2)  # ❸
dst_ye, dst_xe = np.where(dst_mask2 - dst_mask)  # ❹

variable_count = len(dst_x2)
variable_index = np.arange(variable_count)  # ❶

variables = np.zeros(dst.shape[:2], np.int)
variables[dst_y2, dst_x2] = variable_index

x0 = variables[dst_y, dst_x]  # ❷
x1 = variables[dst_y - 1, dst_x]
x2 = variables[dst_y + 1, dst_x]
x3 = variables[dst_y, dst_x - 1]
x4 = variables[dst_y, dst_x + 1]
x_edge = variables[dst_ye, dst_xe]  # ❸

from scipy.sparse import coo_matrix

inner_count = len(x0)
edge_count = len(x_edge)

r = np.r_[x0, x0, x0, x0, x0, x_edge]
c = np.r_[x0, x1, x2, x3, x4, x_edge]
v = np.ones(inner_count * 5 + edge_count)
v[:inner_count] = -4

A = coo_matrix((v, (r, c))).tocsc()

from scipy.sparse.linalg import spsolve

order = np.argsort(np.r_[variables[dst_y, dst_x], variables[dst_ye, dst_xe]])  # ❶

result = dst.copy()

for ch in (0, 1, 2):  # ❷
    b = np.r_[src_laplacian[:, ch], dst[dst_ye, dst_xe, ch]]  # ❸
    u = spsolve(A, b[order])  # ❹
    u = np.clip(u, 0, 255)
    result[dst_y2, dst_x2, ch] = u  # ❺

# 使用泊松混合算法將吉內薇拉·班琪肖像中的眼睛和鼻子部分複製到蒙娜麗莎的肖像之上
fig, axes = plt.subplots(1, 4, figsize=(10, 4))
ax1, ax2, ax3, ax4 = axes.ravel()
ax1.imshow(src[:, :, ::-1])
ax2.imshow(mask, cmap="gray")
ax3.imshow(dst[:, :, ::-1])
ax4.imshow(result[:, :, ::-1])

for ax in axes.ravel():
    ax.axis("off")

fig.subplots_adjust(wspace=0.05)

show()

"""
scpy2.examples.possion：使用TraitsUI撰寫的泊松混合示範程式。
該程式使用scpy2.matplotlib.freedraw_widget中提供的ImageMaskDrawer在圖形上繪制半透明的白色區域。
"""
print("------------------------------------------------------------")  # 60個

from scipy import integrate
from scipy import optimize

# 經典力學類比
# 懸鏈線



x = np.linspace(0, 1, 100)
for a in [0.35, 0.5, 0.8]:
    pl.plot(x, catenary(x, a), label="$a={:g}$".format(a))
ax = pl.gca()
ax.set_aspect("equal")
ax.legend(loc="best")
pl.margins(0.1)

show()

y = catenary(x, 0.35)
cc = np.sqrt(np.diff(x) ** 2 + np.diff(y) ** 2).sum()
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

'''


'''
from sympy import symbols, cosh, S, sqrt, lambdify

x, a = symbols("x, a")
y = a * cosh((x - S(1) / 2) / a)
s = sqrt(1 + y.diff(x) ** 2)
fs = lambdify((x, a), s, modules="math")


def catenary_length(a):
    return integrate.quad(lambda x: fs(x, a), 0, 1)[0]


length = catenary_length(0.35)
print(length)

# 1.3765789965

# 使用運動方程式類比懸鏈線

# 使用運動方程式類比懸鏈線，由於彈簧會被伸展，因此懸鏈線略比原始長度長
N = 31
dump = 0.2  # 阻尼系數
k = 100.0  # 彈簧系數
l = length / (N - 1)  # 彈簧原長度
g = 0.01  # 重力加速度

x0 = np.linspace(0, 1, N)
y0 = np.zeros_like(x0)
vx0 = np.zeros_like(x0)
vy0 = np.zeros_like(x0)


def diff_status(status, t):
    x, y, vx, vy = status.reshape(4, -1)
    dvx = np.zeros_like(x)
    dvy = np.zeros_like(x)
    dx = vx
    dy = vy

    s = np.s_[1:-1]

    l1 = np.sqrt((x[s] - x[:-2]) ** 2 + (y[s] - y[:-2]) ** 2)
    l2 = np.sqrt((x[s] - x[2:]) ** 2 + (y[s] - y[2:]) ** 2)
    dl1 = (l1 - l) / l1
    dl2 = (l2 - l) / l2
    dvx[s] = -vx[s] * dump - (x[s] - x[:-2]) * k * dl1 - (x[s] - x[2:]) * k * dl2
    dvy[s] = -vy[s] * dump - (y[s] - y[:-2]) * k * dl1 - (y[s] - y[2:]) * k * dl2 + g
    return np.r_[dx, dy, dvx, dvy]


status0 = np.r_[x0, y0, vx0, vy0]

t = np.linspace(0, 50, 100)
r = integrate.odeint(diff_status, status0, t)
x, y, vx, vy = r[-1].reshape(4, -1)

r, e = optimize.curve_fit(catenary, x, -y, [1])
print("a =", r[0], "length =", catenary_length(r[0]))

x2 = np.linspace(0, 1, 100)
pl.plot(x2, catenary(x2, 0.35))
pl.plot(x2, catenary(x2, r))
pl.plot(x, -y, "o")
pl.margins(0.1)

# a = 0.336992602016 length = 1.40946777721

show()

"""
scpy2.examples.catenary：使用TraitsUI製作的懸鏈線的動畫示範程式，
可透過界面修改各個參數
"""
print("------------------------------")  # 30個

# 透過能量最小值計算懸鏈線

# %figonly=把懸鏈線分為多個質點並用無質量的連線桿相連
x = np.linspace(0, 1, 1000)
y = catenary(x, 0.35)
s = np.cumsum(np.sqrt(np.diff(x) ** 2 + np.diff(y) ** 2))
p = np.linspace(0, s[-1], 10)
idx = np.searchsorted(s, p)
x, y = x[idx], y[idx]
pl.plot(x, y, "-o", lw=2)
for i, (x1, x2, y1, y2) in enumerate(zip(x[:-1], x[1:], y[:-1], y[1:])):
    pl.text((x1 + x2) * 0.5, (y1 + y2) * 0.5, "%d" % i)
    pl.text(x2, y2, "%d" % i, color="r", fontsize=10)
pl.margins(0.1)

show()

print("------------------------------")  # 30個

N = 30

l = length / N


def g1(theta):
    return np.sum(l * np.cos(theta)) - 1.0


def g2(theta):
    return np.sum(l * np.sin(theta)) - 0.0


def P(theta):
    y = l * np.sin(theta)
    cy = np.cumsum(y)
    return np.sum(cy)


theta0 = np.arccos(1.0 / length)
theta_init = [-theta0] * (N // 2) + [theta0] * (N // 2)  # ❶

theta = optimize.fmin_slsqp(
    P, theta_init, eqcons=[g1, g2], bounds=[(-np.pi / 2, np.pi / 2)] * N  # ❷
)  # ❸

# 使用fmin_slsqp()計算能量最低的狀態，叉點表示最佳化的起始狀態
x_init = np.r_[0, np.cumsum(l * np.cos(theta_init))]
y_init = np.r_[0, np.cumsum(l * np.sin(theta_init))]

x = np.r_[0, np.cumsum(l * np.cos(theta))]
y = np.r_[0, np.cumsum(l * np.sin(theta))]

x2 = np.linspace(0, 1, 100)
pl.plot(x2, catenary(x2, 0.35))
pl.plot(x, y, "o")
pl.plot(x_init, y_init, "x")
pl.margins(0.1)

show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# 最速降線

x, _ = integrate.quad(lambda y: np.sqrt(y / (1.0 - y)), 0, 1)
print(x)

# 使用odeint()計算最速降線


# 使用odeint()計算最速降線
def brachistochrone_curve(D, N=1000):
    eps = 1e-8

    def f(y, x):
        y = min(max(eps, y), D)  # ❶
        flag = -1 if x >= D * np.pi / 2 else 1  # ❷
        return flag * ((D - y) / y) ** 0.5

    x0 = np.linspace(0, D * np.pi, N)
    y = integrate.odeint(f, 0, x0)
    return x0, y.ravel()


x, y = brachistochrone_curve(2.0)
pl.plot(x, -y)

show()

print("------------------------------")  # 30個

# 使用改善算法計算最速降線

# 使用改善算法計算最速降線
N = 100
target = 10.0
x = np.linspace(0, target, N)
tmp = np.linspace(0, -1, N // 2)
y0 = np.r_[tmp, tmp[::-1]]
g = 9.8


def total_time(y):
    s = np.hypot(np.diff(x), np.diff(y))  # ❶
    v = np.sqrt(2 * g * np.abs(y))  # ❷
    avg_v = np.maximum((v[1:] + v[:-1]) * 0.5, 1e-10)  # ❸
    t = s / avg_v
    return t.sum()


def fix_two_ends(y):
    return y[[0, -1]]


from scipy import optimize

y_opt = optimize.fmin_slsqp(total_time, y0, eqcons=[fix_two_ends])  # ❹
pl.plot(x, y0, "k--", label="初值")
pl.plot(x, y_opt, label="改善結果")
x2, y2 = brachistochrone_curve(target / np.pi)
pl.plot(x2, -y2, label="最速降線")
pl.legend(loc="best")

show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# 單擺類比

# 起始角度為1弧度的單擺擺動角度和時間的關系
from math import sin

g = 9.8


def pendulum_equations(w, t, l):
    th, v = w
    dth = v
    dv = -g / l * sin(th)
    return dth, dv


t = np.arange(0, 10, 0.01)
track = integrate.odeint(pendulum_equations, (1.0, 0), t, args=(1.0,))
pl.plot(t, track[:, 0])
pl.xlabel("時間(秒)")
pl.ylabel("震動角度(弧度)")

show()

print("------------------------------")  # 30個

# 小角度時的擺動周期

from sympy import symbols, Function, dsolve

t, g, l = symbols("t,g,l", positive=True)  # 分別表示時間、重力加速度和長度
y = Function("y")  # 擺角函數用y(t)表示
dsolve(y(t).diff(t, 2) + g / l * y(t), y(t))

# 大角度時的擺動周期

g = 9.8


def pendulum_th(t, l, th0):
    track = integrate.odeint(pendulum_equations, (th0, 0), [0, t], args=(l,))
    return track[-1, 0]


def pendulum_period(l, th0):
    t0 = 2 * np.pi * (l / g) ** 0.5 / 4
    t = fsolve(pendulum_th, t0, args=(l, th0))
    return t * 4


def pendulum_th(t, l, th0):
    track = integrate.odeint(pendulum_equations, (th0, 0), [0, t], args=(l,))
    return track[-1, 0]


from scipy.optimize import fsolve


def pendulum_period(l, th0):
    t0 = 2 * np.pi * (l / g) ** 0.5 / 4
    t = fsolve(pendulum_th, t0, args=(l, th0))
    return t * 4


ths = np.arange(0, np.pi / 2.0, 0.01)
periods = [pendulum_period(1, th) for th in ths]

from scipy.special import ellipk

periods2 = 4 * (1.0 / g) ** 0.5 * ellipk(np.sin(ths / 2) ** 2)

# 單擺的擺動周期和起始角度的關系
ths = np.arange(0, np.pi / 2.0, 0.01)
periods = [pendulum_period(1, th) for th in ths]
periods2 = 4 * (1.0 / g) ** 0.5 * ellipk(np.sin(ths / 2) ** 2)  # 計算單擺周期的精確值
pl.plot(ths, periods, label="fsolve計算的單擺周期", linewidth=4.0)
pl.plot(ths, periods2, "r", label="單擺周期精確值", linewidth=2.0)
pl.legend(loc="upper left")
pl.xlabel("起始擺角(弧度)")
pl.ylabel("擺動周期(秒)")

show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
import cython

# 推薦算法
# 讀入資料

columns = ["user_id", "movie_id", "rating"]
dtypes = [np.int32, np.int32, np.float]
ratings = pd.read_table(
    "movielens.data",
    names=columns,
    usecols=[0, 1, 2],
    dtype=dict(zip(columns, dtypes)),
)
ratings["user_id"] -= 1
ratings["movie_id"] -= 1

u, v, r = ratings.user_id.values, ratings.movie_id.values, ratings.rating.values

# 移除評分數少於10的使用者和電影
u_count = pd.value_counts(u)
v_count = pd.value_counts(v)
mask = (u_count >= 10)[u].values & (v_count >= 10)[v].values
u, v, r = u[mask], v[mask], r[mask]


def train_test_split(arrays, test_size=0.1):
    mask_test = np.random.rand(len(arrays[0])) < test_size
    mask_train = ~mask_test

    arrays_train = [arr[mask_train] for arr in arrays]
    arrays_test = [arr[mask_test] for arr in arrays]

    return arrays_train + arrays_test


u_train, v_train, r_train, u_test, v_test, r_test = train_test_split([u, v, r])
nu = np.max(u) + 1
nv = np.max(v) + 1
nr = len(u_train)
print(nr)

assert np.all(np.unique(u_train) == np.unique(u))
assert np.all(np.unique(v_train) == np.unique(v))

# 推薦效能評價標准


def rmse_score(y_true, y_pred):
    d = y_true - y_pred
    return np.mean(d**2) ** 0.5


def r2_score(y_true, y_pred):
    d = y_true - y_pred
    return 1 - (d**2).sum() / ((y_true - y_true.mean()) ** 2).sum()


movies_mean = pd.Series(r_train).groupby(v_train).mean()
r_pred = movies_mean[v_test]

rmse_avg, r2_avg = rmse_score(r_test, r_pred), r2_score(r_test, r_pred)
print(rmse_avg)
print(r2_avg)

# 矩陣分解

from scipy import sparse
from scipy.sparse import linalg

r_avg = r_train.mean()

row_idx = np.r_[np.arange(nr), np.arange(nr)]
col_idx = np.r_[u_train, v_train + nu]
values = np.ones_like(row_idx)

A = sparse.coo_matrix((values, (row_idx, col_idx)), shape=(nr, nu + nv))

x = linalg.lsqr(A, r_train - r_avg)[0]

ub = x[:nu]
vb = x[nu:]

r_pred = r_avg + ub[u_test] + vb[v_test]

rmse, r2 = rmse_score(r_test, r_pred), r2_score(r_test, r_pred)
print(rmse)
print(r2)

r_train2 = r_train - (r_avg + ub[u_train] + vb[v_train])
r_test2 = r_test - r_pred
arrays = u_train, v_train, r_train2, u_test, v_test, r_test2  # 以下的程式從該array元群組取得資料

# 使用最小二乘法實現矩陣分解

from scipy import sparse
from scipy.sparse import linalg
import gc


def uv_decompose(arrays, loop_count, k, maxiter, mu, damp):
    u_train, v_train, r_train, u_test, v_test, r_test = arrays

    U = np.random.rand(nu, k) * 0.1 / k**0.5  # ❶
    V = np.random.rand(nv, k) * 0.1 / k**0.5

    idxv_col = (u_train[:, None] * k + np.arange(k)).ravel()
    idx_row = np.repeat(np.arange(nr), k)
    Av = sparse.coo_matrix(
        (V[v_train].ravel(), (idx_row, idxv_col)), shape=(nr, nu * k)
    ).tocsr()  # ❷

    idxu_col = (v_train[:, None] * k + np.arange(k)).ravel()
    Au = sparse.coo_matrix(
        (U[u_train].ravel(), (idx_row, idxu_col)), shape=(nr, nv * k)
    ).tocsr()

    best_U, best_V = None, None
    best_rmse = 100.0
    rmse_list = []

    for i in range(loop_count):
        U.ravel()[:] = linalg.lsmr(Av, r_train, maxiter=maxiter, damp=damp)[0]  # ❸
        Au.data[:] = Au.data[:] * (1 - mu) + U[u_train].ravel() * mu  # ❹

        V.ravel()[:] = linalg.lsmr(Au, r_train, maxiter=maxiter, damp=damp)[0]
        Av.data[:] = Av.data[:] * (1 - mu) + V[v_train].ravel() * mu

        r_pred = U.dot(V.T)[u_test, v_test]  # ❺
        rmse = rmse_score(r_test, r_pred)
        rmse_list.append(rmse)
        if rmse < best_rmse:
            best_rmse = rmse
            best_U, best_V = U.copy(), V.copy()
        gc.collect()  # ❻

    return best_U, best_V, best_rmse, rmse_list


U1, V1, best_rmse1, rmses1 = uv_decompose(
    arrays, loop_count=20, maxiter=6, k=30, mu=0.4, damp=3.5
)
U2, V2, best_rmse2, rmses2 = uv_decompose(
    arrays, loop_count=20, maxiter=6, k=30, mu=0.4, damp=3.0
)
print(best_rmse1, best_rmse2)

# 0.901107139807 0.904096209664

# damp系數對RMSE的影響
pl.plot(np.arange(1, len(rmses1) + 1), rmses1, label="damp=3.5")
pl.plot(np.arange(1, len(rmses2) + 1), rmses2, label="damp=3.0")
pl.legend(loc="best")
pl.xlabel("迭代次數")
pl.ylabel("RMSE")

show()

print("------------------------------")  # 30個

# 以實際評分對預測評分分群組，繪制每群組的分佈情況
r_pred3 = U1.dot(V1.T)[u_test, v_test] + r_pred
s = pd.DataFrame({"r": r_test, "$\hat{r}$": r_pred3})
s.boxplot(column="$\hat{r}$", by="r", figsize=(12, 6))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 卷冊積的分段運算


# %figonly=使用overlap-add法進行分段卷冊積的過程示範
def windowed_sinc(fc, M, K):
    i = np.arange(0, M, 1.0)
    h = K * np.sin(2 * np.pi * fc * (i - M / 2.0)) / (i - M / 2.0)
    h *= 0.42 - 0.5 * np.cos(2 * np.pi * i / M) + 0.08 * np.cos(4 * np.pi * i / M)
    return h


x = np.random.rand(300) - 0.5
h = windowed_sinc(0.05, 101, 1.0)

xs = []
for i in range(3):
    tmp = np.zeros(len(x), dtype=np.float64)
    tmp[i * 100 : i * 100 + 100] = x[i * 100 : i * 100 + 100]
    xs.append(tmp)

y = np.convolve(x, h)
fig = pl.figure(figsize=(8, 8))

pl.subplot(521)
pl.plot(x, label="原始訊號x")
pl.gca().set_yticklabels([])
pl.gca().set_xticklabels([])
pl.legend()

pl.subplot(522)
pl.plot(h, label="濾波器系數h")
pl.gca().set_yticklabels([])
pl.gca().set_xticklabels([])
pl.legend()

result = []
for i, tmp in enumerate(xs):
    pl.subplot(520 + 3 + i * 2)
    pl.plot(tmp, label="分段%s" % (i + 1))
    pl.gca().set_yticklabels([])
    pl.gca().set_xticklabels([])
    pl.legend()
    pl.subplot(520 + 3 + i * 2 + 1)
    tmp = np.convolve(tmp, h)
    result.append(tmp)
    pl.plot(tmp, label="分段卷冊積%s" % (i + 1))
    pl.gca().set_yticklabels([])
    pl.gca().set_xticklabels([])
    pl.axvspan(i * 100, i * 100 + 200, alpha=0.3, facecolor="g")
    pl.legend()

pl.subplot(529)
pl.plot(np.convolve(x, h), label="原始訊號卷冊積")
pl.gca().set_yticklabels([])
pl.gca().set_xticklabels([])
pl.legend()

pl.subplot(5, 2, 10)
pl.plot(np.sum(result, axis=0), label="分段卷冊積和")
pl.gca().set_yticklabels([])
pl.gca().set_xticklabels([])
pl.legend()

pl.subplots_adjust(
    hspace=0.05, wspace=0.03, top=0.95, bottom=0.01, left=0.03, right=0.97
)
pl.figtext(
    0.5, 0.965, "分段卷冊積示範", ha="center", color="black", weight="bold", size="large"
)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x = np.random.rand(1000)
h = np.random.rand(101)
y = np.convolve(x, h)

N = 50  # 分段大小
M = len(h)  # 濾波器長度

output = []

# 快取起始化為0
buffer = np.zeros(M + N - 1, dtype=np.float64)

for i in range(int(len(x) / N)):
    # 從輸入訊號中讀取N個資料
    xslice = x[i * N : (i + 1) * N]
    # 計算卷冊積
    yslice = np.convolve(xslice, h)
    # 將卷冊積的結果加入到緩沖中
    buffer += yslice
    # 輸出快取中的前N個資料，注意使用copy，否則輸出的是buffer的一個檢視
    output.append(buffer[:N].copy())  # ❶
    # 快取中的資料左搬移N個元素
    buffer[0:-N] = buffer[N:]
    # 後面的補0
    buffer[-N:] = 0

# 將輸出的資料群組合為陣列
y2 = np.hstack(output)
# 計算和直接卷冊積的結果之間的誤差
print("error:", np.max(np.abs(y2 - y[: len(x)])))

# error: 7.1054273576e-15

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 布爾可滿足性問題求解器

from sympy import symbols
from sympy.logic.boolalg import to_cnf

A, B, C, D = symbols("A:D")  # ❶
S1 = ~A
S2 = D
S3 = B
S4 = ~D
dnf = (
    (S1 & ~S2 & ~S3 & ~S4)
    | (~S1 & S2 & ~S3 & ~S4)  # ❷
    | (~S1 & ~S2 & S3 & ~S4)
    | (~S1 & ~S2 & ~S3 & S4)
)

cnf = to_cnf(dnf)  # ❸
# %sympy_latex cnf

from sympy.logic.inference import satisfiable

satisfiable(cnf)


# 數獨游戲

bools = np.arange(1, 9 * 9 * 9 + 1).reshape(9, 9, 9)

from itertools import combinations


def get_conditions(bools):
    conditions = []
    n = bools.shape[-1]
    index = np.array(list(combinations(range(n), 2)))  # ❶
    # 以最後一軸為群組
    # 第一個條件: 每群組只能有一個為真
    conditions.extend(bools.reshape(-1, n).tolist())  # ❷
    # 第二個條件: 每群組中沒有兩個同時為真
    conditions.extend((-bools[..., index].reshape(-1, 2)).tolist())  # ❸
    return conditions


print(get_conditions(np.array([[1, 2, 3], [4, 5, 6]])))

c1 = get_conditions(bools)  # 每個單元格只能取1-9之中的一個數字
c2 = get_conditions(np.swapaxes(bools, 1, 2))  # 每行的數字不能重復
c3 = get_conditions(np.swapaxes(bools, 0, 2))  # 每列的數字不能重復

tmp = np.swapaxes(bools.reshape(3, 3, 3, 3, 9), 1, 2).reshape(9, 9, 9)
c4 = get_conditions(np.swapaxes(tmp, 1, 2))  # 每塊的數字不能重復

conditions = c1 + c2 + c3 + c4


def format_solution(solution):
    solution = np.array(solution).reshape(9, 9, 9)  # ❶
    return (np.where(solution == 1)[2] + 1).reshape(9, 9)  # ❷


sudoku_str = """
000000185
007030000
000021400
800000020
003905600
050000004
004860000
000040300
931000000"""

sudoku = np.array([[int(x) for x in line] for line in sudoku_str.strip().split()])
r, c = np.where(sudoku != 0)
v = sudoku[r, c] - 1

conditions2 = [[x] for x in bools[r, c, v]]  # ❶
print("conditions2:")
print(conditions2)

# 采用matplotlib製作的數獨游戲求解器

# 掃雷游戲
# 識別雷區中的數字

import cv2

X0, Y0, SIZE, COLS, ROWS = 30, 30, 18, 30, 16
SHAPE = ROWS, SIZE, COLS, SIZE, -1

mine_area = np.s_[Y0 : Y0 + SIZE * ROWS, X0 : X0 + SIZE * COLS, :]  # ❶

img_init = cv2.imread("mine_init.png")[mine_area]

img_mine = cv2.imread("mine01.png")[mine_area]

img_numbers = cv2.imread("mine_numbers.png")  # ❷

img_numbers.shape

# 可以透過pl.hist()繪制mask_mean陣列的直方圖，找到最佳的設定值。

# 計算已開啟方塊的位置
mask = (img_init != img_mine).reshape(SHAPE)
mask_mean = np.mean(mask, axis=(1, 3, 4))
block_mask = mask_mean > 0.3

fig, axes = pl.subplots(1, 2, figsize=(12, 4))
axes[0].imshow(block_mask, interpolation="nearest", cmap="gray")
axes[1].imshow(img_mine[:, :, ::-1])
axes[0].set_axis_off()
axes[1].set_axis_off()
fig.subplots_adjust(wspace=0.01)

show()

print("------------------------------")  # 30個

from scipy.spatial import distance

img_mine2 = np.swapaxes(img_mine.reshape(SHAPE), 1, 2)

blocks = img_mine2[block_mask][:, 3:-3, 3:-3, :].copy()
blocks = blocks.reshape(blocks.shape[0], -1)

img_numbers.shape = 8, -1
numbers = np.argmin(distance.cdist(blocks, img_numbers), axis=1)
rows, cols = np.where(block_mask)

# 識別掃雷界面中的數字
# from scpy2.matplotlib import draw_grid

table = np.full((ROWS, COLS), " ", dtype="unicode")
# NG table[rows, cols] = numbers.astype(unicode)
# NG draw_grid(table, fontsize=12)

show()

print("------------------------------")  # 30個

# 用SAT掃雷

variables = range(1, 9)
from itertools import combinations

clauses = []
for vs in combinations(variables, 4):
    clauses.append([-x for x in vs])

for vs in combinations(variables, 6):
    clauses.append(vs)

from collections import defaultdict

variable_neighbors = defaultdict(list)

directs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

variables = np.arange(1, COLS * ROWS + 1).reshape(ROWS, COLS)

for (i, j), v in np.ndenumerate(variables):
    for di, dj in directs:
        i2 = i + di
        j2 = j + dj
        if 0 <= i2 < ROWS and 0 <= j2 < COLS:
            variable_neighbors[v].append(variables[i2, j2])

cc = variable_neighbors[50]
print(cc)


def get_clauses(var_id, num):
    clauses = []
    neighbors = variable_neighbors[var_id]
    neg_neighbors = [-x for x in neighbors]
    clauses.extend(combinations(neg_neighbors, num + 1))
    clauses.extend(combinations(neighbors, len(neighbors) - num + 1))
    clauses.append([-var_id])
    return clauses


table[0, 0] = "★"
table[1, 1] = "★"
table[2, 2] = "●"
table[3, 3] = "●"
# NG 還是沒辦法畫出來
# draw_grid(table, fontsize=12)

show()

# 自動掃雷

# Windows 7系統下自動掃雷，需將掃雷游戲的難度設定為進階（99個雷），
# 並且關閉“顯示動畫”、“播放音效”以及“顯示提示”等選項。

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''

'''
# 分形
# Mandelbrot集合
# 純Python實現

# Mandelbrot集合，以5倍的倍率拉近點(0.273, 0.595)附近
from matplotlib import cm


def iter_point(c):  # ❶
    z = c
    for i in range(1, 100):  # 最多迭代100次
        if abs(z) > 2:
            break  # 半徑大於2則認為逃逸
        z = z * z + c
    return i  # 傳回迭代次數


def mandelbrot(cx, cy, d, n=200):
    x0, x1, y0, y1 = cx - d, cx + d, cy - d, cy + d
    y, x = np.ogrid[y0 : y1 : n * 1j, x0 : x1 : n * 1j]
    c = x + y * 1j  # ❸
    return np.frompyfunc(iter_point, 1, 1)(c).astype(np.float)  # ❹


def draw_mandelbrot(cx, cy, d, n=200):  # ❷
    """
    繪制點(cx, cy)附近正負d的範圍的Mandelbrot
    """
    pl.imshow(mandelbrot(cx, cy, d, n), cmap=cm.Blues_r)  # ❺
    pl.gca().set_axis_off()


x, y = 0.27322626, 0.595153338

pl.figure(figsize=(9, 6))
pl.subplot(231)
draw_mandelbrot(-0.5, 0, 1.5)
for i in range(2, 7):
    pl.subplot(230 + i)
    draw_mandelbrot(x, y, 0.2 ** (i - 1))
pl.subplots_adjust(0, 0, 1, 1, 0.0, 0)

show()

print("------------------------------")  # 30個

# 平順處理後的Mandelbrot集合：逃逸半徑=10，最大迭代次數=20
pl.figure(figsize=(8, 8))
draw_mandelbrot(-0.5, 0, 1.5, n=600)

show()

"""
Mandelbrot示範程式
    scpy2.examples.fractal.mandelbrot_demo：
    使用TraitsUI和matplotlib實時繪制Mandelbrot圖形，
    按住滑鼠左鍵進行平移，使用滑鼠滾軸進行縮放。
"""
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
def ifs(p, eq, init, n):
    """
    進行函數迭代
    p: 每個函數的選取機率清單
    eq: 迭代函數清單
    init: 迭代起始點
    n: 迭代次數

    傳回值： 每次迭代所得的X座標陣列， Y座標陣列， 計算所用的函數索引
    """

    # 迭代向量的起始化
    pos = np.ones(3, dtype=np.float)  # ❶
    pos[:2] = init

    # 透過函數機率，計算函數的選取序列
    p = np.cumsum(p)
    rands = np.random.rand(n)
    select = np.searchsorted(p, rands)  # ❷

    # 結果的起始化
    result = np.zeros((n, 2), dtype=np.float)
    c = np.zeros(n, dtype=np.float)

    for i in range(n):
        eqidx = select[i]  # 所選的函數索引
        tmp = np.dot(eq[eqidx], pos)  # 進行迭代
        pos[:2] = tmp  # 更新迭代向量

        # 儲存結果
        result[i] = tmp
        c[i] = eqidx

    return result[:, 0], result[:, 1], c


fig, axes = pl.subplots(1, 2, figsize=(6, 5))
# axes[0].scatter(x, y, s=1, c="g", marker="s", linewidths=0) #❸
# axes[1].scatter(x, y, s=1, c=c, marker="s", linewidths=0)  #❹
for ax in axes:
    ax.set_aspect("equal")
    ax.set_ylim(0, 10.5)
    ax.axis("off")
pl.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# 2D仿射變換
# 迭代函數系統設計器
"""
    scpy2.examples.fractal.ifs_demo：
    迭代函數分形系統的示範程式，透過修改左側三角形的頂點實時地計算座標變換矩陣，
    並在右側顯示迭代結果。
"""

# %%include python examples/fractal/ifs_demo.py 1
def solve_eq(triangle1, triangle2):
    """
    解方程式，從triangle1變換到triangle2的變換系數
        triangle1,2是二維陣列：
        x0,y0
        x1,y1
        x2,y2
    """
    x0, y0 = triangle1[0]
    x1, y1 = triangle1[1]
    x2, y2 = triangle1[2]

    a = np.zeros((6, 6), dtype=np.float)
    b = triangle2.reshape(-1)
    a[0, 0:3] = x0, y0, 1
    a[1, 3:6] = x0, y0, 1
    a[2, 0:3] = x1, y1, 1
    a[3, 3:6] = x1, y1, 1
    a[4, 0:3] = x2, y2, 1
    a[5, 3:6] = x2, y2, 1

    x = np.linalg.solve(a, b)
    x.shape = (2, 3)
    return x


# %%include python examples/fractal/ifs_demo.py 2
def triangle_area(triangle):
    """
    計算三角形的面積
    """
    A, B, C = triangle
    AB = A - B
    AC = A - C
    return np.abs(np.cross(AB, AC)) / 2.0


# 使用IFS類別繪制迭代函數系統
# from scpy2.examples.fractal.ifs_demo import solve_eq, triangle_area
# from scpy2.examples.fractal.fastfractal import IFS

triangles = np.array(
    [  # ❶
        [-1.945392491467576, -5.331010452961673],
        [6.109215017064848, -0.8710801393728236],
        [-1.1945392491467572, 5.400696864111497],
        [-2.5597269624573373, -4.21602787456446],
        [5.426621160409557, -2.125435540069687],
        [0.5119453924914676, 4.912891986062718],
        [3.5836177474402735, 8.397212543554005],
        [4.0614334470989775, 5.121951219512194],
        [8.56655290102389, 4.7038327526132395],
    ]
)

base_triangle = triangles[:3]
triangle1 = triangles[3:6]
triangle2 = triangles[6:]

area1 = triangle_area(triangle1)  # ❷
area2 = triangle_area(triangle2)
total_area = area1 + area2
p = [area1 / total_area, area2 / total_area]

eq1 = solve_eq(base_triangle, triangle1)  # ❸
eq2 = solve_eq(base_triangle, triangle2)
eqs = np.vstack([eq1, eq2])

from matplotlib.colors import LogNorm

fig, ax = pl.subplots(figsize=(5, 8))
# no counts pl.imshow(counts, cmap="Blues", norm=LogNorm(), origin="lower") #❻
ax.axis("off")

# shape of counts: (600, 477)

show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# L-System分形

rules = [
    {"F": "F+F--F+F", "S": "F", "direct": 180, "angle": 60, "iter": 5, "title": "Koch"},
    {
        "X": "X+YF+",
        "Y": "-FX-Y",
        "S": "FX",
        "direct": 0,
        "angle": 90,
        "iter": 13,
        "title": "Dragon",
    },
    {
        "f": "F-f-F",
        "F": "f+F+f",
        "S": "f",
        "direct": 0,
        "angle": 60,
        "iter": 7,
        "title": "Triangle",
    },
    {
        "X": "F-[[X]+X]+F[+FX]-X",
        "F": "FF",
        "S": "X",
        "direct": -45,
        "angle": 25,
        "iter": 6,
        "title": "Plant",
    },
    {
        "S": "X",
        "X": "-YF+XFX+FY-",
        "Y": "+XF-YFY-FX+",
        "direct": 0,
        "angle": 90,
        "iter": 6,
        "title": "Hilbert",
    },
    {
        "S": "L--F--L--F",
        "L": "+R-F-R+",
        "R": "-L+F+L-",
        "direct": 0,
        "angle": 45,
        "iter": 10,
        "title": "Sierpinski",
    },
]


class L_System(object):
    def __init__(self, rule):
        info = rule["S"]
        for i in range(rule["iter"]):
            ninfo = []
            for c in info:
                if c in rule:
                    ninfo.append(rule[c])
                else:
                    ninfo.append(c)
            info = "".join(ninfo)
        self.rule = rule
        self.info = info

    def get_lines(self):
        from math import sin, cos, pi

        d = self.rule["direct"]
        a = self.rule["angle"]
        p = (0.0, 0.0)
        l = 1.0
        lines = []
        stack = []
        for c in self.info:
            if c in "Ff":
                r = d * pi / 180
                t = p[0] + l * cos(r), p[1] + l * sin(r)
                lines.append(((p[0], p[1]), (t[0], t[1])))
                p = t
            elif c == "+":
                d += a
            elif c == "-":
                d -= a
            elif c == "[":
                stack.append((p, d))
            elif c == "]":
                p, d = stack[-1]
                del stack[-1]
        return lines


def draw(ax, rule, iter=None):
    from matplotlib import collections

    if iter != None:
        rule["iter"] = iter
    lines = L_System(rule).get_lines()  # ❶
    linecollections = collections.LineCollection(lines, lw=0.7, color="black")  # ❷
    ax.add_collection(linecollections, autolim=True)  # ❸
    ax.axis("equal")
    ax.set_axis_off()
    ax.set_xlim(ax.dataLim.xmin, ax.dataLim.xmax)
    ax.invert_yaxis()


# 幾種L-System的迭代圖案
# %config InlineBackend.figure_format = 'png'
fig = pl.figure(figsize=(10, 6))
fig.patch.set_facecolor("w")

for i in range(6):
    ax = fig.add_subplot(231 + i)
    draw(ax, rules[i])

fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)

show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# 分形山脈
# 一維中點移位法


# 一維分形山脈曲線，衰減值越小則最大幅度的衰減越快，曲線越平順
def hill1d(n, d):
    """
    繪制山脈曲線，2**n+1為曲線在X軸上的長度，d為衰減系數
    """
    a = np.zeros(2**n + 1)  # ❶
    scale = 1.0
    for i in range(n, 0, -1):  # ❷
        s = 2 ** (i - 1)  # ❸
        s2 = 2 * s
        tmp = a[::s2]
        a[s::s2] += (tmp[:-1] + tmp[1:]) * 0.5  # ❹
        a[s::s2] += np.random.normal(size=len(tmp) - 1, scale=scale)  # ❺
        scale *= d  # ❻
    return a


pl.figure(figsize=(8, 4))
for i, d in enumerate([0.4, 0.5, 0.6]):
    np.random.seed(8)  # ❼
    a = hill1d(9, d)
    pl.plot(a, label="d=%s" % d, linewidth=3 - i)
pl.xlim(0, len(a))
pl.legend()
show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

'''
# 二維中點移位法
# 二維中點移位法計算山脈曲面
def hill2d(n, d):
    """
    繪制山脈曲面，曲面是一個(2**n + 1)*(2**n + 1)的圖形，
    d為衰減系數
    """
    from numpy.random import normal

    size = 2**n + 1
    scale = 1.0
    a = np.zeros((size, size))

    for i in range(n, 0, -1):
        s = 2 ** (i - 1)
        s2 = s * 2
        tmp = a[::s2, ::s2]
        tmp1 = (tmp[1:, :] + tmp[:-1, :]) * 0.5
        tmp2 = (tmp[:, 1:] + tmp[:, :-1]) * 0.5
        tmp3 = (tmp1[:, 1:] + tmp1[:, :-1]) * 0.5
        a[s::s2, ::s2] = tmp1 + normal(0, scale, tmp1.shape)
        a[::s2, s::s2] = tmp2 + normal(0, scale, tmp2.shape)
        a[s::s2, s::s2] = tmp3 + normal(0, scale, tmp3.shape)
        scale *= d

    return a


# from scpy2 import vtk_scene_to_array
from mayavi import mlab
from scipy.ndimage.filters import convolve

np.random.seed(42)
a = hill2d(8, 0.5)
a /= np.ptp(a) / (0.5 * 2**8)  # ❶
a = convolve(a, np.ones((3, 3)) / 9)  # ❷

mlab.options.offscreen = True
scene = mlab.figure(size=(800, 600))
scene.scene.background = 1, 1, 1
mlab.surf(a)
# img = vtk_scene_to_array(scene.scene)
# %array_image img
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from mayavi import mlab
from scipy.ndimage.filters import convolve
# 菱形方形算法


# 使用菱形方形算法計算山脈曲面
def hill2d_ds(n, d):
    from numpy.random import normal

    size = 2**n + 1
    scale = 1.0
    a = np.zeros((size, size))

    for i in range(n, 0, -1):
        s = 2 ** (i - 1)
        s2 = 2 * s

        # 方形平均
        t = a[::s2, ::s2]
        t2 = (t[:-1, :-1] + t[1:, 1:] + t[1:, :-1] + t[:-1, 1:]) / 4
        tmp = a[s::s2, s::s2]
        tmp[...] = t2 + normal(0, scale, tmp.shape)

        buf = a[::s2, ::s2]

        # 菱形平均分兩步，分別計算水平和垂直方向上的點
        t = a[::s2, s::s2]
        t[...] = buf[:, :-1] + buf[:, 1:]
        t[:-1] += tmp
        t[1:] += tmp
        t[[0, -1], :] /= 3  # 邊上是3個值的平均
        t[1:-1, :] /= 4  # 中間的是4個值的平均
        t[...] += np.random.normal(0, scale, t.shape)

        t = a[s::s2, ::s2]
        t[...] = buf[:-1, :] + buf[1:, :]
        t[:, :-1] += tmp
        t[:, 1:] += tmp
        t[:, [0, -1]] /= 3
        t[:, 1:-1] /= 4
        t[...] += np.random.normal(0, scale, t.shape)

        scale *= d

    return a


np.random.seed(42)
a = hill2d_ds(8, 0.5)
a /= np.ptp(a) / (0.5 * 2**8)
a = convolve(a, np.ones((3, 3)) / 9)

mlab.options.offscreen = True
scene = mlab.figure(size=(800, 600))
scene.scene.background = 1, 1, 1
mlab.surf(a)
# img = vtk_scene_to_array(scene.scene)
# %array_image img


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

"""

print xxxx
print(

b'\n\n\n

print("------------------------------------------------------------")  # 60個

<matplotlib.ticker.NullLocator object at 0x08364F50>

<a list of 2 mcoll.LineCollection objects>


with open(filename, "r", encoding='UTF-8-sig') as f:



"""


# from matplotlib import pyplot as plt
