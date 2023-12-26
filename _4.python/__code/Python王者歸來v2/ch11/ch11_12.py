# ch11_12.py
def subtract(x1, x2):
    """ 減法設計 """
    return x1 - x2                     # 回傳減法結果
def addition(x1, x2):
    """ 加法設計 """
    return x1 + x2                     # 回傳加法結果

# 使用者輸入
print("請輸入運算")
print("1:加法")
print("2:減法")
op = int(input("輸入1/2: "))
a = int(input("a = "))
b = int(input("b = "))

# 程式運算
if op == 1:
    print("a + b = ", addition(a, b))   # 輸出a-b字串和結果
elif op == 2:
    print("a - b = ", subtract(a, b))   # 輸出a-b字串和結果
else:
    print("運算方法輸入錯誤")


