"""
numpy的使用

numpy: 數值計算的標準套件
"""

import sys
import numpy as np
import pandas as pd

print('------------------------------------------------------------')	#60個

print('建立 numpy 陣列 一維')

print('串列 轉 numpy陣列 range() 轉 numpy陣列')

x = np.array(range(10))
print(type(x))
print(x)

print('建立 numpy陣列, 使用 np.arange()')

x = np.arange(10)  # 類似 Python 的 range, 但是回傳 array
print(x)

print('建立 numpy陣列, 使用 np.linspace()')

x = np.linspace(0, 3, 4)  # 建立一個array, 在0與3的範圍之間讓4個點等分
print(x)

ST = 0
SP = 5
N = 11
xx = np.linspace(ST, SP, N, dtype = float)  # 建立一個array, 在 ST 與 SP 的範圍之間讓 N 個點等分
print(xx)

print('aaaaa')
x = np.linspace(-np.pi, np.pi, 5)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.sinc(x)
print('x', x)
print('sin(x) =', y1)
print('cos(x) =', y2)
print('tan(x) =', y3)
print('sinc(x) =', y4)

x1 = np.linspace(0, 10, num = 11)     # 使用linspace()產生陣列
print(type(x1), x1)

x2 = np.arange(0, 11, 1)              # 使用arange()產生陣列
print(type(x2), x2)

x3 = np.arange(11)                  # 簡化語法產生陣列
print(type(x3), x3)

print('串列 轉 numpy陣列')
x = np.array([1, 2, 3])
print(x)
print('每個元素的平方')
print(x ** 2)

print('串列 轉 numpy陣列')
np1 = np.array([1, 2, 3, 4])
print(type(np1))
print(np1)

print('元組 轉 numpy陣列')
np2 = np.array((5, 6, 7, 8))
print(type(np2))
print(np2)

print('------------------------------------------------------------')	#60個

print('建立np陣列')
a = np.arange(15).reshape(3, 5)
print(a)

print('np陣列存檔成np之文字格式')
np.savetxt('np_asc.txt' , a)

print('讀取np之文字格式檔案成np陣列')
b = np.loadtxt('np_asc.txt')
print(b)

print('np陣列存檔成np之binary格式')
np.save('np_bin.npy' , a)

print('讀取np之binary格式檔案成np陣列')
c = np.load('np_bin.npy')
print(c)

print('------------------------------------------------------------')	#60個

my_array = np.arange(101)   # 0 1 2 ... 100

sum_my_array = sum(my_array)
print('和')
print(sum_my_array)

print('------------------------------------------------------------')	#60個

print('numpy 統計函數')

#串列
data = [
    37, 24, 6, 51, 83, 28, 51, 58, 82, 95,
    83, 6, 42, 53, 98, 6, 90, 4, 59, 87,
    28, 17, 28, 46, 40, 53, 70, 49, 55, 41,
    74, 57, 31, 55, 5, 65, 44, 98, 36, 4
    ]

print('串列 轉 numpy陣列')
print('串列長度 :', len(data))

na = np.array(data)

print('資料型態：%s' % type(na))
print('平均值：%.2f' % np.mean(na))
print('中位數：%.2f' % np.median(na))
print('標準差：%.2f' % np.std(na))
print('變異數：%.2f' % np.var(na))
print('極差值：%.2f' % np.ptp(na))

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

print('numpy 統計函數')
na = np.arange(15).reshape(3, 5)
print(na)
print(np.sum)
print(np.sum(na))
print(np.mean(na))
print(np.mean(na, axis = 0))
print(np.mean(na, axis = 1))
print(np.average(na, axis = 0, weights = [11, 6, 2]))
print(np.std(na))
print(np.var(na))
print(np.std(na, axis = 1))
print(np.std(na, axis = 0))
print(np.std(na, axis = 1))
print(np.std(na, axis = 0))
print(np.argmax(na))
print(np.unravel_index(np.argmax(na), na.shape))
print(na)
print(np.ptp(na))

