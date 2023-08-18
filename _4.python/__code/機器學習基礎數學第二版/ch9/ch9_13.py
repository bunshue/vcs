# ch9_13.py
import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np

a = Symbol('a')                         # 定義公式中使用的變數
b = Symbol('b')                         # 定義公式中使用的變數
c = Symbol('c')                         # 定義公式中使用的變數
eq1 = a + b + c - 10                    # 第1次公式
eq2 = 4*a + 2*b + c - 18                # 第2次公式
eq3 = 9*a + 3*b + c - 19                # 第3次公式
ans = solve((eq1, eq2, eq3))
print('a = {}'.format(ans[a]))
print('b = {}'.format(ans[b]))
print('c = {}'.format(ans[c]))

x = np.linspace(0, 4, 50)
y = [(ans[a]*y**2 + ans[b]*y + ans[c]) for y in x]
plt.plot(x, y)                          # 繪二次函數

plt.plot(1, 10, '-x', color='b')        # 繪1次業績點
plt.plot(2, 18, '-x', color='b')        # 繪2次業績點
plt.plot(3, 19, '-x', color='b')        # 繪3次業績點

h = (-1 * ans[b] / (2 * ans[a]))
k = (4 * ans[a] * ans[c] - (ans[b] ** 2)) / (4 * ans[a])
plt.plot(h, k, '-o', color='b')         # 繪最大值座標
h = round(float(h), 1)
k = round(float(k), 1)
plt.text(h-0.25, k-1.5, '('+str(h)+','+str(k)+')')

plt.xlabel("Times")
plt.ylabel("Performance")
plt.grid()                              # 加格線
plt.show()









