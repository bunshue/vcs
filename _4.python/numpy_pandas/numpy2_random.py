# 只使用numpy

"""

np.random.seed()
np.random.rand()
np.random.randn()
np.random.randint(num1, num2)
np.random.choice
np.random.randrange 無
np.random.normal
np.random.uniform(num1, num2)
np.random.sample
np.random.shuffle
np.random.其他

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

print("---- 用 numpy 做的random ------------------------------------")  # 40個

print("---- np.random.seed() ST ------------------------------------")  # 40個

print("固定亂數種子 random seed")
np.random.seed(5)

# Fixing random state for reproducibility
np.random.seed(20060311)
np.random.seed(1234567)
np.random.seed(10**7)

print("---- np.random.seed() SP ------------------------------------")  # 40個

print("---- np.random.rand() ST ------------------------------------")  # 40個

print("產生 0~1之間的隨機浮點數")

# 產生一個多維陣列 0 ~ 1 的隨機數 ( 不包含 1 )
print("np.random.rand() 範圍 0 < r < 1 之小數")

print("建立 1 個隨機數")
cc = np.random.rand()
print(cc)

print("建立 6 個隨機數 一維陣列")
N = 6
cc = np.random.rand(N)
print(cc)

print("建立 10x6 個隨機數 二維陣列")
M, N = 4, 3
A = np.random.rand(M, N)
print(A)

print("最大值 : ", np.max(A))
print("最小值 : ", np.min(A))
print("平均值 : ", np.mean(A))
print("中間值 : ", np.median(A))

M, N, P = 4, 3, 2
A = np.random.rand(M, N, P)
print(A)


c = np.random.randint(5, 10, size=5)
print("np.random.randint(5,10,size=5)")
print(c)
d = np.random.randint(5, 10, size=(2, 3))
print("np.random.randint(5,10,size=(2,3))")
print(d)

print("---- np.random.rand() SP ------------------------------------")  # 40個

print("---- np.random.randn() ST ------------------------------------")  # 40個

# 如果只是想返回一個隨機數，可使用 randn()
# randn 的用法和 rand 類似，也可從標準正態分佈中產生多維陣列隨機數
# https://wiki.mbalib.com/zh-tw/%E6%AD%A3%E6%80%81%E5%88%86%E5%B8%83
cc = np.random.randn()
print(cc)

print("2.產生2x3常態分佈的隨機浮點數\n", np.random.randn(2, 3))

print("常態分布 一維 N = 6")

# 由一個平均為0，變異數為1的高斯分布中隨機取點，並以list儲存。

N = 6
cc = np.random.randn(N)
print(cc)

print("常態分布 二維 5 X 3")
M, N = 5, 3
cc = np.random.randn(M, N)
print(cc)

# numpy.random.randn
# sigma * np.random.randn(...) + mu

s = 3 + 2.5 * np.random.randn(2, 4)
print(s)

print("------------------------------")  # 30個

print("常態分布 一維 N = 1000 統計資料")

N = 1000
cc = np.random.randn(N)

print("型態 : ", type(cc))
print("長度 : ", len(cc))
print("最大 : ", cc.max())
print("最小 : ", cc.min())
print("最大 : ", max(cc))
print("最小 : ", min(cc))
print("平均 : ", cc.mean())
print("標準差 : ", cc.std())

print("------------------------------------------------------------")  # 60個

"""
x = np.random.randn(N, 3)
colors = ["red", "green", "blue"]
plt.hist(x, num_bins, density=True, histtype="bar", color=colors, label=colors)
plt.legend(prop={"size": 10})
plt.title("一次顯示三組數據", fontweight="bold")


print("以直方圖顯示常態分佈")
# 生成 N 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
x = np.random.randn(N)  # 常態分佈數字
plt.hist(x, bins=num_bins, color="r", alpha=0.3)

