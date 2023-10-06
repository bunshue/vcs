# 6-8-8 itertools 模組: starmap() 解包外層容器

import itertools

n = [(1, 2), (2, 3), (3, 5), (5, 7), (7, 11)]

print(list(itertools.starmap(lambda x, y: x * y, n)))

print(list(map(lambda t: t[0] * t[1], n)))