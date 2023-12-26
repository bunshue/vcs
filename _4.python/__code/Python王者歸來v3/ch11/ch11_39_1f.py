# ch11_39_1f.py
def iter_square(n):
    for data in range(1, n+1):
        yield data ** 2
    
myiter = iter_square(5)     # 建立迭代器
for data in myiter:
    print(data)







