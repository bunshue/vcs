# 3-1-1 函式的一級物件特性: 函式是物件

def yell(text):
    return text.upper() + '!'


bark = yell

print(yell('hello'))
print(bark('woof'))

del yell

print(bark('hey'))
print(bark.__name__)

#print(yell('hey'))