"""
numpy的使用

numpy: 數值計算的標準套件
"""

import sys
import numpy as np
import pandas as pd

print('------------------------------------------------------------')	#60個

print('建立陣列 np.array')
x = np.array([1, 2, 3])
print(x)
print('每個元素的平方')
print(x ** 2)

np1 = np.array([1, 2, 3, 4])	#串列 轉 np.array
print(type(np1))
print(np1)

np2 = np.array((5, 6, 7, 8))	#元組 轉 np.array
print(type(np2))
print(np2)

x = np.array(range(10))
print(x)

print('建立陣列 np.arange')
x = np.arange(10)  # 類似 Python 的 range, 但是回傳 array
print(x)

print('建立陣列 np.linspace')

x = np.linspace(0, 3, 4)  # 建立一個array, 在0與3的範圍之間讓4個點等分
print(x)

ST = 0
SP = 5
N = 11
xx = np.linspace(ST, SP, N, dtype = float)  # 建立一個array, 在 ST 與 SP 的範圍之間讓 N 個點等分
print(xx)

print('------------------------------------------------------------')	#60個

print('基本運算')
x = np.linspace(-np.pi, np.pi, 11) 
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.sinc(x)
print('x', x)
print('sin(x) =', y1)
print('cos(x) =', y2)
print('tan(x) =', y3)
print('sinc(x) =', y4)

print('------------------------------------------------------------')	#60個

data = [37, 24, 6, 51, 83, 28, 51, 58, 82, 95,
8, 43, 86, 78, 71, 82, 58, 10, 15, 56,
4, 75, 6, 95, 23, 79, 90, 35, 72, 25,
50, 29, 44, 67, 67, 61, 40, 44, 13, 59,
60, 67, 93, 69, 71, 8, 76, 81, 17, 72,
83, 6, 42, 53, 98, 6, 90, 4, 59, 87,
28, 17, 28, 46, 40, 53, 70, 49, 55, 41,
74, 57, 31, 55, 5, 65, 44, 98, 36, 4]

data = np.array(data)

print('資料型態：%s' % type(data))
print('平均值：%.2f' % np.mean(data))
print('中位數：%.2f' % np.median(data))
print('標準差：%.2f' % np.std(data))
print('變異數：%.2f' % np.var(data))
print('極差值：%.2f' % np.ptp(data))

np1 = np.array([1, 2, 3, 4])	#串列 轉 np.array
np2 = np.array((5, 6, 7, 8))	#元組 轉 np.array
print(np1)
print(np2)
print(type(np1), type(np2))

na = np.array([1, 2, 3, 4], dtype = int)
print(na)
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

listdata = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15]]
na = np.array(listdata)
print(na)
print('維度', na.ndim)
print('形狀', na.shape)
print('數量', na.size)

adata = np.arange(1, 17)
print(adata)
bdata = adata.reshape(4, 4)
print(bdata)

print('------------------------------------------------------------')	#60個

na = np.arange(0, 6)
print(na)           #[0 1 2 3 4 5]
print(na[0])        #0
print(na[5])        #5
print(na[1:5])      #[1 2 3 4]
print(na[1:5:2])    #[1 3]
print(na[5:1:-1])   #[5 4 3 2]
print(na[:])        #[0 1 2 3 4 5]
print(na[:3])       #[0 1 2]
print(na[3:])       #[3 4 5]

print('------------------------------------------------------------')	#60個

na = np.arange(1, 17).reshape(4, 4)
print(na[2, 3])			#12
print(na[1, 1:3])		#[6,7]
print(na[1:3, 2])		#[7,11]
print(na[1:3, 1:3])		#[[6,7],[7,11]]
print(na[::2, ::2])		#[[1,3],[9,11]]
print(na[:, 2])			#[3,7,11,15]
print(na[1, :])			#[5,6,7,8]
print(na[:, :])			#矩陣全部


print('------------------------------------------------------------')	#60個

a = np.arange(16)
print(a)
b = a.reshape((4, 4))
print(b)

print('------------------------------------------------------------')	#60個

#arrange?
a = np.arange(11, 36)
a = a.reshape(5, 5)
print(a)

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

