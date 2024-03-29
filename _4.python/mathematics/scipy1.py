"""
scipy

SciPy是一個開源的Python演算法庫和數學工具包。
SciPy包含的模組有最佳化、線性代數、積分、插值、特殊函數、快速傅立葉轉換、
訊號處理和圖像處理、常微分方程式求解和其他科學與工程中常用的計算。

scipy.integrate
scipy.special
scipy.interpolate
scipy.optimize
scipy.stats
scipy.signal

scipy.stats.norm

"""

import scipy

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

print(
    "---- scipy.integrate 積分 --------------------------------------------------------"
)  # 60個


print("積分")
def my_funciton1(x):
    #return math.sin(x)
    #return (1 - x**2) ** 0.5    #上半圓
    return x**2 + 2 * x + 5 # f(x) = x**2 + 2x + 5

area, err = scipy.integrate.quad(my_funciton1, -3, 3)
print("積分結果 :", area)
print("誤差 :", err)

print("------------------------------------------------------------")  # 60個

# 計算半徑為r的圓的圓周
def calc_area(r):
    return 2 * math.pi * r


# 半徑2～5範圍的圓周總和
s = scipy.integrate.quad(calc_area, 2, 5)
print(s)

# 廁所衛生紙長度 若厚度為0.011
x = s[0] / 0.011
print(x)

print("------------------------------------------------------------")  # 60個

print(
    "---- scipy.special --------------------------------------------------------"
)  # 60個

a = scipy.special.exp10(3)
print("10^3 =", a)

b = scipy.special.exp2(3)
print("2^3 =", b)

c = scipy.special.sindg(90)
print("sind(90) =", c)

d = scipy.special.cosdg(45)
print("cosd(45) =", d)

print(
    "---- scipy.interpolate --------------------------------------------------------"
)  # 60個

print("內插法1")

x = np.arange(5, 20)
y = scipy.special.exp2(x / 3.0)
plt.plot(x, y, "o")

plt.show()

f = scipy.interpolate.interp1d(x, y)
x1 = np.arange(5, 20)
y1 = f(x1)
plt.plot(x, y, "o", x1, y1, "--")

plt.show()

print("內插法2")

x = [1, 2, 3, 4, 5]
y = [5, 8, 7, 4, 3]
plt.plot(x, y, "o")

plt.show()

f = scipy.interpolate.interp1d(x, y)
x1 = [1, 2, 3, 4, 5]
y1 = f(x1)
plt.plot(x, y, "o", x1, y1, "--")

xx = 1.5
yy = f(xx)
print("xx =", xx)
print("yy =", yy)

plt.grid()

plt.show()

print("------------------------------------------------------------")  # 60個

print(
    "---- scipy.optimize --------------------------------------------------------"
)  # 60個

def f(x):
    return x**2 + 15 * np.sin(x)

x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x))

#plt.show()

print("------------------------------------------------------------")  # 60個

result = scipy.optimize.minimize(f, x0=0)
print(result.x)

plt.plot(x, f(x))
plt.plot(result.x, f(result.x), "o")

#plt.show()

print("------------------------------------------------------------")  # 60個

def fmax(x):
    """計算最大值"""
    return -(-3 * x**2 + 12 * x - 9)


def f(x):
    """求解方程式"""
    return -3 * x**2 + 12 * x - 9


a = -3
b = 12
c = -9
r1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # r1
r1_y = f(r1)  # f(r1)
plt.text(r1 + 0.1, r1_y + -0.2, "(" + str(round(r1, 2)) + "," + str(0) + ")")
plt.plot(r1, r1_y, "-o")  # 標記
print("root1 = ", r1)  # print(r1)
r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # r2
r2_y = f(r2)  # f(r2)
plt.text(r2 - 0.5, r2_y - 0.2, "(" + str(round(r2, 2)) + "," + str(0) + ")")
plt.plot(r2, r2_y, "-o")  # 標記
print("root2 = ", r2)  # print(r2)

# 計算最大值
r = scipy.optimize.minimize_scalar(fmax)
print("當x是 %4.2f 時, 有函數最大值 %4.2f" % (r.x, f(r.x)))
plt.text(
    r.x - 0.25,
    f(r.x) - 0.7,
    "(" + str(round(r.x, 2)) + "," + str(round(f(r.x), 2)) + ")",
)
plt.plot(r.x, f(r.x), "-o")  # 標記

