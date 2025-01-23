"""
numpy的使用


"""


"""
numpy的使用

numpy: 數值計算的標準套件

1. 基本建立 np.array
   1.1 自填陣列, 串列轉np陣列
   1.2 自動產生陣列

arr1 = np.array([1, 2, 3, 4, 5])

"""

print("------------------------------")  # 30個

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

print("建立numpy陣列, 串列 轉 numpy陣列")
print("一維")
cc = np.array([1, 2, 3, 4])
print(cc)
print(cc.shape)

print("串列 轉 numpy陣列 int")
cc = np.array([1, 2, 3, 4], dtype=int)
print(cc)

print("串列 轉 numpy陣列 float")
cc = np.array([1, 2, 3, 4], dtype=float)
print(cc)

print("元組 轉 numpy陣列")
cc = np.array((1, 2, 3, 4))
print(cc)

print("------------------------------------------------------------")  # 60個

print("二維串列 轉 numpy陣列")

print("二維陣列 2 X 4")
list2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(list2d)
print(list2d.shape)

list2d = [[1, 2, 3, 4], [5, 6, 7, 8]]
cc = np.array(list2d)
print(cc)
print("維度 :", cc.ndim)
print("形狀 :", cc.shape)
print("數量 :", cc.size)

# 二維，使用 dtype 定義數據類型
list2d = np.array([[1, 2, 3], [5, 6, 7]], dtype=float)
print(list2d)

# 最小維度
list1d = np.array([1, 2, 3], ndmin=3)
print(list1d)

print("------------------------------------------------------------")  # 60個

# 自動產生陣列

# 1. np.arange


# 2. np.linspace


# 3. 其他

print("numpy之基本函數")

print("建立 numpy陣列, 使用 np.arange()")

# 在給定的間隔內返回具有一定步長的整數。
# np.arange(start, stop, step, dtype = None)
# step:數值步長。

cc = np.arange(10)
print(cc)

cc = np.arange(1, 10)
print(cc)

cc = np.arange(0, 11, 3)
print(cc)

cc = np.arange(10, dtype=float)
print(cc)

print("------------------------------------------------------------")  # 60個

print("reshape 它是NumPy中最常用的函數之一。它返回一個數組，其中包含具有新形狀的相同數據。")
# np.reshape(shape)

cc = np.arange(1, 13).reshape(4, 3)  # 一維的 1~9 1X9 改成 二維的 4 X 3
print("shape :", cc.shape)
print(cc)

cc = cc.reshape(3, 4)
print(cc)

"""
#cc = np.arange(0, 16) same
cc = np.arange(16)   # 一維的 1~16 1X16 改成 二維的 4 X 4
print(cc)
cc = cc.reshape(4, 4)
print(cc)

cc = np.arange(1, 10).reshape(3, 3) # 一維的 1~10 1X9 改成 二維的 3 X 3
print(cc)
"""

list2d = np.arange(18).reshape(3, 6)
print(list2d)
print(list2d)
print(list2d[::-1])

h, w = list2d.shape[::]
print(h, w)

w, h = list2d.shape[::-1]
print(w, h)

print("------------------------------------------------------------")  # 60個

print("創建數組 np.linspace()")

# 創建一個具有指定間隔的浮點數的數組。
# np.linspace(start, stop, num=50, endpoint = True, retstep = False, dtype = None, axis = 0)
# start:起始數字
# end:結束
# Num:要生成的樣本數，默認為50。

ST, SP, N = 3, 8, 6  # 從ST到SP共取N個, 包含頭尾
cc = np.linspace(ST, SP, N)
print(cc)

# 使用 linspace 產生數據
cc = np.linspace(1, 10, 10, dtype=int)
print(cc)

cc = np.linspace(1, 2, 10)
print(cc)

print("------------------------------------------------------------")  # 60個

print("建立 numpy陣列, 使用 np.linspace()")

ST, SP, N = 0, 5, 11  # 從ST到SP共取N個, 包含頭尾
cc = np.linspace(ST, SP, N, dtype=float)
print(cc)

cc = np.linspace(ST, SP, num=N)
print(cc)


ST, SP, N = 0, 4, 9  # 從ST到SP共取N個, 包含頭尾
x = np.linspace(-np.pi, np.pi, 5)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.sinc(x)
print("x", x)
print("sin(x) =", y1)
print("cos(x) =", y2)
print("tan(x) =", y3)
print("sinc(x) =", y4)

print("------------------------------------------------------------")  # 60個

print("建立 numpy陣列, 使用 np.logspace()")

# 在對數尺度上生成間隔均勻的數字。
# np.logspace(start, stop, num = 50, endpoint = True, base = 10.0, dtype = None, axis = 0)
# Start:序列的起始值。
# End:序列的最后一個值。
# endpoint:如果為True，最后一個樣本將包含在序列中。
# base:底數。默認是10。

cc = np.logspace(0, 10, 5, base=2)
print(cc)

cc = np.logspace(0, 2, 5)
print(cc)

print("------------------------------------------------------------")  # 60個

print("基本函數 基本運算")

print("使用 numpy函數 對 list / np.array 做處理")
cc = [1, 2, 3, 4]
cc = np.array([[11, 22, 13, 74, 35, 6, 27, 18, 5]])

print("陣列內容 :", cc)
print("最大值 :", np.max(cc))
print("最小值 :", np.min(cc))
print("最大值索引 :", np.argmax(cc))
print("最小值索引 :", np.argmin(cc))
print("平均 :", np.mean(cc))
print("中位數 : ", np.median(cc))
print("和 :", np.sum(cc))

cc = np.array([[-1, 2, 3], [13, 14, 15]])
print(cc)
print(np.sum(cc))  # 輸出46   全部累加
print(np.sum(cc, axis=0))  # 輸出"[12 16 18]" =(-1+13),(2+14),(3+15)
print(np.sum(cc, axis=1))  # 輸出"[ 4 42]" =(-1+2+3),(13+14+15)
print(np.max(cc))  # 最大值 輸出15
print(np.min(cc))  # 最小值 輸出-1
print(np.cumsum(cc))  # 累加[-1  1  4 17 31 46]
# 加權平均值
print(np.average(cc))  # 輸出7.666
# 平均 mean=sum(cc)/len(cc)
print(np.mean(cc))  # 輸出7.666
# 中間值
print(np.median(cc))  # 輸出8.0
# 標準偏差 std = sqrt(mean(abs(cc - cc.mean())**2))
print(np.std(cc))  # 輸出 6.472
# 方差 var = mean(abs(cc - cc.mean())**2)
print(np.var(cc))  # 輸出 41.888
print(cc.T)  # 輸出 [[-1 13] [ 2 14] [ 3 15]]

print("------------------------------------------------------------")  # 60個

my_array = np.arange(101)  # 0 1 2 ... 100

sum_my_array = sum(my_array)
print("和")
print(sum_my_array)


print("串列 轉 numpy陣列")
x = np.array([8, 9, 10, 7, 8, 9, 5, 7, 9, 8])
y = np.array([12, 15, 16, 18, 6, 11, 3, 12, 11, 16])

x_mean = np.mean(x)
y_mean = np.mean(y)

print("------------------------------------------------------------")  # 60個


cc = np.array(range(10))
cc = cc.reshape(5, 2)
print(cc.dtype)
print(cc.size)
print(cc.shape)
print(cc.itemsize)
print(cc.ndim)
print(cc.nbytes)

cc = np.arange(1, 10).reshape(3, 3)
print("陣列的內容：\n", cc)
print("1.最小值與最大值：\n", np.min(cc), np.max(cc))
print("2.每一直行最小值與最大值：\n", np.min(cc, axis=0), np.max(cc, axis=0))
print("3.每一橫列最小值與最大值：\n", np.min(cc, axis=1), np.max(cc, axis=1))
print("4.加總、乘積及平均值：\n", np.sum(cc), np.prod(cc), np.mean(cc))
print(
    "5.每一直行加總、乘積與平均值：\n", np.sum(cc, axis=0), np.prod(cc, axis=0), np.mean(cc, axis=0)
)
print(
    "6.每一橫列加總、乘積與平均值：\n", np.sum(cc, axis=1), np.prod(cc, axis=1), np.mean(cc, axis=1)
)

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3, 4, 5, 6], dtype=np.int64)
print(a.dtype)
a = a.astype(np.float32)
print(a.dtype)
print(a.dtype.type)

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a[0, 0])
print(a[1, 1])

b = [a[0, 0], a[1, 1]]
print(b)

b = a[[0, 0], [1, 1]]
print(b)
print(b[1])
print(a[[0, 1, 2], [0, 1, 0]])

print("------------------------------------------------------------")  # 60個

x = np.array([1, 2])  # numpy自動設定
print(x.dtype)  # 輸出 "int64"

x = np.array([1.0, 2.0])  # numpy自動設定
print(x.dtype)  # 輸出 "float64"

x = np.array([1, 2], dtype=np.int64)  # 設定為int64
print(x.dtype)  # 輸出 "int64"

print("------------------------------------------------------------")  # 60個

A = np.array([[[1, 2, 3], [5, 6, 7]]])

# 取得陣列維度的深度
print(np.ndim(A))

# 依序取得每個維度的數量
print(np.shape(A))

# 修改維度 1,2,3 -> 1,3,2
A.shape = (1, 3, 2)
print(A)

# 也可以使用 reshape，不過不知道為什麼用了之後執行沒問題，但編輯器會報錯
# B = A.reshape(1,2,3)
# print(B)

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2, 3], [4, 5, 6]], int)  # 指定元素型態的陣列
a = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)  # 指定元素型態的陣列
print(a[0, 0], a[0, 1], a[0, 2])
print(a[1, 0], a[1, 1], a[1, 2])

print("陣列元素的資料型態 :", a.dtype)
print("陣列的元素總數", a.size)
print("陣列的形狀", a.shape)
print("陣列元素所占用的拜數", a.itemsize)
print("幾維陣列", a.ndim)
print("整個陣列所占用的拜數", a.nbytes)

print("------------------------------------------------------------")  # 60個

print("陣列的形狀操作 reshape 1")

a = np.array([1, 2, 3, 4, 5, 6])
print(a)
b = a.reshape((3, 2))
print(b)

