import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

#3-4-1 datetime 物件
import datetime as dt

x = dt.datetime(2020, 10, 22)
print(x)

x = dt.datetime(year=2020, month=10, day=22)
print(x)

y = dt.datetime(2020, 10, 22, 10, 30, 45) #設定日期與時間
print(y)

print('------------------------------------------------------------')	#60個

#3-4-2 timedelta 物件

x = dt.timedelta(hours=1, minutes=30) #1 小時又 30 分

print(x)
y = dt.timedelta(days=1, seconds=30) #1 天又 30 秒
print(y)

#3-4-3 用 timedelta 來增減 datetime 或 timedelta 的時間

import datetime as dt

x = dt.datetime(2020, 10, 22, 10, 30, 45) #原始時間

y = dt.timedelta(days=1, hours=2, minutes=5)

print(x)

print(x + y) #用 timedelta 來增減 datetime 的時間

print(x - y)

print(x + y * 2)


print('------------------------------------------------------------')	#60個

#3-4-4 將 datetime 時間以格式化方式輸出

import datetime as dt

x = dt.datetime(2020, 10, 22, 10, 30, 45)

s1 = x.strftime('%Y/%m/%d %H-%M-%S')

print(s1)

s2 = x.strftime('%Y 年 %m 月 %d 日 %H : %M : %S')

print(s2)


print('------------------------------------------------------------')	#60個

#3-4-5 用字串來建立 datetime 物件

import datetime as dt

s = '2020/10/22 10-30-45' #含有特定格式之日期時間字串

x = dt.datetime.strptime(s, '%Y/%m/%d %H-%M-%S')


print(x)

print(type(x))


print('------------------------------------------------------------')	#60個

#4-1-1 lambda 函式簡介

power = lambda x: x ** 2

print(power(10))


add = lambda a, b: a + b

print(add(5, 3))

print('------------------------------------------------------------')	#60個

#4-1-2 在 lambda 內使用一行 if 條件判斷式

absolute = lambda x: x if x >= 0 else -x

func = lambda x: (x ** 2 - 40 * x + 350) if 10 <= x < 30 else 50

#4-2-1 str.split()：分割字串為 list 元素

sentence = 'This is a test sentence'

print(sentence.split (' '))

['This', 'is', 'a', 'test', 'sentence']

#4-2-2 用字串正規化分割字串為 list

import re

sentence = 'This,is a,test.sentence'
time_data = '2020/05/20_12:30:45'

print(re.split('[,. ]', sentence)) #用逗點、句點和空格來分割字串

print(re.split('[/_:]', time_data))

print('------------------------------------------------------------')	#60個

a = [1, -2, 3, -4, 5]

new = []

for x in a:
    new.append(abs(x)) #走訪 a 的元素, 取絕對值後放入 new

print(new)

str_list = ['This', 'is', 'a', 'test', 'sentence']

print(list(map(str.upper, str_list)))

print('------------------------------------------------------------')	#60個

#4-2-4 用 flter() 篩選容器元素

str_list = ['This', 'is', 'a', 'test', 'sentence']

print(list(filter(lambda x: len(x) >= 3, str_list)))

['This', 'test', 'sentence']

#4-2-5 再探 sorted()：自訂目標容器的排序方式

str_list = ['This', 'is', 'a', 'test', 'sentence']

print(sorted(str_list, key=len, reverse=True))

nest_list = [
  [0, 9],
  [1, 8],
  [2, 7],
  [3, 6],
  [4, 5]
]

print(sorted(nest_list))

print(sorted(nest_list, key=lambda x: x[1]))

print(sorted(nest_list, key=lambda x: x[1], reverse=True))

print('------------------------------------------------------------')	#60個

#4-3-1 介紹 list 生成式

a = [1, -2, 3, -4, 5]

print([abs(x) for x in a])

print('------------------------------------------------------------')	#60個

a = [1, -2, 3, -4, 5]

print([x ** 2 for x in a])

str_list = ['This', 'is', 'a', 'test', 'sentence']

print([s.upper() for s in str_list])

#4-3-2 在 list 生成式使用 if 過濾元素

a = [1, -2, 3, -4, 5]

print([x for x in a if x > 0])

str_list = ['This', 'is', 'a', 'test', 'sentence']

print([x for x in str_list if len(x) >= 3])

print('------------------------------------------------------------')	#60個


#4-3-3 在 list 生成式用 zip() 同時走訪多個容器

a = [1, -2, 3, -4, 5]
b = [9, 8, -7, -6, -5]

print([[x, y] for x, y in zip(a, b)])
print([x + y for x, y in zip(a, b)])

print('------------------------------------------------------------')	#60個

a = [1, -2, 3, -4, 5]

b = [9, 8, -7, -6, -5]

print([x + y
  for x, y in zip(a, b)
  if x + y >= 0])


#4-3-4 以巢狀 list 生成式產生複合 list

a = [1, 2, 3]

b = ['A', 'B']

print([[x, y] for x in a for y in b])

print('------------------------------------------------------------')	#60個

print('defaultdict 容器')
from collections import defaultdict

lst = ['foo', 'bar', 'pop', 'foo', 'bar', 'foo']

d = defaultdict(int)

for item in lst:
    d[item] += 1

print(d)

from collections import defaultdict

prices = [
  ['apple', 50],
  ['banana', 120],
  ['grape', 500],
  ['apple', 70],
  ['banana', 150],
  ['banana', 700]
]

fruits = defaultdict(list)

for name, price in prices:
    fruits[name].append(price)

for name, prices in fruits.items():
    print(name, prices)

print('------------------------------------------------------------')	#60個


#4-4-2 Counter 容器

from collections import Counter

lst = ['foo', 'bar', 'pop', 'foo', 'bar', 'foo']

c = Counter(lst)

print(c)

for item, counter in c.items():
    print(item, '出現', counter, '次')

print('出現最多次的項目:', c.most_common(1))

print('------------------------------------------------------------')	#60個

