# ch11_25_6.py
def outer():                   
    def inner(n):
        print('inner running')
        return sum(range(n))
    return inner

f = outer()         # outer()傳回inner位址
print(f)            # 列印inner記憶體
print(f(5))         # 實際執行的是inner()

y = outer()
print(y)
print(y(10))















