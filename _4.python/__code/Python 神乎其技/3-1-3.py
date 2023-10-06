# 3-1-3 函式的一級物件特性: 函式可做為參數傳給其他函式

def yell(text):
    return text.upper()

bark = yell

def greet(func):
    greeting = func('Hi, I am a Python Program')
    print(greeting)


greet(bark)

greet(str.swapcase)

print(list(map(bark, ['hello!', 'hey!', 'hi!'])))