plt.title("np.random.randn")
"""

print("---- np.random.randn() SP ------------------------------------")  # 40個

print("---- np.random.randint() ST ------------------------------------")  # 40個

print("建立 ST ~ SP 間的隨機整數(不含尾)")

ST, SP = 10, 20

cc = np.random.randint(SP)
print(cc)

cc = np.random.randint(ST, SP)
print(cc)

print("建立 3 個 0-9(含) 的整數隨機數")
cc = np.random.randint(10, size=3)
print(cc)

print("一維陣列 N 個, ST ~ SP 間的隨機整數(不含尾)")
N = 10
cc = np.random.randint(ST, SP, N)
print(cc)

print("建立 3x2 個0-9(含) 的整數隨機數")
cc = np.random.randint(0, 10, size=(3, 2))
print(cc)

print("回傳單3*5陣列, 值是0(含)至10(不含)的隨機數")
print("二維鎮列 MXN 個, 0 ~ SP 間的隨機整數(不含尾)")
cc = np.random.randint(SP, size=(3, 5))
print(cc)

print("np亂數建立二維陣列 1 ~ 7(不含尾), 6X4")
cc = np.random.randint(ST, SP, (6, 4))
print(cc)

cc = np.random.randint(10, size=(4, 3))  # 數值0~9, size : 4X3
print("shape :", cc.shape)
print(cc)

cc = np.random.randint(ST, SP, size=5)
print(cc)

cc = np.random.randint(ST, SP, size=(2, 3))
print(cc)

cc = np.random.randint(SP, size=10)
print(cc)

print("統計資料")
cc = np.random.randint(100, size=50)
print("陣列的內容：", cc)
print("1.標準差：", np.std(cc))
print("2.變異數：", np.var(cc))
print("3.中位數：", np.median(cc))
print("4.百分比值：", np.percentile(cc, 80))
print("5.最大最小差值：", np.ptp(cc))

print("------------------------------------------------------------")  # 60個

cc = np.random.randint(ST, SP, (3, 5))
print("原陣列內容：")
print(cc)
print("將每一直行進行排序：")
print(np.sort(cc, axis=0))
print("將每一橫列進行排序：")
print(np.sort(cc, axis=1))

print("------------------------------------------------------------")  # 60個

N = 10
cc = np.random.randint(ST, SP, N)
print(cc)
print(np.unique(cc))  # unique統計陣列中所有不同的值
print(np.bincount(cc))  # bincount統計整數陣列中每個元素出現的次數

print("------------------------------------------------------------")  # 60個

"""
#由low到high中產生一個size大小的list。 dtype，一般來說我們不會動到
np.random.randint(low, high, size, dtype='l')

插播一下, 平常我們要從一個平均值是 0, 標準差是 1 的常態分布中, 隨機取幾個數出來似乎有點困難。但我們打開封印後, 這件事很簡單!
我們可以取整數亂數

np.random.randint(a,b)
樣取出的數字 k 會介於:
a <= k < b

k = np.random.randint(1,101)
1~100