a = np.arange(1, 10).reshape(3, 3)
print('陣列的內容：\n', a)
print('1.最小值與最大值：\n', np.min(a), np.max(a))
print('2.每一直行最小值與最大值：\n', np.min(a, axis = 0), np.max(a, axis = 0))
print('3.每一橫列最小值與最大值：\n', np.min(a, axis = 1), np.max(a, axis = 1))
print('4.加總、乘積及平均值：\n', np.sum(a), np.prod(a), np.mean(a))
print('5.每一直行加總、乘積與平均值：\n', np.sum(a, axis = 0), np.prod(a, axis = 0), np.mean(a, axis = 0))
print('6.每一橫列加總、乘積與平均值：\n', np.sum(a, axis = 1), np.prod(a, axis = 1), np.mean(a, axis = 1))



print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

print('串列 轉 numpy陣列')
np1 = np.array([1, 2, 3, 4])
print(type(np1))
print(np1)

print('元組 轉 numpy陣列')
np2 = np.array((5, 6, 7, 8))
print(type(np2))
print(np2)

print('串列 轉 numpy陣列 int')
na = np.array([1, 2, 3, 4], dtype = int)
print(na)

print('串列 轉 numpy陣列 float')
na = np.array([1, 2, 3, 4], dtype = float)
print(na)

na = np.arange(0, 31, 2)
print(na)

na = np.linspace(1, 15, 3)
print(na)

a = np.zeros((5,))
print(a)

b = np.ones((5,))
print(b)

c = np.empty((5,))
print(c)

print('------------------------------------------------------------')	#60個

print('二維串列 轉 numpy陣列')

listdata = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15]]
na = np.array(listdata)
print(na)
print('維度 :', na.ndim)
print('形狀 :', na.shape)
print('數量 :', na.size)

adata = np.arange(1, 17)
print(adata)
bdata = adata.reshape(4, 4)
print(bdata)

print('------------------------------------------------------------')	#60個

na = np.arange(0, 6)
print(na)               #[0 1 2 3 4 5]
print(na[0])            #0
print(na[5])            #5
print(na[1 : 5])        #[1 2 3 4]
print(na[1 : 5 : 2])    #[1 3]
print(na[5 : 1 : -1])   #[5 4 3 2]
print(na[:])            #[0 1 2 3 4 5]
print(na[: 3])          #[0 1 2]
print(na[3 :])          #[3 4 5]

print('------------------------------------------------------------')	#60個

na = np.arange(1, 17).reshape(4, 4) # 一維的 1~16 1X16 改成 二維的 4 X 4
print(na[2, 3])			#12
print(na[1, 1:3])		#[6,7]
print(na[1:3, 2])		#[7,11]
print(na[1:3, 1:3])		#[[6,7],[7,11]]
print(na[::2, ::2])		#[[1,3],[9,11]]
print(na[:, 2])			#[3,7,11,15]
print(na[1, :])			#[5,6,7,8]
print(na[:, :])			#矩陣全部

print('------------------------------------------------------------')	#60個

#na = np.arange(0, 16) same
na = np.arange(16)   # 一維的 1~16 1X16 改成 二維的 4 X 4
print(na)
na = na.reshape(4, 4)
print(na)

print('------------------------------------------------------------')	#60個

na = np.array(range(10))
na = na.reshape(5, 2)
print(na.dtype)
print(na.size)
print(na.shape)
print(na.itemsize)
print(na.ndim)
print(na.nbytes)

print('------------------------------------------------------------')	#60個

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(10, 19).reshape(3, 3)
print('a 陣列內容：\n', a)
print('b 陣列內容：\n', b)
print('a 陣列元素都加值：\n', a + 1)
print('a 陣列元素都平方：\n', a ** 2)
print('a 陣列元素加判斷：\n', a < 5)
print('a 陣列取出第一個row都加1：\n', a[0,:] + 1)
print('a 陣列取出第一個col都加1：\n', a[:,0] + 1)
print('a b 陣列對應元素相加：\n', a + b)
print('a b 陣列對應元素相乘：\n', a * b)
print('a b 陣列點積計算：\n', np.dot(a, b))

