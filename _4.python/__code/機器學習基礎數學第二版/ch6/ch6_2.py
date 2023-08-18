# ch6_2.py
import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np
                                
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






