# 只使用numpy

"""
np.random.seed()
np.random.rand()
np.random.randn()
np.random.randint(num1, num2)
np.random.choice
np.random.randrange 無
np.random.uniform(num1, num2)
np.random.sample
np.random.shuffle
np.random.其他

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

print(
    "---- 用 numpy 做的 random --------------------------------------------------------"
)  # 60個

print('---- np.random.seed() ST --------------------------------------------------------')	#60個

print('固定亂數種子 random seed')
np.random.seed(5)

# Fixing random state for reproducibility
np.random.seed(20060311)

np.random.seed(1234567)
np.random.seed(0)
np.random.seed(10**7)

print('---- np.random.seed() SP --------------------------------------------------------')	#60個

print('---- np.random.rand() ST --------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('np.random.rand() 範圍 0 < r < 1 之小數')

print('建立 1 個隨機數')
y = np.random.rand()
print(y)

print('建立 6 個隨機數 陣列')
y = np.random.rand(6)
print(y)
  
print('建立 10x6 個隨機數 二維陣列')
y = np.random.rand(10, 6)
#print(y)

print('最大值 : ', np.max(y))
print('最小值 : ', np.min(y))
print('平均值 : ', np.mean(y))
print('中間值 : ', np.median(y))

print('------------------------------------------------------------')	#60個

N = 50

spread = np.random.rand(N) * 100 #放大100倍 原本0~1 後來 0~100
#print(spread)

center = np.ones(25) * 50
#print(center)

flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low), 0)

plt.boxplot(data)

plt.show()


print('------------------------------------------------------------')	#60個



print('---- np.random.rand() SP --------------------------------------------------------')	#60個


print('---- np.random.randn() ST --------------------------------------------------------')	#60個

print('常態分布 一維 N = 10')

N = 10
y = np.random.randn(N)
print(y)

print('常態分布 二維 5 X 3')
M = 5
N = 3
z = np.random.randn(M, N)
print(z)

print("------------------------------------------------------------")  # 60個

print('常態分布 N = 1000')

N = 1000
y = np.random.randn(N)

print("型態 : ", type(y))
print("長度 : ", len(y))
print("最大 : ", y.max())
print("最小 : ", y.min())
print("最大 : ", max(y))
print("最小 : ", min(y))
print("平均 : ", y.mean())
print("標準差 : ", y.std())

print('------------------------------------------------------------')	#60個

N = 30
plt.plot(np.random.randn(N))
#plt.plot(range(N), np.random.randn(N))  #same
plt.scatter(range(N), np.random.randn(N))

plt.show()


print('------------------------------------------------------------')	#60個


print('---- np.random.randn() SP --------------------------------------------------------')	#60個

print('---- np.random.randint() ST --------------------------------------------------------')	#60個


a = np.random.randint(0, 10, (3, 5))
print('原陣列內容：')
print(a)
print('將每一直行進行排序：')
print(np.sort(a, axis = 0))
print('將每一橫列進行排序：')
print(np.sort(a, axis = 1))

print('------------------------------------------------------------')	#60個

c = np.random.randint(5, 10, size = 5)
print(c)
d = np.random.randint(5, 10, size = (2, 3))
print(d)

x = np.random.randint(10, size=10)
print(x)

a = np.random.randint(100,size=50)
print('陣列的內容：', a)
print('1.標準差：', np.std(a))
print('2.變異數：', np.var(a))
print('3.中位數：', np.median(a))
print('4.百分比值：', np.percentile(a, 80))
print('5.最大最小差值：', np.ptp(a))

print('------------------------------------------------------------')	#60個

print("回傳值是10(含)至20(不含)的單一隨機數")
x1 = np.random.randint(10, 20)
print(x1)

print("回傳一維陣列10個元素, 值是1(含)至5(不含)的隨機數")
x2 = np.random.randint(1, 5, 10)
print(x2)

print("回傳單3*5陣列, 值是0(含)至10(不含)的隨機數")
x3 = np.random.randint(10, size=(3, 5))     
print(x3)

print('------------------------------------------------------------')	#60個

print('建立 1 個 0-4(含) 的整數隨機數')
x = np.random.randint(5)
print(x)

print('建立 3 個 0-9(含) 的整數隨機數')
x = np.random.randint(10,size=3)
print(x)

print('建立 3x2 個0-9(含) 的整數隨機數')
x = np.random.randint(0, 10, size=(3,2))
print(x)

print('------------------------------------------------------------')	#60個

print("np亂數建立一維陣列 1 ~ 7(不含尾), 300個")
a = np.random.randint(1, 7, 300)
print(a)

print("np亂數建立二維陣列 1 ~ 7(不含尾), 6X4")
a = np.random.randint(1, 7, (6, 4))
print(a)

print('------------------------------------------------------------')	#60個

a = np.random.randint(0, 5, 10)
print(a)
print(np.unique(a))  # unique統計陣列中所有不同的值

print(np.bincount(a))  # bincount統計整數陣列中每個元素出現的次數

print('------------------------------------------------------------')	#60個



print('---- np.random.randint() SP --------------------------------------------------------')	#60個


print('---- np.random.choice() ST --------------------------------------------------------')	#60個

print('在名詞字串中隨機選取一個字串')
#animals = list("鼠牛虎兔龍蛇")
animals = ['鼠', '牛', '虎', '兔', '龍', '蛇']
for _ in range(10):
    animal = np.random.choice(animals)
    print(animal)

print('------------------------------------------------------------')	#60個

animals = ['鼠', '牛', '虎', '兔', '龍', '蛇']
animals1 = np.random.choice(animals,3)
print("隨機挑選 3 種動物")
print(animals1)

animals2 = np.random.choice(animals,5)
print("隨機挑選 5 種動物 -- 可以重複")
print(animals2)
    
animals3 = np.random.choice(animals,5,replace=False)
print("隨機挑選 5 種動物 -- 不可以重複")
print(animals3)

print('------------------------------------------------------------')	#60個

animals = ['鼠', '牛', '虎', '兔', '龍', '蛇']
animals1 = np.random.choice(animals,5,p=[0.2,0.6,0.05,0.05,0.05,0.05])
print("依權重挑選 5 種動物")
print(animals1)

animals2 = np.random.choice(animals,5,p=[0.05,0.05,0.05,0.05,0.3,0.5])
print("依權重挑選 5 種動物")
print(animals2)

print('------------------------------------------------------------')	#60個

a = np.random.choice(50, size=10, replace=False)
print('排序前的陣列：', a)
print('排序後的陣列：', np.sort(a))
print('排序後的索引：', np.argsort(a))
#用索引到陣列取值
for i in np.argsort(a):
    print(a[i], end=',')

print("------------------------------------------------------------")  # 60個

rawdata = """我
我的
眼睛
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止"""
words = rawdata.split("\n")


def poem():
    n = np.random.randint(2, 8)  # 2-8句, 決定有幾句

    for _ in range(n):
        m = np.random.randint(1, 6)  # 決定每句的長度
        sentence = np.random.choice(words, m, replace=False)
        print(" ".join(sentence))

poem()

print("------------------------------------------------------------")  # 60個



print('---- np.random.choice() SP --------------------------------------------------------')	#60個

print('---- np.random.randrange() ST --------------------------------------------------------')	#60個


print('---- np.random.randrange() SP --------------------------------------------------------')	#60個


print('---- np.random.uniform() ST --------------------------------------------------------')	#60個

for _ in range(50):
    a = np.random.uniform()
    print(a)

print("------------------------------------------------------------")  # 60個

print('---- np.random.uniform() SP --------------------------------------------------------')	#60個

print('---- np.random.sample() ST --------------------------------------------------------')	#60個


print('---- np.random.sample() SP --------------------------------------------------------')	#60個


print('---- np.random.shuffle() ST --------------------------------------------------------')	#60個

animals = ['鼠', '牛', '虎', '兔', '龍', '蛇']

print('原list')
print(animals)

print('shuffle list')
np.random.shuffle(animals)
print(animals)

print('再 shuffle list')
np.random.shuffle(animals)
print(animals)

print('再 shuffle list')
np.random.shuffle(animals)
print(animals)


"""index = []
ran = random.sample(range(0, 10),2)
for i in ran:
    index.append(i)
