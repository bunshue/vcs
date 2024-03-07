"""
numpy pandas 新進

"""

import sys
import numpy as np
import pandas as pd

print('------------------------------------------------------------')	#60個

print("------------------------------------------------------------")  # 60個
print("numpy")
print("------------------------------------------------------------")  # 60個

a = np.array([2,3,4,5,6])
print(f'a = {a}')
b = np.ma.masked_where(a > 3, a)
print(f'b = {b}')

print('------------------------------------------------------------')	#60個


print(np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])])
print(np.c_[np.array([[1, 2, 3]]), 0, 0, np.array([[4, 5, 6]])])

"""
array([[1, 4],
       [2, 5],
       [3, 6]])
"""

#array([[1, 2, 3, ..., 4, 5, 6]])

print('------------------------------------------------------------')	#60個

#numpy.c_() and numpy.r_()的用法


#####np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等，类似于pandas中的merge()。
#####np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等，类似于pandas中的concat()。

#np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等。
#np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等。


#1.numpy.c_:

x = np.arange(12).reshape(3,4)
print('x:',x, x.shape)

y = np.arange(10,22).reshape(3,4)
print('y:',y, y.shape)

z = np.c_[x,y]
print('z:',z, z.shape)

#2.numpy.r_用法:

x = np.arange(12).reshape(3,4)
print('x:',x, x.shape)

y = np.arange(10,22).reshape(3,4)
print('y:',y, y.shape)

z = np.r_[x,y]
print('z:',z, z.shape)

print("------------------------------------------------------------")  # 60個

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(x))

print("------------------------------------------------------------")  # 60個

print("二維陣列 6 X 4")
a = np.array(
    [[0, 0, 0, 1], [1, 1, 1, 2], [2, 2, 2, 3], [3, 3, 3, 4], [4, 4, 4, 5], [5, 5, 5, 6]]
)
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.nbytes)

print("第3列 之 第1~4項(不含尾)")
print(a[3, 1:4])

print("前2列 之 第2欄之後")
print(a[:2, 2:])

print("第2列 之 全部")
print(a[2, :])

print("全部列 之 第3欄, 轉成row")
print(a[:, 3])

print("全部列 之 偶數欄")
print(a[:, ::2])

print("偶數列 之 036欄")
print(a[::2, ::3])

# axis = 0 : 第0維 直行
# axis = 1 : 第1維 橫列
print("全部和:", a.sum())
print("直行加:", a.sum(axis=0))
print("橫列加:", a.sum(axis=1))

# np.argmin()求最小值對應的索引
# np.argmax()求最大值對應的索引

print("每個直行的最小值:", a.min(axis=0))
print("每個直行的最小值對應的索引:", a.argmin(axis=0))
print("每個直行的標準差:", a.std(axis=0))

print("全部平均:", a.mean())
print("直行平均:", a.mean(axis=0))
print("橫列平均:", a.mean(axis=1))

print("------------------------------------------------------------")  # 60個

print("一維陣列 10個元素")
a = np.arange(10)
print(a)

print("前4項")
print(a[:4])

print("第3項 至 第7項(不含尾)")
print(a[3:7])

print("第5項 至 最後")
print(a[5:])

print("第3至第9項 跳一個")
print(a[3:9:2])

print("第2項開始至最後, 跳一個")
print(a[2::2])

print("從頭至最後, 跳二個")
print(a[::3])

print("------------------------------------------------------------")  # 60個

print("使用 numpy函數 對 list做處理")

x = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0]

print(np.max(x))
print(np.mean(x))
print(np.min(x))

print("------------------------------------------------------------")  # 60個

print("用numpy建立資料")
a = np.arange(5)
print(a)
a = np.arange(2,5,1)
print(a)
a = np.linspace(2,5,4)
print(a)
a = np.logspace(0,2,5)
print(a)

a = np.empty(5) # 生成5個元素，值爲隨機數的數組（速度快）
print(a)
a = np.zeros(5) # 生成5個值全爲0的數組
print(a)
a = np.ones(5) # 生成5個值全爲1的數組
print(a)
a = np.full(5, 6) # 生成5個值全爲6的數組
print(a)