print("陣列的形狀操作 reshape 2")

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a.reshape((3, 3))
print(b)

c = b.flatten()
print(c)

print("------------------------------------------------------------")  # 60個

# np 之基本運算

print("串列 轉 numpy陣列")
x = np.array([1, 2, 3])
print(x)
print("每個元素的平方")
print(x**2)

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(10, 19).reshape(3, 3)
print("a 陣列內容：\n", a)
print("b 陣列內容：\n", b)
print("a 陣列元素都加值：\n", a + 1)
print("a 陣列元素都平方：\n", a**2)
print("a 陣列元素加判斷：\n", a < 5)
print("a 陣列取出第一個row都加1：\n", a[0, :] + 1)
print("a 陣列取出第一個col都加1：\n", a[:, 0] + 1)
print("a b 陣列對應元素相加：\n", a + b)
print("a b 陣列對應元素相乘：\n", a * b)
print("a b 陣列點積計算：\n", np.dot(a, b))

print("------------------------------------------------------------")  # 60個

print("陣列點積計算")

a = np.random.randn(10)
b = np.random.randn(10)

np.dot(a, b)

print("------------------------------------------------------------")  # 60個

print("一維陣列 10個元素")
cc = np.arange(10)
print(cc)

print("前4項")
print(cc[:4])

print("第3項 至 第7項(不含尾)")
print(cc[3:7])

print("第5項 至 最後")
print(cc[5:])

print("第3至第9項 跳一個")
print(cc[3:9:2])

print("第2項開始至最後, 跳一個")
print(cc[2::2])

print("從頭至最後, 跳二個")
print(cc[::3])

print("------------------------------------------------------------")  # 60個

# 使用布林陣列篩選值

A = np.arange(10)

A2 = A < 5

print(A)
print(A2)
print(A[A2])

print("------------------------------------------------------------")  # 60個

print("陣列轉置 (transpose)")

A = np.arange(10).reshape(2, 5)
print(A)
print(A.T)

print(A.transpose(1, 0))  # 不知道是什麼意思

print("二維串列 轉 numpy陣列")
A = np.array([[1, 2], [3, 4], [5, 6]])
print(A)
print(A.T)
print(A.transpose())

A = np.array([1, 2, 3, 4, 5, 6])
B = np.reshape(A, (3, 2))
print(B)
print(B.T)
print(B.transpose())
print(np.transpose(B))

print("------------------------------------------------------------")  # 60個

# 陣列的切片操作
cc = np.arange(10)
print(cc)

cc[0:3] = 1
print(cc)

print("------------------------------------------------------------")  # 60個

print("numpy 統計函數")

# 串列
data = [
    37,
    24,
    6,
    51,
    83,
    28,
    51,
    58,
    82,
    95,
    83,
    6,
    42,
    53,
    98,
    6,
    90,
    4,
    59,
    87,
    28,
    17,
    28,
    46,
    40,
    53,
    70,
    49,
    55,
    41,
    74,
    57,
    31,
    55,
    5,
    65,
    44,
    98,
    36,
    4,
]

print("串列長度 :", len(data))

print("串列 轉 numpy陣列")
cc = np.array(data)  # 串列 轉 numpy陣列

print("資料型態：%s" % type(cc))
print("平均值：%.2f" % np.mean(cc))
print("中位數：%.2f" % np.median(cc))
print("標準差：%.2f" % np.std(cc))
print("變異數：%.2f" % np.var(cc))
print("極差值：%.2f" % np.ptp(cc))

"""
sum(a, axis = None)	根據給定軸axis計算陣列a相關元素之和, axis整數或元組
mean(a, axis = None)	根據給定軸axis計算陣列a相關元素之期值, axis整數或元組
average(a, axis = None, weight = None)	根據給定軸axis計算陣列a相關元素之加權平均值
std(a, axis = None)	根據給定軸axis計算陣列a相關元素之標準差
var(a, axis = None)	根據給定軸axis計算陣列a相關元素之方差

min(a) max(a)		計算陣列a中元素的 最小值 最大值
argmin(a) argmax(a)	計算陣列a中元素的 最小值 最大值 的降一維後下標
unravel_index(index, shape)	根據shape將一維下標index轉換成多維下標
ptp(a)	計算陣列a中元素最大值與最小值的差
median(a)計算陣列a中元素的中位數(中值)
"""

print("numpy 統計函數")
cc = np.arange(15).reshape(3, 5)
print(cc)
print(np.sum)
print(np.sum(cc))
print(np.mean(cc))
print(np.mean(cc, axis=0))
print(np.mean(cc, axis=1))
print(np.average(cc, axis=0, weights=[11, 6, 2]))
print(np.std(cc))
print(np.var(cc))
print(np.std(cc, axis=1))
print(np.std(cc, axis=0))
print(np.std(cc, axis=1))
print(np.std(cc, axis=0))
print(np.argmax(cc))
print(np.unravel_index(np.argmax(cc), cc.shape))
print(cc)
print(np.ptp(cc))

print("------------------------------------------------------------")  # 60個

"""
50個常用的Numpy函數解釋，參數和使用示例
Numpy是python中最有用的工具之一。
它可以有效地處理大容量數據。使用NumPy的最大原因之一是它有很多處理數組的函數。
在本文中，將介紹NumPy在數據科學中最重要和最有用的一些函數。
"""

# np.array()用於創建一維或多維數組
# array(object, dtype = None, *, copy = True, order = 'K', subok = False, ndmin = 0)
# dtype:生成數組所需的數據類型。
# ndim:指定生成數組的最小維度數。

print("創建數組 Array")

print("創建數組 full")
# 創建一個單獨值的n維數組。
# np.full(shape, fill_value, dtype = None)
# fill_value:填充值。

cc = np.full((2, 4), fill_value=2)
print(cc)

print("創建數組 Identity")
# 創建具有指定維度的單位矩陣。
# np.identity(n, dtype = None)

cc = np.identity(4)
print(cc)

print("unique 單一化")

A = np.random.randint(0, 10, 20)
print("原資料 :", A)
print(len(A), "個")

B = np.unique(A)
print("單一化後 :", B)
print(len(B), "個")

print("unique 返回一個所有唯一元素排序的數組。")
# np.unique(ar, return_index = Fasle, return_inverse = Fasle, return_counts = Fasle, axis = None)
# return_index:如果為True，返回數組的索引。
# return_inverse:如果為True，返回唯一數組的下標。
# return_counts:如果為True，返回數組中每個唯一元素出現的次數。
# axis:要操作的軸。默認情況下，數組被認為是扁平的。

A = np.array([1, 1, 2, 3, 3, 4, 5, 6, 6, 2])
cc = np.unique(A, return_counts=True)
print(cc)

print("mean 返回數組的平均數")
# np.mean(a, axis = None, dtype = None, out = None)
cc = np.mean(A, dtype="int")
print(cc)

print("medain 返回數組的中位數。")
# np.median(a, axis = None, out = None)
print("二維串列 轉 numpy陣列")
list2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
cc = np.median(list2d)
print(cc)

print("digitize 返回輸入數組中每個值所屬的容器的索引。")
# np.digitize(x, bins, right = False)
# bin：容器的數組。
# right:表示該間隔是否包括右邊或左邊的bin。

print("串列 轉 numpy陣列")
a = np.array([-0.9, 0.5, 0.9, 1, 1.2, 1.4, 3.6, 4.7, 5.3])
bins = np.array([0, 1, 2, 3])
cc = np.digitize(a, bins)
print(cc)

"""
Exp        Value 
x < 0     :   0 
0 <= x <1 :   1 
1 <= x <2 :   2 
2 <= x <3 :   3 
3 <=x     :   4 
Compares -0.9 to 0, here x < 0 so Put 0 in resulting array. 
Compares  0.5 to 0, here 0 <= x <1 so Put 1. 
Compares 5.4 to 4, here 3<=x so Put 4
"""

print("expand_dims 它用於擴展數組的維度。")
# np.expand_dims(a, axis)
print("串列 轉 numpy陣列")
list1d = np.array([8, 14, 1, 8, 11, 4, 9, 4, 1, 13, 13, 11])
cc = np.expand_dims(cc, axis=0)
print(cc)

cc = np.expand_dims(cc, axis=1)
print(cc)

print("squeeze 通過移除一個單一維度來降低數組的維度。")
# np.squeeze(a, axis = None)

print("串列 轉 numpy陣列")
A = np.array([[8], [14], [1], [8], [11], [4], [9], [4], [1], [13], [13], [11]])
cc = np.squeeze(A)
print(cc)

print("count_nonzero 計算所有非零元素并返回它們的計數。")
# np.count_nonzero(a, axis = None, ...)

print("串列 轉 numpy陣列")
list1d = np.array([0, 0, 1, 1, 1, 0])
cc = np.count_nonzero(list1d)
print(cc)

print("argwhere 查找并返回非零元素的所有下標。")
# np.argwhere(a)

print("串列 轉 numpy陣列")
list1d = np.array([0, 0, 1, 1, 1, 0])
cc = np.argwhere(list1d)
print(cc)

print("argmax & argmin argmax返回數組中Max元素的索引。它可以用於多類圖像分類問題中獲得高概率預測標簽的指標。")
# np.argmax(a, axis = None, out = None)
print("串列 轉 numpy陣列")
A = np.array([[0.12, 0.64, 0.19, 0.05]])
cc = np.argmax(A)
print(cc)

print("argmin將返回數組中min元素的索引。")
# np.argmin(a, axis = None, out = None)
cc = np.argmin(min)
print(cc)

print("sort 對數組排序。")
# np.sort(a, axis = -1, kind = None, order = None)
# kind:要使用的排序算法。{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}

print("clip 它可以將數組的裁剪值保持在一個范圍內。")

print("串列 轉 numpy陣列")
list1d = np.array([0, 1, -3, -4, 5, 6, 7, 2, 3])
cc = list1d.clip(0, 5)
print(cc)

cc = list1d.clip(0, 3)
print(cc)

cc = list1d.clip(3, 5)
print(cc)

# 集合操作

print("查找公共元素 intersect1d函數以排序的方式返回兩個數組中所有唯一的值。")
# np.intersect1d(arg1, arg2, assume_unique = False, return_indices = False)
# Assume_unique:如果為真值，則假設輸入數組都是唯一的。
# Return_indices:如果為真，則返回公共元素的索引。

