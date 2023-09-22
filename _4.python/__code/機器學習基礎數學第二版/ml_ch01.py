import sys

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體

print('------------------------------------------------------------')	#60個

from sympy import Symbol, solve
                                
a = Symbol('a')                 # 定義公式中使用的變數
b = Symbol('b')                 # 定義公式中使用的變數
eq1 = a + b - 1                 # 方程式 1
eq2 = 5 * a + b - 2             # 方程式 2
ans = solve((eq1, eq2))
print(type(ans))
print(ans)
print('a = {}'.format(ans[a]))
print('b = {}'.format(ans[b]))

print('------------------------------------------------------------')	#60個

from sympy import Symbol, solve
                                
a = Symbol('a')                 # 定義公式中使用的變數
b = Symbol('b')                 # 定義公式中使用的變數
eq1 = a + b - 1                 # 方程式 1
eq2 = 5 * a + b - 2             # 方程式 2
ans = solve((eq1, eq2))
print('a = {}'.format(ans[a]))
print('b = {}'.format(ans[b]))

pt_x1 = 600                             
pt_y1 = ans[a] * pt_x1 + ans[b]         # 計算x=600時的y值
pt_x2 = 1000
pt_y2 = ans[a] * pt_x2 + ans[b]         # 計算x=1000時的y值

x = np.linspace(0, 2500, 250)
y = ans[a] * x + ans[b]
plt.plot(x, y)                          # 繪函數直線
plt.plot(pt_x1, pt_y1, '-o')            # 繪點 pt1
plt.text(pt_x1+60, pt_y1-10, 'pt1')      # 輸出文字pt1
plt.plot(pt_x2, pt_y2, '-o')            # 繪點 pt2
plt.text(pt_x2+60, pt_y2-10, 'pt2')      # 輸出文字pt2
plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()                              # 加格線

plt.show()

print('------------------------------------------------------------')	#60個

a = 0.03
b = -18
x = np.linspace(0, 2500, 250)
y = a * x + b
pt_x = 1500
pt_y = a * pt_x + b
print('f(1500) = {}'.format(pt_y))
plt.plot(x, y)                          # 繪函數直線
plt.plot(pt_x, pt_y, '-o')              # 繪點 f(1500)
plt.text(pt_x-150, pt_y+3, 'f(1500)')   # 輸出文字f(1500)
plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()                              # 加格線

plt.show()

print('------------------------------------------------------------')	#60個

a = 0.03
b = -18
x = np.linspace(0, 2500, 250)
y = a * x + b
pt_y = 48
pt_x = (pt_y + 18) / 0.03 
print('獲利48萬需有 {} 來客數'.format(int(pt_x)))
plt.plot(x, y)                                      # 繪函數直線
plt.plot(pt_x, pt_y, '-o')                          # 繪點
plt.text(pt_x-150, pt_y+3, '('+str(int(pt_x))+','+str(pt_y)+')')   
plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()                                          # 加格線

plt.show()

print('------------------------------------------------------------')	#60個

from sympy import Symbol, solve
                                
x = Symbol('x')                         # 定義公式中使用的變數
y = Symbol('y')                         # 定義公式中使用的變數
eq1 = x + y - 35                        # 方程式 1
eq2 = 2 * x + 4 * y - 100               # 方程式 2
ans = solve((eq1, eq2))
print('雞 = {}'.format(ans[x]))
print('兔 = {}'.format(ans[y]))

line1_x = np.linspace(0, 100, 100)
line1_y = [35 - y for y in line1_x]
line2_x = np.linspace(0, 100, 100)
line2_y = [25 - 0.5 * y for y in line2_x]

plt.plot(line1_x, line1_y)              # 繪函數直線公式 1
plt.plot(line2_x, line2_y)              # 繪函數直線公式 2

plt.plot(ans[x], ans[y], '-o')          # 繪交叉點
plt.text(ans[x]-5, ans[y]+5, '('+str(ans[x])+','+str(ans[y])+')')
plt.xlabel("Chicken")
plt.ylabel("Rabbit")
plt.grid()                              # 加格線

plt.show()

print('------------------------------------------------------------')	#60個

from sympy import Symbol, solve
                                
x = Symbol('x')                         # 定義公式中使用的變數
y = Symbol('y')                         # 定義公式中使用的變數
eq1 = x + y - 100                       # 方程式 1
eq2 = 2 * x + 4 * y - 350               # 方程式 2
ans = solve((eq1, eq2))
print('菜鳥業務員須外出天數 = {}'.format(ans[x]))
print('資深業務員須外出天數 = {}'.format(ans[y]))

