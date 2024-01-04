import os
import sys
import time
import random


print("------------------------------------------------------------")  # 60個
'''
import matplotlib.pyplot as plt
import numpy as np

def normal_distribution(x, mean, sigma):
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(- (x - mean)**2 / (2 * sigma**2))

x = np.linspace(0, 6, 500)
mean1 = 1
mean2 = 1
sigma1 = 0.1
sigma2 = 0.3

plt.figure(figsize=(10, 3), dpi=144)

# sub plot 1
plt.subplot(1, 2, 1)
plt.title('Gaussian Distribution for $\mu={0}, \sigma={1}$'.format(mean1, sigma1))

plt.xlim(0, 2)
plt.ylim(0, 5)
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.plot(x, normal_distribution(x, mean1, sigma1), 'r-')

# sub plot 2
plt.subplot(1, 2, 2)
plt.title('Gaussian Distribution for $\mu={0}, \sigma={1}$'.format(mean2, sigma2))

plt.xlim(0, 2)
plt.ylim(0, 5)
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.plot(x, normal_distribution(x, mean2, sigma2), 'r-')

plt.show()


print(normal_distribution(6, 5.855, np.sqrt(3.5033e-02)))


print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import numpy as np

from time import time
from sklearn.datasets import load_files

""" 缺資料
print("loading train dataset ...")
t = time()
news_train = load_files('datasets/mlcomp/379/train')
print("summary: {0} documents in {1} categories.".format(
    len(news_train.data), len(news_train.target_names)))
print("done in {0} seconds".format(time() - t))


from sklearn.feature_extraction.text import TfidfVectorizer

print("vectorizing train dataset ...")
t = time()
vectorizer = TfidfVectorizer(encoding='latin-1')
X_train = vectorizer.fit_transform((d for d in news_train.data))
print("n_samples: %d, n_features: %d" % X_train.shape)
print("number of non-zero features in sample [{0}]: {1}".format(
    news_train.filenames[0], X_train[0].getnnz()))
print("done in {0} seconds".format(time() - t))



print("------------------------------------------------------------")  # 60個

from sklearn.naive_bayes import MultinomialNB

print("traning models ...".format(time() - t))
t = time()
y_train = news_train.target
clf = MultinomialNB(alpha=0.0001)
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
print("train score: {0}".format(train_score))
print("done in {0} seconds".format(time() - t))

print("------------------------------------------------------------")  # 60個

print("loading test dataset ...")
t = time()
news_test = load_files('datasets/mlcomp/379/test')
print("summary: {0} documents in {1} categories.".format(
    len(news_test.data), len(news_test.target_names)))
print("done in {0} seconds".format(time() - t))

print("------------------------------------------------------------")  # 60個

print("vectorizing test dataset ...")
t = time()
X_test = vectorizer.transform((d for d in news_test.data))
y_test = news_test.target
print("n_samples: %d, n_features: %d" % X_test.shape)
print("number of non-zero features in sample [{0}]: {1}".format(
    news_test.filenames[0], X_test[0].getnnz()))
print("done in %fs" % (time() - t))


print("------------------------------------------------------------")  # 60個

pred = clf.predict(X_test[0])
print("predict: {0} is in category {1}".format(
    news_test.filenames[0], news_test.target_names[pred[0]]))
print("actually: {0} is in category {1}".format(
    news_test.filenames[0], news_test.target_names[news_test.target[0]]))

print("------------------------------------------------------------")  # 60個

print("predicting test dataset ...")
t = time()
pred = clf.predict(X_test)
print("done in %fs" % (time() - t))


print("------------------------------------------------------------")  # 60個

from sklearn.metrics import classification_report

print("classification report on test set for classifier:")
print(clf)
print(classification_report(y_test, pred,
                            target_names=news_test.target_names))



print("------------------------------------------------------------")  # 60個

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, pred)
print("confusion matrix:")
print(cm)

print("------------------------------------------------------------")  # 60個

# Show confusion matrix
plt.figure(figsize=(8, 8), dpi=144)
plt.title('Confusion matrix of the classifier')
ax = plt.gca()                                  
ax.spines['right'].set_color('none')            
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.matshow(cm, fignum=1, cmap='gray')
plt.colorbar()

plt.show()
"""



print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import numpy as np


dots = np.array([[1, 1.5], [2, 1.5], [3, 3.6], [4, 3.2], [5, 5.5]])

def cross_point(x0, y0):
    """
    1. line1: y = x
    2. line2: y = -x + b => x = b/2
    3. [x0, y0] is in line2 => b = x0 + y0

    => x1 = b/2 = (x0 + y0) / 2
    => y1 = x1
    """
    x1 = (x0 + y0) / 2
    return x1, x1


plt.figure(figsize=(8, 6), dpi=144)
plt.title('2-dimension to 1-dimension')

plt.xlim(0, 8)
plt.ylim(0, 6)
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.scatter(dots[:, 0], dots[:, 1], marker='s', c='b')
plt.plot([0.5, 6], [0.5, 6], '-r')
for d in dots:
    x1, y1 = cross_point(d[0], d[1])
    plt.plot([d[0], x1], [d[1], y1], '--b')
    plt.scatter(x1, y1, marker='o', c='r')
plt.annotate(r'projection point',
             xy=(x1, y1), xycoords='data',
             xytext=(x1 + 0.5, y1 - 0.5), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'vector $u^{(1)}$',
             xy=(4.5, 4.5), xycoords='data',
             xytext=(5, 4), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.show()


print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import numpy as np

print('PCA 算法模拟')

A = np.array([[3, 2000], 
              [2, 3000], 
              [4, 5000], 
              [5, 8000], 
              [1, 2000]], dtype='float')

# 数据归一化
mean = np.mean(A, axis=0)
norm = A - mean
# 数据缩放
scope = np.max(norm, axis=0) - np.min(norm, axis=0)
norm = norm / scope
print(norm)

U, S, V = np.linalg.svd(np.dot(norm.T, norm))
print(U)

U_reduce = U[:, 0].reshape(2,1)
print(U_reduce)

R = np.dot(norm, U_reduce)
print(R)

Z = np.dot(R, U_reduce.T)
print(Z)

print(np.multiply(Z, scope) + mean)

print("------------------------------------------------------------")  # 60個

print('使用 sklearn 包实现')

from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

def std_PCA(**argv):
    scaler = MinMaxScaler()
    pca = PCA(**argv)
    pipeline = Pipeline([('scaler', scaler),
                         ('pca', pca)])
    return pipeline

pca = std_PCA(n_components=1)
R2 = pca.fit_transform(A)
print(R2)

print(pca.inverse_transform(R2))

print("------------------------------------------------------------")  # 60個

print('降维及恢复示意图')

plt.figure(figsize=(8, 8), dpi=144)

plt.title('Physcial meanings of PCA')

ymin = xmin = -1
ymax = xmax = 1
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.scatter(norm[:, 0], norm[:, 1], marker='s', c='b')
plt.scatter(Z[:, 0], Z[:, 1], marker='o', c='r')
plt.arrow(0, 0, U[0][0], U[1][0], color='r', linestyle='-')
plt.arrow(0, 0, U[0][1], U[1][1], color='r', linestyle='--')
plt.annotate(r'$U_{reduce} = u^{(1)}$',
             xy=(U[0][0], U[1][0]), xycoords='data',
             xytext=(U_reduce[0][0] + 0.2, U_reduce[1][0] - 0.1), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'$u^{(2)}$',
             xy=(U[0][1], U[1][1]), xycoords='data',
             xytext=(U[0][1] + 0.2, U[1][1] - 0.1), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'raw data',
             xy=(norm[0][0], norm[0][1]), xycoords='data',
             xytext=(norm[0][0] + 0.2, norm[0][1] - 0.2), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'projected data',
             xy=(Z[0][0], Z[0][1]), xycoords='data',
             xytext=(Z[0][0] + 0.2, Z[0][1] - 0.1), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.show()
'''
print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import numpy as np

