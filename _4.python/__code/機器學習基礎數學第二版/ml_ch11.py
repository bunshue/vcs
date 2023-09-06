import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

from sympy import *
A = FiniteSet('a', 'b')
B = FiniteSet('c', 'd')
AB = A * B
for ab in AB:
    print(type(ab), ab)

print('------------------------------------------------------------')	#60個

from sympy import *
A = FiniteSet('a', 'b', 'c', 'd', 'e')
B = FiniteSet('f', 'g')
AB = A * B
print('The length of Cartesian product', len(AB))
for ab in AB:
    print(ab)

print('------------------------------------------------------------')	#60個

from sympy import *
A = FiniteSet('a', 'b')
AAA = A**3
print('The length of Cartesian product', len(AAA))
for a in AAA:
    print(a)

print('------------------------------------------------------------')	#60個

