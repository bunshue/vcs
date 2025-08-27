"""
scikit-learn01

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass

num_bins = 50  # 直方圖顯示時的束數

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from scipy import stats
from sklearn import neighbors
from sklearn import datasets

from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_circles

from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

from sklearn.model_selection import validation_curve
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score

print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

n_samples, n_features = iris.data.shape
print(iris.keys())
print((n_samples, n_features))
print(iris.data.shape)
print(iris.target.shape)
print(iris.target_names)
print(iris.feature_names)

# 'sepal width (cm)'
x_index = 1
# 'petal length (cm)'
y_index = 2

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

plt.scatter(
    iris.data[:, x_index],
    iris.data[:, y_index],
    c=iris.target,
    cmap=plt.cm.get_cmap("RdYlBu", 3),
)
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.clim(-0.5, 2.5)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])
show()

# K-Nearest Neighbors Classifier
# The K-Nearest Neighbors (KNN) algorithm is a method used for algorithm used for classification or for regression. In both cases, the input consists of the k closest training examples in the feature space. Given a new, unknown observation, look up which points have the closest features and assign the predominant class.

iris = datasets.load_iris()
X, y = iris.data, iris.target

# create the model
knn = neighbors.KNeighborsClassifier(n_neighbors=5, weights="uniform")

# fit the model
knn.fit(X, y)

# What kind of iris has 3cm x 5cm sepal and 4cm x 2cm petal?
X_pred = [3, 5, 4, 2]
result = knn.predict(
    [
        X_pred,
    ]
)

print(iris.target_names[result])
print(iris.target_names)
print(
    knn.predict_proba(
        [
            X_pred,
        ]
    )
)

from fig_code import plot_iris_knn

plot_iris_knn()
show()


sys.exit()
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

sns.set()

# Linear Regression

# Create some simple data
np.random.seed(0)
X = np.random.random(size=(20, 1))
y = 3 * X.squeeze() + 2 + np.random.randn(20)

plt.plot(X.squeeze(), y, "o")
show()

# Fit the model:

model = LinearRegression()
model.fit(X, y)

# Plot the data and the model prediction
X_fit = np.linspace(0, 1, 100)[:, np.newaxis]
y_fit = model.predict(X_fit)

plt.plot(X.squeeze(), y, "o")
plt.plot(X_fit.squeeze(), y_fit)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# scikit-learn-k-means

sns.set()

# K-Means Clustering

iris = datasets.load_iris()

X, y = iris.data, iris.target

pca = PCA(n_components=2)
pca.fit(X)
X_reduced = pca.transform(X)
print("Reduced dataset shape:", X_reduced.shape)

plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap="RdYlBu")

print("Meaning of the 2 components:")
for component in pca.components_:
    print(
        " + ".join(
            "%.3f x %s" % (value, name)
            for value, name in zip(component, iris.feature_names)
        )
    )
show()

k_means = KMeans(n_clusters=3, random_state=0)  # Fixing the RNG in kmeans
k_means.fit(X)
y_pred = k_means.predict(X)

plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y_pred, cmap="RdYlBu")
show()

X, y = make_blobs(n_samples=300, centers=4, random_state=0, cluster_std=0.60)
plt.scatter(X[:, 0], X[:, 1], s=50)
show()

est = KMeans(4)  # 4 clusters
est.fit(X)
y_kmeans = est.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap="rainbow")
show()

""" NG
#The K-Means Algorithm: Expectation Maximization

from fig_code import plot_kmeans_interactive
plot_kmeans_interactive()
show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# scikit-learn-svm

sns.set()

# Support Vector Machine Classifier

X, y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)

xfit = np.linspace(-1, 3.5)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap="spring")

# Draw three lines that couple separate the data
for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]:
    yfit = m * xfit + b
    plt.plot(xfit, yfit, "-k")
    plt.fill_between(
        xfit, yfit - d, yfit + d, edgecolor="none", color="#AAAAAA", alpha=0.4
    )

plt.xlim(-1, 3.5)
show()

clf = SVC(kernel="linear")
clf.fit(X, y)

