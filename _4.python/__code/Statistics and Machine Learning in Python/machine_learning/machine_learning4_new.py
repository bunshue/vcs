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

from sklearn import linear_model
import sklearn.linear_model
from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


import sklearn.linear_model as lm
import sklearn.metrics as metrics

np.set_printoptions(precision=2)
# pd.set_option('precision', 2)


bv = np.array([10, 20, 30, 40, 50])  # business volume
tax = 0.2 * bv  # Tax
bp = 0.1 * bv + np.array([-0.1, 0.2, 0.1, -0.2, 0.1])  # business potential

X = np.column_stack([bv, tax])
beta_star = np.array([0.1, 0])  # true solution

"""
Since tax and bv are correlated, there is an infinite number of linear combinations
leading to the same prediction.
"""

# 10 times the bv then subtract it 9 times using the tax variable:
beta_medium = np.array([0.1 * 10, -0.1 * 9 * (1 / 0.2)])
# 100 times the bv then subtract it 99 times using the tax variable:
beta_large = np.array([0.1 * 100, -0.1 * 99 * (1 / 0.2)])

print(
    "L2 norm of coefficients: small:%.2f, medium:%.2f, large:%.2f."
    % (np.sum(beta_star**2), np.sum(beta_medium**2), np.sum(beta_large**2))
)

print("However all models provide the exact same predictions.")
assert np.all(np.dot(X, beta_star) == np.dot(X, beta_medium))
assert np.all(np.dot(X, beta_star) == np.dot(X, beta_large))


# Dataset with some correlation
X, y, coef = datasets.make_regression(
    n_samples=100, n_features=10, n_informative=5, effective_rank=3, coef=True
)

lr = lm.LinearRegression().fit(X, y)

l2 = lm.Ridge(alpha=10).fit(X, y)  # lambda is alpha!

l1 = lm.Lasso(alpha=0.1).fit(X, y)  # lambda is alpha !

l1l2 = lm.ElasticNet(alpha=0.1, l1_ratio=0.9).fit(X, y)

pd.DataFrame(
    np.vstack((coef, lr.coef_, l2.coef_, l1.coef_, l1l2.coef_)),
    index=["True", "lr", "l2", "l1", "l1l2"],
)


print("------------------------------------------------------------")  # 60個

import sklearn.metrics as metrics

X, y = datasets.make_regression()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

lr = lm.LinearRegression()
lr.fit(X_train, y_train)
yhat = lr.predict(X_test)

r2 = metrics.r2_score(y_test, yhat)
mse = metrics.mean_squared_error(y_test, yhat)
mae = metrics.mean_absolute_error(y_test, yhat)

print("r2: %.3f, mae: %.3f, mse: %.3f" % (r2, mae, mse))


print("------------------------------------------------------------")  # 60個

res = y_test - lr.predict(X_test)

y_mu = np.mean(y_test)
ss_tot = np.sum((y_test - y_mu) ** 2)
ss_res = np.sum(res**2)

r2 = 1 - ss_res / ss_tot
mse = np.mean(res**2)
mae = np.mean(np.abs(res))

print("r2: %.3f, mae: %.3f, mse: %.3f" % (r2, mae, mse))


print("------------------------------------------------------------")  # 60個
# linear_classification
print("------------------------------------------------------------")  # 60個


import sklearn.linear_model as lm
import sklearn.metrics as metrics

np.set_printoptions(precision=2)
# pd.set_option('precision', 2)


# Linear discriminant analysis (LDA)


from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# Dataset 2 two multivariate normal
n_samples, n_features = 100, 2
mean0, mean1 = np.array([0, 0]), np.array([0, 2])
Cov = np.array([[1, 0.8], [0.8, 1]])

X0 = np.random.multivariate_normal(mean0, Cov, n_samples)
X1 = np.random.multivariate_normal(mean1, Cov, n_samples)
X = np.vstack([X0, X1])
y = np.array([0] * X0.shape[0] + [1] * X1.shape[0])


