# ch6_7.py
import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np

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






