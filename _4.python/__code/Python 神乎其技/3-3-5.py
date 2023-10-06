# 3-3-5 修飾有傳入參數的函式

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'追蹤: 呼叫函式 {func.__name__}, 參數為 {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'追蹤: 函式 {func.__name__} 傳回 {original_result!r}')
        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'


print(say('珍', '早唷!'))