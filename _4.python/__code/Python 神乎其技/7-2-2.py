# 7-2-2 用 sort() 以值排序 dict

xs = {'a': 4, 'c': 1, 'd': 3, 'b': 2}

print(xs.items())

print(sorted(xs.items(), key=lambda x: x[1]))

print(sorted(xs.items(), key=lambda x: x[1], reverse=True))