import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch12\ch12_1.py

# ch12_1.py
import itertools
n = {1, 2, 3, 4}
r = 3
A = set(itertools.permutations(n, 3))
print('元素數量 = {}'.format(len(A)))
for a in A:
    print(a)











print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch12\ch12_2.py

# ch12_2.py
import itertools
n = {'a', 'b', 'c', 'd', 'e'}
r = 2
A = set(itertools.permutations(n, 2))
print('基因配對組合數量 = {}'.format(len(A)))
for a in A:
    print(a)











print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch12\ch12_3.py

# ch12_3.py
import itertools
n = {'A', 'B', 'C', 'D', 'E'}
r = 5
A = set(itertools.permutations(n, 5))
print('業務員路徑數 = {}'.format(len(A)))
for a in A:
    print(a)











print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch12\ch12_4.py

# ch12_4.py
import math

N = 30
times = 10000000000000              # 電腦每秒可處理數列數目
day_secs = 60 * 60 * 24             # 一天秒數
year_secs = 365 * day_secs          # 一年秒數
combinations = math.factorial(N)    # 組合方式
years = combinations / (times * year_secs)
print("需要 %d 年才可以獲得結果" % years)






    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch12\ch12_5.py

# ch12_5.py
import itertools
n = {1, 2, 3, 4, 5}
A = set(itertools.product(n, n, n))
print('排列組合 = {}'.format(len(A)))
for a in A:
    print(a)











print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch12\ch12_6.py

# ch12_6.py
import itertools
n = {1, 2, 3, 4, 5}
A = set(itertools.combinations(n, 3))
print('組合 = {}'.format(len(A)))
for a in A:
    print(a)











print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch12\ch12_7.py

# ch12_7.py
import itertools
n = {1, 2, 3, 4, 5, 6}
A = set(itertools.combinations(n, 2))
print('組合 = {}'.format(len(A)))
for a in A:
    print(a)











print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

