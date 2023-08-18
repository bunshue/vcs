# ch11_8.py
from sympy import *
A = FiniteSet('a', 'b', 'c', 'd', 'e')
B = FiniteSet('f', 'g')
AB = A * B
print('The length of Cartesian product', len(AB))
for ab in AB:
    print(ab)








