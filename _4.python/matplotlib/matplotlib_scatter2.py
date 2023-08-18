# scatter 集合

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個


'''
x = np.linspace(0, 10, 11)
print(type(x))
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(x))

y1 = np.sin(x) * 5 + 5
y2 = np.cos(x) * 5 + 5

plt.scatter(x, y1, c = 'r')       #畫出每個x-y對應點
plt.scatter(x, y2, c = 'g')       #畫出每個x-y對應點
plt.show()
'''


print('------------------------------------------------------------')	#60個

'''

A = 10  #震幅
N = 100  #總點數
rng = np.random.RandomState(42)
#print(rng)
x = A * rng.rand(N)     #0~A取N個數出來
print(type(x))
y = A * rng.rand(N)     #0~A取N個數出來
plt.scatter(x, y)       #畫出每個x-y對應點
plt.show()




print('------------------------------------------------------------')	#60個



'''



#曲線資料加入雜訊
x = np.linspace(-5,5,200)
y = np.sin(x)
yn = y + np.random.rand(1, len(y))*1.5

fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(x,yn,c='blue',marker = '.')
ax.plot(x,y+0.75,'r')
plt.show()




'''
蒙地卡羅模擬 Monte Carlo Simulation 使用亂數與機率來解決問題
'''

import math
import random
import matplotlib.pyplot as plt

print('蒙地卡羅模擬')

L = 100
NUMBER_OF_TRIALS = 1000
numberOfHits = 0

r = L / 2
cx = r
cy = r

numberOfHits = 0
for i in range(NUMBER_OF_TRIALS):
    x = random.randint(0, L) # 0 ~ L (含前後) 之間的任意整數
    y = random.randint(0, L) # 0 ~ L (含前後) 之間的任意整數
    #print(x, y)

    d = math.sqrt((x-cx)**2+(y-cy)**2)  #點與中心的距離
    if d <= r:
        numberOfHits += 1
        plt.scatter(x, y, marker = '.', c = 'r')
    else:
        plt.scatter(x, y, marker = '.', c = 'g')
        
#求圓周率
p = numberOfHits / NUMBER_OF_TRIALS
pi = p * 4
print('圓周率 = ', pi)

plt.axis('equal')

plt.show()