index.sort()
"""

print('------------------------------------------------------------')	#60個

print("一維陣列之shuffle")
arr1 = np.arange(20)    # 0 1 2 ... 20
print('初')
print(arr1)
np.random.shuffle(arr1)         # 重新排列
print("末")
print(arr1)

print("二維陣列之shuffle")
arr2 = np.arange(25).reshape((5,5))
print('初')
print(arr2)
np.random.shuffle(arr2)         # 重新排列
print("末")
print(arr2)

print('------------------------------------------------------------')	#60個



print('---- np.random.shuffle() SP --------------------------------------------------------')	#60個


print('---- np.random.其他 ST--------------------------------------------------------')	#60個

print('綜合比較')	#60個

print('1.產生2x3 0~1之間的隨機浮點數\n', np.random.rand(2,3))
print('2.產生2x3常態分佈的隨機浮點數\n', np.random.randn(2,3))
print('3.產生0~4(不含5)隨機整數\n', np.random.randint(5))
print('4.產生2~4(不含5)5個隨機整數\n', np.random.randint(2,5,[5]))
print('5.產生3個 0~1之間的隨機浮點數\n',
      np.random.random(3),'\n',
      np.random.random_sample(3),'\n',
      np.random.sample(3))
print('6.產生0~4(不含5)2x3的隨機整數\n', np.random.choice(5,[2,3]))
print('7.產生0~42(不含43)6個不重複的隨機整數\n', np.random.choice(43,6,replace=False))

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



"""
#由一個平均為0，變異數為1的高斯分布中隨機取點，並以list儲存。
np.random.randn(size)

