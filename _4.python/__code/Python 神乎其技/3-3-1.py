# 3-3-1 修飾器基礎 (1)

def null_decorator(func):
    return func

def greet():
    return '哈嘍!'


greet = null_decorator(greet)

print(greet())