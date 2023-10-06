# 6-8-4 itertools 模組: chain() 串聯可走訪物件

import itertools

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