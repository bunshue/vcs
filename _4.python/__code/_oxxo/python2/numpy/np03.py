import numpy as np

# 複製數據
a = [1, 2, 3]
b = np.asarray(a)
c = a
a = [4, 5, 6]
d = np.asarray(a, dtype=float)
print(a)   # [4, 5, 6]
print(b)   # [1 2 3]
print(c)   # [1, 2, 3]
print(d)   # [4. 5. 6.]

# 產生數據
x = np.arange(5, dtype=float)
print(x)  # [0. 1. 2. 3. 4.]
x2 = np.arange(0, 10, 2)
print(x2)  # [0 2 4 6 8]

# 使用 linspace 產生數據
y = np.linspace(1,10,10, dtype=int)
print(y) # [ 1  2  3  4  5  6  7  8  9 10]
y2 = np.linspace(1,2,10)
print(y2) 
# [1. 1.11111111 1.22222222 1.33333333 1.44444444 1.55555556 1.66666667 1.77777778 1.88888889 2.]
