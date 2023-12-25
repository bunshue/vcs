import math
x = 10
y = -2

z = math.fabs(x / y)
h = math.factorial(z)

if math.isnan(h) == False:
    print("計算後數值：", h)
    print("最大公約數：", math.gcd(h, x))
