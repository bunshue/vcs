"""
numpy 新進

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


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

np.random.seed(0)

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)

print("dtype:", x3.dtype)

print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")


grid = np.arange(1, 10).reshape((3, 3))
print(grid)

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate([x, y])

z = [99, 99, 99]
print(np.concatenate([x, y, z]))

grid = np.array([[1, 2, 3], [4, 5, 6]])

# concatenate along the first axis
cc = np.concatenate([grid, grid])
print(cc)


# concatenate along the second axis (zero-indexed)
cc = np.concatenate([grid, grid], axis=1)
print(cc)


x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7], [6, 5, 4]])

# vertically stack the arrays
cc = np.vstack([x, grid])
print(cc)

# horizontally stack the arrays
y = np.array([[99], [99]])
cc = np.hstack([grid, y])
print(cc)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Create evenly spaced numbers over the specified interval
x = np.linspace(0, 2, 10)
plt.plot(x, "o-")
plt.show()

# Create sample data, add some noise
x = np.random.uniform(1, 100, 1000)
y = np.log(x) + np.random.normal(0, 0.3, 1000)

plt.scatter(x, y)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# rng = np.random.RandomState(0)
# x = random.randint(10, size=(3, 4))
x = np.random.randint(10, size=(3, 4))  # Two-dimensional array
print(x)

# 邏輯運算
cc = x < 6
print(cc)

# 統計
cc = np.count_nonzero(x < 6)
print(cc)

# sum
cc = np.sum(x < 6)  # False=0, True=1
print(cc)

cc = np.sum(x < 6, axis=0)
print(cc)

cc = np.sum(x < 6, axis=1)
print(cc)

cc = np.any(x > 8)
print(cc)

cc = np.any(x < 0)
print(cc)

cc = np.all(x < 10)
print(cc)

cc = np.all(x == 6)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

rand = np.random.RandomState(42)

mean = [0, 0]
cov = [[1, 2], [2, 5]]
X = rand.multivariate_normal(mean, cov, 100)
print(X.shape)

sns.set()  # for plot styling

plt.scatter(X[:, 0], X[:, 1])
plt.show()

indices = np.random.choice(X.shape[0], 20, replace=False)
print(indices)

selection = X[indices]  # fancy indexing here
print(selection.shape)

# (20, 2)

# Now to see which points were selected, let's over-plot large circles at the locations of the selected points:

plt.scatter(X[:, 0], X[:, 1], alpha=0.3, s=400)
plt.scatter(selection[:, 0], selection[:, 1], facecolor="none", alpha=0.3, s=200)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Modifying Values with Fancy Indexing

x = np.arange(10)
i = np.array([2, 1, 8, 4])
x[i] = 99
print(x)

x[i] -= 10
print(x)

x = np.zeros(10)
x[[0, 0]] = [4, 6]
print(x)

i = [2, 3, 3, 4, 4, 4]
x[i] += 1
print(x)

x = np.zeros(10)
np.add.at(x, i, 1)
print(x)

# Example: Binning Data
x = np.random.randn(100)

# compute a histogram by hand
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)

# find the appropriate bin for each x
i = np.searchsorted(bins, x)

# add 1 to each of these bins
np.add.at(counts, i, 1)

# The counts now reflect the number of points within each bin–in other words, a histogram:

# plot the results
plt.plot(bins, counts, linestyle="dashed")
show()

# Of course, it would be silly to have to do this each time you want to plot a histogram. This is why Matplotlib provides the plt.hist() routine, which does the same in a single line:

plt.hist(x, bins, histtype="step")
show()

print("NumPy routine:")
counts, edges = np.histogram(x, bins)

print("Custom routine:")
np.add.at(counts, np.searchsorted(bins, x), 1)

x = np.random.randn(1000000)
print("NumPy routine:")
counts, edges = np.histogram(x, bins)

print("Custom routine:")
# np.add.at(counts, np.searchsorted(bins, x), 1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Sorting along rows or columns

rand = np.random.RandomState(42)
X = rand.randint(0, 10, (4, 6))
print(X)

# sort each column of X
np.sort(X, axis=0)

# sort each row of X
np.sort(X, axis=1)

# Example: k-Nearest Neighbors

X = rand.rand(10, 2)

sns.set()  # Plot styling
plt.scatter(X[:, 0], X[:, 1], s=100)
show()

dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=-1)

# for each pair of points, compute differences in their coordinates
differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
print(differences.shape)

# (10, 10, 2)

# square the coordinate differences
sq_differences = differences**2
print(sq_differences.shape)

# (10, 10, 2)

# sum the coordinate differences to get the squared distance
dist_sq = sq_differences.sum(-1)
print(dist_sq.shape)

# (10, 10)

print(dist_sq.diagonal())

# array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])

nearest = np.argsort(dist_sq, axis=1)
print(nearest)

K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)

plt.scatter(X[:, 0], X[:, 1], s=100)

# draw lines from each point to its two nearest neighbors
K = 2

for i in range(X.shape[0]):
    for j in nearest_partition[i, : K + 1]:
        # plot a line from X[i] to X[j]
        # use some zip magic to make it happen:
        plt.plot(*zip(X[j], X[i]), color="black")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

name = ["Alice", "Bob", "Cathy", "Doug"]
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

x = np.zeros(4, dtype=int)

# Use a compound data type for structured arrays
data = np.zeros(
    4, dtype={"names": ("name", "age", "weight"), "formats": ("U10", "i4", "f8")}
)
print(data.dtype)

data["name"] = name
data["age"] = age
data["weight"] = weight
print(data)

# Get all names
cc = data["name"]
print(cc)

# Get first row of data
cc = data[0]
print(cc)

# Get the name from the last row
cc = data[-1]["name"]
print(cc)

# Get names where age is under 30
cc = data[data["age"] < 30]["name"]
print(cc)

# Creating Structured Arrays

np.dtype({"names": ("name", "age", "weight"), "formats": ("U10", "i4", "f8")})

np.dtype(
    {"names": ("name", "age", "weight"), "formats": ((np.str_, 10), int, np.float32)}
)

np.dtype([("name", "S10"), ("age", "i4"), ("weight", "f8")])

np.dtype("S10,i4,f8")

# More Advanced Compound Types

tp = np.dtype([("id", "i8"), ("mat", "f8", (3, 3))])
X = np.zeros(1, dtype=tp)
print(X[0])
print(X["mat"][0])

# RecordArrays: Structured Arrays with a Twist

cc = data["age"]
print(cc)

data_rec = data.view(np.recarray)
cc = data_rec.age
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


row1 = [1, 2, 3]
arr1 = np.array(row1, ndmin=2)
print(f"陣列維度 = {arr1.ndim}")
print(f"陣列外型 = {arr1.shape}")
print(f"陣列大小 = {arr1.size}")
print("陣列內容")
print(arr1)

row2 = [4, 5, 6]
arr2 = np.array([row1, row2], ndmin=2)
print(f"陣列維度 = {arr2.ndim}")
print(f"陣列外型 = {arr2.shape}")
print(f"陣列大小 = {arr2.size}")
print("陣列內容")
print(arr2)

print("------------------------------------------------------------")  # 60個

x = np.array([[1, 2, 3], [4, 5, 6]])
print(f"陣列維度 = {x.ndim}")
print(f"陣列外型 = {x.shape}")
print(f"陣列大小 = {x.size}")
print("陣列內容")
print("x :", x)

print("------------------------------------------------------------")  # 60個

x1 = np.ones(3)
print("x1 :", x1)

x2 = np.ones((2, 3), dtype=np.uint8)
print("x2 :", x2)

print("------------------------------------------------------------")  # 60個

x1 = np.empty(3)
print("x1 :", x1)

x2 = np.empty((2, 3), dtype=np.uint8)
print("x2 :", x2)

print("------------------------------------------------------------")  # 60個

x1 = np.random.randint(10, 20)
print("回傳值是10(含)至20(不含)的單一隨機數")
print("x1 :", x1)

print("回傳一維陣列10個元素, 值是1(含)至5(不含)的隨機數")
x2 = np.random.randint(1, 5, 10)
print("x2 :", x2)

print("回傳單3*5陣列, 值是0(含)至10(不含)的隨機數")
x3 = np.random.randint(10, size=(3, 5))
print("x3 :", x3)

print("------------------------------------------------------------")  # 60個

x = np.arange(16)
print("x :", x)
print(np.reshape(x, (4, -1)))

print("------------------------------------------------------------")  # 60個

x = np.arange(16)
print("x :", x)
print(np.reshape(x, (-1, 8)))

print("------------------------------------------------------------")  # 60個

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"陣列元素如下 : {x} ")
print(f"x[2:]       = {x[2:]}")
print(f"x[:2]       = {x[:3]}")
print(f"x[0:3]      = {x[0:3]}")
print(f"x[1:4]      = {x[1:4]}")
print(f"x[0:9:2]    = {x[0:9:2]}")
print(f"x[-1]       = {x[-1]}")
print(f"x[::2]      = {x[::2]}")
print(f"x[2::3]     = {x[2::3]}")
print(f"x[:]        = {x[:]}")
print(f"x[::]       = {x[::]}")
print(f"x[-3:-7:-1] = {x[-3:-7:-1]}")

print("------------------------------------------------------------")  # 60個

print("測試 copy=True/False")

print("測試 copy=True, 完全複製, 不連動")
x1 = np.array([0, 1, 2, 3, 4, 5])
x2 = np.array(x1, copy=True)

print("x1 :", x1)
print("x2 :", x2)
x2[0] = 9
print("x1 :", x1)
print("x2 :", x2)

print("測試 copy=False, 會連動")
x1 = np.array([0, 1, 2, 3, 4, 5])
x2 = np.array(x1, copy=False)

print("x1 :", x1)
print("x2 :", x2)
x2[0] = 9
print("x1 :", x1)
print("x2 :", x2)

print("預設, 無copy=True/False, 就是True, 完全複製, 不連動")
x1 = np.array([0, 1, 2, 3, 4, 5])
x2 = np.array(x1)

print("x1 :", x1)
print("x2 :", x2)
x2[0] = 9
print("x1 :", x1)
print("x2 :", x2)

print("------------------------------------------------------------")  # 60個

x1 = np.array([0, 1, 2, 3, 4, 5])
x2 = x1.copy()

print("x1 :", x1)
print("x2 :", x2)
x2[0] = 9
print("x1 :", x1)
print("x2 :", x2)

print("------------------------------------------------------------")  # 60個

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
print("x4 :", x4)

print("------------------------------------------------------------")  # 60個

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
x5 = np.array([x4, x4])
print("x5 :", x5)

print("------------------------------------------------------------")  # 60個

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
print(f"x4[2][1] = {x4[2][1]}")
print(f"x4[1][3] = {x4[1][3]}")

print("------------------------------------------------------------")  # 60個

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
print(f"x4[2,1] = {x4[2,1]}")
print(f"x4[1,3] = {x4[1,3]}")

print("------------------------------------------------------------")  # 60個

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
x5 = np.array([x4, x4])
print(f"x5[0][2][1] = {x5[0][2][1]}")
print(f"x5[0][1][3] = {x5[0][1][3]}")
print(f"x5[1][0][1] = {x5[1][0][1]}")
print(f"x5[1][1][4] = {x5[1][1][4]}")

print("------------------------------------------------------------")  # 60個

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
x5 = np.array([x4, x4])
print(f"x5[0,2,1] = {x5[0,2,1]}")
print(f"x5[0,1,3] = {x5[0,1,3]}")
print(f"x5[1,0,1] = {x5[1,0,1]}")
print(f"x5[1,1,4] = {x5[1,1,4]}")

print("------------------------------------------------------------")  # 60個

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x = np.array([x1, x2, x3])
print("x[:,:]   = 結果是二維陣列")  # 結果是二維陣列
print(x[:, :])

print("x[2,:4]  = 結果是一維陣列")  # 結果是一維陣列
print(x[2, :4])

print("x[:2,:1] = 結果是二維陣列")  # 結果是二維陣列
print(x[:2, :1])

print("x[:,4:]  =  結果是二維陣列")  # 結果是二維陣列
print(x[:, 4:])

print("x[:,4]   =  結果是一維陣列")  # 結果是一維陣列
print(x[:, 4])

print("------------------------------------------------------------")  # 60個

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x = np.array([x1, x2, x3])
print("x[:2,4]  = 結果是一維陣列")  # 結果是一維陣列
print(x[:2, 4])

print("------------------------------------------------------------")  # 60個

x1 = np.arange(4).reshape(2, 2)
print(f"陣列 1 \n{x1}")
x2 = np.arange(4, 8).reshape(2, 2)
print(f"陣列 2 \n{x2}")
x = np.vstack((x1, x2))
print(f"合併結果 \n{x}")

print("------------------------------------------------------------")  # 60個

x1 = np.arange(4).reshape(2, 2)
print(f"陣列 1 \n{x1}")
x2 = np.arange(4, 8).reshape(2, 2)
print(f"陣列 2 \n{x2}")
x = np.hstack((x1, x2))
print(f"合併結果 \n{x}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

a = np.arange(1, 10).reshape(3, 3)
print("陣列的內容：\n", a)
print("1.最小值與最大值：\n", np.min(a), np.max(a))
print("2.每一直行最小值與最大值：\n", np.min(a, axis=0), np.max(a, axis=0))
print("3.每一橫列最小值與最大值：\n", np.min(a, axis=1), np.max(a, axis=1))
print("4.加總、乘積及平均值：\n", np.sum(a), np.prod(a), np.mean(a))
print("5.每一直行加總、乘積與平均值：\n", np.sum(a, axis=0), np.prod(a, axis=0), np.mean(a, axis=0))
print("6.每一橫列加總、乘積與平均值：\n", np.sum(a, axis=1), np.prod(a, axis=1), np.mean(a, axis=1))

print("------------------------------------------------------------")  # 60個

a = np.random.randint(100, size=50)
print("陣列的內容：", a)
print("1.標準差：", np.std(a))
print("2.變異數：", np.var(a))
print("3.中位數：", np.median(a))
print("4.百分比值：", np.percentile(a, 80))
print("5.最大最小差值：", np.ptp(a))

print("------------------------------------------------------------")  # 60個

a = np.random.choice(50, size=10, replace=False)
print("排序前的陣列：", a)
print("排序後的陣列：", np.sort(a))
print("排序後的索引：", np.argsort(a))
# 用索引到陣列取值
for i in np.argsort(a):
    print(a[i], end=",")

print("------------------------------------------------------------")  # 60個

a = np.random.randint(0, 10, (3, 5))
print("原陣列內容：")
print(a)
print("將每一直行進行排序：")
print(np.sort(a, axis=0))
print("將每一橫列進行排序：")
print(np.sort(a, axis=1))

print("------------------------------------------------------------")  # 60個

listdata = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
na = np.array(listdata)
print(na)
print("維度", na.ndim)
print("形狀", na.shape)
print("數量", na.size)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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