# LDA with scikit-learn
lda = LDA()
proj = lda.fit(X, y).transform(X)
y_pred_lda = lda.predict(X)

errors = y_pred_lda != y
print("Nb errors=%i, error rate=%.2f" % (errors.sum(), errors.sum() / len(y_pred_lda)))


print("------------------------------------------------------------")  # 60個


# Logistic regression
def logistic(x):
    return 1 / (1 + np.exp(-x))


x = np.linspace(-6, 6, 100)
plt.plot(x, logistic(x))
plt.grid(True)
plt.title("Logistic (sigmoid)")


logreg = lm.LogisticRegression().fit(X, y)

# This class implements regularized logistic regression.
# C is the Inverse of regularization strength.
# Large value => no regularization.

logreg.fit(X, y)
y_pred_logreg = logreg.predict(X)

errors = y_pred_logreg != y
print(
    "Nb errors=%i, error rate=%.2f" % (errors.sum(), errors.sum() / len(y_pred_logreg))
)
print(logreg.coef_)


print("------------------------------------------------------------")  # 60個

# Dataset with some correlation
X, y = datasets.make_classification(
    n_samples=100,
    n_features=10,
    n_informative=5,
    n_redundant=3,
    n_classes=2,
    shuffle=False,
)

lr = lm.LogisticRegression().fit(X, y)

l2 = lm.LogisticRegression(penalty="l2", C=0.1).fit(X, y)  # lambda = 1 / C!

# use solver 'saga' to handle L1 penalty
l1 = lm.LogisticRegression(penalty="l1", C=0.1, solver="saga").fit(
    X, y
)  # lambda = 1 / C!

l1l2 = lm.LogisticRegression(
    penalty="elasticnet", C=0.1, l1_ratio=0.5, solver="saga"
).fit(
    X, y
)  # lambda = 1 / C!


pd.DataFrame(
    np.vstack((lr.coef_, l2.coef_, l1.coef_, l1l2.coef_)),
    index=["lr", "l2", "l1", "l1l2"],
)


print("------------------------------------------------------------")  # 60個

# Ridge Fisher's linear classification (L2-regularization)
# Ridge logistic regression (L2-regularization)

from sklearn import linear_model

lrl2 = linear_model.LogisticRegression(penalty="l2", C=0.1)
# This class implements regularized logistic regression. C is the Inverse of regularization strength.
# Large value => no regularization.

lrl2.fit(X, y)
y_pred_l2 = lrl2.predict(X)
prob_pred_l2 = lrl2.predict_proba(X)

print("Probas of 5 first samples for class 0 and class 1:")
print(prob_pred_l2[:5, :])

print("Coef vector:")
print(lrl2.coef_)

# Retrieve proba from coef vector
probas = 1 / (1 + np.exp(-(np.dot(X, lrl2.coef_.T) + lrl2.intercept_))).ravel()
print("Diff", np.max(np.abs(prob_pred_l2[:, 1] - probas)))

errors = y_pred_l2 != y
print("Nb errors=%i, error rate=%.2f" % (errors.sum(), errors.sum() / len(y)))

print("------------------------------------------------------------")  # 60個

# Lasso logistic regression (L1-regularization)

from sklearn import linear_model

lrl1 = lm.LogisticRegression(penalty="l1", C=0.1, solver="saga")  # lambda = 1 / C!

# This class implements regularized logistic regression. C is the Inverse of regularization strength.
# Large value => no regularization.

lrl1.fit(X, y)
y_pred_lrl1 = lrl1.predict(X)

errors = y_pred_lrl1 != y
print("Nb errors=%i, error rate=%.2f" % (errors.sum(), errors.sum() / len(y_pred_lrl1)))

print("Coef vector:")
print(lrl1.coef_)


print("------------------------------------------------------------")  # 60個


