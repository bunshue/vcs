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
import sklearn.linear_model as lm
import sklearn.metrics as metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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

from sklearn.decomposition import PCA

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

from sklearn.datasets import fetch_olivetti_faces
from sklearn import decomposition

n_row, n_col = 2, 3
n_components = n_row * n_col
image_shape = (64, 64)

faces, _ = fetch_olivetti_faces(return_X_y=True, shuffle=True, random_state=9487)
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

from sklearn.decomposition import PCA

# https://tgmstat.wordpress.com/2013/11/28/computing-and-visualizing-pca-in-r/

df = pd.read_csv("data/machine_learning4_iris.csv")

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

df["PC1"] = PC[:, 0]
df["PC2"] = PC[:, 1]

ax = sns.pairplot(df, hue="species")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Manifold(岐管, 流形) learning: non-linear dimension reduction

# Pairwise distance between European cities

url = "data/machine_learning4_eurodist.csv"
df = pd.read_csv(url)

print(df.iloc[:5, :5])

city = df["city"]
D = np.array(df.iloc[:, 1:])  # Distance matrix

# Arbitrary choice of K=2 components
from sklearn.manifold import MDS

mds = MDS(
    dissimilarity="precomputed",
    n_components=2,
    random_state=9487,
    max_iter=3000,
    eps=1e-9,
)
X = mds.fit_transform(D)

# Recover coordinates of the cities in Euclidean referential whose orientation is arbitrary:

from sklearn import metrics

Deuclidean = metrics.pairwise.pairwise_distances(X, metric="euclidean")
print(np.round(Deuclidean[:5, :5]))

# Plot: apply some rotation and flip
theta = 80 * np.pi / 180.0
rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
Xr = np.dot(X, rot)
# flip x
Xr[:, 0] *= -1

plt.scatter(Xr[:, 0], Xr[:, 1])

for i in range(len(city)):
    plt.text(Xr[i, 0], Xr[i, 1], city[i])
plt.axis("equal")

plt.show()

print("------------------------------------------------------------")  # 60個

k_range = range(1, min(5, D.shape[0] - 1))
stress = [
    MDS(
        dissimilarity="precomputed",
        n_components=k,
        random_state=9487,
        max_iter=300,
        eps=1e-9,
    )
    .fit(D)
    .stress_
    for k in k_range
]

print(stress)
plt.plot(k_range, stress)
plt.xlabel("k")
plt.ylabel("stress")

plt.show()

print("------------------------------------------------------------")  # 60個

print("Dataset S curve")

from mpl_toolkits.mplot3d import Axes3D
from sklearn import manifold

X, color = datasets.make_s_curve(1000, random_state=9487)

# 沒有畫出來
# plt.show()

# Isomap

isomap = manifold.Isomap(n_neighbors=10, n_components=2)
X_isomap = isomap.fit_transform(X)

print("t-SNE")

tsne = manifold.TSNE(n_components=2, init="pca", random_state=9487)
X_tsne = tsne.fit_transform(X)

fig = plt.figure(figsize=(15, 5))
plt.suptitle("Manifold Learning", fontsize=14)

ax = fig.add_subplot(131, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)
ax.view_init(4, -72)
plt.title('2D "S shape" manifold in 3D')

ax = fig.add_subplot(132)
plt.scatter(X_isomap[:, 0], X_isomap[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("Isomap")
plt.xlabel("First component")
plt.ylabel("Second component")

ax = fig.add_subplot(133)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("t-SNE")
plt.xlabel("First component")
plt.ylabel("Second component")
plt.axis("tight")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# MDS
from sklearn.decomposition import PCA
from sklearn.manifold import MDS

df = pd.read_csv("data/machine_learning4_iris.csv")

X = np.asarray(df.iloc[:, :4])
X -= np.mean(X, axis=0)
X /= np.std(X, axis=0, ddof=1)

from sklearn import metrics

D = metrics.pairwise.pairwise_distances(X, metric="euclidean")

stress = [
    MDS(
        dissimilarity="precomputed",
        n_components=k,
        random_state=42,
        max_iter=300,
        eps=1e-9,
    )
    .fit(D)
    .stress_
    for k in range(1, X.shape[1] + 1)
]

print("Stress", stress)
plt.plot(range(1, 5), stress)

K = 2
mds = MDS(
    dissimilarity="precomputed", n_components=K, random_state=42, max_iter=300, eps=1e-9
)
Xmds = mds.fit_transform(D)

pca = PCA(n_components=K)
pca.fit(X)
PC = pca.transform(X)

print("Correlation between PCA and MDS")
cor = [
    np.corrcoef(Xmds[:, j], PC[:, j])[0, 1]
    for j in range(min(Xmds.shape[1], PC.shape[1]))
]
print(cor)


sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from matplotlib.ticker import NullFormatter
from sklearn import manifold
from time import time

n_samples = 300
n_components = 2
(fig, subplots) = plt.subplots(3, 5, figsize=(15, 8))
perplexities = [5, 30, 50, 100]

X, y = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05)

red = y == 0
green = y == 1

ax = subplots[0][0]
ax.scatter(X[red, 0], X[red, 1], c="r")
ax.scatter(X[green, 0], X[green, 1], c="g")
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")

for i, perplexity in enumerate(perplexities):
    ax = subplots[0][i + 1]

    t0 = time()
    tsne = manifold.TSNE(
        n_components=n_components, init="random", random_state=0, perplexity=perplexity
    )
    Y = tsne.fit_transform(X)
    t1 = time()
    print("circles, perplexity=%d in %.2g sec" % (perplexity, t1 - t0))
    ax.set_title("Perplexity=%d" % perplexity)
    ax.scatter(Y[red, 0], Y[red, 1], c="r")
    ax.scatter(Y[green, 0], Y[green, 1], c="g")
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    ax.axis("tight")

# Another example using s-curve
X, color = datasets.make_s_curve(n_samples, random_state=0)

ax = subplots[1][0]
ax.scatter(X[:, 0], X[:, 2], c=color)
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())

