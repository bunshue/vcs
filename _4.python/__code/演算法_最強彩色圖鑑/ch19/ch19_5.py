# ch19_5.py
def gcd(a, b):
    '輾轉相除法求最大公約數'
    if a < b:
        a, b = b, a
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

def lcm(a, b):
    return a*b // gcd(a, b)

a, b = eval(input("請輸入2個整數值 : "))
print("最大公約數是 : ", gcd(a, b))
print("最小公倍數是 : ", lcm(a, b))





