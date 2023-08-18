# ch1_34.py
import numpy as np

# 計算 3 的 2 次方
x = np.power(3, 2)
print("計算 3 的 2 次方")
print(x)

# 底數是陣列
print("底數是陣列, 指數是 3")
x1 = np.arange(6)
print(f"x1 = {x1}")
y1 = np.power(x1,3)
print(f"y1 = {y1}")

# 底數和指數皆是陣列
print("底數是 x1 和指數是 x2 皆是陣列")
print(f"x1 = {x1}")
x2 = [1,2,3,3,2,1]
print(f"x2 = {x2}")
y2 = np.power(x1,x2)
print(f"y2 = {y2}")
    