# Plot the boundary:


def plot_svc_decision_function(clf, ax=None):
    """Plot the decision function for a 2D SVC"""
    if ax is None:
        ax = plt.gca()
    x = np.linspace(plt.xlim()[0], plt.xlim()[1], 30)
    y = np.linspace(plt.ylim()[0], plt.ylim()[1], 30)
    Y, X = np.meshgrid(y, x)
    P = np.zeros_like(X)
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            P[i, j] = clf.decision_function([xi, yj])
    # plot the margins
    ax.contour(
        X, Y, P, colors="k", levels=[-1, 0, 1], alpha=0.5, linestyles=["--", "-", "--"]
    )


plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap="spring")
# NG plot_svc_decision_function(clf)
plt.scatter(
    clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=200, facecolors="none"
)
show()


def plot_svm(N=100):
    X, y = make_blobs(n_samples=200, centers=2, random_state=0, cluster_std=0.60)
    X = X[:N]
    y = y[:N]
    clf = SVC(kernel="linear")
    clf.fit(X, y)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap="spring")
    plt.xlim(-1, 4)
    plt.ylim(-1, 6)
    # plot_svc_decision_function(clf, plt.gca())
    plt.scatter(
        clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=200, facecolors="none"
    )

N = 100
plot_svm(N)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Support Vector Machine with Kernels Classifier
X, y = make_circles(100, factor=0.1, noise=0.1)

clf = SVC(kernel="linear").fit(X, y)

plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap="spring")
# plot_svc_decision_function(clf)
show()

# A simple model that could be useful is a radial basis function:

r = np.exp(-(X[:, 0] ** 2 + X[:, 1] ** 2))

from mpl_toolkits import mplot3d

elev=30
azim=30

ax = plt.subplot(projection="3d")
ax.scatter3D(X[:, 0], X[:, 1], r, c=y, s=50, cmap="spring")
ax.view_init(elev=elev, azim=azim)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("r")

show()


# In three dimensions, there is a clear separation between the data. Run the SVM with the rbf kernel:

clf = SVC(kernel="rbf")
clf.fit(X, y)

plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap="spring")
# NG plot_svc_decision_function(clf)
plt.scatter(
    clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=200, facecolors="none"
)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# scikit-learn-pca
# Dimensionality Reduction: PCA

sns.set()

iris = datasets.load_iris()

X, y = iris.data, iris.target

pca = PCA(n_components=2)
pca.fit(X)
X_reduced = pca.transform(X)
print("Reduced dataset shape:", X_reduced.shape)

plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap="RdYlBu")

print("Meaning of the 2 components:")
for component in pca.components_:
    print(
        " + ".join(
            "%.3f x %s" % (value, name)
            for value, name in zip(component, iris.feature_names)
        )
    )
show()

# Dimensionality Reduction: Principal Component Analysis in-depth

np.random.seed(1)
X = np.dot(np.random.random(size=(2, 2)), np.random.normal(size=(2, 200))).T
plt.plot(X[:, 0], X[:, 1], "o")
plt.axis("equal")
show()

pca = PCA(n_components=2)
pca.fit(X)
print(pca.explained_variance_)
print(pca.components_)

plt.plot(X[:, 0], X[:, 1], "o", alpha=0.5)
for length, vector in zip(pca.explained_variance_ratio_, pca.components_):
    v = vector * 3 * np.sqrt(length)
    plt.plot([0, v[0]], [0, v[1]], "-k", lw=3)
plt.axis("equal")
show()

clf = PCA(0.95)  # keep 95% of variance
X_trans = clf.fit_transform(X)
print(X.shape)
print(X_trans.shape)

X_new = clf.inverse_transform(X_trans)
plt.plot(X[:, 0], X[:, 1], "o", alpha=0.2)
plt.plot(X_new[:, 0], X_new[:, 1], "ob", alpha=0.8)
plt.axis("equal")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Validation and Model Selection

# from __future__ import print_function, division

sns.set()

# Validating Models