for i, perplexity in enumerate(perplexities):
    ax = subplots[1][i + 1]

    t0 = time()
    tsne = manifold.TSNE(
        n_components=n_components, init="random", random_state=0, perplexity=perplexity
    )
    Y = tsne.fit_transform(X)
    t1 = time()
    print("S-curve, perplexity=%d in %.2g sec" % (perplexity, t1 - t0))

    ax.set_title("Perplexity=%d" % perplexity)
    ax.scatter(Y[:, 0], Y[:, 1], c=color)
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    ax.axis("tight")


# Another example using a 2D uniform grid
x = np.linspace(0, 1, int(np.sqrt(n_samples)))
xx, yy = np.meshgrid(x, x)
X = np.hstack(
    [
        xx.ravel().reshape(-1, 1),
        yy.ravel().reshape(-1, 1),
    ]
)
color = xx.ravel()
ax = subplots[2][0]
ax.scatter(X[:, 0], X[:, 1], c=color)
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())

for i, perplexity in enumerate(perplexities):
    ax = subplots[2][i + 1]

    t0 = time()
    tsne = manifold.TSNE(
        n_components=n_components, init="random", random_state=0, perplexity=perplexity
    )
    Y = tsne.fit_transform(X)
    t1 = time()
    print("uniform grid, perplexity=%d in %.2g sec" % (perplexity, t1 - t0))

    ax.set_title("Perplexity=%d" % perplexity)
    ax.scatter(Y[:, 0], Y[:, 1], c=color)
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    ax.axis("tight")


plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Ensemble learning: bagging, boosting and stacking

# Bagged Decision Trees for Classification

import pandas
from sklearn import model_selection
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pandas.read_csv(
    "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv",
    names=names,
)

array = dataframe.values
x = array[:, 0:8]
y = array[:, 8]
max_features = 3

kfold = model_selection.KFold(n_splits=10)

rf = DecisionTreeClassifier(max_features=max_features)

num_trees = 100

# model = BaggingClassifier(base_estimator=rf, n_estimators=num_trees, random_state=2020)
model = BaggingClassifier(rf, n_estimators=num_trees, random_state=2020)
results = model_selection.cross_val_score(model, x, y, cv=kfold)
print("Accuracy: %0.2f (+/- %0.2f)" % (results.mean(), results.std()))

# Random Forest Classification

import pandas
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier

names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pandas.read_csv(
    "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv",
    names=names,
)

array = dataframe.values
x = array[:, 0:8]
y = array[:, 8]

kfold = model_selection.KFold(n_splits=10)

rf = DecisionTreeClassifier()
num_trees = 100
max_features = 3

kfold = model_selection.KFold(n_splits=10)
model = RandomForestClassifier(n_estimators=num_trees, max_features=max_features)
results = model_selection.cross_val_score(model, x, y, cv=kfold)
print("Accuracy: %0.2f (+/- %0.2f)" % (results.mean(), results.std()))

print("------------------------------")  # 30個

# Boosting

# Adaboost Classifier

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

breast_cancer = load_breast_cancer()
x = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
y = pd.Categorical.from_codes(breast_cancer.target, breast_cancer.target_names)
# Transforming string Target to an int
encoder = LabelEncoder()
binary_encoded_y = pd.Series(encoder.fit_transform(y))

# Train Test Split
train_x, test_x, train_y, test_y = train_test_split(x, binary_encoded_y, random_state=1)
clf_boosting = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), n_estimators=200)
clf_boosting.fit(train_x, train_y)
predictions = clf_boosting.predict(test_x)
print(
    "For Boosting : F1 Score {}, Accuracy {}".format(
        round(f1_score(test_y, predictions), 2),
        round(accuracy_score(test_y, predictions), 2),
    )
)

# Random Forest as a bagging classifier

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier

breast_cancer = load_breast_cancer()
x = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
y = pd.Categorical.from_codes(breast_cancer.target, breast_cancer.target_names)
# Transforming string Target to an int
encoder = LabelEncoder()
binary_encoded_y = pd.Series(encoder.fit_transform(y))

