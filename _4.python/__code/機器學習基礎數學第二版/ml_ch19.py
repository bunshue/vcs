import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_1.py

# ch19_1.py

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
print(f'總消費金額 = {sum(x)}')




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_2.py

# ch19_2.py

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
print(f'平均消費金額 = {sum(x)/len(x)}')




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_3.py

# ch19_3.py
import numpy as np

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
print(f'平均消費金額 = {np.mean(x)}')




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_4.py

# ch19_4.py
import numpy as np

x1 = [7, 2, 11, 9, 20]
print(f'中位數 = {np.median(x1)}')

x1 = [30, 7, 2, 11, 9, 20]
print(f'中位數 = {np.median(x1)}')




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_5.py

# ch19_5.py
import numpy as np

x1 = np.array([0, 1, 1, 3, 2, 1])
# 因為 x1 元素最大值是 3, 所以 bin 是 4
print(f'np.bincount = {np.bincount(x1)}')       

x2 = np.array([0, 1, 1, 7, 2, 1])
# 因為 x2 元素最大值是 7, 所以 bin 是 8
print(f'np.bincount = {np.bincount(x2)}') 


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_6.py

# ch19_6.py
import numpy as np

x1 = np.array([0, 1, 1, 3, 2, 1])
# 因為 x1 元素最大值是 3, 所以 bin 是 4
print(f'np.bincount = {np.bincount(x1)}')
print(f'mode        = {np.argmax(np.bincount(x1))}')

x2 = np.array([0, 1, 1, 7, 2, 1])
# 因為 x2 元素最大值是 7, 所以 bin 是 8
print(f'np.bincount = {np.bincount(x2)}') 
print(f'mode        = {np.argmax(np.bincount(x1))}')

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_7.py

# ch19_7.py
import statistics as st

x1 = [0, 1, 1, 3, 2, 1]
print(f'mode = {st.mode(x1)}')
      


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_8.py

# ch19_8.py
import numpy as np
import statistics as st
import matplotlib.pyplot as plt

sc = [60,10,40,80,80,30,80,60,70,90,50,50,50,70,60,80,80,50,60,70,
      70,40,30,70,60,80,20,80,70,50,90,80,40,40,70,60,80,30,20,70]
print(f'平均成績 = {np.mean(sc)}')
print(f'中位成績 = {np.median(sc)}')
print(f'眾數成績 = {st.mode(sc)}')

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

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_9.py

# ch19_9.py
import numpy as np
import statistics as st
import matplotlib.pyplot as plt

sc = [60,10,40,80,80,30,80,60,70,90,50,50,50,70,60,80,80,50,60,70,
      70,40,30,70,60,80,20,80,70,50,90,80,40,40,70,60,80,30,20,70]
print(f'平均成績 = {np.mean(sc)}')
print(f'中位成績 = {np.median(sc)}')
print(f'眾數成績 = {st.mode(sc)}')
plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.hist(sc, 9)

plt.ylabel('學生人數')
plt.xlabel('分數')
plt.title('成績表')
plt.show()



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_10.py

# ch19_10.py
import numpy as np
import statistics as st
import matplotlib.pyplot as plt

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

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_11.py

# ch19_11.py
x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
mean = sum(x) / len(x)

# 計算變異數
myvar = 0
for v in x:
    myvar += ((v - mean)**2)
myvar = myvar / len(x)
print(f"變異數 : {myvar}")


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_12.py

# ch19_12.py
import numpy as np
import statistics as st
x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]

print(f"Numpy模組母體變異數  : {np.var(x):6.2f}")
print(f"Numpy模組樣本變異數  : {np.var(x,ddof=1):6.2f}")
print(f"Statistics母體變異數 : {st.pvariance(x):6.2f}")
print(f"Statistics樣本變異數 : {st.variance(x):6.2f}")



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_13.py

# ch19_13.py

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
mean = sum(x) / len(x)

# 計算變異數
var = 0
for v in x:
    var += ((v - mean)**2)
sd = (var / len(x))**0.5
print(f"標準差 : {sd:6.2f}")






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_14.py

# ch19_14.py
import numpy as np
import statistics as st

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
print(f"Numpy模組母體標準差  : {np.std(x):6.2f}")
print(f"Numpy模組樣本標準差  : {np.std(x,ddof=1):6.2f}")
print(f"Statistics母體標準差 : {st.pstdev(x):6.2f}")
print(f"Statistics樣本標準差 : {st.stdev(x):6.2f}")



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_15.py