print("串列 轉 numpy陣列")
list1d1 = np.array([1, 2, 3, 4, 5, 6])
list1d2 = np.array([3, 4, 5, 8, 9, 1])
np.intersect1d(list1d1, list1d2)

np.intersect1d(list1d1, list1d2, return_indices=True)

print("查找不同元素 np.setdiff1d函數返回arr1中在arr2中不存在的所有唯一元素。")
print("串列 轉 numpy陣列")
a = np.array([1, 7, 3, 2, 4, 1])
b = np.array([9, 2, 5, 6, 7, 8])
np.setdiff1d(a, b)

print("從兩個數組中提取唯一元素 Setxor1d 將按順序返回兩個數組中所有唯一的值。")
print("串列 轉 numpy陣列")
a = np.array([1, 2, 3, 4, 6])
b = np.array([1, 4, 9, 4, 36])
np.setxor1d(a, b)

print("合并 Union1d函數將兩個數組合并為一個。")
print("串列 轉 numpy陣列")
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 3, 5, 4, 36])
np.union1d(a, b)

# 數組分割

print("水平分割 Hsplit函數將數據水平分割為n個相等的部分。")
print("二維串列 轉 numpy陣列")
list2d = np.array([[3, 4, 5, 2], [6, 7, 2, 6]])
np.hsplit(list2d, 2)  ## splits the data into two equal parts

np.hsplit(list2d, 4)  ## splits the data into four equal parts

print("垂直分割 Vsplit將數據垂直分割為n個相等的部分。")
print("二維串列 轉 numpy陣列")
list2d = np.array([[3, 4, 5, 2], [6, 7, 2, 6]])
np.vsplit(list2d, 2)

# 數組疊加

print("水平疊加 hstack 將在另一個數組的末尾追加一個數組。")
print("串列 轉 numpy陣列")
list1da = np.array([1, 2, 3, 4, 5])
list1db = np.array([1, 4, 9, 16, 25])

cc = np.hstack((list1da, list1db))
print(cc)

print("垂直疊加 vstack將一個數組堆疊在另一個數組上。")

cc = np.vstack((list1da, list1db))
print(cc)

# 數組比較

print("allclose 如果兩個數組的形狀相同，則Allclose函數根據公差值查找兩個數組是否相等或近似相等。")

print("串列 轉 numpy陣列")
list1da = np.array([0.25, 0.4, 0.6, 0.32])
list1db = np.array([0.26, 0.3, 0.7, 0.32])

tolerance = 0.1  ## Total Difference
np.allclose(list1da, list1db, tolerance)

tolerance = 0.5
np.allclose(list1da, list1db, tolerance)

print("equal 它比較兩個數組的每個元素，如果元素匹配就返回True。")

cc = np.equal(list1da, list1da)
print("兩陣列相同 :", cc)
cc = np.equal(list1da, list1db)
print("兩陣列相同 :", cc)

print("------------------------------------------------------------")  # 60個

# 重復的數組元素

print("repeat 它用於重復數組中的元素n次。")
# np.repeat(a, repeats, axis = None)

# A:重復的元素

# Repeats:重復的次數。
N = 10
cc = np.repeat("ABCD", N)
print(cc)

N = 10
cc = np.repeat([0, 1, 2], N)
print(cc)

print("------------------------------------------------------------")  # 60個

print("tile 通過重復A，rep次來構造一個數組。")
# np.tile(A, reps)

na = np.tile("Ram", 5)
print(na)

na = np.tile(3, (2, 3))
print(na)

# 愛因斯坦求和

print("einsum 此函數用於計算數組上的多維和線性代數運算。")

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(21, 30).reshape(3, 3)

na = np.einsum("ii->i", a)
print(na)

na = np.einsum("ji", a)
print(na)

na = np.einsum("ij,jk", a, b)
print(na)

na = np.einsum("ii", a)
print(na)

# 統計分析

print("直方圖 這是Numpy的重要統計分析函數，可計算一組數據的直方圖值。")

print("二維串列 轉 numpy陣列")
A = np.array([[3, 4, 5, 2], [6, 7, 2, 6]])
na = np.histogram(A)
print(na)

print("百分位數 沿指定軸計算數據的Q-T-T百分位數。")

# a:輸入。
# q:要計算的百分位。
# overwrite_input:如果為true，則允許輸入數組修改中間計算以節省內存。
print("二維串列 轉 numpy陣列")
a = np.array([[2, 4, 6], [4, 8, 12]])
na = np.percentile(a, 50)
print(na)
na = np.percentile(a, 10)
print(na)

A = np.array([2, 3, 4, 1, 6, 7])

na = np.percentile(a, 5)
print(na)

print("標準偏差和方差 std和var是NumPy的兩個函數，用於計算沿軸的標準偏差和方差。")

print("二維串列 轉 numpy陣列")
a = np.array([[2, 4, 6], [4, 8, 12]])

na = np.std(a, axis=1)
print(na)
na = np.std(a, axis=0)  ## Column Wise
print(na)
na = np.var(a, axis=1)
print(na)
na = np.var(a, axis=0)
print(na)

# 數組打印

print("顯示帶有兩個十進制值的浮點數")

np.set_printoptions(precision=2)

print("串列 轉 numpy陣列")
na = np.array([12.23456, 32.34535])
print(na)

print("設置打印數組最大值")

na = np.set_printoptions(threshold=np.inf)
print(na)

print("增加一行中元素的數量")

na = np.set_printoptions(linewidth=100)  ## 默認是 75
print(na)

print("------------------------------------------------------------")  # 60個

print("串列 轉 numpy陣列")
x1 = np.array([0, 1, 1, 3, 2, 1])
# 因為 x1 元素最大值是 3, 所以 bin 是 4
print("np.bincount :", np.bincount(x1))

print("串列 轉 numpy陣列")
x2 = np.array([0, 1, 1, 7, 2, 1])
# 因為 x2 元素最大值是 7, 所以 bin 是 8
print("np.bincount :", np.bincount(x2))

print("------------------------------------------------------------")  # 60個

print("串列 轉 numpy陣列")
x1 = np.array([0, 1, 1, 3, 2, 1])
# 因為 x1 元素最大值是 3, 所以 bin 是 4
print("np.bincount :", np.bincount(x1))
print("mode :", np.argmax(np.bincount(x1)))

print("串列 轉 numpy陣列")
x2 = np.array([0, 1, 1, 7, 2, 1])
# 因為 x2 元素最大值是 7, 所以 bin 是 8
print("np.bincount :", np.bincount(x2))
print("mode :", np.argmax(np.bincount(x1)))

print("------------------------------------------------------------")  # 60個

print("串列 轉 numpy陣列")
a = np.array([1, 1])
b = np.array([5, 5])
c = np.array([1, 5])
d = np.array([5, 1])

ab = b - a  # 向量ab
cd = d - c  # 向量bc

norm_a = np.linalg.norm(ab)  # 計算向量大小
norm_b = np.linalg.norm(cd)  # 計算向量大小

dot_ab = np.dot(ab, cd)  # 計算向量內積

cos_angle = dot_ab / (norm_a * norm_b)  # 計算cos值
rad = math.acos(cos_angle)  # acos轉成弧度
deg = math.degrees(rad)  # 轉成角度
print("角度是 = {}".format(deg))

print("------------------------------------------------------------")  # 60個


def cosine_similarity(va, vb):
    norm_a = np.linalg.norm(va)  # 計算向量大小
    norm_b = np.linalg.norm(vb)  # 計算向量大小
    dot_ab = np.dot(va, vb)  # 計算向量內積
    return dot_ab / (norm_a * norm_b)  # 回傳相似度


print("串列 轉 numpy陣列")
a = np.array([2, 1, 1, 1, 0, 0, 0, 0])
b = np.array([1, 1, 0, 0, 1, 1, 1, 0])
c = np.array([1, 1, 0, 0, 1, 1, 0, 1])
print("a 和 b 相似度 = {0:5.3f}".format(cosine_similarity(a, b)))
print("a 和 c 相似度 = {0:5.3f}".format(cosine_similarity(a, c)))
print("b 和 c 相似度 = {0:5.3f}".format(cosine_similarity(b, c)))

print("------------------------------------------------------------")  # 60個

print("兩陣列的相關係數")
print("串列 轉 numpy陣列")
x = np.array([8, 9, 10, 7, 8, 9, 5, 7, 9, 8])
y = np.array([12, 15, 16, 18, 6, 11, 3, 12, 11, 16])
print("x陣列長度 :", len(x))
print("y陣列長度 :", len(y))
x_mean = np.mean(x)
y_mean = np.mean(y)

xi_x = [v - x_mean for v in x]
yi_y = [v - y_mean for v in y]

data1 = [0] * 10
data2 = [0] * 10
data3 = [0] * 10
for i in range(len(x)):
    data1[i] = xi_x[i] * yi_y[i]
    data2[i] = xi_x[i] ** 2
    data3[i] = yi_y[i] ** 2

v1 = np.sum(data1)
v2 = np.sum(data2)
v3 = np.sum(data3)
r = v1 / ((v2**0.5) * (v3**0.5))
print("相關係數 : {}".format(r))

print("------------------------------------------------------------")  # 60個

print("串列 轉 numpy陣列")
a = np.array([4, 2])
b = np.array([1, 3])

norm_a = np.linalg.norm(a)  # 計算向量大小
norm_b = np.linalg.norm(b)  # 計算向量大小

dot_ab = np.dot(a, b)  # 計算向量內積

cos_angle = dot_ab / (norm_a * norm_b)  # 計算cos值
rad = math.acos(cos_angle)  # acos轉成弧度

area = norm_a * norm_b * math.sin(rad) / 2
print("area = {0:5.2f}".format(area))

print("------------------------------------------------------------")  # 60個

print("串列 轉 numpy陣列")
a = np.array([4, 2])
b = np.array([1, 3])

ab_cross = np.cross(a, b)  # 計算向量外積
area = np.linalg.norm(ab_cross) / 2  # 向量長度除以2

print("area = {0:5.2f}".format(area))

