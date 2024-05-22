"""

各種演算法

"""


print("------------------------------------------------------------")  # 60個


def bubbleSort(list):
    needNextPass = True

    k = 1
    while k < len(list) and needNextPass:
        # List may be sorted and next pass not needed
        needNextPass = False
        for i in range(len(list) - k):
            if list[i] > list[i + 1]:
                # swap list[i] with list[i + 1]
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp

                needNextPass = True  # Next pass still needed


list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
bubbleSort(list)
for v in list:
    print(v)

print("------------------------------------------------------------")  # 60個


def Fibonacci(n):  # 写出从第0项到第n项的Fibonacci系列
    a, b, i = 0, 1, 0
    while i <= n:
        print(a, end=" ")
        a, b, i = b, a + b, i + 1
    print()


print(Fibonacci(10))

print("------------------------------------------------------------")  # 60個

# n = int(input("請輸入大於 1 的整數："))
n = 1723
if n == 2:
    print("2 是質數！")
else:
    for i in range(2, n):
        if n % i == 0:
            print("%d 不是質數！" % n)
            break
    else:
        print("%d 是質數！" % n)

print("------------------------------------------------------------")  # 60個


def gcd(n1, n2):
    g = 1  # 最初化最大公約數
    n = 2  # 從2開始檢測
    while n <= n1 and n <= n2:
        if n1 % n == 0 and n2 % n == 0:
            g = n  # 新最大公約數
        n += 1
    return g


n1, n2 = 1233, 2477
print("最大公約數是 : ", gcd(n1, n2))

print("------------------------------------------------------------")  # 60個


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a


a, b = 1233, 2477
print("最大公約數是 : ", gcd(a, b))

print("------------------------------------------------------------")  # 60個


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


a, b = 1233, 2477
print("最大公約數是 : ", gcd(a, b))

print("------------------------------------------------------------")  # 60個


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


a, b = 1233, 2477
print("最大公約數是 : ", gcd(a, b))
print("最小公倍數是 : ", lcm(a, b))


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
