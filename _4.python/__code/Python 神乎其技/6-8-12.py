# 6-8-12 itertools 模組:
# product() 笛卡兒積
# permutations() 排列
# combinations() 組合
# combinations_with_replacement() 同元素可重複的組合

import itertools

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