from sklearn import svm

svmlin = svm.LinearSVC(C=0.1)
# Remark: by default LinearSVC uses squared_hinge as loss
svmlin.fit(X, y)
y_pred_svmlin = svmlin.predict(X)

errors = y_pred_svmlin != y
print(
    "Nb errors=%i, error rate=%.2f" % (errors.sum(), errors.sum() / len(y_pred_svmlin))
)
print("Coef vector:")
print(svmlin.coef_)

print("------------------------------------------------------------")  # 60個

from sklearn import svm

svmlinl1 = svm.LinearSVC(penalty="l1", dual=False)
# Remark: by default LinearSVC uses squared_hinge as loss

svmlinl1.fit(X, y)
y_pred_svmlinl1 = svmlinl1.predict(X)

errors = y_pred_svmlinl1 != y
print(
    "Nb errors=%i, error rate=%.2f"
    % (errors.sum(), errors.sum() / len(y_pred_svmlinl1))
)
print("Coef vector:")
print(svmlinl1.coef_)


print("------------------------------------------------------------")  # 60個

# Use SGD solver
enetlog = lm.SGDClassifier(
    loss="log_loss", penalty="elasticnet", alpha=0.1, l1_ratio=0.5
)
enetlog.fit(X, y)

# Or saga solver:
# enetloglike = lm.LogisticRegression(penalty='elasticnet',
#                                    C=.1, l1_ratio=0.5, solver='saga')

enethinge = lm.SGDClassifier(
    loss="hinge", penalty="elasticnet", alpha=0.1, l1_ratio=0.5
)
enethinge.fit(X, y)

print("Hinge loss and logistic loss provide almost the same predictions.")
print("Confusion matrix")
metrics.confusion_matrix(enetlog.predict(X), enethinge.predict(X))

print("Decision_function log x hinge losses:")
_ = plt.plot(enetlog.decision_function(X), enethinge.decision_function(X), "o")

print("------------------------------------------------------------")  # 60個


from sklearn import metrics

y_pred = [0, 1, 0, 0]
y_true = [0, 1, 0, 1]

metrics.accuracy_score(y_true, y_pred)

# The overall precision an recall
metrics.precision_score(y_true, y_pred)
metrics.recall_score(y_true, y_pred)

# Recalls on individual classes: SEN & SPC
recalls = metrics.recall_score(y_true, y_pred, average=None)
recalls[0]  # is the recall of class 0: specificity
recalls[1]  # is the recall of class 1: sensitivity

# Balanced accuracy
b_acc = recalls.mean()

# The overall precision an recall on each individual class
p, r, f, s = metrics.precision_recall_fscore_support(y_true, y_pred)


print("------------------------------------------------------------")  # 60個

""" NG
import scipy.stats

acc, N = 0.65, 70
pval = scipy.stats.binom_test(x=int(acc * N), n=N, p=0.5) / 2
print(pval)
"""
print("------------------------------------------------------------")  # 60個

# Area Under Curve (AUC) of Receiver operating characteristic (ROC)

score_pred = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
y_true = np.array([0, 0, 0, 0, 1, 1, 1, 1])
thres = 0.9
y_pred = (score_pred > thres).astype(int)

print("With a threshold of %.2f, the rule always predict 0. Predictions:" % thres)
print(y_pred)
metrics.accuracy_score(y_true, y_pred)

# The overall precision an recall on each individual class
r = metrics.recall_score(y_true, y_pred, average=None)
print(
    "Recalls on individual classes are:",
    r,
    "ie, 100% of specificity, 0% of sensitivity",
)

# However AUC=1 indicating a perfect separation of the two classes
auc = metrics.roc_auc_score(y_true, score_pred)
print("But the AUC of %.2f demonstrate a good classes separation." % auc)


print("------------------------------------------------------------")  # 60個

