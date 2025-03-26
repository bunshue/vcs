"""
PythonMachineLearning20_新進測試

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

import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from matplotlib.colors import ListedColormap

from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# OLS 迴歸

import statsmodels.api as sm     #回歸模型套件
import numpy as np               #資料處理套件
import pandas as pd              #資料處理套件
# 2. 輸入資料。

df0 = pd.read_csv("data/TaipeiAllBus0105.csv")   #輸入資料
print(df0)


df0_X = df0.drop("volumn", axis=1)           #將作為y的變數volunm刪去，並另存為x
df0_X1 = df0_X.drop("transfer01", axis=1)    #之後要做相關係數，而因為transfer01變數為虛擬變數，故不須納入做相關係數，故刪除

df0_y = df0[["volumn"]]      #製作變數y

#4. 相關係數檢驗。

rDf0 = df0_X1.corr()  #查看數據間的相關係數
print(rDf0)


#%matplotlib inline
sns.set(font_scale=1.5)

sns.set_context({"figure.figsize":(8,8)})
sns.heatmap(data = rDf0, square = True, cmap="RdBu_r", annot = True)

show()


import seaborn as sns               #載入分布圖形套件
import matplotlib.pyplot as plt     #載入畫圖套件

sns.pairplot(df0, x_vars=["People","MRTpax", "shift", "kilometer"], y_vars='volumn', size=7, aspect=0.8, kind='reg')  
show()


df0_X = sm.add_constant(df0_X)   #增加模型的常數，使更為符合回歸模型

model0 = sm.OLS(df0_y, df0_X)    #OLS回歸
results0 = model0.fit()

print(results0.summary())

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
