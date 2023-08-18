# ch8_1.py
import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np
                                
x = Symbol('x')                         # 定義公式中使用的變數
y = Symbol('y')                         # 定義公式中使用的變數
eq1 = 8 - 0.6 * x - y                   # 方程式 1
eq2 = 17.5 - 2.5 * x - y                # 方程式 2
ans = solve((eq1, eq2))
print('x = {}'.format(int(ans[x])))
print('y = {}'.format(int(ans[y])))

z = 50 * int(ans[x]) + 50 * int(ans[y])
print('最大獲利 = {} 萬'.format(z))








