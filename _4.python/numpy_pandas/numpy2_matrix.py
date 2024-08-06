"""
numpy的使用 矩陣運算

#mat == matrix

"""

import sys

import numpy as np

print("------------------------------------------------------------")  # 60個

# 基本操作
print("創建 1行3列(1X3) 矩陣")
m = np.mat([1, 2, 3])

print("矩陣")
print(type(m))
print(m)

print("矩陣 第0行")
print(m[0])  # 取一行

print("矩陣 [0, 1]")
print(m[0, 1])  # 第一行，第2个数据

print("串列轉矩陣")
list = [1, 2, 3]
print("矩陣")
m = np.mat(list)
print(type(m))
print(m)

print("ndarray轉矩陣")
n = np.array([1, 2, 3])
print(type(n))
print(n)

print("矩陣")
m = np.mat(n)
print(type(m))
print(m)

print("------------------------------------------------------------")  # 60個

print("排序")

print("創建 2行3列(2X3) 矩陣")
m = np.mat([[2, 5, 1], [4, 6, 2]])
print("矩陣")
print(m)

print("对每一行进行排序")
m.sort()
print("矩陣")
print(m)

print("获得矩阵的行列数")  # 2X3
print(m.shape)

print("获得矩阵的行数")  # 2
print(m.shape[0])

print("获得矩阵的列数")  # 3
print(m.shape[1])

print("索引取值")
print(m[1, :])  # 取得第一行的所有元素
# matrix([[2, 4, 6]])

print(m[1, 0:1])  # 第一行第0个元素，注意左闭右开
# matrix([[2]])

print(m[1, 0:3])
# matrix([[2, 4, 6]])

print(m[1, 0:2])
# matrix([[2, 4]])

print("------------------------------------------------------------")  # 60個

print("矩陣乘法")

a = np.mat([[1, 2, 3], [2, 3, 4]])  # 2X3
b = np.mat([[1, 2], [3, 4], [5, 6]])  # 3X2
print(a)
print(b)

"""
matrix([[1, 2, 3],
        [2, 3, 4]])
matrix([[1, 2],
        [3, 4],
        [5, 6]])
"""

print("方法一, a * b")
c = a * b  # 方法一
print(c)

print("方法二, matmul")
c2 = np.matmul(a, b)  # 方法二
print(c2)

print("方法三, dot")
c3 = np.dot(a, b)  # 方法三
print(c3)

print("------------------------------------------------------------")  # 60個

print("矩陣點乘, 要同大小矩陣, 相同位置的數值相乘")
# 点乘，只剩下multiply方法了。

a = np.mat([[1, 2], [3, 4]])
b = np.mat([[2, 2], [3, 3]])
c = np.multiply(a, b)
print(c)

print("矩陣轉置")

# 转置有两种方法：

print(a)
"""
matrix([[1, 2],
        [3, 4]])
"""
print("矩陣轉置, 方法一")
print(a.T)  # 方法一，ndarray也行
"""
matrix([[1, 3],
        [2, 4]])
"""

print("矩陣轉置, 方法二")
print(np.transpose(a))  # 方法二
"""
matrix([[1, 3],
        [2, 4]])
"""
# 值得一提的是，matrix中求逆还有一种简便方法（ndarray中不行）：

print(a)
"""
matrix([[1, 2],
        [3, 4]])
"""

print("反矩陣")
print(a.I)
"""
matrix([[-2.0,  1.0],
        [ 1.5, -0.5]])
"""

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 5, 6)
print(type(x))
print(x)

print("轉置矩陣")
X = np.mat(x).T  # array轉矩陣再轉置
print(X)

print("------------------------------------------------------------")  # 60個

A = np.mat(np.random.rand(3, 3))
print(type(A))
print(A)

print("反矩陣")
B = A.I

print(B * A)
print(A * B)
print(B)

print("------------------------------------------------------------")  # 60個

import numpy as np

print("建立 4 X 4 的 陣列")
A = np.random.rand(4, 4)

print("建立 4 X 4 的 矩陣 (陣列轉矩陣)")
B = np.mat(np.random.rand(4, 4))

print("建立 3 X 3 的 矩陣")
B = np.mat("1 2 3; 4 5 6; 7 8 9")

print("矩陣 與 轉置矩陣 與 反矩陣")
# A = np.mat('1 2 3; 4 5 6; 7 8 9')  #不可求反矩陣
A = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])

print("矩陣A")
print(A)

print("轉置矩陣 A.T")
print(A.T)

print("反矩陣")
print(A.I)

print("A * A.I")
print(A * A.I)

print("------------------------------------------------------------")  # 60個

# 矩阵基本运算

