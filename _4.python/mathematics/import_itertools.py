import sys
import itertools
'''
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

# itertools 模組:
# product() 笛卡兒積
# permutations() 排列
# combinations() 組合
# combinations_with_replacement() 同元素可重複的組合

data1 = ['A', 'B', 'C']
data2 = [1, 2, 3]

print(list(itertools.product(data1, data2)))

print(list(itertools.product(data1, data2, repeat=2)))

print(list(itertools.product(data1, repeat=2)))

print(list(itertools.permutations(data1, 2)))

print(list(itertools.permutations(data1, 3)))

print(list(itertools.combinations(data1, 2)))

print(list(itertools.combinations(data1, 3)))

print(list(itertools.combinations_with_replacement(data1, 2)))

print(list(itertools.combinations_with_replacement(data1, 3)))

print('------------------------------------------------------------')	#60個

# itertools 模組: tee() 同單一來源建立多個走訪器

data = [1, 2, 3, 4, 5]

generators = itertools.tee(data, 3)

for g in generators:
    print(list(g))
print('------------------------------------------------------------')	#60個

# itertools 模組: compress() 過濾元素

data = 'ABCDEFG'
selector = [1, 0, 1, 1, 0, 1, 0]

print(list(itertools.compress(data, selector)))

print('------------------------------------------------------------')	#60個

print('itertools 模組: count() 無限計數器')
"""
for item in itertools.count(3, 2):
    print(item)
"""

print('itertools 模組: cycle() 無限循環')
"""
for item in itertools.cycle(range(3)):
    print(item)
"""

print('itertools 模組: repeat() 無限重複')

for item in itertools.repeat('Hello!', 5):
    print(item)

    
print('itertools 模組: chain() 串聯可走訪物件')

print(list(itertools.chain(
        ['A', 'B', 'C'],
        [1, 2, 3],
        [True, False]
    )))


matrix = [
        ['A', 'B', 'C'],
        [1, 2, 3],
        [True, False]
    ]

print(list(itertools.chain.from_iterable(matrix)))


print('itertools 模組: zip_longest() - 完整走訪版 zip')

x = ['A', 'B', 'C', 'D', 'E']
y = [1, 2, 3]

print(list(zip(x, y)))

print(list(itertools.zip_longest(x, y)))

print(list(itertools.zip_longest(x, y, fillvalue=0)))

print('------------------------------------------------------------')	#60個

print('itertools 模組: islice() 切片')

n = [0, 1, 2, 3, 4]

print(list(itertools.islice(n, 3)))

print(list(itertools.islice(n, 1, 3)))

print(list(itertools.islice(n, 0, 5, 2)))

print('------------------------------------------------------------')	#60個

print('itertools 模組: accumulate() 累加')

n = [0, 1, 2, 3, 4]
print(list(itertools.accumulate(n)))

c = ['A', 'B', 'C', 'D', 'E']
print(list(itertools.accumulate(c)))


data = range(1, 11)
multiply = lambda x, y: x * y

print(list(itertools.accumulate(data, multiply)))

print('------------------------------------------------------------')	#60個

print('itertools 模組: starmap() 解包外層容器')

n = [(1, 2), (2, 3), (3, 5), (5, 7), (7, 11)]

print(list(itertools.starmap(lambda x, y: x * y, n)))

print(list(map(lambda t: t[0] * t[1], n)))

print('------------------------------------------------------------')	#60個

print('itertools 模組: groupby() 給連續資料分組')

data = ['a', 'a', 'a', 'b', 'b', 'b', 'a', 'a', 'c', 'c', 'd']

for key, item in itertools.groupby(data):
    print(key, list(item))

print('')
data.sort()

for key, item in itertools.groupby(data):
    print(key, list(item))


print('')
data = ['Python', 'Java', 'C#', 'Perl', 'Basic', 'Go', 'COBOL', 'Ruby']
data.sort(key=len)

for key, item in itertools.groupby(data, len):
    print(key, list(item))


print('')
first_letter = lambda i: i[0]
data.sort(key=first_letter)

for key, item in itertools.groupby(data, first_letter):
    print(key, list(item))


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

# 迭代工具 - 排列 / 組合 / 笛卡爾積

cc = itertools.permutations("ABCD")
print(type(cc))
print(cc)

cc = itertools.combinations("ABCDE", 3)
print(type(cc))
print(cc)

cc = itertools.product("ABCD", "123")
print(type(cc))
print(cc)
'''
print('------------------------------------------------------------')	#60個

x = ["1", "2", "3"]
perm = itertools.permutations(x)
for i in perm:
    print(i)


print('------------------------------------------------------------')	#60個

import itertools

x = ["北京", "天津", "上海", "廣州", "武漢"]
perm = itertools.permutations(x)
n = 0
for i in perm:
    n += 1
    print(i)
print("總共有 %d 拜訪方式" % n)




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

