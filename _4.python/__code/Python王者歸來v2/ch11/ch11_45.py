# ch11_45.py

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = eval(input("請輸入2個整數值 : "))
print("最大公約數是 : ", gcd(a, b))
print("最小公倍數是 : ", lcm(a, b))




