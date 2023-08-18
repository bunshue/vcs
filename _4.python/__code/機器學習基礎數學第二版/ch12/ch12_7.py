# ch12_7.py
import itertools
n = {1, 2, 3, 4, 5, 6}
A = set(itertools.combinations(n, 2))
print('組合 = {}'.format(len(A)))
for a in A:
    print(a)










