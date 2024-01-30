import sys

import random

#只使用numpy

"""
np.random.seed()
np.random.rand()
np.random.randint(num1, num2)
np.random.choice
np.random.randrange
np.random.uniform(num1, num2)
np.random.sample
其他

"""

print('---- 用 numpy 做的 random --------------------------------------------------------')	#60個

import pandas as pd
import numpy as np


print('---- np.random.seed() --------------------------------------------------------')	#60個

print('固定random seed')
np.random.seed(5)

# Fixing random state for reproducibility
np.random.seed(20060311)

print('---- np.random.rand() --------------------------------------------------------')	#60個

a = np.random.rand(5)
print(a)

b = np.random.rand(3, 2)  
print(b)

r = np.random.rand(3, 3)      # 建立一個 3x3 隨機矩陣
print(r)

r = np.random.rand(10)
print(r)

print('最大值 : ', np.max(r))
print('最小值 : ', np.min(r))
print('平均值 : ', np.mean(r))
print('中間值 : ', np.median(r))



print('---- np.random.randint() --------------------------------------------------------')	#60個


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

print('---- np.random.randrange() --------------------------------------------------------')	#60個



print('---- np.random.choice() --------------------------------------------------------')	#60個



print('---- np.random.randrange() --------------------------------------------------------')	#60個


print('---- np.random.uniform() --------------------------------------------------------')	#60個


print('---- np.random.sample() --------------------------------------------------------')	#60個