print('------------------------------------------------------------')	#60個

print('串列 轉 numpy陣列')
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)

b, c, d = a[1:3], a[:4], a[3:]
print(b, c, d)

print('------------------------------------------------------------')	#60個

print('二維串列 轉 numpy陣列')
b = np.array([[1, 2], [3, 4], [5, 6]])
print(b)

c = b.T
print(c)

c = b.transpose()
print(c)

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




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


"""
50個常用的Numpy函數解釋，參數和使用示例

Numpy是python中最有用的工具之一。它可以有效地處理大容量數據。使用NumPy的最大原因之一是它有很多處理數組的函數。在本文中，將介紹NumPy在數據科學中最重要和最有用的一些函數。
"""
print('創建數組 Array')

#它用于創建一維或多維數組
#array(object, dtype = None, *, copy = True, order = 'K', subok = False, ndmin = 0)
#Dtype:生成數組所需的數據類型。
#ndim:指定生成數組的最小維度數。

print('串列 轉 numpy陣列')
na = np.array([1, 2, 3, 4, 5]) 
print(na)

#還可以使用此函數將pandas的df和series轉為NumPy數組。

sex = pd.Series(['Male','Male','Female']) 
na = np.array(sex) 
print(na)

print('創建數組 Linspace')

#創建一個具有指定間隔的浮點數的數組。
#np.linspace(start, stop, num=50, endpoint = True, retstep = False, dtype = None, axis = 0)
#start:起始數字
#end:結束
#Num:要生成的樣本數，默認為50。

na = np.linspace(10, 100, 10) 
print(na)

print('創建數組 Arange')
#在給定的間隔內返回具有一定步長的整數。
#np.arange(start, stop, step, dtype = None)
#step:數值步長。

na = np.arange(5, 10, 2)
print(na)

print('創建數組 Logspace')

#在對數尺度上生成間隔均勻的數字。
#np.logspace(start, stop, num = 50, endpoint = True, base = 10.0, dtype = None, axis = 0)
#Start:序列的起始值。
#End:序列的最后一個值。
#endpoint:如果為True，最后一個樣本將包含在序列中。
#base:底數。默認是10。

na = np.logspace(0, 10, 5,base = 2)
print(na)

print('創建數組 zeroes')

#np.zeroes會創建一個全部為0的數組。
#np.zeros(shape, dtype = float, order = 'C')
#shape:陣列的形狀。
#Dtype:生成數組所需的數據類型。' int '或默認' float '

na = np.zeros((2, 3), dtype = 'int') 
print(na)

na = np.zeros(5) 
print(na)

print('創建數組 ones')
#np.ones函數創建一個全部為1的數組。
#np.ones(shape, dtype = None, order = 'C')

na = np.ones((3, 4))
print(na)

print('創建數組 full')
#創建一個單獨值的n維數組。
#np.full(shape, fill_value, dtype = None)
#fill_value:填充值。

na = np.full((2, 4), fill_value = 2)
print(na)

print('創建數組 Identity')
#創建具有指定維度的單位矩陣。
#np.identity(n, dtype = None)

na = np.identity(4) 
print(na)

#數組操作

print('min 返回數組中的最小值。')
#np.min(a, axis = None, out = None, ...)
#axis:用于操作的軸。
#out:用于存儲輸出的數組。

print('串列 轉 numpy陣列')
arr = np.array([1, 1, 2, 3, 3, 4, 5, 6, 6, 2]) 
na = np.min(arr) 
print(na)

print('max 返回數組中的最大值。')
#np.max(a, axis = None, out = None, ...)
na = np.max(arr) 
print(na)

print('unique 返回一個所有唯一元素排序的數組。')
#np.unique(ar, return_index = Fasle, return_inverse = Fasle, return_counts = Fasle, axis = None)
#return_index:如果為True，返回數組的索引。

#return_inverse:如果為True，返回唯一數組的下標。