print("------------------------------------------------------------")  # 60個

print("串列 轉 numpy陣列")
x = np.array([1, 2, 3])  # 1 x 3 陣列 x
y = np.array([2, 3, 4])  # 1 x 3 陣列 y
print("x :", x)
print("y :", y)

print()

y = y.reshape(-1, 1)  # y 改為 3 x 1 陣列
print("新 y :", y)

print()

print("x + y :", x + y)

print("------------------------------------------------------------")  # 60個

print("numpy 之 array 之 形狀轉換")

animal_list = [
    [1, "鼠", "mouse", 3],
    [2, "牛", "ox", 48],
    [3, "虎", "tiger", 33],
    [4, "兔", "rabbit", 8],
    [5, "龍", "dragon", 38],
    [6, "蛇", "snake", 16],
]

na_animal1 = np.array(animal_list)
# print(na_animal1)
print("維度 :", na_animal1.ndim)
print("形狀 :", na_animal1.shape)
print("數量 :", na_animal1.size)

print("numpy 之 array 之 reshape 用法, 轉成 3 X 8")
na_animal2 = na_animal1.reshape(3, 8)  # ravel()方法將數組維度拉成一維數組
print(na_animal2)
print("維度 :", na_animal2.ndim)
print("形狀 :", na_animal2.shape)
print("數量 :", na_animal2.size)

print("numpy 之 array 之 ravel 用法, 轉成 一維陣列")
na_animal3 = na_animal1.ravel()  # ravel()方法將數組維度拉成一維數組
# print(na_animal3)
print("維度 :", na_animal3.ndim)
print("形狀 :", na_animal3.shape)
print("數量 :", na_animal3.size)

print("------------------------------------------------------------")  # 60個

print("numpy 之 mgrid()方法生成等差數列")

print("一維等差數列")
a = np.mgrid[0:5:1]  # 用mgrid()方法生成等差數列a
print(a)

print("二維等差數列")
a, b = np.mgrid[0:5:1, 0:5:1]  # 用mgrid()方法生成等差數列a,b
print(a)
print(b)

print("------------------------------------------------------------")  # 60個

num = 3.2
print("數值{0:2.1f} 取log10 {1:4.3f}".format(num, np.log10(num)))

print("------------------------------------------------------------")  # 60­э


print("------------------------------------------------------------")  # 60個
print("numpy")
print("------------------------------------------------------------")  # 60個

print(np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])])
print(np.c_[np.array([[1, 2, 3]]), 0, 0, np.array([[4, 5, 6]])])

"""
array([[1, 4],
       [2, 5],
       [3, 6]])
"""

# array([[1, 2, 3, ..., 4, 5, 6]])

print("------------------------------------------------------------")  # 60個

# numpy.c_() and numpy.r_()的用法


#####np.c_是按行连接两个矩陣，就是把两矩陣左右相加，要求行数相等，类似於pandas中的merge()。
#####np.r_是按列连接两个矩陣，就是把两矩陣上下相加，要求列数相等，类似於pandas中的concat()。

# np.c_是按行连接两个矩陣，就是把两矩陣左右相加，要求行数相等。
# np.r_是按列连接两个矩陣，就是把两矩陣上下相加，要求列数相等。


# 1.numpy.c_:

x = np.arange(12).reshape(3, 4)
print("x:", x, x.shape)

y = np.arange(10, 22).reshape(3, 4)
print("y:", y, y.shape)

z = np.c_[x, y]
print("z:", z, z.shape)

# 2.numpy.r_用法:

x = np.arange(12).reshape(3, 4)
print("x:", x, x.shape)

y = np.arange(10, 22).reshape(3, 4)
print("y:", y, y.shape)

z = np.r_[x, y]
print("z:", z, z.shape)

print("------------------------------------------------------------")  # 60個

print("二維陣列 6 X 4")
cc = np.array(
    [[0, 0, 0, 1], [1, 1, 1, 2], [2, 2, 2, 3], [3, 3, 3, 4], [4, 4, 4, 5], [5, 5, 5, 6]]
)
print(cc)
print(cc.shape)
print(cc.dtype)
print(cc.ndim)
print(cc.size)
print(cc.nbytes)

print("第3列 之 第1~4項(不含尾)")
print(cc[3, 1:4])

print("前2列 之 第2欄之後")
print(cc[:2, 2:])

print("第2列 之 全部")
print(cc[2, :])

print("全部列 之 第3欄, 轉成row")
print(cc[:, 3])

print("全部列 之 偶數欄")
print(cc[:, ::2])

print("偶數列 之 036欄")
print(cc[::2, ::3])

# np.argmin()求最小值對應的索引
# np.argmax()求最大值對應的索引

print("每個直行的最小值:", cc.min(axis=0))
print("每個直行的最小值對應的索引:", cc.argmin(axis=0))
print("每個直行的標準差:", cc.std(axis=0))

print("全部平均:", cc.mean())
print("直行平均:", cc.mean(axis=0))
print("橫列平均:", cc.mean(axis=1))

print("------------------------------------------------------------")  # 60個

print("相關係數矩陣")

xx = [0, 1, 2, 3, 4, 5]
yy = [0, 1, 2, 3, 4, 5]
zz = [5, 4, 3, 2, 1, 0]

print(np.corrcoef(xx, yy))
print(np.corrcoef(xx, zz))

"""
abs < 0.3 : 低度相關
abs > 0.7 : 高度相關
abs 中間  : 中度相關

"""
print("------------------------------------------------------------")  # 60個

print("矩陣與二維數組")
cc = np.mat(np.mat([[1, 2, 3], [4, 5, 6]]))
print(type(cc))
print(cc)

cc = np.mat([[1.0, 2.0], [3.0, 4.0]])

print("矩陣乘積")
print(np.dot(cc, cc))

print("矩陣點乘")
print(np.multiply(cc, cc))

print("矩陣轉置")
print(cc.T)

print("矩陣求逆")
print(cc.I)

print("求矩陣的跡")
print(np.trace(cc))

print("特徵分解")
print(np.linalg.eig(cc))

evals, evecs = np.linalg.eig(cc)
print("特征值:", evals, "\n特征向量:", evecs)

print("------------------------------")  # 30個

cc = np.mat(np.mat([[1, 2, 3], [4, 5, 6]]))

print(cc.sum())
print(cc.sum(axis=0))
print(cc.sum(axis=1))

# axis = 0 : 第0維 直行
# axis = 1 : 第1維 橫列
print("全部和:", cc.sum())
print("直行加:", cc.sum(axis=0))
print("橫列加:", cc.sum(axis=1))

print("------------------------------")  # 30個

# n阶方阵的行列式运算
A = np.mat(
    [
        [
            1,
            2,
            4,
            5,
            7,
        ],
        [
            9,
            12,
            11,
            8,
            2,
        ],
        [
            6,
            4,
            3,
            2,
            1,
        ],
        [9, 1, 3, 4, 5],
        [0, 2, 3, 4, 1],
    ]
)

print("det(A):", np.linalg.det(A))  # 方阵的行列式

invA = np.linalg.inv(A)  # 矩陣的逆矩陣
print("inv(A):", invA)

AT = A.T  # 矩陣的对称
print(A * AT)

# 矩陣的秩
print(np.linalg.matrix_rank(A))

# 可逆矩陣求解
b = [1, 0, 1, 0, 1]
S = np.linalg.solve(A, np.transpose(b))
print(S)

print("------------------------------")  # 30個

base = np.mat([[3, 1], [1, 3]])
v1 = np.mat([1, 2])
print(np.linalg.norm(v1))
print((base[0] * base[1].T) / (np.linalg.norm(base[1]) * np.linalg.norm(base[0])))

v2 = v1 * base
print(v2)
print(np.linalg.norm(v2))

print("------------------------------")  # 30個

base = np.mat([[1, 3], [3, 1]])
print(base[0] + base[1])

print("------------------------------")  # 30個

# 一維陣列轉矩陣
list1d = [1, 2, 3, 4, 5]
print(type(list1d))

A = np.mat(list1d)

N = 10
print(N * A)

print("------------------------------")  # 30個

# 二維陣列轉矩陣
list2d = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(type(list2d))

A = np.mat(list2d)

cc = np.shape(A)

print("矩陣")
print(A)
print("shape :", cc)

print("------------------------------")  # 30個

list2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A = np.mat(list2d)

N = 10
print(N * A)

print(sum(A))

A2 = 1.5 * np.ones([3, 3])
print(np.multiply(A, A2))

print(np.power(A, 2))

print("------------------------------")  # 30個

A1 = np.mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

A2 = np.mat([[1], [2], [3]])
print(A1 * A2)

# 矩陣的转置
print(A1.T)
A1.transpose()
print(A1)

print("------------------------------")  # 30個

list2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A = np.mat(list2d)

[m, n] = np.shape(A)  # 矩陣的行列数
print("矩陣的行数和列数:", m, n)

myscl1 = A[0]  # 按行切片
print("按行切片:", myscl1)

myscl2 = A.T[0]  # 按列切片
print("按列切片:", myscl2)

mycpmat = A.copy()  # 矩陣的复制
print("复制矩陣:\n", mycpmat)

# 比较
print("矩陣元素的比较:\n", A < A.T)

print("------------------------------")  # 30個

featuremat = np.mat(
    [
        [
            88.5,
            96.8,
            104.1,
            111.3,
            117.7,
            124.0,
            130.0,
            135.4,
            140.2,
            145.3,
            151.9,
            159.5,
            165.9,
            169.8,
            171.6,
            172.3,
            172.7,
        ],
        [
            12.54,
            14.65,
            16.64,
            18.98,
            21.26,
            24.06,
            27.33,
            30.46,
            33.74,
            37.69,
            42.49,
            48.08,
            53.37,
            57.08,
            59.35,
            60.68,
            61.40,
        ],
    ]
)

# 计算均值
mv1 = np.mean(featuremat[0])  # 第一列的均值
mv2 = np.mean(featuremat[1])  # 第二列的均值

# 计算两列标准差
dv1 = np.std(featuremat[0])
dv2 = np.std(featuremat[1])

corref = np.mean(np.multiply(featuremat[0] - mv1, featuremat[1] - mv2)) / (dv1 * dv2)
print(corref)

