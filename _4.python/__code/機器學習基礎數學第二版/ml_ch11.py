import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch11\ch11_1.py

# ch11_1.py
empty_dict = {}                      # 這是建立空字典
print("列印類別 = ", type(empty_dict))
empty_set = set()                    # 這是建立空集合
print("列印類別 = ", type(empty_set))

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch11\ch11_2.py

# ch11_2.py
fruits1 = ['apple', 'orange', 'apple', 'banana', 'orange']
x = set(fruits1)                # 將串列轉成集合
fruits2 = list(x)               # 將集合轉成串列
print("原先串列資料fruits1 = ", fruits1)
print("新的串列資料fruits2 = ", fruits2)







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch11\ch11_3.py

# ch11_3.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
both1 = math & physics
print("同時參加數學與物理夏令營的成員 ",both1)
both2 = math.intersection(physics)
print("同時參加數學與物理夏令營的成員 ",both2)



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch11\ch11_4.py

# ch11_4.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
allmember1 = math | physics
print("參加數學或物理夏令營的成員 ",allmember1)
allmember2 = math.union(physics)
print("參加數學或物理夏令營的成員 ",allmember2)



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch11\ch11_5.py

# ch11_5.py 
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

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch11\ch11_6.py

# ch11_6.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_sydi_physics1 = math ^ physics
print("沒有同時參加數學和物理夏令營的成員 ",math_sydi_physics1)
math_sydi_physics2 = math.symmetric_difference(physics)
print("沒有同時參加數學和物理夏令營的成員 ",math_sydi_physics2)





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch11\ch11_7.py

# ch11_7.py
from sympy import *
A = FiniteSet('a', 'b')
B = FiniteSet('c', 'd')
AB = A * B
for ab in AB:
    print(type(ab), ab)









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch11\ch11_8.py

# ch11_8.py
from sympy import *
A = FiniteSet('a', 'b', 'c', 'd', 'e')
B = FiniteSet('f', 'g')
AB = A * B
print('The length of Cartesian product', len(AB))
for ab in AB:
    print(ab)









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch11\ch11_9.py

# ch11_9.py
from sympy import *
A = FiniteSet('a', 'b')
AAA = A**3
print('The length of Cartesian product', len(AAA))
for a in AAA:
    print(a)









print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

