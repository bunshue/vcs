import sys

import random

#只使用numpy

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

print('---- 用 numpy 做的 random --------------------------------------------------------')	#60個

import pandas as pd
import numpy as np

'''
print('---- np.random.seed() ST --------------------------------------------------------')	#60個

print('固定random seed')
np.random.seed(5)

# Fixing random state for reproducibility
np.random.seed(20060311)

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

import matplotlib.pyplot as plt

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

import matplotlib.pyplot as plt

print('畫出 常態分布 一維 N = 1000')
N = 1000
plt.hist(np.random.randn(N))
plt.show()

print('畫出 常態分布 二維 20 X 20')
N = 20
plt.imshow(np.random.randn(N, N))
plt.show()

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


import matplotlib.pyplot as plt

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

sides = 6
# 建立 10000 個 1-6(含) 的整數隨機數
dice = np.random.randint(1,sides+1,size=10000)  # 建立隨機數
    
h = plt.hist(dice, sides)                       # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('Frequency')
plt.title('Test 10000 times')

plt.show()

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

'''
print('---- np.random.uniform() ST --------------------------------------------------------')	#60個

for _ in range(50):
    a = np.random.uniform()
    print(a)

sys.exit()
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

import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

min = 1
max = 6
for _ in range(10):
    print(random.randint(min, max), end = ' ')
print()

print('------------------------------------------------------------')	#60個

x = np.random.normal(1,4,(3,5))
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



