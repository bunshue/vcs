

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

#逻辑回归模型成本函数

def f_1(x):
    return -np.log(x)

def f_0(x):
    return -np.log(1 - x)

X = np.linspace(0.01, 0.99, 100)
f = [f_1, f_0]
titles = ["y=1: $-log(h_\\theta(x))$", "y=0: $-log(1 - h_\\theta(x))$"]
plt.figure(figsize=(12, 4))
for i in range(len(f)):
    plt.subplot(1, 2, i + 1)
    plt.title(titles[i])
    plt.xlabel("$h_\\theta(x)$")
    plt.ylabel("$Cost(h_\\theta(x), y)$")
    plt.plot(X, f[i](X), 'r-')

plt.suptitle('邏輯回歸模型成本函數')

plt.show()

print("------------------------------------------------------------")  # 60個

print('L1/L2 范数')

def L1(x):
    return 1 - np.abs(x)

def L2(x):
    return np.sqrt(1 - np.power(x, 2))

def contour(v, x):
    return 5 - np.sqrt(v - np.power(x + 2, 2))    # 4x1^2 + 9x2^2 = v

def format_spines(title):    
    ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
    ax.spines['right'].set_color('none')            # 隐藏坐标轴
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')           # 设置刻度显示位置
    ax.spines['bottom'].set_position(('data',0))    # 设置下方坐标轴位置
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))      # 设置左侧坐标轴位置

    plt.title(title)
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)

plt.figure(figsize=(8.4, 4), dpi=144)

x = np.linspace(-1, 1, 100)
cx = np.linspace(-3, 1, 100)

plt.subplot(1, 2, 1)
format_spines('L1 norm')
plt.plot(x, L1(x), 'r-', x, -L1(x), 'r-')
plt.plot(cx, contour(20, cx), 'r--', cx, contour(15, cx), 'r--', cx, contour(10, cx), 'r--')

plt.subplot(1, 2, 2)
format_spines('L2 norm')
plt.plot(x, L2(x), 'b-', x, -L2(x), 'b-')
plt.plot(cx, contour(19, cx), 'b--', cx, contour(15, cx), 'b--', cx, contour(10, cx), 'b--')

plt.show()

print("------------------------------------------------------------")  # 60個

# 载入数据
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target
print('data shape: {0}; no. positive: {1}; no. negative: {2}'.format(
    X.shape, y[y==1].shape[0], y[y==0].shape[0]))
print(cancer.data[0])

print(cancer.feature_names)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型训练
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print('train score: {train_score:.6f}; test score: {test_score:.6f}'.format(
    train_score=train_score, test_score=test_score))

# 样本预测
y_pred = model.predict(X_test)
print('matchs: {0}/{1}'.format(np.equal(y_pred, y_test).sum(), y_test.shape[0]))

# 预测概率：找出低于 90% 概率的样本个数
y_pred_proba = model.predict_proba(X_test)
print('sample of predict probability: {0}'.format(y_pred_proba[0]))
y_pred_proba_0 = y_pred_proba[:, 0] > 0.1 
result = y_pred_proba[y_pred_proba_0]
y_pred_proba_1 = result[:, 1] > 0.1
print(result[y_pred_proba_1])

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

# 增加多项式预处理
def polynomial_model(degree=1, **kwarg):
    polynomial_features = PolynomialFeatures(degree=degree,
                                             include_bias=False)
    logistic_regression = LogisticRegression(**kwarg)
    pipeline = Pipeline([("polynomial_features", polynomial_features),
                         ("logistic_regression", logistic_regression)])
    return pipeline

model = polynomial_model(degree=2, penalty='l1', solver='liblinear')

start = time.time()
model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
cv_score = model.score(X_test, y_test)
print('elaspe: {0:.6f}; train_score: {1:0.6f}; cv_score: {2:.6f}'.format(
    time.time()-start, train_score, cv_score))

logistic_regression = model.named_steps['logistic_regression']
print('model parameters shape: {0}; count of non-zero element: {1}'.format(
    logistic_regression.coef_.shape, 
    np.count_nonzero(logistic_regression.coef_)))

from common.utils import plot_learning_curve
from sklearn.model_selection import ShuffleSplit

cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
title = 'Learning Curves (degree={0}, penalty={1})'
degrees = [1, 2]
penalty = 'l1'

start = time.time()
plt.figure(figsize=(12, 4), dpi=144)
for i in range(len(degrees)):
    plt.subplot(1, len(degrees), i + 1)
    plot_learning_curve(plt, polynomial_model(degree=degrees[i], penalty=penalty, solver='liblinear', max_iter=300), 
                        title.format(degrees[i], penalty), X, y, ylim=(0.8, 1.01), cv=cv)

print('elaspe: {0:.6f}'.format(time.time()-start))

plt.show()

print("------------------------------------------------------------")  # 60個

import warnings
warnings.filterwarnings("ignore")

penalty = 'l2'

start = time.time()
plt.figure(figsize=(12, 4), dpi=144)
for i in range(len(degrees)):
    plt.subplot(1, len(degrees), i + 1)
    plot_learning_curve(plt, polynomial_model(degree=degrees[i], penalty=penalty, solver='lbfgs'), 
                        title.format(degrees[i], penalty), X, y, ylim=(0.8, 1.01), cv=cv)

print('elaspe: {0:.6f}'.format(time.time()-start))

plt.show()

print("------------------------------------------------------------")  # 60個

def entropy(px):
    return - (px * np.log2(px))

x = np.linspace(0.01, 1, 100)
plt.figure(figsize=(5, 3), dpi=200)
plt.title('$Entropy(x) = - P(x) * log_2(P(x))$')
plt.xlim(0, 1)
plt.ylim(0, 0.6)
plt.xlabel('P(x)')
plt.ylabel('Entropy')
plt.plot(x, entropy(x), 'r-');

plt.show()

print("------------------------------------------------------------")  # 60個

def gini_impurity(px):
    return px * (1 - px)

x = np.linspace(0.01, 1, 100)
plt.figure(figsize=(5, 3), dpi=200)
plt.title('$Gini(x) = P(x) (1 - P(x))$')
plt.xlim(0, 1)
plt.ylim(0, 0.6)
plt.xlabel('P(x)')
plt.ylabel('Gini Impurity')
plt.plot(x, entropy(x), 'r-');

plt.show()

print("------------------------------------------------------------")  # 60個

import pandas as pd

def read_dataset(fname):
    # 指定第一列作为行索引
    data = pd.read_csv(fname, index_col=0) 
    # 丢弃无用的数据
    data.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
    # 处理性别数据
    data['Sex'] = (data['Sex'] == 'male').astype('int')
    # 处理登船港口数据
    labels = data['Embarked'].unique().tolist()
    data['Embarked'] = data['Embarked'].apply(lambda n: labels.index(n))
    # 处理缺失数据
    data = data.fillna(0)
    return data

train = read_dataset('datasets/titanic/train.csv')

print(train.head())

print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import train_test_split

y = train['Survived'].values
X = train.drop(['Survived'], axis=1).values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print('train dataset: {0}; test dataset: {1}'.format(X_train.shape, X_test.shape))

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print('train score: {0}; test score: {1}'.format(train_score, test_score))

print("------------------------------------------------------------")  # 60個

from sklearn.tree import export_graphviz

with open("titanic.dot", 'w') as f:
    f = export_graphviz(clf, out_file=f)

# 1. 在电脑上安装 graphviz
# 2. 运行 `dot -Tpng titanic.dot -o titanic.png` 
# 3. 在当前目录查看生成的决策树 titanic.png

# 参数选择 max_depth
def cv_score(d):
    clf = DecisionTreeClassifier(max_depth=d)
    clf.fit(X_train, y_train)
    tr_score = clf.score(X_train, y_train)
    cv_score = clf.score(X_test, y_test)
    return (tr_score, cv_score)

depths = range(2, 15)
scores = [cv_score(d) for d in depths]
tr_scores = [s[0] for s in scores]
cv_scores = [s[1] for s in scores]

best_score_index = np.argmax(cv_scores)
best_score = cv_scores[best_score_index]
best_param = depths[best_score_index]
print('best param: {0}; best score: {1}'.format(best_param, best_score))

