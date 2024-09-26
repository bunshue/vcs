"""
Scikit-learn 詳解與企業應用_機器學習最佳入門與實戰

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
'''
#SelectFromModel

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectFromModel
from sklearn.svm import SVC

#載入資料集

X, y = datasets.load_iris(return_X_y=True)
cc = X.shape
print(cc)

#SelectFromModel特徵選取

svc = SVC(kernel="linear", C=1)
clf = SelectFromModel(estimator=svc, threshold='mean')
X_new = clf.fit_transform(X, y)
cc = X_new.shape
print(cc)

# 特徵是否被選取
cc = clf.get_support()
print(cc)

#3. 不須進行特徵工程

#4. 資料分割

# 選擇2個特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

#((120, 2), (30, 2), (120,), (30,))

#特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)

# 7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#96.67%

# 混淆矩陣
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

#使用全部特徵

# 載入資料集
X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#(120, 4) (30, 4) (120,) (30,)
#93.33%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#順序特徵選取(Sequential Feature Selection)

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.svm import SVC

#載入資料集

X, y = datasets.load_iris(return_X_y=True)
cc = X.shape
print(cc)

#SFS 特徵選取
svc = SVC(kernel="linear", C=1)
clf = SequentialFeatureSelector(estimator=svc, n_features_to_select=2)
X_new = clf.fit_transform(X, y)
cc = X_new.shape
print(cc)

# 特徵是否被選取
cc = clf.get_support()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

# 選擇2個特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
X_train.shape, X_test.shape, y_train.shape, y_test.shape

#特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

#5. 選擇演算法

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

#6. 模型訓練

clf.fit(X_train_std, y_train)

#7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#86.67%

# 混淆矩陣
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

#使用全部特徵

# 載入資料集
X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#(120, 4) (30, 4) (120,) (30,)
#96.67%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#實現PCA演算法

#建立測試資料

import numpy as np

# 固定隨機種子
np.random.seed(2342347) 

# 第一個類別
mu_vec1 = np.array([0,0,0]) # 平均數
cov_mat1 = np.array([[1,0,0],[0,1,0],[0,0,1]]) # 共變異矩陣
class1_sample = np.random.multivariate_normal(mu_vec1, cov_mat1, 20).T

# 第二個類別
mu_vec2 = np.array([1,1,1]) # 平均數
cov_mat2 = np.array([[1,0,0],[0,1,0],[0,0,1]]) # 共變異矩陣
class2_sample = np.random.multivariate_normal(mu_vec2, cov_mat2, 20).T

cc = class1_sample.shape, class2_sample.shape
print(cc)

#繪圖

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

# 修正中文亂碼
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] 
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
plt.rcParams['legend.fontsize'] = 10   
ax.plot(class1_sample[0,:], class1_sample[1,:], class1_sample[2,:], 'o',
        markersize=8, color='blue', alpha=0.5, label='類別1')
ax.plot(class2_sample[0,:], class2_sample[1,:], class2_sample[2,:], '^', 
        markersize=8, alpha=0.5, color='red', label='類別2')

plt.title('測試資料')
ax.legend(loc='upper right')

plt.show()

#合併資料

all_samples = np.concatenate((class1_sample, class2_sample), axis=1)
cc = all_samples.shape
print(cc)

#計算共變異數矩陣(covariance matrix)

cov_mat = np.cov([all_samples[0,:],all_samples[1,:],all_samples[2,:]])
print('共變異數矩陣:\n', cov_mat)

#計算特徵向量(eigenvector)及對應的特徵值(eigenvalue, λ)

# 計算特徵值(eigenvalue)及對應的特徵向量(eigenvector)
eig_val_sc, eig_vec_sc = np.linalg.eig(cov_mat)
print('特徵向量:\n', eig_vec_sc)
print('特徵值:\n', eig_val_sc)

#繪製特徵向量

from mpl_toolkits.mplot3d import Axes3D, proj3d
from matplotlib.patches import FancyArrowPatch

# 繪製箭頭
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        return np.min(zs)
    
# 設定 3D 繪圖    
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')

# 繪製特徵向量
ax.plot(all_samples[0,:], all_samples[1,:], all_samples[2,:], 'o', 
        markersize=8, color='green', alpha=0.2)
[mean_x, mean_y, mean_z] = np.mean(all_samples, axis=1)
ax.plot([mean_x], [mean_y], [mean_z], 'o', markersize=10, color='red', 
        alpha=0.5)
for v in eig_vec_sc.T:
    a = Arrow3D([mean_x, v[0]], [mean_y, v[1]], [mean_z, v[2]], 
                mutation_scale=20, lw=3, arrowstyle="-|>", color="r")
    ax.add_artist(a)
ax.set_xlabel('x_values');ax.set_ylabel('y_values');ax.set_zlabel('z_values')

plt.show()

#合併特徵向量及特徵值，針對特徵值降冪排序，挑出前2名。

# 合併特徵向量及特徵值
eig_pairs = [(np.abs(eig_val_sc[i]), eig_vec_sc[:,i]) for i in range(len(eig_val_sc))]

# 針對特徵值降冪排序
eig_pairs.sort(key=lambda x: x[0], reverse=True)

# 挑出前2名
for i in eig_pairs[:2]:
    print(i[1])

#座標轉換矩陣

matrix_w = np.hstack((eig_pairs[0][1].reshape(3,1), eig_pairs[1][1].reshape(3,1)))
print('Matrix W:\n', matrix_w)

#原始資料乘以轉換矩陣，得到主成分

transformed = matrix_w.T.dot(all_samples)
cc = transformed.shape
print(cc)

#繪製轉換後的資料

plt.plot(transformed[0,0:20], transformed[1,0:20], 'o', 
         markersize=7, color='blue', alpha=0.5, label='class1')
plt.plot(transformed[0,20:40], transformed[1,20:40], '^', 
         markersize=7, color='red', alpha=0.5, label='class2')
plt.xlim([-4,4])
plt.ylim([-4,4])
plt.xlabel('x_values')
plt.ylabel('y_values')
plt.legend()
plt.title('Transformed samples with class labels');
plt.show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#PCA 個案實作

from sklearn import datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1. 載入資料

ds = datasets.load_wine()
df = pd.DataFrame(ds.data, columns=ds.feature_names)
cc = df.head()
print(cc)

#2. 資料清理、資料探索與分析

# 資料集說明
#print(ds.DESCR)

#3. 資料分割

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 指定X、Y
X = df.values
y = ds.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

#4. 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

#進行特徵萃取(PCA)

# PCA 函數實作
def PCA_numpy(X, X_test, no):
    cov_mat = np.cov(X.T)
    # 計算特徵值(eigenvalue)及對應的特徵向量(eigenvector)
    eigen_val, eigen_vecs = np.linalg.eig(cov_mat)
    # 合併特徵向量及特徵值
    eigen_pairs = [(np.abs(eigen_val[i]), eigen_vecs[:,i]) for i in range(len(eigen_vecs))]

    # 針對特徵值降冪排序
    eigen_pairs.sort(key=lambda x: x[0], reverse=True)

    w = eigen_pairs[0][1][:, np.newaxis]
    for i in range(1, no):
        w = np.hstack((w, eigen_pairs[i][1][:, np.newaxis]))

    # 轉換：矩陣相乘 (n, m) x (m, 2) = (n, 2)
    return X.dot(w), X_test.dot(w)

X_train_pca, X_test_pca = PCA_numpy(X_train_std, X_test_std, 2) # 取 2 個特徵
cc = X_train_pca.shape, X_test_pca.shape
print(cc)

#5. 選擇演算法

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

#6. 模型訓練

clf.fit(X_train_pca, y_train)

#7. 模型計分

# 計算準確率
y_pred = clf.predict(X_test_pca)
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#100.00%

#繪製決策邊界(Decision regions)

from matplotlib.colors import ListedColormap

def plot_decision_regions(X, y, classifier, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], 
                    y=X[y == cl, 1],
                    alpha=0.6, 
                    color=cmap(idx),
                    marker=markers[idx], 
                    label=cl)

plot_decision_regions(X_test_pca, y_test, classifier=clf)
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend(loc='lower left')
plt.tight_layout()
# plt.savefig('decision_regions.png', dpi=300)
plt.show()

#使用全部特徵

# 載入資料集
X, y = datasets.load_wine(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#(142, 13) (36, 13) (142,) (36,)
#100.00%



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個









print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()



