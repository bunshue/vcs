def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
    
def operate_on(x, y, func):
    return func(x, y)

print('函數: 使用函數作為參數')

a = 16
b = 20

c1 = operate_on(a, b, add)   # 呼叫函數
print("operate_on(16, 20, add) = ", c1)
          
c2 = operate_on(a, b, subtract)   # 呼叫函數
print("operate_on(16, 20, subtract) = ", c2)

c3 = operate_on(a, b, multiply)   # 呼叫函數
print("operate_on(16, 20, multiply) = ", c3)

c4 = operate_on(a, b, divide)   # 呼叫函數
print("operate_on(16, 20, divide) = ", c4)