#return_counts:如果為True，返回數組中每個唯一元素出現的次數。

#axis:要操作的軸。默認情況下，數組被認為是扁平的。

na = np.unique(arr, return_counts = True)
print(na)

print('mean 返回數組的平均數')
#np.mean(a, axis = None, dtype = None, out = None)
na = np.mean(arr, dtype = 'int')

print(na)

print('medain 返回數組的中位數。')
#np.median(a, axis = None, out = None)
print('二維串列 轉 numpy陣列')
arr = np.array([[1, 2, 3], [5, 8, 4]]) 
na = np.median(arr) 

print(na)

print('digitize 返回輸入數組中每個值所屬的容器的索引。')
#np.digitize(x, bins, right = False)
#bin：容器的數組。
#right:表示該間隔是否包括右邊或左邊的bin。

print('串列 轉 numpy陣列')
a = np.array([-0.9, 0.5, 0.9, 1, 1.2, 1.4, 3.6, 4.7, 5.3]) 
bins = np.array([0, 1, 2, 3]) 
na = np.digitize(a,bins) 
print(na)

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

print('reshape 它是NumPy中最常用的函數之一。它返回一個數組，其中包含具有新形狀的相同數據。')
#np.reshape(shape)

A = np.random.randint(15, size = (4, 3))
print(A)
 
na = A.reshape(3, 4)
print(na)

na = A.reshape(-1)
print(na)

print('expand_dims 它用于擴展數組的維度。')
#np.expand_dims(a, axis)
print('串列 轉 numpy陣列')
arr = np.array([8, 14, 1, 8, 11, 4, 9, 4, 1, 13, 13, 11])
na = np.expand_dims(A, axis = 0)
print(na)

na = np.expand_dims(A, axis = 1)
print(na)

print('squeeze 通過移除一個單一維度來降低數組的維度。')
#np.squeeze(a, axis = None)

print('串列 轉 numpy陣列')
arr = np.array([[8], [14], [1], [8], [11], [4], [9], [4], [1], [13], [13], [11]]) 
na = np.squeeze(arr)
print(na)

print('count_nonzero 計算所有非零元素并返回它們的計數。')
#np.count_nonzero(a, axis = None, ...)

print('串列 轉 numpy陣列')
a = np.array([0, 0, 1, 1, 1, 0]) 
na = np.count_nonzero(a)
print(na)

print('argwhere 查找并返回非零元素的所有下標。')
#np.argwhere(a)

print('串列 轉 numpy陣列')
a = np.array([0, 0, 1, 1, 1, 0]) 
na = np.argwhere(a)
print(na)

print('argmax & argmin argmax返回數組中Max元素的索引。它可以用于多類圖像分類問題中獲得高概率預測標簽的指標。')
#np.argmax(a, axis = None, out = None)
print('串列 轉 numpy陣列')
arr = np.array([[0.12, 0.64, 0.19, 0.05]]) 
na = np.argmax(arr) 
print(na)

print('argmin將返回數組中min元素的索引。')
#np.argmin(a, axis = None, out = None)
na = np.argmin(min) 
print(na)

print('sort 對數組排序。')
#np.sort(a, axis = -1, kind = None, order = None)
#kind:要使用的排序算法。{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}

print('串列 轉 numpy陣列')
arr = np.array([2, 3, 1, 7, 4, 5]) 
na = np.sort(arr)
print(na)


print('abs 返回數組中元素的絕對值。當數組中包含負數時，它很有用。')
#TBD
print('串列 轉 numpy陣列')
#A = np.array([[1, -3, 4], [-2, -4, 3]])np.abs(A) 
#print(A)

print('round 將浮點值四舍五入到指定數目的小數點。')
#np.round(a, decimals = 0, out = None)
#decimals:要保留的小數點的個數。

na = np.random.random(size = (3, 4))
print(na)

na = np.round(a,decimals = 0)
print(na)

na = np.round(a,decimals = 1)
print(na)

print('clip 它可以將數組的裁剪值保持在一個范圍內。')

