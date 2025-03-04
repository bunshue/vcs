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
'''
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

grid = np.array([[1, 2, 3],
                 [4, 5, 6]])

# concatenate along the first axis
cc = np.concatenate([grid, grid])
print(cc)


# concatenate along the second axis (zero-indexed)
cc = np.concatenate([grid, grid], axis=1)
print(cc)


x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])

# vertically stack the arrays
cc = np.vstack([x, grid])
print(cc)

# horizontally stack the arrays
y = np.array([[99],
              [99]])
cc = np.hstack([grid, y])
print(cc)
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df_11 = pd.DataFrame(np.random.randint(low=2,high=8,size=[3, 4]),
                  columns=list('ABCD'))
print(df_11)

df_11 = np.abs(df_11)
print(df_11)

func_1 = lambda x: x.max() - x.min()
cc = df_11.apply(func_1)
print(cc)

cc = df_11.apply(func_1, axis=1)
print(cc)

func_2 = lambda x: pd.Series([x.min(), x.max()], index=['min', 'max'])
cc = df_11.apply(func_2)
print(cc)

func_3 = lambda x: '%.2f' %x
cc = df_11.applymap(func_3)
print(cc)

cc = df_11['A'].map(func_3)
print(cc)

print(df_11)

df_11.replace(7, "GOOD", inplace=True)
print(df_11)

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