"""

print("------------------------------------------------------------")  # 60個

print("創建數組 Random.randint")
# 在一个范围内生成n个随机整数样本。
# np.random.randint(low, high = None, size = None, dtype = int)
na = np.random.randint(5, 10, 10)
print(na)

a = np.random.randint(0, 5, 10)
print(a)
print(np.unique(a))
print(np.bincount(a))
print(np.histogram(a, bins=5))

# 產生隨機整數，也可用 size 產生多維陣列隨機數
d = np.random.randint(1, 100, 10)
print(d)
e = np.random.randint(1, 100, size=(2, 2, 3))
print(e)

print("---- np.random.randint() SP ------------------------------------")  # 40個

print("---- np.random.choice() ST ------------------------------------")  # 40個

print("在名詞字串中隨機選取一個字串")
# animals = list("鼠牛虎兔龍蛇")
animals = ["鼠", "牛", "虎", "兔", "龍", "蛇"]
for _ in range(10):
    animal = np.random.choice(animals)
    print(animal)

print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔", "龍", "蛇"]
animals1 = np.random.choice(animals, 3)
print("隨機挑選 3 種動物")
print(animals1)

animals2 = np.random.choice(animals, 5)
print("隨機挑選 5 種動物 -- 可以重複")
print(animals2)

animals3 = np.random.choice(animals, 5, replace=False)
print("隨機挑選 5 種動物 -- 不可以重複")
print(animals3)

print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔", "龍", "蛇"]
animals1 = np.random.choice(animals, 5, p=[0.2, 0.6, 0.05, 0.05, 0.05, 0.05])
print("依權重挑選 5 種動物")
print(animals1)

animals2 = np.random.choice(animals, 5, p=[0.05, 0.05, 0.05, 0.05, 0.3, 0.5])
print("依權重挑選 5 種動物")
print(animals2)

print("------------------------------------------------------------")  # 60個

print("6.產生0~4(不含5)2x3的隨機整數\n", np.random.choice(5, [2, 3]))
print("7.產生0~42(不含43)6個不重複的隨機整數\n", np.random.choice(43, 6, replace=False))

animals = ["鼠", "牛", "虎", "兔", "龍", "蛇"]
cc = np.random.choice(animals, 5)
print(cc)

"""
#size = np.random.choice(np.arange(100), 100)
"""

print("------------------------------------------------------------")  # 60個

a = np.random.choice(50, size=10, replace=False)
print("排序前的陣列：", a)
print("排序後的陣列：", np.sort(a))
print("排序後的索引：", np.argsort(a))
# 用索引到陣列取值
for i in np.argsort(a):
    print(a[i], end=",")

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

print("---- np.random.choice() SP ------------------------------------")  # 40個

print("---- np.random.randrange() ST ------------------------------------")  # 40個

print("---- np.random.randrange() SP ------------------------------------")  # 40個

print("---- np.random.normal() ST ------------------------------------")  # 40個

N = 10
cc = np.random.normal(0, 1, N)
print(cc)

# 使用 NumPy 隨機數的「常態分佈」產生 N 個數據點
N = 10
cc = np.random.normal(5, 50, N)
print(cc)

cc = np.random.normal(3, 2.5, size=(2, 4))
print(cc)


x = np.random.normal(1, 4, (3, 5))
y = np.argmax(x, axis=1)
print(x)
print(x.shape)
print(y)
print(y.shape)

print("查詢函數用法")
help(np.max)

print("------------------------------------------------------------")  # 60個

"""
x1 = np.random.normal(mu, sigma, size=N*10)  # 隨機數

# list 移除資料的寫法
x2 = x1[x1 <= 100.0]
x2 = x2[x2 >= 0]
"""

# 過濾資料

"""
scores1 = np.random.normal(mu, sigma, size=N)  # 隨機數
print("資料個數1 :", len(scores1))
print("最高分 :", max(scores1))
print("最低分 :", min(scores1))

scores2 = scores1[scores1 <= 100.0]
scores3 = scores2[scores2 >= 0.0]
"""

print("---- np.random.normal() SP ------------------------------------")  # 40個

print("---- np.random.uniform() ST ------------------------------------")  # 40個

for _ in range(50):
    cc = np.random.uniform()
    print(cc)

print("創建數組 Uniform")
# np.uniform(low = 0.0, high = 1.0, size = None)
# 在上下限之间的均匀分布中生成随机样本。

na = np.random.uniform(5, 10, size=4)
print(na)

na = np.random.uniform(size=5)
print(na)

na = np.random.uniform(size=(2, 3))
print(na)

print("------------------------------------------------------------")  # 60個

print("---- np.random.uniform() SP ------------------------------------")  # 40個

print("---- np.random.sample() ST ------------------------------------")  # 40個

print("---- np.random.sample() SP ------------------------------------")  # 40個

print("---- np.random.shuffle() ST ------------------------------------")  # 40個

animals = ["鼠", "牛", "虎", "兔", "龍", "蛇"]

print("原list")
print(animals)

print("shuffle list")
np.random.shuffle(animals)
print(animals)

print("再 shuffle list")
np.random.shuffle(animals)
print(animals)

print("再 shuffle list")
np.random.shuffle(animals)
print(animals)


"""index = []
ran = random.sample(range(0, 10),2)
for i in ran:
    index.append(i)
