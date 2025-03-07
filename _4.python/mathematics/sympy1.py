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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import sympy


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
'''
print("sympy模組的版本")

VERSION = sympy.__version__
print(VERSION)

print("------------------------------------------------------------")  # 60個
print("解方程式 ST")
print("------------------------------------------------------------")  # 60個

print("解二元一次方程式")

# 定義公式中使用的變數
x = sympy.Symbol("x")
y = sympy.Symbol("y")

eq1 = x - y  # 方程式 1 : x - y = 0
eq2 = x + y - 10  # 方程式 2 : x + y - 10 = 0

# 解二元一次方程式
root = sympy.solve((eq1, eq2))
print(type(root))
print(root)
print("x = {}".format(root[x]))
print("y = {}".format(root[y]))

print("------------------------------------------------------------")  # 60個

print("解二元一次方程式")

# 定義公式中使用的變數
a = sympy.Symbol("a")  # 定義公式中使用的變數
b = sympy.Symbol("b")  # 定義公式中使用的變數
eq1 = a - b  # 方程式 1 : x - y = 0
eq2 = a + b - 10  # 方程式 2 : x + y - 10 = 0
root = sympy.solve((eq1, eq2))
print(type(root))
print(root)
print("a = {}".format(root[a]))
print("b = {}".format(root[b]))

pt_x1 = 60
pt_y1 = root[a] * pt_x1 + root[b]  # 計算x=60時的y值
pt_x2 = 100
pt_y2 = root[a] * pt_x2 + root[b]  # 計算x=100時的y值

xx = np.linspace(0, 250, 251)
yy = root[a] * xx + root[b]
plt.plot(xx, yy)  # 繪函數直線

plt.plot(pt_x1, pt_y1, "-o")  # 繪點 pt1
plt.text(pt_x1 + 10, pt_y1 - 10, "pt1")  # 輸出文字pt1

plt.plot(pt_x2, pt_y2, "-o")  # 繪點 pt2
plt.text(pt_x2 + 10, pt_y2 - 10, "pt2")  # 輸出文字pt2

plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()

show()

print("------------------------------------------------------------")  # 60個

print("解二元一次方程式")

# 定義公式中使用的變數
x = sympy.Symbol("x")  # 定義公式中使用的變數
y = sympy.Symbol("y")  # 定義公式中使用的變數
eq1 = x + y - 35  # 方程式 1
eq2 = 2 * x + 4 * y - 100  # 方程式 2
eq1 = x - y  # 方程式 1 : x - y = 0
eq2 = x + y - 10  # 方程式 2 : x + y - 10 = 0
root = sympy.solve((eq1, eq2))
print("x = {}".format(root[x]))
print("y = {}".format(root[y]))

line1_x = np.linspace(0, 10, 100)
line1_y = [y for y in line1_x]
line2_x = np.linspace(0, 10, 100)
line2_y = [10 - y for y in line2_x]

plt.plot(line1_x, line1_y, "r")  # 繪函數直線公式 1
plt.plot(line2_x, line2_y, "g")  # 繪函數直線公式 2

plt.plot(root[x], root[y], "b-o")  # 繪交叉點
plt.text(root[x] + 0.5, root[y] + 0, "(" + str(root[x]) + "," + str(root[y]) + ")")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

show()

print("------------------------------------------------------------")  # 60個

print("解二元一次方程式")

# 定義公式中使用的變數
x = sympy.Symbol("x")  # 定義公式中使用的變數
y = sympy.Symbol("y")  # 定義公式中使用的變數
eq1 = x + y - 100  # 方程式 1
eq2 = 2 * x + 4 * y - 350  # 方程式 2
eq1 = x - y  # 方程式 1 : x - y = 0
eq2 = x + y - 10  # 方程式 2 : x + y - 10 = 0
root = sympy.solve((eq1, eq2))
print("x = {}".format(root[x]))
print("y = {}".format(root[y]))

line1_x = np.linspace(0, 10, 100)
line1_y = [y for y in line1_x]
line2_x = np.linspace(0, 10, 100)
line2_y = [10 - y for y in line2_x]

plt.plot(line1_x, line1_y, "r")  # 繪函數直線公式 1
plt.plot(line2_x, line2_y, "g")  # 繪函數直線公式 2

plt.plot(root[x], root[y], "b-o")  # 繪交叉點
plt.text(root[x] + 0.5, root[y] + 0, "(" + str(root[x]) + "," + str(root[y]) + ")")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

show()

print("------------------------------------------------------------")  # 60個

print("解二元一次方程式")

# 定義公式中使用的變數
x = sympy.Symbol("x")  # 定義公式中使用的變數
y = sympy.Symbol("y")  # 定義公式中使用的變數
eq1 = x - y  # 方程式 1
eq2 = -x - y + 2  # 方程式 2
eq1 = x - y  # 方程式 1 : x - y = 0
eq2 = x + y - 10  # 方程式 2 : x + y - 10 = 0

root = sympy.solve((eq1, eq2))
print("x = {}".format(root[x]))
print("y = {}".format(root[y]))

line1_x = np.linspace(0, 10, 100)
line1_y = [y for y in line1_x]
line2_x = np.linspace(0, 10, 100)
line2_y = [10 - y for y in line2_x]

plt.plot(line1_x, line1_y, "r")  # 繪函數直線公式 1
plt.plot(line2_x, line2_y, "g")  # 繪函數直線公式 2

plt.plot(root[x], root[y], "b-o")  # 繪交叉點
plt.text(root[x] + 0.5, root[y] + 0, "(" + str(root[x]) + "," + str(root[y]) + ")")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.axis("equal")  # 讓x, y軸距長度一致

show()

print("------------------------------------------------------------")  # 60個

print("解二元一次方程式")

# 定義公式中使用的變數
x = sympy.Symbol("x")  # 定義公式中使用的變數
y = sympy.Symbol("y")  # 定義公式中使用的變數
eq1 = 0.5 * x - y - 0.5  # 方程式 1
eq2 = -2 * x - y + 7  # 方程式 2
eq1 = x - y  # 方程式 1 : x - y = 0
eq2 = x + y - 10  # 方程式 2 : x + y - 10 = 0
root = sympy.solve((eq1, eq2))
print("x = {}".format(root[x]))
print("y = {}".format(root[y]))

line1_x = np.linspace(0, 10, 100)
line1_y = [y for y in line1_x]
line2_x = np.linspace(0, 10, 100)
line2_y = [10 - y for y in line2_x]

plt.plot(line1_x, line1_y, "r")  # 繪函數直線公式 1
plt.plot(line2_x, line2_y, "g")  # 繪函數直線公式 2

plt.plot(root[x], root[y], "b-o")  # 繪交叉點
plt.text(
    root[x] + 0.5, root[y] + 0, "(" + str(int(root[x])) + "," + str(int(root[y])) + ")"
)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.axis("equal")  # 讓x, y軸距長度一致

show()

print("------------------------------------------------------------")  # 60個

print("解一元二次方程式")

# 定義公式中使用的變數
x = sympy.Symbol("x")
# f = sympy.Symbol('f')

print("解一元二次方程式 f = x^2 -2x - 8")
f = x**2 - 2 * x - 8

print("解一元二次方程式 f = 3(x-2)^2 - 2")
f = 3 * (x - 2) ** 2 - 2

print("解一元二次方程式 f = -3.5x^2 + 18.5x - 20")
f = -3.5 * x**2 + 18.5 * x - 20

root = sympy.solve(f)

print(root)

x1 = round(root[0], 1)
x2 = round(root[1], 1)
print("x1 = {}".format(x1))
print("x2 = {}".format(x2))

print("------------------------------------------------------------")  # 60個

print("解一元二次方程式")


def f1(x):  # 求解方程式
    return 3 * x**2 - 12 * x + 10


def f2(x):  # 求解方程式
    return -3 * x**2 + 12 * x - 9


a = 3
b = -12
c = 10
r1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # r1
r1_y = f1(r1)  # f1(r1)
plt.text(r1 - 0.2, r1_y + 0.3, "(" + str(round(r1, 2)) + "," + str(0) + ")")
plt.plot(r1, r1_y, "-o")  # 標記
print("root1 = ", r1)

r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # r2
r2_y = f1(r2)  # f1(r2)
plt.text(r2 - 0.2, r2_y + 0.3, "(" + str(round(r2, 2)) + "," + str(0) + ")")
plt.plot(r2, r2_y, "-o")  # 標記
print("root2 = ", r2)

# 繪製此函數圖形
xx = np.linspace(0, 4, 50)
yy = 3 * xx**2 - 12 * xx + 10
plt.plot(xx, yy)

show()

print("------------------------------------------------------------")  # 60個

print("解三元一次方程式")

# 定義公式中使用的變數
a = sympy.Symbol("a")  # 定義公式中使用的變數
b = sympy.Symbol("b")  # 定義公式中使用的變數
c = sympy.Symbol("c")  # 定義公式中使用的變數
eq1 = a + b + c - 500  # 第100次公式
eq2 = 4 * a + 2 * b + c - 1000  # 第200次公式
eq3 = 9 * a + 3 * b + c - 2000  # 第300次公式
root = sympy.solve((eq1, eq2, eq3))
print("a = {}".format(root[a]))
print("b = {}".format(root[b]))
print("c = {}".format(root[c]))

xx = np.linspace(0, 5, 50)
yy = [(root[a] * yy**2 + root[b] * yy + root[c]) for yy in xx]
plt.plot(xx, yy)  # 繪二次函數

x4 = 4  # 第400次
y4 = root[a] * x4**2 + root[b] * x4 + root[c]  # 第400次的y值
plt.plot(x4, y4, "-o")  # 繪交叉點
plt.text(x4 - 0.7, y4 - 50, "(" + str(x4) + "," + str(y4) + ")")

plt.plot(1, 500, "-x", color="b")  # 繪100次業績點
plt.text(1 - 0.7, 500 - 50, "(" + str(1) + "," + str(500) + ")")
plt.plot(2, 1000, "-x", color="b")  # 繪200次業績點
plt.text(2 - 0.7, 1000 - 50, "(" + str(2) + "," + str(1000) + ")")
plt.plot(3, 2000, "-x", color="b")  # 繪300次業績點
plt.text(3 - 0.7, 2000 - 50, "(" + str(3) + "," + str(2000) + ")")

plt.xlabel("Times(unit=100)")
plt.ylabel("Revenue")
plt.grid()

show()

print("------------------------------------------------------------")  # 60個

print("解三元一次方程式")

# 定義公式中使用的變數
a = sympy.Symbol("a")  # 定義公式中使用的變數
b = sympy.Symbol("b")  # 定義公式中使用的變數
c = sympy.Symbol("c")  # 定義公式中使用的變數
eq1 = a + b + c - 10  # 第1次公式
eq2 = 4 * a + 2 * b + c - 18  # 第2次公式
eq3 = 9 * a + 3 * b + c - 19  # 第3次公式
root = sympy.solve((eq1, eq2, eq3))
print("a = {}".format(root[a]))
print("b = {}".format(root[b]))
print("c = {}".format(root[c]))

xx = np.linspace(0, 4, 50)
yy = [(root[a] * yy**2 + root[b] * yy + root[c]) for yy in xx]
plt.plot(xx, yy)  # 繪二次函數

plt.plot(1, 10, "-x", color="b")  # 繪1次業績點
plt.plot(2, 18, "-x", color="b")  # 繪2次業績點
plt.plot(3, 19, "-x", color="b")  # 繪3次業績點

h = -1 * root[b] / (2 * root[a])
k = (4 * root[a] * root[c] - (root[b] ** 2)) / (4 * root[a])
plt.plot(h, k, "-o", color="b")  # 繪最大值座標
h = round(float(h), 1)
k = round(float(k), 1)
plt.text(h - 0.25, k - 1.5, "(" + str(h) + "," + str(k) + ")")

plt.xlabel("Times")
plt.ylabel("Performance")
plt.grid()

show()

print("------------------------------------------------------------")  # 60個

a, b, c = sympy.symbols("a,b,c")
print(sympy.solve(a * x**2 + b * x + c, x))

print(sympy.solve((x**2 + x * y + 1, y**2 + x * y + 2), x, y))

print(sympy.roots(x**3 - 3 * x**2 + x + 1))

print("------------------------------------------------------------")  # 60個
print("解方程式 SP")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("微分積分 ST")
print("------------------------------------------------------------")  # 60個

# 數值微分

x = sympy.symbols("x", real=True)
h = sympy.symbols("h", positive=True)
f = sympy.symbols("f", cls=sympy.Function)

f_diff = f(x).diff(x, 1)
print(f_diff)

expr_diff = sympy.calculus.finite_diff._as_finite_diff(
    f_diff, [x, x - h, x - 2 * h, x - 3 * h]
)
print(expr_diff)

sym_dexpr = f_diff.subs(f(x), x * sympy.exp(-(x**2))).doit()
print(sym_dexpr)

sym_dfunc = sympy.lambdify([x], sym_dexpr, modules="numpy")
cc = sym_dfunc(np.array([-1, 0, 1]))
print(cc)
# array([-0.36787944,  1.        , -0.36787944])

print(expr_diff.args)
# (-3*f(-h + x)/h, -f(-3*h + x)/(3*h), 3*f(-2*h + x)/(2*h), 11*f(x)/(6*h))

w = sympy.Wild("w")
c = sympy.Wild("c")
patterns = [arg.match(c * f(w)) for arg in expr_diff.args]
print(patterns[0])
# {w_: -h + x, c_: -3/h}

coefficients = [t[c] for t in sorted(patterns, key=lambda t: t[w])]
print(coefficients)

coeff_arr = np.array([float(coeff.subs(h, 1e-3)) for coeff in coefficients])
print(coeff_arr)


def moving_window(x, size):
    from numpy.lib.stride_tricks import as_strided

    x = np.ascontiguousarray(x)
    return as_strided(
        x, shape=(x.shape[0] - size + 1, size), strides=(x.itemsize, x.itemsize)
    )

x_arr = np.arange(-2, 2, 1e-3)
y_arr = x_arr * np.exp(-x_arr * x_arr)

num_res = (moving_window(y_arr, 4) * coeff_arr).sum(axis=1)
sym_res = sym_dfunc(x_arr[3:])

print(np.max(abs(num_res - sym_res)))


def finite_diff_coefficients(f_diff, order, h):
    v = f_diff.variables[0]
    points = [x - i * h for i in range(order)]
    expr_diff = sympy.calculus.finite_diff._as_finite_diff(f_diff, points)
    w = sympy.Wild("w")
    c = sympy.Wild("c")
    patterns = [arg.match(c * f(w)) for arg in expr_diff.args]
    coefficients = np.array([float(t[c]) for t in sorted(patterns, key=lambda t: t[w])])
    return coefficients


# %figonly=比較不同點數的數值微分的誤差
fig, ax = plt.subplots(figsize=(8, 4))

for order in range(2, 5):
    c = finite_diff_coefficients(f_diff, order, 1e-3)
    num_diff = (moving_window(y_arr, order) * c).sum(axis=1)
    sym_diff = sym_dfunc(x_arr[order - 1 :])
    error = np.abs(num_diff - sym_diff)
    ax.semilogy(x_arr[order - 1 :], error, label=str(order))

ax.legend(loc="best")

show()

print("------------------------------------------------------------")  # 60個

# 定義公式中使用的變數
x, y, z = sympy.symbols("x y z")
sympy.init_printing()
sympy.Integral(sympy.sqrt(1 / x), x)

print("------------------------------------------------------------")  # 60個

print("積分")
from sympy import symbols
from sympy import integrate
from sympy import sqrt

x = symbols("x")
cc = integrate(sqrt(1 - x**2), (x, -1, 1)) * 2
print(cc)

print("------------------------------------------------------------")  # 60個

x = sympy.symbols("x")

# 球體體積

cc = sympy.integrate(x * sympy.sin(x), x)
print(cc)

cc = sympy.integrate(x * sympy.sin(x), (x, 0, 2 * sympy.pi))
print(cc)

x, y = sympy.symbols("x, y")
r = sympy.symbols("r", positive=True)
circle_area = 2 * sympy.integrate(sympy.sqrt(r**2 - x**2), (x, -r, r))
cc = circle_area
print(cc)

circle_area = circle_area.subs(r, sympy.sqrt(r**2 - x**2))
cc = circle_area
print(cc)

cc = sympy.integrate(circle_area, (x, -r, r))
print(cc)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("微分積分 SP")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

a, b = 500, 600
numbers = range(a, b)
prime_numbers = filter(sympy.isprime, numbers)

print("從 {} 到 {} 之間的質數 :".format(a, b))
for prime_number in prime_numbers:
    print(prime_number, end=",")
print()

print("------------------------------------------------------------")  # 60個

A = sympy.FiniteSet("a", "b")
B = sympy.FiniteSet("c", "d")
AB = A * B
for ab in AB:
    print(type(ab), ab)

print("------------------------------------------------------------")  # 60個

A = sympy.FiniteSet("a", "b", "c", "d", "e")
B = sympy.FiniteSet("f", "g")
AB = A * B
print("The length of Cartesian product", len(AB))
for ab in AB:
    print(ab)

print("------------------------------------------------------------")  # 60個

A = sympy.FiniteSet("a", "b")
AAA = A**3
print("The length of Cartesian product", len(AAA))
for a in AAA:
    print(a)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""
eq1 = x + y - 1
eq2 = 5 * x + y - 3
eq1 = -1 * x + y - 2  # -x + y - 2 = 0
eq2 = 2 * x + y - 4   # 2*x + y - 4 = 0
eq1 = -3 / 2 * x + 6 - y  # 直線1的式子
eq2 = 1 / 2 * x + 2 - y   # 直線2的式子
eq1 = 4 * x - 4 * y      # 4*x - 4*y = 0
eq2 = -6 * x -2 * y + 4  # -6*x - 2*y + 4
eq1 = -x + y -2
eq2 = x + y - 4
eq1 = 8 - 0.6 * x - y                   # 方程式 1
eq2 = 17.5 - 2.5 * x - y                # 方程式 2
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("繪製座標圖")
print("y = 2 * x - 5")
from sympy.plotting import plot

x = sympy.Symbol("x")

# 預設
# plot(2*x-5)

# 設定 x軸區間
# plot((2*x-5), (x, -5, 5))

# 設定 x軸 標籤 與標題
# plot((2*x-5), (x, -5, 5), title ='Sympy', xlabel = 'x', ylabel = '2x-5')

# 多函數圖形
# plot(2*x-5, '3*x+2')

# 設定線的顏色 + 圖例
line = plot(2 * x - 5, "3*x+2", legend=True, show=False)
line[0].line_color = "r"  # 第0條線
line[1].line_color = "g"  # 第1條線

#不顯示
#line.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SymPy-符號運算好幫手

cc = sympy.E ** (sympy.I * sympy.pi) + 1
print(cc)

x = sympy.symbols("x")
cc = sympy.expand(sympy.E ** (sympy.I * x))
print(cc)

cc = sympy.expand(sympy.exp(sympy.I * x), complex=True)
print(cc)

x = sympy.Symbol("x", real=True)
cc = sympy.expand(sympy.exp(sympy.I * x), complex=True)
print(cc)

tmp = sympy.series(sympy.exp(sympy.I * x), x, 0, 10)
print(tmp)

print(sympy.re(tmp))

cc = sympy.series(sympy.cos(x), x, 0, 10)
print(cc)

cc = sympy.im(tmp)
print(cc)

cc = sympy.series(sympy.sin(x), x, 0, 10)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 數學表達式
# 符號

print(sympy.var("x0,y0,x1,y1"))

print(type(x0))
print(x0.name)
print(type(x0.name))

x1, y1 = sympy.symbols("x1, y1")
type(x1)

x2 = sympy.Symbol("x2")

t = x0
a, b = sympy.symbols("alpha, beta")
cc = sympy.sin(a) + sympy.sin(b) + t
print(cc)

m, n = sympy.symbols("m, n", integer=True)
x = sympy.Symbol("x", positive=True)

cc = [attr for attr in dir(x) if attr.startswith("is_") and attr.lower() == attr]

print(cc)

print(x.is_Symbol)
print(x.is_positive)
print(x.is_imaginary)
print(x.is_complex)

cc = x.assumptions0
print(cc)

cc = sympy.Symbol.mro()
print(cc)

# 數值

print(1 / 2 + 1 / 3)
print(sympy.S(1) / 2 + 1 / sympy.S(3))

type(sympy.S(5) / 6)

cc = sympy.Rational(5, 10)  # 有理數會自動進行約分處理
print(cc)

print(sympy.N(0.1, 60))
print(sympy.N(10000.1, 60))

print(sympy.N(sympy.Float(0.1, 60), 60))  # 用浮點數建立Real物件時，精度和浮點數相同
print(sympy.N(sympy.Float("0.1", 60), 60))  # 用字串建立Real物件時，所特殊的精度有效
print(sympy.N(sympy.Float("0.1", 60), 65))  # 精度再高，也不是完全精確的

print(sympy.N(sympy.pi, 50))
print(sympy.N(sympy.sqrt(2), 50))

# 運算符和函數

sympy.var("x, y, z")
sympy.Add(x, y, z)

cc = sympy.Add(sympy.Mul(x, y, z), sympy.Pow(x, y), sympy.sin(z))
print(cc)

cc = x * y * z + x**y + sympy.sin(z)
print(cc)

t = x - y
print(t.func)
print(t.args)
print(t.args[0].func)
print(t.args[0].args)

# %fig=表達式的樹狀結構
from sympy.printing.dot import dotprint

graph = dotprint(x * y * sympy.sqrt(x**2 - y**2) / (x + y))
# %dot -f svg graph

# b'\r\n\r\n\r\n\r\nMulxyPowPowAdd-1yxAdd1/2MulPow-1Powy2x2

f = sympy.Function("f")

cc = issubclass(f, sympy.Function)
print(cc)

# True

t = f(x, y)
print(type(t))
print(t.func)
print(t.args)

t + t * t

"""
#通配符
    執行SymPy提供的init_printing()可以使用數學符號顯示運算結果。
    但它會將Python的內建物件也轉換成LateX顯示。為了撰寫方便，本書使用一般文字顯示內建物件，
    而用本書提供的%sympy_latex魔法方法將內建物件轉為LaTeX。
"""

x, y = sympy.symbols("x, y")
a = sympy.Wild("a")
b = sympy.Wild("b")

cc = (3 * x * (x + y) ** 2).match(a * b**2)
print(cc)

expr = sympy.expand((x + y) ** 3)
print(expr)
print(expr.find(a * b**2))


def find_match(expr, pattern):
    return [e.match(pattern) for e in expr.find(pattern)]


find_match(expr, a * b**2)

# 表達式 	比對結果

a = sympy.Wild("a", exclude=[1])
b = sympy.Wild("b", exclude=[1, sympy.Pow])

find_match(expr, a * b**2)

# 表達式 	比對結果

expr.replace(a * b**2, (a + b) ** 2)

expr = sympy.sqrt(x) / sympy.sin(y**2) + abs(sympy.exp(x) * x)

find_match(expr, f)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from IPython.display import Latex  # 用IPython

# %init_sympy_printing
x, y, z = sympy.symbols("x, y, z")
a, b = sympy.symbols("a, b")
f = sympy.Function("f")

# 符號運算
# 表達式變換和化簡

cc = sympy.simplify((x + 2) ** 2 - (x + 1) ** 2)
print(cc)

cc = sympy.radsimp(1 / (sympy.sqrt(5) + 2 * sympy.sqrt(2)))
print(cc)

cc = sympy.radsimp(1 / (y * sympy.sqrt(x) + x * sympy.sqrt(y)))
print(cc)

cc = sympy.ratsimp(x / (x + y) + y / (x - y))
print(cc)

print(sympy.fraction(sympy.ratsimp(1 / x + 1 / y)))

print(sympy.fraction(1 / x + 1 / y))

cc = sympy.cancel((x**2 - 1) / (1 + x))
print(cc)

s = sympy.symbols("s")
trans_func = 1 / (s**3 + s**2 + s + 1)
cc = sympy.apart(trans_func)
print(cc)

cc = sympy.trigsimp(
    sympy.sin(x) ** 2 + 2 * sympy.sin(x) * sympy.cos(x) + sympy.cos(x) ** 2
)
print(cc)

cc = sympy.expand_trig(sympy.sin(2 * x + y))
print(cc)

from tabulate import tabulate
from IPython.display import Markdown  # 用IPython
from IPython.display import display_markdown  # 用IPython

flags = ["mul", "log", "multinomial", "power_base", "power_exp"]
expressions = [
    x * (y + z),
    sympy.log(x * y**2),
    (x + y) ** 3,
    (x * y) ** z,
    x ** (y + z),
]
infos = ["展開乘法", "展開對數函數的參數中的乘積和冪運算", "展開加減法表達式的整數次冪", "展開冪函數的底數乘積", "展開對冪函數的指數和"]
table = []
for flag, expression, info in zip(flags, expressions, infos):
    table.append(
        [
            "`{}`".format(flag),
            "`expand({})`".format(expression),
            "${}$".format(sympy.latex(sympy.expand(expression))),
            info,
        ]
    )

display_markdown(Markdown(tabulate(table, ["標志", "表達式", "結果", "說明"], "pipe")))


x, y, z = sympy.symbols("x,y,z", positive=True)
cc = sympy.expand(x * sympy.log(y * z), mul=False)
print(cc)

from tabulate import tabulate
from IPython.display import Markdown  # 用IPython

flags = ["complex", "func", "trig"]
expressions = [x * y, sympy.gamma(1 + x), sympy.sin(x + y)]
infos = ["展開乘法", "展開對數函數的參數中的乘積和冪運算", "展開加減法表達式的整數次冪", "展開冪函數的底數乘積", "展開對冪函數的指數和"]
table = []
for flag, expression, info in zip(flags, expressions, infos):
    table.append(
        [
            "`{}`".format(flag),
            "`expand({})`".format(expression),
            "${}$".format(sympy.latex(sympy.expand(expression))),
            info,
        ]
    )

display_markdown(Markdown(tabulate(table, ["標志", "表達式", "結果", "說明"], "pipe")))

x, y = sympy.symbols("x,y", complex=True)
cc = sympy.expand(x * y, complex=True)
print(cc)

cc = sympy.expand(sympy.gamma(1 + x), func=True)
print(cc)

cc = sympy.expand(sympy.sin(x + y), trig=True)
print(cc)

cc = sympy.factor(15 * x**2 + 2 * y - 3 * x - 10 * x * y)
print(cc)

eq = (1 + a * x) ** 3 + (1 + b * x) ** 2
eq2 = sympy.expand(eq)
cc = sympy.collect(eq2, x)
print(cc)

p = sympy.collect(eq2, x, evaluate=False)
print(p[sympy.S(1)])
print(p[x**2])

print(eq2.coeff(x, 0))
print(eq2.coeff(x, 2))

cc = sympy.collect(a * sympy.sin(2 * x) + b * sympy.sin(2 * x), sympy.sin(2 * x))
print(cc)

# 微分

t = sympy.Derivative(sympy.sin(x), x)
print(t)

cc = t.doit()
print(cc)

cc = sympy.diff(sympy.sin(2 * x), x)
print(cc)

cc = sympy.Derivative(f(x), x)
print(cc)

cc = sympy.Derivative(f(x), x, x, x)  # 也可以寫作Derivative(f(x), x, 3)
print(cc)

cc = sympy.Derivative(f(x, y), x, 2, y, 3)
print(cc)

cc = sympy.diff(sympy.sin(x * y), x, 2, y, 3)
print(cc)

# 微分方程式

x = sympy.symbols("x")
f = sympy.symbols("f", cls=sympy.Function)
cc = sympy.dsolve(sympy.Derivative(f(x), x) - f(x), f(x))
print(cc)

eq = sympy.Eq(f(x).diff(x) + f(x), (sympy.cos(x) - sympy.sin(x)) * f(x) ** 2)
cc = sympy.classify_ode(eq, f(x))
print(cc)

cc = sympy.dsolve(eq, f(x))
print(cc)

cc = sympy.dsolve(eq, f(x), hint="lie_group")
print(cc)

cc = sympy.dsolve(eq, f(x), hint="all")
print(cc)

"""
cc = sympy.ode.allhints
print(cc)
"""

# 積分

e = sympy.Integral(x * sympy.sin(x), x)
print(e)

cc = e.doit()
print(cc)

e2 = sympy.Integral(sympy.sin(x) / x, (x, 0, 1))
cc = e2.doit()
print(cc)

print(e2.evalf())
print(e2.evalf(50))  # 可以指定精度

e3 = sympy.Integral(sympy.sin(x) / x, (x, 0, sympy.oo))
cc = e3.evalf()
print(cc)

cc = e3.doit()
print(cc)
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 计算两个椭圆的交点

import pylab as pl

sympy.init_printing()

# 椭圆的参数方程

# 下面是用参数方程计算椭圆上各点，并绘图的函数：


def ellipse(e, t):
    from numpy import cos, sin

    a, b, x_c, y_c, theta = e
    ct, st, cth, sth = cos(t), sin(t), cos(theta), sin(theta)
    x = a * ct * cth - b * st * sth + x_c
    y = a * sth * ct + b * st * cth + y_c
    return x, y


def plot_ellipse(e):
    t = np.linspace(0, np.pi * 2, 100)
    x, y = ellipse(e, t)
    pl.plot(x, y)


e1 = (5.0, 3.0, 1.0, 2.0, 0.3)
plot_ellipse(e1)
x, y = ellipse(e1, [0, np.pi])
pl.plot(x, y, "--")
pl.plot(x.mean(), y.mean(), "o")
pl.axis("equal")
show()

# 椭圆的隐函数方程

x, y, theta, xc, yc, a, b = sympy.symbols("x y theta x_c y_c a b", real=True)
M = sympy.Matrix(
    [[sympy.cos(theta), sympy.sin(theta)], [-sympy.sin(theta), sympy.cos(theta)]]
)
P = sympy.Matrix([[x - xc], [y - yc]])
P2 = M * P
eq = (x / a) ** 2 + (y / b) ** 2 - 1
eq2 = eq.subs({x: P2[0], y: P2[1]}, simultaneous=True)
print(eq2)

# 隐函数方程的曲线可以通过等值线函数contour()绘制：


def implicit_ellipse(e, x, y):
    from numpy import cos, sin

    a, b, x_c, y_c, theta = e
    return (
        -1
        + (-(x - x_c) * sin(theta) + (y - y_c) * cos(theta)) ** 2 / b**2
        + ((x - x_c) * cos(theta) + (y - y_c) * sin(theta)) ** 2 / a**2
    )


yg, xg = np.mgrid[-2:6:100j, -5:7:100j]
zg = implicit_ellipse(e1, xg, yg)

pl.contour(xg, yg, zg, levels=[0])
show()

# 计算两个椭圆的交点

# 计算隐函数方程的系数

from IPython.display import display

p = eq2.as_poly(x, y)
for coef in p.coeffs(order="grlex"):
    display(coef)

display(P2)
sympy.cse(P2)

# 下面的两个函数可以将cse()得到结果转换成一个Python函数，用于数值运算。在后续的程序中生成的cse中会出现Eq和Piecewise函数。这里使用自定义PythoPrinter类将上述两个函数分别输出为等于操作符和调用_piecewise_func()函数。

from sympy.printing import StrPrinter


def _piecewise_func(*args):
    for expr, cond in args:
        if cond:
            return expr


class PythonPrinter(StrPrinter):
    def _print_Equality(self, expr):
        return "{} == {}".format(self._print(expr.lhs), self._print(expr.rhs))

    def _print_Piecewise(self, expr):
        return "_piecewise_func({})".format(
            ", ".join(self._print(arg) for arg in expr.args)
        )


cse2func_history = {}


def cse2func(funcname, precodes, seq, printer_class=PythonPrinter):
    import textwrap

    printer = printer_class()
    codes = ["def %s:" % funcname]
    if isinstance(precodes, str):
        precodes = [precodes]
    for line in precodes:
        codes.append("    %s" % line)
    for variable, value in seq[0]:
        codes.append("    %s = %s" % (variable, printer._print(value)))
    returns = "    return (%s)" % ", ".join([printer._print(value) for value in seq[1]])
    codes.append("\n".join(textwrap.wrap(returns, 80)))
    code = "\n".join(codes)
    # get_ipython().run_code(code)
    cse2func_history[funcname] = code
    return code


# 下面我们用cse2func()得到计算椭圆的隐函数方程系数的函数ellipse_equation():

seq = sympy.cse(p.coeffs(order="grlex"))
code = cse2func(
    "ellipse_equation(a, b, x_c, y_c, theta)", "from math import sin, cos", seq
)
print(code)


def ellipse_equation(a, b, x_c, y_c, theta):
    from math import sin, cos

    x0 = a ** (-2)
    x1 = cos(theta)
    x2 = x1**2
    x3 = x0 * x2
    x4 = b ** (-2)
    x5 = sin(theta)
    x6 = x5**2
    x7 = x4 * x6
    x8 = 2 * x1 * x5
    x9 = x0 * x8
    x10 = x4 * x8
    x11 = x0 * x6
    x12 = x2 * x4
    x13 = 2 * x_c
    x14 = 2 * y_c
    x15 = x9 * x_c
    x16 = x10 * x_c
    x17 = x_c**2
    x18 = y_c**2
    return (
        x3 + x7,
        -x10 + x9,
        x11 + x12,
        x10 * y_c - x13 * x3 - x13 * x7 - x9 * y_c,
        -x11 * x14 - x12 * x14 - x15 + x16,
        x11 * x18 + x12 * x18 + x15 * y_c - x16 * y_c + x17 * x3 + x17 * x7 - 1,
    )


# 下面是前面的椭圆e1的隐函数方程中各项的系数：

print(ellipse_equation(*e1))

# (0.04621028924765588, -0.040152353663646945, 0.10490082186345522, -0.012115871168017864, -0.3794509337901739, -0.6144911306258172)

# 交点的一元四阶方程的系数

# 首先参数方程：

theta, xc, yc, a, b, t = sympy.symbols("theta x_c y_c a b t", real=True)
x = a * sympy.cos(t)
y = b * sympy.sin(t)
M = sympy.Matrix(
    [[sympy.cos(theta), -sympy.sin(theta)], [sympy.sin(theta), sympy.cos(theta)]]
)
P = sympy.Matrix([[x], [y]])
xt, yt = M * P + sympy.Matrix([[xc], [yc]])
print(xt, yt)

# 将参数方程代入到隐函数方程中：

A, B, C, D, E, F, x, y = sympy.symbols("A B C D E F x y")
eq = A * x**2 + B * x * y + C * y**2 + D * x + E * y + F
eq = sympy.expand(eq.subs({x: xt, y: yt}))

tc = sympy.symbols("t_c")
sqrt_term = sympy.sqrt(1 - tc**2)
eq1 = eq.subs({sympy.cos(t): tc, sympy.sin(t): sqrt_term})

# leq为含有根号的项，req为不含根号的项。两边平方之后应该相等：

leq = sqrt_term * eq1.coeff(sqrt_term)
req = eq1 - sympy.expand(leq)
eq_square = sympy.expand(leq**2 - req**2)

p = eq_square.as_poly(tc)
seq = sympy.cse(p.coeffs())
cse2func(
    "ellipses_intersection_equation(A, B, C, D, E, F, a, b, x_c, y_c, theta)",
    "from math import sin, cos",
    seq,
)
show()

# 一元四次方程的解

a, b, c, d, e, x = sympy.symbols("a,b,c,d,e,x", real=True)
r = sympy.roots(sympy.Poly(a * x**4 + b * x**3 + c * x**2 + d * x + e), x).keys()
seq = sympy.cse(r)
cse2func(
    "roots4(a,b,c,d,e)",
    ["from cmath import sqrt", "if abs(a)<1e-10: return roots3(b,c,d,e)"],
    seq,
)

r = sympy.roots(sympy.Poly(b * x**3 + c * x**2 + d * x + e), x).keys()
seq = sympy.cse(r)
cse2func(
    "roots3(b,c,d,e)",
    ["from cmath import sqrt", "if abs(b)<1e-10: return roots2(c,d,e)"],
    seq,
)

r = sympy.roots(sympy.Poly(c * x**2 + d * x + e), x).keys()
seq = sympy.cse(r)
cse2func(
    "roots2(c,d,e)",
    ["from cmath import sqrt", "if abs(c)<1e-10: return roots1(d,e)"],
    seq,
)

r = sympy.roots(sympy.Poly(d * x + e), x).keys()
seq = sympy.cse(r)
cse2func("roots1(d,e)", ["from cmath import sqrt", "if abs(d)<1e-10: return []"], seq)

# 计算椭圆的交点


def ellipse(e, t):
    if np.isscalar(t):
        from math import cos, sin
    else:
        from numpy import cos, sin
    a, b, x_c, y_c, theta = e
    ct, st, cth, sth = cos(t), sin(t), cos(theta), sin(theta)
    x = a * ct * cth - b * st * sth + x_c
    y = a * sth * ct + b * st * cth + y_c
    return x, y


def ellipse_implicit(e, x, y):
    a, b, c, d, e, f = e
    return a * x**2 + b * x * y + c * y**2 + d * x + e * y + f


def ellipse_intersections(e1, e2, eps=1.0e-6):
    from math import acos, sqrt

    e1imp = ellipse_equation(*e1)
    p = ellipses_intersection_equation(*(tuple(e1imp) + e2))
    roots = [r.real for r in roots4(*p) if abs(r.imag) < eps]

    points = []
    for root in roots:
        t = acos(float(root))
        for t2 in [t, -t]:
            xp, yp = ellipse(e2, t2)
            if abs(ellipse_implicit(e1imp, xp, yp)) < eps:
                if not points:
                    points.append((xp, yp))
                else:
                    mindist = min(
                        [sqrt((po[0] - xp) ** 2 + (po[1] - yp) ** 2) for po in points]
                    )
                    if mindist > eps:
                        points.append((xp, yp))
    return points


# 下面的ellipse_plot()计算并绘制两个椭圆的交点。


def ellipse_plot(e1, e2, draw_e1=True, draw_e2=True):
    t = np.linspace(0, np.pi * 2, 100)
    x1, y1 = ellipse(e1, t)
    x2, y2 = ellipse(e2, t)
    if draw_e1:
        pl.plot(x1, y1)
    if draw_e2:
        pl.plot(x2, y2)

    points = ellipse_intersections(e1, e2)
    xp = [p[0] for p in points]
    yp = [p[1] for p in points]
    pl.plot(xp, yp, "o")
    show()


# 最后让我们看看程序的运行效果：

e1 = (5.0, 3.0, 1.0, 2.0, 0.2)
e2 = (7.0, 4.0, 0, 0, -0.3)
e3 = (5.0, 3.0, 1.0, 2.0, 0.2 + np.pi / 2)
""" NG
ellipse_plot(e1, e2)
ellipse_plot(e1, e3, False, True)
ellipse_plot(e2, e3, False, False)

e1 = (5.0, 3.0, 1.0, 2.0, 0.2)
e2 = (5.0, 3.0, -1.0, 1.2, 0.2)
ellipse_plot(e1, e2)

ellipse_plot((5.0, 3.0, 1.0, 2.0, 0.0), (5.0, 3.0, 0.0, 0.0, 0.0))

ellipse_plot((5.0, 3.0, 1.0, 2.0, 0.0), (5.0, 3.0, 1.0, 2.0, 0.01))

ellipse_plot((5.0, 3.0, 1.0, 2.0, 0.0), (5.0, 3.0, 1.0, 2.1, 0.0))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用SymPy把模拟滤波器转换为数字滤波器

from sympy import *
from cytoolz import compose

init_printing()

# 巴特沃斯低通滤波器的传递函数


s = Symbol("s", real=True)


def butterworth(n, s):
    n = S(n)
    sk = [exp(I * (2 * k + n - 1) * pi / (2 * n)) for k in range(S(1), n + 1)]
    denominator = Mul(*[s - v for v in sk])
    simplify_func = compose(simplify, expand, simplify, expand_complex)
    Hs = 1 / simplify_func(denominator)
    return Hs


# 下面是2阶和3阶滤波器的传递函数：

hs = butterworth(2, s)
print(hs)

hs = butterworth(3, s)
print(hs)

# 为了将标准的低通传递函数转换为任何圆频率omega的传递函数，可以对s进行如下替换：

wc = Symbol("\omega_c", real=True)


def lp2lp(hs, s, wc):
    return hs.subs(s, s / wc)


hs2 = lp2lp(hs, s, wc)
print(hs2)


def bilinear(hs, s, z, T):
    hz = hs.subs(s, 2 / T * (z - 1) / (z + 1))
    simplify_func = compose(simplify, expand, simplify, expand)
    return simplify_func(hz)


z, T = symbols("z T", real=True)
hz = bilinear(hs2, s, z, T)
print(hz)


def freqz(hs, z, w, T):
    hz_freq = hz.subs(z, exp(I * w * T))
    exp_hz_freq = expand_complex(hz_freq)
    return simplify(re(exp_hz_freq)), simplify(im(exp_hz_freq))


w = Symbol("\omega", real=True)
re_hz_freq, im_hz_freq = freqz(hs, z, w, T)

print(re_hz_freq)

print(im_hz_freq)

# 为了把上面的表达式转换为JavaScript代码，我们首先使用cse()对其进行分步运算。

steps, res = cse([re_hz_freq, im_hz_freq])
print(steps)

print(res)


def to_javascript(funcname, args, expr):
    from sympy.printing import jscode

    steps, res = cse(expr, symbols=numbered_symbols("_tmp"))
    code = ["window.{} = function(args){{".format(funcname)]

    for i, v in enumerate(args):
        code.append("var {} = args[{}];".format(str(v), i))

    for v, e in steps:
        code.append("var {} = {};".format(v, jscode(e)))

    code.append("return [{}];".format(", ".join(jscode(r) for r in res)))
    code.append("}")
    return "\n".join(code).replace("\\", "")


code = to_javascript("butter_lp_freqz", [T, w, wc], [re_hz_freq, im_hz_freq])
print(code)

# 下面通过IPython.display.display_javascript()将上述JavaScript代码输出到Notebook中。

from IPython.display import display_javascript

display_javascript(code, raw=True)

# from bokeh.io import output_notebook, show
# output_notebook()

# Loading BokehJS ...

# 最后调用本书提供的make_curve_viewer()显示滤波器的增益曲线。

# from bokehelp import make_curve_viewer


def freq_response(f, pars):
    w = 2 * Math.PI * f
    fs = pars["fs"]
    fc = pars["fc"]
    wc = 2 * Math.PI * fc
    T = 1 / fs
    re, im = butter_lp_freqz([T, w, wc])
    return dict(p=20 * Math.log10(Math.sqrt(re * re + im * im)))


inputs = [
    dict(title="fs", start=1000, end=10000, step=1000, value=5000),
    dict(title="fc", start=1, end=1000, step=1, value=100),
]

outputs = [dict(name="p", legend="p", line_width=2)]

""" NG
model = make_curve_viewer(freq_response, inputs, outputs, x_data=np.logspace(0, 4, 500), 
                          xlabel = "Freq(Hz)",
                          ylabel = "Gain(dB)",
                          fig_kwargs=dict(x_axis_type="log"))
show(model)
"""

# 下面的get_ba()得到滤波器的系数b和a。


def get_ba(hz, z):
    n, d = fraction(hz)
    b = Matrix(Poly(n, z).coeffs())
    a = Matrix(Poly(d, z).coeffs())
    b = b / a[0]
    a = a / a[0]
    return list(b) + list(a)


ba = get_ba(hz, z)
print(ba)

# 将上面的表达式转换为JavaScript代码：

ba_code = to_javascript("butter_ba", [T, wc], ba)
display_javascript(ba_code, raw=True)
print(ba_code)

# 下面使用Bokeh的DataTable显示运算结果。

from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn, Slider

# from bokeh.io import output_file, show
# from bokeh.layouts import column, row, widgetbox

data = dict(
    a=[0, 0, 0],
    b=[0, 0, 0],
)

""" NG
source = ColumnDataSource(data)

columns = [
        TableColumn(field="a", title="a"),
        TableColumn(field="b", title="b"),
    ]
data_table = DataTable(source=source, columns=columns, width=400, height=150)

sliders = [
    Slider(title="fs", start=1000, end=10000, step=1000, value=5000),
    Slider(title="fc", start=1, end=5000, step=1, value=100),
]
"""

""" NG
wbox = widgetbox(sliders)

def callback_func(source=source, wbox=wbox, table=data_table):
    window.table_t = table
    fs = wbox.children[0].value
    fc = wbox.children[1].value
    T = 1 / fs
    wc = 2 * Math.PI * fc
    ba = window.butter_ba([T, wc])
    source.data.a = ba[3:]
    source.data.b = ba[:3]
    source.change.emit()
    table.change.emit()
    
callback = CustomJS.from_py_func(callback_func)

for slider in sliders:
    slider.js_on_change("value", callback)

show(column(data_table, wbox))
"""
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
