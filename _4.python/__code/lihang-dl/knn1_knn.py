"""
ml01_knn

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

import math
from itertools import combinations


def Distance(x, y, p=2):
    if len(x) == len(y) and len(x) > 1:
        sum = 0
        for i in range(len(x)):
            sum += math.pow(abs(x[i] - y[i]), p)
        return math.pow(sum, 1 / p)
    else:
        return 0


# 二维空间的三个点坐标
x1 = [1, 1]
x2 = [5, 1]
x3 = [4, 4]

for i in range(1, 5):
    r = {"p={} x1=[1,1],x2={}".format(i, x2): Distance(x1, x2, p=i)}
    print(min(zip(r.keys(), r.values())))

for i in range(1, 5):
    r = {"p={} x1=[1,1],x3={}".format(i, c): Distance(x1, c, p=i) for c in [x3]}
    print(min(zip(r.keys(), r.values())))

# 对iris花瓣数据分类 python实现

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from collections import Counter

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["label"] = iris.target
# 构建数据列名
df.columns = ["sepal length", "sepal width", "petal length", "petal width", "label"]

# 展示部分数据(展示10条记录)，截取部分记录 df[start:end]
cc = df[0:10]
print(cc)


# 以花萼长度和宽度构架二维数据并展示
plt.scatter(df[:50]["sepal length"], df[:50]["sepal width"], label="0")
plt.scatter(df[50:100]["sepal length"], df[50:100]["sepal width"], label="1")
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.legend()
show()

# 2.定义KNN


class KNN:
    def __init__(self, X_train, y_train, n_neighbors=3, p=2):
        """
        parameter: n_neighbors 临近点个数
        parameter: p 距离度量
        """
        self.n = n_neighbors
        self.p = p
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X):
        # 取出n个点
        knn_list = []
        for i in range(self.n):
            dist = np.linalg.norm(X - self.X_train[i], ord=self.p)
            knn_list.append((dist, self.y_train[i]))

        for i in range(self.n, len(self.X_train)):
            max_index = knn_list.index(max(knn_list, key=lambda x: x[0]))
            dist = np.linalg.norm(X - self.X_train[i], ord=self.p)
            if knn_list[max_index][0] > dist:
                knn_list[max_index] = (dist, self.y_train[i])

        # 统计
        knn = [k[-1] for k in knn_list]
        count_pairs = Counter(knn)
        max_count = sorted(count_pairs, key=lambda x: x)[-1]
        return max_count

    def score(self, X_test, y_test):
        # 投票得分
        right_count = 0
        n = 10
        for X, y in zip(X_test, y_test):
            label = self.predict(X)
            if label == y:
                right_count += 1
        return right_count / len(X_test)


# 构建训练数据和测试数据

data = np.array(df.iloc[:100, [0, 1, -1]])
X, y = data[:, :-1], data[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 4.训练

clf = KNN(X_train, y_train)

# 5.测试

# 给定测试数据，计算其分类正确性
cc = clf.score(X_test, y_test)
print(cc)

# 1.0

# 6.预测

# 构建测试点 预测其类别
point = [7.0, 4.0]
print("测试点类别: {}".format(clf.predict(point)))

plt.scatter(df[:50]["sepal length"], df[:50]["sepal width"], label="0")
plt.scatter(df[50:100]["sepal length"], df[50:100]["sepal width"], label="1")
plt.plot(point[0], point[1], "g*", label="point")
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.legend()
show()

# 测试点类别: 1.0


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
