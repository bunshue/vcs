"""
機器學習_決策樹

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

from common1 import *
import sklearn.linear_model
from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

print("------------------------------------------------------------")  # 60個


def gini_index(groups, classes):
    sumSample = float(sum([len(group) for group in groups])) # 計算分割點的所有樣本
    gini = 0.0                                                                                       # 每組的加權基尼係數
    for group in groups:
        size = float(len(group))
        if size == 0:   # 避免除以零
            continue
        score = 0.0
        # 根據每個班級的分數對該組進行評分
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        gini += (1.0 - score) * (size / sumSample) # 通過相對大小對組得分進行加權
    return gini

# 計算Gini
print(gini_index([[[1, 1], [1, 0]], [[1, 1], [1, 0]]], [0, 1]))
print(gini_index([[[1, 0], [1, 0]], [[1, 1], [1, 1]]], [0, 1]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import tree

X=np.array([[180, 85],[174, 80],[170, 75],
      [167, 45],[158, 52],[155, 44]])
Y = np.array(['man', 'man','man','woman', 'woman',  'woman'])


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
prediction = clf.predict([[173, 76]])
print(prediction)

#繪圖
plt.plot(X[:3,0], X[:3,1], 'yx' )
plt.plot(X[3:,0], X[3:,1], 'g.' )
plt.plot([173], [76], 'r^' )                                                                                       #綠色點
plt.ylabel('W')
plt.xlabel('H')
plt.legend(('man','woman'),  loc='upper left')
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import tree
#from sklearn.externals.six import StringIO
import pydot
from os import system

X=np.array([[180, 85],[174, 80],[170, 75],
      [167, 45],[158, 52],[155, 44]])
Y = np.array(['man', 'man','man','woman', 'woman',  'woman'])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

tree.export_graphviz(clf,out_file='tmp_tree222.dot')

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
