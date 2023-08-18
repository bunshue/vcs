# ch6_5.py
import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np
                                
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






