"""
decisiontree 决策树

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

"""
决策树

决策树(decision tree)是一种基本的分类与回归方法。在处理分类问题中，其主要优点是模型具有可读性，分类速度快。

决策树模型定义：

分类决策树模型是一种描述对实例进行分类的树形结构。决策树又结点和有向边组成。结点类型包括：内部结点和叶结点。其中内部结点表示一个特征或属性，叶结点表示一个类。

决策树的学习通常包括3个步骤：
第一步：特征选择；
第二步：决策树的生成；
第三步：决策树的修剪。
常用的算法有ID3、 C4.5和CART。
特征选择

特征选择的目的在于选取对训练数据能够分类的特征，即特征选择是决定用哪个特征来划分特征空间。在实际场景中，特征的种类是多种多样的，选择不同的特征会决定产生不同的决策树。那究竟如何选择特征会更好？这里的关键就是确定选择特征的准则。信息增益(information gain)就是这样一种准则。
"""

import numpy as np
import pandas as pd
from math import log

#构建数据
def create_data():
    datasets = [['青年', '否', '否', '一般', '否'],
               ['青年', '否', '否', '好', '否'],
               ['青年', '是', '否', '好', '是'],
               ['青年', '是', '是', '一般', '是'],
               ['青年', '否', '否', '一般', '否'],
               ['中年', '否', '否', '一般', '否'],
               ['中年', '否', '否', '好', '否'],
               ['中年', '是', '是', '好', '是'],
               ['中年', '否', '是', '非常好', '是'],
               ['中年', '否', '是', '非常好', '是'],
               ['老年', '否', '是', '非常好', '是'],
               ['老年', '否', '是', '好', '是'],
               ['老年', '是', '否', '好', '是'],
               ['老年', '是', '否', '非常好', '是'],
               ['老年', '否', '否', '一般', '否'],
               ]
    labels = [u'年龄', u'有工作', u'有自己的房子', u'信贷情况', u'类别']
    # 返回数据集和每个维度的名称
    return datasets, labels

# 获取数据集和标签集
datasets, labels = create_data()
train_data = pd.DataFrame(datasets, columns=labels)
cc = train_data
print(cc)

# 定义熵、经验条件熵、信息增益等

print(labels)

# 熵
def calc_ent(datasets):
    data_length = len(datasets)
    label_count = {}
    for i in range(data_length):
        label = datasets[i][-1]
        if label not in label_count:
            label_count[label] = 0
        label_count[label] += 1
    ent = -sum([(p / data_length) * log(p / data_length, 2)
                for p in label_count.values()])
    return ent

# 经验条件熵
def cond_ent(datasets, axis=0):
    data_length = len(datasets)
    feature_sets = {}
    for i in range(data_length):
        feature = datasets[i][axis]
        if feature not in feature_sets:
            feature_sets[feature] = []
        feature_sets[feature].append(datasets[i])
    cond_ent = sum(
        [(len(p) / data_length) * calc_ent(p) for p in feature_sets.values()])
    return cond_ent


# 信息增益
def info_gain(ent, cond_ent):
    return ent - cond_ent


def info_gain_train(datasets):
    count = len(datasets[0]) - 1
    ent = calc_ent(datasets)
    best_feature = []
    for i in range(count):
        i_info_gain = info_gain(ent, cond_ent(datasets, axis=i))
        best_feature.append((i, i_info_gain))
        print('特征-({}) - info_gain - {:.3f}'.format(labels[i], i_info_gain))
    # 比较大小
    best_ = max(best_feature, key=lambda x: x[-1])
    return '特征-({})的信息增益最大，选择为根节点特征'.format(labels[best_[0]])

info_gain_train(np.array(datasets))

"""
特征-(年龄) - info_gain - 0.083
特征-(有工作) - info_gain - 0.324
特征-(有自己的房子) - info_gain - 0.420
特征-(信贷情况) - info_gain - 0.363

'特征-(有自己的房子)的信息增益最大，选择为根节点特征'
"""


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
