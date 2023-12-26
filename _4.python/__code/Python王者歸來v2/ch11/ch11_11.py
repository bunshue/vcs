# ch11_11.py
def subtract(x1, x2):
    """ 減法設計 """
    result = x1 - x2
    return result                   # 回傳減法結果
print("本程式會執行 a - b 的運算")     
a = int(input("a = "))
b = int(input("b = "))
print("a - b = ", subtract(a, b))   # 輸出a-b字串和結果


