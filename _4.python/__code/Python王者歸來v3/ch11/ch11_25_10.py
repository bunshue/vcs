# ch11_25_10.py
def factorial(n):
    """ 計算n的階乘, n 必須是正整數 """
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact    

value = 3
print(f"{value} 的階乘結果是 = {factorial(value)}")
value = 5
print(f"{value} 的階乘結果是 = {factorial(value)}")


    
