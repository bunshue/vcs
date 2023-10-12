import sys

import matplotlib.pyplot as plt
import numpy as np

print('------------------------------------------------------------')	#60個
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
print(f'總消費金額 = {sum(x)}')

print('------------------------------------------------------------')	#60個

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
print(f'平均消費金額 = {sum(x)/len(x)}')

print('------------------------------------------------------------')	#60個

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
print(f'平均消費金額 = {np.mean(x)}')

print('------------------------------------------------------------')	#60個

x1 = [7, 2, 11, 9, 20]
print(f'中位數 = {np.median(x1)}')

x1 = [30, 7, 2, 11, 9, 20]
print(f'中位數 = {np.median(x1)}')

print('------------------------------------------------------------')	#60個

x1 = np.array([0, 1, 1, 3, 2, 1])
# 因為 x1 元素最大值是 3, 所以 bin 是 4
print(f'np.bincount = {np.bincount(x1)}')       

x2 = np.array([0, 1, 1, 7, 2, 1])
# 因為 x2 元素最大值是 7, 所以 bin 是 8
print(f'np.bincount = {np.bincount(x2)}') 

print('------------------------------------------------------------')	#60個

x1 = np.array([0, 1, 1, 3, 2, 1])
# 因為 x1 元素最大值是 3, 所以 bin 是 4
print(f'np.bincount = {np.bincount(x1)}')
print(f'mode        = {np.argmax(np.bincount(x1))}')

x2 = np.array([0, 1, 1, 7, 2, 1])
# 因為 x2 元素最大值是 7, 所以 bin 是 8
print(f'np.bincount = {np.bincount(x2)}') 
print(f'mode        = {np.argmax(np.bincount(x1))}')

print('------------------------------------------------------------')	#60個









import statistics

x1 = [0, 1, 1, 3, 2, 1]
print(f'mode = {statistics.mode(x1)}')

print('------------------------------------------------------------')	#60個

import statistics

sc = [60,10,40,80,80,30,80,60,70,90,50,50,50,70,60,80,80,50,60,70,
      70,40,30,70,60,80,20,80,70,50,90,80,40,40,70,60,80,30,20,70]
print(f'平均成績 = {np.mean(sc)}')
print(f'中位成績 = {np.median(sc)}')
print(f'眾數成績 = {statistics.mode(sc)}')

hist = [0]*9
for s in sc:
    if s == 10: hist[0] += 1
    elif s == 20:
        hist[1] += 1
    elif s == 30:
        hist[2] += 1
    elif s == 40:
        hist[3] += 1
    elif s == 50:
        hist[4] += 1
    elif s == 60:
        hist[5] += 1
    elif s == 70:
        hist[6] += 1
    elif s == 80:
        hist[7] += 1
    elif s == 90:
        hist[8] += 1
width = 0.35
N = len(hist)
x = np.arange(N)
plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.bar(x, hist, width)
plt.ylabel('學生人數')
plt.xlabel('分數')
plt.xticks(x,('10','20','30','40','50','60','70','80','90'))
plt.title('成績表')

plt.show()

print('------------------------------------------------------------')	#60個

import statistics

sc = [60,10,40,80,80,30,80,60,70,90,50,50,50,70,60,80,80,50,60,70,
      70,40,30,70,60,80,20,80,70,50,90,80,40,40,70,60,80,30,20,70]
print(f'平均成績 = {np.mean(sc)}')
print(f'中位成績 = {np.median(sc)}')
print(f'眾數成績 = {statistics.mode(sc)}')
plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.hist(sc, 9)

plt.ylabel('學生人數')
plt.xlabel('分數')
plt.title('成績表')

plt.show()

print('------------------------------------------------------------')	#60個

import statistics

sc1 = [60,10,40,80,80,30,80,60,70,90,50,50,50,70,60,80,80,50,60,70,
      70,40,30,70,60,80,20,80,70,50,90,80,40,40,70,60,80,30,20,70]

sc2 = [50,10,60,80,70,30,80,60,30,90,50,50,90,70,60,50,80,50,60,70,
      60,50,30,70,70,80,10,80,70,50,90,80,40,50,70,60,80,40,20,70]

plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.hist([sc1,sc2],9)

plt.ylabel('學生人數')
plt.xlabel('分數')
plt.title('成績表')

plt.show()

print('------------------------------------------------------------')	#60個

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
mean = sum(x) / len(x)

# 計算變異數
myvar = 0
for v in x:
    myvar += ((v - mean)**2)
myvar = myvar / len(x)
print(f"變異數 : {myvar}")

print('------------------------------------------------------------')	#60個

import statistics
x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]

print(f"Numpy模組母體變異數  : {np.var(x):6.2f}")
print(f"Numpy模組樣本變異數  : {np.var(x,ddof=1):6.2f}")
print(f"Statistics母體變異數 : {statistics.pvariance(x):6.2f}")
print(f"Statistics樣本變異數 : {statistics.variance(x):6.2f}")

print('------------------------------------------------------------')	#60個

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
mean = sum(x) / len(x)

# 計算變異數
var = 0
for v in x:
    var += ((v - mean)**2)
sd = (var / len(x))**0.5
print(f"標準差 : {sd:6.2f}")

print('------------------------------------------------------------')	#60個

import statistics

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
print(f"Numpy模組母體標準差  : {np.std(x):6.2f}")
print(f"Numpy模組樣本標準差  : {np.std(x,ddof=1):6.2f}")
print(f"Statistics母體標準差 : {statistics.pstdev(x):6.2f}")
print(f"Statistics樣本標準差 : {statistics.stdev(x):6.2f}")


print('------------------------------------------------------------')	#60個

mu = 0                                                  # 平均值
sigma = 1                                               # 標準差
s = np.random.randn(10000)                              # 隨機數
print(s)

count, bins, ignored = plt.hist(s, 30, density=True)    # 直方圖
# 繪製曲線圖
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')

plt.show()

print('------------------------------------------------------------')	#60個

mu = 0                                                  # 均值
sigma = 1                                               # 標準差
s = np.random.normal(mu, sigma, 10000)                  # 隨機數

count, bins, ignored = plt.hist(s, 30, density=True)    # 直方圖
# 繪製曲線圖
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')

plt.show()

print('------------------------------------------------------------')	#60個

import seaborn as sns #海生, 自動把圖畫得比較好看

mu = 0                                                  # 均值
sigma = 1                                               # 標準差
s = np.random.normal(mu, sigma, 10000)                  # 隨機數

count, bins, ignored = plt.hist(s, 30, density=True)    # 直方圖
# 繪製曲線圖
sns.kdeplot(s)

plt.show()

print('------------------------------------------------------------')	#60個

s = np.random.uniform(0.0,5.0,size=250)     # 隨機數
plt.hist(s, 5)                              # 直方圖

plt.show()

print('------------------------------------------------------------')	#60個

import seaborn as sns #海生, 自動把圖畫得比較好看

s = np.random.uniform(size=10000)           # 隨機數

plt.hist(s, 30, density=True)               # 直方圖

# 繪製曲線圖
sns.kdeplot(s)

plt.show()

print('------------------------------------------------------------')	#60個