# 繪製此函數圖形
x = np.linspace(0, 4, 50)
y = -3 * x**2 + 12 * x - 9
plt.plot(x, y, color="b")
plt.grid()

#plt.show()

print("------------------------------------------------------------")  # 60個


def f(x):
    """求解方程式"""
    return 3 * x**2 - 12 * x + 10


a = 3
b = -12
c = 10
r1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # r1
r1_y = f(r1)  # f(r1)
plt.text(r1 + 0.1, r1_y - 0.2, "(" + str(round(r1, 2)) + "," + str(0) + ")")
plt.plot(r1, r1_y, "-o")  # 標記
print("root1 = ", r1)  # print(r1)
r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # r2
r2_y = f(r2)  # f(r2)
plt.text(r2 - 0.6, r2_y - 0.2, "(" + str(round(r2, 2)) + "," + str(0) + ")")
plt.plot(r2, r2_y, "-o")  # 標記
print("root2 = ", r2)  # print(r2)

# 計算最小值
r = scipy.optimize.minimize_scalar(f)
print("當x是 %4.2f 時, 有函數最小值 %4.2f" % (r.x, f(r.x)))
plt.text(
    r.x - 0.25,
    f(r.x) + 0.3,
    "(" + str(round(r.x, 2)) + "," + str(round(f(r.x), 2)) + ")",
)
plt.plot(r.x, f(r.x), "-o")  # 標記

# 繪製此函數圖形
x = np.linspace(0, 4, 50)
y = 3 * x**2 - 12 * x + 10
plt.plot(x, y, color="b")

#plt.show()

print("------------------------------------------------------------")  # 60個


def fmax(x):
    """計算最大值"""
    return -(-3 * x**2 + 12 * x - 9)


def f(x):
    """求解方程式"""
    return -3 * x**2 + 12 * x - 9


a = -3
b = 12
c = -9
r1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # r1
r1_y = f(r1)  # f(r1)
plt.text(r1 + 0.1, r1_y + -0.2, "(" + str(round(r1, 2)) + "," + str(0) + ")")
plt.plot(r1, r1_y, "-o")  # 標記
print("root1 = ", r1)  # print(r1)
r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # r2
r2_y = f(r2)  # f(r2)
plt.text(r2 - 0.5, r2_y - 0.2, "(" + str(round(r2, 2)) + "," + str(0) + ")")
plt.plot(r2, r2_y, "-o")  # 標記
print("root2 = ", r2)  # print(r2)

# 計算最大值
r = scipy.optimize.minimize_scalar(fmax)
print("當x是 %4.2f 時, 有函數最大值 %4.2f" % (r.x, f(r.x)))
plt.text(
    r.x - 0.25,
    f(r.x) - 0.7,
    "(" + str(round(r.x, 2)) + "," + str(round(f(r.x), 2)) + ")",
)
plt.plot(r.x, f(r.x), "-o")  # 標記

print("------------------------------------------------------------")  # 60個

print(
    "---- scipy.stats --------------------------------------------------------"
)  # 60個

def normal_pdf(x, mu, sigma):
    pi = 3.1415926
    e = 2.718281
    f = (1.0 / np.sqrt(2 * pi * sigma**2)) * e ** (
        -((x - mu) ** 2) / (2.0 * sigma**2)
    )
    return f


ax = np.linspace(-5, 5, 100)
ay = [normal_pdf(x, 0, 1) for x in ax]
plt.plot(ax, ay)

#plt.show()

x = [x / 10.0 for x in range(-50, 60)]
plt.plot(x, scipy.stats.norm.pdf(x, 0, 1), "r-", lw=1, alpha=0.6, label="mu=0,sigma=1")
plt.plot(x, scipy.stats.norm.pdf(x, 0, 2), "b--", lw=1, alpha=0.6, label="mu=0,sigma=2")
plt.plot(x, scipy.stats.norm.pdf(x, 2, 1), "g-.", lw=1, alpha=0.6, label="mu=2,sigma=1")
plt.legend()
plt.title("Various Normal PDF")

#plt.show()

samples = [9, 3, 27]

desc = scipy.stats.describe(samples)
print(desc)

samples2 = [[1, 3, 27], [3, 4, 6], [7, 6, 3], [3, 6, 8]]

