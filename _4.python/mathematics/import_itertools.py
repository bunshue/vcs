import sys
import itertools

print('------------------------------------------------------------')	#60個

'''
n = {1, 2, 3, 4}
r = 3
A = set(itertools.permutations(n, 3))
print('元素數量 = {}'.format(len(A)))
for a in A:
    print(a)

print('------------------------------------------------------------')	#60個

n = {'a', 'b', 'c', 'd', 'e'}
r = 2
A = set(itertools.permutations(n, 2))
print('基因配對組合數量 = {}'.format(len(A)))
for a in A:
    print(a)

print('------------------------------------------------------------')	#60個

n = {'A', 'B', 'C', 'D', 'E'}
r = 5
A = set(itertools.permutations(n, 5))
print('業務員路徑數 = {}'.format(len(A)))
for a in A:
    print(a)

print('------------------------------------------------------------')	#60個

n = {1, 2, 3, 4, 5}
A = set(itertools.product(n, n, n))
print('排列組合 = {}'.format(len(A)))
for a in A:
    print(a)

print('------------------------------------------------------------')	#60個

n = {1, 2, 3, 4, 5}
A = set(itertools.combinations(n, 3))
print('組合 = {}'.format(len(A)))
for a in A:
    print(a)

print('------------------------------------------------------------')	#60個

n = {1, 2, 3, 4, 5, 6}
A = set(itertools.combinations(n, 2))
print('組合 = {}'.format(len(A)))
for a in A:
    print(a)

print('------------------------------------------------------------')	#60個
'''

color_next = itertools.cycle(['r','g','b','y','m','c','k']) # 定義顏色

for _ in range(10):
    print('下一個顏色 :', next(color_next))

cy = itertools.cycle('abc')
for _ in range(10):
    print(next(cy))

print('------------------------------------------------------------')	#60個

rp = itertools.repeat('b') # forever. b
for _ in range(10):
    print(next(rp))

for x, y in itertools.product(range(3), range(3)):
    print(x, y)


for x, y in itertools.product(list('ABC'), list('123')):
    print(x, y)

print('------------------------------------------------------------')	#60個

print('ABCD 四選二')
strings = 'ABCD'
for text1, text2 in itertools.combinations(strings, 2):
    print(text1, text2)


print(list(itertools.combinations('ABCD', 2)))
print(list(itertools.combinations_with_replacement('ABCD', 2)))
print(list(itertools.permutations('ABCD', 2)))


print('------------------------------------------------------------')	#60個

ccc = itertools.product('abc', repeat=2)
print(ccc)



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
