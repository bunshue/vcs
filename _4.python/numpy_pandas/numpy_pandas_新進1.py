"""
numpy的使用
pandas的使用


numpy: 數值計算的標準套件

1. 基本建立 np.array
   1.1 自填陣列, 串列轉np陣列
   1.2 自動產生陣列

arr1 = np.array([1, 2, 3, 4, 5])

"""
print("------------------------------")  # 30個

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    # pass
    plt.tight_layout()  # 緊密排列，並填滿原圖大小
    plt.show()


print("------------------------------------------------------------")  # 60個

import os.path

salary = pd.read_csv("data/salary_table.csv")
print(salary.head())

xls_filename = "tmp_salary_table.xlsx"
salary.to_excel(xls_filename, sheet_name="users", index=False)

# 讀取
df = pd.read_excel(xls_filename, sheet_name="users")  # 讀取頁面 users
print(df)

# Multiple sheets
with pd.ExcelWriter(xls_filename) as writer:
    salary.to_excel(writer, sheet_name="users", index=False)  # 寫入頁面 users
    salary.to_excel(writer, sheet_name="salary", index=False)  # 寫入頁面 salary

df1 = pd.read_excel(xls_filename, sheet_name="users")  # 讀取頁面 users
print(df1)

df2 = pd.read_excel(xls_filename, sheet_name="salary")  # 讀取頁面 salary
print(df2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SQL (SQLite)

import sqlite3

db_filename = "tmp_salary_table.db"

conn = sqlite3.connect(db_filename)

##############################################################################
salary = pd.read_csv("data/salary_table.csv")
print(salary.head())

salary.to_sql("salary", conn, if_exists="replace")

##############################################################################
# Push modifications

cur = conn.cursor()
values = (100, 14000, 5, "Bachelor", "N")
cur.execute("insert into salary values (?, ?, ?, ?, ?)", values)
conn.commit()

##############################################################################
# Reading results into a pandas DataFrame

salary_sql = pd.read_sql_query("select * from salary;", conn)
print(salary_sql.head())

pd.read_sql_query("select * from salary;", conn).tail()
pd.read_sql_query("select * from salary where salary>25000;", conn)
pd.read_sql_query("select * from salary where experience=16;", conn)
pd.read_sql_query('select * from salary where education="Master";', conn)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

##############################################################################
# Exercises
# ---------
# Data Frame
# ~~~~~~~~~~
# 1. Read the iris dataset at "https://github.com/neurospin/pystatsml/tree/master/datasets/iris.csv"
# 2. Print column names
# 3. Get numerical columns
# 4. For each species compute the mean of numerical columns and store it in  a ``stats`` table like:
#           species  sepal_length  sepal_width  petal_length  petal_width
#     0      setosa         5.006        3.428         1.462        0.246
#     1  versicolor         5.936        2.770         4.260        1.326
#     2   virginica         6.588        2.974         5.552        2.026
# Missing data
# ~~~~~~~~~~~~
# Add some missing data to the previous table ``users``:

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Exercises: Pandas: data manipulation
------------------------------------
Data Frame
~~~~~~~~~~
1. Read the iris dataset at "https://github.com/neurospin/pystatsml/tree/master/datasets/iris.csv"
2. Print column names
3. Get numerical columns
4. For each species compute the mean of numerical columns and store it in  a ``stats`` table like:
::
          species  sepal_length  sepal_width  petal_length  petal_width
    0      setosa         5.006        3.428         1.462        0.246
    1  versicolor         5.936        2.770         4.260        1.326
    2   virginica         6.588        2.974         5.552        2.026
"""

url = "https://github.com/duchesnay/pystatsml/raw/master/datasets/iris.csv"
df = pd.read_csv(url)

num_cols = df._get_numeric_data().columns

stats = list()

for grp, d in df.groupby("species"):
    print(grp)
    # print()
    stats.append([grp] + d.loc[:, num_cols].mean(axis=0).tolist())

stats = pd.DataFrame(stats, columns=["species"] + num_cols.tolist())
print(stats)

df.groupby("species").mean()

df.loc[[0, 1], "petal_width"] = None

df.petal_width

df["petal_width"][df["petal_width"].isnull()] = df["petal_width"][
    df["petal_width"].notnull()
].median()

l = [(1, "a", 1), (2, "b", 2)]

for x, y, z in l:
    print(x, y, z)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Numpy: arrays and matrices
==========================
NumPy is an extension to the Python programming language,
adding support for large,
multi-dimensional (numerical) arrays and matrices,
along with a large library of high-level mathematical functions to operate on these arrays.

**Sources**:
- Kevin Markham: https://github.com/justmarkham
Computation time:
    l = [v for v in range(10 ** 8)]
    s = 0
    %time for v in l: s += v
    arr = np.arange(10 ** 8)
    %time arr.sum()
"""

##############################################################################
# Create arrays
# Create ndarrays from lists.
# note: every element must be the same type (will be converted if possible)

data1 = [1, 2, 3, 4, 5]  # list
arr1 = np.array(data1)  # 1d array
data2 = [range(1, 5), range(5, 9)]  # list of lists
arr2 = np.array(data2)  # 2d array
arr2.tolist()  # convert array back to list

##############################################################################
# create special arrays

np.zeros(10)
np.zeros((3, 6))
np.ones(10)
np.linspace(0, 1, 5)  # 0 to 1 (inclusive) with 5 points
np.logspace(0, 3, 4)  # 10^0 to 10^3 (inclusive) with 4 points

##############################################################################
# arange is like range, except it returns an array (not a list)

int_array = np.arange(5)
float_array = int_array.astype(float)

##############################################################################
# Examining arrays

arr1.dtype  # float64
arr2.ndim  # 2
arr2.shape  # (2, 4) - axis 0 is rows, axis 1 is columns
arr2.size  # 8 - total number of elements
len(arr2)  # 2 - size of first dimension (aka axis)

##############################################################################
# Reshaping

arr = np.arange(10, dtype=float).reshape((2, 5))
print(arr.shape)
print(arr.reshape(5, 2))

##############################################################################
# Add an axis

a = np.array([0, 1])
a_col = a[:, np.newaxis]
print(a_col)

a_col = a[:, None]

##############################################################################
# Transpose

print(a_col.T)

##############################################################################
# Flatten: always returns a flat copy of the orriginal array

arr_flt = arr.flatten()
arr_flt[0] = 33
print(arr_flt)
print(arr)

##############################################################################
# Ravel: returns a view of the original array whenever possible.

arr_flt = arr.ravel()
arr_flt[0] = 33
print(arr_flt)
print(arr)

##############################################################################
# Summary on axis, reshaping/flattening and selection
# ---------------------------------------------------
# Numpy internals: By default Numpy use C convention, ie, Row-major language:
# The matrix is stored by rows. In C, the last index changes most rapidly as one moves through the array as stored in memory.
# For 2D arrays, sequential move in the memory will:
# - iterate over rows (axis 0)
#    - iterate over columns (axis 1)
# For 3D arrays, sequential move in the memory will:
# - iterate over plans (axis 0)
#    - iterate over rows (axis 1)
#        - iterate over columns (axis 2)

x = np.arange(2 * 3 * 4)
print(x)

##############################################################################
# Reshape into 3D (axis 0, axis 1, axis 2)

x = x.reshape(2, 3, 4)
print(x)

##############################################################################
# Selection get first plan

print(x[0, :, :])

##############################################################################
# Selection get first rows

print(x[:, 0, :])

##############################################################################
# Selection get first columns

print(x[:, :, 0])

##############################################################################
# Simple example with 2 array
# Exercise:
# - Get second line
# - Get third column

arr = np.arange(10, dtype=float).reshape((2, 5))
print(arr)

arr[1, :]
arr[:, 2]

##############################################################################
# Ravel

print(x.ravel())

##############################################################################
# Stack arrays

a = np.array([0, 1])
b = np.array([2, 3])

##############################################################################
# Horizontal stacking

np.hstack([a, b])

##############################################################################
# Vertical stacking

np.vstack([a, b])

##############################################################################
# Default Vertical

np.stack([a, b])

##############################################################################
# Selection
# Single item

arr = np.arange(10, dtype=float).reshape((2, 5))

arr[0]  # 0th element (slices like a list)
arr[0, 3]  # row 0, column 3: returns 4
arr[0][3]  # alternative syntax

##############################################################################
# Slicing
# Syntax: ``start:stop:step`` with ``start`` *(default 0)* ``stop`` *(default last)* ``step`` *(default 1)*

arr[0, :]  # row 0: returns 1d array ([1, 2, 3, 4])
arr[:, 0]  # column 0: returns 1d array ([1, 5])
arr[:, :2]  # columns strictly before index 2 (2 first columns)
arr[:, 2:]  # columns after index 2 included
arr2 = arr[:, 1:4]  # columns between index 1 (included) and 4 (excluded)
print(arr2)

##############################################################################
# Slicing returns a view (not a copy)
# Modification

arr2[0, 0] = 33
print(arr2)
print(arr)

##############################################################################
# Row 0: reverse order
print(arr[0, ::-1])

# The rule of thumb here can be: in the context of lvalue indexing (i.e. the indices are placed in the left hand side value of an assignment), no view or copy of the array is created (because there is no need to). However, with regular values, the above rules for creating views does apply.
##############################################################################
# Fancy indexing: Integer or boolean array indexing
# Fancy indexing returns a copy not a view.
# Integer array indexing

arr2 = arr[:, [1, 2, 3]]  # return a copy
print(arr2)
arr2[0, 0] = 44
print(arr2)
print(arr)

##############################################################################
# Boolean arrays indexing

arr2 = arr[arr > 5]  # return a copy

print(arr2)
arr2[0] = 44
print(arr2)
print(arr)

##############################################################################
# However, In the context of lvalue indexing (left hand side value of an assignment)
# Fancy authorizes the modification of the original array

arr[arr > 5] = 0
print(arr)

##############################################################################
# Boolean arrays indexing continues

names = np.array(["Bob", "Joe", "Will", "Bob"])
names == "Bob"  # returns a boolean array
names[names != "Bob"]  # logical selection
(names == "Bob") | (names == "Will")  # keywords "and/or" don't work with boolean arrays
names[names != "Bob"] = "Joe"  # assign based on a logical selection
np.unique(names)  # set function

##############################################################################
# Vectorized operations

nums = np.arange(5)
nums * 10  # multiply each element by 10
nums = np.sqrt(nums)  # square root of each element
np.ceil(nums)  # also floor, rint (round to nearest int)
np.isnan(nums)  # checks for NaN
nums + np.arange(5)  # add element-wise
np.maximum(nums, np.array([1, -2, 3, -4, 5]))  # compare element-wise

# math and stats
A = np.random.randn(4, 2)  # random normals in 4x2 array
print(A)
cc = A.mean()
print(cc)
cc = A.std()
print(cc)

cc = A.argmin()  # index of minimum element
print(cc)

cc = A.sum()
print(cc)

cc = A.sum(axis=0)  # sum of columns
print(cc)

cc = A.sum(axis=1)  # sum of rows
print(cc)

# methods for boolean arrays
cc = (A > 0).sum()  # counts number of positive values
print(cc)

cc = (A > 0).any()  # checks if any value is True
print(cc)

cc = (A > 0).all()  # checks if all values are True
print(cc)

# random numbers
cc = np.random.rand(2, 3)  # 2 x 3 matrix in [0, 1]
print(cc)

cc = np.random.randn(10)  # random normals (mean 0, sd 1)
print(cc)

cc = np.random.randint(0, 2, 10)  # 10 randomly picked 0 or 1
print(cc)

##############################################################################
# Broadcasting
# Sources: https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html
# Implicit conversion to allow operations on arrays of different sizes.
# - The smaller array is stretched or “broadcasted” across the larger array so that they have compatible shapes.
# - Fast vectorized operation in C instead of Python.
# - No needless copies.
# Rules
# Starting with the trailing axis and working backward, Numpy compares arrays dimensions.
# - If two dimensions are equal then continues
# - If one of the operand has dimension 1 stretches it to match the largest one
# - When one of the shapes runs out of dimensions (because it has less dimensions than the other shape), Numpy will use 1 in the comparison process until the other shape's dimensions run out as well.

a = np.array([[0, 0, 0], [10, 10, 10], [20, 20, 20], [30, 30, 30]])

b = np.array([0, 1, 2])

print(a + b)

##############################################################################
# Center data column-wise

a - a.mean(axis=0)

##############################################################################
# Scale (center, normalise) data column-wise

(a - a.mean(axis=0)) / a.std(axis=0)

##############################################################################
# Examples
# Shapes of operands A, B and result:
#   A      (2d array):  5 x 4
#   B      (1d array):      1
#   Result (2d array):  5 x 4
#
#   A      (2d array):  5 x 4
#   B      (1d array):      4
#   Result (2d array):  5 x 4
#
#   A      (3d array):  15 x 3 x 5
#   B      (3d array):  15 x 1 x 5
#   Result (3d array):  15 x 3 x 5
#
#   A      (3d array):  15 x 3 x 5
#   B      (2d array):       3 x 5
#   Result (3d array):  15 x 3 x 5
#
#   A      (3d array):  15 x 3 x 5
#   B      (2d array):       3 x 1
#   Result (3d array):  15 x 3 x 5


##############################################################################
# Exercises
# ---------
# Given the array:

A = np.random.randn(4, 2)  # random normals in 4x2 array
print(A)

##############################################################################
# - For each column find the row index of the minimum value.
# - Write a function ``standardize(A)`` that return an array whose columns are centered and scaled (by std-dev).

print("------------------------------------------------------------")  # 60個

A = np.random.randn(4, 2)
print(A)

# For each column find the row indices of the minimiun value.

[np.argmin(A[:, j]) for j in range(A.shape[1])]

np.argmin(A, axis=0)

# Write a function ``scale(A)`` that return an array whose columns are centered and scaled (by std-dev).


def scale(A):
    return (A - A.mean(axis=0)) / A.std(axis=0)


A = np.random.randn(5, 3)
As = scale(A)

As.mean(axis=0)
As.std(axis=0)

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(9, 3))
x = np.linspace(0, 10, 50)
sinus = np.sin(x)

