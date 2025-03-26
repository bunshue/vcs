"""
machine_learning_numpy_pandas01

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

print("------------------------------------------------------------")  # 60個


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Correlation and covariance

from numpy.random import randint as ri

"""
A = ri(1,5,20) # 20 random integeres from a small range (1-10)
B = 2*A+5*np.random.randn(20) # B is twice that of A plus some random noise
print("\nB is twice that of A plus some random noise")
plt.scatter(A,B) # Scatter plot of B
plt.title("Scatter plot of A vs. B, expect a small positive correlation")
show()
print(np.corrcoef(A,B)) # Correleation coefficient matrix between A and B

A = ri(1,50,20) # 20 random integeres from a larger range (1-50)
B = 100-2*A+10*np.random.randn(20) # B is 100 minus twice that of A plus some random noise
print("\nB is 100 minus twice that of A plus some random noise")
plt.scatter(A,B) # Scatter plot of B
plt.title("Scatter plot of A vs. B, expect a large negative correlation")
show()
print(np.corrcoef(A,B)) # Correleation coefficient matrix between A and B
"""

# Singular value decomposition (SVD)

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


# Eigenvalues and eigenvectors

A = np.random.randn(9).reshape(3, 3)
print("Original matrix\n", A)
print("\n")
w, v = np.linalg.eig(A)
print("Eigenvalues:\n", w)
print("\n")
print("Eigenvectors:\n", v)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Linear equation solving, matrix inverse, linear least suqare

# 2x + 5y + z = 14;
# 3x - 2y - z = -1;
# x - 3y + z = 4

A = np.array([[2, 5, 1], [3, -2, -1], [1, -3, 1]])
B = np.array([14, -1, 4])
x = np.linalg.solve(A, B)

print("The solutions are:", x)

# The solutions are: [ 2.  1.  5.]

# Linear least squares can be calculated easily as a solution to a linear regression problem **

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
print("------------------------------------------------------------")  # 60個

"""
Selecting/indexing Rows

    Label-based 'loc' method
    Index (numeric) 'iloc' method
