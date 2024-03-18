#畫y=x^2
#畫y=sin(x)

'''
import math
import matplotlib.pyplot as plt

x=[]
y=[]
for i in range(10):
    print(i)
    x.append(i)
    y.append(i*i)  #y=x^2
    #y.append(math.sin(i))  #y=sin(x)

plt.plot(x, y)  # 繪圖

plt.show()

print('------------------------------------------------------------')	#60個

#畫直線 y = 3*x + 2

import math
import matplotlib.pyplot as plt

x=[]
y=[]
for i in range(-10, 10):
    print(i)
    x.append(i)
    y.append(3*i + 2)  #y = 3*x + 2

plt.plot(x, y)  # 繪圖

plt.show()

print('------------------------------------------------------------')	#60個

#畫更精細的y=sin(x)

#畫y=x^2
#畫y=sin(x)

import math
import matplotlib.pyplot as plt

x=[]
y=[]
for i in range(100):
    #print(i)
    x.append(i)
    y.append(math.sin(i/10))  #y=sin(x)

plt.plot(x, y)  # 繪圖

plt.show()

'''
print('------------------------------------------------------------')	#60個

#等差數列 等差級數 等比數列 等比級數
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
