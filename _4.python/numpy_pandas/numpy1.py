'''
numpy的使用

'''
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
print(a**2)

print('------------------------------------------------------------')	#60個

print('全域方法')
x = np.linspace(-np.pi, np.pi, 11) 
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.sinc(x)
print('x', x)
print('sin(x) = ', y1)
print('cos(x) = ', y2)
print('tan(x) = ', y3)
print('sinc(x) = ' , y4)

print('------------------------------------------------------------')	#60個

print('亂數')
r = np.random.rand(3, 3)      # 建立一個 3x3 隨機矩陣
print(r)

print('亂數')
r = np.random.rand(10)
print(r)

print('最大值 : ', np.max(r))
print('最小值 : ', np.min(r))
print('平均值 : ', np.mean(r))
print('中間值 : ', np.median(r))

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

np1 = np.array([1,2,3,4])	#使用list
np2 = np.array((5,6,7,8))	#使用tuple
print(np1)
print(np2)
print(type(np1), type(np2))

na = np.array([1,2,3,4], dtype=int)
print(na)
na = np.array([1,2,3,4], dtype=float)
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

listdata = [[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15]]
na = np.array(listdata)
print(na)
print('維度', na.ndim)
print('形狀', na.shape)
print('數量', na.size)

adata = np.arange(1,17)
print(adata)
bdata = adata.reshape(4,4)
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

a = np.arange(1,10).reshape(3,3)
b = np.arange(10,19).reshape(3,3)
print('a 陣列內容：\n', a)
print('b 陣列內容：\n', b)
print('a 陣列元素都加值：\n', a + 1)
print('a 陣列元素都平方：\n', a ** 2)
print('a 陣列元素加判斷：\n', a < 5)
print('a 陣列取出第一個row都加1：\n', a[0,:] + 1)
print('a 陣列取出第一個col都加1：\n', a[:,0] + 1)
print('a b 陣列對應元素相加：\n', a + b)
print('a b 陣列對應元素相乘：\n', a * b)
print('a b 陣列點積計算：\n', np.dot(a,b))

a = np.arange(1,10).reshape(3,3)
print('陣列的內容：\n', a)
print('1.最小值與最大值：\n', np.min(a), np.max(a))
print('2.每一直行最小值與最大值：\n', np.min(a, axis=0), np.max(a, axis=0))
print('3.每一橫列最小值與最大值：\n', np.min(a, axis=1), np.max(a, axis=1))
print('4.加總、乘積及平均值：\n', np.sum(a), np.prod(a), np.mean(a))
print('5.每一直行加總、乘積與平均值：\n', np.sum(a, axis=0), np.prod(a, axis=0), np.mean(a, axis=0))
print('6.每一橫列加總、乘積與平均值：\n', np.sum(a, axis=1), np.prod(a, axis=1), np.mean(a, axis=1))

a = np.random.randint(100,size=50)
print('陣列的內容：', a)
print('1.標準差：', np.std(a))
print('2.變異數：', np.var(a))
print('3.中位數：', np.median(a))
print('4.百分比值：', np.percentile(a, 80))
print('5.最大最小差值：', np.ptp(a))

a = np.random.choice(50, size=10, replace=False)
print('排序前的陣列：', a)
print('排序後的陣列：', np.sort(a))
print('排序後的索引：', np.argsort(a))
#用索引到陣列取值
for i in np.argsort(a):
    print(a[i], end=',')

a = np.random.randint(0,10,(3,5))
print('原陣列內容：')
print(a)
print('將每一直行進行排序：')
print(np.sort(a, axis=0))
print('將每一橫列進行排序：')
print(np.sort(a, axis=1))

print('------------------------------------------------------------')	#60個
#mat == matrix

#基本操作
print('創建矩陣')
m = np.mat([1,2,3])
print(m)
#matrix([[1, 2, 3]])

print(m[0])                #取一行
#matrix([[1, 2, 3]])
print(m[0,1])              #第一行，第2个数据

#将Python的列表转换成NumPy的矩阵
list=[1,2,3]
print(np.mat(list))
#matrix([[1, 2, 3]])

#Numpy dnarray转换成Numpy矩阵
n = np.array([1,2,3])
print(n)
#array([1, 2, 3])

print(np.mat(n))
#matrix([[1, 2, 3]])

print('排序')
m=np.mat([[2,5,1],[4,6,2]])    #创建2行3列矩阵
print(m)
'''
matrix([[2, 5, 1],
        [4, 6, 2]])

'''

m.sort()                    #对每一行进行排序
print(m)
'''
matrix([[1, 2, 5],
        [2, 4, 6]])
'''

print(m.shape)                     #获得矩阵的行列数
#(2, 3)
print(m.shape[0])                  #获得矩阵的行数
#2
print(m.shape[1])                  #获得矩阵的列数
#3

print('索引取值')
print(m[1,:])                      #取得第一行的所有元素
#matrix([[2, 4, 6]])

print(m[1,0:1])                    #第一行第0个元素，注意左闭右开
#matrix([[2]])

print(m[1,0:3])
#matrix([[2, 4, 6]])

print(m[1,0:2])
#matrix([[2, 4]])

print('矩陣乘法')

a = np.mat([[1,2,3], [2,3,4]])
b = np.mat([[1,2], [3,4], [5,6]])
print(a)
print(b)
'''
matrix([[1, 2, 3],
        [2, 3, 4]])
matrix([[1, 2],
        [3, 4],
        [5, 6]])
'''
c = a * b         #方法一
print(c)

c2 = np.matmul(a, b)   #方法二
print(c2)

c3 = np.dot(a, b)     #方法三
print(c3)

'''
matrix([[22, 28],
        [31, 40]])
matrix([[22, 28],
        [31, 40]])
matrix([[22, 28],
        [31, 40]])
'''

print('矩陣點乘')
#点乘，只剩下multiply方法了。

a = np.mat([[1,2], [3,4]])
b = np.mat([[2,2], [3,3]])
c = np.multiply(a, b)
print(c)
'''
matrix([[ 2,  4],
        [ 9, 12]])
'''

print('矩陣轉置')
 
#转置有两种方法：

print(a)
'''
matrix([[1, 2],
        [3, 4]])
'''
print(a.T)           #方法一，ndarray也行
'''
matrix([[1, 3],
        [2, 4]])
'''
print(np.transpose(a))   #方法二
'''
matrix([[1, 3],
        [2, 4]])
'''
#值得一提的是，matrix中求逆还有一种简便方法（ndarray中不行）：

print(a)
'''
matrix([[1, 2],
        [3, 4]])
'''
print(a.I)
'''
matrix([[-2. ,  1. ],
        [ 1.5, -0.5]])
'''
 
print('------------------------------------------------------------')	#60個

x = np.linspace(0, 5, 6)
print(x)
X = np.mat(x).T #array轉矩陣再轉置
print(X)

print('------------------------------------------------------------')	#60個