#由low到high中產生一個size大小的list。 dtype，一般來說我們不會動到
np.random.randint(low, high, size, dtype='l')

print(np.random.randn(6))
#output:[ 1.3265288  -0.15050998 -0.59429709  0.6356734  -0.89041176  0.2790698]

print(np.random.randn(2,3))
#output:[[-0.51469048 -0.82356942  0.80310762]
#        [ 0.21914897 -0.04437828 -0.41106366]]

print(np.random.randint(1,10,6))
#output: [[4 6 7],[4 2 9]]



插播一下, 平常我們要從一個平均值是 0, 標準差是 1 的常態分布中, 隨機取幾個數出來似乎有點困難。但我們打開封印後, 這件事很簡單!
我們可以取整數亂數

np.random.randint(a,b)
樣取出的數字 k 會介於:
a <= k < b

k = np.random.randint(1,101)
1~100

"""

print('------------------------------------------------------------')	#60個

min = 1
max = 6
for _ in range(10):
    print(random.randint(min, max), end = ' ')
print()

print('------------------------------------------------------------')	#60個

x = np.random.normal(1,4,(3,5))
y = np.argmax(x,axis=1)
print(x)
print(x.shape)
print(y)
print(y.shape)
                                                                                                                  
print('查詢函數用法')
help(np.max)

print("------------------------------------------------------------")  # 60個


"""

np.random.randint(1,15,6)
np.random.randint(0, 10)	#np.random之randint不含尾