# dataset
X, y = datasets.make_classification(
    n_samples=500,
    n_features=5,
    n_informative=2,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    shuffle=False,
)

print(*["#samples of class %i = %i;" % (lev, np.sum(y == lev)) for lev in np.unique(y)])

print("# No Reweighting balanced dataset")
lr_inter = linear_model.LogisticRegression(C=1)
lr_inter.fit(X, y)
p, r, f, s = metrics.precision_recall_fscore_support(y, lr_inter.predict(X))
print("SPC: %.3f; SEN: %.3f" % tuple(r))
print("# => The predictions are balanced in sensitivity and specificity\n")

# Create imbalanced dataset, by subsampling sample of class 0: keep only 10% of
# class 0's samples and all class 1's samples.
n0 = int(np.rint(np.sum(y == 0) / 20))
subsample_idx = np.concatenate((np.where(y == 0)[0][:n0], np.where(y == 1)[0]))
Ximb = X[subsample_idx, :]
yimb = y[subsample_idx]
print(
    *[
        "#samples of class %i = %i;" % (lev, np.sum(yimb == lev))
        for lev in np.unique(yimb)
    ]
)

print("# No Reweighting on imbalanced dataset")
lr_inter = linear_model.LogisticRegression(C=1)
lr_inter.fit(Ximb, yimb)
p, r, f, s = metrics.precision_recall_fscore_support(yimb, lr_inter.predict(Ximb))
print("SPC: %.3f; SEN: %.3f" % tuple(r))
print("# => Sensitivity >> specificity\n")

print("# Reweighting on imbalanced dataset")
lr_inter_reweight = linear_model.LogisticRegression(C=1, class_weight="balanced")
lr_inter_reweight.fit(Ximb, yimb)
p, r, f, s = metrics.precision_recall_fscore_support(
    yimb, lr_inter_reweight.predict(Ximb)
)
print("SPC: %.3f; SEN: %.3f" % tuple(r))
print("# => The predictions are balanced in sensitivity and specificity\n")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# clustering
print("------------------------------------------------------------")  # 60個

from sklearn import cluster
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, :2]  # use only 'sepal length and sepal width'
y_iris = iris.target

km2 = cluster.KMeans(n_clusters=2).fit(X)
km3 = cluster.KMeans(n_clusters=3).fit(X)
km4 = cluster.KMeans(n_clusters=4).fit(X)

plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.scatter(X[:, 0], X[:, 1], c=km2.labels_)
plt.title("K=2, J=%.2f" % km2.inertia_)

plt.subplot(132)
plt.scatter(X[:, 0], X[:, 1], c=km3.labels_)
plt.title("K=3, J=%.2f" % km3.inertia_)

plt.subplot(133)
plt.scatter(X[:, 0], X[:, 1], c=km4.labels_)  # .astype(np.float))
plt.title("K=4, J=%.2f" % km4.inertia_)

plt.show()

print("------------------------------------------------------------")  # 60個

import plot_utils
import sklearn
from sklearn import datasets
from sklearn.mixture import GaussianMixture

# import pystatsml.plot_utils

colors = sns.color_palette()

iris = datasets.load_iris()
X = iris.data[:, :2]  # 'sepal length (cm)''sepal width (cm)'
y_iris = iris.target

gmm2 = GaussianMixture(n_components=2, covariance_type="full").fit(X)
gmm3 = GaussianMixture(n_components=3, covariance_type="full").fit(X)
gmm4 = GaussianMixture(n_components=4, covariance_type="full").fit(X)

plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.scatter(
    X[:, 0], X[:, 1], c=[colors[lab] for lab in gmm2.predict(X)]
)  # , color=colors)
for i in range(gmm2.covariances_.shape[0]):
    plot_utils.plot_cov_ellipse(
        cov=gmm2.covariances_[i, :],
        pos=gmm2.means_[i, :],
        facecolor="none",
        linewidth=2,
        edgecolor=colors[i],
    )
    plt.scatter(
        gmm2.means_[i, 0],
        gmm2.means_[i, 1],
        edgecolor=colors[i],
        marker="o",
        s=100,
        facecolor="w",
        linewidth=2,
    )
