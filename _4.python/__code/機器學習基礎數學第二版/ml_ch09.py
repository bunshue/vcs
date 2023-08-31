import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個
from sympy import *

x = Symbol('x')
f = Symbol('f')

print('解一元二次方程式 f = x^2 -2x - 8')
f = x**2 - 2*x - 8

print('解一元二次方程式 f = 3(x-2)^2 - 2')
f = 3*(x-2)**2 - 2

root = solve(f)
print(root)

print('------------------------------------------------------------')	#60個

from sympy import *

x = Symbol('x')

print('解一元二次方程式 f = -3.5x^2 + 18.5x - 20')
f = -3.5*x**2 + 18.5*x - 20

root = solve(f)

x1 = round(root[0], 1)
x2 = round(root[1], 1)
print('x1 = {}'.format(x1))
print('x2 = {}'.format(x2))

print('------------------------------------------------------------')	#60個

def f(x):
    ''' 求解方程式 '''
    return (3*x**2 - 12*x + 10)

a = 3
b = -12
c = 10
r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)         # r1
r1_y = f(r1)                                # f(r1)
plt.text(r1-0.2, r1_y+0.3, '('+str(round(r1,2))+','+str(0)+')')         
plt.plot(r1, r1_y, '-o')                    # 標記
print('root1 = ', r1)                       # print(r1)
r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)         # r2
r2_y = f(r2)                                # f(r2)
plt.text(r2-0.2, r2_y+0.3, '('+str(round(r2,2))+','+str(0)+')') 
plt.plot(r2, r2_y, '-o')                    # 標記
print('root2 = ', r2)                       # print(r2)

# 繪製此函數圖形
x = np.linspace(0, 4, 50)
y = 3*x**2 - 12*x + 10
plt.plot(x, y)

plt.show()

print('------------------------------------------------------------')	#60個

def f(x):
    ''' 求解方程式 '''
    return (-3*x**2 + 12*x - 9)

a = -3
b = 12
c = -9
r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)         # r1
r1_y = f(r1)                                # f(r1)
plt.text(r1-0.2, r1_y+0.3, '('+str(round(r1,2))+','+str(0)+')')         
plt.plot(r1, r1_y, '-o')                    # 標記
print('root1 = ', r1)                       # print(r1)
r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)         # r2
r2_y = f(r2)                                # f(r2)
plt.text(r2-0.3, r2_y+0.3, '('+str(round(r2,2))+','+str(0)+')') 
plt.plot(r2, r2_y, '-o')                    # 標記
print('root2 = ', r2)                       # print(r2)

# 繪製此函數圖形
x = np.linspace(0, 4, 50)
y = -3*x**2 + 12*x - 9
plt.plot(x, y)

plt.show()

print('------------------------------------------------------------')	#60個

from scipy.optimize import minimize_scalar

def f(x):
    ''' 求解方程式 '''
    return (3*x**2 - 12*x + 10)

a = 3
b = -12
c = 10
r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)         # r1
r1_y = f(r1)                                # f(r1)
plt.text(r1+0.1, r1_y-0.2, '('+str(round(r1,2))+','+str(0)+')')         
plt.plot(r1, r1_y, '-o')                    # 標記
print('root1 = ', r1)                       # print(r1)
r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)         # r2
r2_y = f(r2)                                # f(r2)
plt.text(r2-0.6, r2_y-0.2, '('+str(round(r2,2))+','+str(0)+')') 
plt.plot(r2, r2_y, '-o')                    # 標記
print('root2 = ', r2)                       # print(r2)

# 計算最小值
r = minimize_scalar(f)
print("當x是 %4.2f 時, 有函數最小值 %4.2f" % (r.x, f(r.x)))
plt.text(r.x-0.25, f(r.x)+0.3, '('+str(round(r.x,2))+','+str(round(f(r.x),2))+')') 
plt.plot(r.x, f(r.x), '-o')                 # 標記

# 繪製此函數圖形
x = np.linspace(0, 4, 50)
y = 3*x**2 - 12*x + 10
plt.plot(x, y, color='b')

plt.show()

print('------------------------------------------------------------')	#60個

from scipy.optimize import minimize_scalar

def fmax(x):
    ''' 計算最大值 '''
    return (-(-3*x**2 + 12*x - 9))

def f(x):
    ''' 求解方程式 '''
    return (-3*x**2 + 12*x - 9)