print("相關係數矩陣")
print(np.corrcoef(featuremat))

covinv = np.linalg.inv(np.cov(featuremat))
print(covinv)
tp = featuremat.T[0] - featuremat.T[1]
distma = np.sqrt(np.dot(np.dot(tp, covinv), tp.T))
print(distma)

print("------------------------------")  # 30個

vectormat = np.mat([[1, 2, 3], [4, 5, 6]])
v12 = vectormat[0] - vectormat[1]
print(np.sqrt(v12 * v12.T))

# norm
varmat = np.std(vectormat.T, axis=0)
normvmat = (vectormat - np.mean(vectormat)) / varmat.T

# norm
print(normvmat)
normv12 = normvmat[0] - normvmat[1]
print(np.sqrt(normv12 * normv12.T))

print("------------------------------------------------------------")  # 60個

print("一維np陣列")

cc = np.array([1, 2, 3])  # Create a rank 1 array
print(type(cc))  # Prints "<type 'numpy.ndarray'>"
print(cc.shape)  # Prints "(3,)"
print(cc[0], cc[1], cc[2])  # Prints "1 2 3"
cc[0] = 5  # Change an element of the array
print(cc)  # Prints "[5, 2, 3]"
cc = np.array([[1, 2, 3], [4, 5, 6]])  # Create a rank 2 array
print(cc.shape)  # Prints "(2, 3)"
print(cc[0, 0], cc[0, 1], cc[1, 0])  # Prints "1 2 4"

print("------------------------------------------------------------")  # 60個

print("二維np陣列")

c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
cc = c[0:2, 1:3]  # 取得部分資料
# cc= c[0:2,1:3].copy() # 複製cc為c的部分資料
print(cc)  # 輸出[[2 3], [6 7]]
cc[0, 0] = 99  # 修改cc的局部資料
print(cc)  # 輸出[[99  3], [ 6  7]]
print(c)  # 輸出[[ 1 99  3  4],[ 5  6  7  8],[ 9 10 11 12]]

print("------------------------------------------------------------")  # 60個

print("二維np陣列")

cc = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
row_r1 = cc[1, :]
row_r2 = cc[1:2, :]
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)

col_r1 = cc[:, 1]
col_r2 = cc[:, 1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)

print("------------------------------------------------------------")  # 60個

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
v = np.array([9, 10], dtype=np.float64)

# 加法
print(x + y)  # 輸出 [[ 6.0  8.0] [10.0 12.0]]
print(np.add(x, y))  # 輸出 [[ 6.0  8.0] [10.0 12.0]]
print(x + 10)  # 輸出 [[11. 12.] [13. 14.]]
# 減法
print(x - y)  # 輸出 [[-4.0 -4.0] [-4.0 -4.0]]
print(np.subtract(x, y))  # 輸出 [[-4.0 -4.0] [-4.0 -4.0]]
print(x - [1, 2])  # 輸出 [[0. 0.]  [2. 2.]]
# 乘法
print(x * y)
print(np.multiply(x, y))  # 輸出  [[ 5.0 12.0][21.0 32.0]]
# 除法
print(x / y)
print(np.divide(x, y))  # 輸出 [[ 0.2  0.33333333] [ 0.42857143  0.5]]
# 平方
print(x**2)
print(np.sqrt(x))  # 輸出[[ 1. 1.41421356] [ 1.73205081  2.]]

# 矩陣乘法，兩個數組的點積 Dot product
print(x.dot(y))  # 輸出         [[19. 22.] [43. 50.]]
print(np.dot(x, y))  # [[5+14 , 6+16] []]

print("------------------------------------------------------------")  # 60個

cc = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
bool_idx = (cc % 2) == 0
print(bool_idx)
print(cc[bool_idx])
print(cc[cc > 10])
print(cc[cc % 2 == 1] * 10)

print("------------------------------------------------------------")  # 60個

# 方法1
x = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([1, 0, 1])
y = np.empty_like(x)
for i in range(2):
    y[i, :] = x[i, :] + v
print(y)  # 輸出[[2 2 4][5 5 7]]

# 方法2
v2 = np.tile(v, (2, 1))
print(v2)  # 輸出[[1 0 1][1 0 1]]
print(x + v2)  # 輸出[[2 2 4] [5 5 7]]

# 方法3
print(x + v)  # 輸出[[2 2 4] [5 5 7]]

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a[0], b[1])

a = np.append(a, b)
print(a)

d = a[1]
print(d)

a2 = np.delete(a, 1)
print(a2)
a3 = np.insert(a, 1, d)
print(a3)

print("------------------------------------------------------------")  # 60個

# 複製數據
a = [1, 2, 3]
b = np.asarray(a)
c = a
a = [4, 5, 6]
d = np.asarray(a, dtype=float)
print(a)  # [4, 5, 6]
print(b)  # [1 2 3]
print(c)  # [1, 2, 3]
print(d)  # [4. 5. 6.]

print("------------------------------------------------------------")  # 60個

# 合併陣列
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a)
print(b)

print("陣列合併, 無參數就是直向合併, axis=0")
cc = np.concatenate((a, b))
print(cc)

print("陣列直向合併, axis=0")
cc = np.concatenate((a, b), axis=0)
print(cc)

print("陣列橫向合併, axis=1")
cc = np.concatenate((a, b), axis=1)
print(cc)

print("陣列橫向合併, axis=1, 多個")
cc = np.concatenate((a, a, a, b, b), axis=1)
print(cc)

a = np.array([1, 2, 3])
print("a=" + str(a))

b = a.copy()
print("b=a.copy()->" + str(b))
b.fill(4)
print("b.fill(0)=" + str(b))
c = np.concatenate((a, b))
print("c=np.concatenate((a,b))->" + str(c))

print("------------------------------------------------------------")  # 60個

# 擴充或刪除陣列的維度
a = np.array([[1, 2, 3, 4, 5, 6, 7, 8]])
b = a.reshape(2, 4)
print(b.shape)
c = np.expand_dims(b, axis=0)
d = np.expand_dims(b, axis=1)
print(c.shape, d.shape)
e = np.squeeze(c)
f = np.squeeze(d)
print(e.shape, f.shape)

print("------------------------------------------------------------")  # 60個

print("矩陣運算")
N = 5

print("建立NXN之隨機矩陣A")
matA = np.array(np.random.rand(N, N))
print(matA.shape)
print(matA)

print("建立NXN之隨機矩陣B")
matB = np.array(np.random.rand(N, N))
print(matB.shape)
print(matB)

print("建立NXN之矩陣C 元素全為3")
matC = np.array([[3] * N for _ in range(N)])
print(matC.shape)
print(matC)

print("使用 Python 計算")

for i in range(N):
    for j in range(N):
        for k in range(N):
            matC[i][j] = matA[i][k] * matB[k][j]

print("使用 NumPy 計算")

matC = np.dot(matA, matB)

print("------------------------------------------------------------")  # 60個

print("---------------↓不使用 copy()↓---------------")

arr1 = np.array([1, 2, 3, 4, 5])

print("arr1:" + str(arr1))

arr2 = arr1

arr2[0] = 100

print("arr2:" + str(arr1))
print("arr1:" + str(arr2))

print("---------------↓使用 copy()↓-----------------")

arr1 = np.array([1, 2, 3, 4, 5])

print(arr1)

arr2 = arr1.copy()

arr2[0] = 100

print("arr1:" + str(arr1))
print("arr2:" + str(arr2))
print("arr1:" + str(arr1))

print("------------------------------------------------------------")  # 60個

# 使用 NumPy 陣列
storages = np.array([1, 2, 3, 4])

A1 = np.array([2, 4, 6, 8, 10])
A2 = np.array([1, 3, 5, 7, 9])

# 相加
print("A1 + A2:")
print(A1 + A2)

# 相減
print("A1 - A2:")
print(A1 - A2)

# A ** 3 (三次方)
print("A1 ** 3:")
print(A1**3)

# A1 / A2(相除)
print("A1 / A2:")
print(A1 / A2)

print()

print("------------------------------------------------------------")  # 60個

# 體驗好用的 NumPy 函式

A = np.array([4, -9, 16, -4, 20])
print(A)

A_abs = np.abs(A)
print("絕對值:", A_abs)

print("e為底數:", np.exp(A_abs))

print("平方根:", np.sqrt(A_abs))

A1 = np.array([2, 5, 7, 9, 5, 2])

A2 = np.array([2, 5, 8, 3, 1])

new_A1 = np.unique(A1)

print("剔除A1重複元素:", new_A1)

print("聯集:", np.union1d(new_A1, A2))

print("交集:", np.intersect1d(new_A1, A2))

print("差集:", np.setdiff1d(new_A1, A2))

print("------------------------------------------------------------")  # 60個

# 陣列的軸 (axis)

cc = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print("shape")
print(cc.shape)
print("sum()")
print(cc.sum())
print("sum(axis=0) 第0軸和")
print(cc.sum(axis=0))
print("sum(axis=1) 第1軸和")
print(cc.sum(axis=1))

cc = np.array([[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]])
print("shape")
print(cc.shape)
print("sum()")
print(cc.sum())
print("sum(axis=0) 第0軸和")
print(cc.sum(axis=0))
print("sum(axis=1) 第1軸和")
print(cc.sum(axis=1))
print("sum(axis=2) 第2軸和")
print(cc.sum(axis=2))

print("------------------------------------------------------------")  # 60個

# 陣列的 shape 與 reshape

cc = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print("原 shape  :", cc.shape)
print("內容 :", cc)

cc = cc.reshape(4, 2)

print("新 shape  :", cc.shape)
print("內容 :", cc)

cc = cc.reshape(-1)
print(cc)

print("新 shape  :", cc.shape)
print("內容 :", cc)

print("------------------------------------------------------------")  # 60個

# 多軸陣列的切片做法

cc = np.array([[1, 2, 3], [4, 5, 6]])
print(cc[1])

cc = np.array([[1, 2, 3], [4, 5, 6]])
print(cc[1][2])

cc = np.array([[1, 2, 3], [4, 5, 6]])
print(cc[1, 1:])

cc = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(cc[[3, 2, 0]])

print("------------------------------------------------------------")  # 60個

# 陣列排序