digits = datasets.load_digits()
X = digits.data
y = digits.target

# Let's fit a K-neighbors classifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)

y_pred = knn.predict(X)

print("{0} / {1} correct".format(np.sum(y == y_pred), len(y)))

# Validation Sets

X_train, X_test, y_train, y_test = train_test_split(X, y)
X_train.shape, X_test.shape

# ((1347, 64), (450, 64))

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print("{0} / {1} correct".format(np.sum(y_test == y_pred), len(y_test)))

cc = accuracy_score(y_test, y_pred)
print(cc)

# 0.97333333333333338

cc = knn.score(X_test, y_test)
print(cc)

# 0.97333333333333338

for n_neighbors in [1, 5, 10, 20, 30]:
    knn = KNeighborsClassifier(n_neighbors)
    knn.fit(X_train, y_train)
    print(n_neighbors, knn.score(X_test, y_test))

# Cross-Validation

X1, X2, y1, y2 = train_test_split(X, y, test_size=0.5, random_state=0)
X1.shape, X2.shape

# ((898, 64), (899, 64))

print(KNeighborsClassifier(1).fit(X2, y2).score(X1, y1))
print(KNeighborsClassifier(1).fit(X1, y1).score(X2, y2))

cv = cross_val_score(KNeighborsClassifier(1), X, y, cv=10)
cc = cv.mean()
print(cc)

# K-fold Cross-Validation

cc = cross_val_score(KNeighborsClassifier(1), X, y, cv=10)
print(cc)

# Overfitting, Underfitting and Model Selection


def test_func(x, err=0.5):
    y = 10 - 1.0 / (x + 0.1)
    if err > 0:
        y = np.random.normal(y, err)
    return y


# Now let's create a realization of this dataset:


def make_data(N=40, error=1.0, random_seed=1):
    # randomly sample the data
    np.random.seed(1)
    X = np.random.random(N)[:, np.newaxis]
    y = test_func(X.ravel(), error)

    return X, y


X, y = make_data(40, error=1)
plt.scatter(X.ravel(), y)
show()

# Now say we want to perform a regression on this data. Let's use the built-in linear regression function to compute a fit:

X_test = np.linspace(-0.1, 1.1, 500)[:, None]

model = LinearRegression()
model.fit(X, y)
y_test = model.predict(X_test)

plt.scatter(X.ravel(), y)
plt.plot(X_test.ravel(), y_test)
plt.title("mean squared error: {0:.3g}".format(mean_squared_error(model.predict(X), y)))
show()

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


def PolynomialRegression(degree=2, **kwargs):
    return make_pipeline(PolynomialFeatures(degree), LinearRegression(**kwargs))


# Now we'll use this to fit a quadratic curve to the data.

model = PolynomialRegression(2)
model.fit(X, y)
y_test = model.predict(X_test)

plt.scatter(X.ravel(), y)
plt.plot(X_test.ravel(), y_test)
plt.title("mean squared error: {0:.3g}".format(mean_squared_error(model.predict(X), y)))
show()

# This reduces the mean squared error, and makes a much better fit. What happens if we use an even higher-degree polynomial?

model = PolynomialRegression(30)
model.fit(X, y)
y_test = model.predict(X_test)

plt.scatter(X.ravel(), y)
plt.plot(X_test.ravel(), y_test)
plt.title("mean squared error: {0:.3g}".format(mean_squared_error(model.predict(X), y)))
plt.ylim(-4, 14)
show()


degree=1
Npts=50
X, y = make_data(Npts, error=1)
X_test = np.linspace(-0.1, 1.1, 500)[:, None]

model = PolynomialRegression(degree=degree)
model.fit(X, y)
y_test = model.predict(X_test)

plt.scatter(X.ravel(), y)
plt.plot(X_test.ravel(), y_test)
plt.ylim(-4, 14)
plt.title("mean squared error: {0:.2f}".format(mean_squared_error(model.predict(X), y)))

show()

# Detecting Over-fitting with Validation Curves

X, y = make_data(120, error=1.0)
plt.scatter(X, y)
show()