plt.title("K=2")

plt.subplot(132)
plt.scatter(X[:, 0], X[:, 1], c=[colors[lab] for lab in gmm3.predict(X)])
for i in range(gmm3.covariances_.shape[0]):
    plot_utils.plot_cov_ellipse(
        cov=gmm3.covariances_[i, :],
        pos=gmm3.means_[i, :],
        facecolor="none",
        linewidth=2,
        edgecolor=colors[i],
    )
    plt.scatter(
        gmm3.means_[i, 0],
        gmm3.means_[i, 1],
        edgecolor=colors[i],
        marker="o",
        s=100,
        facecolor="w",
        linewidth=2,
    )
plt.title("K=3")

plt.subplot(133)
plt.scatter(
    X[:, 0], X[:, 1], c=[colors[lab] for lab in gmm4.predict(X)]
)  # .astype(np.float))
for i in range(gmm4.covariances_.shape[0]):
    plot_utils.plot_cov_ellipse(
        cov=gmm4.covariances_[i, :],
        pos=gmm4.means_[i, :],
        facecolor="none",
        linewidth=2,
        edgecolor=colors[i],
    )
    plt.scatter(
        gmm4.means_[i, 0],
        gmm4.means_[i, 1],
        edgecolor=colors[i],
        marker="o",
        s=100,
        facecolor="w",
        linewidth=2,
    )
_ = plt.title("K=4")

plt.show()

print("------------------------------------------------------------")  # 60個

# Bayesian information criterion (BIC)

X = iris.data
y_iris = iris.target

bic = list()
# print(X)

ks = np.arange(1, 10)

for k in ks:
    gmm = GaussianMixture(n_components=k, covariance_type="full")
    gmm.fit(X)
    bic.append(gmm.bic(X))

k_chosen = ks[np.argmin(bic)]

plt.plot(ks, bic)
plt.xlabel("k")
plt.ylabel("BIC")
plt.show()

print("Choose k=", k_chosen)


print("------------------------------------------------------------")  # 60個

from sklearn import cluster
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, :2]  # 'sepal length (cm)''sepal width (cm)'
y_iris = iris.target

ward2 = cluster.AgglomerativeClustering(n_clusters=2, linkage="ward").fit(X)
ward3 = cluster.AgglomerativeClustering(n_clusters=3, linkage="ward").fit(X)
ward4 = cluster.AgglomerativeClustering(n_clusters=4, linkage="ward").fit(X)

plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.scatter(X[:, 0], X[:, 1], c=ward2.labels_)
plt.title("K=2")

plt.subplot(132)
plt.scatter(X[:, 0], X[:, 1], c=ward3.labels_)
plt.title("K=3")

plt.subplot(133)
plt.scatter(X[:, 0], X[:, 1], c=ward4.labels_)  # .astype(np.float))
plt.title("K=4")

plt.show()
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# decomposition
print("------------------------------------------------------------")  # 60個

import scipy
from sklearn.decomposition import PCA

# dataset
n_samples = 100
experience = np.random.normal(size=n_samples)
salary = 1500 + experience + np.random.normal(size=n_samples, scale=0.5)
X = np.column_stack([experience, salary])
print(X.shape)

# PCA using SVD
X -= X.mean(axis=0)  # Centering is required
U, s, Vh = scipy.linalg.svd(X, full_matrices=False)
# U : Unitary matrix having left singular vectors as columns.
#     Of shape (n_samples,n_samples) or (n_samples,n_comps), depending on
#     full_matrices.
#
# s : The singular values, sorted in non-increasing order. Of shape (n_comps,),
#     with n_comps = min(n_samples, n_features).
#
# Vh: Unitary matrix having right singular vectors as rows.
#     Of shape (n_features, n_features) or (n_comps, n_features) depending
# on full_matrices.

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.scatter(U[:, 0], U[:, 1], s=50)
plt.axis("equal")
plt.title("U: Rotated and scaled data")