plt.plot(x, sinus)
plt.show()

plt.figure(figsize=(9, 3))

plt.plot(x, sinus, "o")
plt.show()
# use plt.plot to get color / marker abbreviations

# Rapid multiplot

plt.figure(figsize=(9, 3))
cosinus = np.cos(x)
plt.plot(x, sinus, "-b", x, sinus, "ob", x, cosinus, "-r", x, cosinus, "or")
plt.xlabel("this is x!")
plt.ylabel("this is y!")
plt.title("My First Plot")
plt.show()

# Step by step

plt.figure(figsize=(9, 3))
plt.plot(x, sinus, label="sinus", color="blue", linestyle="--", linewidth=2)
plt.plot(x, cosinus, label="cosinus", color="red", linestyle="-", linewidth=2)
plt.legend()
plt.show()

# Scatter (2D) plots

salary = pd.read_csv("data/salary_table.csv")
print(salary.head())

df = salary
print(df.head())

# Simple scatter with colors

plt.figure(figsize=(3, 3), dpi=100)
_ = sns.scatterplot(x="experience", y="salary", hue="education", data=salary)

# Legend outside

ax = sns.relplot(x="experience", y="salary", hue="education", data=salary)

# Linear model

ax = sns.lmplot(x="experience", y="salary", hue="education", data=salary)

