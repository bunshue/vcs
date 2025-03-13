"""
單純貝氏分類器 naive Bayes classifier

單純貝氏分類器（英語：Naive Bayes classifier，中國大陸稱為樸素貝葉斯分類器），
在機器學習中是一系列以假設特徵之間強（樸素）獨立下運用貝氏定理為基礎的簡單機率分類器。


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

from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
朴素贝叶斯
朴素贝叶斯是基于贝叶斯定理与特征条件独立假设的分类方法。
"""

"""
API Reference: http://scikit-learn.org/stable/modules/naive_bayes.html#naive-bayes
定义一个MultinomialNB类
"""


class MultinomialNB(object):
    def __init__(self, alpha=1.0, fit_prior=True, class_prior=None):
        """
        多项式模型的朴素贝叶斯分类器。多项式朴素贝叶斯分类器适用于具有离散特征的分类。

        参数
        ----------
        alpha : 平滑参数(float类型)，默认为1.0;
        如果alpha=0则不平滑。
        如果 0 < alpha < 1 则为Lidstone平滑
        如果 alpha = 1 则为Laplace 平滑

        fit_prior : 布尔型
        是否学习类别先验概率。
        如果设置为False，将使用统一的优先权。

        class_prior : array-like, size (n_classes,)
                类别的先验概率。如果指定，则不会根据数据调整优先级。
        """
        self.alpha = alpha
        self.fit_prior = fit_prior
        self.class_prior = class_prior
        self.classes = None
        self.conditional_prob = None

    def _calculate_feature_prob(self, feature):
        values = np.unique(feature)
        total_num = float(len(feature))
        value_prob = {}
        for v in values:
            value_prob[v] = (np.sum(np.equal(feature, v)) + self.alpha) / (
                total_num + len(values) * self.alpha
            )
        return value_prob

    def fit(self, X, y):
        # TODO: check X,y

        self.classes = np.unique(y)
        # 计算类别先验概率: P(y=ck)
        if self.class_prior == None:
            class_num = len(self.classes)
            if not self.fit_prior:
                self.class_prior = [
                    1.0 / class_num for _ in range(class_num)
                ]  # uniform prior
            else:
                self.class_prior = []
                sample_num = float(len(y))
                for c in self.classes:
                    c_num = np.sum(np.equal(y, c))
                    self.class_prior.append(
                        (c_num + self.alpha) / (sample_num + class_num * self.alpha)
                    )

        # 计算条件概率 P( xj | y=ck )
        self.conditional_prob = (
            {}
        )  # like { c0:{ x0:{ value0:0.2, value1:0.8 }, x1:{} }, c1:{...} }
        for c in self.classes:
            self.conditional_prob[c] = {}
            for i in range(len(X[0])):  # for each feature
                feature = X[np.equal(y, c)][:, i]
                self.conditional_prob[c][i] = self._calculate_feature_prob(feature)
        return self

    # 给定values_prob {value0:0.2,value1:0.1,value3:0.3,.. } and target_value
    # 返回target_value的概率
    def _get_xj_prob(self, values_prob, target_value):
        return values_prob[target_value]

    # 基于(class_prior,conditional_prob)预测单个样本
    def _predict_single_sample(self, x):
        label = -1
        max_posterior_prob = 0

        # 对于每个类别，计算其后验概率: class_prior * conditional_prob
        for c_index in range(len(self.classes)):
            current_class_prior = self.class_prior[c_index]
            current_conditional_prob = 1.0
            feature_prob = self.conditional_prob[self.classes[c_index]]
            j = 0
            for feature_i in feature_prob.keys():
                current_conditional_prob *= self._get_xj_prob(
                    feature_prob[feature_i], x[j]
                )
                j += 1

            # 比较后验概率并更新最大后验概率，标签
            if current_class_prior * current_conditional_prob > max_posterior_prob:
                max_posterior_prob = current_class_prior * current_conditional_prob
                label = self.classes[c_index]
        return label

    # 样本预测(也可以是单样本预测)
    def predict(self, X):
        # TODO1:check and raise NoFitError
        # ToDO2:check X
        if X.ndim == 1:
            return self._predict_single_sample(X)
        else:
            # 为每个样本进行分类
            labels = []
            for i in range(X.shape[0]):
                label = self._predict_single_sample(X[i])
                labels.append(label)
            return labels


