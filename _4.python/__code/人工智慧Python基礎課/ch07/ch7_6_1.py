# 函數: 計算2個參數和
def sum(a, b):
    return a + b
    
# 建立匿名函數
square = lambda x: x * x

# 將變數指定成函數
total = sum
r = square(10)   # 呼叫匿名函數
print("square(10) = ", r)
r = sum(10, 5)   # 呼叫函數
print("sum(10, 5) = ", r)
r = total(10, 5) # 使用變數呼叫函數
print("total(10, 5) = ", r)
          




