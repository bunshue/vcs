"""
introduction_to_machine_learning_03_svm

Support Vector Machine
    Support vector machine (SVM) is a binary linear classifier
    There are tricks to make SVM able to solve non-linear problems
    There are extensions which allows using SVM to multiclass classification or regression
    SVM is a supervised learning algorithm
    There are extensions which allows using SVM for (unsupervised) clustering

Linear SVM
    Lets consider a training dataset of N samples ( x → 1 , y 1 ) , ⋯ , ( x → N , y N )
    x → i is D -dimensional vector representing features
    y i is a class label, for convenience
    Missing or unrecognized delimiter for \left
    $y_i = \left{-1, 1\right}$
    At this point we assume that classes are linearly separable
    For visualization purpose lets use D = 2
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
from sklearn import tree
from sklearn import svm
from sklearn.datasets import make_blobs
from matplotlib.colors import ListedColormap


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# just to overwrite default colab style
plt.style.use("default")
plt.style.use("seaborn-talk")

# class I
X01 = [(2, 9), (7, 19), (1, 10), (3, 19), (4, 16), (5, 18)]

# class II
X02 = [(4, 3), (6, 7), (1, -10), (3, -1), (9, 5), (5, -7)]

"""
plt.xlim([0, 10])
plt.scatter(*(zip(*X01)), c='r')
plt.scatter(*(zip(*X02)), c='g')
plt.plot([0, 10], [0, 15], "b")
plt.plot([0, 10], [2, 22], "b")

plt.scatter(5, 9, c="m")  # test point
plt.text(0.5, -1.5, "aaa")
plt.text(0.3, 2.5, "bbb")
plt.text(2.9, 14, "ccc")

plt.title('aaa')
show()
"""

print("------------------------------------------------------------")  # 60個

"""
plt.plot([0, 10], [0, 20], "r-", zorder=0)
plt.plot([0, 10], [5, 25], "g--", zorder=0)
plt.plot([0, 10], [-5, 15], "b--", zorder=0)

plt.annotate("", (0, 5), (0.55, -4), arrowprops=dict(arrowstyle="<->"))
plt.annotate("", (3.05, 18.1), (3.8, 7.75), arrowprops=dict(arrowstyle="<->"))

plt.scatter(*(zip(*X01)), zorder=1, c='r')
plt.scatter(*(zip(*X02)), zorder=1, c='g')

sv = X01[:2] + X02[:2]

plt.scatter(*(zip(*sv)), zorder=1, facecolors="none", edgecolors="r", s=500)

plt.title('bbb')
show()
"""

print("------------------------------------------------------------")  # 60個

"""
# Hard margin
# Functional margin
# Geometric margin
# The optimal margin
# Lagrange multipliers


def flc(c, n=100):
    # Level curves of objective functions
    return np.array(
        [(c * np.cos(ang), c * np.sin(ang)) for ang in np.linspace(0, 2 * np.pi, n)]
    )


def g(n=100):
    # Constraint
    return np.array([(x, 1.0 / x) for x in np.linspace(0.1, 2.5, n)])


##### PLOT SETTINGS #####

plt.figure(figsize=(8, 8))
plt.xlim([-2.5, 2.5])
plt.ylim([-2.5, 2.5])
plt.grid(color="0.5", linestyle="--", linewidth=0.5)

##### LEVEL CURVES OF f(x, y) #####

for c in (0.2, 0.6, 1, 1.8, 2.2):
    plt.plot(*flc(c).T, color="C0")

plt.plot(*flc(np.sqrt(2)).T, color="C0", label="$f(x, y) = c$")

##### CONSTRAINTS #####

plt.plot(*g().T, color="C1", label="$g(x, y) = 0$")
plt.plot(*-g().T, color="C1")

##### INTERSECTIONS #####

plt.scatter(1, 1, c="C2", zorder=4)
plt.scatter(np.sqrt(0.345), np.sqrt(1 / 0.345), c="C3", zorder=4)

plt.legend()
plt.title('ccc')
show()

print("------------------------------------------------------------")  # 60個

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

ax = plt.figure().add_subplot(111, projection=Axes3D.name)

X, Y = np.meshgrid(np.linspace(-1, 3, 50), np.linspace(-5, 1, 50))
L = X**2 + Y * (X - 1)

ax.plot_surface(X, Y, L, cmap=cm.hsv)

ax.view_init(elev=45, azim=120)

ax.set_xlabel("$x$", labelpad=20)
ax.set_ylabel("$\lambda$", labelpad=20)
ax.set_zlabel("$\mathcal{L}$", labelpad=10)
plt.title("3D畫圖")
show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# Non-linear SVM
"""
    SVM can be applied to non-linear problems using the kernel trick
    However, before we go there, lets consider a simple non-linear problem

Example
    Lets consider two classes of 2D points:
        inside a circle
        outside a circle
"""


def generate_circle_data(R1=0, R2=1, N=500):
    """Generate N points in a circle for radius range (R1, R2)"""
    r = lambda: R1 + np.random.random() * (R2 - R1)

    return np.array(
        [(r() * np.cos(ang), r() * np.sin(ang)) for ang in np.linspace(0, 2 * np.pi, N)]
    )


