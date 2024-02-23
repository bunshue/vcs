# ch12_2.py
 
def fib(i):
    ''' 計算 Fibonacci number '''
    if i == 0:                              # 定義 0
        return 0
    elif i == 1:                            # 定義 1
        return 1
    else:                                   # 執行遞迴計算     
        return fib(i - 1) + fib(i - 2)

n = eval(input("請輸入 Fibonacci number: "))
for i in range(n+1):
    print("n = {},   Fib({}) = {}".format(i, i, fib(i)))



          


