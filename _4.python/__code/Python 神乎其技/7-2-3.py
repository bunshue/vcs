# 7-2-3 用 reversed() 產生倒轉的 dict 走訪器

xs = {'a': 4, 'c': 1, 'd': 3, 'b': 2}

print(xs.items())

print(reversed(xs.items()))

print(list(reversed(xs.items())))

for key, item in reversed(xs.items()):
    print(key, item)