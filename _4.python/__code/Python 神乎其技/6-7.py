# 6-7 走訪器串聯

def numbers():
    for i in range(10):
        yield i

def square(value):
    for v in value:
        yield v ** 2

def negative(value):
    for v in value:
        yield v * -1


result = negative(square(numbers()))

for item in result:
    print(item)