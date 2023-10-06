# 3-3-8 讓修飾器本身也可輸入參數

import functools

def uppercase_repeat(n):
    def uppercase(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result = result.upper()
            for _ in range(n):
                print(result)
            return result
        return wrapper
    return uppercase

@uppercase_repeat(5)
def say(text):
    return text


print(say('Good morning, Bob!'))