print('串列 轉 numpy陣列')
arr = np.array([0, 1, -3, -4, 5, 6, 7, 2, 3]) 
na = arr.clip(0, 5)
print(na)

na = arr.clip(0, 3)
print(na)

na = arr.clip(3, 5)
print(na)

print('替換數組中的值 where put copyto')

print('where 返回滿足條件的數組元素。')
#np.where(condition, [x, y])
#condition:匹配的條件。如果true則返回x，否則y。

na = np.arange(12).reshape(4, 3)
print(na)

na = np.where(a > 5)      ## Get The Index
print(na)
 
na = a[np.where(a > 5)]  ## Get Values
print(na)

#它還可以用來替換pandas df中的元素。

#na = np.where(data[feature].isnull(), 1, 0)
#print(na)

print('put 用給定的值替換數組中指定的元素。')
#np.put(a, ind, v)
#a:數組
#Ind:需要替換的索引。
#V:替換值。

print('串列 轉 numpy陣列')
na = np.array([1, 2, 3, 4, 5, 6]) 
print(na)
 
na = np.put(arr, [1, 2], [6, 7]) 
print(na)

print('copyto 將一個數組的內容復制到另一個數組中。')
#np.copyto(dst, src, casting = 'same_kind', where = True)
#dst：目標
#src：來源

print('串列 轉 numpy陣列')
arr1 = np.array([1, 2, 3])
print('串列 轉 numpy陣列')
arr2 = np.array([4, 5, 6])

print("Before arr1", arr1)
print("Before arr2", arr1)
np.copyto(arr1, arr2)
print("After arr1", arr1)
print("After arr2", arr2)

#集合操作

print('查找公共元素 intersect1d函數以排序的方式返回兩個數組中所有唯一的值。')
#np.intersect1d(arg1, arg2, assume_unique = False, return_indices = False)
#Assume_unique:如果為真值，則假設輸入數組都是唯一的。
#Return_indices:如果為真，則返回公共元素的索引。

print('串列 轉 numpy陣列')
ar1 = np.array([1, 2, 3, 4, 5, 6]) 
ar2 = np.array([3, 4, 5, 8, 9, 1]) 
np.intersect1d(ar1, ar2) 
 
np.intersect1d(ar1, ar2, return_indices = True) 

print('查找不同元素 np.setdiff1d函數返回arr1中在arr2中不存在的所有唯一元素。')
print('串列 轉 numpy陣列')
a = np.array([1, 7, 3, 2, 4, 1]) 
b = np.array([9, 2, 5, 6, 7, 8]) 
np.setdiff1d(a, b) 

print('從兩個數組中提取唯一元素 Setxor1d 將按順序返回兩個數組中所有唯一的值。')
print('串列 轉 numpy陣列')
a = np.array([1, 2, 3, 4, 6]) 
b = np.array([1, 4, 9, 4, 36]) 
np.setxor1d(a,b) 

print('合并 Union1d函數將兩個數組合并為一個。')
print('串列 轉 numpy陣列')
a = np.array([1, 2, 3, 4, 5]) 
b = np.array([1, 3, 5, 4, 36]) 
np.union1d(a,b) 

#數組分割

print('水平分割 Hsplit函數將數據水平分割為n個相等的部分。')
print('二維串列 轉 numpy陣列')
A = np.array([[3, 4, 5, 2], [6, 7, 2, 6]]) 
np.hsplit(A, 2)    ## splits the data into two equal parts 
 
np.hsplit(A, 4)    ## splits the data into four equal parts 

print('垂直分割 Vsplit將數據垂直分割為n個相等的部分。')
print('二維串列 轉 numpy陣列')
A = np.array([[3, 4, 5, 2], [6, 7, 2, 6]]) 
np.vsplit(A, 2) 

#數組疊加

print('水平疊加 hstack 將在另一個數組的末尾追加一個數組。')
print('串列 轉 numpy陣列')
a = np.array([1, 2, 3, 4, 5]) 
b = np.array([1, 4, 9, 16, 25]) 
 
