# ch11_20.py
def gcd(a, b):
    # 輾轉相除法, 也就是歐幾里德演算法 
    if a < b:
        a, b = b, a
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

a, b = eval(input("請輸入2個整數值 : "))
print("最大公約數是 : ", gcd(a, b))