a = -3
b = 12
c = -9
r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)         # r1
r1_y = f(r1)                                # f(r1)
plt.text(r1+0.1, r1_y+-0.2, '('+str(round(r1,2))+','+str(0)+')')         
plt.plot(r1, r1_y, '-o')                    # 標記
print('root1 = ', r1)                       # print(r1)
r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)         # r2
r2_y = f(r2)                                # f(r2)
plt.text(r2-0.5, r2_y-0.2, '('+str(round(r2,2))+','+str(0)+')') 
plt.plot(r2, r2_y, '-o')                    # 標記
print('root2 = ', r2)                       # print(r2)

# 計算最大值
r = minimize_scalar(fmax)
print("當x是 %4.2f 時, 有函數最大值 %4.2f" % (r.x, f(r.x)))
plt.text(r.x-0.25, f(r.x)-0.7, '('+str(round(r.x,2))+','+str(round(f(r.x),2))+')') 
plt.plot(r.x, f(r.x), '-o')                 # 標記

print('------------------------------------------------------------')	#60個

from sympy import Symbol, solve

a = Symbol('a')                         # 定義公式中使用的變數
b = Symbol('b')                         # 定義公式中使用的變數
c = Symbol('c')                         # 定義公式中使用的變數

eq1 = a + b + c - 500                   # 第100次公式
eq2 = 4*a + 2*b + c - 1000              # 第200次公式
eq3 = 9*a + 3*b + c - 2000              # 第300次公式
root = solve((eq1, eq2, eq3))
print('a = {}'.format(root[a]))
print('b = {}'.format(root[b]))
print('c = {}'.format(root[c]))

print('------------------------------------------------------------')	#60個

from sympy import Symbol, solve

a = Symbol('a')                         # 定義公式中使用的變數
b = Symbol('b')                         # 定義公式中使用的變數
c = Symbol('c')                         # 定義公式中使用的變數
eq1 = a + b + c - 500                   # 第100次公式
eq2 = 4*a + 2*b + c - 1000              # 第200次公式
eq3 = 9*a + 3*b + c - 2000              # 第300次公式
root = solve((eq1, eq2, eq3))
print('a = {}'.format(root[a]))
print('b = {}'.format(root[b]))
print('c = {}'.format(root[c]))

x = np.linspace(0, 5, 50)
y = [(root[a]*y**2 + root[b]*y + root[c]) for y in x]
plt.plot(x, y)                          # 繪二次函數

x4 = 4                                  # 第400次
y4 = root[a]*x4**2 + root[b]*x4 + root[c]  # 第400次的y值
plt.plot(x4, y4, '-o')                  # 繪交叉點
plt.text(x4-0.7, y4-50, '('+str(x4)+','+str(y4)+')')

plt.plot(1, 500, '-x', color='b')       # 繪100次業績點
plt.text(1-0.7, 500-50, '('+str(1)+','+str(500)+')')
plt.plot(2, 1000, '-x', color='b')      # 繪200次業績點
plt.text(2-0.7, 1000-50, '('+str(2)+','+str(1000)+')')
plt.plot(3, 2000, '-x', color='b')      # 繪300次業績點
plt.text(3-0.7, 2000-50, '('+str(3)+','+str(2000)+')')

plt.xlabel("Times(unit=100)")
plt.ylabel("Revenue")
plt.grid()                              # 加格線

plt.show()

print('------------------------------------------------------------')	#60個

from sympy import Symbol, solve

a = Symbol('a')                         # 定義公式中使用的變數
b = Symbol('b')                         # 定義公式中使用的變數
c = Symbol('c')                         # 定義公式中使用的變數
eq1 = a + b + c - 10                    # 第1次公式
eq2 = 4*a + 2*b + c - 18                # 第2次公式
eq3 = 9*a + 3*b + c - 19                # 第3次公式
root = solve((eq1, eq2, eq3))
print('a = {}'.format(root[a]))
print('b = {}'.format(root[b]))
print('c = {}'.format(root[c]))

x = np.linspace(0, 4, 50)
y = [(root[a]*y**2 + root[b]*y + root[c]) for y in x]
plt.plot(x, y)                          # 繪二次函數

plt.plot(1, 10, '-x', color='b')        # 繪1次業績點
plt.plot(2, 18, '-x', color='b')        # 繪2次業績點
plt.plot(3, 19, '-x', color='b')        # 繪3次業績點

h = (-1 * root[b] / (2 * root[a]))
k = (4 * root[a] * root[c] - (root[b] ** 2)) / (4 * root[a])
plt.plot(h, k, '-o', color='b')         # 繪最大值座標
h = round(float(h), 1)
k = round(float(k), 1)
plt.text(h-0.25, k-1.5, '('+str(h)+','+str(k)+')')

plt.xlabel("Times")
plt.ylabel("Performance")
plt.grid()                              # 加格線

plt.show()

print('------------------------------------------------------------')	#60個


