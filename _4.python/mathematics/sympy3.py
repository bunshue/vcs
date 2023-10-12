import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

import sympy

A = sympy.FiniteSet('a', 'b')
B = sympy.FiniteSet('c', 'd')
AB = A * B
for ab in AB:
    print(type(ab), ab)

print('------------------------------------------------------------')	#60個

A = sympy.FiniteSet('a', 'b', 'c', 'd', 'e')
B = sympy.FiniteSet('f', 'g')
AB = A * B
print('The length of Cartesian product', len(AB))
for ab in AB:
    print(ab)

print('------------------------------------------------------------')	#60個

A = sympy.FiniteSet('a', 'b')
AAA = A ** 3
print('The length of Cartesian product', len(AAA))
for a in AAA:
    print(a)

print('------------------------------------------------------------')	#60個


import sympy

a = sympy.Symbol('a')
b = sympy.Symbol('b')
eq1 = -a + b -2
eq2 = a + b - 4
ans = sympy.solve((eq1, eq2))
print('a = {}'.format(ans[a]))
print('b = {}'.format(ans[b]))