index.sort()
"""

print("------------------------------------------------------------")  # 60個

print("一維陣列之shuffle")
cc = np.arange(20)  # 0 1 2 ... 20
print("初")
print(cc)
np.random.shuffle(cc)  # 重新排列
print("末")
print(cc)

print("二維陣列之shuffle")
cc = np.arange(25).reshape((5, 5))
print("初")
print(cc)
np.random.shuffle(cc)  # 重新排列
print("末")
print(cc)

print("------------------------------------------------------------")  # 60個

print("---- np.random.shuffle() SP ------------------------------------")  # 40個

print("---- np.random.其他 ST ------------------------------------")  # 40個

print("綜合比較")  # 60個

print("3.產生0~4(不含5)隨機整數\n", np.random.randint(5))
print("4.產生2~4(不含5)5個隨機整數\n", np.random.randint(2, 5, [5]))
print(
    "5.產生3個 0~1之間的隨機浮點數\n",
    np.random.random(3),
    "\n",
    np.random.random_sample(3),
    "\n",
    np.random.sample(3),
)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("統計函數")
a = np.arange(10, 0, -1)
print(a)
print(a.mean())
print(a.var())
print(a.std())
print(np.average(a, weights=np.arange(0, 10, 1)))
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

print("------------------------------------------------------------")  # 60個

# mu + sigma * np.random.standard_normal(size=...)
# np.random.normal(mu, sigma, size=...)

for _ in range(10):
    cc = np.random.standard_normal()
    print(cc)

s = np.random.standard_normal(8000)
print(s)
print(s.shape)

s = np.random.standard_normal(size=(3, 4, 2))
print(s)
print(s.shape)


# mean 3 and standard deviation 2.5:
mu = 3
sigma = 2.5

s = mu + sigma * np.random.standard_normal(size=(2, 4))
print(s)
print(s.shape)

print("------------------------------------------------------------")  # 60個

"""
print('round 將浮點值四舍五入到指定數目的小數點。')
#np.round(a, decimals = 0, out = None)
#decimals:要保留的小數點的個數。

cc = np.round(a,decimals = 0)
print(cc)

cc = np.round(a,decimals = 1)
print(cc)
"""

print("------------------------------------------------------------")  # 60個

# numpy.random.RandomState的用法
rng = np.random.RandomState(0)  # 偽隨機數產生器, 類似random.seed, 但語法不一樣

N = 6
cc = rng.randn(N)
print(cc)

rng = np.random.RandomState(42)  # 固定random seed
# print(rng)

generator = np.random.RandomState(1)  # 隨機數種子

# numpy random generator
numpy_rng = np.random.RandomState(123)

print("------------------------------------------------------------")  # 60個

# np.random.random_sample ST

# 產生一個 0~1 的隨機數
r1 = np.random.random_sample()
print(r1)
r2 = np.random.random_sample((2, 2))
print(r2)

# np.random.random_sample SP


# np.random.random ST

N = 6
cc = np.random.random(N)
print(cc)

cc = np.random.random(size=(3, 4))
print(cc)

cc = np.mat(np.random.random((2, 2)))
print(cc)

cc = np.random.random((2, 2))
print(cc)

# np.random.random SP

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


MIN = 1
MAX = 6
for _ in range(10):
    print(random.randint(MIN, MAX), end=" ")
print()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("畫圖類")

N = 30
plt.plot(np.random.randn(N))
# plt.plot(range(N), np.random.randn(N))  #same
plt.scatter(range(N), np.random.randn(N))

plt.show()

print("------------------------------------------------------------")  # 60個


# numpy.random.uniform
# random.uniform(low=0.0, high=1.0, size=None)

s = np.random.uniform(-1, 0, 10)
print(s)
count, bins, ignored = plt.hist(s, 15, density=True)
plt.plot(bins, np.ones_like(bins), linewidth=2, color="r")
plt.show()


print("------------------------------------------------------------")  # 60個

# np.random.normal

mu, sigma = 0, 0.1  # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)

"""
Verify the mean and the variance:
abs(mu - np.mean(s))
0.0  # may vary

