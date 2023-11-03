# ch11_26.py
def factorial(n):
    # 計算n的階乘, n 必須是正整數
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

value = 3
print(value, " 的階乘結果是 = ", factorial(value))
value = 5
print(value, " 的階乘結果是 = ", factorial(value))


    