def rms_error(model, X, y):
    y_pred = model.predict(X)
    return np.sqrt(np.mean((y - y_pred) ** 2))


degree = np.arange(0, 18)
val_train, val_test = validation_curve(
    PolynomialRegression(),
    X,
    y,
    param_name="polynomialfeatures__degree",
    param_range=degree,
    cv=7,
    scoring="neg_root_mean_squared_error",
)

# Now let's plot the validation curves:


def plot_with_err(x, data, **kwargs):
    mu, std = data.mean(1), data.std(1)
    lines = plt.plot(x, mu, "-", **kwargs)
    plt.fill_between(
        x,
        mu - std,
        mu + std,
        edgecolor="none",
        facecolor=lines[0].get_color(),
        alpha=0.2,
    )


plot_with_err(degree, val_train, label="training scores")
plot_with_err(degree, val_test, label="validation scores")
plt.xlabel("degree")
plt.ylabel("rms error")
plt.legend()
show()

model = PolynomialRegression(4).fit(X, y)
plt.scatter(X, y)
plt.plot(X_test, model.predict(X_test))
show()

# Detecting Data Sufficiency with Learning Curves

# from sklearn.learning_curve import learning_curve # old
# from sklearn.learning_curve import learning_curve
from sklearn.model_selection import learning_curve


def plot_learning_curve(degree=3):
    train_sizes = np.linspace(0.05, 1, 20)
    N_train, val_train, val_test = learning_curve(
        PolynomialRegression(degree),
        X,
        y,
        train_sizes=train_sizes,
        cv=5,
        scoring="accuracy",
    )  # 5折交叉驗證
    plot_with_err(N_train, val_train, label="training scores")
    plot_with_err(N_train, val_test, label="validation scores")
    plt.xlabel("Training Set Size")
    plt.ylabel("rms error")
    plt.ylim(0, 3)
    plt.xlim(5, 80)
    plt.legend()


plot_learning_curve(1)
show()

plot_learning_curve(3)
show()

plot_learning_curve(10)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# scikit-learn-random forest

sns.set()

# Random Forest Classifier

import fig_code

fig_code.plot_example_decision_tree()

# Creating a Decision Tree

X, y = make_blobs(n_samples=300, centers=4, random_state=0, cluster_std=1.0)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap="rainbow")
show()

# We have some convenience functions in the repository that help
from fig_code import visualize_tree

# Decision Trees and over-fitting

clf = DecisionTreeClassifier()

plt.figure()
visualize_tree(clf, X[:200], y[:200], boundaries=False)
show()

plt.figure()
visualize_tree(clf, X[-200:], y[-200:], boundaries=False)
show()

# Ensembles of Estimators: Random Forests

random_state=0
X, y = make_blobs(n_samples=300, centers=4, random_state=0, cluster_std=2.0)
clf = DecisionTreeClassifier(max_depth=15)

rng = np.random.RandomState(random_state)
i = np.arange(len(y))
rng.shuffle(i)
visualize_tree(
    clf,
    X[i[:250]],
    y[i[:250]],
    boundaries=False,
    xlim=(X[:, 0].min(), X[:, 0].max()),
    ylim=(X[:, 1].min(), X[:, 1].max()),
)
show()

clf = RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1)
visualize_tree(clf, X, y, boundaries=False)
show()

# Random Forest Regressor

X = 10 * np.random.rand(100)


def model(X, sigma=0.3):
    fast_oscillation = np.sin(5 * X)
    slow_oscillation = np.sin(0.5 * X)
    noise = sigma * np.random.randn(len(X))

    return slow_oscillation + fast_oscillation + noise


y = model(X)
plt.errorbar(X, y, 0.3, fmt="o")
show()

xfit = np.linspace(0, 10, 1000)
yfit = RandomForestRegressor(100).fit(X[:, None], y).predict(xfit[:, None])
ytrue = model(xfit, 0)

plt.errorbar(X, y, 0.3, fmt="o")
plt.plot(xfit, yfit, "-r")
plt.plot(xfit, ytrue, "-k", alpha=0.5)
show()

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