cc = np.array([[8, 4, 2], [3, 5, 1]])

print("---------------原陣列----------------")

print(cc)

print("----------對 cc 以軸 1 方向排序---------")

print(np.sort(cc))

print("----------對 cc 以軸 0 方向排序---------")

cc.sort(axis=0)

print(cc)

print("-------------argsort排序-------------")

print(cc.argsort())

print("------------------------------------------------------------")  # 60個

# 陣列擴張 (Broadcasting)

x = np.arange(15).reshape(3, 5)
y = np.array([np.arange(5)])
z = x - y
print(z)

print("------------------------------------------------------------")  # 60個

# 用 NumPy 函式計算矩陣乘積

cc = np.arange(9).reshape(3, 3)

print(np.dot(cc, cc))

print("------------------------------------------------------------")  # 60個

# 數組操作
print("min 返回數組中的最小值。")
# np.min(a, axis = None, out = None, ...)
# axis:用於操作的軸。
# out:用於存儲輸出的數組。

print("串列 轉 numpy陣列")
A = np.array([1, 1, 2, 3, 3, 4, 5, 6, 6, 2])
cc = np.min(A)
print(cc)

print("max 返回數組中的最大值。")
# np.max(a, axis = None, out = None, ...)
cc = np.max(A)
print(cc)

print("串列 轉 numpy陣列")
A = np.array([2, 3, 1, 7, 4, 5])
cc = np.sort(A)
print(cc)

print("abs 返回數組中元素的絕對值。當數組中包含負數時，它很有用。")
print("串列 轉 numpy陣列")
cc = np.array([[1, -3, 4], [-2, -4, 3]])
cc = np.abs(cc)
print(cc)

print("------------------------------------------------------------")  # 60­э

print("numpy 存讀檔案")
# save  txt

print("建立np陣列")
a = np.arange(15).reshape(3, 5)
print(a)

print("np陣列存檔成np之文字格式")
np.savetxt("tmp_np_asc.txt", a)

print("讀取np之文字格式檔案成np陣列")
b = np.loadtxt("tmp_np_asc.txt")
print(b)

print("np陣列存檔成np之binary格式")
np.save("tmp_np_bin.npy", a)

print("讀取np之binary格式檔案成np陣列")
c = np.load("tmp_np_bin.npy")
print(c)

print("------------------------------------------------------------")  # 60個

# Python numpy 寫入 csv
# 將 numpy array 用 savetxt 寫入 csv

cc = np.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(type(cc))  # <class 'numpy.ndarray'>

np.savetxt("tmp_output_data1.csv", cc, delimiter=",")
np.savetxt("tmp_output_data2.csv", cc, delimiter=",", fmt="%d")
np.savetxt("tmp_output_data3.csv", cc, delimiter=",", fmt="%.2f")

print("------------------------------------------------------------")  # 60個

# 保存和加載數據

print("保存")

# savetxt 在文本文件中保存數組的內容。

A = np.linspace(10, 100, 500).reshape(25, 20)
np.savetxt("tmp_array.txt", A)

print("加載")  # 從文本文件加載數組，它以文件名作為參數。

np.loadtxt("tmp_array.txt")

print("------------------------------------------------------------")  # 60個

print("替換數組中的值 where put copyto")

print("where 返回滿足條件的數組元素。")
# np.where(condition, [x, y])
# condition:匹配的條件。如果true則返回x，否則y。

cc = np.arange(12).reshape(4, 3)
print(cc)

print("大於5的")
cc = np.where(a > 5)  ## Get The Index
print(cc)

print("大於5的")
cc = a[np.where(a > 5)]  ## Get Values
print(cc)

# cc = np.where(data[feature].isnull(), 1, 0)
# print(cc)

print("put 用給定的值替換數組中指定的元素。")
# np.put(a, ind, v)
# a:數組
# Ind:需要替換的索引。
# V:替換值。

cc = np.put(A, [1, 2], [6, 7])
print(cc)

print("copyto 將一個數組的內容復制到另一個數組中。")
# np.copyto(dst, src, casting = 'same_kind', where = True)
# dst：目標
# src：來源

print("串列 轉 numpy陣列")
arr1 = np.array([1, 2, 3, 4])
print("串列 轉 numpy陣列")
arr2 = np.array([5, 6, 7, 8])

print("Before arr1", arr1)
print("Before arr2", arr1)
np.copyto(arr1, arr2)
print("After arr1", arr1)
print("After arr2", arr2)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


""" new


array 大變身!
A = np.random.rand(50)

A.shape
A.shape = (5,10)
A.reshape(10,5)
拉平 ravel
A.ravel()

其實掌握矩陣, 或很像矩陣的陣列都是「先列後行」就可以!

A = np.arange(10).reshape(2,5)
array([[0, 1, 2, 3, 4],
,       [5, 6, 7, 8, 9]])

【重點】 一列一列算下來是 axis=0	直行總和
A.sum(axis=0)

【重點】 一行一行算過去是 axis=1	橫行總和
A.sum(axis=1)

【提示】當然也有可能全部算	全部總和
A.sum()
  
print("------------------------------------------------------------")  # 60個

"""
# numpy統計

"""
2. 統計平均
numpy.sum(a, axis=None, dtype=None, out=None, keepdims=False)：
numpy.mean(a, axis=None, dtype=None, out=None, keepdims=False)：
numpy.std(a, axis=None, dtype=None, out=None, keepdims=False)：
在array A，取其總和(sum)、平均(mean)或標準差(std)，
而當axis=0是針對列(row)進行各列之間的統計；axis=1是針對行(column)進行各列之間的統計，
dtype可以限制其輸出型態，常見有np.float32,np.unit8，
這就請大家多加嘗試看自己希望型態長怎麼樣囉
"""

A = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
print(np.sum(A))  # output: 171
print(np.mean(A, axis=0))
# 如果先將A的型態透過np.array(A)進行變成numpy的一個物件的話，下面的操作也是可以接受的
A = np.array(A)
print(A.sum(axis=0))  # output: [21 24 27 30 33 36]
print(A.mean(axis=1))  # output:[ 3.5  9.5 15.5]
print(A.std(axis=1))  # output:[1.70782513, 1.70782513, 1.70782513]

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


""" 共同抽出

plt.annotate("(1,3)",xy = (1,3))	

plt.annotate("(3,1)",xy = (3,1))	

plt.annotate("(4,4)",xy = (4,4))	


plt.annotate("向量(1,2)",xy = (1,2))	
plt.annotate("向量(1,3)",xy = (1,3))	
ax.plot(x4,y4,"b",linestyle='--')	
ax.plot(x7,y7,"c",linestyle='--')	

"""

print("------------------------------------------------------------")  # 60個
print("np陣列")
print("------------------------------------------------------------")  # 60個

print("全零np陣列 np.zeros()")

# 全零np陣列
# np.zeros會創建一個全部為0的數組。
# np.zeros(shape, dtype = float, order = 'C')
# shape:陣列的形狀。
# Dtype:生成數組所需的數據類型。' int '或默認' float '

cc = np.zeros(5)  # 生成5個值全爲0的數組
print(cc)

cc = np.zeros((5,))
print(cc)

print("全零np陣列 3X5")
cc = np.zeros([3, 5])
print(cc)

print("全零np陣列 3X5")
cc = np.zeros((3, 5), dtype="int")
print(cc)

cc = np.zeros((2, 2))
print(cc)


print("全壹np陣列 np.ones()")

# 全壹np陣列
# np.ones函數創建一個全部為1的數組。
# np.ones(shape, dtype = None, order = 'C')

cc = np.ones(5)  # 生成5個值全爲1的數組
print(cc)

cc = np.ones((5,))
print(cc)

cc = np.ones((3, 4))
print(cc)

cc = np.ones((1, 2))
print(cc)

print("全一np陣列 3X5")
cc = np.ones([3, 5])
print(cc)


print("單位np陣列 np.eye()")


print("單位np陣列 3X3")
cc = np.eye(3)
print(cc)


print("空白np陣列 np.empty()")

a = np.empty(5)  # 生成5個元素，值爲隨機數的數組（速度快）
print(a)

c = np.empty((5,))
print(c)

print("full np陣列 np.full()")


a = np.full(5, 6)  # 生成5個值全爲6的數組
print(a)

c = np.full((2, 2), 7)  # Create a constant array
print(c)


print("diag np陣列 np.diag()")

cc = np.diag([2, 3])
print(cc)


cc1 = np.ones([3, 3])  # 3*3的全1矩陣
cc2 = np.eye(3)  # 3*3的单位阵
print(cc1 + cc2)
print(cc1 - cc2)

print("------------------------------")  # 30個

print("------------------------------------------------------------")  # 60個

print("過濾資料 where")

a = np.array([3, 6, 8, 1, 2, 88])
b = np.where(a > 5)
print("原np陣列")
print(a)
print("過濾資料 >5 的部分")
print(b)

print("------------------------------")  # 30個

a = np.array([[3, 6, 8, 77, 66], [1, 2, 88, 3, 98], [11, 2, 67, 5, 2]])
b = np.where(a > 5)
print("原np陣列")
print(a)
print("過濾資料 >5 的部分")
print(b)

print("------------------------------")  # 30個

x1 = np.linspace(-2.0, 2.0, 11)  # 包含頭尾共21點

# 移除 x1 > 0.55 的點, 就是保存 x1 <=0.6的點
x2 = x1[x1 <= 0.55]

# 遮罩 x1 > 0.7 的點, 會多了點線標記
x3 = np.ma.masked_where(x1 > 0.7, x1)

print("x1 :", x1)
print("x2 :", x2)
print("x3 :", x3)

print("------------------------------")  # 30個

print("分段函數")

x = np.arange(10)
print(x)

print(np.where(x < 5, x, 9 - x))

a = np.arange(10)
print(np.select([x < 3, x > 6], [-1, 1], 0))

a = np.arange(10)
print(np.piecewise(x, [x < 3, x > 6], [lambda x: x * 2, lambda x: x * 3]))

print("------------------------------")  # 30個

a = np.array([2, 3, 4, 5, 6])
print(f"a = {a}")
b = np.ma.masked_where(a > 3, a)
print(f"b = {b}")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


