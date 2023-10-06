# 4-8 用物件實作修飾器

import functools

class Uppercase:
    
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
    
    def __call__(self, *args, **kwargs):
        original_result = self.func(*args, **kwargs)
        return original_result.upper()

@Uppercase
def say(name, line):
    return f'{name}, {line}!'


print(say('Jane', 'Good morning'))