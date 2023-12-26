# ch11_42.py
def gcd(n1, n2):
    g = 1                               # 最初化最大公約數
    n = 2                               # 從2開始檢測
    while n <= n1 and n <= n2:
        if n1 % n == 0 and n2 % n == 0:
            g = n                       # 新最大公約數
        n += 1
    return g

n1, n2 = eval(input("請輸入2個整數值 : "))
print("最大公約數是 : ", gcd(n1,n2))


