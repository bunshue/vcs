# ch12_5.py
import itertools
n = {1, 2, 3, 4, 5}
A = set(itertools.product(n, n, n))
print('排列組合 = {}'.format(len(A)))
for a in A:
    print(a)










