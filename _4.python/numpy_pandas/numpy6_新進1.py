"""
python_data_science01

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

np.random.seed(0)  # seed for reproducibility

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

np.random.seed(42)
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


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
