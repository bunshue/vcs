# ch11_33_2.py
def func(b):
    return lambda x : 2 * x + b 

linear  = func(5)       # 5將傳給lambda的 b
print(linear(10))       # 10是lambda的 x

linear2 = func(3)
print(linear2(10))












