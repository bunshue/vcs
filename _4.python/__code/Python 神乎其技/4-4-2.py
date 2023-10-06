# 4-4-2 物件深拷貝

import copy

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)

print('xs == zs:', xs == zs)
print('xs is zs:', xs is zs)

xs[1][0] = 'X'

print('xs =', xs)
print('zs =', zs)