line1_x = np.linspace(0, 100, 100)
line1_y = [100 - y for y in line1_x]
line2_x = np.linspace(0, 100, 100)
line2_y = [(350 - 2 * y) / 4 for y in line2_x]

plt.plot(line1_x, line1_y)              # 繪函數直線公式 1
plt.plot(line2_x, line2_y)              # 繪函數直線公式 2

plt.plot(ans[x], ans[y], '-o')          # 繪交叉點
plt.text(ans[x]-5, ans[y]+5, '('+str(ans[x])+','+str(ans[y])+')')
plt.xlabel("Junior Salesman")
plt.ylabel("Senior Salesman")
plt.grid()                              # 加格線

plt.show()

print('------------------------------------------------------------')	#60個

from sympy import Symbol, solve

x = Symbol('x')                         # 定義公式中使用的變數
y = Symbol('y')                         # 定義公式中使用的變數
eq1 = x - y                             # 方程式 1
eq2 = -x -y + 2                         # 方程式 2
ans = solve((eq1, eq2))
print('x = {}'.format(ans[x]))
print('y = {}'.format(ans[y]))

line1_x = np.linspace(-5, 5, 10)
line1_y = [y for y in line1_x]
line2_x = np.linspace(-5, 5, 10)
line2_y = [-y + 2 for y in line2_x]

plt.plot(line1_x, line1_y)              # 繪函數直線公式 1
plt.plot(line2_x, line2_y)              # 繪函數直線公式 2

plt.plot(ans[x], ans[y], '-o')          # 繪交叉點
plt.text(ans[x]-0.5, ans[y]+0.3, '('+str(ans[x])+','+str(ans[y])+')')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()                              # 加格線
plt.axis('equal')                       # 讓x, y軸距長度一致

plt.show()

print('------------------------------------------------------------')	#60個

from sympy import Symbol, solve

x = Symbol('x')                         # 定義公式中使用的變數
y = Symbol('y')                         # 定義公式中使用的變數
eq1 = 0.5 * x - y - 0.5                 # 方程式 1
eq2 = -2 * x - y + 7                    # 方程式 2
ans = solve((eq1, eq2))
print('x = {}'.format(ans[x]))
print('y = {}'.format(ans[y]))


line1_x = np.linspace(-5, 5, 10)
line1_y = [(0.5 * y - 0.5) for y in line1_x]
line2_x = np.linspace(-5, 5, 10)
line2_y = [(-2 * y + 7) for y in line2_x]

plt.plot(line1_x, line1_y)              # 繪函數直線公式 1
plt.plot(line2_x, line2_y)              # 繪函數直線公式 2

plt.plot(ans[x], ans[y], '-o')          # 繪交叉點
plt.text(ans[x]-0.7, ans[y]+0.5, '('+str(int(ans[x]))+','+str(int(ans[y]))+')')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()                              # 加格線
plt.axis('equal')                       # 讓x, y軸距長度一致

plt.show()

print('------------------------------------------------------------')	#60個

from sympy import Symbol, solve
                                
x = Symbol('x')                         # 定義公式中使用的變數
y = Symbol('y')                         # 定義公式中使用的變數
eq1 = 8 - 0.6 * x - y                   # 方程式 1
eq2 = 17.5 - 2.5 * x - y                # 方程式 2
ans = solve((eq1, eq2))
print('x = {}'.format(int(ans[x])))
print('y = {}'.format(int(ans[y])))

z = 50 * int(ans[x]) + 50 * int(ans[y])
print('最大獲利 = {} 萬'.format(z))

print('------------------------------------------------------------')	#60個

plt.plot([0, 0], [20, 0])              # 繪函數直線公式 1
plt.plot([0, 0], [0, 20])              # 繪函數直線公式 2
                                
line3_x = np.linspace(0, 20, 20)
line3_y = [(8 - 0.6 * y) for y in line3_x]

line4_x = np.linspace(0, 20, 20)
line4_y = [(17.5 - 2.5 * y) for y in line4_x]

lineobj_x = np.linspace(0, 20, 20)
lineobj_y = [10 - y for y in lineobj_x]

plt.axis([0, 20, 0, 20])

plt.plot(line3_x, line3_y)              # 繪函數直線公式 3
plt.plot(line4_x, line4_y)              # 繪函數直線公式 4
plt.plot(lineobj_x, lineobj_y)          # 繪目標函數直線公式

plt.plot(5, 5, '-o')                    # 繪交叉點
plt.text(4.5, 5.5, '(5, 5)')            # 輸出(5, 5)
plt.xlabel("Research")
plt.ylabel("UI")
plt.grid()                              # 加格線

plt.show()

print('------------------------------------------------------------')	#60個