import time
import logging
from sklearn.datasets import fetch_olivetti_faces

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

data_home='datasets/'

logging.info('Start to load dataset')
faces = fetch_olivetti_faces(data_home=data_home)
logging.info('Done with load dataset')

print("------------------------------------------------------------")  # 60個

X = faces.data
y = faces.target
targets = np.unique(faces.target)
target_names = np.array(["c%d" % t for t in targets])
n_targets = target_names.shape[0]
n_samples, h, w = faces.images.shape
print('Sample count: {}\nTarget count: {}'.format(n_samples, n_targets))
print('Image size: {}x{}\nDataset shape: {}\n'.format(w, h, X.shape))


print("------------------------------------------------------------")  # 60個

def plot_gallery(images, titles, h, w, n_row=2, n_col=5):
    """显示图片阵列"""
    plt.figure(figsize=(2 * n_col, 2.2 * n_row), dpi=144)
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.01)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i])
        plt.axis('off')

n_row = 2
n_col = 6

sample_images = None
sample_titles = []
for i in range(n_targets):
    people_images = X[y==i]
    people_sample_index = np.random.randint(0, people_images.shape[0], 1)
    people_sample_image = people_images[people_sample_index, :]
    if sample_images is not None:
        sample_images = np.concatenate((sample_images, people_sample_image), axis=0)
    else:
        sample_images = people_sample_image
    sample_titles.append(target_names[i])