a = np.arange(1, 10).reshape(3, 3)
print('陣列的內容：\n', a)
print('1.最小值與最大值：\n', np.min(a), np.max(a))
print('2.每一直行最小值與最大值：\n', np.min(a, axis = 0), np.max(a, axis = 0))
print('3.每一橫列最小值與最大值：\n', np.min(a, axis = 1), np.max(a, axis = 1))
print('4.加總、乘積及平均值：\n', np.sum(a), np.prod(a), np.mean(a))
print('5.每一直行加總、乘積與平均值：\n', np.sum(a, axis = 0), np.prod(a, axis = 0), np.mean(a, axis = 0))
print('6.每一橫列加總、乘積與平均值：\n', np.sum(a, axis = 1), np.prod(a, axis = 1), np.mean(a, axis = 1))

print('------------------------------------------------------------')	#60個

a = np.array(range(10))
b = a.reshape((5, 2))
print(b.dtype)
print(b.size)
print(b.shape)
print(b.itemsize)
print(b.ndim)
print(b.nbytes)

print('------------------------------------------------------------')	#60個

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)
b, c, d = a[1:3], a[:4], a[3:]
print(b, c, d)

print('------------------------------------------------------------')	#60個

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
print('numpy 统计函数')

a=np.arange(15).reshape(3,5)

print(a)

print(np.sum)

print(np.sum(a))

print(np.mean(a))

print(np.mean(a,axis=0))

print(np.mean(a,axis=1))

print(np.average(a,axis=0,weights=[11,6,2]))

print(np.std(a))

print(np.var(a))

print(np.std(a,axis=1))

print(np.std(a,axis=0))

print(np.std(a,axis=1))

print(np.std(a,axis=0))

print(np.argmax(a))

print(np.unravel_index(np.argmax(a), a.shape))

print(a)

print(np.ptp(a))


"""
np.gradient(f) 计算数组f中元素的梯度，当f为多维时，返回每个维度梯度

梯度：连续值之间的变化率，即斜率

XY坐标轴连续三个X坐标对应的Y轴值：a, b, c，其中，b的梯度是： (c‐a)/2
"""

a=np.random.randint(0,50,(11))

print(a)

print(np.gradient(a))

b=np.random.randint(0,50,(11))

print(b)

print(np.gradient(b))




print('------------------------------------------------------------')	#60個



"""
50个常用的Numpy函数解释，参数和使用示例

Numpy是python中最有用的工具之一。它可以有效地处理大容量数据。使用NumPy的最大原因之一是它有很多处理数组的函数。在本文中，将介绍NumPy在数据科学中最重要和最有用的一些函数。
"""
print('創建數組 Array')

#它用于创建一维或多维数组
#array(object, dtype = None, *, copy = True, order = 'K', subok = False, ndmin = 0)
#Dtype:生成数组所需的数据类型。
#ndim:指定生成数组的最小维度数。

tt = np.array([1,2,3,4,5]) 
print(tt)

#还可以使用此函数将pandas的df和series转为NumPy数组。

sex = pd.Series(['Male','Male','Female']) 
tt = np.array(sex) 
print(tt)

print('創建數組 Linspace')

#创建一个具有指定间隔的浮点数的数组。
#np.linspace(start, stop, num=50, endpoint = True, retstep = False, dtype = None, axis = 0)
#start:起始数字
#end:结束
#Num:要生成的样本数，默认为50。

tt = np.linspace(10,100,10) 
print(tt)

print('創建數組 Arange')
#在给定的间隔内返回具有一定步长的整数。
#np.arange(start, stop, step, dtype = None)
#step:数值步长。

tt = np.arange(5,10,2) 
print(tt)

print('創建數組 Uniform')
#np.uniform(low = 0.0, high = 1.0, size = None)
#在上下限之间的均匀分布中生成随机样本。

tt = np.random.uniform(5,10,size = 4) 
print(tt)
 
tt = np.random.uniform(size = 5) 
print(tt)
 
tt = np.random.uniform(size = (2,3)) 
print(tt)

print('創建數組 Random.randint')
#在一个范围内生成n个随机整数样本。
#np.random.randint(low, high = None, size = None, dtype = int)
tt = np.random.randint(5,10,10) 
print(tt)

print('創建數組 Random.random')
#生成N个随机浮点数样本。
#np.random(size = None)
N = 10
tt = np.random.random(N)
print(tt)

