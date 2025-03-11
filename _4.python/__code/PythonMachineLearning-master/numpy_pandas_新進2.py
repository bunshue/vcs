"""
numpy的使用
pandas的使用

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
import seaborn as sns

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# Correlation and covariance
from numpy.random import randint as ri

A = ri(1, 5, 20)  # 20 random integeres from a small range (1-10)
B = 2 * A + 5 * np.random.randn(20)  # B is twice that of A plus some random noise
print("\nB is twice that of A plus some random noise")
plt.scatter(A, B)  # Scatter plot of B
plt.title("Scatter plot of A vs. B, expect a small positive correlation")
plt.show()
print(np.corrcoef(A, B))  # Correleation coefficient matrix between A and B

A = ri(1, 50, 20)  # 20 random integeres from a larger range (1-50)
B = (
    100 - 2 * A + 10 * np.random.randn(20)
)  # B is 100 minus twice that of A plus some random noise
print("\nB is 100 minus twice that of A plus some random noise")
plt.scatter(A, B)  # Scatter plot of B
plt.title("Scatter plot of A vs. B, expect a large negative correlation")
plt.show()
print("")
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
plt.show()

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

import numpy as np
import time

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
# plt.xscale('log')
# plt.yscale('log')
plt.scatter(n_samples, time_lst_read)
plt.scatter(n_samples, time_npy_read)
plt.legend(["Normal read from CSV", "Read from .npy file"])
plt.show()

print(time_npy_read)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
