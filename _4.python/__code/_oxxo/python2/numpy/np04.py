import numpy as np

# 產生一個 0~1 的隨機數
r1 = np.random.random_sample()
print(r1)
r2 = np.random.random_sample((2,2))
print(r2)

# 產生一個多維陣列 0 ~ 1 的隨機數 ( 不包含 1 )
# 一樣有 seed 概念，seed 相同產生的隨機數就相同
a = np.random.rand(4, 3)
print(a)
b = np.random.rand(4, 3, 2)
print(b)

# 如果只是想返回一個隨機數，可使用 randn()
# randn 的用法和 rand 類似，也可從標準正態分佈中產生多維陣列隨機數
# https://wiki.mbalib.com/zh-tw/%E6%AD%A3%E6%80%81%E5%88%86%E5%B8%83
c = np.random.randn()
print(c)

# 產生隨機整數，也可用 size 產生多維陣列隨機數
d = np.random.randint(1, 100, 10)
print(d)
e = np.random.randint(1, 100, size=(2, 2, 3))
print(e)