print('---- np.random. 其他 --------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


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

a = np.random.choice(50, size=10, replace=False)
print('排序前的陣列：', a)
print('排序後的陣列：', np.sort(a))
print('排序後的索引：', np.argsort(a))
#用索引到陣列取值
for i in np.argsort(a):
    print(a[i], end=',')

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


my_array = np.arange(10)  # [0 1 2 3 4]

print('原list')
print(my_array)

print('shuffle list')
np.random.shuffle(my_array)
print(my_array)

print('shuffle list')
np.random.shuffle(my_array)
print(my_array)

print('shuffle list')
np.random.shuffle(my_array)
print(my_array)

sum_my_array = sum(my_array)
print('和')
print(sum_my_array)

"""index = []
ran = random.sample(range(0, 10),2)
for i in ran:
    index.append(i)
index.sort()
"""
print('------------------------------------------------------------')	#60個



import numpy as np

print("回傳值是10(含)至20(不含)的單一隨機數")
x1 = np.random.randint(10, 20)
print(x1)

print("回傳一維陣列10個元素, 值是1(含)至5(不含)的隨機數")
x2 = np.random.randint(1, 5, 10)
print(x2)

print("回傳單3*5陣列, 值是0(含)至10(不含)的隨機數")
x3 = np.random.randint(10, size=(3, 5))     
print(x3)

A = np.random.rand(50)

mydata = np.random.randn(4,3)
df3 = pd.DataFrame(np.random.randn(3,3), columns=list("ABC"))


"""

插播一下, 平常我們要從一個平均值是 0, 標準差是 1 的常態分布中, 隨機取幾個數出來似乎有點困難。但我們打開封印後, 這件事很簡單!

我們可以取整數亂數

np.random.randint(a,b)
樣取出的數字 k 會介於:
a <= k < b

k = np.random.randint(1,101)
1~100





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


"""


print('---- 新進 --------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import numpy as np

N = 5

"""
#plt.plot(np.random.randn(N))
plt.plot(range(N), np.random.randn(N))
plt.scatter(range(N), np.random.randn(N))
"""

ccc = np.random.randn(N)

print(type(ccc))
print(len(ccc))
print(ccc)
print(max(ccc))
print(min(ccc))

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import sys

import numpy as np
import matplotlib.pyplot as plt

import random

print('------------------------------------------------------------')	#60個

min = 1
max = 6
for i in range(10):
    print(random.randint(min, max), end = ' ')
print()

print('------------------------------------------------------------')	#60個

from random import randint

min = 1
max = 6                                         # 骰子有幾面
times = 10000                                   # 擲骰子次數

dice = [0] * 7                                  # 建立擲骰子的串列
for i in range(times):
    data = randint(min, max)
    dice[data] += 1
print(dice)    
del dice[0]                                     # 刪除索引0資料
    
for i, c in enumerate(dice, 1):
    print('{} = {} 次'.format(i, c))
print(dice)
x = [i for i in range(1, max+1)]                # 長條圖x軸座標
width = 0.35                                    # 長條圖寬度
plt.bar(x, dice, width, color='g')              # 繪製長條圖
plt.ylabel('Frequency')
plt.title('Test 10000 times')

plt.show()

print('------------------------------------------------------------')	#60個

print('建立 1 個隨機數')
x = np.random.rand()
print(x)

print('建立 3 個隨機數')
x = np.random.rand(3)
print(x)
    
print('建立 3x2 個隨機數')
x = np.random.rand(3, 2)
print(x)

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


print('------------------------------------------------------------')	#60個

# 一維陣列
arr1 = np.arange(9)
print("一維陣列")
print(arr1)
np.random.shuffle(arr1)         # 重新排列
print("重新排列")
print(arr1)

# 二維陣列
arr2 = np.arange(9).reshape((3,3))
print("二維陣列")
print(arr2)
np.random.shuffle(arr2)         # 重新排列
print("重新排列")
print(arr2)

print('------------------------------------------------------------')	#60個

fruits = ["Apple", "Orange", "Grapes", "Banana", "Mango"]
fruit1 = np.random.choice(fruits,3)
print("隨機挑選 3 種水果")
print(fruit1)

fruit2 = np.random.choice(fruits,5)
print("隨機挑選 5 種水果 -- 可以重複")
print(fruit2)
    
fruit3 = np.random.choice(fruits,5,replace=False)
print("隨機挑選 5 種水果 -- 不可以重複")
print(fruit3)

print('------------------------------------------------------------')	#60個

fruits = ["Apple", "Orange", "Grapes", "Banana", "Mango"]
fruit1 = np.random.choice(fruits,5,p=[0.8,0.05,0.05,0.05,0.05])
print("依權重挑選 5 種水果")
print(fruit1)

fruit2 = np.random.choice(fruits,5,p=[0.05,0.05,0.05,0.05,0.8])
print("依權重挑選 5 種水果")
print(fruit2)


print('------------------------------------------------------------')	#60個


import numpy as np
for i in range(5):
    c = np.random.choice(animals)
    print(f"本次抽中 {c}。")


import numpy as np

a = np.random.randint(0, 5, 10)
print(a)
print(np.unique(a))  # unique統計陣列中所有不同的值

print(np.bincount(a))  # bincount統計整數陣列中每個元素出現的次數

print("------------------------------------------------------------")  # 60個




print("np亂數建立一維陣列 1 ~ 7(不含尾), 300個")
a = np.random.randint(1, 7, 300)
print(a)

print("np亂數建立二維陣列 1 ~ 7(不含尾), 6X4")
a = np.random.randint(1, 7, (6, 4))
print(a)

for _ in range(10):
    a = np.random.uniform()
    print(a)


print("------------------------------------------------------------")  # 60個

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
N = 10
y = np.random.randn(N)

print(y)



print("------------------------------------------------------------")  # 60個

print('從常態分佈抽樣')

N = 100
L = np.random.randn(N)

print(L.mean())
print(L.std())




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

    for i in range(n):
        m = np.random.randint(1, 6)  # 決定每句的長度
        sentence = np.random.choice(words, m, replace=False)
        print(" ".join(sentence))


poem()


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個





N = 50
# fake up some data
spread = np.random.rand(N) * 100
print(spread)
center = np.ones(25) * 50
print(center)
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low), 0)

plt.boxplot(data)

plt.show()


plt.imshow(np.random.randn(100, 100))
plt.show()

print("------------------------------------------------------------")  # 60個

plt.hist(np.random.randn(1000))
plt.show()


"""

np.random.randint(1,15,6)
np.random.randint(0, 10)	#np.random之randint不含尾

"""