plt.figure(figsize=(10, 6), dpi=144)
plt.grid()
plt.xlabel('max depth of decision tree')
plt.ylabel('score')
plt.plot(depths, cv_scores, '.g-', label='cross-validation score')
plt.plot(depths, tr_scores, '.r--', label='training score')
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

# 训练模型，并计算评分
def cv_score(val):
    clf = DecisionTreeClassifier(criterion='gini', min_impurity_decrease=val)
    clf.fit(X_train, y_train)
    tr_score = clf.score(X_train, y_train)
    cv_score = clf.score(X_test, y_test)
    return (tr_score, cv_score)

# 指定参数范围，分别训练模型，并计算评分
values = np.linspace(0, 0.005, 50)
scores = [cv_score(v) for v in values]
tr_scores = [s[0] for s in scores]
cv_scores = [s[1] for s in scores]

# 找出评分最高的模型参数
best_score_index = np.argmax(cv_scores)
best_score = cv_scores[best_score_index]
best_param = values[best_score_index]
print('best param: {0}; best score: {1}'.format(best_param, best_score))

# 画出模型参数与模型评分的关系
plt.figure(figsize=(10, 6), dpi=144)
plt.grid()
plt.xlabel('threshold of entropy')
plt.ylabel('score')
plt.plot(values, cv_scores, '.g-', label='cross-validation score')
plt.plot(values, tr_scores, '.r--', label='training score')
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

def plot_curve(train_sizes, cv_results, xlabel):
    train_scores_mean = cv_results['mean_train_score']
    train_scores_std = cv_results['std_train_score']
    test_scores_mean = cv_results['mean_test_score']
    test_scores_std = cv_results['std_test_score']
    plt.figure(figsize=(10, 6), dpi=144)
    plt.title('parameters turning')
    plt.grid()
    plt.xlabel(xlabel)
    plt.ylabel('score')
    plt.fill_between(train_sizes, 
                     train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, 
                     alpha=0.1, color="r")
    plt.fill_between(train_sizes, 
                     test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, 
                     alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, '.--', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, '.-', color="g",
             label="Cross-validation score")

    plt.legend(loc="best")

from sklearn.model_selection import GridSearchCV

thresholds = np.linspace(0, 0.005, 50)
# Set the parameters by cross-validation
param_grid = {'min_impurity_decrease': thresholds}

clf = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5, return_train_score=True)
clf.fit(X, y)
print("best param: {0}\nbest score: {1}".format(clf.best_params_, clf.best_score_))

plot_curve(thresholds, clf.cv_results_, xlabel='gini thresholds')

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import GridSearchCV

entropy_thresholds = np.linspace(0, 0.01, 50)
gini_thresholds = np.linspace(0, 0.005, 50)

# Set the parameters by cross-validation
param_grid = [{'criterion': ['entropy'], 
               'min_impurity_decrease': entropy_thresholds},
              {'criterion': ['gini'], 
               'min_impurity_decrease': gini_thresholds},
              {'max_depth': range(2, 10)},
              {'min_samples_split': range(2, 30, 2)}]

clf = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5, return_train_score=True)
clf.fit(X, y)
print("best param: {0}\nbest score: {1}".format(clf.best_params_, clf.best_score_))

print("------------------------------------------------------------")  # 60個

print('生成决策树图形')

clf = DecisionTreeClassifier(criterion='entropy', min_impurity_decrease=0.002857142857142857)
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print('train score: {0}; test score: {1}'.format(train_score, test_score))

# 导出 titanic.dot 文件
with open("titanic.dot", 'w') as f:
    f = export_graphviz(clf, out_file=f)

# 1. 在电脑上安装 graphviz
# 2. 运行 `dot -Tpng titanic.dot -o titanic.png` 
# 3. 在当前目录查看生成的决策树 titanic.png

print("------------------------------------------------------------")  # 60個

class1 = np.array([[1, 1], [1, 3], [2, 1], [1, 2], [2, 2]])
class2 = np.array([[4, 4], [5, 5], [5, 4], [5, 3], [4, 5], [6, 4]])

plt.figure(figsize=(8, 6), dpi=144)

plt.title('Decision Boundary')

