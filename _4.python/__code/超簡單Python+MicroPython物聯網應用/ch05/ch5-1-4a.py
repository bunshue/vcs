def sum(a, b, c):
    return a + b + c

r1 = sum(1, 2, 3)       # 函式呼叫(位置引數)
r2 = sum(b=2, c=3, a=1) # 函式呼叫(關鍵字引數)
print("總和 = ", r1)
print("總和 = ", r2)
