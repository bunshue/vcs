# ch11_13.py
def mutifunction(x1, x2):
    """ 加, 減, 乘, 除四則運算 """
    addresult = x1 + x2
    subresult = x1 - x2
    mulresult = x1 * x2
    divresult = x1 / x2
    return addresult, subresult, mulresult, divresult

x1 = x2 = 10
add, sub, mul, div = mutifunction(x1, x2)
print("加法結果 = ", add)
print("減法結果 = ", sub)
print("乘法結果 = ", mul)
print("除法結果 = ", div)


