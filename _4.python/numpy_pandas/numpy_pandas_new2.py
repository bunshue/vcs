"""
numpy的使用

numpy: 數值計算的標準套件
"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import time
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

# DataFrame 是二維數組對象
df = pd.DataFrame(np.random.randn(6,4), columns=list('ABCD'))
print(df)

print(df.iloc[0])

print('顯示A欄')
print(df.A)

print("Row data type: {}".format(type(df.iloc[0])))
print("Column data type: {}".format(type(df.A)))

print('df之大小')
print(df.shape)

print('df之內容')
print(df)

print('df之頭3行')
print(df.head(3))

print('df之尾2行')
print(df.tail(2))

print('顯示df之欄')
print(df.columns)
print('顯示df之index')
print(df.index)
print('顯示df之describe')
print(df.describe())

print('排序')
print(df.sort_index(axis=1, ascending=False))

print('依B欄排序')
print(df.sort_values(by='B'))

print('顯示df之3:5')
print(df[3:5])

print('顯示df之A B D欄')
print(df[['A', 'B', 'D']])

print('顯示')
print(df.loc[3, 'A'])

print('顯示')
print(df.iloc[3, 0])

print('顯示')
print(df.iloc[2:5, 0:2])

print('顯示')
print(df[df.C > 0])

print('加入TAG')
df["TAG"] = ["cat", "dog", "cat", "cat", "cat", "dog"]
print(df)

print(df.groupby('TAG').sum())

print('顯示')
n_items = 366
ts = pd.Series(np.random.randn(n_items), index=pd.date_range('20000101', periods=n_items))

print('顯示ts大小')
print(ts.shape)

print('顯示ts頭5項')
print(ts.head(5))

print('顯示')
print(ts.resample("1m").sum())

plt.figure(figsize=(10, 6))
cs = ts.cumsum()
cs.plot()
plt.show()

plt.figure(figsize=(10, 6))
ts.resample("1m").sum().plot.bar()
plt.show()

df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))
df.to_csv('tmp_data.csv')

df = pd.read_csv('tmp_data.csv', index_col=0)
print(df.shape)
print(df.head(5))

print("------------------------------------------------------------")  # 60個
