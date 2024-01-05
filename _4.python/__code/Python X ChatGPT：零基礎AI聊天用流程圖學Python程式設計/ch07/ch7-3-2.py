# 函數: 計算3個參數的總和
def total(a, b, c):
    return a + b + c

r1 = total(1, 2, 3)       # 函數呼叫(位置引數)
r2 = total(b=2, c=3, a=1) # 函數呼叫(關鍵字引數)
r3 = total(1, c=3, b=2)   # 混合使用位置和關鍵字引數
r4 = total(1, 2, c=3)
print("總和 = ", r1)
print("總和 = ", r2)
print("總和 = ", r3)
print("總和 = ", r4)