desc = scipy.stats.describe(samples2, axis=0)
print(desc)


desc = scipy.stats.describe(samples2, axis=1)
print(desc)

print(
    "---- scipy.signal --------------------------------------------------------"
)  # 60個

t = np.linspace(6, 10, 500)
w = scipy.signal.chirp(t, f0=4, f1=2, t1=5, method="linear")
plt.plot(t, w)
plt.title("Linear Chirp")
plt.xlabel("time in sec)")

#plt.show()

img = np.load("scipy_data/digit8.npy")

plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")

#plt.show()

print("------------------------------------------------------------")  # 60個

edge = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("original image")
plt.subplot(1, 2, 2)
c_digit = scipy.signal.convolve2d(img, edge, boundary="symm", mode="same")
plt.imshow(c_digit, cmap="gray")
plt.axis("off")
plt.title("edge-detection image")

#plt.show()

print("------------------------------------------------------------")  # 60個

sharpen = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("original image")
plt.subplot(1, 2, 2)
c_digit = scipy.signal.convolve2d(img, sharpen, boundary="symm", mode="same")
plt.imshow(c_digit, cmap="gray")
plt.axis("off")
plt.title("sharpen image")

#plt.show()

print("------------------------------------------------------------")  # 60個

img = np.load("scipy_data/digit3.npy")
filters = [
    [[-1, -1, -1], [1, 1, 1], [0, 0, 0]],
    [[-1, 1, 0], [-1, 1, 0], [-1, 1, 0]],
    [[0, 0, 0], [1, 1, 1], [-1, -1, -1]],
    [[0, 1, -1], [0, 1, -1], [0, 1, -1]],
]

plt.figure()
plt.subplot(1, 5, 1)
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("original")

for i in range(2, 6):
    plt.subplot(1, 5, i)
    c = scipy.signal.convolve2d(img, filters[i - 2], boundary="symm", mode="same")
    plt.imshow(c, cmap="gray")
    plt.axis("off")
    plt.title("filter" + str(i - 1))

#plt.show()

print("------------------------------------------------------------")  # 60個

A = np.array([[2, 3], [5, 7]])
B = scipy.linalg.inv(A)
print(B)

A = np.array([[3, 8], [4, 6]])
B = scipy.linalg.det(A)
print(B)

a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

x = scipy.linalg.solve(a, b)
print(x)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("傑卡德相似係數 Jaccard Similarity Coefficient")

mat1 = [1, 1, 0, 1, 0, 1, 0, 0, 1]
mat2 = [0, 1, 1, 0, 0, 0, 1, 1, 1]
mat3 = [1, 1, 0, 1, 0, 1, 0, 0, 1]  # the same as mat1
mat4 = [0, 0, 1, 0, 1, 0, 1, 1, 0]  # invert of mat1

matV = np.mat([mat1, mat4])
print(type(matV))
print(matV)
print("傑卡德相似係數 : ")
print(scipy.spatial.distance.pdist(matV, "jaccard"))

print("------------------------------------------------------------")  # 60個


print(
    "---- scipy.stats.norm --------------------------------------------------------"
)  # 60個

# MH采样

data = np.random.randn(200)
print("平均 :", np.mean(data))


def sampler(
    data,
    samples=100,
    mu_init=0.2,
    proposal_width=0.1,
    plot=False,
    mu_prior_mu=0,
    mu_prior_sd=1.0,
):
    mu_current = mu_init
    posterior = [mu_current]
    for i in range(samples):
        mu_proposal = scipy.stats.norm(mu_current, proposal_width).rvs()

        likelihood_current = scipy.stats.norm(mu_current, 1).pdf(data).prod()
        likelihood_proposal = scipy.stats.norm(mu_proposal, 1).pdf(data).prod()

        prior_current = scipy.stats.norm(mu_prior_mu, mu_prior_sd).pdf(mu_current)
        prior_proposal = scipy.stats.norm(mu_prior_mu, mu_prior_sd).pdf(mu_proposal)

        p_current = likelihood_current * prior_current
        p_proposal = likelihood_proposal * prior_proposal

        p_accept = p_proposal / p_current

        accept = np.random.rand() < p_accept

        if accept:
            # Update position
            mu_current = mu_proposal
            posterior.append(mu_current)

    return posterior


tt = sampler(data, samples=5)
print(tt)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

