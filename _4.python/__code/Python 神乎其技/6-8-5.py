# 6-8-5 itertools 模組: zip_longest() - 完整走訪版 zip

import itertools

x = ['A', 'B', 'C', 'D', 'E']
y = [1, 2, 3]

print(list(zip(x, y)))

print(list(itertools.zip_longest(x, y)))

print(list(itertools.zip_longest(x, y, fillvalue=0)))