"""
from numpy.random import randn as rn

matrix_data = rn(5, 4)
row_labels = ["A", "B", "C", "D", "E"]
column_headings = ["W", "X", "Y", "Z"]

df = pd.DataFrame(data=matrix_data, index=row_labels, columns=column_headings)
print("\nThe data frame looks like\n", "-" * 45, sep="")
print(df)

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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Merging, Joining, Concatenating

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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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

cc = pd.merge(left, right, how="left", on=["key1", "key2"])
print(cc)

cc = pd.merge(left, right, how="right", on=["key1", "key2"])
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Joining

left = pd.DataFrame(
    {"A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]}, index=["K0", "K1", "K2"]
)

right = pd.DataFrame(
    {"C": ["C0", "C2", "C3"], "D": ["D0", "D2", "D3"]}, index=["K0", "K2", "K3"]
)

cc = left.join(right)
print(cc)

cc = left.join(right, how="outer")
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(
    {
        "col1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "col2": [444, 555, 666, 444, 333, 222, 666, 777, 666, 555],
        "col3": "aaa bb c dd eeee fff gg h iii j".split(),
    }
)
print(df)

# Applying functions

# Pandas work with 'apply' method to accept any user-defined function


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
cc = df.head()
print(cc)

cc = df.isnull()
print(cc)

cc = df.fillna("FILL")
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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
print("------------------------------------------------------------")  # 60個

# Pandas built-in Visualization

df1 = pd.read_csv("data/pd_df1.csv", index_col=0)
cc = df1.head()
print(cc)

df2 = pd.read_csv("data/pd_df2.csv")
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
df2.plot.area(alpha=0.4)
show()

# Bar plot (with and without stacking)
df2.plot.bar()
show()

df2.plot.bar(stacked=True)
show()

""" NG
# Lineplot
# Note matplotlib arguments like 'lw' and 'figsize'
df1.plot.line(x=df1.index,y=['B','C'],figsize=(12,4),lw=1)
show()
"""

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

df4 = pd.read_excel("data/Height_Weight.xlsx")
print(df4)

cc = df4["Height"] > 155
print(cc)

cc = df4[df4["Height"] > 155]
print(cc)

cc = df4[(df4["Height"] > 155) & (df4["Weight"] < 140)]
print(cc)


df4["BMI"] = df4["Weight"] * 0.453592 / (df4["Height"] / 100) ** 2
print(df4)

cc = df4.sort_values(by="BMI")
print(cc)


# Use inplace=True to make the changes reflected on the original DataFrame

print(df4)


df4.sort_values(by="BMI", inplace=True)
print(df4)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 速度比較

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

# Save as a .npy file and read
np.save("tmp_fnumpy.npy", array_lst)


t1 = time.time()
array_reloaded = np.load("tmp_fnumpy.npy")
t2 = time.time()
print(array_reloaded)
print("\nShape: ", array_reloaded.shape)
print(f"Time took to load: {t2-t1} seconds.")


t1 = time.time()
array_reloaded = np.load("tmp_fnumpy.npy").reshape(10000, 100)
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

    np.save("tmp_fnumpy.npy", array_lst)

    t1 = time.time()
    array_reloaded = np.load("tmp_fnumpy.npy")
    t2 = time.time()
    time_npy_read.append(1000 * (t2 - t1))
    print("Array shape:", array_reloaded.shape)

    print(f"Processing done for {sample_size} samples\n")

plt.figure(figsize=(8, 5))
# plt.xscale('log')
# plt.yscale('log')
plt.scatter(n_samples, time_lst_read)
plt.scatter(n_samples, time_npy_read)
plt.legend(["Normal read from CSV", "Read from .npy file"])
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_excel("data/Sample - Superstore.xls")

df.drop("Row ID", axis=1, inplace=True)

print(df.shape)

df_subset = df.loc[
    [i for i in range(5, 10)],
    ["Customer ID", "Customer Name", "City", "Postal Code", "Sales"],
]
print(df_subset)

df_subset = df.loc[[i for i in range(100, 200)], ["Sales", "Profit"]]
cc = df_subset.describe()
print(cc)

df_subset.plot.box()
plt.title("Boxplot of sales and profit", fontsize=15)
plt.ylim(0, 500)
plt.grid(True)
show()

cc = df["State"].unique()
print(cc)

cc = df["State"].nunique()
print(cc)

cc = df["Country"].unique()
print(cc)

cc = df.drop("Country", axis=1, inplace=True)
print(cc)

df_subset = df.loc[[i for i in range(10)], ["Ship Mode", "State", "Sales"]]
print(df_subset)

# df_subset>100

# df_subset[df_subset>100]

df_subset[df_subset["Sales"] > 100]

df_subset[(df_subset["State"] != "California") & (df_subset["Sales"] > 100)]

matrix_data = np.matrix("22,66,140;42,70,148;30,62,125;35,68,160;25,62,152")
row_labels = ["A", "B", "C", "D", "E"]
column_headings = ["Age", "Height", "Weight"]

df1 = pd.DataFrame(data=matrix_data, index=row_labels, columns=column_headings)
print("\nThe DataFrame\n", "-" * 25, sep="")
print(df1)
print("\nAfter resetting index\n", "-" * 35, sep="")
print(df1.reset_index())
print("\nAfter resetting index with 'drop' option TRUE\n", "-" * 45, sep="")
print(df1.reset_index(drop=True))
print("\nAdding a new column 'Profession'\n", "-" * 45, sep="")
df1["Profession"] = "Student Teacher Engineer Doctor Nurse".split()
print(df1)
print("\nSetting 'Profession' column as index\n", "-" * 45, sep="")
print(df1.set_index("Profession"))

# GroupBy method

df_subset = df.loc[[i for i in range(10)], ["Ship Mode", "State", "Sales"]]
df_subset

byState = df_subset.groupby("State")

byState

print("\nGrouping by 'State' column and listing mean sales\n", "-" * 50, sep="")
# print(byState.mean())

print("\nGrouping by 'State' column and listing total sum of sales\n", "-" * 50, sep="")
print(byState.sum())

print(pd.DataFrame(df_subset.groupby("State").describe().loc["California"]).transpose())

df_subset.groupby("Ship Mode").describe().loc[["Second Class", "Standard Class"]]

pd.DataFrame(byState.describe().loc["California"])

byStateCity = df.groupby(["State", "City"])

byStateCity.describe()["Sales"]

# Missing values in Pandas

df_missing = pd.read_excel("data/Sample - Superstore.xls", sheet_name="Missing")

df_missing

df_missing.isnull()

for c in df_missing.columns:
    miss = df_missing[c].isnull().sum()
    if miss > 0:
        print("{} has {} missing value(s)".format(c, miss))
    else:
        print("{} has NO missing value!".format(c))

# Filling missing values with fillna()

df_missing.fillna("FILL")

df_missing[["Customer", "Product"]].fillna("FILL")

# NG df_missing['Sales'].fillna(method='ffill')

# NG df_missing['Sales'].fillna(method='bfill')

# NG df_missing['Sales'].fillna(df_missing.mean()['Sales'])

# Dropping missing values with dropna()

df_missing.dropna(axis=0)

df_missing.dropna(axis=1)

df_missing.dropna(axis=1, thresh=10)

# Outlier detection using simple statistical test

df_sample = df[["Customer Name", "State", "Sales", "Profit"]].sample(n=50).copy()

# Assign a wrong (negative value) in few places
df_sample["Sales"].iloc[5] = -1000.0
df_sample["Sales"].iloc[15] = -500.0

df_sample.plot.box()
plt.title("Boxplot of sales and profit", fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.grid(True)
show()

# Concatenation

df_1 = df[["Customer Name", "State", "Sales", "Profit"]].sample(n=4)
df_2 = df[["Customer Name", "State", "Sales", "Profit"]].sample(n=4)
df_3 = df[["Customer Name", "State", "Sales", "Profit"]].sample(n=4)

df_1

df_2

df_3

df_cat1 = pd.concat([df_1, df_2, df_3], axis=0)
df_cat1

df_cat2 = pd.concat([df_1, df_2, df_3], axis=1)
df_cat2

# Merging by a common key

df_1 = df[["Customer Name", "Ship Date", "Ship Mode"]][0:4]
df_1


df_2 = df[["Customer Name", "Product Name", "Quantity"]][0:4]
df_2

pd.merge(df_1, df_2, on="Customer Name", how="inner")

pd.merge(df_1, df_2, on="Customer Name", how="inner").drop_duplicates()

df_3 = df[["Customer Name", "Product Name", "Quantity"]][2:6]
df_3


pd.merge(df_1, df_3, on="Customer Name", how="inner").drop_duplicates()


pd.merge(df_1, df_3, on="Customer Name", how="outer").drop_duplicates()


# Join method

df_1 = df[["Customer Name", "Ship Date", "Ship Mode"]][0:4]
df_1.set_index(["Customer Name"], inplace=True)
df_1

df_2 = df[["Customer Name", "Product Name", "Quantity"]][2:6]
df_2.set_index(["Customer Name"], inplace=True)
df_2

df_1.join(df_2, how="left").drop_duplicates()

df_1.join(df_2, how="right").drop_duplicates()

df_1.join(df_2, how="inner").drop_duplicates()

df_1.join(df_2, how="outer").drop_duplicates()

# Miscelleneous useful methods

# Randomized sampling - sample method

df.sample(n=5)

df.sample(frac=0.001)

df.sample(frac=0.001, replace=True)

# Pandas value_count method to return unique records

df["Customer Name"].value_counts()[:10]

# Pivot table functionality - pivot_table

df_sample = df.sample(n=100)

df_sample.pivot_table(
    values=["Sales", "Quantity", "Profit"], index=["Region", "State"], aggfunc="mean"
)

# Sorting by particular column

df_sample = df[["Customer Name", "State", "Sales", "Quantity"]].sample(n=15)
df_sample

df_sample.sort_values(by="Sales")

df_sample.sort_values(by=["State", "Sales"])

# Flexibility for user-defined function with apply method


def categorize_sales(price):
    if price < 50:
        return "Low"
    elif price < 200:
        return "Medium"
    else:
        return "High"


df_sample = df[["Customer Name", "State", "Sales"]].sample(n=100)
df_sample.head(10)

df_sample["Sales Price Category"] = df_sample["Sales"].apply(categorize_sales)
df_sample.head(10)

df_sample["Customer Name Length"] = df_sample["Customer Name"].apply(len)
df_sample.head(10)

df_sample["Discounted Price"] = df_sample["Sales"].apply(
    lambda x: 0.85 * x if x > 200 else x
)
df_sample.head(10)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# How fast are NumPy operations compared to regular Python math?

from math import log10 as lg10

N = 1000000  # Number of records to process
speed = []  # Empty list to store operation speeds (time taken)

# Create a list of 1 million numbers

l1 = list(100 * (np.random.random(N)) + 1)
print("Length of l1:", len(l1))

print("First few elements of the array:", l1[:4])

# Create a NumPy ndarray object from that list i.e. vectorize it

a1 = np.array(l1)

print("Shape of a1 object:", a1.shape)
print("Type of a1 object:", type(a1))

# Create a blank list for appending elements

l2 = []  # Just a blanck list to append to

# How fast is - For loop and appending

t1 = time.time()
for item in l1:
    l2.append(lg10(item))
t2 = time.time()
print("With for loop and appending it took {} seconds".format(t2 - t1))
speed.append(t2 - t1)

# With for loop and appending it took 0.3542044162750244 seconds

print("First few elements of the resulting array:", l2[:4])

# How fast it - List comprehension

t1 = time.time()
l2 = [lg10(i) for i in range(1, 1000001)]
t2 = time.time()
print("With list comprehension, it took {} seconds".format(t2 - t1))
speed.append(t2 - t1)

# With list comprehension, it took 0.16927814483642578 seconds

print("First few elements of the resulting array:", l2[:4])

# How fast is - Map function method


def op1(x):
    return lg10(x)


t1 = time.time()
l2 = list(map(op1, l1))
t2 = time.time()
print("With map functional method it took {} seconds".format(t2 - t1))
speed.append(t2 - t1)

# With map functional method it took 0.2851881980895996 seconds

print("First few elements of the resulting array:", l2[:4])

# First few elements of the resulting array: [1.4892398404100269, 0.6115145218774171, 1.8453449275438665, 1.9578573118312546]

# How fast is - NumPy operation (vectorized array)

t1 = time.time()
a2 = np.log10(a1)
t2 = time.time()
print("With direct NumPy log10 method it took {} seconds".format(t2 - t1))
speed.append(t2 - t1)

# With direct NumPy log10 method it took 0.0312502384185791 seconds

l3 = list(a2)
print("First few elements of the resulting array:", l3[:4])

# First few elements of the resulting array: [1.4892398404100269, 0.61151452187741706, 1.8453449275438665, 1.9578573118312546]

# Plot the time taken by each operation

plt.figure(figsize=(10, 6))
plt.ylabel("Time taken to process 1 million records in seconds", fontsize=12)
plt.xlabel("Various types of operations", fontsize=14)
plt.grid(True)
plt.bar(
    x=[1, 2, 3, 4],
    height=speed,
    align="center",
    tick_label=["For-loop", "List comprehension", "Map function", "NumPy"],
)
show()

# Therefore, we see the evidence that NumPy operations over ndarray objects are much faster than regular Python math operations over corresponding list. The exact speed of regular Python operations vary a little but they are always much slower compared to the vectorized NumPy operation.

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Basics of Matplotlib and Seaborn - data visualization with Python
"""
    scatterplot,
    boxplot,
    histogram,
    violin plot,
    bar charts,
    heatmap
    time series line plot
