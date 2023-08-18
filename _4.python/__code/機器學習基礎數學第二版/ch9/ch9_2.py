# ch9_2.py
from sympy import *

x = Symbol('x')
f = Symbol('f')
f = x**2 - 2*x - 8
root = solve(f)
print(root)