# Train Test Split
train_x, test_x, train_y, test_y = train_test_split(x, binary_encoded_y, random_state=1)
clf_bagging = RandomForestClassifier(n_estimators=200, max_depth=1)
clf_bagging.fit(train_x, train_y)
predictions = clf_bagging.predict(test_x)
print(
    "For Bagging : F1 Score {}, Accuracy {}".format(
        round(f1_score(test_y, predictions), 2),
        round(accuracy_score(test_y, predictions), 2),
    )
)

print("------------------------------")  # 30個

# Stacking

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

breast_cancer = load_breast_cancer()
x = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
y = pd.Categorical.from_codes(breast_cancer.target, breast_cancer.target_names)

# Transforming string Target to an int
encoder = LabelEncoder()
binary_encoded_y = pd.Series(encoder.fit_transform(y))

# Train Test Split
train_x, test_x, train_y, test_y = train_test_split(x, binary_encoded_y)

boosting_clf_ada_boost = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1), n_estimators=3
)
bagging_clf_rf = RandomForestClassifier(
    n_estimators=200, max_depth=1, random_state=2020
)


clf_rf = RandomForestClassifier(n_estimators=200, max_depth=1, random_state=2020)
clf_ada_boost = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1, random_state=2020), n_estimators=3
)

clf_logistic_reg = LogisticRegression(solver="liblinear", random_state=2020)


# Customizing and Exception message
class NumberOfClassifierException(Exception):
    pass


# Creating a stacking class
class Stacking:

    """
    This is a test class for stacking !
    Please fill Free to change it to fit your needs
    We suppose that at least the First N-1 Classifiers have
    a predict_proba function.
    """

    def __init__(self, classifiers):
        if len(classifiers) < 2:
            raise numberOfClassifierException(
                "You must fit your classifier with 2 classifiers at least"
            )
        else:
            self._classifiers = classifiers

    def fit(self, data_x, data_y):
        stacked_data_x = data_x.copy()
        for classfier in self._classifiers[:-1]:
            classfier.fit(data_x, data_y)
            stacked_data_x = np.column_stack(
                (stacked_data_x, classfier.predict_proba(data_x))
            )

        last_classifier = self._classifiers[-1]
        last_classifier.fit(stacked_data_x, data_y)

    def predict(self, data_x):
        stacked_data_x = data_x.copy()
        for classfier in self._classifiers[:-1]:
            prob_predictions = classfier.predict_proba(data_x)
            stacked_data_x = np.column_stack((stacked_data_x, prob_predictions))

        last_classifier = self._classifiers[-1]
        return last_classifier.predict(stacked_data_x)


bagging_clf_rf.fit(train_x, train_y)
boosting_clf_ada_boost.fit(train_x, train_y)

classifers_list = [clf_rf, clf_ada_boost, clf_logistic_reg]
clf_stacking = Stacking(classifers_list)
clf_stacking.fit(train_x, train_y)

predictions_bagging = bagging_clf_rf.predict(test_x)
predictions_boosting = boosting_clf_ada_boost.predict(test_x)
predictions_stacking = clf_stacking.predict(test_x)

print(
    "For Bagging : F1 Score {}, Accuracy {}".format(
        round(f1_score(test_y, predictions_bagging), 2),
        round(accuracy_score(test_y, predictions_bagging), 2),
    )
)
print(
    "For Boosting : F1 Score {}, Accuracy {}".format(
        round(f1_score(test_y, predictions_boosting), 2),
        round(accuracy_score(test_y, predictions_boosting), 2),
    )
)
print(
    "For Stacking : F1 Score {}, Accuracy {}".format(
        round(f1_score(test_y, predictions_stacking), 2),
        round(accuracy_score(test_y, predictions_stacking), 2),
    )
)