plt.subplot(132)

# Project data
PC = np.dot(X, Vh.T)
plt.scatter(PC[:, 0], PC[:, 1], s=50)
plt.axis("equal")
plt.title("XV: Rotated data")
plt.xlabel("PC1")
plt.ylabel("PC2")

plt.subplot(133)
plt.scatter(X[:, 0], X[:, 1], s=50)
for i in range(Vh.shape[0]):
    plt.arrow(
        x=0,
        y=0,
        dx=Vh[i, 0],
        dy=Vh[i, 1],
        head_width=0.2,
        head_length=0.2,
        linewidth=2,
        fc="r",
        ec="r",
    )
    plt.text(
        Vh[i, 0],
        Vh[i, 1],
        "v%i" % (i + 1),
        color="r",
        fontsize=15,
        horizontalalignment="right",
        verticalalignment="top",
    )
plt.axis("equal")
plt.ylim(-4, 4)

plt.title("X: original data (v1, v2:PC dir.)")
plt.xlabel("experience")
plt.ylabel("salary")

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

np.random.seed(42)

# dataset
n_samples = 100
experience = np.random.normal(size=n_samples)
salary = 1500 + experience + np.random.normal(size=n_samples, scale=0.5)
X = np.column_stack([experience, salary])

# PCA with scikit-learn
pca = PCA(n_components=2)
pca.fit(X)
print(pca.explained_variance_ratio_)

PC = pca.transform(X)

plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1])
plt.xlabel("x1")
plt.ylabel("x2")

plt.subplot(122)
plt.scatter(PC[:, 0], PC[:, 1])
plt.xlabel("PC1 (var=%.2f)" % pca.explained_variance_ratio_[0])
plt.ylabel("PC2 (var=%.2f)" % pca.explained_variance_ratio_[1])
plt.axis("equal")
plt.tight_layout()

from time import time
import matplotlib.pyplot as plt
from matplotlib import offsetbox
from sklearn import (
    manifold,
    datasets,
    decomposition,
    ensemble,
    discriminant_analysis,
    random_projection,
    neighbors,
)

print(__doc__)

digits = datasets.load_digits(n_class=6)
X = digits.data
y = digits.target
n_samples, n_features = X.shape
n_neighbors = 30


plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn import decomposition

n_row, n_col = 2, 3
n_components = n_row * n_col
image_shape = (64, 64)

faces, _ = fetch_olivetti_faces(return_X_y=True, shuffle=True, random_state=1)
n_samples, n_features = faces.shape


# Utils function
def plot_gallery(title, images, n_col=n_col, n_row=n_row, cmap=plt.cm.gray):
    plt.figure(figsize=(2.0 * n_col, 2.26 * n_row))
    plt.suptitle(title, size=16)
    for i, comp in enumerate(images):
        plt.subplot(n_row, n_col, i + 1)
        vmax = max(comp.max(), -comp.min())
        plt.imshow(
            comp.reshape(image_shape),
            cmap=cmap,
            interpolation="nearest",
            vmin=-vmax,
            vmax=vmax,
        )
        plt.xticks(())
        plt.yticks(())
    plt.subplots_adjust(0.01, 0.05, 0.99, 0.93, 0.04, 0.0)


plt.show()


print("------------------------------------------------------------")  # 60個

# Preprocessing

# global centering
faces_centered = faces - faces.mean(axis=0)

# local centering
faces_centered -= faces_centered.mean(axis=1).reshape(n_samples, -1)

# First centered Olivetti faces

plot_gallery("First centered Olivetti faces", faces_centered[:n_components])