na = np.hstack((a, b))
print(na)
      
print('垂直疊加 vstack將一個數組堆疊在另一個數組上。')

na = np.vstack((a, b))
print(na)
      
#數組比較

print('allclose 如果兩個數組的形狀相同，則Allclose函數根據公差值查找兩個數組是否相等或近似相等。')

print('串列 轉 numpy陣列')
a = np.array([0.25, 0.4, 0.6, 0.32]) 
b = np.array([0.26, 0.3, 0.7, 0.32]) 
 
tolerance = 0.1           ## Total Difference  
np.allclose(a, b, tolerance) 
 
tolerance = 0.5 
np.allclose(a, b, tolerance) 

print('equal 它比較兩個數組的每個元素，如果元素匹配就返回True。')

np.equal(arr1, arr2) 

#重復的數組元素

print('repeat 它用于重復數組中的元素n次。')
#np.repeat(a, repeats, axis = None)

#A:重復的元素

#Repeats:重復的次數。

na = np.repeat('2017', 3)
print(na)


#讓我們來看一個更實際的示例，我們有一個包含按年數量銷售的數據集。

fruits = pd.DataFrame([
    ['Mango', 40],
    ['Apple', 90],
    ['Banana', 130]
    ],columns=['Product','ContainerSales'])
print(fruits)

#在數據集中，缺少年份列。我們嘗試使用numpy添加它。

fruits['year'] = np.repeat(2020, fruits.shape[0])
print(fruits)

print('tile 通過重復A，rep次來構造一個數組。')
#np.tile(A, reps)

na = np.tile("Ram", 5)
print(na)
 
na = np.tile(3, (2, 3))
print(na)

#愛因斯坦求和

print('einsum 此函數用于計算數組上的多維和線性代數運算。')

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(21, 30).reshape(3, 3)
 
na = np.einsum('ii->i', a)
print(na)

na = np.einsum('ji', a)
print(na)

na = np.einsum('ij,jk', a, b)
print(na)

na = np.einsum('ii', a)
print(na)

#統計分析

print('直方圖 這是Numpy的重要統計分析函數，可計算一組數據的直方圖值。')

print('二維串列 轉 numpy陣列')
A = np.array([[3, 4, 5, 2],
              [6, 7, 2, 6]])
na = np.histogram(A) 
print(na)

print('百分位數 沿指定軸計算數據的Q-T-T百分位數。')

#a:輸入。
#q:要計算的百分位。
#overwrite_input:如果為true，則允許輸入數組修改中間計算以節省內存。
print('二維串列 轉 numpy陣列')
a = np.array([[2, 4, 6], [4, 8, 12]])
na = np.percentile(a, 50)
print(na)
na = np.percentile(a, 10)
print(na)
arr = np.array([2, 3, 4, 1, 6, 7])
na = np.percentile(a, 5)
print(na)

print('標準偏差和方差 std和var是NumPy的兩個函數，用于計算沿軸的標準偏差和方差。')

print('二維串列 轉 numpy陣列')
a = np.array([[2, 4, 6], [4, 8, 12]]) 
 
na = np.std(a,axis = 1) 
print(na) 
na = np.std(a,axis = 0)    ## Column Wise 
print(na)
na = np.var(a,axis = 1) 
print(na) 
na = np.var(a,axis = 0) 
print(na)

#數組打印

print('顯示帶有兩個十進制值的浮點數')

np.set_printoptions(precision = 2)

print('串列 轉 numpy陣列')
na = np.array([12.23456, 32.34535]) 
print(na) 

print('設置打印數組最大值')

na = np.set_printoptions(threshold = np.inf)
print(na)

print('增加一行中元素的數量')

na = np.set_printoptions(linewidth = 100) ## 默認是 75
print(na)

#保存和加載數據

print('保存')

#savetxt用于在文本文件中保存數組的內容。

arr = np.linspace(10, 100, 500).reshape(25, 20)
np.savetxt('array.txt', arr)

