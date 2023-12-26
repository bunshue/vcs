# ch11_13_1.py
def mutifunction(x1, x2):
    """ 加, 減, 乘, 除四則運算 """
    addresult = x1 + x2
    subresult = x1 - x2
    mulresult = x1 * x2
    divresult = x1 / x2
    return addresult, subresult, mulresult, divresult

x1 = x2 = 10
ans = mutifunction(x1, x2)
print("資料型態 : ", type(ans))
print("加法結果 = ", ans[0])
print("減法結果 = ", ans[1])
print("乘法結果 = ", ans[2])
print("除法結果 = ", ans[3])






