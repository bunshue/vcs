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

e = np.random.random((2,2)) # Create an array (lled with random values
print(e) # Might print "[[ 0.91940167 0.08143941]
# [ 0.68744134 0.87236687]]"

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

