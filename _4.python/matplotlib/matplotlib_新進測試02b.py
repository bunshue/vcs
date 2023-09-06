import numpy as np
import matplotlib.pyplot as plt



print('------------------------------------------------------------')	#60個

import pandas as pd

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV6_score.csv'

dat = pd.read_csv(filename, encoding='UTF-8')
print(dat.head())

print('------------------------------------------------------------')	#60個

#計算平均數、中位數、眾數

import pandas as pd
import numpy as np

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV6_score.csv'

dat = pd.read_csv(filename, encoding='UTF-8')

# 平均數、中位數
print('平均數', np.mean(dat['數學']))
print('中位數', np.median(dat['數學']))

# 眾數
bincnt = np.bincount(dat['數學'])  # 計算同樣的值的個數
mode = np.argmax(bincnt)  # 取得bincnt中最大的值
print('眾數', mode)

print('------------------------------------------------------------')	#60個
print('畫出頻率分布圖')

import matplotlib.pyplot as plt
import pandas as pd

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV6_score.csv'

dat = pd.read_csv(filename, encoding='UTF-8')

# 計算各組別頻率
hist = [0]*10 # 頻率（元素個數10，初始化為0）
for dat in dat['數學']:
    if dat < 10:   hist[0] += 1
    elif dat < 20:  hist[1] += 1
    elif dat < 30:  hist[2] += 1
    elif dat < 40:  hist[3] += 1
    elif dat < 50:  hist[4] += 1
    elif dat < 60:  hist[5] += 1
    elif dat < 70:  hist[6] += 1
    elif dat < 80:  hist[7] += 1
    elif dat < 90:  hist[8] += 1
    elif dat <= 100:  hist[9] += 1 
print('頻率:', hist)

# 頻率分布圖
x = list(range(1,11))  # x軸的值
labels = ['0~','10~','20~','30~','40~','50~','60~','70~','80~','90~']  # x軸的刻度標籤
plt.bar(x, hist, tick_label=labels, width=1)# 描繪長條圖

plt.show()



print('------------------------------------------------------------')	#60個
print('描繪頻率分布圖')

import matplotlib.pyplot as plt
import pandas as pd

# 讀入csv檔
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV7_onigiri.csv'
dat = pd.read_csv(filename, encoding='UTF-8')

# 頻率分布圖
plt.hist(dat['店長'], bins=range(0, 200, 10), alpha=0.5)
plt.hist(dat['太郎'], bins=range(0, 200, 10), alpha=0.5)

plt.show()



print('計算平均數、變異數、標準差')


import numpy as np
print('店長---------')
print('平均:', np.mean(dat['店長']))
print('變異數:', np.var(dat['店長']))
print('標準差:', np.std(dat['店長']))

print('太郎---------')
print('平均:', np.mean(dat['太郎']))
print('變異數:', np.var(dat['太郎']))
print('標準差:', np.std(dat['太郎']))

print('------------------------------------------------------------')	#60個
print('亂數')

import random
rand = [] 
for i in range(10):
    rand.append(random.randint(0,100)) # 產生0～100的亂數
print(rand)

print('------------------------------------------------------------')	#60個

a = 4     # 亂數的初始值
b = 7
c = 9
rn = 1    
rand = []
for i in range(20):
    rn = ((a * rn + b) % c)    # 產生亂數
    rand.append(rn)
print(rand)

print('------------------------------------------------------------')	#60個

plt.show()

print('------------------------------------------------------------')	#60個

plt.show()

print('------------------------------------------------------------')	#60個


plt.show()

print('------------------------------------------------------------')	#60個

#SciPy.integrate.quad()函式


from scipy import integrate

# f(x) = x**2 + 2x + 5
def func(x):
    return x**2 + 2*x + 5

print(integrate.quad(func, -3, 3))

#(47.99999999999999, 5.32907051820075e-13)




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



