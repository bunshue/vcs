# 3-6 函式的隱含 return 敘述

def foo1(value):
    if value:
        return value
    else:
        return None

def foo2(value):
    if value:
        return value
    else:
        return

def foo3(value):
    if value:
        return value


print(foo1(0))
print(foo2(0))
print(foo3(0))
print(type(foo1(0)))
print(type(foo2(0)))
print(type(foo3(0)))