"""
np.gradient(f) 計算數組f中元素的梯度，當f為多維時，返回每個維度梯度
梯度：連續值之間的變化率，即斜率
XY坐標軸連續三個X坐標對應的Y軸值：a, b, c，其中，b的梯度是： (c‐a)/2
"""
na = np.random.randint(0, 50, (11))
print(na)
print(np.gradient(na))

print("------------------------------------------------------------")  # 60個

# 建立陣列

cc = np.array([1, 2, 3])
print(cc)

z = np.linspace(0, 15, 100)
x = np.sin(z)
y = np.cos(z)
x2 = np.sin(z)

print("------------------------------------------------------------")  # 60個

cc = np.arange(6).reshape(2, 3)  # 陣列轉成 2 x 3
print(cc)
print(cc.ravel())

print("------------------------------------------------------------")  # 60個

xx = [1, 2, 3, 4, 5]
yy = [6, 7, 8]
# x軸1~5, y軸6~8, 編織出來15個點 X, Y
X, Y = np.meshgrid(xx, yy)
print("X = \n", X)
print("Y = \n", Y)

print("------------------------------------------------------------")  # 60個

x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8])
# x軸1~5, y軸6~8, 編織出來15個點 X, Y
X, Y = np.meshgrid(x, y)

print("X = \n", X)
print("Y = \n", Y)

print("------------------------------------------------------------")  # 60個

xx = np.linspace(1, 5, 5)
yy = np.linspace(6, 8, 3)

# x軸1~5, y軸6~8, 編織出來15個點 X, Y
X, Y = np.meshgrid(xx, yy)
nprint("X = \n", X)
print("Y = \n", Y)

print("------------------------------------------------------------")  # 60個


xx = [1, 2, 3, 4, 5]
yy = [6, 7, 8]
# x軸1~5, y軸6~8, 編織出來15個點 X, Y
X, Y = np.meshgrid(xx, yy)
print("X = \n", X)
print("Y = \n", Y)

print("------------------------------------------------------------")  # 60個

x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8])
# x軸1~5, y軸6~8, 編織出來15個點 X, Y
X, Y = np.meshgrid(x, y)

print("X = \n", X)
print("Y = \n", Y)

print("------------------------------------------------------------")  # 60個

xx = np.linspace(1, 5, 5)
yy = np.linspace(6, 8, 3)
# x軸1~5, y軸6~8, 編織出來15個點 X, Y
X, Y = np.meshgrid(xx, yy)
print("X = \n", X)
print("Y = \n", Y)

print("------------------------------------------------------------")  # 60個

# 用NumPy实现拟合
# Numpy拟合基于最小二乘法

X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Y = np.array([0, 1, 2, 6, 4, 5, 6, 6, 8, 9, 10])

plt.scatter(X, Y, label="真實資料")

# 用一次多项式拟合，相当于线性拟合
z1 = np.polyfit(X.reshape(len(X)), Y, 1)
p1 = np.poly1d(z1)
print(z1)
print(p1)

y = z1[0] * X + z1[1]
plt.plot(X, y, c="red", label="線性擬合")
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# nparraylist.py

x = [1, 2]
print("x 是", type(x))
print("x[0] 的值是", x[0])
print("x * 2 = ", x * 2)
print()
y = np.array([1, 2])
print("y 是", type(y))
print("y[0] 的值是", x[0])
print("y * 2 = ", y * 2)


# npcompute1.py

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(10, 19).reshape(3, 3)
print("a 陣列內容：\n", a)
print("b 陣列內容：\n", b)
print("a 陣列元素都加值：\n", a + 1)
print("a 陣列元素都平方：\n", a**2)
print("a 陣列元素加判斷：\n", a < 5)
print("a 陣列取出第一個row都加1：\n", a[0, :] + 1)
print("a 陣列取出第一個col都加1：\n", a[:, 0] + 1)
print("a b 陣列對應元素相加：\n", a + b)
print("a b 陣列對應元素相乘：\n", a * b)

print("------------------------------------------------------------")  # 60個

# npcompute2.py

a = np.arange(1, 10).reshape(3, 3)
print("陣列的內容：\n", a)
print("1.最小值與最大值：\n", np.min(a), np.max(a))
print("2.每一直行最小值與最大值：\n", np.min(a, axis=0), np.max(a, axis=0))
print("3.每一橫列最小值與最大值：\n", np.min(a, axis=1), np.max(a, axis=1))
print("4.加總、乘積及平均值：\n", np.sum(a), np.prod(a), np.mean(a))
print("5.每一直行加總、乘積與平均值：\n", np.sum(a, axis=0), np.prod(a, axis=0), np.mean(a, axis=0))
print("6.每一橫列加總、乘積與平均值：\n", np.sum(a, axis=1), np.prod(a, axis=1), np.mean(a, axis=1))

print("------------------------------------------------------------")  # 60個

# npcompute3.py

a = np.random.randint(100, size=50)
print("陣列的內容：", a)
print("1.標準差：", np.std(a))
print("2.變異數：", np.var(a))
print("3.中位數：", np.median(a))
print("4.百分比值：", np.percentile(a, 80))
print("5.最大最小差值：", np.ptp(a))

print("------------------------------------------------------------")  # 60個

# npcreate.py

# array()
np1 = np.array([1, 2, 3, 4])  # 使用list
np2 = np.array((5, 6, 7, 8))  # 使用tuple
print("np1=", np1, type(np1))
print("np2=", np2, type(np2))
# arange()
np3 = np.arange(0, 11, 2)
print("np3=", np3)
# linespace()
np4 = np.linspace(1, 9, 3)
print("np4=", np4)
# zeros()
np5 = np.zeros((2,))
print("np5=", np5)
# ones()
np6 = np.ones((2,))
print("np6=", np6)
# empty()
np7 = np.empty((2,))
print("np7=", np7)

print("------------------------------------------------------------")  # 60個

# npinfo.py

listdata = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
na = np.array(listdata)
print(na)
print("維度", na.ndim)
print("形狀", na.shape)
print("數量", na.size)

print("------------------------------------------------------------")  # 60個

# npreshape.py

adata = np.arange(1, 17)
print(adata)
bdata = adata.reshape(4, 4)
print(bdata)

print("------------------------------------------------------------")  # 60個

# npfile.py

a = np.genfromtxt("_new/scores.csv", delimiter=",", skip_header=1)
print(a.shape)

print("------------------------------------------------------------")  # 60個

# npsort1.py

a = np.random.choice(50, size=10, replace=False)
print("排序前的陣列：", a)
print("排序後的陣列：", np.sort(a))
print("排序後的索引：", np.argsort(a))
# 用索引到陣列取值
for i in np.argsort(a):
    print(a[i], end=",")

print("------------------------------------------------------------")  # 60個

# npsort2.py

a = np.random.randint(0, 10, (3, 5))
print("原陣列內容：")
print(a)
print("將每一直行進行排序：")
print(np.sort(a, axis=0))
print("將每一橫列進行排序：")
print(np.sort(a, axis=1))

print("------------------------------------------------------------")  # 60個

# npvalue1.py

na = np.arange(0, 6)
print(na)  # [0 1 2 3 4 5]
print(na[0])  # 0
print(na[5])  # 5
print(na[1:5])  # [1 2 3 4]
print(na[1:5:2])  # [1 3]
print(na[5:1:-1])  # [5 4 3 2]
print(na[:])  # [0 1 2 3 4 5]
print(na[:3])  # [0 1 2]
print(na[3:])  # [3 4 5]

# npvalue2.py

na = np.arange(1, 17).reshape(4, 4)
print(na[2, 3])  # 12
print(na[1, 1:3])  # [6,7]
print(na[1:3, 2])  # [7,11]
print(na[1:3, 1:3])  # [[6,7],[7,11]]
print(na[::2, ::2])  # [[1,3],[9,11]]
print(na[:, 2])  # [3,7,11,15]
print(na[1, :])  # [5,6,7,8]
print(na[:, :])  # 矩陣全部

print("------------------------------------------------------------")  # 60個


a = np.array([1, 2, 3, 4, 5])
b = np.array((1, 2, 3, 4, 5))
print(type(a), type(b))
print("---------------------------")
print(a[0], a[1], a[2], a[3], a[4])
print("---------------------------")
b[0] = 5
print(b)
print("---------------------------")
b[4] = 0
print(b)

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[0, 0], a[0, 1], a[0, 2])
print(a[1, 0], a[1, 1], a[1, 2])
print("---------------------------")
a[0, 0] = 6
a[1, 2] = 1
print(a)

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3, 4, 5], int)
b = np.array((1, 2, 3, 4, 5), dtype=float)
print(a)
print("---------------------------")
print(b)

print("------------------------------------------------------------")  # 60個

a = np.arange(5)
print(a)
print("---------------------------")
b = np.arange(1, 6, 2)
print(b)
print("===========================")
c = np.zeros(2)
print(c)
print("---------------------------")
d = np.zeros((2, 2))
print(d)
print("===========================")
e = np.ones(2)
print(e)
print("---------------------------")
f = np.ones((2, 2))
print(f)
print("===========================")
g = np.full(2, 7)
print(g)
print("---------------------------")
h = np.full((2, 2), 7)
print(h)

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.zeros_like(a)
print(b)
print("===========================")
c = np.ones_like(a)
print(c)
print("===========================")
d = np.eye(3)
print(d)
print("---------------------------")
e = np.eye(3, k=1)
print(e)
print("===========================")
f = np.random.rand(3)
print(f)
print("---------------------------")
g = np.random.rand(3, 3)
print(g)

print("------------------------------------------------------------")  # 60個

a = np.arange(16)
print(a)
print("---------------------------")
b = a.reshape((4, 4))
print(b)
print("===========================")
c = np.array(range(10), float)
print(c)
print("---------------------------")
d = c.reshape((5, 2))
print(d)

print("------------------------------------------------------------")  # 60個

a = np.array(
    [
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
        [26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35],
    ]
)

print(type(a))
print(a.dtype)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.ndim)
print(a.nbytes)

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2], [3, 4], [5, 6]])
for ele in a:
    print(ele)

print("---------------------------")
for ele in a:
    for item in ele:
        print(str(item) + " ", end="")

print("------------------------------------------------------------")  # 60個

