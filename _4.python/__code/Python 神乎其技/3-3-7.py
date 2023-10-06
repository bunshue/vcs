# 3-3-7 對類別 method 套用修飾器

import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


class Greet:
    def __init__(self):
        pass
    
    @uppercase
    def say(self, text):
        return text


greet = Greet()

print(greet.say('Good morning, Bob!'))