print('創建數組 Logspace')

#在对数尺度上生成间隔均匀的数字。
#np.logspace(start, stop, num = 50, endpoint = True, base = 10.0, dtype = None, axis = 0)
#Start:序列的起始值。
#End:序列的最后一个值。
#endpoint:如果为True，最后一个样本将包含在序列中。
#base:底数。默认是10。

tt = np.logspace(0,10,5,base=2) 
print(tt)

print('創建數組 zeroes')

#np.zeroes会创建一个全部为0的数组。
#np.zeros(shape, dtype = float, order = 'C')
#shape:阵列的形状。
#Dtype:生成数组所需的数据类型。' int '或默认' float '

tt = np.zeros((2,3),dtype='int') 
print(tt)

tt = np.zeros(5) 
print(tt)

print('創建數組 ones')
#np.ones函数创建一个全部为1的数组。
#np.ones(shape, dtype = None, order = 'C')

tt = np.ones((3,4)) 
print(tt)

print('創建數組 full')
#创建一个单独值的n维数组。
#np.full(shape, fill_value, dtype = None)
#fill_value:填充值。

tt = np.full((2,4),fill_value=2) 
print(tt)

print('創建數組 Identity')
#创建具有指定维度的单位矩阵。
#np.identity(n, dtype = None)

tt = np.identity(4) 
print(tt)

#数组操作

print('min 返回数组中的最小值。')
#np.min(a, axis = None, out = None, ...)
#axis:用于操作的轴。
#out:用于存储输出的数组。

arr = np.array([1,1,2,3,3,4,5,6,6,2]) 
tt = np.min(arr) 
print(tt)

print('max 返回数组中的最大值。')
#np.max(a, axis = None, out = None, ...)
tt = np.max(arr) 
print(tt)

print('unique 返回一个所有唯一元素排序的数组。')
#np.unique(ar, return_index = Fasle, return_inverse = Fasle, return_counts = Fasle, axis = None)
#return_index:如果为True，返回数组的索引。

#return_inverse:如果为True，返回唯一数组的下标。

#return_counts:如果为True，返回数组中每个唯一元素出现的次数。

#axis:要操作的轴。默认情况下，数组被认为是扁平的。

tt = np.unique(arr,return_counts=True)
print(tt)

print('mean 返回数组的平均数')
#np.mean(a, axis = None, dtype = None, out = None)
tt = np.mean(arr, dtype = 'int')

print(tt)

print('medain 返回数组的中位数。')
#np.median(a, axis = None, out = None)
arr = np.array([[1, 2, 3], [5, 8, 4]]) 
tt = np.median(arr) 

print(tt)

print('digitize 返回输入数组中每个值所属的容器的索引。')
#np.digitize(x, bins, right = False)
#bin：容器的数组。
#right:表示该间隔是否包括右边或左边的bin。

a = np.array([-0.9, 0.5, 0.9, 1, 1.2, 1.4, 3.6, 4.7, 5.3]) 
bins = np.array([0, 1, 2, 3]) 
tt = np.digitize(a,bins) 
print(tt)

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

print('reshape 它是NumPy中最常用的函数之一。它返回一个数组，其中包含具有新形状的相同数据。')
#np.reshape(shape)

A = np.random.randint(15,size=(4,3)) 
print(A)
 
tt = A.reshape(3,4) 
print(tt)

tt = A.reshape(-1)   
print(tt)

print('expand_dims 它用于扩展数组的维度。')
#np.expand_dims(a, axis)
arr = np.array([ 8, 14,  1,  8, 11,  4,  9,  4, 1, 13, 13, 11]) 
tt = np.expand_dims(A,axis=0) 
print(tt)

tt = np.expand_dims(A,axis=1) 
print(tt)

print('squeeze 通过移除一个单一维度来降低数组的维度。')
#np.squeeze(a, axis = None)

arr = np.array([[ 8],[14],[ 1],[ 8],[11],[ 4],[ 9],[ 4],[ 1],[13],[13],[11]]) 
tt = np.squeeze(arr)
print(tt)


print('count_nonzero 计算所有非零元素并返回它们的计数。')
#np.count_nonzero(a, axis = None, ...)

