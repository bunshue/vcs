# ch11_39_1c.py
def iter_data():
    x = 10
    yield x
    x = x * x
    yield x
    x = 2 * x
    yield x

myiter = iter_data()    # 建立迭代器
print(next(myiter))
print(next(myiter))
print(next(myiter))