print('加載')

#用于從文本文件加載數組，它以文件名作為參數。

np.loadtxt('array.txt') 

print('------------------------------------------------------------')	#60個

x1 = [7, 2, 11, 9, 20]
print(f'中位數 = {np.median(x1)}')

x1 = [30, 7, 2, 11, 9, 20]
print(f'中位數 = {np.median(x1)}')

print('------------------------------------------------------------')	#60個

print('串列 轉 numpy陣列')
x1 = np.array([0, 1, 1, 3, 2, 1])
# 因為 x1 元素最大值是 3, 所以 bin 是 4
print(f'np.bincount = {np.bincount(x1)}')       

print('串列 轉 numpy陣列')
x2 = np.array([0, 1, 1, 7, 2, 1])
# 因為 x2 元素最大值是 7, 所以 bin 是 8
print(f'np.bincount = {np.bincount(x2)}') 

print('------------------------------------------------------------')	#60個

print('串列 轉 numpy陣列')
x1 = np.array([0, 1, 1, 3, 2, 1])
# 因為 x1 元素最大值是 3, 所以 bin 是 4
print(f'np.bincount = {np.bincount(x1)}')
print(f'mode        = {np.argmax(np.bincount(x1))}')

print('串列 轉 numpy陣列')
x2 = np.array([0, 1, 1, 7, 2, 1])
# 因為 x2 元素最大值是 7, 所以 bin 是 8
print(f'np.bincount = {np.bincount(x2)}') 
print(f'mode        = {np.argmax(np.bincount(x1))}')

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import math

print('------------------------------------------------------------')	#60個

print('串列 轉 numpy陣列')
a = np.array([1, 1])
b = np.array([5, 5])
c = np.array([1, 5])
d = np.array([5, 1])

ab = b - a                              # 向量ab
cd = d - c                              # 向量bc

norm_a = np.linalg.norm(ab)             # 計算向量大小
norm_b = np.linalg.norm(cd)             # 計算向量大小
                    
dot_ab = np.dot(ab, cd)                 # 計算向量內積

cos_angle = dot_ab / (norm_a * norm_b)  # 計算cos值
rad = math.acos(cos_angle)              # acos轉成弧度
deg = math.degrees(rad)                 # 轉成角度
print('角度是 = {}'.format(deg))

print('------------------------------------------------------------')	#60個

def cosine_similarity(va, vb):
    norm_a = np.linalg.norm(va)                 # 計算向量大小
    norm_b = np.linalg.norm(vb)                 # 計算向量大小
    dot_ab = np.dot(va, vb)                     # 計算向量內積
    return (dot_ab / (norm_a * norm_b))         # 回傳相似度

print('串列 轉 numpy陣列')
a = np.array([2, 1, 1, 1, 0, 0, 0, 0])
b = np.array([1, 1, 0, 0, 1, 1, 1, 0])
c = np.array([1, 1, 0, 0, 1, 1, 0, 1])
print('a 和 b 相似度 = {0:5.3f}'.format(cosine_similarity(a, b)))
print('a 和 c 相似度 = {0:5.3f}'.format(cosine_similarity(a, c)))
print('b 和 c 相似度 = {0:5.3f}'.format(cosine_similarity(b, c)))

print('------------------------------------------------------------')	#60個

print('兩陣列的相關係數')
print('串列 轉 numpy陣列')
x = np.array([8, 9, 10, 7, 8, 9, 5, 7, 9, 8])
y = np.array([12, 15, 16, 18, 6, 11, 3, 12, 11, 16])
print('x陣列長度 :', len(x))
print('y陣列長度 :', len(y))
x_mean = np.mean(x)
y_mean = np.mean(y)

xi_x = [v - x_mean  for v in x]
yi_y = [v - y_mean  for v in y]

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
r = v1 / ((v2 ** 0.5) * (v3 ** 0.5))
print('相關係數 : {}'.format(r))

print('------------------------------------------------------------')	#60個