abs(sigma - np.std(s, ddof=1))
0.1  # may vary
"""
count, bins, ignored = plt.hist(s, 30, density=True)

plt.plot(
    bins,
    1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((bins - mu) ** 2) / (2 * sigma**2)),
    linewidth=2,
    color="r",
)

plt.show()

print("------------------------------------------------------------")  # 60個

dice = [1, 2, 3, 4, 5, 6]
population = []
for x in range(10000):
    sample = np.random.choice(a=dice, size=100)
    population.append(sample.mean())
print("母體平均數:", sum(population) / 10000.0)

size_range = [10, 100, 1000]
for sample_size in size_range:
    sample = np.random.choice(a=population, size=sample_size)
    sample_mean = sample.mean()
    print(sample_size, "樣本平均數:", sample_mean)

print("------------------------------------------------------------")  # 60個

population = (
    (["臺灣閩南語"] * 7330) + (["臺灣客家語"] * 1200) + (["其他漢語方言"] * 1300) + (["原住民語"] * 170)
)
sample_size = 1000
sample = random.sample(population, sample_size)
for lang in set(sample):
    print(lang + "比例估計:", sample.count(lang) / sample_size)

print("------------------------------------------------------------")  # 60個

"""
1. 隨機變數
np.random.randn(size)：由一個平均為0，變異數為1的高斯分布中隨機取點，並以list儲存。
np.random.randint(low, high, size, dtype='l')：由low到high中產生一個size大小的list。 dtype，一般來說我們不會動到

random.random()：在0 <= output < 1之間產生一個浮點數
random.uniform(low,hight)：在low<= output <=hight之間產生一個浮點數
random.randint(low,hight)：在low<= output <=hight之間產生一個整數
"""

print(np.random.randn(6))
# output:[ 1.3265288  -0.15050998 -0.59429709  0.6356734  -0.89041176  0.2790698]

print(np.random.randn(2, 3))
# output:[[-0.51469048 -0.82356942  0.80310762]
#        [ 0.21914897 -0.04437828 -0.41106366]]

print(np.random.randint(1, 10, 6))
# output: [[4 6 7],[4 2 9]]

print("------------------------------------------------------------")  # 60個

print("2.產生2x3常態分佈的隨機浮點數\n", np.random.randn(2, 3))
print("3.產生0~4(不含5)隨機整數\n", np.random.randint(5))
print("4.產生2~4(不含5)5個隨機整數\n", np.random.randint(2, 5, [5]))
print(
    "5.產生3個 0~1之間的隨機浮點數\n",
    np.random.random(3),
    "\n",
    np.random.random_sample(3),
    "\n",
    np.random.sample(3),
)
print("6.產生0~4(不含5)2x3的隨機整數\n", np.random.choice(5, [2, 3]))
print("7.產生0~42(不含43)6個不重複的隨機整數\n", np.random.choice(43, 6, replace=False))


print("------------------------------------------------------------")  # 60個

v1 = np.random.random()
v2 = np.random.random()
print(v1, v2)
v3 = np.random.randint(5, 10)
v4 = np.random.randint(1, 101)
print(v3, v4)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
