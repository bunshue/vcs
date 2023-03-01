# 自定義函數


import my_print  #把整個 my_print.py 都引進來
print("測試導入自定義模組")
my_print.print_func("Python")



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



def add(x,y):
    return x+y

z = add(1234,5678)
print(z)



#撰寫接受任意數目引數的函式
def avg(first, *rest):
    return (first + sum(rest)) / (1+len(rest))

a = avg(1,2)
b = avg(1,2,3,4)

print("average 1", a, "\n")
print("average 2", b, "\n")