# ch19_15.py
import numpy as np
import matplotlib.pyplot as plt

temperature = [25,31,28,22,27,30,29,33,32,26]           # 天氣溫度
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]   # 營業額

print(f"相關係數 = {np.corrcoef(temperature,rev).round(2)}")

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.scatter(temperature, rev)
plt.title('天氣溫度與冰品銷售')
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)
plt.show()





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_16.py

# ch19_16.py
import numpy as np

temperature = [25,31,28,22,27,30,29,33,32,26]           # 天氣溫度
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]   # 營業額 

coef = np.polyfit(temperature, rev, 1)                  # 迴歸直線係數
reg = np.poly1d(coef)                                   # 線性迴歸方程式
print(coef.round(2))
print(reg)              








print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_17.py

# ch19_17.py
import numpy as np

temperature = [25,31,28,22,27,30,29,33,32,26]           # 天氣溫度
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]   # 營業額 

coef = np.polyfit(temperature, rev, 1)                  # 迴歸直線係數
reg = np.poly1d(coef)                                   # 線性迴歸方程式
print(f"當溫度是 35 度時冰品銷售金額 = {reg(35).round(0)}")     












print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_18.py

# ch19_18.py
import numpy as np
import matplotlib.pyplot as plt
temperature = [25,31,28,22,27,30,29,33,32,26]           # 天氣溫度
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]   # 營業額 

coef = np.polyfit(temperature, rev, 1)                  # 迴歸直線係數
reg = np.poly1d(coef)                                   # 線性迴歸方程式
     
plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.scatter(temperature, rev)
plt.plot(temperature,reg(temperature),color='red')
plt.title('天氣溫度與冰品銷售')
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)
plt.show()











print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_19.py

# ch19_19.py
import numpy as np
import matplotlib.pyplot as plt
times = [1,2,3]                                         # 臉書行銷次數
rev = [10,18,19]                                        # 增加業績 

coef = np.polyfit(times, rev, 2)                        # 二次函數係數
reg = np.poly1d(coef)                                   # 二次函數迴歸方程式
print(reg)    
plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.scatter(times, rev)
plt.plot(times,reg(times),color='red')
plt.title('臉書行銷與業績增加金額')
plt.xlabel("臉書行銷次數", fontsize=14)
plt.ylabel("增加業績金額", fontsize=14)
plt.show()











print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_20.py

# ch19_20.py
import numpy as np
import matplotlib.pyplot as plt
temperature = [22,25,26,27,28,29,30,31,32,33]           # 天氣溫度
rev = [600,900,1100,720,950,1020,1000,1200,1420,1500]   # 營業額

coef = np.polyfit(temperature, rev, 2)                  # 迴歸直線係數
reg = np.poly1d(coef)                                   # 線性迴歸方程式
print(reg)     
plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.scatter(temperature, rev)
plt.plot(temperature,reg(temperature),color='red')
plt.title('天氣溫度與冰品銷售')
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)
plt.show()











print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_21.py

# ch19_21.py
import matplotlib.pyplot as plt
import numpy as np

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

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_22.py

# ch19_22.py
import matplotlib.pyplot as plt
import numpy as np

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

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_23.py

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns #海生, 自動把圖畫得比較好看

mu = 0                                                  # 均值
sigma = 1                                               # 標準差
s = np.random.normal(mu, sigma, 10000)                  # 隨機數

count, bins, ignored = plt.hist(s, 30, density=True)    # 直方圖
# 繪製曲線圖
sns.kdeplot(s)

plt.show()












print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_24.py

# ch19_24.py
import matplotlib.pyplot as plt
import numpy as np

s = np.random.uniform(0.0,5.0,size=250)     # 隨機數
plt.hist(s, 5)                              # 直方圖
plt.show()












print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch19\ch19_25.py

# ch19_25.py
import matplotlib.pyplot as plt
import numpy as np

import seaborn as sns #海生, 自動把圖畫得比較好看

s = np.random.uniform(size=10000)           # 隨機數

plt.hist(s, 30, density=True)               # 直方圖

# 繪製曲線圖
sns.kdeplot(s)

plt.show()












print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

