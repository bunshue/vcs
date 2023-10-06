# 6-8-11 itertools 模組: compress() 過濾元素

import itertools

data = 'ABCDEFG'
selector = [1, 0, 1, 1, 0, 1, 0]

print(list(itertools.compress(data, selector)))