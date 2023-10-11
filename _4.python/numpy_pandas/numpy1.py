'''
numpy的使用

'''

import sys
import numpy as np

print('------------------------------------------------------------')	#60個

print('建立陣列')
x = np.array([1, 2, 3])
y = np.arange(10)  # 類似 Python 的 range, 但是回傳 array
print(x)
print(y)

print('------------------------------------------------------------')	#60個

print('基本運算')
a = np.array([1, 2, 3, 6])
print(a)

b = np.linspace(0, 2, 4)  # 建立一個array, 在0與2的範圍之間讓4個點等分
print(b)

c = a - b
print(c)
print(a ** 2)

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

na = np.arange(0,6)
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

a = np.arange(16)
print(a)
b = a.reshape((4, 4))
print(b)

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

#arrange?
a = np.arange(11, 36)
a = a.reshape(5, 5)
print(a)

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



print('------------------------------------------------------------')	#60個



