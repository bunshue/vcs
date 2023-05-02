# scatter 集合


import matplotlib.pyplot as plt
import numpy as np

A = 10  #震幅
N = 10  #總點數
rng = np.random.RandomState(42)
#print(rng)
x = A * rng.rand(N)     #0~A取N個數出來
y = A * rng.rand(N)     #0~A取N個數出來
plt.scatter(x, y)       #畫出每個x-y對應點
plt.show()



'''
import numpy as np
import matplotlib.pyplot as plt

#曲線資料加入雜訊
x = np.linspace(-5,5,200)
y = np.sin(x)
yn = y + np.random.rand(1, len(y))*1.5

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x,yn,c='blue',marker = '.')
ax.plot(x,y+0.75,'r')
plt.show()
'''