# Scatter plot with colors and symbols

ax = sns.relplot(
    x="experience", y="salary", hue="education", style="management", data=salary
)

# Saving Figures

### bitmap format
plt.plot(x, sinus)
plt.savefig("tmp_sinus.png")
plt.close()

# Prefer vectorial format (SVG: Scalable Vector Graphics) can be edited with
# Inkscape, Adobe Illustrator, Blender, etc.
plt.plot(x, sinus)
plt.savefig("tmp_sinus.svg")
plt.close()

# Or pdf
plt.plot(x, sinus)
plt.savefig("tmp_sinus.pdf")
plt.close()

# Boxplot and violin plot: one factor

# Box plots are non-parametric: they display variation in samples of a statistical population without making any assumptions of the underlying statistical distribution.

# title{width=7cm}

ax = sns.boxplot(x="management", y="salary", data=salary)
ax = sns.stripplot(x="management", y="salary", data=salary, jitter=True, color="black")
ax = sns.violinplot(x="management", y="salary", data=salary)
ax = sns.stripplot(x="management", y="salary", data=salary, jitter=True, color="white")

# Boxplot and violin plot: two factors

ax = sns.boxplot(x="management", y="salary", hue="education", data=salary)
ax = sns.stripplot(
    x="management",
    y="salary",
    hue="education",
    data=salary,
    jitter=True,
    dodge=True,
    linewidth=1,
)

