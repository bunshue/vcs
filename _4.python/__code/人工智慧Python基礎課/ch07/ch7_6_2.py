# 函數: 計算2個參數和
def sum(a, b):
    return a + b
    
# 函數: 使用函數作為參數    
def operate_on(x, y, func):
    return func(x, y)

r = operate_on(16, 20, sum)   # 呼叫函數
print("operate_on(16, 20, sum) = ", r)
          