print("------------------------------------------------------------")  # 60個

a = np.array([1,2,3,4,5,6], dtype=np.int64)
print(a.dtype) 
a = a.astype(np.float32)
print(a.dtype) 
print(a.dtype.type)

print("------------------------------------------------------------")  # 60個

print("分段函數")

x=np.arange(10)
print(x)

print(np.where(x<5, x, 9-x))


a=np.arange(10)
print(np.select([x<3,x>6], [-1,1], 0))


a=np.arange(10)
print(np.piecewise(x, [x<3,x>6], [lambda x: x * 2, lambda x: x * 3]))

print("------------------------------------------------------------")  # 60個

print("矩陣與二維數組")
a = np.mat(np.mat([[1,2,3],[4,5,6]]))
print(type(a))

print(np.eye(2))
print(np.diag([2,3]))

a = np.mat([[1.,2.],[3.,4.]])
print(np.dot(a,a))    # 矩陣乘積
print(np.multiply(a,a))    # 矩陣點乘
print(a.T)   # 矩陣轉置
print(a.I)   # 矩陣求逆
print(np.trace(a))    # 求矩陣的跡
print(np.linalg.eig(a))   # 特徵分解

a = np.mat(np.mat([[1,2,3],[4,5,6]]))
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

filename = "data/python_ReadWrite_CSV6_score.csv"

dat = pd.read_csv(filename, encoding="UTF-8")

print(dat.head())

print("數學平均", np.mean(dat["數學"]))
print("數學中位數", np.median(dat["數學"]))

print("------------------------------------------------------------")  # 60­э



print("------------------------------------------------------------")  # 60­э

import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<type 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"
b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

print('------------------------------------------------------------')	#60個

a = np.zeros((2,2))
print(a) # Prints "[[ 0. 0.]
# [0. 0.]]"

b = np.ones((1,2)) # Create an array of all ones
print(b) # Prints "[[ 1. 1.]]"

c = np.full((2,2), 7) # Create a constant array
print(c)

d = np.eye(3)
print(d)

print('------------------------------------------------------------')	#60個

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b= a[0:2,1:3]         # 定義b為a 的部分資料
#b= a[0:2,1:3].copy() # 複製b為a 的部分資料
print(b)              #輸出[[2 3], [6 7]]
b[0, 0] = 99          # 修改b的局部資料
print(b)              #輸出[[99  3], [ 6  7]]
print(a)              # 輸出[[ 1 99  3  4],[ 5  6  7  8],[ 9 10 11 12]]

print('------------------------------------------------------------')	#60個

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row_r1 = a[1, :]
row_r2 = a[1:2, :]
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)

print('------------------------------------------------------------')	#60個

a = np.array([[1,2], [3, 4], [5, 6]])
print(a[0, 0])
print(a[1, 1])
b=[a[0, 0], a[1, 1]];
print(b)
b=a[[0, 0], [1, 1]];
print(b)
print(b[1])
print(a[[0,1,2], [0,1,0]])

print('------------------------------------------------------------')	#60個

x = np.array([1, 2])  #numpy自動設定
print(x.dtype)         # 輸出 "int64"
x = np.array([1.0, 2.0])  #numpy自動設定
print(x.dtype)             # 輸出 "float64"
x = np.array([1, 2], dtype=np.int64)  #設定為int64
print(x.dtype)                         # 輸出 "int64"

print('------------------------------------------------------------')	#60個

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
v = np.array([9, 10], dtype=np.float64)

# 加法
print(x + y)        # 輸出 [[ 6.0  8.0] [10.0 12.0]]
print(np.add(x, y)) # 輸出 [[ 6.0  8.0] [10.0 12.0]]
print(x + 10)       # 輸出 [[11. 12.] [13. 14.]]
# 減法
print(x - y)        # 輸出 [[-4.0 -4.0] [-4.0 -4.0]]
print(np.subtract(x, y)) # 輸出 [[-4.0 -4.0] [-4.0 -4.0]]
print(x -[1,2])     # 輸出 [[0. 0.]  [2. 2.]]
# 乘法
print(x * y)
print(np.multiply(x, y)) # 輸出  [[ 5.0 12.0][21.0 32.0]]
# 除法
print(x / y)
print(np.divide(x, y))# 輸出 [[ 0.2  0.33333333] [ 0.42857143  0.5]]
# 平方
print(x **2)
print(np.sqrt(x))# 輸出[[ 1. 1.41421356] [ 1.73205081  2.]]