plt.xlim(0, 8)
plt.ylim(0, 6)
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.scatter(class1[:, 0], class1[:, 1], marker='o')
plt.scatter(class2[:, 0], class2[:, 1], marker='s')
plt.plot([1, 5], [5, 1], '-r')
plt.arrow(4, 4, -1, -1, shape='full', color='r')
plt.plot([3, 3], [0.5, 6], '--b')
plt.arrow(4, 4, -1, 0, shape='full', color='b', linestyle='--')
plt.annotate(r'margin 1',
             xy=(3.5, 4), xycoords='data',
             xytext=(3.1, 4.5), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'margin 2',
             xy=(3.5, 3.5), xycoords='data',
             xytext=(4, 3.5), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'support vector',
             xy=(4, 4), xycoords='data',
             xytext=(5, 4.5), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'support vector',
             xy=(2, 2), xycoords='data',
             xytext=(0.5, 1.5), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(8, 6), dpi=144)

plt.title('Support Vector Machine')

plt.xlim(0, 8)
plt.ylim(0, 6)
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.scatter(class1[:, 0], class1[:, 1], marker='o')
plt.scatter(class2[:, 0], class2[:, 1], marker='s')
plt.plot([1, 5], [5, 1], '-r')
plt.plot([0, 4], [4, 0], '--b', [2, 6], [6, 2], '--b')
plt.arrow(4, 4, -1, -1, shape='full', color='b')
plt.annotate(r'$w^T x + b = 0$',
             xy=(5, 1), xycoords='data',
             xytext=(6, 1), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'$w^T x + b = 1$',
             xy=(6, 2), xycoords='data',
             xytext=(7, 2), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'$w^T x + b = -1$',
             xy=(3.5, 0.5), xycoords='data',
             xytext=(4.5, 0.2), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'd',
             xy=(3.5, 3.5), xycoords='data',
             xytext=(2, 4.5), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'A',
             xy=(4, 4), xycoords='data',
             xytext=(5, 4.5), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs

plt.figure(figsize=(13, 6), dpi=144)

# sub plot 1
plt.subplot(1, 2, 1)

X, y = make_blobs(n_samples=100, 
                  n_features=2, 
                  centers=[(1, 1), (2, 2)], 
                  random_state=4, 
                  shuffle=False,
                  cluster_std=0.4)

plt.title('Non-linear Separatable')

plt.xlim(0, 3)
plt.ylim(0, 3)
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.scatter(X[y==0][:, 0], X[y==0][:, 1], marker='o')
plt.scatter(X[y==1][:, 0], X[y==1][:, 1], marker='s')
plt.plot([0.5, 2.5], [2.5, 0.5], '-r')

# sub plot 2
plt.subplot(1, 2, 2)

class1 = np.array([[1, 1], [1, 3], [2, 1], [1, 2], [2, 2], [1.5, 1.5], [1.2, 1.7]])
class2 = np.array([[4, 4], [5, 5], [5, 4], [5, 3], [4, 5], [6, 4], [5.5, 3.5], [4.5, 4.5], [2, 1.5]])

plt.title('Slack Variable')

plt.xlim(0, 7)
plt.ylim(0, 7)
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.scatter(class1[:, 0], class1[:, 1], marker='o')
plt.scatter(class2[:, 0], class2[:, 1], marker='s')
plt.plot([1, 5], [5, 1], '-r')
plt.plot([0, 4], [4, 0], '--b', [2, 6], [6, 2], '--b')
plt.arrow(2, 1.5, 2.25, 2.25, shape='full', color='b')
plt.annotate(r'violate margin rule.',
             xy=(2, 1.5), xycoords='data',
             xytext=(0.2, 0.5), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'normal sample. $\epsilon = 0$',
             xy=(4, 5), xycoords='data',
             xytext=(4.5, 5.5), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'$\epsilon > 0$',
             xy=(3, 2.5), xycoords='data',
             xytext=(3, 1.5), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(8, 4), dpi=144)

plt.title('Cost')

plt.xlim(0, 4)
plt.ylim(0, 2)
plt.xlabel('$y^{(i)} (w^T x^{(i)} + b)$')
plt.ylabel('Cost')
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.plot([0, 1], [1.5, 0], '-r')
plt.plot([1, 3], [0.015, 0.015], '-r')
plt.annotate(r'$J_i = R \epsilon_i$ for $y^{(i)} (w^T x^{(i)} + b) \geq 1 - \epsilon_i$',
             xy=(0.7, 0.5), xycoords='data',
             xytext=(1, 1), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'$J_i = 0$ for $y^{(i)} (w^T x^{(i)} + b) \geq 1$',
             xy=(1.5, 0), xycoords='data',
             xytext=(1.8, 0.2), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(13, 6), dpi=144)

class1 = np.array([[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [3, 2], [4, 1], [5, 1]])
class2 = np.array([[2.2, 4], [1.5, 5], [1.8, 4.6], [2.4, 5], [3.2, 5], [3.7, 4], [4.5, 4.5], [5.4, 3]])

# sub plot 1
plt.subplot(1, 2, 1)

plt.title('Non-linear Separatable in Low Dimension')

plt.xlim(0, 6)
plt.ylim(0, 6)
plt.yticks(())
plt.xlabel('X1')
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')
ax.spines['left'].set_color('none')

plt.scatter(class1[:, 0], np.zeros(class1[:, 0].shape[0]) + 0.05, marker='o')
plt.scatter(class2[:, 0], np.zeros(class2[:, 0].shape[0]) + 0.05, marker='s')

# sub plot 2
plt.subplot(1, 2, 2)

plt.title('Linear Separatable in High Dimension')

plt.xlim(0, 6)
plt.ylim(0, 6)
plt.xlabel('X1')
plt.ylabel('X2')
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.scatter(class1[:, 0], class1[:, 1], marker='o')
plt.scatter(class2[:, 0], class2[:, 1], marker='s')
plt.plot([1, 5], [3.8, 2], '-r')

plt.show()

print("------------------------------------------------------------")  # 60個

def gaussian_kernel(x, mean, sigma):
    return np.exp(- (x - mean)**2 / (2 * sigma**2))

x = np.linspace(0, 6, 500)
mean = 1
sigma1 = 0.1
sigma2 = 0.3

plt.figure(figsize=(10, 3), dpi=144)

# sub plot 1
plt.subplot(1, 2, 1)
plt.title('Gaussian for $\sigma={0}$'.format(sigma1))

plt.xlim(0, 2)
plt.ylim(0, 1.1)
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.plot(x, gaussian_kernel(x, mean, sigma1), 'r-')

# sub plot 2
plt.subplot(1, 2, 2)
plt.title('Gaussian for $\sigma={0}$'.format(sigma2))

plt.xlim(0, 2)
plt.ylim(0, 1.1)
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.plot(x, gaussian_kernel(x, mean, sigma2), 'r-')

plt.show()

print("------------------------------------------------------------")  # 60個

def plot_hyperplane(clf, X, y, 
                    h=0.02, 
                    draw_sv=True, 
                    title='hyperplan'):
    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    plt.title(title)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap='hot', alpha=0.5)

    markers = ['o', 's', '^']
    colors = ['b', 'r', 'c']
    labels = np.unique(y)
    for label in labels:
        plt.scatter(X[y==label][:, 0], 
                    X[y==label][:, 1], 
                    c=colors[label], 
                    marker=markers[label])
    if draw_sv:
        sv = clf.support_vectors_
        plt.scatter(sv[:, 0], sv[:, 1], c='y', marker='x')
        
from sklearn import svm
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=100, centers=2, 
                  random_state=0, cluster_std=0.3)
