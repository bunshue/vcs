# 6-8-7 itertools 模組: accumulate() 累加

import itertools

n = [0, 1, 2, 3, 4]
print(list(itertools.accumulate(n)))

c = ['A', 'B', 'C', 'D', 'E']
print(list(itertools.accumulate(c)))


data = range(1, 11)
multiply = lambda x, y: x * y

print(list(itertools.accumulate(data, multiply)))