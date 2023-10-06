# 3-3-3 修飾器能夠修改函式行為

def uppercase(func):
    
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    
    return wrapper

@uppercase
def greet():
    return 'Hello!'


print(greet())
print(greet)