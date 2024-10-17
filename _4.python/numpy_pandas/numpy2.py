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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# nparraylist.py
import numpy as np

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
import numpy as np

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
import numpy as np

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
import numpy as np

a = np.random.randint(100, size=50)
print("陣列的內容：", a)
print("1.標準差：", np.std(a))
print("2.變異數：", np.var(a))
print("3.中位數：", np.median(a))
print("4.百分比值：", np.percentile(a, 80))
print("5.最大最小差值：", np.ptp(a))

print("------------------------------------------------------------")  # 60個

# npcreate.py
import numpy as np

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
import numpy as np

listdata = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
na = np.array(listdata)
print(na)
print("維度", na.ndim)
print("形狀", na.shape)
print("數量", na.size)

print("------------------------------------------------------------")  # 60個

# npreshape.py
import numpy as np

adata = np.arange(1, 17)
print(adata)
bdata = adata.reshape(4, 4)
print(bdata)


# nprandom.py
import numpy as np

print("1.產生2x3 0~1之間的隨機浮點數\n", np.random.rand(2, 3))
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


print("------------------------------------------------------------")  # 60個

# npfile.py
import numpy as np

a = np.genfromtxt("_new/scores.csv", delimiter=",", skip_header=1)
print(a.shape)

print("------------------------------------------------------------")  # 60個

# npsort1.py
import numpy as np

a = np.random.choice(50, size=10, replace=False)
print("排序前的陣列：", a)
print("排序後的陣列：", np.sort(a))
print("排序後的索引：", np.argsort(a))
# 用索引到陣列取值
for i in np.argsort(a):
    print(a[i], end=",")

print("------------------------------------------------------------")  # 60個

# npsort2.py
import numpy as np

a = np.random.randint(0, 10, (3, 5))
print("原陣列內容：")
print(a)
print("將每一直行進行排序：")
print(np.sort(a, axis=0))
print("將每一橫列進行排序：")
print(np.sort(a, axis=1))

print("------------------------------------------------------------")  # 60個

# npvalue1.py
import numpy as np

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
import numpy as np

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

a = np.array([1, 2, 3, 4, 5, 6])
print("a=" + str(a))

b = np.reshape(a, (3, 2))
print("b=np.reshape(a,(3,2))->")
print(b)
c = b.T
print("c=b.T->")
print(c)
c = b.transpose()
print("c=b.transpose()->")
print(c)
c = np.transpose(b)
print("c=np.transpose(b)->")
print(c)

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

a = np.array([1, 2, 3])
print("a=" + str(a))

b = a.copy()
print("b=a.copy()->" + str(b))
b.fill(4)
print("b.fill(0)=" + str(b))
c = np.concatenate((a, b))
print("c=np.concatenate((a,b))->" + str(c))

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.concatenate((a, b))
print("c=np.concatenate((a,b))->")
print(c)
c = np.concatenate((a, b), axis=0)
print("c=np.concatenate((a,b), axis=0)->")
print(c)
c = np.concatenate((a, b), axis=1)
print("c=np.concatenate((a,b), axis=1)->")
print(c)

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

v1 = np.random.random()
v2 = np.random.random()
print(v1, v2)
v3 = np.random.randint(5, 10)
v4 = np.random.randint(1, 101)
print(v3, v4)

print("------------------------------------------------------------")  # 60個

a = np.random.rand(5)
print("np.random.rand(5)=")
print(a)
b = np.random.rand(3, 2)
print("np.random.rand(3,2)=")
print(b)
c = np.random.randint(5, 10, size=5)
print("np.random.randint(5,10,size=5)")
print(c)
d = np.random.randint(5, 10, size=(2, 3))
print("np.random.randint(5,10,size=(2,3))")
print(d)

print("------------------------------------------------------------")  # 60個

a = np.array([30, 45, 60])

print(np.sin(a * np.pi / 180))
print(np.cos(a * np.pi / 180))
print(np.tan(a * np.pi / 180))

print("------------------------------------------------------------")  # 60個

a = np.array([1.0, 5.55, 123, 0.567, 25.532])
print("a=" + str(a))

print(np.around(a))
print(np.around(a, decimals=1))
print(np.around(a, decimals=-1))

a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print("a=" + str(a))

b = np.floor(a)
print("floor()=" + str(b))
b = np.ceil(a)
print("ceil()=" + str(b))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