"""




print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


print('創建數組 Uniform')
#np.uniform(low = 0.0, high = 1.0, size = None)
#在上下限之间的均匀分布中生成随机样本。

na = np.random.uniform(5, 10, size = 4)
print(na)
 
na = np.random.uniform(size = 5)
print(na)
 
na = np.random.uniform(size = (2, 3))
print(na)

print('創建數組 Random.randint')
#在一个范围内生成n个随机整数样本。
#np.random.randint(low, high = None, size = None, dtype = int)
na = np.random.randint(5, 10, 10)
print(na)

print('創建數組 Random.random')
#生成N个随机浮点数样本。
#np.random(size = None)
N = 10
na = np.random.random(N)
print(na)




print("統計函數")
a=np.arange(10,0,-1)
print(a)
print(a.mean())
print(a.var())
print(a.std())
print(np.average(a, weights=np.arange(0,10,1)))
print(np.median(a))
print(np.percentile(a, 75))


print(a.min())
print(a.max())
print(a.ptp())
print(a.argmin())
print(a.argmax())
print(a.argsort())
a.sort()
print(a)

a=np.random.randint(0,5,10)
print(a) 
print(np.unique(a)) 
print(np.bincount(a)) 
print(np.histogram(a,bins=5))

print("------------------------------------------------------------")  # 60個

a = np.mat(np.random.random((2,2)))
print(a)



print("------------------------------------------------------------")  # 60個


print('常態分布 二維 轉 df')
df3 = pd.DataFrame(np.random.randn(3,3), columns=list("ABC"))


print("------------------------------------------------------------")  # 60個


e = np.random.random((2,2)) # Create an array (lled with random values
print(e) # Might print "[[ 0.91940167 0.08143941]
# [ 0.68744134 0.87236687]]"


print("------------------------------------------------------------")  # 60個

# 產生一個 0~1 的隨機數
r1 = np.random.random_sample()
print(r1)
r2 = np.random.random_sample((2, 2))
print(r2)

# 產生一個多維陣列 0 ~ 1 的隨機數 ( 不包含 1 )
# 一樣有 seed 概念，seed 相同產生的隨機數就相同
a = np.random.rand(4, 3)
print(a)
b = np.random.rand(4, 3, 2)
print(b)

# 如果只是想返回一個隨機數，可使用 randn()
# randn 的用法和 rand 類似，也可從標準正態分佈中產生多維陣列隨機數
# https://wiki.mbalib.com/zh-tw/%E6%AD%A3%E6%80%81%E5%88%86%E5%B8%83
c = np.random.randn()
print(c)

# 產生隨機整數，也可用 size 產生多維陣列隨機數
d = np.random.randint(1, 100, 10)
print(d)
e = np.random.randint(1, 100, size=(2, 2, 3))
print(e)

print("------------------------------------------------------------")  # 60個

# cc = np.random.randint(3, 5)

print("亂數分佈二維陣列")
cc = np.random.rand(3, 5)
print(cc)

print("常態分佈二維陣列")
cc = np.random.randn(3, 5)
print(cc)

print('------------------------------------------------------------')	#60個

#mu + sigma * np.random.standard_normal(size=...)
#np.random.normal(mu, sigma, size=...)

for _ in range(10):
    cc = np.random.standard_normal()
    print(cc)

s = np.random.standard_normal(8000)
print(s)
print(s.shape)

s = np.random.standard_normal(size=(3, 4, 2))
print(s)
print(s.shape)


#mean 3 and standard deviation 2.5:
mu = 3
sigma = 2.5

s = mu + sigma * np.random.standard_normal(size=(2, 4))
print(s)
print(s.shape)



print('------------------------------------------------------------')	#60個

#numpy.random.normal

mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)


"""
Verify the mean and the variance:
abs(mu - np.mean(s))
0.0  # may vary

abs(sigma - np.std(s, ddof=1))
0.1  # may vary

