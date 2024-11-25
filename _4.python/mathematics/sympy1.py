import sympy

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
'''
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
plt.grid()  # 加格線

plt.show()

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
plt.grid()  # 加格線

plt.show()

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
plt.grid()  # 加格線

plt.show()

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
plt.grid()  # 加格線
plt.axis("equal")  # 讓x, y軸距長度一致

plt.show()

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
plt.grid()  # 加格線
plt.axis("equal")  # 讓x, y軸距長度一致

plt.show()

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
print("root1 = ", r1)  # print(r1)

r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # r2
r2_y = f1(r2)  # f1(r2)
plt.text(r2 - 0.2, r2_y + 0.3, "(" + str(round(r2, 2)) + "," + str(0) + ")")
plt.plot(r2, r2_y, "-o")  # 標記
print("root2 = ", r2)  # print(r2)

# 繪製此函數圖形
xx = np.linspace(0, 4, 50)
yy = 3 * xx**2 - 12 * xx + 10
plt.plot(xx, yy)

plt.show()

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
plt.grid()  # 加格線

plt.show()

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
plt.grid()  # 加格線

plt.show()

print("------------------------------------------------------------")  # 60個

a, b = 500, 600
numbers = range(a, b)
prime_numbers = filter(sympy.isprime, numbers)

print("從 {} 到 {} 之間的質數 :".format(a, b))
for prime_number in prime_numbers:
    print(prime_number, end=",")
print()

print("------------------------------------------------------------")  # 60個

# 定義公式中使用的變數
x, y, z = sympy.symbols("x y z")
sympy.init_printing()
sympy.Integral(sympy.sqrt(1 / x), x)

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
'''

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
line.show()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