# 多项式模型下的朴素贝叶斯分类算法测试：

X = np.array(
    [
        [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
        [4, 5, 5, 4, 4, 4, 5, 5, 6, 6, 6, 5, 5, 6, 6],
    ]
)
X = X.T
y = np.array([-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1])

nb = MultinomialNB(alpha=1.0, fit_prior=True)
nb.fit(X, y)
print(nb.predict(np.array([2, 4])))  # 输出-1

# 高斯模型 GaussianNB


# GaussianNB differ from MultinomialNB in these two method:
# _calculate_feature_prob, _get_xj_prob
class GaussianNB(MultinomialNB):
    # 计算给定特征的平均值（mu）和标准偏差（sigma）
    def _calculate_feature_prob(self, feature):
        mu = np.mean(feature)
        sigma = np.std(feature)
        return (mu, sigma)

    # 高斯分布的概率密度
    def _prob_gaussian(self, mu, sigma, x):
        return (
            1.0
            / (sigma * np.sqrt(2 * np.pi))
            * np.exp(-((x - mu) ** 2) / (2 * sigma**2))
        )

    # 给定mu和sigma，目标值返回高斯分布概率
    def _get_xj_prob(self, mu_sigma, target_value):
        return self._prob_gaussian(mu_sigma[0], mu_sigma[1], target_value)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/wine.data.csv")
df.head(10)

# df.iloc[:,1:].describe()

for c in df.columns[1:]:
    df.boxplot(c, by="Class", figsize=(7, 4), fontsize=14)
    plt.title("{}\n".format(c), fontsize=16)
    plt.xlabel("Wine Class", fontsize=16)
    plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(
    df["OD280/OD315 of diluted wines"],
    df["Flavanoids"],
    c=df["Class"],
    edgecolors="k",
    alpha=0.8,
    s=100,
)
plt.grid(True)
plt.title(
    "Scatter plot of two features showing the \ncorrelation and class seperation",
    fontsize=15,
)
plt.xlabel("OD280/OD315 of diluted wines", fontsize=15)
plt.ylabel("Flavanoids", fontsize=15)
plt.show()


def correlation_matrix(df):
    from matplotlib import cm as cm

    fig = plt.figure(figsize=(16, 12))
    ax1 = fig.add_subplot(111)
    cmap = cm.get_cmap("jet", 30)
    cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
    ax1.grid(True)
    plt.title("Wine data set features correlation\n", fontsize=15)
    labels = df.columns
    ax1.set_xticklabels(labels, fontsize=9)
    ax1.set_yticklabels(labels, fontsize=9)
    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    fig.colorbar(cax, ticks=[0.1 * i for i in range(-11, 11)])
    plt.show()


cc = correlation_matrix(df)
print(cc)

# Naive Bayes Classification

test_size = 0.3  # Test-set fraction

X = df.drop("Class", axis=1)
y = df["Class"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

X_train.shape

(124, 13)

X_train.head()

# Classification using GaussianNB

from sklearn.naive_bayes import GaussianNB

nbc = GaussianNB()

nbc.fit(X_train, y_train)

GaussianNB(priors=None)

# Prediction, classification report, and confusion matrix

y_pred = nbc.predict(X_test)
mislabel = np.sum((y_test != y_pred))
print(
    "Total number of mislabelled data points from {} test samples is {}".format(
        len(y_test), mislabel
    )
)

# Total number of mislabelled data points from 54 test samples is 2

print("The classification report is as follows...\n")
print(classification_report(y_pred, y_test))


cm = confusion_matrix(y_test, y_pred)
cmdf = pd.DataFrame(
    cm,
    index=["Class 1", "Class 2", " Class 3"],
    columns=["Class 1", "Class 2", " Class 3"],
)
print("The confusion matrix looks like following...\n")
cmdf

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


print("------------------------------------------------------------")  # 60個