a = np.array([0, 0, 1, 1, 1, 0]) 
tt = np.count_nonzero(a)
print(tt)

print('argwhere 查找并返回非零元素的所有下标。')
#np.argwhere(a)

a = np.array([0, 0, 1, 1, 1, 0]) 
tt = np.argwhere(a)
print(tt)

print('argmax & argmin argmax返回数组中Max元素的索引。它可以用于多类图像分类问题中获得高概率预测标签的指标。')
#np.argmax(a, axis = None, out = None)
arr = np.array([[0.12, 0.64, 0.19, 0.05]]) 
tt = np.argmax(arr) 
print(tt)

print('argmin将返回数组中min元素的索引。')
#np.argmin(a, axis = None, out = None)
tt = np.argmin(min) 
print(tt)

print('sort 对数组排序。')
#np.sort(a, axis = -1, kind = None, order = None)
#kind:要使用的排序算法。{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}

arr = np.array([2, 3, 1, 7, 4, 5]) 
tt = np.sort(arr)
print(tt)


print('abs 返回数组中元素的绝对值。当数组中包含负数时，它很有用。')
#TBD
#A = np.array([[1, -3, 4], [-2, -4, 3]])np.abs(A) 
#print(A)

print('round 将浮点值四舍五入到指定数目的小数点。')
#np.round(a, decimals = 0, out = None)
#decimals:要保留的小数点的个数。

tt = np.random.random(size=(3,4)) 
print(tt) 
 
tt = np.round(a,decimals=0) 
print(tt)

tt = np.round(a,decimals=1) 
print(tt)

print('clip 它可以将数组的裁剪值保持在一个范围内。')

arr = np.array([0, 1, -3, -4, 5, 6, 7, 2, 3]) 
tt = arr.clip(0,5) 
print(tt)

tt = arr.clip(0,3) 
print(tt)

tt = arr.clip(3,5) 
print(tt)

print('替换数组中的值 where put copyto')

print('where 返回满足条件的数组元素。')
#np.where(condition, [x, y])
#condition:匹配的条件。如果true则返回x，否则y。

tt = np.arange(12).reshape(4,3) 
print(tt)

tt = np.where(a>5)      ## Get The Index 
print(tt)
 
tt = a[np.where(a>5)]  ## Get Values 
print(tt)

#它还可以用来替换pandas df中的元素。

#tt = np.where(data[feature].isnull(), 1, 0)
#print(tt)

print('put 用给定的值替换数组中指定的元素。')
#np.put(a, ind, v)
#a:数组
#Ind:需要替换的索引。
#V:替换值。

tt = np.array([1, 2, 3, 4, 5, 6]) 
print(tt)
 
tt = np.put(arr, [1, 2], [6, 7]) 
print(tt)

print('copyto 将一个数组的内容复制到另一个数组中。')
#np.copyto(dst, src, casting = 'same_kind', where = True)
#dst：目标
#src：来源

arr1 = np.array([1, 2, 3]) 
arr2 = np.array([4, 5, 6]) 
print("Before arr1", arr1) 
print("Before arr2", arr1)
np.copyto(arr1, arr2) 
print("After arr1", arr1) 
print("After arr2", arr2) 


#集合操作

print('查找公共元素 intersect1d函数以排序的方式返回两个数组中所有唯一的值。')
#np.intersect1d(arg1, arg2, assume_unique = False, return_indices = False)
#Assume_unique:如果为真值，则假设输入数组都是唯一的。
#Return_indices:如果为真，则返回公共元素的索引。

ar1 = np.array([1, 2, 3, 4, 5, 6]) 
ar2 = np.array([3, 4, 5, 8, 9, 1]) 
np.intersect1d(ar1, ar2) 
 
np.intersect1d(ar1, ar2, return_indices = True) 

print('查找不同元素 np.setdiff1d函数返回arr1中在arr2中不存在的所有唯一元素。')

a = np.array([1, 7, 3, 2, 4, 1]) 
b = np.array([9, 2, 5, 6, 7, 8]) 
np.setdiff1d(a, b) 

print('从两个数组中提取唯一元素 Setxor1d 将按顺序返回两个数组中所有唯一的值。')

a = np.array([1, 2, 3, 4, 6]) 
b = np.array([1, 4, 9, 4, 36]) 
np.setxor1d(a,b) 

