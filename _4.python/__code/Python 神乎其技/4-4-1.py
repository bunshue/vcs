# 4-4-1 物件淺拷貝

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)

print('xs =', xs)
print('ys =', ys)
print('xs == ys:', xs == ys)
print('xs is ys:', xs is ys)

xs.append([10, 11, 12])

print('xs =', xs)
print('ys =', ys)

xs[1][0] = 'X'

print('xs =', xs)
print('ys =', ys)