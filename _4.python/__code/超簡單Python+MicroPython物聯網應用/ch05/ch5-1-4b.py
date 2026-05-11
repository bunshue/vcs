def sum(a, b, c):
    return a + b + c

r3 = sum(1, c=3, b=2)   # 混合使用位置和關鍵字引數
r4 = sum(1, 2, c=3)     # 混合使用位置和關鍵字引數
print("總和 = " + str(r3))
print("總和 = " + str(r4))