"""
count, bins, ignored = plt.hist(s, 30, density=True)

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')

plt.show()

s = np.random.normal(3, 2.5, size=(2, 4))
print(s)



print('------------------------------------------------------------')	#60個

#numpy.random.randn
#sigma * np.random.randn(...) + mu

s = 3 + 2.5 * np.random.randn(2, 4)
print(s)

print('------------------------------------------------------------')	#60個

#numpy.random.uniform
#random.uniform(low=0.0, high=1.0, size=None)

s = np.random.uniform(-1,0,10)
print(s)


count, bins, ignored = plt.hist(s, 15, density=True)

plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

cc = np.random.random(size = (3, 4))
print(cc)

cc = np.random.randint(10, size = (4, 3))  # 數值0~9, size : 4X3
print('shape :', cc.shape)
print(cc)

"""
print('round 將浮點值四舍五入到指定數目的小數點。')
#np.round(a, decimals = 0, out = None)
#decimals:要保留的小數點的個數。

cc = np.round(a,decimals = 0)
print(cc)

cc = np.round(a,decimals = 1)
print(cc)
"""

print('------------------------------------------------------------')	#60個

"""
np.gradient(f) 計算數組f中元素的梯度，當f為多維時，返回每個維度梯度
梯度：連續值之間的變化率，即斜率
XY坐標軸連續三個X坐標對應的Y軸值：a, b, c，其中，b的梯度是： (c‐a)/2
"""
na = np.random.randint(0, 50, (11))
print(na)
print(np.gradient(na))

print('------------------------------------------------------------')	#60個

#建立陣列

cc = np.array([1, 2, 3])
print(cc)

print('不固定亂數種子')
X = np.random.randn(5)
Y = np.random.randn(5)

print('X:', X)
print('Y:', Y)

print('固定亂數種子')
np.random.seed(0)
X = np.random.randn(5)

np.random.seed(0)
Y = np.random.randn(5)

print('X (seed=0):', X)
print('Y (seed=0):', Y)

#X: [-0.89002049  0.30911242 -0.69646098 -0.68680865  0.54940027]
#Y: [-0.11053683  0.81934032 -1.48607749 -1.10757407  0.24476998]

#X (seed=0): [1.76405235 0.40015721 0.97873798 2.2408932  1.86755799]
#Y (seed=0): [1.76405235 0.40015721 0.97873798 2.2408932  1.86755799]

print('------------------------------------------------------------')	#60個

# arr1
arr1 = np.random.randint(0, 11, (5, 2))
print('arr1:')
print(arr1)

# arr2
arr2 = np.random.rand(3)
print('arr2:')
print(arr2)

print('------------------------------------------------------------')	#60個

np.random.seed(0)
x = ['蘋果', '橘子', '香蕉', '鳳梨', '奇異果', '草莓']
print(np.random.choice(x, 5))

#['奇異果' '草莓' '蘋果' '鳳梨' '鳳梨']

print('------------------------------------------------------------')	#60個

"""
x1 = np.random.normal(mu, sigma, size=N*10)  # 隨機數

# list 移除資料的寫法
x2 = x1[x1 <= 100.0]
x2 = x2[x2 >= 0]
"""

#過濾資料

"""
scores1 = np.random.normal(mu, sigma, size=N)  # 隨機數
print("資料個數1 :", len(scores1))
print("最高分 :", max(scores1))
print("最低分 :", min(scores1))

scores2 = scores1[scores1 <= 100.0]
scores3 = scores2[scores2 >= 0.0]
"""

print('------------------------------------------------------------')	#60個

#np.random.rand(M, N)  # random values in a given shape

count = 10
range = 10

xs = np.random.rand(count) * range
print(xs)
#ys = np.random.rand(count) * range
#zs = np.random.rand(count) * range


N = 100
range = 100

xs = np.random.rand(N) * range
ys = np.random.rand(N) * range
zs = np.random.rand(N) * range


print('------------------------------------------------------------')	#60個

N = 10
x = np.random.randn(N)
y = np.random.randn(N)
z = np.random.randn(N)



""" 新進

#size = np.random.choice(np.arange(100), 100)


"""
