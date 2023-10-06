# 6-8-6 itertools 模組: islice() 切片

import itertools

n = [0, 1, 2, 3, 4]

print(list(itertools.islice(n, 3)))

print(list(itertools.islice(n, 1, 3)))

print(list(itertools.islice(n, 0, 5, 2)))