# ch9_14.py
from sympy import *

x = Symbol('x')
eq = -3.5*x**2 + 18.5*x - 20
ans = solve(eq)
x1 = round(ans[0], 1)
x2 = round(ans[1], 1)
print('x1 = {}'.format(x1))
print('x2 = {}'.format(x2))












