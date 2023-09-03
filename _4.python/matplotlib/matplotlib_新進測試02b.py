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

plt.show()

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


'''
xpt = list(range(1,11))        # 建立1-100序列x座標點

plt.plot(squares, lw=10)       # 串列squares數據是y軸的值, 線條寬度是10
plt.tick_params(axis='both', labelsize=12, color='red')

plt.plot(seq, data1, 'g--', seq, data2, 'r-.', seq, data3, 'y:', seq, data4, 'k.')   
plt.plot(seq, data1, '-*', seq, data2, '-o', seq, data3, '-^', seq, data4, '-s')   
plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度

plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   

'''

'''
print('------------------------------------------------------------')	#60個
seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度
plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')


plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)


seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度




print('------------------------------------------------------------')	#60個
plt.plot(x, y, label="$sin(x)$", color='red', lw=2)
plt.plot(x, z, label="$cos(x^2)$", color='b')


plt.plot(x, y, c='#6b8fb4', lw=5, marker='o', mfc='#fffa7c', mec="#084c61", mew=3, ms=20)
'''

print('------------------------------------------------------------')	#60個

'''
plt.plot(x, np.sin(x), c='#e63946', lw=3)
plt.plot(x, np.sin(3*x), c='#7fb069', lw=3)
plt.scatter(x, np.random.randn(100), c='#daa73e', s=50, alpha=0.5)
plt.bar(range(10), np.random.randint(1,30,10), fc='#e55934')

plt.plot(x,y,'r-.')
'''


print('------------------------------------------------------------')	#60個

plt.plot(x, y, marker='o')
plt.plot(x, y, c='#6b8fb4', lw=5, marker='o', mfc='#fffa7c', mec="#084c61", mew=3, ms=20)

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


import matplotlib.pyplot as plt

Benz = [3367, 4120, 5539]               # Benz線條
BMW = [4000, 3590, 4423]                # BMW線條
Lexus = [5200, 4930, 5350]              # Lexus線條

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度
plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend(loc='best')
plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)

#後面要用
plt.savefig('out1_14.jpg', bbox_inches='tight')

plt.show()

print('------------------------------------------------------------')	#60個


import matplotlib.pyplot as plt
import matplotlib.image as img

fig = img.imread('out1_14.jpg')
plt.imshow(fig)

plt.show()


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



