# 自定義函數


print("自定義函數")

def mycnt1():
    for i in range(10, 20, 5):
        print(i)

mycnt1()

print("自定義函數 加參數")

def mycnt2(n):
    for i in range(10, n, 5):
        print(i)

mycnt2(30)

print("自定義函數 加參數，有預設值")

def mycnt3(n = 20):
    for i in range(10, n, 5):
        print(i)

mycnt3()
mycnt3(30)

print("自定義函數 多個參數")

def mycnt4(n1 = 10, n2 = 20):
    for i in range(n1, n2, 5):
        print(i)

mycnt4()
mycnt4(5)
mycnt4(5, 15)

print("函數返回值")

def mysum(n1, n2):
    "函數的說明"
    return n1 + n2

print(mysum(10, 20))




def f(x):
    return x**2

f(10)