print('串列 轉 numpy陣列')
x = np.array([8, 9, 10, 7, 8, 9, 5, 7, 9, 8])
y = np.array([12, 15, 16, 18, 6, 11, 3, 12, 11, 16])             
x_mean = np.mean(x)
y_mean = np.mean(y)
xpt1 = np.linspace(0, 12, 12)      
ypt1 = [y_mean for xp in xpt1]          # 平均購買次數
ypt2 = np.linspace(0, 20, 20)
xpt2 = [x_mean for yp in ypt2]          # 平均滿意度

plt.scatter(x, y)                       # 滿意度 vs 購買次數
plt.plot(xpt1, ypt1, 'ro-')               # 平均購買次數
plt.plot(xpt2, ypt2, 'go-')               # 平均滿意度
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個

print('串列 轉 numpy陣列')
a = np.array([4, 2])
b = np.array([1, 3])

norm_a = np.linalg.norm(a)              # 計算向量大小
norm_b = np.linalg.norm(b)              # 計算向量大小
                    
dot_ab = np.dot(a, b)                   # 計算向量內積

cos_angle = dot_ab / (norm_a * norm_b)  # 計算cos值
rad = math.acos(cos_angle)              # acos轉成弧度

area = norm_a * norm_b * math.sin(rad) / 2
print('area = {0:5.2f}'.format(area))

print('------------------------------------------------------------')	#60個

print('串列 轉 numpy陣列')
a = np.array([4, 2])
b = np.array([1, 3])

ab_cross = np.cross(a, b)               # 計算向量外積
area = np.linalg.norm(ab_cross) / 2     # 向量長度除以2
                    
print('area = {0:5.2f}'.format(area))

print('------------------------------------------------------------')	#60個

print('串列 轉 numpy陣列')
x = np.array([1, 2, 3])         # 1 x 3 陣列 x
y = np.array([2, 3, 4])         # 1 x 3 陣列 y
print(f'x = {x}')
print(f'y = {y}')

print()

y = y.reshape(-1, 1)            # y 改為 3 x 1 陣列 
print(f'新的 y = \n{y}')

print()

print(f'x + y = \n{x+y}')

print('------------------------------------------------------------')	#60個

#Python numpy 寫入 csv 
#將 numpy array 用 savetxt 寫入 csv

arr = np.asarray([
  [1,2,3],
  [4,5,6],
  [7,8,9]
  ])

print(type(arr)) # <class 'numpy.ndarray'>
np.savetxt('output_data1.csv', arr, delimiter = ',')
np.savetxt('output_data2.csv', arr, delimiter = ',', fmt = '%d')
np.savetxt('output_data3.csv', arr, delimiter = ',', fmt = '%.2f')

print('------------------------------------------------------------')	#60個


x = np.array( [[40, 70, 25], [75, 80, 65], [80, 90, 100]])

print(x.shape)
print(x)

y = x.reshape(1, 9)
print(y.shape)
print(y)

y = x.ravel()
print(y.shape)
print(y)

x = [1, 2, 3, 4, 5, 6]
print(x)





print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

a = np.array([3, 6, 8, 1, 2, 88])
b = np.where(a > 5)
print(a)
print(b)

print('------------------------------------------------------------')	#60個

a = np.array([[3, 6, 8, 77, 66],
              [1, 2, 88, 3, 98],
              [11, 2, 67, 5, 2]])
b = np.where(a > 5)
print(a)
print(b)

print('------------------------------------------------------------')	#60個

list2d = np.arange(18).reshape(3,6)
print(list2d)
h, w = list2d.shape[::]
print(h, w)
w, h = list2d.shape[::-1]
print(w, h)

print('------------------------------------------------------------')	#60個

list2d = np.arange(18).reshape(3,6)
print(list2d)
print(list2d[::-1])

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

xx = [1,2,3,4]
yy = [5,6,7,8]
X, Y = np.meshgrid(xx,yy)
print(X, Y)

X, Y = np.meshgrid(np.linspace(-7, 7, 30), np.linspace(-7, 7, 30))
print(X, Y)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


