'''
#pandas製作資料 修改資料 用matplotlib顯示

'''

import os
import sys
import time
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

# 使用 NumPy 生成随机数
random_data = np.random.normal(170, 10, 250)

# 将数据转换为 Pandas DataFrame
dataframe = pd.DataFrame(random_data)

# 使用 Pandas hist() 方法绘制直方图
dataframe.hist()

# 设置图表属性
plt.title("RUNOOB hist() Test")
plt.xlabel("X-Value")
plt.ylabel("Y-Value")

plt.show()

print("------------------------------------------------------------")  # 60個

# 生成随机数据
data = pd.Series(np.random.normal(size=100))

data.hist()

# 设置图形标题和坐标轴标签
plt.title("RUNOOB hist() Tes")
plt.xlabel("X-Values")
plt.ylabel("Y-Values")

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


