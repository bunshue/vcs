# 3-2-2 在 sorted() 使用 lambda 匿名函式

tuples_list = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]


print(sorted(tuples_list))

print(sorted(tuples_list, key=lambda x: x[1]))

print(sorted(range(-5, 6), key=lambda x: x ** 2))