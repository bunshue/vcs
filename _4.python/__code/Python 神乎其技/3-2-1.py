# 3-2-1 lambda: 只有單一運算式的匿名函式

add = lambda x, y: x + y

print(add(5, 3))

print((lambda x, y: x + y)(5, 3))