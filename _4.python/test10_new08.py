import numpy as np
import matplotlib.pyplot as plt


'''
print('------------------------------------------------------------')	#60個

# 資料
x = [1, 2, 3, 4, 5, 6, 7]
y = [64.3, 63.8, 63.6, 64.0, 63.5, 63.2, 63.1]


# y = 3 * x - 24
y = []
for x in range(1, 11):
    y.append(3 * x - 24)
print(type(y))
print(y)



# 資料
x = np.arange(-1.0, 1.01, 0.01)

y = x ** 2



# 繪圖
plt.plot(x, y)        # 描繪折線
plt.grid(color='0.8') # 顯示格線
plt.show()            # 顯示在畫面上


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個






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


'''

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





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



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
print('畫出年收入圖')

import matplotlib.pyplot as plt
import pandas as pd

# 讀入csv檔
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV7_salary.csv'
dat = pd.read_csv(filename, encoding='UTF-8')

# 設定資料
x = dat['年齡']
y = dat['年收入']

# 繪圖
plt.plot(x, y)
plt.grid(color='0.8')
plt.show()




import sys
sys.exit()

print('------------------------------------------------------------')	#60個
print('描繪差額圖')
# 資料筆數
cnt = len(dat)

# 取差額
diff_y = []
for i in range(0, cnt-1):
    diff_y.append(y[i+1] - y[i])

# 繪圖
plt.plot(x[1:], diff_y)
plt.grid(color='0.8')
plt.show()





print('------------------------------------------------------------')	#60個
print('畫出函數與導函數的圖')

import matplotlib.pyplot as plt
import numpy as np

# x的值
x = np.arange(-10, 10, 0.1)

# 原來的函數 f(x) = x**3 + 3x**2 + 3x + 1
y = x**3 + 3*x**2 + 3*x + 1
plt.plot(x, y)
plt.grid(color='0.8')
plt.show()

# 導函數 f'(x) = 3x**2 + 6x + 3
y2 = 3*x**2 + 6*x + 3
plt.plot(x, y2)
plt.grid(color='0.8')
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
print('描繪切線')


import matplotlib.pyplot as plt
import numpy as np

# x的值
x = np.arange(-1, 1, 0.1)

# 原來的函數
y = 2*x*x + 3

# 切線
a = 4*0.25            # 導函數 f'(x)= 4x（斜率）
b = 3.125 - a * 0.25  # 截距 b = y - ax
y2 = a*x + b          # 切線的式子

# 繪圖
plt.plot(x, y)   # 原來的函數
plt.plot(x, y2)  # 切線
plt.grid(color='0.8')
plt.show()

print('------------------------------------------------------------')	#60個








from scipy import integrate
import math

# 計算半徑為r的圓的圓周
def calc_area(r):
    return 2 * math.pi * r

# 半徑2～5範圍的圓周總和
s = integrate.quad(calc_area, 2, 5)
print(s)

# 廁所衛生紙長度
x = s[0] / 0.011
print(x)


print('------------------------------------------------------------')	#60個