print('合并 Union1d函数将两个数组合并为一个。')

a = np.array([1, 2, 3, 4, 5]) 
b = np.array([1, 3, 5, 4, 36]) 
np.union1d(a,b) 

#数组分割

print('水平分割 Hsplit函数将数据水平分割为n个相等的部分。')

A = np.array([[3, 4, 5, 2], [6, 7, 2, 6]]) 
np.hsplit(A,2)    ## splits the data into two equal parts 
 
np.hsplit(A,4)    ## splits the data into four equal parts 

print('垂直分割 Vsplit将数据垂直分割为n个相等的部分。')

A = np.array([[3, 4, 5, 2], [6, 7, 2, 6]]) 
np.vsplit(A,2) 

#数组叠加

print('水平叠加 hstack 将在另一个数组的末尾追加一个数组。')

a = np.array([1, 2, 3, 4, 5]) 
b = np.array([1, 4, 9, 16, 25]) 
 
tt = np.hstack((a, b))
print(tt)
      
print('垂直叠加 vstack将一个数组堆叠在另一个数组上。')

tt = np.vstack((a, b))
print(tt)
      
#数组比较

print('allclose 如果两个数组的形状相同，则Allclose函数根据公差值查找两个数组是否相等或近似相等。')

a = np.array([0.25, 0.4, 0.6, 0.32]) 
b = np.array([0.26, 0.3, 0.7, 0.32]) 
 
tolerance = 0.1           ## Total Difference  
np.allclose(a, b, tolerance) 
 
tolerance = 0.5 
np.allclose(a, b, tolerance) 

print('equal 它比较两个数组的每个元素，如果元素匹配就返回True。')

np.equal(arr1, arr2) 

#重复的数组元素

print('repeat 它用于重复数组中的元素n次。')
#np.repeat(a, repeats, axis = None)

#A:重复的元素

#Repeats:重复的次数。

tt = np.repeat('2017', 3)
print(tt)


#让我们来看一个更实际的示例，我们有一个包含按年数量销售的数据集。

fruits = pd.DataFrame([ 
    ['Mango',40], 
    ['Apple',90], 
    ['Banana',130] 
],columns=['Product','ContainerSales']) 
print(fruits)

#在数据集中，缺少年份列。我们尝试使用numpy添加它。

fruits['year'] = np.repeat(2020,fruits.shape[0]) 
print(fruits)

print('tile 通过重复A，rep次来构造一个数组。')
#np.tile(A, reps)

tt = np.tile("Ram",5)
print(tt)
 
tt = np.tile(3,(2,3)) 
print(tt)

#爱因斯坦求和

print('einsum 此函数用于计算数组上的多维和线性代数运算。')

a = np.arange(1,10).reshape(3,3) 
b = np.arange(21,30).reshape(3,3) 
 
tt = np.einsum('ii->i',a) 
print(tt)

tt = np.einsum('ji',a) 
print(tt)

tt = np.einsum('ij,jk',a,b) 
print(tt)

tt = np.einsum('ii',a) 
print(tt)

#统计分析

print('直方图 这是Numpy的重要统计分析函数，可计算一组数据的直方图值。')

A = np.array([[3, 4, 5, 2], 
              [6, 7, 2, 6]]) 
tt = np.histogram(A) 
print(tt)

print('百分位数 沿指定轴计算数据的Q-T-T百分位数。')

#a:输入。
#q:要计算的百分位。
#overwrite_input:如果为true，则允许输入数组修改中间计算以节省内存。
a = np.array([[2, 4, 6], [4, 8, 12]]) 
tt = np.percentile(a, 50) 
print(tt)
tt = np.percentile(a, 10) 
print(tt) 
arr = np.array([2,3,4,1,6,7]) 
tt = np.percentile(a,5) 
print(tt)

print('标准偏差和方差 std和var是NumPy的两个函数，用于计算沿轴的标准偏差和方差。')

a = np.array([[2, 4, 6], [4, 8, 12]]) 
 
tt = np.std(a,axis = 1) 
print(tt) 
tt = np.std(a,axis = 0)    ## Column Wise 
print(tt)
tt = np.var(a,axis = 1) 
print(tt) 
tt = np.var(a,axis = 0) 
print(tt)

