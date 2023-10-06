# 7-2-1 用 sort() 排序 dict

xs = {'a': 4, 'c': 1, 'd': 3, 'b': 2}

print(xs.items())

print(sorted(xs.items()))

for key, item in sorted(xs.items()):
    print(key, item)