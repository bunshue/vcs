"""
統計專用

"""

print('------------------------------------------------------------')	#60個


import numpy as np

a = 580
b = 600
c = 680
d = 620

a = 600
b = 600
c = 600
d = 600

arr = np.array([a, b, c, d])

print(a, b, c, d)
print(np.std(arr, ddof = 0))#lee use this  wiki use this

average = (a + b + c + d) / 4
print(average)

print(average + 2 * np.std(arr, ddof = 0))

#指定 ddof 參數，全名為 Delta Degree of Freedom，np.std() 預設的 ddof 是 0
#ddof=0，回傳 population standard deviation 母體標準差，分母(n)，有偏估計
#ddof=1，回傳 sample standard deviation 樣本標準差，分母(n-1)，無偏估計



print(np.std(arr, ddof = 1))#this

print('------------------------------------------------------------')	#60個


import statistics

arr = [580, 600, 680, 620]
#arr = [5, 6, 8, 9]
a = statistics.stdev(arr)
print(a)   # 2.7386127875258306


print('------------------------------------------------------------')	#60個

import statistics
from statistics import mean

import statistics

arr = [1, 2, 3, 4, 5, 6, 7, 8]
a = statistics.mean(arr)    # 計算平均值
print(a)                    # 4.5

print('------------------------------------------------------------')	#60個
import statistics

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = statistics.pstdev(arr)
b = statistics.pvariance(arr)
print(a)   # 2.581988897471611
print(b)   # 6.666666666666667



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

"""
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
"""

print('------------------------------------------------------------')	#60個

import statistics

sc = [60,10,40,80,80,30,80,60,70,90,50,50,50,70,60,80,80,50,60,70,
      70,40,30,70,60,80,20,80,70,50,90,80,40,40,70,60,80,30,20,70]
print(f'平均成績 = {np.mean(sc)}')
print(f'中位成績 = {np.median(sc)}')
print(f'眾數成績 = {statistics.mode(sc)}')

"""
plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.hist(sc, 9)

plt.ylabel('學生人數')
plt.xlabel('分數')
plt.title('成績表')

plt.show()
"""

print('------------------------------------------------------------')	#60個

import statistics

sc1 = [60,10,40,80,80,30,80,60,70,90,50,50,50,70,60,80,80,50,60,70,
      70,40,30,70,60,80,20,80,70,50,90,80,40,40,70,60,80,30,20,70]

sc2 = [50,10,60,80,70,30,80,60,30,90,50,50,90,70,60,50,80,50,60,70,
      60,50,30,70,70,80,10,80,70,50,90,80,40,50,70,60,80,40,20,70]

"""
plt.rcParams['font.family'] = 'Microsoft JhengHei'

plt.hist([sc1,sc2],9)

plt.ylabel('學生人數')
plt.xlabel('分數')
plt.title('成績表')

plt.show()
"""

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


