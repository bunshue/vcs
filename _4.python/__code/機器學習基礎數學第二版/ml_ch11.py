import sys

import numpy as np
import matplotlib.pyplot as plt

print('Container 測試')

print('------------------------------------------------------------')	#60個

empty_dict = {}                      # 這是建立空字典
empty_set = set()                    # 這是建立空集合
fruits1 = ['apple', 'orange', 'apple', 'banana', 'orange']
x = set(fruits1)                # 將串列轉成集合
fruits2 = list(x)               # 將集合轉成串列

print('------------------------------------------------------------')	#60個
#set
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
both1 = math & physics
print("同時參加數學與物理夏令營的成員 ",both1)
both2 = math.intersection(physics)
print("同時參加數學與物理夏令營的成員 ",both2)

print('------------------------------------------------------------')	#60個
#set
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
allmember1 = math | physics
print("參加數學或物理夏令營的成員 ",allmember1)
allmember2 = math.union(physics)
print("參加數學或物理夏令營的成員 ",allmember2)

print('------------------------------------------------------------')	#60個
#set
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_only1 = math - physics
print("參加數學夏令營同時沒有參加物理夏令營的成員 ",math_only1)
math_only2 = math.difference(physics)
print("參加數學夏令營同時沒有參加物理夏令營的成員 ",math_only2)
physics_only1 = physics - math
print("參加物理夏令營同時沒有參加數學夏令營的成員 ",physics_only1)
physics_only2 = physics.difference(math)
print("參加物理夏令營同時沒有參加數學夏令營的成員 ",physics_only2)

print('------------------------------------------------------------')	#60個
#set
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_sydi_physics1 = math ^ physics
print("沒有同時參加數學和物理夏令營的成員 ",math_sydi_physics1)
math_sydi_physics2 = math.symmetric_difference(physics)
print("沒有同時參加數學和物理夏令營的成員 ",math_sydi_physics2)

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