"""
Comparaison
Metric 	Bagging 	Boosting 	Stacking
Accuracy 	0.90 	0.94 	0.98
F1-Score 	0.88 	0.93 	0.98
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Scikit-learn processing pipelines

# Encoding categorical features

import warnings

warnings.filterwarnings("once")

print(pd.get_dummies(["A", "B", "C", "A", "B", "D"]))

# Standardization of input features

from sklearn import linear_model as lm
from sklearn import preprocessing

# dataset
n_samples, n_features, n_features_info = 100, 5, 3
X = np.random.randn(n_samples, n_features)
beta = np.zeros(n_features)
beta[:n_features_info] = 1
Xbeta = np.dot(X, beta)
eps = np.random.randn(n_samples)
y = Xbeta + eps

X[:, 0] *= 1e6  # inflate the first feature
X[:, 1] += 1e6  # bias the second feature
y = 100 * y + 1000  # bias and scale the output

print("== Linear regression: scaling is not required ==")
model = lm.LinearRegression()
model.fit(X, y)
print("Coefficients:", model.coef_, model.intercept_)
print("Test R2:%.2f" % cross_val_score(estimator=model, X=X, y=y, cv=5).mean())

print("== Lasso without scaling ==")
model = lm.LassoCV(cv=3)
model.fit(X, y)
print("Coefficients:", model.coef_, model.intercept_)
print("Test R2:%.2f" % cross_val_score(estimator=model, X=X, y=y, cv=5).mean())

print("== Lasso with scaling ==")
model = lm.LassoCV(cv=3)
scaler = preprocessing.StandardScaler()
Xc = scaler.fit(X).transform(X)
model.fit(Xc, y)
print("Coefficients:", model.coef_, model.intercept_)
print("Test R2:%.2f" % cross_val_score(estimator=model, X=Xc, y=y, cv=5).mean())

# Scikit-learn pipelines

# Standardization of input features

from sklearn import preprocessing
from sklearn.pipeline import make_pipeline

model = make_pipeline(preprocessing.StandardScaler(), lm.LassoCV(cv=3))

# or
from sklearn.pipeline import Pipeline

model = Pipeline(
    [("standardscaler", preprocessing.StandardScaler()), ("lassocv", lm.LassoCV(cv=3))]
)

scores = cross_val_score(estimator=model, X=X, y=y, cv=5)
print("Test  r2:%.2f" % scores.mean())

# Features selection

from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.pipeline import Pipeline

n_samples, n_features, n_features_info = 100, 100, 3
X = np.random.randn(n_samples, n_features)
beta = np.zeros(n_features)
beta[:n_features_info] = 1
Xbeta = np.dot(X, beta)
eps = np.random.randn(n_samples)
y = Xbeta + eps

X[:, 0] *= 1e6  # inflate the first feature
X[:, 1] += 1e6  # bias the second feature
y = 100 * y + 1000  # bias and scale the output

model = Pipeline(
    [("anova", SelectKBest(f_regression, k=3)), ("lm", lm.LinearRegression())]
)
scores = cross_val_score(estimator=model, X=X, y=y, cv=5)
print("Anova filter + linear regression, test  r2:%.2f" % scores.mean())

from sklearn.pipeline import Pipeline

model = Pipeline(
    [("standardscaler", preprocessing.StandardScaler()), ("lassocv", lm.LassoCV(cv=3))]
)
scores = cross_val_score(estimator=model, X=X, y=y, cv=5)
print("Standardize + Lasso, test  r2:%.2f" % scores.mean())

# Regression pipelines with CV for parameters selection

from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

# Datasets
n_samples, n_features, noise_sd = 100, 100, 20
X, y, coef = datasets.make_regression(
    n_samples=n_samples,
    n_features=n_features,
    noise=noise_sd,
    n_informative=5,
    random_state=42,
    coef=True,
)

# Use this to tune the noise parameter such that snr < 5
print("SNR:", np.std(np.dot(X, coef)) / noise_sd)

print("=============================")
print("== Basic linear regression ==")
print("=============================")

scores = cross_val_score(estimator=lm.LinearRegression(), X=X, y=y, cv=5)
print("Test  r2:%.2f" % scores.mean())

print("==============================================")
print("== Scaler + anova filter + ridge regression ==")
print("==============================================")

anova_ridge = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        ("selectkbest", SelectKBest(f_regression)),
        ("ridge", lm.Ridge()),
    ]
)
param_grid = {
    "selectkbest__k": np.arange(10, 110, 10),
    "ridge__alpha": [0.001, 0.01, 0.1, 1, 10, 100],
}

# Expect execution in ipython, for python remove the %time
print("----------------------------")
print("-- Parallelize inner loop --")
print("----------------------------")

anova_ridge_cv = GridSearchCV(anova_ridge, cv=5, param_grid=param_grid, n_jobs=-1)
cores = cross_val_score(estimator=anova_ridge_cv, X=X, y=y, cv=5)
print("Test r2:%.2f" % scores.mean())

print("----------------------------")
print("-- Parallelize outer loop --")
print("----------------------------")

anova_ridge_cv = GridSearchCV(anova_ridge, cv=5, param_grid=param_grid)
scores = cross_val_score(estimator=anova_ridge_cv, X=X, y=y, cv=5, n_jobs=-1)
print("Test r2:%.2f" % scores.mean())


print("=====================================")
print("== Scaler + Elastic-net regression ==")
print("=====================================")

alphas = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
l1_ratio = [0.1, 0.5, 0.9]

print("----------------------------")
print("-- Parallelize outer loop --")
print("----------------------------")

enet = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        ("enet", lm.ElasticNet(max_iter=10000)),
    ]
)
param_grid = {"enet__alpha": alphas, "enet__l1_ratio": l1_ratio}
enet_cv = GridSearchCV(enet, cv=5, param_grid=param_grid)
scores = cross_val_score(estimator=enet_cv, X=X, y=y, cv=5, n_jobs=-1)
print("Test r2:%.2f" % scores.mean())

print("-----------------------------------------------")
print("-- Parallelize outer loop + built-in CV      --")
print("-- Remark: scaler is only done on outer loop --")
print("-----------------------------------------------")

enet_cv = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        (
            "enet",
            lm.ElasticNetCV(max_iter=10000, l1_ratio=l1_ratio, alphas=alphas, cv=3),
        ),
    ]
)

scores = cross_val_score(estimator=enet_cv, X=X, y=y, cv=5)
print("Test r2:%.2f" % scores.mean())


# Classification pipelines with CV for parameters selection

from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

# Datasets
n_samples, n_features, noise_sd = 100, 100, 20
X, y = datasets.make_classification(
    n_samples=n_samples, n_features=n_features, n_informative=5, random_state=42
)


def balanced_acc(estimator, X, y, **kwargs):
    # Balanced acuracy scorer
    return metrics.recall_score(y, estimator.predict(X), average=None).mean()


print("=============================")
print("== Basic logistic regression ==")
print("=============================")

scores = cross_val_score(
    estimator=lm.LogisticRegression(C=1e8, class_weight="balanced", solver="lbfgs"),
    X=X,
    y=y,
    cv=5,
    scoring=balanced_acc,
)
print("Test  bACC:%.2f" % scores.mean())

print("=======================================================")
print("== Scaler + anova filter + ridge logistic regression ==")
print("=======================================================")

anova_ridge = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        ("selectkbest", SelectKBest(f_classif)),
        (
            "ridge",
            lm.LogisticRegression(
                penalty="l2", class_weight="balanced", solver="lbfgs"
            ),
        ),
    ]
)
param_grid = {
    "selectkbest__k": np.arange(10, 110, 10),
    "ridge__C": [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000],
}


# Expect execution in ipython, for python remove the %time
print("----------------------------")
print("-- Parallelize inner loop --")
print("----------------------------")

anova_ridge_cv = GridSearchCV(
    anova_ridge, cv=5, param_grid=param_grid, scoring=balanced_acc, n_jobs=-1
)
scores = cross_val_score(estimator=anova_ridge_cv, X=X, y=y, cv=5, scoring=balanced_acc)
print("Test bACC:%.2f" % scores.mean())

print("----------------------------")
print("-- Parallelize outer loop --")
print("----------------------------")

anova_ridge_cv = GridSearchCV(
    anova_ridge, cv=5, param_grid=param_grid, scoring=balanced_acc
)
scores = cross_val_score(
    estimator=anova_ridge_cv, X=X, y=y, cv=5, scoring=balanced_acc, n_jobs=-1
)
print("Test bACC:%.2f" % scores.mean())


print("========================================")
print("== Scaler + lasso logistic regression ==")
print("========================================")

Cs = np.array([0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000])
alphas = 1 / Cs
l1_ratio = [0.1, 0.5, 0.9]

print("----------------------------")
print("-- Parallelize outer loop --")
print("----------------------------")

lasso = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        ("lasso", lm.LogisticRegression(penalty="l1", class_weight="balanced")),
    ]
)
param_grid = {"lasso__C": Cs}
enet_cv = GridSearchCV(lasso, cv=5, param_grid=param_grid, scoring=balanced_acc)
""" NG
scores = cross_val_score(estimator=enet_cv, X=X, y=y, cv=5,\
                               scoring=balanced_acc, n_jobs=-1)