A = np.mat("1 2 3; 4 5 6; 7 8 9")
B = np.mat("4 5 6; 7 8 9; 10 11 12")

print("A + B")
print(A + B)
print("A * B")
print(A * B)
print("B * A")
print(B * A)
print("A * 10")
print(A * 10)

print("------------------------------------------------------------")  # 60個

c = np.mat(np.random.rand(4, 4))

print("矩陣")
print(c)
print("反矩陣")
print(c.I)

print("反矩陣")
d = c.I

c * d

d * c

np.linalg.matrix_rank(A)

np.linalg.det(A)

print(A)
print("反矩陣")
# print(A.I)
# A.I
print("反矩陣")
# d = A.I
# A*d

# d * A

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

A = np.matrix([[1, 2, 3], [4, 5, 6]])
B = np.matrix([[4, 5, 6], [7, 8, 9]])

print("A + B = {}".format(A + B))
print("A - B = {}".format(A - B))

print("------------------------------------------------------------")  # 60個

A = np.matrix([[1, 2, 3], [4, 5, 6]])

print("2 * A   = {}".format(2 * A))
print("0.5 * A = {}".format(0.5 * A))

print("------------------------------------------------------------")  # 60個

A = np.matrix([[1, 2], [3, 4]])
B = np.matrix([[5, 6], [7, 8]])
print("A * B = {}".format(A * B))

C = np.matrix([[1, 0, 2], [-1, 3, 1]])
D = np.matrix([[3, 1], [2, 1], [1, 0]])
print("C @ D = {}".format(C @ D))

print("------------------------------------------------------------")  # 60個

A = np.matrix([[2, 3, 1], [3, 2, 5]])
B = np.matrix([[30, 50], [60, 80], [50, 60]])
print("A * B = {}".format(A * B))

print("------------------------------------------------------------")  # 60個

A = np.matrix([[1, 2, 1], [2, 1, 2]])
B = np.matrix([[30], [50], [20]])
print("A * B = {}".format(A * B))

print("------------------------------------------------------------")  # 60個

A = np.matrix([[1, 2], [3, 4]])
B = np.matrix([[5, 6], [7, 8]])
print("A * B = {}".format(A * B))
print("B * A = {}".format(B * A))

print("------------------------------------------------------------")  # 60個

A = np.matrix([[1, 2], [3, 4]])
B = np.matrix([[1, 0], [0, 1]])
print("A * B = {}".format(A * B))
print("B * A = {}".format(B * A))

print("------------------------------------------------------------")  # 60個

print("反矩陣")

A = np.matrix([[2, 3], [5, 7]])
B = np.linalg.inv(A)
print("A_inv = {}".format(B))
print("E     = {}".format((A * B).astype(np.int64)))

print("------------------------------------------------------------")  # 60個

A = np.matrix([[3, 2], [1, 2]])
A_inv = np.linalg.inv(A)
B = np.matrix([[5], [-1]])
print("{}".format(A_inv * B))

print("------------------------------------------------------------")  # 60個

A = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

print("{}".format(A))
print("shape = {}".format(np.shape(A)))  # 取得矩陣的行列數
print(np.shape(A))

print("------------------------------------------------------------")  # 60個

A = np.array([[0, 2, 4, 6], [1, 3, 5, 7]])

print("轉置矩陣")
B = A.T
print("{}".format(B))
C = np.transpose(A)
print("{}".format(C))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


mat1 = [1, 1, 0, 1, 0, 1, 0, 0, 1]
mat2 = [0, 1, 1, 0, 0, 0, 1, 1, 1]
mat3 = [1, 1, 0, 1, 0, 1, 0, 0, 1]  # the same as mat1
mat4 = [0, 0, 1, 0, 1, 0, 1, 1, 0]  # invert of mat1

matV = np.mat([mat1, mat4])
print(type(matV))
print(matV)


print("------------------------------------------------------------")  # 60個


trainingData = np.matrix(
    [[501, 10], [255, 10], [501, 255], [10, 501]], dtype=np.float32
)

print(type(trainingData))
print(trainingData)

print("------------------------------------------------------------")  # 60個

# 矩阵和线性代数

import numpy as np
import numpy.linalg  # linear algebra


def matrix_linear():
    m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
    print(m)

    # Create a vector and multiply
    v = np.matrix([[2], [3], [4]])
    print(v)
    print(m * v)

    # Determinant 行列式
    print(numpy.linalg.det(m))

    # Eigenvalues 特征值
    print(numpy.linalg.eigvals(m))

    # Solve for x in m*x = v
    x = numpy.linalg.solve(m, v)
    print(x)
    print(m * x)
    print(v)


matrix_linear()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