#矩陣乘法，兩個數組的點積 Dot product
print(x.dot(y))# 輸出         [[19. 22.] [43. 50.]]
print(np.dot(x, y))   # [[5+14 , 6+16] []]

print('------------------------------------------------------------')	#60個

x = np.array([[-1,2,3],[13,14,15]])
print(x)
print(np.sum(x))       # 輸出46   全部累加
print(np.sum(x, axis=0))  # 輸出"[12 16 18]" =(-1+13),(2+14),(3+15)
print(np.sum(x, axis=1))  # 輸出"[ 4 42]" =(-1+2+3),(13+14+15)
print(np.max(x))       #最大值 輸出15
print(np.min(x))       #最小值 輸出-1
print(np.cumsum(x))    # 累加[-1  1  4 17 31 46]
# 加權平均值
print(np.average(x))   # 輸出7.666
# 平均 mean=sum(x)/len(x)
print(np.mean(x))      # 輸出7.666
# 中間值
print(np.median(x))   # 輸出8.0
# 標準偏差 std = sqrt(mean(abs(x - x.mean())**2))
print(np.std(x))       # 輸出 6.472
# 方差 var = mean(abs(x - x.mean())**2)
print(np.var(x))       # 輸出 41.888
print(x.T)       # 輸出 [[-1 13] [ 2 14] [ 3 15]]

print('------------------------------------------------------------')	#60個

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
bool_idx =  ((a % 2)==0)
print(bool_idx)
print(a[bool_idx])
print(a[a > 10])
print(a[a%2==1]*10)

print('------------------------------------------------------------')	#60個

#方法1
x = np.array([[1,2,3], [4,5,6]])
v = np.array([1, 0, 1])
y = np.empty_like(x)
for i in range(2):
    y[i, :] = x[i, :] + v
print(y)    #輸出[[2 2 4][5 5 7]]

#方法2
v2 = np.tile(v, (2, 1))
print(v2)   #輸出[[1 0 1][1 0 1]]
print(x+v2) #輸出[[2 2 4] [5 5 7]]

#方法3
print(x+v)  #輸出[[2 2 4] [5 5 7]]

print('------------------------------------------------------------')	#60個


import numpy as np

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

# 一維
a = np.array([1, 2, 3])
print(a)

# 二維
b = np.array([[1, 2, 3], [5, 6, 7]])
print(b)

# 二維，使用 dtype 定義數據類型
bb = np.array([[1, 2, 3], [5, 6, 7]], dtype=float)
print(bb)

# 最小維度
c = np.array([1, 2, 3], ndmin=3)
print(c)


print("------------------------------------------------------------")  # 60個

a = np.array([[[1, 2, 3], [5, 6, 7]]])

# 取得陣列維度的深度
print(np.ndim(a))

# 依序取得每個維度的數量
print(np.shape(a))

# 修改維度 1,2,3 -> 1,3,2
a.shape = (1, 3, 2)
print(a)

# 也可以使用 reshape，不過不知道為什麼用了之後執行沒問題，但編輯器會報錯
# b = a.reshape(1,2,3)
# print(b)

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

# 產生數據
x = np.arange(5, dtype=float)
print(x)  # [0. 1. 2. 3. 4.]
x2 = np.arange(0, 10, 2)
print(x2)  # [0 2 4 6 8]

# 使用 linspace 產生數據
y = np.linspace(1, 10, 10, dtype=int)
print(y)  # [ 1  2  3  4  5  6  7  8  9 10]
y2 = np.linspace(1, 2, 10)
print(y2)
# [1. 1.11111111 1.22222222 1.33333333 1.44444444 1.55555556 1.66666667 1.77777778 1.88888889 2.]

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個






print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