C01 = generate_circle_data()
C02 = generate_circle_data(1, 2)

plt.scatter(*C01.T, marker=".")
plt.scatter(*C02.T, marker=".")
plt.title('eee')
show()

print("------------------------------")  # 30個

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

ax = plt.figure().add_subplot(111, projection=Axes3D.name)

Z01 = np.array([x**2 + y**2 for x, y in C01])
Z02 = np.array([x**2 + y**2 for x, y in C02])

ax.scatter(*C01.T, Z01, cmap=cm.hsv)
ax.scatter(*C02.T, Z02, cmap=cm.hsv)

ax.view_init(elev=15, azim=60)
plt.title('fff')
show()
'''
print("------------------------------------------------------------")  # 60個

# class I
X01 = [(2, 9), (7, 19), (1, 10), (3, 19), (4, 16), (5, 18)]

# class II
X02 = [(4, 3), (6, 7), (1, -10), (3, -1), (9, 5), (5, -7)]


plt.plot([0, 10], [0, 20], "C2-", zorder=0)
plt.plot([0, 10], [4, 24], "C3-", zorder=0)

plt.scatter(3, 9, c="C1", marker=",")

plt.scatter(*(zip(*X01)), zorder=1)
plt.scatter(*(zip(*X02)), zorder=1)
plt.title("ggg")
show()

print("------------------------------------------------------------")  # 60個

plt.plot([0, 10], [0, 20], "C2-", zorder=0)
plt.plot([0, 10], [5, 25], "C2--", zorder=0)
plt.plot([0, 10], [-5, 15], "C2--", zorder=0)

plt.scatter(3, 9, c="C1", marker=",")
plt.annotate("", (3.05, 8.7), (3.5, 1.75), arrowprops=dict(arrowstyle="<->"))
plt.text(3.5, 4.5, "$\\xi_i$")

plt.annotate("", (0, 5), (0.55, -4), arrowprops=dict(arrowstyle="<->"))
plt.text(0.5, -1.5, "$m$")
plt.text(0.3, 2.5, "$m$")

plt.annotate("", (3.05, 18.1), (3.8, 7.75), arrowprops=dict(arrowstyle="<->"))
plt.text(2.9, 14, "$m_i$")

plt.scatter(*(zip(*X01)), zorder=1)
plt.scatter(*(zip(*X02)), zorder=1)

sv = X01[:2] + X02[:2]

plt.scatter(*(zip(*sv)), zorder=1, facecolors="none", edgecolors="r", s=500)
plt.title("hhh")
show()

# Regularization

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SMO algorithm

plt.xticks([], [])
plt.yticks([], [])
plt.xlim([0, 1])
plt.ylim([0, 1])

plt.text(1.05, 0.5, "$\mu_1 = C$")
plt.text(-0.1, 0.5, "$\mu_1 = 0$")
plt.text(0.5, 1.05, "$\mu_2 = C$")
plt.text(0.5, -0.05, "$\mu_2 = 0$")

plt.plot(
    (0.6, 1), (0, 0.75), label="$y_1 \\neq y_2 \Rightarrow \mu_1 - \mu_2 = \gamma$"
)
plt.plot((0.4, 0), (0, 0.75), label="$y_1 = y_2 \Rightarrow \mu_1 + \mu_2 = \gamma$")

plt.legend()
plt.title("iii")
show()

print("------------------------------------------------------------")  # 60個

# class I
X01 = [(2, 9), (7, 19), (1, 10), (3, 19), (4, 16), (5, 18)]

# class II
X02 = [(4, 3), (6, 7), (1, -10), (3, -1), (9, 5), (5, -7)]

plt.xlim([0, 10])

plt.scatter(*(zip(*X01)))
plt.scatter(*(zip(*X02)))
plt.title("jjj")
show()

print("------------------------------------------------------------")  # 60個

# class I
X01 = [(2, 9), (7, 19), (1, 10), (3, 19), (4, 16), (5, 18)]

# class II
X02 = [(4, 3), (6, 7), (1, -10), (3, -1), (9, 5), (5, -7)]

# create a classifier
clf = svm.SVC(kernel="linear")

# train classifier - assign -1 label for X01 and 1 for X02
clf.fit(X01 + X02, [-1] * len(X01) + [1] * len(X02))

"""
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma='auto', kernel='linear',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
"""

# Lets visualize the result

sv = clf.support_vectors_  # support vectors
w = clf.coef_[0]  # weights
b = clf.intercept_  # intercept

# w[0] * x + w[1] * y + b = 0
f = lambda x: -(b + w[0] * x) / w[1]

# plot training data
plt.scatter(*(zip(*X01)))
plt.scatter(*(zip(*X02)))

# plt decision boundary
plt.plot([1, 9], [f(1), f(9)])

# mark support vectors
plt.scatter(*(zip(*sv)), zorder=1, facecolors="none", edgecolors="r", s=500)
plt.title("kkk")
show()

print("------------------------------------------------------------")  # 60個

# Circle


def generate_circle_data(R1=0, R2=1, N=500):
    """Generate N points in a circle for radius range (R1, R2)"""
    r = lambda: R1 + np.random.random() * (R2 - R1) + np.random.normal(0, 0.2)

    return np.array(
        [(r() * np.cos(ang), r() * np.sin(ang)) for ang in np.linspace(0, 2 * np.pi, N)]
    )


C01 = generate_circle_data()
C02 = generate_circle_data(1, 2)

plt.scatter(*C01.T, marker=".")
plt.scatter(*C02.T, marker=".")
plt.title("lll")
show()

print("mmmmmmmmmmmmm")
sys.exit()

print("------------------------------------------------------------")  # 60個

print("4種 SVM 核心 比較")
"""
We will consider 4 different kernels:
        linear
        polynomial of degree 3
        polynomial of degree 10
        Gaussian radial basis function (RBF)
"""

# create classifier with different kernels
clf_linear = svm.SVC(kernel="linear")
clf_rbf = svm.SVC(kernel="rbf")
clf_poly3 = svm.SVC(kernel="poly", degree=3)
clf_poly10 = svm.SVC(kernel="poly", degree=10)

titles = ("Linear", "RBF", "Polynomial, degree = 3", "Plynomial, degree = 10")

# create a mesh to plot in
xx, yy = np.meshgrid(np.arange(-3, 3, 0.01), np.arange(-3, 3, 0.01))

# loop over classifiers
for i, clf in enumerate((clf_linear, clf_rbf, clf_poly3, clf_poly10)):
    # train classifier - assign -1 label for C01 and 1 for C02
    clf.fit(np.concatenate((C01, C02), axis=0), [-1] * len(C01) + [1] * len(C02))

    # visualize results
    plt.subplot(2, 2, i + 1)

    # decision boundary
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)

    # training data
    plt.scatter(*C01.T, marker=".")
    plt.scatter(*C02.T, marker=".")

    plt.title(titles[i])

plt.tight_layout()
plt.title("mmm")
show()

print("------------------------------------------------------------")  # 60個

# Multiclass classification

# Example: blobs

# generate 5 blobs with fixed random generator
X, Y = make_blobs(n_samples=500, centers=8, random_state=300)

plt.scatter(*X.T, c=Y, marker=".", cmap="Dark2")
plt.title("nnn")
show()

print("------------------------------------------------------------")  # 60個

# We can use the same function as last time to train and visualize


def train_and_look(classifier, X, Y, ax=None, title="", cmap="Dark2"):
    """Train classifier on (X,Y). Plot data and prediction."""
    # create new axis if not provided
    ax = ax or plt.gca()

    ax.set_title(title)

    # plot training data
    ax.scatter(*X.T, c=Y, marker=".", cmap=cmap)

    # train a cliassifier
    classifier.fit(X, Y)

    # create a grid of testing points
    x_, y_ = np.meshgrid(
        np.linspace(*ax.get_xlim(), num=200), np.linspace(*ax.get_ylim(), num=200)
    )

    # convert to an array of 2D points
    test_data = np.vstack([x_.ravel(), y_.ravel()]).T

    # make a prediction and reshape to grid structure
    z_ = classifier.predict(test_data).reshape(x_.shape)

    # arange z bins so class labels are in the middle
    z_levels = np.arange(len(np.unique(Y)) + 1) - 0.5

    # plot contours corresponding to classifier prediction
    ax.contourf(x_, y_, z_, alpha=0.25, cmap=cmap, levels=z_levels)


fig, ax = plt.subplots(1, 3, figsize=(15, 5))

title = ("Linear", "RBF", "Polynomial")

settings = ({"kernel": "linear"}, {"kernel": "rbf"}, {"kernel": "poly", "degree": 5})

# train and look at SVM with different kernels
for i in range(0, 3):
    train_and_look(svm.SVC(**settings[i]), X, Y, ax=ax[i], title=title[i])

plt.title("ooo")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" no boston
#SVM regression

#Example - Boston Housing dataset

from sklearn.datasets import load_boston

boston = load_boston()

print(boston.DESCR)

#Visualize dataset

for i, feature in enumerate(boston.data.T):
    plt.subplot(3, 5, i+1)
    plt.scatter(feature, boston.target, marker='.')
    plt.title(boston.feature_names[i])
  
plt.tight_layout()
plt.title('ppp')
show()

print("------------------------------------------------------------")  # 60個

boston_pd = pd.DataFrame(boston.data)     # load features
boston_pd.columns = boston.feature_names  # add features names
boston_pd['PRICE'] = boston.target        # add a column with price

boston_pd.head()

#Test SVR

from sklearn.svm import SVR

regressor = SVR(kernel="linear")
regressor.fit(boston.data, boston.target)

prediction = regressor.predict(boston.data)

plt.xlabel("True price")
plt.ylabel("Predicted price")

plt.scatter(boston.target, prediction, marker='.')
plt.title('qqq last')
show()
"""
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


print("------------------------------------------------------------")  # 60個