ax = sns.violinplot(x="management", y="salary", hue="education", data=salary)
ax = sns.stripplot(
    x="management",
    y="salary",
    hue="education",
    data=salary,
    jitter=True,
    dodge=True,
    linewidth=1,
)

# Distributions and density plot

ax = sns.displot(x="salary", hue="management", kind="kde", data=salary, fill=True)

# Multiple axis

fig, axes = plt.subplots(3, 1, figsize=(9, 9), sharex=True)

i = 0
for edu, d in salary.groupby(["education"]):
    sns.kdeplot(
        x="salary", hue="management", data=d, fill=True, ax=axes[i], palette="muted"
    )
    axes[i].set_title(edu)
    i += 1

# Pairwise scatter plots

ax = sns.pairplot(salary, hue="management")

# Time series

sns.set(style="darkgrid")

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")

""" NG
# Plot the responses for different events and regions
ax = sns.pointplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
# Correlation and covariance
from numpy.random import randint as ri

A = ri(1, 5, 20)  # 20 random integeres from a small range (1-10)
B = 2 * A + 5 * np.random.randn(20)  # B is twice that of A plus some random noise
print("\nB is twice that of A plus some random noise")
plt.scatter(A, B)  # Scatter plot of B
plt.title("Scatter plot of A vs. B, expect a small positive correlation")
show()

print(np.corrcoef(A, B))  # Correleation coefficient matrix between A and B

A = ri(1, 50, 20)  # 20 random integeres from a larger range (1-50)
B = (
    100 - 2 * A + 10 * np.random.randn(20)
)  # B is 100 minus twice that of A plus some random noise
print("\nB is 100 minus twice that of A plus some random noise")
plt.scatter(A, B)  # Scatter plot of B
plt.title("Scatter plot of A vs. B, expect a large negative correlation")
show()

print(np.corrcoef(A, B))  # Correleation coefficient matrix between A and B

print("------------------------------------------------------------")  # 60個

# Singular value decomposition (SVD) 奇異值分解

A = np.random.randint(1, 10, 9).reshape(3, 3)
print("Original matrix\n", A)
print("\n")
u, s, v = np.linalg.svd(A, compute_uv=1, full_matrices=True)
print("u:", u)
print("\n")
print("Singular values, s:", s)
print("\n")
print("v:", v)
print("\n")
print("Reconstruction of A, u*s*v\n", np.dot(u, np.dot(np.diag(s), v)))

print("------------------------------------------------------------")  # 60個

# QR decomposition/factorization

A = np.random.randint(1, 10, 9).reshape(3, 3)
print("Original matrix\n", A)
print("\n")
q, r = np.linalg.qr(A)
print("Q:", q)
print("\n")
print("R:", r)
print("\n")
print("Reconstruction of A, Q*R\n", np.dot(q, r))

print("------------------------------------------------------------")  # 60個

# Eigenvalues and eigenvectors

A = np.random.randn(9).reshape(3, 3)
print("Original matrix\n", A)
print("\n")
w, v = np.linalg.eig(A)
print("Eigenvalues:\n", w)
print("\n")
print("Eigenvectors:\n", v)

print("------------------------------------------------------------")  # 60個

# Linear equation solving, matrix inverse, linear least suqare

A = np.array([[2, 5, 1], [3, -2, -1], [1, -3, 1]])
B = np.array([14, -1, 4])
x = np.linalg.solve(A, B)

print("The solutions are:", x)

x = np.arange(1, 11, 1)
y = 2 * x + np.random.randn(10) - 1
print(x)
print(y)

A = np.vstack([x, np.ones(len(x))]).T
print(A)

m, c = np.linalg.lstsq(A, y)[0]
print("Coefficient:" + str(m) + "\n" + "intercept:" + str(c))

# Plot the fitteed line
plt.plot(x, y, "o", label="Original data", markersize=10)
plt.plot(x, m * x + c, "r", label="Fitted line")
plt.legend()
show()

# Coefficient:1.94754443612
# intercept:-0.719737172139

A = 0.1 * np.random.randint(1, 20, 16).reshape(4, 4)
print("A:\n", A)
print("Inverse of A:\n", np.linalg.inv(A))

A = 0.1 * np.random.randint(1, 20, 15).reshape(5, 3)
print("A:\n", A)
print("Pseudo-inverse of A:\n", np.linalg.pinv(A))
print("Matrix product of A and pseudo inverse:\n", np.dot(np.linalg.pinv(A), A))

print("------------------------------------------------------------")  # 60個

# Speed difference between reading numerical data from plain CSV vs. using .npy file format
# 比較速度

n_samples = 1000000

with open("tmp_fdata.txt", "w") as fdata:
    for _ in range(n_samples):
        fdata.write(str(10 * np.random.random()) + ",")

t1 = time.time()
array_direct = np.fromfile("tmp_fdata.txt", dtype=float, count=-1, sep=",").reshape(
    1000, 1000
)
t2 = time.time()

print(array_direct)
print("\nShape: ", array_direct.shape)
print(f"Time took to read: {t2-t1} seconds.")

t1 = time.time()
with open("tmp_fdata.txt", "r") as fdata:
    datastr = fdata.read()
lst = datastr.split(",")
lst.pop()
array_lst = np.array(lst, dtype=float).reshape(1000, 1000)
t2 = time.time()

print(array_lst)
print("\nShape: ", array_lst.shape)
print(f"Time took to read: {t2-t1} seconds.")

np.save("fnumpy.npy", array_lst)

t1 = time.time()
array_reloaded = np.load("fnumpy.npy")
t2 = time.time()

print(array_reloaded)
print("\nShape: ", array_reloaded.shape)
print(f"Time took to load: {t2-t1} seconds.")

t1 = time.time()
array_reloaded = np.load("fnumpy.npy").reshape(10000, 100)
t2 = time.time()

print(array_reloaded)
print("\nShape: ", array_reloaded.shape)
print(f"Time took to load: {t2-t1} seconds.")

# Speed enhancement as the sample size grows...

n_samples = [100000 * i for i in range(1, 11)]
time_lst_read = []
time_npy_read = []

for sample_size in n_samples:
    with open("tmp_fdata.txt", "w") as fdata:
        for _ in range(sample_size):
            fdata.write(str(10 * np.random.random()) + ",")

    t1 = time.time()
    with open("tmp_fdata.txt", "r") as fdata:
        datastr = fdata.read()
    lst = datastr.split(",")
    lst.pop()
    array_lst = np.array(lst, dtype=float)
    t2 = time.time()
    time_lst_read.append(1000 * (t2 - t1))
    print("Array shape:", array_lst.shape)

    np.save("fnumpy.npy", array_lst)

    t1 = time.time()
    array_reloaded = np.load("fnumpy.npy")
    t2 = time.time()
    time_npy_read.append(1000 * (t2 - t1))
    print("Array shape:", array_reloaded.shape)

    print(f"Processing done for {sample_size} samples\n")

plt.figure(figsize=(8, 5))
# plt.xscale("log")
# plt.yscale("log")
plt.scatter(n_samples, time_lst_read)
plt.scatter(n_samples, time_npy_read)
plt.legend(["Normal read from CSV", "Read from .npy file"])
show()

print(time_npy_read)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Series

labels = ["a", "b", "c"]
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {"a": 10, "b": 20, "c": 30}

print("Labels:", labels)
print("My data:", my_data)
print("Dictionary:", d)

# Creating a Series (Pandas class)

cc = pd.Series(data=my_data)  # Output looks very similar to a NumPy array
print(cc)

cc = pd.Series(data=my_data, index=labels)  # Note the extra information about index
print(cc)

# Inputs are in order of the expected parameters (not explicitly named), NumPy array is used for data
cc = pd.Series(arr, labels)
print(cc)

cc = pd.Series(d)  # Using a pre-defined Dictionary object
print(cc)

# What type of values can a Pandas Series hold?

print("\nHolding numerical data\n", "-" * 25, sep="")
print(pd.Series(arr))
print("\nHolding text labels\n", "-" * 20, sep="")
print(pd.Series(labels))
print("\nHolding functions\n", "-" * 20, sep="")
print(pd.Series(data=[sum, print, len]))
print("\nHolding objects from a dictionary\n", "-" * 40, sep="")
print(pd.Series(data=[d.keys, d.items, d.values]))


# Indexing and slicing

ser1 = pd.Series([1, 2, 3, 4], ["CA", "OR", "CO", "AZ"])
ser2 = pd.Series([1, 2, 5, 4], ["CA", "OR", "NV", "AZ"])

print("\nIndexing by name of the item/object (string identifier)\n", "-" * 56, sep="")
print("Value for CA in ser1:", ser1["CA"])
print("Value for AZ in ser1:", ser1["AZ"])
print("Value for NV in ser2:", ser2["NV"])

print("\nIndexing by number (positional value in the series)\n", "-" * 52, sep="")
print("Value for CA in ser1:", ser1[0])
print("Value for AZ in ser1:", ser1[3])
print("Value for NV in ser2:", ser2[2])

print("\nIndexing by a range\n", "-" * 25, sep="")
print("Value for OR, CO, and AZ in ser1:\n", ser1[1:4], sep="")

# Adding/Merging two series with common indices

ser1 = pd.Series([1, 2, 3, 4], ["CA", "OR", "CO", "AZ"])
ser2 = pd.Series([1, 2, 5, 4], ["CA", "OR", "NV", "AZ"])
ser3 = ser1 + ser2

print(
    "\nAfter adding the two series, the result looks like this...\n", "-" * 59, sep=""
)
print(ser3)
print(
    "\nPython tries to add values where it finds common index name, and puts NaN where indices are missing\n"
)

print("\nThe idea works even for multiplication...\n", "-" * 43, sep="")
print(ser1 * ser2)

print("\nOr even for combination of mathematical operations!\n", "-" * 53, sep="")
print(np.exp(ser1) + np.log10(ser2))

# Python tries to add values where it finds common index name, and puts NaN where indices are missing

# DataFrame (the Real Meat!)

from numpy.random import randn as rn

# Creating and accessing DataFrame

np.random.seed(101)
matrix_data = rn(5, 4)
row_labels = ["A", "B", "C", "D", "E"]
column_headings = ["W", "X", "Y", "Z"]

df = pd.DataFrame(data=matrix_data, index=row_labels, columns=column_headings)
print("\nThe data frame looks like\n", "-" * 45, sep="")
print(df)

# Indexing and slicing (columns)

print("\nThe 'X' column\n", "-" * 25, sep="")
print(df["X"])
print("\nType of the column: ", type(df["X"]), sep="")
print("\nThe 'X' and 'Z' columns indexed by passing a list\n", "-" * 55, sep="")
print(df[["X", "Z"]])
print("\nType of the pair of columns: ", type(df[["X", "Z"]]), sep="")
print("\nSo, for more than one column, the object turns into a DataFrame")

print("\nThe 'X' column accessed by DOT method (NOT recommended)\n", "-" * 55, sep="")
print(df.X)

# Creating and deleting a (new) column (or row)

print(
    "\nA column is created by assigning it in relation to an existing column\n",
    "-" * 75,
    sep="",
)
df["New"] = df["X"] + df["Z"]
df["New (Sum of X and Z)"] = df["X"] + df["Z"]
print(df)
print("\nA column is dropped by using df.drop() method\n", "-" * 55, sep="")
df = df.drop(
    "New", axis=1
)  # Notice the axis=1 option, axis = 0 is default, so one has to change it to 1
print(df)
df1 = df.drop("A")
print(
    "\nA row (index) is dropped by using df.drop() method and axis=0\n",
    "-" * 65,
    sep="",
)
print(df1)
print(
    "\nAn in-place change can be done by making inplace=True in the drop method\n",
    "-" * 75,
    sep="",
)
df.drop("New (Sum of X and Z)", axis=1, inplace=True)
print(df)

# Selecting/indexing Rows

print("\nLabel-based 'loc' method can be used for selecting row(s)\n", "-" * 60, sep="")
print("\nSingle row\n")
print(df.loc["C"])
print("\nMultiple rows\n")
print(df.loc[["B", "C"]])
print(
    "\nIndex position based 'iloc' method can be used for selecting row(s)\n",
    "-" * 70,
    sep="",
)
print("\nSingle row\n")
print(df.iloc[2])
print("\nMultiple rows\n")
print(df.iloc[[1, 2]])

# Subsetting DataFrame

np.random.seed(101)
matrix_data = rn(5, 4)
row_labels = ["A", "B", "C", "D", "E"]
column_headings = ["W", "X", "Y", "Z"]
df = pd.DataFrame(data=matrix_data, index=row_labels, columns=column_headings)

print("\nThe DatFrame\n", "-" * 45, sep="")
print(df)
print("\nElement at row 'B' and column 'Y' is\n")
print(df.loc["B", "Y"])
print("\nSubset comprising of rows B and D, and columns W and Y, is\n")
df.loc[["B", "D"], ["W", "Y"]]

# Conditional selection, index (re)setting, multi-index
# Basic idea of conditional check and Boolean DataFrame

print("\nThe DataFrame\n", "-" * 45, sep="")
print(df)
print(
    "\nBoolean DataFrame(s) where we are checking if the values are greater than 0\n",
    "-" * 75,
    sep="",
)
print(df > 0)
print("\n")
print(df.loc[["A", "B", "C"]] > 0)
booldf = df > 0
print("\nDataFrame indexed by boolean dataframe\n", "-" * 45, sep="")
print(df[booldf])

# Passing Boolean series to conditionally subset the DataFrame

matrix_data = np.matrix("22,66,140;42,70,148;30,62,125;35,68,160;25,62,152")
row_labels = ["A", "B", "C", "D", "E"]
column_headings = ["Age", "Height", "Weight"]

df = pd.DataFrame(data=matrix_data, index=row_labels, columns=column_headings)
print("\nA new DataFrame\n", "-" * 25, sep="")
print(df)
print("\nRows with Height > 65 inch\n", "-" * 35, sep="")
print(df[df["Height"] > 65])

booldf1 = df["Height"] > 65
booldf2 = df["Weight"] > 145
print("\nRows with Height > 65 inch and Weight >145 lbs\n", "-" * 55, sep="")
print(df[(booldf1) & (booldf2)])

print(
    "\nDataFrame with only Age and Weight columns whose Height > 65 inch\n",
    "-" * 68,
    sep="",
)
print(df[booldf1][["Age", "Weight"]])

# Re-setting and Setting Index

matrix_data = np.matrix("22,66,140;42,70,148;30,62,125;35,68,160;25,62,152")
row_labels = ["A", "B", "C", "D", "E"]
column_headings = ["Age", "Height", "Weight"]

df = pd.DataFrame(data=matrix_data, index=row_labels, columns=column_headings)
print("\nThe DataFrame\n", "-" * 25, sep="")
print(df)
print("\nAfter resetting index\n", "-" * 35, sep="")
print(df.reset_index())
print("\nAfter resetting index with 'drop' option TRUE\n", "-" * 45, sep="")
print(df.reset_index(drop=True))
print("\nAdding a new column 'Profession'\n", "-" * 45, sep="")
df["Profession"] = "Student Teacher Engineer Doctor Nurse".split()
print(df)
print("\nSetting 'Profession' column as index\n", "-" * 45, sep="")
print(df.set_index("Profession"))

# Multi-indexing

# Index Levels
outside = ["G1", "G1", "G1", "G2", "G2", "G2"]
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))

print("\nTuple pairs after the zip and list command\n", "-" * 45, sep="")
print(hier_index)
hier_index = pd.MultiIndex.from_tuples(hier_index)
print("\nIndex hierarchy\n", "-" * 25, sep="")
print(hier_index)
print("\nIndex hierarchy type\n", "-" * 25, sep="")
print(type(hier_index))

print("\nCreating DataFrame with multi-index\n", "-" * 37, sep="")
np.random.seed(101)
df1 = pd.DataFrame(
    data=np.round(rn(6, 3), 2), index=hier_index, columns=["A", "B", "C"]
)
print(df1)

print("\nSubsetting multi-index DataFrame using two 'loc' methods\n", "-" * 60, sep="")
print(df1.loc["G2"].loc[[1, 3]][["B", "C"]])

print("\nNaming the indices by 'index.names' method\n", "-" * 45, sep="")
df1.index.names = ["Outer", "Inner"]
print(df1)

# Cross-section ('XS') command

print("\nGrabbing a cross-section from outer level\n", "-" * 45, sep="")
print(df1.xs("G1"))
print(
    "\nGrabbing a cross-section from inner level (for all outer levels)\n",
    "-" * 65,
    sep="",
)
print(df1.xs(2, level="Inner"))

# Missing Values

df = pd.DataFrame({"A": [1, 2, np.nan], "B": [5, np.nan, np.nan], "C": [1, 2, 3]})
df["States"] = "CA NV AZ".split()
df.set_index("States", inplace=True)
print(df)

# Pandas 'dropna' method

print("\nDropping any rows with a NaN value\n", "-" * 35, sep="")
print(df.dropna(axis=0))
print("\nDropping any column with a NaN value\n", "-" * 35, sep="")
print(df.dropna(axis=1))
print(
    "\nDropping a row with a minimum 2 NaN value using 'thresh' parameter\n",
    "-" * 68,
    sep="",
)
print(df.dropna(axis=0, thresh=2))

# Pandas 'fillna' method

print("\nFilling values with a default value\n", "-" * 35, sep="")
print(df.fillna(value="FILL VALUE"))
print(
    "\nFilling values with a computed value (mean of column A here)\n", "-" * 60, sep=""
)
print(df.fillna(value=df["A"].mean()))

# GroupBy method

# Create dataframe
data = {
    "Company": ["GOOG", "GOOG", "MSFT", "MSFT", "FB", "FB"],
    "Person": ["Sam", "Charlie", "Amy", "Vanessa", "Carl", "Sarah"],
    "Sales": [200, 120, 340, 124, 243, 350],
}
df = pd.DataFrame(data)
print(df)

byComp = df.groupby("Company")
print("\nGrouping by 'Company' column and listing mean sales\n", "-" * 55, sep="")
# NG print(byComp.mean())
print("\nGrouping by 'Company' column and listing sum of sales\n", "-" * 55, sep="")
print(byComp.sum())
# Note dataframe conversion of the series and transpose
print("\nAll in one line of command (Stats for 'FB')\n", "-" * 65, sep="")
print(pd.DataFrame(df.groupby("Company").describe().loc["FB"]).transpose())
print("\nSame type of extraction with little different command\n", "-" * 68, sep="")
print(df.groupby("Company").describe().loc[["GOOG", "MSFT"]])

# Merging, Joining, Concatenating
# Concatenation

# Creating data frames
df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)

df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)

df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)

print("\nThe DataFrame number 1\n", "-" * 30, sep="")
print(df1)
print("\nThe DataFrame number 2\n", "-" * 30, sep="")
print(df2)
print("\nThe DataFrame number 3\n", "-" * 30, sep="")
print(df3)

df_cat1 = pd.concat([df1, df2, df3], axis=0)
print("\nAfter concatenation along row\n", "-" * 30, sep="")
print(df_cat1)

df_cat2 = pd.concat([df1, df2, df3], axis=1)
print("\nAfter concatenation along column\n", "-" * 60, sep="")
print(df_cat2)
df_cat2.fillna(value=0, inplace=True)
print("\nAfter filling missing values with zero\n", "-" * 60, sep="")
print(df_cat2)

# Merging by a common 'key'

left = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)

right = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)

print("\nThe DataFrame 'left'\n", "-" * 30, sep="")
print(left)
print("\nThe DataFrame 'right'\n", "-" * 30, sep="")
print(right)

merge1 = pd.merge(left, right, how="inner", on="key")
print("\nAfter simple merging with 'inner' method\n", "-" * 50, sep="")
print(merge1)

# Merging on a set of keys

left = pd.DataFrame(
    {
        "key1": ["K0", "K0", "K1", "K2"],
        "key2": ["K0", "K1", "K0", "K1"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)

right = pd.DataFrame(
    {
        "key1": ["K0", "K1", "K1", "K2"],
        "key2": ["K0", "K0", "K0", "K0"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)

print(left)

print(right)

cc = pd.merge(left, right, on=["key1", "key2"])
print(cc)

cc = pd.merge(left, right, how="outer", on=["key1", "key2"])
print(cc)

cc = pd.merge(left, right, how="left", on=["key1", "key2"])
print(cc)

cc = pd.merge(left, right, how="right", on=["key1", "key2"])
print(cc)

# Joining

left = pd.DataFrame(
    {"A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]}, index=["K0", "K1", "K2"]
)

right = pd.DataFrame(
    {"C": ["C0", "C2", "C3"], "D": ["D0", "D2", "D3"]}, index=["K0", "K2", "K3"]
)

print(left)

print(right)

cc = left.join(right)
print(cc)

cc = left.join(right, how="outer")
print(cc)

# Useful operations

df = pd.DataFrame(
    {
        "col1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "col2": [444, 555, 666, 444, 333, 222, 666, 777, 666, 555],
        "col3": "aaa bb c dd eeee fff gg h iii j".split(),
    }
)
print(df)

print("\nMethod head() is for showing first few entries\n", "-" * 50, sep="")
cc = df.head()
print(cc)

print(
    "\nFinding unique values in 'col2'\n", "-" * 40, sep=""
)  # Note 'unique' method applies to pd.series only
print(df["col2"].unique())

print("\nFinding number of unique values in 'col2'\n", "-" * 45, sep="")
print(df["col2"].nunique())

print("\nTable of unique values in 'col2'\n", "-" * 40, sep="")
t1 = df["col2"].value_counts()
print(t1)

# Applying functions


# Define a function
def testfunc(x):
    if x > 500:
        return 10 * np.log10(x)
    else:
        return x / 10


df["FuncApplied"] = df["col2"].apply(testfunc)
print(df)

# Apply works with built-in function too!

df["col3length"] = df["col3"].apply(len)
print(df)

# Combine 'apply' with lambda expession for in-line calculations

cc = df["FuncApplied"].apply(lambda x: np.sqrt(x))
print(cc)

# Standard statistical functions directly apply to columns

print("\nSum of the column 'FuncApplied' is: ", df["FuncApplied"].sum())
print("Mean of the column 'FuncApplied' is: ", df["FuncApplied"].mean())
print("Std dev of the column 'FuncApplied' is: ", df["FuncApplied"].std())
print(
    "Min and max of the column 'FuncApplied' are: ",
    df["FuncApplied"].min(),
    "and",
    df["FuncApplied"].max(),
)

# Deletion, sorting, list of column and row names
# Getting the names of the columns

print("\nName of columns\n", "-" * 20, sep="")
print(df.columns)
l = list(df.columns)
print("\nColumn names in a list of strings for later manipulation:", l)

# Deletion by 'del' command # This affects the dataframe immediately, unlike drop method.

print("\nDeleting last column by 'del' command\n", "-" * 50, sep="")
del df["col3length"]
print(df)
df["col3length"] = df["col3"].apply(len)

cc = df.sort_values(by="col2")  # inplace=False by default
print(cc)

cc = df.sort_values(by="FuncApplied", ascending=False)  # inplace=False by default
print(cc)

# Find Null Values or Check for Null Values

df = pd.DataFrame(
    {
        "col1": [1, 2, 3, np.nan],
        "col2": [np.nan, 555, 666, 444],
        "col3": ["abc", "def", "ghi", "xyz"],
    }
)
print(df.head())

cc = df.isnull()
print(cc)

cc = df.fillna("FILL")
print(cc)

# Pivot Table

data = {
    "A": ["foo", "foo", "foo", "bar", "bar", "bar"],
    "B": ["one", "one", "two", "two", "one", "one"],
    "C": ["x", "y", "x", "y", "x", "y"],
    "D": [1, 3, 2, 5, 4, 1],
}

df = pd.DataFrame(data)
print(df)

# Index out of 'A' and 'B', columns from 'C', actual numerical values from 'D'
cc = df.pivot_table(values="D", index=["A", "B"], columns=["C"])
print(cc)

# Index out of 'A' and 'B', columns from 'C', actual numerical values from 'D'
cc = df.pivot_table(values="D", index=["A", "B"], columns=["C"], fill_value="FILLED")
print(cc)

print("------------------------------------------------------------")  # 60個

# Pandas built-in Visualization

df1 = pd.read_csv("data/pandas_data1.csv", index_col=0)
cc = df1.head()
print(cc)

df2 = pd.read_csv("data/pandas_data1.csv")
cc = df2.head()
print(cc)

# Histogram of a single column

df1["A"].hist()

show()

# Histogram with a different set of arguments (list of columns, bins, figure size, etc)

df1.hist(column=["B", "C"], bins=20, figsize=(10, 4))
show()

# Histogram with generic plot method of Pandas

df1.plot(kind="hist", bins=30, grid=True, figsize=(12, 7))
show()

# Area plot
# df2.plot.area(alpha=0.4)
# show()

# Bar plot (with and without stacking)

df2.plot.bar()

show()

df2.plot.bar(stacked=True)

show()

# Lineplot

# df1.plot.line(x=df1.index, y=["B", "C"], figsize=(12, 4), lw=1)
# show()

# Scatterplot

df1.plot.scatter(x="A", y="B", figsize=(12, 8))

show()

df1.plot.scatter(
    x="A", y="B", c="C", cmap="coolwarm", figsize=(12, 8)
)  # Color of the scatter dots set based on column C

show()

df1.plot.scatter(
    x="A", y="B", s=10 * np.exp(df1["C"]), c="C", figsize=(12, 8)
)  # Size of the dots set based on column C

show()

# Boxplot

df2.plot.box()

show()

# Hexagonal bin plot for bivariate data

df = pd.DataFrame(data=np.random.randn(1000, 2), columns=["A", "B"])
cc = df.head()
print(cc)

df.plot.hexbin(x="A", y="B", gridsize=30, cmap="coolwarm")
show()

# Kernel density estimation

df2.plot.density(lw=3)

show()

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