pca = decomposition.PCA(n_components=n_components)
pca.fit(faces_centered)
plot_gallery("PCA first %i loadings" % n_components, pca.components_[:n_components])

plt.show()

print("------------------------------------------------------------")  # 60個
# decomposition_solutions
print("------------------------------------------------------------")  # 60個

# Principal Component Analysis(PCA)

import scipy
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA


class BasicPCA:
    def fit(self, X):
        # U : Unitary matrix having left singular vectors as columns.
        #     Of shape (n_samples,n_samples) or (n_samples,n_comps), depending on
        #     full_matrices.
        #
        # s : The singular values, sorted in non-increasing order. Of shape (n_comps,),
        #     with n_comps = min(n_samples, n_features).
        #
        # Vh: Unitary matrix having right singular vectors as rows.
        #     Of shape (n_features, n_features) or (n_comps, n_features) depending on full_matrices.
        self.mean = X.mean(axis=0)
        Xc = X - self.mean  # Centering is required
        U, s, V = scipy.linalg.svd(Xc, full_matrices=False)
        self.explained_variance_ = (s**2) / X.shape[0]
        self.explained_variance_ratio_ = (
            self.explained_variance_ / self.explained_variance_.sum()
        )
        self.princ_comp_dir = V

    def transform(self, X):
        Xc = X - self.mean
        return np.dot(Xc, self.princ_comp_dir.T)


# dataset
n_samples = 100
experience = np.random.normal(size=n_samples)
salary = 1500 + experience + np.random.normal(size=n_samples, scale=0.5)
X = np.column_stack([experience, salary])

X = np.column_stack([experience, salary])
pca = PCA(n_components=2)
pca.fit(X)

basic_pca = BasicPCA()
basic_pca.fit(X)

print(pca.explained_variance_ratio_)
# assert np.all(basic_pca.transform(X) == pca.transform(X))

# Apply PCA on iris dataset

import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

# https://tgmstat.wordpress.com/2013/11/28/computing-and-visualizing-pca-in-r/

try:
    salary = pd.read_csv("datasets/iris.csv")
except:
    url = "https://github.com/duchesnay/pystatsml/raw/master/datasets/iris.csv"
    df = pd.read_csv(url)

print(df.head())

print(df.describe())

X = np.array(df.iloc[:, :4])
# np.around(np.corrcoef(X.T), 3)

# Center and standardize

X = np.array(df.iloc[:, :4])
X -= np.mean(X, axis=0)
X /= np.std(X, axis=0, ddof=1)
np.around(np.corrcoef(X.T), 3)

pca = PCA(n_components=X.shape[1])
pca.fit(X)

print(pca.explained_variance_ratio_)

K = 2
pca = PCA(n_components=X.shape[1])
pca.fit(X)
PC = pca.transform(X)
# print(PC)

print(pca.components_)
CorPC = pd.DataFrame(
    [
        [np.corrcoef(X[:, j], PC[:, k])[0, 1] for j in range(X.shape[1])]
        for k in range(K)
    ],
    columns=df.columns[:4],
    index=["PC %i" % k for k in range(K)],
)

print(CorPC)

colors = {"setosa": "r", "versicolor": "g", "virginica": "blue"}
print(df["species"].unique())
# plt.scatter(df['experience'], df['salary'], c=df['education'].apply(lambda x: colors[x]), s=100)
plt.scatter(PC[:, 0], PC[:, 1], c=df["species"].apply(lambda x: colors[x]))
plt.xlabel("PC1")
plt.ylabel("PC2")

# Pairewise plot

import seaborn as sns

df["PC1"] = PC[:, 0]
df["PC2"] = PC[:, 1]

ax = sns.pairplot(df, hue="species")

plt.show()

print("------------------------------------------------------------")  # 60個


plt.show()

print("------------------------------------------------------------")  # 60個


plt.show()

print("------------------------------------------------------------")  # 60個


plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
