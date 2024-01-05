# 函數: 回傳2個參數的最大值
def bigger(a, b):
    if a > b:
       return a, b
    else:
       return b, a            

t = bigger(10, 30)
print(t)
print(type(t))
x, y = bigger(10, 20)
print(x, y)
