# ch11_21.py
def factorial(n):
    """ 計算n的階乘, n 必須是正整數 """
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

N = eval(input("請輸入階乘數 : "))
print(N, " 的階乘結果是 = ", factorial(N))





    
