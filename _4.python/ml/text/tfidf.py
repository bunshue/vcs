"""
tfidf

sklearn: TfidfVectorizer 中文处理及一些使用参数

TfidfVectorizer可以把原始文本转化为tf-idf的特征矩阵，从而为后续的文本相似度计算，
主题模型(如LSI)，文本搜索排序等一系列应用奠定基础。

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

import jieba
import sklearn.linear_model
from sklearn.metrics import accuracy_score  # 正解率
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction.text import TfidfVectorizer

document = ["I have a pen.",
            "I have an apple."]

tfidf_model = TfidfVectorizer().fit(document)
sparse_result = tfidf_model.transform(document)     # 得到tf-idf矩阵，稀疏矩阵表示法
print(sparse_result)
# (0, 3)	0.814802474667   # 第0个字符串，对应词典序号为3的词的TFIDF为0.8148
# (0, 2)	0.579738671538
# (1, 2)	0.449436416524
# (1, 1)	0.631667201738
# (1, 0)	0.631667201738

print(sparse_result.todense())                     # 转化为更直观的一般矩阵
# [[ 0.          0.          0.57973867  0.81480247]
#  [ 0.6316672   0.6316672   0.44943642  0.        ]]

print(tfidf_model.vocabulary_)                      # 词语与列的对应关系
# {'have': 2, 'pen': 3, 'an': 0, 'apple': 1}

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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
