"""
等差數列 等比數列
等差級數 等比級數

"""

print('------------------------------------------------------------')	#60個

#等差數列 等差級數

for i in range(10):
    print(i)

x = range(11) # 0, 1, 2, ... 10
s = sum(x)
print('等差級數 :', s)

x = range(3, 21, 3) # 3, 6, 9, ... 18
for i in x:
    print(i)
s = sum(x)
print('等差級數 :', s)

print('------------------------------------------------------------')	#60個

#等比數列 等比級數

r = 2
A0 = 1
x = []
y = []
total = 0
for i in range(10 + 1):
    print(i)
    x.append(i)
    y.append(A0 * r ** i)
    total += A0 * r ** i

print(x)
print(y)
print(total)

import matplotlib.pyplot as plt
plt.plot(x, y)  # 繪圖
plt.show()

print('------------------------------------------------------------')	#60個