clf = svm.SVC(C=1.0, kernel='linear')
clf.fit(X, y)

plt.figure(figsize=(12, 4), dpi=144)
plot_hyperplane(clf, X, y, h=0.01, title='Maximum Margin Hyperplan')

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import svm
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=100, centers=3, 
                  random_state=0, cluster_std=0.8)
clf_linear = svm.SVC(C=1.0, kernel='linear')
clf_poly = svm.SVC(C=1.0, kernel='poly', degree=3)
clf_rbf = svm.SVC(C=1.0, kernel='rbf', gamma=0.5)
clf_rbf2 = svm.SVC(C=1.0, kernel='rbf', gamma=0.1)

plt.figure(figsize=(10, 10), dpi=144)

clfs = [clf_linear, clf_poly, clf_rbf, clf_rbf2]
titles = ['Linear Kernel', 
          'Polynomial Kernel with Degree=3', 
          'Gaussian Kernel with $\gamma=0.5$', 
          'Gaussian Kernel with $\gamma=0.1$']
for clf, i in zip(clfs, range(len(clfs))):
    clf.fit(X, y)
    plt.subplot(2, 2, i+1)
    plot_hyperplane(clf, X, y, title=titles[i])

plt.show()

print("------------------------------------------------------------")  # 60個

# 载入数据
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target
print('data shape: {0}; no. positive: {1}; no. negative: {2}'.format(
    X.shape, y[y==1].shape[0], y[y==0].shape[0]))


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


