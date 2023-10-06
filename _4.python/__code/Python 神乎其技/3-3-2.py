# 3-3-2 修飾器基礎 (2)

def null_decorator(func):
    return func

@null_decorator
def greet():
    return '哈嘍!'


print(greet())
