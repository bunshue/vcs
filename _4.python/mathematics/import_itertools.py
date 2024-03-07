"""
# itertools 迭代工具

itertools.permutations 排列

itertools.combinations 組合
    combinations() 組合
    combinations_with_replacement() 同元素可重複的組合

itertools.product() 笛卡兒積


"""

import sys
import itertools

print('permutations 排列 ST------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

#全排列
cc = itertools.permutations("鼠牛虎兔")
dd = list(cc)
print(dd)

print('------------------------------------------------------------')	#60個

#部分排列
print('P(4, 2)')
cc = itertools.permutations('鼠牛虎兔', 2)
dd = list(cc)
print(dd)

print('------------------------------------------------------------')	#60個

print('P(4, 2)')

animals = {'鼠', '牛', '虎', '兔'}
cc = itertools.permutations(animals, 2)
A = set(cc)
print('組合數量 = {}'.format(len(A)))
for a in A:
    print(a)

print('------------------------------------------------------------')	#60個

animals = ['鼠', '牛', '虎', '兔']
cc = itertools.permutations(animals)
n = 0
for i in cc:
    n += 1
    print(i)
print("總共有 %d 拜訪方式" % n)

print('------------------------------------------------------------')	#60個

# 全排列
animals = ['鼠', '牛', '虎', '兔']
cc = itertools.permutations(animals)
for p in cc:
    print(p)

# 指定长度
animals = ['鼠', '牛', '虎', '兔']
cc = itertools.permutations(animals, 2)
for p in cc:
    print(p)

animals = ['鼠', '牛', '虎', '兔']
cc = itertools.permutations(animals, 2)
dd = list(cc)
print(dd)

print('permutations 排列 SP------------------------------------------------------------')	#60個


print('combinations 組合 ST------------------------------------------------------------')	#60個

cc = itertools.combinations("鼠牛虎兔", 3)
print(cc)
dd = list(cc)
print(dd)

sys.exit()
print('------------------------------------------------------------')	#60個

n = {1, 2, 3, 4, 5}
cc = itertools.combinations(n, 3)
A = set(cc)
print('組合 = {}'.format(len(A)))
for a in A:
    print(a)

print('------------------------------------------------------------')	#60個

n = {1, 2, 3, 4, 5, 6}
cc = itertools.combinations(n, 2)
A = set(cc)
print('組合 = {}'.format(len(A)))
for a in A:
    print(a)

print('------------------------------------------------------------')	#60個

print('鼠牛虎兔 四選二')
strings = '鼠牛虎兔'
for text1, text2 in itertools.combinations(strings, 2):
    print(text1, text2)


print(list(itertools.combinations('鼠牛虎兔', 2)))

print(list(itertools.combinations_with_replacement('鼠牛虎兔', 2)))

print('------------------------------------------------------------')	#60個

animals = ['鼠', '牛', '虎', '兔']
# 组合
for c in itertools.combinations(animals, 3):
    print(c)

print('------------------------------------------------------------')	#60個

animals = ['鼠', '牛', '虎', '兔']
# 可重复组合
for c in itertools.combinations_with_replacement(animals, 3):
    print(c)

animals = ['鼠', '牛', '虎', '兔']
print(list(itertools.combinations(animals, 2)))
print(list(itertools.combinations(animals, 3)))
print(list(itertools.combinations_with_replacement(animals, 2)))
print(list(itertools.combinations_with_replacement(animals, 3)))


print('combinations 組合 SP------------------------------------------------------------')	#60個


print('product 笛卡兒積 ST------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

n = {1, 2, 3, 4}
A = set(itertools.product(n, n, n))
print('排列組合 = {}'.format(len(A)))
for a in A:
    print(a)

print('------------------------------------------------------------')	#60個


data1 = ['A', 'B', 'C']
data2 = [1, 2, 3]

print(list(itertools.product(data1, data2)))

print(list(itertools.product(data1, data2, repeat=2)))

print(list(itertools.product(data1, repeat=2)))

print('------------------------------------------------------------')	#60個

rp = itertools.repeat('b') # forever. b
for _ in range(10):
    print(next(rp))

for x, y in itertools.product(range(3), range(3)):
    print(x, y)


for x, y in itertools.product(list('ABC'), list('123')):
    print(x, y)

print('------------------------------------------------------------')	#60個

#TBD
ccc = itertools.product('鼠牛虎兔', repeat=2)
print(ccc)

print('------------------------------------------------------------')	#60個

#笛卡爾積

cc = itertools.product("鼠牛虎兔", "123")
print(type(cc))
print(cc)



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('product 笛卡兒積 SP------------------------------------------------------------')	#60個



print('其他 ST------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
#1
color_next = itertools.cycle(['r','g','b','y','m','c','k']) # 定義顏色

for _ in range(10):
    print('下一個顏色 :', next(color_next))

cy = itertools.cycle('abc')
for _ in range(10):
    print(next(cy))


print('itertools 模組: cycle() 無限循環')
"""
for item in itertools.cycle(range(3)):
    print(item)
"""

print('------------------------------------------------------------')	#60個
#2

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

print('------------------------------------------------------------')	#60個

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

# itertools 模組: tee() 同單一來源建立多個走訪器

data = [1, 2, 3, 4, 5]

generators = itertools.tee(data, 3)

for g in generators:
    print(list(g))
print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

# Helper to generate new thread names
_counter = itertools.count().__next__
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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