print('高斯核函数')

from sklearn.svm import SVC

clf = SVC(C=1.0, kernel='rbf', gamma=0.1)
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print('train score: {0}; test score: {1}'.format(train_score, test_score))

from common.utils import plot_param_curve
from sklearn.model_selection import GridSearchCV

gammas = np.linspace(0, 0.0003, 30)
param_grid = {'gamma': gammas}
clf = GridSearchCV(SVC(), param_grid, cv=5)
#clf = GridSearchCV(SVC(), param_grid, cv=5, scoring='roc_auc',n_jobs=-1) 

clf.fit(X, y)
print("best param: {0}\nbest score: {1}".format(clf.best_params_, clf.best_score_))

""" 有錯誤
plt.figure(figsize=(10, 4), dpi=144)

plot_param_curve(plt, gammas, clf.cv_results_, xlabel='gamma');

plt.show()
"""

print("------------------------------------------------------------")  # 60個

from common.utils import plot_learning_curve
from sklearn.model_selection import ShuffleSplit

cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
title = 'Learning Curves for Gaussian Kernel'

start = time.time()
plt.figure(figsize=(10, 4), dpi=144)
plot_learning_curve(plt, SVC(C=1.0, kernel='rbf', gamma=0.01),
                    title, X, y, ylim=(0.5, 1.01), cv=cv)

print('elaspe: {0:.6f}'.format(time.time()-start))

plt.show()

print("------------------------------------------------------------")  # 60個

print('多项式核函数')

from sklearn.svm import SVC

clf = SVC(C=1.0, kernel='poly', degree=2)
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print('train score: {0}; test score: {1}'.format(train_score, test_score))

from common.utils import plot_learning_curve
from sklearn.model_selection import ShuffleSplit

cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
title = 'Learning Curves with degree={0}'
degrees = [1, 2]

start = time.time()
plt.figure(figsize=(12, 4), dpi=144)
for i in range(len(degrees)):
    plt.subplot(1, len(degrees), i + 1)
    plot_learning_curve(plt, SVC(C=1.0, kernel='poly', degree=degrees[i]),
                        title.format(degrees[i]), X, y, ylim=(0.8, 1.01), cv=cv, n_jobs=4)

print('elaspe: {0:.6f}'.format(time.time()-start))

plt.show()

print("------------------------------------------------------------")  # 60個

print('多项式 LinearSVC')

from sklearn.svm import LinearSVC
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline

def create_model(degree=2, **kwarg):
    polynomial_features = PolynomialFeatures(degree=degree,
                                             include_bias=False)
    scaler = MinMaxScaler()
    linear_svc = LinearSVC(**kwarg)
    pipeline = Pipeline([("polynomial_features", polynomial_features),
                         ("scaler", scaler),
                         ("linear_svc", linear_svc)])
    return pipeline

clf = create_model(penalty='l1', dual=False)
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print('train score: {0}; test score: {1}'.format(train_score, test_score))

from common.utils import plot_learning_curve
from sklearn.model_selection import ShuffleSplit

cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
title = 'Learning Curves for LinearSVC with Degree={0}'
degrees = [1, 2]

start = time.time()
plt.figure(figsize=(12, 4), dpi=144)
for i in range(len(degrees)):
    plt.subplot(1, len(degrees), i + 1)
    plot_learning_curve(plt, create_model(penalty='l1', dual=False, degree=degrees[i]),
                        title.format(degrees[i]), X, y, ylim=(0.8, 1.01), cv=cv)

print('elaspe: {0:.6f}'.format(time.time()-start))

plt.show()

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