"""

people = [
    "Ann",
    "Brandon",
    "Chen",
    "David",
    "Emily",
    "Farook",
    "Gagan",
    "Hamish",
    "Imran",
    "Julio",
    "Katherine",
    "Lily",
]
age = [21, 12, 32, 45, 37, 18, 28, 52, 5, 40, 48, 15]
weight = [55, 35, 77, 68, 70, 60, 72, 69, 18, 65, 82, 48]
height = [160, 135, 170, 165, 173, 168, 175, 159, 105, 171, 155, 158]

plt.scatter(age, height)
show()

# Set figure size
plt.figure(figsize=(8, 6))

# Add a main title
plt.title("Plot of Age vs. Height (in cms)\n", fontsize=20, fontstyle="italic")

# X- and Y-label with fontsize
plt.xlabel("Age (years)", fontsize=16)
plt.ylabel("Height (cms)", fontsize=16)

# Turn on grid
plt.grid(True)

# Set Y-axis limit
plt.ylim(100, 200)

# X- and Y-axis ticks customization with fontsize and placement
plt.xticks([i * 5 for i in range(12)], fontsize=15)
plt.yticks(fontsize=15)

# Main plotting function with choice of color, marker size, and marker edge color
plt.scatter(x=age, y=height, c="orange", s=150, edgecolors="k")

# Adding bit of text to the plot
plt.text(
    x=15,
    y=105,
    s="Height increaes up to around \n20 years and then tapers off",
    fontsize=15,
    rotation=30,
    linespacing=2,
)
plt.text(x=22, y=185, s="Nobody has a height beyond 180 cm", fontsize=15)

# Adding a vertical line
plt.vlines(x=20, ymin=100, ymax=180, linestyles="dashed", color="blue", lw=3)

# Adding a horizontal line
plt.hlines(y=180, xmin=0, xmax=55, linestyles="dashed", color="red", lw=3)

# Adding a legend
plt.legend(["Height in cms"], loc=2, fontsize=14)

# Final show method
show()

# Bar chart

plt.figure(figsize=(12, 4))
plt.title("People's weight in kgs", fontsize=16, fontstyle="italic")
# Main plot function 'bar'
plt.bar(x=people, height=weight, width=0.6, color="orange", edgecolor="k", alpha=0.6)
plt.xlabel("People", fontsize=15)
plt.xticks(fontsize=14, rotation=30)
plt.yticks(fontsize=14)
plt.ylabel("Weight (in kgs)", fontsize=15)
show()

# Histogram

plt.figure(figsize=(7, 5))
# Main plot function 'hist'
plt.hist(weight, color="red", edgecolor="k", alpha=0.75, bins=5)
plt.title("Histogram of patient weight", fontsize=18)
plt.xlabel("Weight in kgs", fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
show()

# Simple line plot

days = np.arange(1, 31)
candidate_A = 50 + days * 0.07 + 2 * np.random.randn(30)
candidate_B = 50 - days * 0.1 + 3 * np.random.randn(30)

# Determine the minimum and maximum of stock prices
ymin = min(candidate_A.min(), candidate_B.min())
ymax = max(candidate_A.max(), candidate_B.max())

# Set style
plt.style.use("fivethirtyeight")

plt.figure(figsize=(12, 5))
plt.title(
    "Time series plot of poll percentage over a month\n",
    fontsize=20,
    fontstyle="italic",
)
plt.xlabel("Days", fontsize=16)
plt.ylabel("Poll percentage (%)", fontsize=16)
plt.grid(True)
plt.ylim(ymin * 0.98, ymax * 1.02)
plt.xticks([i * 2 for i in range(16)], fontsize=14)
plt.yticks(fontsize=15)

# Main plotting function - plot (note markersize, lw (linewidth) arguments)
plt.plot(days, candidate_A, "o-", markersize=10, c="blue", lw=2)
plt.plot(days, candidate_B, "^-", markersize=10, c="green", lw=2)

plt.legend(
    ["Poll percentage of candidate A (%)", "Poll percentage of candidate B (%)"],
    loc=2,
    fontsize=14,
)
show()

# Boxplot

plt.style.use("ggplot")
# Note how to convert default numerical x-axis ticks to the list of string by passing two lists
plt.boxplot(x=[candidate_A, candidate_B], showmeans=True)
plt.grid(True)
plt.xticks([1, 2], ["Candidate A", "Candidate B"])
# plt.yticks(fontsize=15)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Pandas DataFrames support some visualizations directly!

df = pd.read_csv("data/wine.data.csv")

cc = df.head()
print(cc)

# Just to set the Matplotlib style to default
import matplotlib as mpl

mpl.rcParams.update(mpl.rcParamsDefault)

# Scatter plot

df.plot.scatter("Alcohol", "Color intensity")
show()

# Histogram

df["Alcohol"].plot.hist(bins=20, figsize=(5, 5), edgecolor="k")
plt.xlabel("Alcohol percentage")
show()

# Seaborn - advanced statistical visualizations

# Boxplot separated by class/groups of data

sns.boxplot(x="Class", y="Alcohol", data=df)
show()

# Violin plots (combination of boxplot and histogram/kernel density)

sns.violinplot(x="Class", y="Alcohol", data=df)
show()

# regplot - computes and plots the linear regression fit along with confidence interval

sns.regplot(x="Alcohol", y="Color intensity", data=df)
show()

# lmplot - combination of regplot with grid to visualize across various groups/classes

sns.lmplot(x="Alcohol", y="Color intensity", hue="Class", data=df)
show()

# Correlation matrix and heatmap

corr_mat = np.corrcoef(df, rowvar=False)

corr_mat.shape

# (14, 14)

corr_df = pd.DataFrame(corr_mat, columns=df.columns, index=df.columns)

print(np.round(corr_mat, 3))

sns.heatmap(corr_df, linewidth=1, cmap="plasma")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Iteration with Pandas

from time import time

np.random.seed(101)
df = pd.DataFrame(
    np.random.randint(0, 100, size=(100000, 4)), columns=list("ABCD"), dtype=np.int16
)
df.head()

df.info(memory_usage="deep")

df.describe()

# Most inefficient for loop

count = 0
t1 = time()
for i in range(len(df)):
    if df.iloc[i]["A"] + df.iloc[i]["B"] > df.iloc[i]["C"] + df.iloc[i]["D"]:
        count += 1
t2 = time()
delt1 = round((t2 - t1), 2)
print(f"Time:{delt1} seconds")
print("Count:", count)

# Time:32.22 seconds
# Count: 49769

# Comparing iterrows() and df.values - 1

count = 0
t1 = time()
for idx, row in df.iterrows():
    if row["A"] + row["B"] > (row["C"] + row["D"]):
        count += 1
t2 = time()
delt1 = round((t2 - t1), 2)
print(f"Time:{delt1} seconds")
print("Count:", count)

# Time:6.91 seconds
# Count: 49769

count = 0
t1 = time()
for row in df.values:
    if row[0] + row[1] > (row[2] + row[3]):
        count += 1
t2 = time()
delt2 = round((t2 - t1), 3)
print(f"Time:{delt2} seconds")
print("Count:", count)

# Time:0.112 seconds
# Count: 49769

print(f"df.values is {round(delt1/delt2,2)} times faster")

# df.values is 61.7 times faster

# Comparing iterrows() and df.values - 2

count = 0
t1 = time()
for idx, row in df.iterrows():
    if row["A"] + row["B"] > 1.25 * (row["C"] + row["D"]):
        count += 1
t2 = time()
delt1 = round((t2 - t1), 2)
print(f"Time:{delt1} seconds")
print("Count:", count)

# Time:8.05 seconds
# Count: 35886

count = 0
t1 = time()
for row in df.values:
    if row[0] + row[1] > 1.25 * (row[2] + row[3]):
        count += 1
t2 = time()
delt2 = round((t2 - t1), 3)
print(f"Time:{delt2} seconds")
print("Count:", count)

# Time:0.546 seconds
# Count: 35886

print(f"df.values is {round(delt1/delt2,2)} times faster")

# df.values is 14.74 times faster

# Comparing iterrows() and df.values - 3

count = 0
t1 = time()
for idx, row in df.iterrows():
    if np.log(1 + row["A"] + row["B"]) > np.sqrt(0.5 * (row["C"] + row["D"])):
        count += 1
t2 = time()
delt1 = round((t2 - t1), 2)
print(f"Time:{delt1} seconds")
print("Count:", count)

# Time:8.76 seconds
# Count: 9202

count = 0
t1 = time()
for row in df.values:
    if np.log(1 + row[0] + row[1]) > np.sqrt(0.5 * (row[2] + row[3])):
        count += 1
t2 = time()
delt2 = round((t2 - t1), 3)
print(f"Time:{delt2} seconds")
print("Count:", count)

# Time:0.962 seconds
# Count: 9202

print(f"df.values is {round(delt1/delt2,2)} times faster")

# df.values is 9.11 times faster

# Simple vectorized operation is fastest in this counting example

t1 = time()
df["result"] = np.log(1 + df["A"] + df["B"]) > np.sqrt(0.5 * (df["C"] + df["D"]))
t2 = time()
delt3 = round((t2 - t1), 3)
print(f"Time:{delt3} seconds")
print("Count:", df["result"].sum())

# Time:0.01 seconds
# Count: 9202

# String identifier


def identifier():
    # Generates random identifier string of 5 characters
    letters = list("CFJQZ")
    numbers = list("123456789")

    random_id = ""
    random_id += np.random.choice(letters)
    random_id += np.random.choice(letters)
    random_id += np.random.choice(numbers)
    random_id += np.random.choice(numbers)
    # random_id+=np.random.choice(numbers)
    # random_id+=np.random.choice(numbers)
    # random_id+=np.random.choice(letters)
    random_id += np.random.choice(letters)

    return random_id


for i in range(10):
    print(identifier())


df.head()

id_lst = []
for i in range(100000):
    id_lst.append(identifier())
id_lst = np.array(id_lst)

df.insert(0, "ID", id_lst)

df.sample(5)

df["ID"].nunique()

# 10125

ratio_dict = {"ID": [], "Ratio": []}
t1 = time()
for _, row in df.iterrows():
    if row["ID"][0:2] == "ZZ" and row["ID"][-1] == "F":
        ratio = (row["A"] + row["B"]) / (0.01 + row["C"] + row["D"])
        ratio_dict["ID"].append(row[0])
        ratio_dict["Ratio"].append(ratio)
t2 = time()
delt4 = round((t2 - t1), 3)
print(f"Time:{delt4} seconds")

# Time:6.597 seconds

ratio_dict = {"ID": [], "Ratio": []}
t1 = time()
for row in df.values:
    if row[0][0:2] == "ZZ" and row[0][-1] == "F":
        ratio = (row[1] + row[2]) / (0.01 + row[3] + row[4])
        ratio_dict["ID"].append(row[0])
        ratio_dict["Ratio"].append(ratio)
t2 = time()
delt4 = round((t2 - t1), 3)
print(f"Time:{delt4} seconds")

# Time:0.056 seconds

pd.DataFrame(ratio_dict)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Example of pipelining with Pandas with pdpipe

import pdpipe as pdp

df = pd.read_csv("data/USA_Housing.csv")

round(df.sample(5), 2)

df.shape

df.columns

round(df.describe().T, 2)


def size(n):
    if n <= 4:
        return "Small"
    elif 4 < n <= 6:
        return "Medium"
    else:
        return "Big"


df["House_size"] = df["Avg. Area Number of Rooms"].apply(size)

df["House_size"] = df["Avg. Area Number of Rooms"].apply(size)

round(df.sample(5), 2)

# Drop a column

drop_age = pdp.ColDrop("Avg. Area House Age")

df2 = drop_age(df)

round(df2.sample(5))

# Chaining stages by adding them up

pipeline = pdp.ColDrop("Avg. Area House Age")
pipeline += pdp.OneHotEncode("House_size")

df3 = pipeline(df)

round(df3.sample(5))


def price_tag(x):
    if x > 250000:
        return "keep"
    else:
        return "drop"


pipeline = pdp.ColDrop("Avg. Area House Age")
pipeline += pdp.OneHotEncode("House_size")
pipeline += pdp.ApplyByCols("Price", price_tag, "Price_tag", drop=False)

df4 = pipeline(df)

df4.shape

round(df4.sample(5), 2)

pipeline = pdp.ColDrop("Avg. Area House Age")
pipeline += pdp.OneHotEncode("House_size")
pipeline += pdp.ApplyByCols("Price", price_tag, "Price_tag", drop=False)
pipeline += pdp.ValDrop(["drop"], "Price_tag")
pipeline += pdp.ColDrop("Price_tag")

df5 = pipeline(df)

df5.shape

# Scikit-learn scaling

pipeline_scale = pdp.Scale(
    "StandardScaler", exclude_columns=["House_size_Medium", "House_size_Small"]
)

df6 = pipeline_scale(df5)

round(df6.sample(5), 3)

# NLTK stages

pipeline_tokenize = pdp.TokenizeWords("Address")

df7 = pipeline_tokenize(df6)

df7.sample(5)


def extract_state(token):
    return str(token[-2])


pipeline_state = pdp.ApplyByCols("Address", extract_state, result_columns="State")

df8 = pipeline_state(df7)

round(df8.sample(5), 3)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Speeding up Numpy and Pandas using numexpr and pd.eval

import numexpr as ne

a = np.arange(1e6)
b = np.arange(1e6)

c = a + 1

# 3.55 ms ± 52.1 µs per loop (mean ± std. dev. of 10 runs, 200 loops each)

c = ne.evaluate("a + 1")

# 1.94 ms ± 86.5 µs per loop (mean ± std. dev. of 10 runs, 200 loops each)

# Arithmatic operation involving two arrays

c = 2 * a + 3 * b

# 11.7 ms ± 177 µs per loop (mean ± std. dev. of 10 runs, 100 loops each)

c = ne.evaluate("2*a+3*b")

# 2.14 ms ± 130 µs per loop (mean ± std. dev. of 10 runs, 100 loops each)

# More complicated operation involving more arrays

a = np.random.normal(size=(1000000, 5))
a1, a2, a3, a4, a5 = a[:, 0], a[:, 1], a[:, 2], a[:, 3], a[:, 4]

c = (a1**2 + 2 * a2 + (3 / a3)) / (np.sqrt(a4**2 + a5**2))

# 47 ms ± 220 µs per loop (mean ± std. dev. of 10 runs, 100 loops each)

ne.evaluate("(a1**2+2*a2+(3/a3))/(sqrt(a4**2+a5**2))")

# 3.96 ms ± 218 µs per loop (mean ± std. dev. of 10 runs, 100 loops each)

# Expression involving a conditional (boolean filtering)

x1 = np.random.random(1000000)
x2 = np.random.random(1000000)
y1 = np.random.random(1000000)
y2 = np.random.random(1000000)

c = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) > 0.5

# 23.2 ms ± 143 µs per loop (mean ± std. dev. of 10 runs, 100 loops each)

c = ne.evaluate("sqrt((x1-x2)**2+(y1-y2)**2) > 0.5")

# 1.86 ms ± 112 µs per loop (mean ± std. dev. of 10 runs, 100 loops each)

# NG c = ne.evaluate("2*a+3*b > 3.5",optimization='moderate')

# 763 µs ± 85.4 µs per loop (mean ± std. dev. of 10 runs, 100 loops each)

# Expression involving complex numbers

a = np.random.random(1000000)
b = np.random.random(1000000)

cplx = a + b * 1j

c = np.log10(cplx)

# 55.9 ms ± 159 µs per loop (mean ± std. dev. of 10 runs, 100 loops each)

c = ne.evaluate("log10(cplx)")

# 9.9 ms ± 117 µs per loop (mean ± std. dev. of 10 runs, 100 loops each)

# How the array size impacts the speed improvement

from time import time

result_np = {"Size": [], "Time": []}
for i in [int(10 ** (j / 5)) for j in range(25, 40)]:
    a = np.random.random(size=i)
    b = np.random.random(size=i)
    times = [0] * 10
    for j in range(10):
        t1 = time()
        c = 2 * a + 3 * b > 3.5
        t2 = time()
        times[j] = (t2 - t1) * 1000
    times = np.array(times)
    result_np["Size"].append(i)
    result_np["Time"].append(times.mean())

result_ne = {"Size": [], "Time": []}
for i in [int(10 ** (j / 5)) for j in range(25, 40)]:
    a = np.random.random(size=i)
    b = np.random.random(size=i)
    times = [0] * 10
    for j in range(10):
        t1 = time()
        c = ne.evaluate("2*a+3*b > 3.5")
        t2 = time()
        times[j] = (t2 - t1) * 1000
    times = np.array(times)
    result_ne["Size"].append(i)
    result_ne["Time"].append(times.mean())


def speed_benchmark(result1, result2, leg_text):
    """
    Plots timing results
    """
    plt.semilogx(result1["Size"], result1["Time"], c="blue", marker="o")
    plt.semilogx(result2["Size"], result2["Time"], c="k", marker="^")
    plt.grid(True)
    plt.legend(leg_text, fontsize=14)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.xlabel("Number of elements in the array", fontsize=15)
    plt.ylabel("Time (milliseconds)", fontsize=15)
    plt.show()


speed_benchmark(result_np, result_ne, leg_text=["Just NumPy", "With numexpr"])

# Pandas pd.eval

nrows, ncols = 50000, 100

df1, df2, df3, df4 = [pd.DataFrame(np.random.randn(nrows, ncols)) for _ in range(4)]

c = 2 * df1 - (df2 / 2) + (df3 / df4)

# 55.8 ms ± 1.8 ms per loop (mean ± std. dev. of 10 runs, 20 loops each)

pd.eval("2*df1 - (df2/2) + (df3/df4)")

# 17.3 ms ± 539 µs per loop (mean ± std. dev. of 10 runs, 20 loops each)

# How the DataFrame size impacts the speed

ncols = 100
result_no_eval = {"Size": [], "Time": []}
for i in [int(10 ** (j / 5)) for j in range(15, 32)]:
    df1, df2, df3, df4 = [pd.DataFrame(np.random.randn(i, ncols)) for _ in range(4)]
    times = [0] * 10
    for j in range(10):
        t1 = time()
        c = df1 + df2 + df3 + df4
        t2 = time()
        times[j] = (t2 - t1) * 1000
    times = np.array(times)
    result_no_eval["Size"].append(i)
    result_no_eval["Time"].append(times.mean())

ncols = 100
result_eval = {"Size": [], "Time": []}
for i in [int(10 ** (j / 5)) for j in range(15, 32)]:
    df1, df2, df3, df4 = [pd.DataFrame(np.random.randn(i, ncols)) for _ in range(4)]
    times = [0] * 10
    for j in range(10):
        t1 = time()
        c = ne.evaluate("df1+df2+df3+df4")
        t2 = time()
        times[j] = (t2 - t1) * 1000
    times = np.array(times)
    result_eval["Size"].append(i)
    result_eval["Time"].append(times.mean())


def speed_benchmark_pd(result1, result2, leg_text):
    """
    Plots timing results
    """
    plt.semilogx(result1["Size"], result1["Time"], c="blue", marker="o")
    plt.semilogx(result2["Size"], result2["Time"], c="k", marker="^")
    plt.grid(True)
    plt.legend(leg_text, fontsize=14)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.xlabel("Number of rows in the DataFrame", fontsize=15)
    plt.ylabel("Time (milliseconds)", fontsize=15)
    plt.show()


speed_benchmark_pd(
    result_no_eval, result_eval, leg_text=["Normal boring Pandas", "With pd.eval"]
)


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