#数组打印

print('显示带有两个十进制值的浮点数')

np.set_printoptions(precision = 2)
 
tt = np.array([12.23456, 32.34535]) 
print(tt) 

print('设置打印数组最大值')

tt = np.set_printoptions(threshold = np.inf)
print(tt)

print('增加一行中元素的数量')

tt = np.set_printoptions(linewidth = 100) ## 默认是 75
print(tt)

#保存和加载数据

print('保存')

#savetxt用于在文本文件中保存数组的内容。

arr = np.linspace(10, 100, 500).reshape(25, 20)
np.savetxt('array.txt', arr)

print('加载')

#用于从文本文件加载数组，它以文件名作为参数。

np.loadtxt('array.txt') 

print('------------------------------------------------------------')	#60個


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


print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import math

print('------------------------------------------------------------')	#60個

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

a = np.array([2, 1, 1, 1, 0, 0, 0, 0])
b = np.array([1, 1, 0, 0, 1, 1, 1, 0])
c = np.array([1, 1, 0, 0, 1, 1, 0, 1])
print('a 和 b 相似度 = {0:5.3f}'.format(cosine_similarity(a, b)))
print('a 和 c 相似度 = {0:5.3f}'.format(cosine_similarity(a, c)))
print('b 和 c 相似度 = {0:5.3f}'.format(cosine_similarity(b, c)))

print('------------------------------------------------------------')	#60個

x = np.array([8, 9, 10, 7, 8, 9, 5, 7, 9, 8])
y = np.array([12, 15, 16, 18, 6, 11, 3, 12, 11, 16])             
x_mean = np.mean(x)
y_mean = np.mean(y)

xi_x = [v - x_mean  for v in x]
yi_y = [v - y_mean  for v in y]

data1 = [0]*10
data2 = [0]*10
data3 = [0]*10
for i in range(len(x)):
    data1[i] = xi_x[i] * yi_y[i]
    data2[i] = xi_x[i]**2
    data3[i] = yi_y[i]**2

v1 = np.sum(data1)
v2 = np.sum(data2)
v3 = np.sum(data3)
r = v1 / ((v2**0.5)*(v3**0.5))
print('coefficient = {}'.format(r))

print('------------------------------------------------------------')	#60個

x = np.array([8, 9, 10, 7, 8, 9, 5, 7, 9, 8])
y = np.array([12, 15, 16, 18, 6, 11, 3, 12, 11, 16])             
x_mean = np.mean(x)
y_mean = np.mean(y)
xpt1 = np.linspace(0, 12, 12)      
ypt1 = [y_mean for xp in xpt1]          # 平均購買次數
ypt2 = np.linspace(0, 20, 20)
xpt2 = [x_mean for yp in ypt2]          # 平均滿意度

plt.scatter(x, y)                       # 滿意度 vs 購買次數
plt.plot(xpt1, ypt1, 'g')               # 平均購買次數
plt.plot(xpt2, ypt2, 'g')               # 平均滿意度
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個

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

a = np.array([4, 2])
b = np.array([1, 3])

ab_cross = np.cross(a, b)               # 計算向量外積
area = np.linalg.norm(ab_cross) / 2     # 向量長度除以2
                    
print('area = {0:5.2f}'.format(area))

print('------------------------------------------------------------')	#60個

x1 = np.linspace(0, 10, num=11)     # 使用linspace()產生陣列
print(type(x1), x1)
x2 = np.arange(0,11,1)              # 使用arange()產生陣列
print(type(x2), x2)
x3 = np.arange(11)                  # 簡化語法產生陣列
print(type(x3), x3)

print('------------------------------------------------------------')	#60個

x = np.array([1, 2, 3])         # 1 x 3 陣列 x
y = np.array([2, 3, 4])         # 1 x 3 陣列 y
print(f'x = {x}')
print(f'y = {y}')

print()

y = y.reshape(-1,1)             # y 改為 3 x 1 陣列 
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
np.savetxt('output_data1.csv', arr, delimiter=',')
np.savetxt('output_data2.csv', arr, delimiter=',', fmt='%d')
np.savetxt('output_data3.csv', arr, delimiter=',', fmt='%.2f')


print('------------------------------------------------------------')	#60個



