# ch12_2.py
import itertools
n = {'a', 'b', 'c', 'd', 'e'}
r = 2
A = set(itertools.permutations(n, 2))
print('基因配對組合數量 = {}'.format(len(A)))
for a in A:
    print(a)










