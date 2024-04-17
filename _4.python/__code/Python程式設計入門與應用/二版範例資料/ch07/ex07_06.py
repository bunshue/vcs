# Filename: ex07_06.py
def factorial(n):
    if n==0:
        return 1                   #base
    else:
        return n*factorial(n-1)    #recursive
n = int(input("請輸入一個正整數:"))
print("輸入的正整數為%d，計算的階層值為%d"%(n, factorial(n)))     