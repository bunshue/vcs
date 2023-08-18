# ch6_1.py
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








