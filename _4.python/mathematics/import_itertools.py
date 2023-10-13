import sys
import itertools

print('------------------------------------------------------------')	#60個

n = {1, 2, 3, 4}
r = 3
A = set(itertools.permutations(n, 3))
print('元素數量 = {}'.format(len(A)))
for a in A:
    print(a)

print('------------------------------------------------------------')	#60個

#animals = ['鼠', '牛', '虎', '兔', '龍', '蛇']

n = {'鼠', '牛', '虎', '兔', '龍'}
r = 2
A = set(itertools.permutations(n, 2))
print('基因配對組合數量 = {}'.format(len(A)))
for a in A:
    print(a)

print('------------------------------------------------------------')	#60個

n = {'鼠', '牛', '虎', '兔', '龍'}
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

print('鼠牛虎兔 四選二')
strings = '鼠牛虎兔'
for text1, text2 in itertools.combinations(strings, 2):
    print(text1, text2)


print(list(itertools.combinations('鼠牛虎兔', 2)))
print(list(itertools.combinations_with_replacement('鼠牛虎兔', 2)))
print(list(itertools.permutations('鼠牛虎兔', 2)))


print('------------------------------------------------------------')	#60個

#TBD
ccc = itertools.product('鼠牛虎兔', repeat=2)
print(ccc)

print('------------------------------------------------------------')	#60個

from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

print('排列組合')

#animals = ['鼠', '牛', '虎', '兔', '龍', '蛇']
animals = ['鼠', '牛', '虎', '兔']

# 全排列
for p in permutations(animals):
    print(p)

# 指定长度
for p in permutations(animals, 2):
    print(p)

# 组合
for c in combinations(animals, 3):
    print(c)

# 可重复组合
for c in combinations_with_replacement(animals, 3):
    print(c)

print('------------------------------------------------------------')	#60個

from itertools import islice as _islice, count as _count

# Helper to generate new thread names
_counter = _count().__next__
_counter() # Consume 0 so first non-main thread has id 1.
def _newname(template="Thread-%d"):
    return template % _counter()

print(_newname())
print(_newname())
print(_newname())
print(_newname())
print(_newname())
print(_newname())

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
