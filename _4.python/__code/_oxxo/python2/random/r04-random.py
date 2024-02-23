import random

# random.random() 並不是真正的隨機數，如果 seed 相同則結果相同
a = random.random()
print(a)

# uniform 返回兩個值中間的隨機浮點數
b = random.uniform(3,8)
print(b)

# triangular 返回兩個值中間的隨機浮點數
c = random.triangular(3,8)
print(c)

# beta 分佈，兩個值需都大於 0，返回 0~1 之間隨機浮點數
d = random.betavariate(3,8)
print(d)

# 指數分佈，不可為 0，若為負，則是小於零的福點數
e = random.expovariate(-5)
print(e)

# 其他還有
# random.gammavariate(alpha, beta)
# random.gauss(mu, sigma)
# random.lognormvariate(mu, sigma)
# random.normalvariate(mu, sigma)
# random.vonmisesvariate(mu, kappa)
# random.paretovariate(alpha)
# random.weibullvariate(alpha, beta)

# 參考：https://docs.python.org/zh-cn/3/library/random.html#random.random
