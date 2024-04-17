# Filename: ex07_07.py
# 循序搜尋
#資料排序
def fib(n):
    if n==0:
        return 0                   #base
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)    #recursive
n = int(input("請輸入一個正整數:"))
print("費氏數列第%d個值為%d"%(n, fib(n)))     