plot_gallery(sample_images, sample_titles, h, w, n_row, n_col)
plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=4)


from sklearn.svm import SVC

start = time.time()
print('Fitting train datasets ...')
clf = SVC(class_weight='balanced')
clf.fit(X_train, y_train)
print('Done in {0:.2f}s'.format(time.time()-start))

start = time.time()
print("Predicting test dataset ...")
y_pred = clf.predict(X_test)
print('Done in {0:.2f}s'.format(time.time()-start))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred, labels=range(n_targets))
print("confusion matrix:\n")

np.set_printoptions(threshold=sys.maxsize)
print(cm)


""" not match
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred, target_names=target_names))
"""

print("------------------------------------------------------------")  # 60個

from sklearn.decomposition import PCA

print("Exploring explained variance ratio for dataset ...")
candidate_components = range(10, 300, 30)
explained_ratios = []
start = time.time()
for c in candidate_components:
    pca = PCA(n_components=c)
    X_pca = pca.fit_transform(X)
    explained_ratios.append(np.sum(pca.explained_variance_ratio_))
print('Done in {0:.2f}s'.format(time.time()-start))



print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(10, 6), dpi=144)
plt.grid()
plt.plot(candidate_components, explained_ratios)
plt.xlabel('Number of PCA Components')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained variance ratio for PCA')
plt.yticks(np.arange(0.5, 1.05, .05))
plt.xticks(np.arange(0, 300, 20));

plt.show()

print("------------------------------------------------------------")  # 60個

def title_prefix(prefix, title):
    return "{}: {}".format(prefix, title)

n_row = 1
n_col = 5

sample_images = sample_images[0:5]
sample_titles = sample_titles[0:5]

plotting_images = sample_images
plotting_titles = [title_prefix('orig', t) for t in sample_titles]
candidate_components = [140, 75, 37, 19, 8]
for c in candidate_components:
    print("Fitting and projecting on PCA(n_components={}) ...".format(c))
    start = time.time()
    pca = PCA(n_components=c)
    pca.fit(X)
    X_sample_pca = pca.transform(sample_images)
    X_sample_inv = pca.inverse_transform(X_sample_pca)
    plotting_images = np.concatenate((plotting_images, X_sample_inv), axis=0)
    sample_title_pca = [title_prefix('{}'.format(c), t) for t in sample_titles]
    plotting_titles = np.concatenate((plotting_titles, sample_title_pca), axis=0)
    print("Done in {0:.2f}s".format(time.time() - start))

print("Plotting sample image with different number of PCA conpoments ...")
plot_gallery(plotting_images, plotting_titles, h, w,
    n_row * (len(candidate_components) + 1), n_col)

plt.show()



print("------------------------------------------------------------")  # 60個

n_components = 140

print("Fitting PCA by using training data ...")
start = time.time()
pca = PCA(n_components=n_components, svd_solver='randomized', whiten=True).fit(X_train)
print("Done in {0:.2f}s".format(time.time() - start))

print("Projecting input data for PCA ...")
start = time.time()
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print("Done in {0:.2f}s".format(time.time() - start))


from sklearn.model_selection import GridSearchCV

print("Searching the best parameters for SVC ...")
param_grid = {'C': [1, 5, 10, 50, 100],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01]}
clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid, verbose=2, n_jobs=4)
clf = clf.fit(X_train_pca, y_train)
print("Best parameters found by grid search:")
print(clf.best_params_)


start = time.time()
print("Predict test dataset ...")
y_pred = clf.best_estimator_.predict(X_test_pca)
cm = confusion_matrix(y_test, y_pred, labels=range(n_targets))
print("Done in {0:.2f}.\n".format(time.time()-start))
print("confusion matrix:")
np.set_printoptions(threshold=sys.maxsize)
print(cm)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