print("Test bACC:%.2f" % scores.mean())
"""

print("-----------------------------------------------")
print("-- Parallelize outer loop + built-in CV      --")
print("-- Remark: scaler is only done on outer loop --")
print("-----------------------------------------------")

lasso_cv = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        ("lasso", lm.LogisticRegressionCV(Cs=Cs, scoring=balanced_acc)),
    ]
)

scores = cross_val_score(estimator=lasso_cv, X=X, y=y, cv=5)
print("Test bACC:%.2f" % scores.mean())


print("=============================================")
print("== Scaler + Elasticnet logistic regression ==")
print("=============================================")

print("----------------------------")
print("-- Parallelize outer loop --")
print("----------------------------")

enet = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        (
            "enet",
            lm.SGDClassifier(
                loss="log",
                penalty="elasticnet",
                alpha=0.0001,
                l1_ratio=0.15,
                class_weight="balanced",
            ),
        ),
    ]
)

param_grid = {"enet__alpha": alphas, "enet__l1_ratio": l1_ratio}

enet_cv = GridSearchCV(enet, cv=5, param_grid=param_grid, scoring=balanced_acc)
""" NG
scores = cross_val_score(estimator=enet_cv, X=X, y=y, cv=5,\
    scoring=balanced_acc, n_jobs=-1)
