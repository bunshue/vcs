'''
統計專用

'''

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


'''
print(np.std(arr, ddof = 1))#this

print('------------------------------------------------------------')	#60個


import statistics

arr = [580, 600, 680, 620]
#arr = [5, 6, 8, 9]
a = statistics.stdev(arr)
print(a)   # 2.7386127875258306

'''


'''

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


'''
print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