a = np.arange(10)
outputfile = "tmp_Example.npy"
with open(outputfile, "wb") as fp:
    np.save(fp, a)

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2, 3], [4, 5, 6]])
outputfile = "tmp_Example.out"
np.savetxt(outputfile, a, delimiter=",")

print("------------------------------------------------------------")  # 60個

outputfile = "tmp_Example.npy"
with open(outputfile, "rb") as fp:
    a = np.load(fp)
print(a)

print("------------------------------------------------------------")  # 60個

outputfile = "tmp_Example.out"
a = np.loadtxt(outputfile, delimiter=",")
print(a)

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3])
print("a=" + str(a))
s = 5
print("s=" + str(s))
b = a + s
print("a+s=" + str(b))
b = a - s
print("a-s=" + str(b))
b = a * s
print("a*s=" + str(b))
b = a / s
print("a/s=" + str(b))

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3])
print("a=" + str(a))
s = 5
print("s=" + str(s))
b = np.add(a, s)
print("np.add(a,s)=" + str(b))
b = np.subtract(a, s)
print("np.subtract(a,s)=" + str(b))
b = np.multiply(a, s)
print("np.multiply(a,s)=" + str(b))
b = np.divide(a, s)
print("np.divide(a,s)=" + str(b))

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3])
print("a=" + str(a))
s = np.array([4, 5, 6])
print("s=" + str(s))
b = a + s
print("a+s=" + str(b))
b = a - s
print("a-s=" + str(b))
b = a * s
print("a*s=" + str(b))
b = a / s
print("a/s=" + str(b))

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3])
print("c=" + str(a))
s = np.array([4, 5, 6])
print("s=" + str(s))
b = np.add(a, s)
print("np.add(a,s)=" + str(b))
b = np.subtract(a, s)
print("np.subtract(a,s)=" + str(b))
b = np.multiply(a, s)
print("np.multiply(a,s)=" + str(b))
b = np.divide(a, s)
print("np.divide(a,s)=" + str(b))

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3])
print("a=" + str(a))
s = np.array([4, 5, 6])
print("s=" + str(s))
b = a.dot(s)
print("a.dot(s)=" + str(b))

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("a=" + str(a))

b = a[1:3]  # 索引 1,2
print("a[1:3]=" + str(b))
b = a[:4]  # 索引 0,1,2,3
print("a[:4]=" + str(b))
b = a[3:]  # 索引 3,4,5,6,7,8
print("a[3:]=" + str(b))
b = a[2:9:3]  # 索引 2,5,8
print("a[2:9:3]=" + str(b))
b = a[::2]  # 索引 0,2,4,6,8
print("a[::2]=" + str(b))
b = a[::-1]  # 索引 8,7,6,5,4,3,2,1,0
print("a[::-1]=" + str(b))
b = a[2:-2]  # 索引 8,7,6,5,4,3,2,1,0
print("a[2:-2]=" + str(b))

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("a=" + str(a))

print(a[0], a[2], a[-1])  # 索引 0,2,最後1個
b = a[[1, 3, 5, 7]]  # 索引 1,3,5,7
print("a[[1,3,5,7]]=" + str(b))
b = a[range(6)]  # 索引 0,1,2,3,4,5
print("a[range(6)]=" + str(b))
a[[2, 6]] = 10  # 同時更改多個索引值
print("a[[2,6]]=10->" + str(a))

print("------------------------------------------------------------")  # 60個

a = np.array([14, 8, 10, 11, 6, 3, 18, 13, 12, 9])
print("a=" + str(a))
mask = a % 3 == 0  # 建立布林值陣列
print("mask=" + str(mask))
b = a[mask]  # 使用布林值陣列取出值
print("a[mask]=" + str(b))
a[a % 3 == 0] = -1  # 同時更改多個True索引
print("a[a%3==0]=-1->" + str(a))

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2, 3], [4, 5, 6]])
print("a=")
print(a)
s = 5
print("s=" + str(s))
b = a + s
print("a+s=")
print(b)
b = a - s
print("a-s=")
print(b)
b = a * s
print("a*s=")
print(b)
b = a / s
print("a/s=")
print(b)

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2, 3], [4, 5, 6]])
print("a=")
print(a)
s = 5
print("s=" + str(s))
b = np.add(a, s)
print("np.add(a,s)=")
print(b)
b = np.subtract(a, s)
print("np.subtract(a,s)=")
print(b)
b = np.multiply(a, s)
print("np.multiply(a,s)=")
print(b)
b = np.divide(a, s)
print("np.divide(a,s)=")
print(b)

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2], [3, 4]])
print("a=")
print(a)
s = np.array([[5, 6], [7, 8]])
print("s=")
print(s)
b = a + s
print("a+s=")
print(b)
b = a - s
print("a-s=")
print(b)
b = a * s
print("a*s=")
print(b)
b = a / s
print("a/s=")
print(b)

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2], [3, 4]])
print("a=")
print(a)
s = np.array([[5, 6], [7, 8]])
print("s=")
print(s)
b = np.add(a, s)
print("np.add(a,s)=")
print(b)
b = np.subtract(a, s)
print("np.subtract(a,s)=")
print(b)
b = np.multiply(a, s)
print("np.multiply(a,s)=")
print(b)
b = np.divide(a, s)
print("np.divide(a,s)=")
print(b)

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2], [3, 4]])
print("a=")
print(a)
s = np.array([[5, 6], [7, 8]])
print("s=")
print(s)
b = a.dot(s)
print("a.dot(s)=")
print(b)

print("------------------------------------------------------------")  # 60個

a = np.arange(11, 36)
a = a.reshape(5, 5)
print("a=")
print(a)

b = a[0, 1:4]  # 索引 [0,1~3]
print("a[0,1:4]=")
print(b)
b = a[1:4, 0]  # 索引 [1~3,0]
print("a[1:4,0]=")
print(b)
b = a[:2, 1:3]  # 索引 [0~1,1~2]
print("a[:2,1:3]=")
print(b)
b = a[:, 1]  # 索引 [0~4,1]
print("a[:,1]=")
print(b)
b = a[::2, ::2]  # 索引 [0~2~4,0~2~4]
print("a[::2,::2]=")
print(b)

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("a=")
print(a)

b = a[[0, 1, 2], [0, 1, 0]]  # 索引 [0,0][1,1][2,0]
print("a[[0,1,2],[0,1,0]]=")
print(b)
b = np.array([a[0, 0], a[1, 1], a[2, 0]])  # 索引 [0,0][1,1][2,0]
print("np.array([a[0,0],a[1,1],a[2,0]])")
print(b)

idx = np.array([0, 2, 0, 1])
print("idx=" + str(idx))
b = a[np.arange(4), idx]  # 索引 [0,0][1,2][2,0][3,1]
print("a[np.arange(4),idx]=")
print(b)
a[np.arange(4), idx] += 10
print("a[np.arange(4), idx] += 10->")
print(a)

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2], [3, 4], [5, 6]])
print("a=")
print(a)

mask = a > 2
print("mask=")
print(mask)
b = a[mask]  # 使用布林值陣列取出值
print("a[mask]=" + str(b))
a[a > 2] = -1  # 同時更改多個True索引
print("a[a>2]=-1->")
print(a)

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("a=")
print(a)
print("a 形狀: " + str(a.shape))
b = np.array([1, 0, 1])
print("b=" + str(b))
print("b 形狀: " + str(b.shape))

c = a + b
print(c)

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2, 3], [4, 5, 6]])
print("a=")
print(a)

b = a.ravel()
print("a.ravel()=" + str(b))
c = a.flatten()
print("a.flatten()=" + str(c))
d = np.ravel(a)
print("np.ravel(a)=" + str(d))

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3])
print("a=" + str(a))

b = a[:, np.newaxis]
print("b=a[:,np.newaxis]->")
print(b)
print(b.shape)
b = a[np.newaxis, :]
print("b=a[np.newaxis,:]->")
print(b)
print(b.shape)

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2, 3, 4, 5, 6, 7, 8]])
b = a.reshape(2, 4)
print(b.shape)
print("---------------------------")
c = np.expand_dims(b, axis=0)
d = np.expand_dims(b, axis=1)
print(c.shape, d.shape)
print("---------------------------")
e = np.squeeze(c)
f = np.squeeze(d)
print(e.shape, f.shape)

print("------------------------------------------------------------")  # 60個

a = np.array([[11, 22, 13, 74, 35, 6, 27, 18]])

min_value = np.min(a)
max_value = np.max(a)
print("最小值: " + str(min_value))
print("最大值: " + str(max_value))

min_idx = np.argmin(a)
max_idx = np.argmax(a)
print("最小值索引: " + str(min_idx))
print("最大值索引: " + str(max_idx))

print("------------------------------------------------------------")  # 60個

a = np.array([30, 45, 60])

print(np.sin(a * np.pi / 180))
print(np.cos(a * np.pi / 180))
print(np.tan(a * np.pi / 180))

print("------------------------------------------------------------")  # 60個

print("四捨五入相關")

a = 123.456789
print(np.around(a))
print(np.around(a, decimals=3))
print(np.around(a, decimals=-3))

b = np.floor(a)
print("floor()=" + str(b))
b = np.ceil(a)
print("ceil()=" + str(b))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


# numpy的allclose方法，比较两个array是不是每一元素都相等，默认在1e-05的误差范围内

a = np.random.randn(9, 6)
b = np.random.randn(9, 6)

cc = np.allclose(a, b, a, b, a)  # 可以多個陣列
print(cc)

cc = np.allclose(a, a)
print(cc)


print("column_stack 的使用, 並排合併np陣列")
N = 10
experience1 = np.random.normal(size=N)
experience2 = np.random.normal(size=N)
print(experience1.shape)
print(type(experience1))

X = np.column_stack([experience1, experience2])
print(X.shape)

plt.scatter(X[:, 0], X[:, 1])

plt.arrow(
    x=0,
    y=0,
    dx=1,
    dy=1,
    head_width=0.2,
    head_length=0.2,
    linewidth=2,
    fc="r",
    ec="r",
)
plt.text(
    0.5,
    0.5,
    "aaaaa",
    color="r",
    fontsize=15,
    horizontalalignment="right",
    verticalalignment="top",
)

plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