print("Test bACC:%.2f" % scores.mean())
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Resampling methods
==================
"""
from sklearn.model_selection import KFold
from sklearn.model_selection import PredefinedSplit
from sklearn.model_selection import GridSearchCV

X, y = datasets.make_regression(
    n_samples=100, n_features=100, n_informative=10, random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, shuffle=True, random_state=42
)

mod = lm.Ridge(alpha=10)

mod.fit(X_train, y_train)

y_pred_test = mod.predict(X_test)
print("Test R2: %.2f" % metrics.r2_score(y_test, y_pred_test))

train_idx, validation_idx = train_test_split(
    np.arange(X_train.shape[0]), test_size=0.25, shuffle=True, random_state=42
)

split_inner = PredefinedSplit(test_fold=validation_idx)
print("Train set size: %i" % X_train[train_idx].shape[0])
print("Validation set size: %i" % X_train[validation_idx].shape[0])
print("Test set size: %i" % X_test.shape[0])

lm_cv = GridSearchCV(
    lm.Ridge(), {"alpha": 10.0 ** np.arange(-3, 3)}, cv=split_inner, n_jobs=5
)

# Fit, indluding model selection with internal Train/validation split
lm_cv.fit(X_train, y_train)

# Predict
y_pred_test = lm_cv.predict(X_test)
print("Test R2: %.2f" % metrics.r2_score(y_test, y_pred_test))

from sklearn.model_selection import KFold

estimator = lm.Ridge(alpha=10)

cv = KFold(n_splits=5, shuffle=True, random_state=42)
r2_train, r2_test = list(), list()

for train, test in cv.split(X):
    estimator.fit(X[train, :], y[train])
    r2_train.append(metrics.r2_score(y[train], estimator.predict(X[train, :])))
    r2_test.append(metrics.r2_score(y[test], estimator.predict(X[test, :])))

print("Train r2:%.2f" % np.mean(r2_train))
print("Test  r2:%.2f" % np.mean(r2_test))

scores = cross_val_score(estimator=estimator, X=X, y=y, cv=5)
print("Test  r2:%.2f" % scores.mean())

cv = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(estimator=estimator, X=X, y=y, cv=cv)
print("Test  r2:%.2f" % scores.mean())

from sklearn.model_selection import cross_validate

scores = cross_validate(
    estimator=mod, X=X, y=y, cv=cv, scoring=["r2", "neg_mean_absolute_error"]
)

print(
    "Test R2:%.2f; MAE:%.2f"
    % (scores["test_r2"].mean(), -scores["test_neg_mean_absolute_error"].mean())
)

from sklearn.model_selection import StratifiedKFold

X, y = datasets.make_classification(
    n_samples=100, n_features=100, shuffle=True, n_informative=10, random_state=42
)

mod = lm.LogisticRegression(C=1, solver="lbfgs")

cv = StratifiedKFold(n_splits=5)

# Lists to store scores by folds (for macro measure only)
bacc, auc = [], []

for train, test in cv.split(X, y):
    mod.fit(X[train, :], y[train])
    bacc.append(metrics.roc_auc_score(y[test], mod.decision_function(X[test, :])))
    auc.append(metrics.balanced_accuracy_score(y[test], mod.predict(X[test, :])))

print("Test AUC:%.2f; bACC:%.2f" % (np.mean(bacc), np.mean(auc)))


# %%
# `cross_val_score()`: single metric

scores = cross_val_score(estimator=mod, X=X, y=y, cv=5)

print("Test  ACC:%.2f" % scores.mean())


# %%
# Provide your own CV and score
def balanced_acc(estimator, X, y, **kwargs):
    """Balanced acuracy scorer."""
    return metrics.recall_score(y, estimator.predict(X), average=None).mean()


scores = cross_val_score(estimator=mod, X=X, y=y, cv=cv, scoring=balanced_acc)
print("Test  bACC:%.2f" % scores.mean())


# %%
# `cross_validate()`: multi metric, + time, etc.

from sklearn.model_selection import cross_validate

scores = cross_validate(
    estimator=mod, X=X, y=y, cv=cv, scoring=["balanced_accuracy", "roc_auc"]
)

print(
    "Test AUC:%.2f; bACC:%.2f"
    % (scores["test_roc_auc"].mean(), scores["test_balanced_accuracy"].mean())
)


# Outer split:
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, shuffle=True, random_state=42
)

cv_inner = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Cross-validation for model selection
lm_cv = GridSearchCV(
    lm.LogisticRegression(), {"C": 10.0 ** np.arange(-3, 3)}, cv=cv_inner, n_jobs=5
)

# Fit, indluding model selection with internal CV
lm_cv.fit(X_train, y_train)

# Predict
y_pred_test = lm_cv.predict(X_test)
print("Test bACC: %.2f" % metrics.balanced_accuracy_score(y_test, y_pred_test))


# %%
# Cross-validation for both model (outer) evaluation and model (inner) selection
# ------------------------------------------------------------------------------

cv_outer = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_inner = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Cross-validation for model (inner) selection
lm_cv = GridSearchCV(
    lm.Ridge(), {"alpha": 10.0 ** np.arange(-3, 3)}, cv=cv_inner, n_jobs=5
)

# Cross-validation for model (outer) evaluation
scores = cross_validate(
    estimator=mod, X=X, y=y, cv=cv_outer, scoring=["balanced_accuracy", "roc_auc"]
)

print(
    "Test AUC:%.2f; bACC:%.2f, Time: %.2fs"
    % (
        scores["test_roc_auc"].mean(),
        scores["test_balanced_accuracy"].mean(),
        scores["fit_time"].sum(),
    )
)

# %%
# Models with built-in cross-validation
# --------------------------------------
#
# Let sklearn select the best parameters over a default grid.
#
# **Classification**

print("== Logistic Ridge (L2 penalty) ==")
mod_cv = lm.LogisticRegressionCV(
    class_weight="balanced", scoring="balanced_accuracy", n_jobs=-1, cv=5
)
scores = cross_val_score(estimator=mod_cv, X=X, y=y, cv=5)
print("Test  ACC:%.2f" % scores.mean())

# %%
# **Regression**

X, y, coef = datasets.make_regression(
    n_samples=50, n_features=100, noise=10, n_informative=2, random_state=42, coef=True
)

print("== Ridge (L2 penalty) ==")
model = lm.RidgeCV(cv=3)
scores = cross_val_score(estimator=model, X=X, y=y, cv=5)
print("Test  r2:%.2f" % scores.mean())

print("== Lasso (L1 penalty) ==")
model = lm.LassoCV(n_jobs=-1, cv=3)
scores = cross_val_score(estimator=model, X=X, y=y, cv=5)
print("Test  r2:%.2f" % scores.mean())

print("== ElasticNet (L1 penalty) ==")
model = lm.ElasticNetCV(l1_ratio=[0.1, 0.5, 0.9], n_jobs=-1, cv=3)
scores = cross_val_score(estimator=model, X=X, y=y, cv=5)
print("Test  r2:%.2f" % scores.mean())

# Regression dataset where first 2 features are predictives
np.random.seed(0)
n_features = 5
n_features_info = 2
n_samples = 100
X = np.random.randn(100, 5)
beta = np.zeros(n_features)
beta[:n_features_info] = 1
Xbeta = np.dot(X, beta)
eps = np.random.randn(n_samples)
y = Xbeta + eps

# %%
# Random permutations
# -------------------

# Fit model on all data (!! risk of overfit)
model = lm.RidgeCV()
model.fit(X, y)
print("Coefficients on all data:")
print(model.coef_)

# Random permutation loop
nperm = 1000  # !! Should be at least 1000 (to assess a p-value at 1%)
scores_names = ["r2"]
scores_perm = np.zeros((nperm + 1, len(scores_names)))
coefs_perm = np.zeros((nperm + 1, X.shape[1]))

scores_perm[0, :] = metrics.r2_score(y, model.predict(X))
coefs_perm[0, :] = model.coef_

orig_all = np.arange(X.shape[0])
for perm_i in range(1, nperm + 1):
    model.fit(X, np.random.permutation(y))
    y_pred = model.predict(X).ravel()
    scores_perm[perm_i, :] = metrics.r2_score(y, y_pred)
    coefs_perm[perm_i, :] = model.coef_

# One-tailed empirical p-value
pval_pred_perm = np.sum(scores_perm >= scores_perm[0]) / scores_perm.shape[0]
pval_coef_perm = np.sum(coefs_perm >= coefs_perm[0, :], axis=0) / coefs_perm.shape[0]

print("R2 p-value: %.3f" % pval_pred_perm)
print("Coeficients p-values:", np.round(pval_coef_perm, 3))

# %%
# Compute p-values corrected for multiple comparisons using FWER max-T
# (Westfall and Young, 1993) procedure.

pval_coef_perm_tmax = (
    np.array(
        [
            np.sum(coefs_perm.max(axis=1) >= coefs_perm[0, j])
            for j in range(coefs_perm.shape[1])
        ]
    )
    / coefs_perm.shape[0]
)
print("P-values with FWER (Westfall and Young) correction")
print(pval_coef_perm_tmax)

# %%
# Plot distribution of third coefficient under null-hypothesis
# Coeffitients 0 and 1 are significantly different from 0.
#


def hist_pvalue(perms, ax, name):
    """Plot statistic distribution as histogram.

    Paramters
    ---------
    perms: 1d array, statistics under the null hypothesis.
           perms[0] is the true statistic .
    """
    # Re-weight to obtain distribution
    pval = np.sum(perms >= perms[0]) / perms.shape[0]
    weights = np.ones(perms.shape[0]) / perms.shape[0]
    ax.hist(
        [perms[perms >= perms[0]], perms],
        histtype="stepfilled",
        bins=100,
        label="p-val<%.3f" % pval,
        weights=[weights[perms >= perms[0]], weights],
    )
    ax.axvline(x=perms[0], color="k", linewidth=2)  # , label="observed statistic")
    ax.set_ylabel(name)
    ax.legend()
    return ax


n_coef = coefs_perm.shape[1]
fig, axes = plt.subplots(n_coef, 1, figsize=(12, 9))
for i in range(n_coef):
    hist_pvalue(coefs_perm[:, i], axes[i], str(i))

_ = axes[-1].set_xlabel("Coefficient distribution under null hypothesis")


# Bootstrap loop
nboot = 100  # !! Should be at least 1000
scores_names = ["r2"]
scores_boot = np.zeros((nboot, len(scores_names)))
coefs_boot = np.zeros((nboot, X.shape[1]))

orig_all = np.arange(X.shape[0])
for boot_i in range(nboot):
    boot_tr = np.random.choice(orig_all, size=len(orig_all), replace=True)
    boot_te = np.setdiff1d(orig_all, boot_tr, assume_unique=False)
    Xtr, ytr = X[boot_tr, :], y[boot_tr]
    Xte, yte = X[boot_te, :], y[boot_te]
    model.fit(Xtr, ytr)
    y_pred = model.predict(Xte).ravel()
    scores_boot[boot_i, :] = metrics.r2_score(yte, y_pred)
    coefs_boot[boot_i, :] = model.coef_

# %%
# Compute Mean, SE, CI
# Coeffitients 0 and 1 are significantly different from 0.

scores_boot = pd.DataFrame(scores_boot, columns=scores_names)
scores_stat = scores_boot.describe(percentiles=[0.975, 0.5, 0.025])

print(
    "r-squared: Mean=%.2f, SE=%.2f, CI=(%.2f %.2f)"
    % tuple(scores_stat.loc[["mean", "std", "2.5%", "97.5%"], "r2"])
)

coefs_boot = pd.DataFrame(coefs_boot)
coefs_stat = coefs_boot.describe(percentiles=[0.975, 0.5, 0.025])
print("Coefficients distribution")
print(coefs_stat)

# Plot coefficient distribution

df = pd.DataFrame(coefs_boot)
staked = pd.melt(df, var_name="Variable", value_name="Coef. distribution")
sns.set_theme(style="whitegrid")
ax = sns.violinplot(x="Variable", y="Coef. distribution", data=staked)
_ = ax.axhline(0, ls="--", lw=2, color="black")

# Parallel computation with joblib
# --------------------------------
#
# Dataset

from sklearn.model_selection import StratifiedKFold

X, y = datasets.make_classification(
    n_samples=20, n_features=5, n_informative=2, random_state=42
)
cv = StratifiedKFold(n_splits=5)


# %%
# Use `cross_validate` function

from sklearn.model_selection import cross_validate

estimator = lm.LogisticRegression(C=1, solver="lbfgs")
cv_results = cross_validate(estimator, X, y, cv=cv, n_jobs=5)
print(np.mean(cv_results["test_score"]), cv_results["test_score"])


# %%
# Sequential computation
#
# If we want have full control of the operations performed within each fold (retrieve the models parameters, etc.). We would like to parallelize the folowing sequetial code:

# In[22]:


estimator = lm.LogisticRegression(C=1, solver="lbfgs")
y_test_pred_seq = np.zeros(len(y))  # Store predictions in the original order
coefs_seq = list()
for train, test in cv.split(X, y):
    X_train, X_test, y_train, y_test = X[train, :], X[test, :], y[train], y[test]
    estimator.fit(X_train, y_train)
    y_test_pred_seq[test] = estimator.predict(X_test)
    coefs_seq.append(estimator.coef_)

test_accs = [
    metrics.accuracy_score(y[test], y_test_pred_seq[test])
    for train, test in cv.split(X, y)
]
print(np.mean(test_accs), test_accs)
coefs_cv = np.array(coefs_seq)
print(coefs_cv)

print(coefs_cv.mean(axis=0))
print("Std Err of the coef")
print(coefs_cv.std(axis=0) / np.sqrt(coefs_cv.shape[0]))


# %%
# Parallel computation with joblib
# --------------------------------


from joblib import Parallel, delayed
from sklearn.base import is_classifier, clone


def _split_fit_predict(estimator, X, y, train, test):
    X_train, X_test, y_train, y_test = X[train, :], X[test, :], y[train], y[test]
    estimator.fit(X_train, y_train)
    return [estimator.predict(X_test), estimator.coef_]


estimator = lm.LogisticRegression(C=1, solver="lbfgs")

parallel = Parallel(n_jobs=5)
cv_ret = parallel(
    delayed(_split_fit_predict)(clone(estimator), X, y, train, test)
    for train, test in cv.split(X, y)
)

y_test_pred_cv, coefs_cv = zip(*cv_ret)

# Retrieve predictions in the original order
y_test_pred = np.zeros(len(y))
for i, (train, test) in enumerate(cv.split(X, y)):
    y_test_pred[test] = y_test_pred_cv[i]

test_accs = [
    metrics.accuracy_score(y[test], y_test_pred[test]) for train, test in cv.split(X, y)
]
print(np.mean(test_accs), test_accs)


# %%
# Test same predictions and same coeficients

assert np.all(y_test_pred == y_test_pred_seq)
assert np.allclose(np.array(coefs_cv).squeeze(), np.array(coefs_seq).squeeze())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import StratifiedKFold

X, y = datasets.make_classification(
    n_samples=100, n_features=100, n_informative=10, random_state=42
)

model = lm.LogisticRegression(C=1)
nperm = 100
scores_perm = np.zeros((nperm, 3))  # 3 scores acc, recall0, recall1

for perm in range(0, nperm):
    # perm = 0; y == yp
    # first run on non-permuted samples
    yp = y if perm == 0 else np.random.permutation(y)
    # CV loop
    y_test_pred = np.zeros(len(yp))
    cv = StratifiedKFold(5)
    for train, test in cv.split(X, y):
        X_train, X_test, y_train, y_test = X[train, :], X[test, :], yp[train], yp[test]
        model.fit(X_train, y_train)
        y_test_pred[test] = model.predict(X_test)
    scores_perm[perm, 0] = metrics.accuracy_score(yp, y_test_pred)
    scores_perm[perm, [1, 2]] = metrics.recall_score(yp, y_test_pred, average=None)

# Empirical permutation based p-values
pval = np.sum(scores_perm >= scores_perm[0, :], axis=0) / nperm

print(
    "ACC:%.2f(P=%.3f); SPC:%.2f(P=%.3f); SEN:%.2f(P=%.3f)"
    % (
        scores_perm[0, 0],
        pval[0],
        scores_perm[0, 1],
        pval[1],
        scores_perm[0, 2],
        pval[2],
    )
)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
