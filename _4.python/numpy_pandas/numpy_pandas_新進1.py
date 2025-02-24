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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import tempfile
import os.path

tmpdir = tempfile.gettempdir()
print(tmpdir)

csv_filename = os.path.join(tmpdir, "users.csv")

print(csv_filename)

# 讀取網頁上的csv檔
url = "https://github.com/duchesnay/pystatsml/raw/master/datasets/salary_table.csv"
salary = pd.read_csv(url)

""" no df users
xls_filename = os.path.join(tmpdir, "users.xlsx")
users.to_excel(xls_filename, sheet_name='users', index=False)

pd.read_excel(xls_filename, sheet_name='users')

# Multiple sheets
with pd.ExcelWriter(xls_filename) as writer:
    users.to_excel(writer, sheet_name='users', index=False)
    df.to_excel(writer, sheet_name='salary', index=False)

pd.read_excel(xls_filename, sheet_name='users')
pd.read_excel(xls_filename, sheet_name='salary')
"""

##############################################################################
# SQL (SQLite)
# ~~~~~~~~~~~~

import sqlite3

db_filename = os.path.join(tmpdir, "users.db")

##############################################################################
# Connect

conn = sqlite3.connect(db_filename)

##############################################################################
# Creating tables with pandas

url = "https://github.com/duchesnay/pystatsml/raw/master/datasets/salary_table.csv"
salary = pd.read_csv(url)

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


##############################################################################
# Exercises
# ---------
# Data Frame
# ~~~~~~~~~~
#
# 1. Read the iris dataset at 'https://github.com/neurospin/pystatsml/tree/master/datasets/iris.csv'
# 2. Print column names
# 3. Get numerical columns
# 4. For each species compute the mean of numerical columns and store it in  a ``stats`` table like:
# ::
#
#           species  sepal_length  sepal_width  petal_length  petal_width
#     0      setosa         5.006        3.428         1.462        0.246
#     1  versicolor         5.936        2.770         4.260        1.326
#     2   virginica         6.588        2.974         5.552        2.026
# Missing data
# ~~~~~~~~~~~~
# Add some missing data to the previous table ``users``:

print("------------------------------------------------------------")  # 60個

"""
Exercises: Pandas: data manipulation
------------------------------------

Data Frame
~~~~~~~~~~
1. Read the iris dataset at 'https://github.com/neurospin/pystatsml/tree/master/datasets/iris.csv'
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
NumPy is an extension to the Python programming language, adding support for large, multi-dimensional (numerical) arrays and matrices, along with a large library of high-level mathematical functions to operate on these arrays.
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
# -------------
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
#
# Shapes of operands A, B and result:
# ::
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

"""
For each column find the row indices of the minimiun value.
"""
[np.argmin(A[:, j]) for j in range(A.shape[1])]

np.argmin(A, axis=0)

"""
Write a function ``scale(A)`` that return an array whose columns are centered and scaled (by std-dev).
"""


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

# 讀取本地檔案 若無 讀取遠端檔案

try:
    salary = pd.read_csv("salary_table.csv")
except:
    url = "https://github.com/duchesnay/pystatsml/raw/master/datasets/salary_table.csv"
    salary = pd.read_csv(url)

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

# 获取当前日期
# datetime模块date类的today()方法获取当前日期
import datetime

print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.today())
print(datetime.date.today().year)
print(datetime.date.today().month)
print(datetime.date.today().day)

# datetime模块datetime类的today()方法获取当前日期和时间
import datetime

print(datetime.datetime.now())
print(datetime.datetime.min)
print(datetime.datetime.max)
print(datetime.datetime.today())
print(datetime.datetime.today().year)
print(datetime.datetime.today().month)
print(datetime.datetime.today().day)
print(datetime.datetime.today().hour)
print(datetime.datetime.today().hour)

# UTC时间
import datetime

# 创建一个时间戳（以秒为单位）
timestamp = 22
# 带UTC时区时间
dt_with_timezone = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)
print("带UTC时区时间:", dt_with_timezone)
# 不带UTC时区时间
dt_without_timezone = datetime.datetime.fromtimestamp(timestamp)
print("不带UTC时区时间", dt_without_timezone)

# 时间戳
import time

print(time.time())
print(time.localtime())  # 获取到当前时间的元组
print(time.mktime(time.localtime()))
# 一周的第几天(周一是0,0-6)、一年的第几天(从1开始，1-366)、夏时令(是夏时令1，不是0，未知-1)。

# 字符串和时间转换
# 利用time模块的strftime()函数可以将时间戳转换成系统时间。
import time

time_str = time.strftime(("%Y-%m-%d %H:%M:%S"), time.localtime())
print(time_str)

# 可以用strptime函数将日期字符串转换为datetime数据类型，
import datetime

print(datetime.datetime.strptime("2022-01-15", "%Y-%m-%d"))

# 可以用Pandas的to_datetime()函数将日期字符串转换为datetime数据类型。
# to_datetime()函数转化后的时间是精准到时分秒精度的
import pandas as pd

print(pd.to_datetime("2022/01/15"))

# 时间差
# 3. 时间运算--时间差
# 利用datetime将时间类型数据进行转换，然后利用减法运算计算时间的不同之处
# 默认输出结果转换为用（“天”，“秒”）表达
import datetime

delta = datetime.datetime(2022, 1, 16) - datetime.datetime(2021, 1, 1, 9, 15)
print(delta)
print(delta.days)
print(delta.seconds)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個
