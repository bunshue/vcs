# 3-3-6 用 functools.wraps 讓修飾器正名和更易除錯

import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    """說明: 傳回友善的問候"""
    return '哈嘍!'


print(greet.__name__)
print(greet.__doc__)