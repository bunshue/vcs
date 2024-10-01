"""
iris 01

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

from sklearn.datasets import load_iris

print('iris data')

iris = load_iris()
print('特徵值：')
print(iris.data[0:3])
print('目標值：')
print(iris.target)
print('特徵名稱：')
print(iris.feature_names)
print('目標名稱：')
print(iris.target_names)

print("------------------------------------------------------------")  # 60個


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import joblib

print('save model')

iris = load_iris()
x_train , x_test , y_train , y_test = train_test_split(iris.data,iris.target,test_size=0.2)

std = StandardScaler()
x_train = std.fit_transform(x_train)
x_test = std.transform(x_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
joblib.dump(knn, 'data/iris.pkl')

print("------------------------------------------------------------")  # 60個


iris = load_iris()

x_train , x_test , y_train , y_test = train_test_split(iris.data,iris.target,test_size=0.2)
std = StandardScaler()
x_train = std.fit_transform(x_train)
x_test = std.transform(x_test)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
y_predict = knn.predict(x_test)
print('預測結果：{}'.format(y_predict))
print('準確率：{}'.format(knn.score(x_test, y_test)))

print("------------------------------------------------------------")  # 60個

""" fail
from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib

clf = svm.SVC()
iris = datasets.load_iris()
clf.fit(iris.data, iris.target)
joblib.dump(clf, "tmp3.pkl")

clf1 = joblib.load("tmp3.pkl")
print(clf1.predict(iris.data[:2]))
"""

print("------------------------------------------------------------")  # 60個


print('模型篩選特徵')

from sklearn.datasets import load_iris 
from sklearn import tree 

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
print(clf.feature_importances_)

print('------------------------------------------------------------')	#60個

print('數學方法降維')

from sklearn.decomposition import PCA
from sklearn import datasets
import seaborn as sns

iris = datasets.load_iris()
data = pd.DataFrame(iris.data, columns=['SpealLen', 'SpealWid', 
                             'PetalLen', 'PetalWid'])
mat = data.corr()
sns.heatmap(mat, annot=True, vmax=1, vmin=-1, xticklabels= True, 
            yticklabels= True, square=True, cmap="gray")

plt.show()

print('------------------------------------------------------------')	#60個

pca = PCA(n_components=2)
data1 = pca.fit_transform(data)
print(data1.shape)
print(pca.explained_variance_ratio_, 
      pca.explained_variance_ratio_.sum())
plt.scatter(data1[:,0], data1[:,1], c = np.array(iris.target), 
            cmap=plt.cm.copper)

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris=load_iris()
X = iris.data  # 獲取自變量
y = iris.target  # 獲取因變量
X_train, X_test, y_train ,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
clf = svm.SVC(C=0.8, kernel='rbf', gamma=1) # 高斯核，鬆弛度0.8
#clf = svm.SVC(C=0.5, kernel='linear') # 線性核，鬆弛度0.5
clf.fit(X_train, y_train.ravel())

print('trian pred:%.3f' %(clf.score(X_train, y_train))) # 對訓練集打分
print('test pred:%.3f' %(clf.score(X_test, y_test))) # 對測試集打分
print(clf.support_vectors_) #支持向量列表，從中看到切分邊界
print(clf.n_support_) # 每類別持向量個數

plt.plot(X_train[:,0], X_train[:,1],'o', color = '#bbbbbb')
plt.plot(clf.support_vectors_[:,0], clf.support_vectors_[:,1],'o')

plt.show()

print("------------------------------------------------------------")  # 60個

print('決策樹')

from sklearn.datasets import load_iris # 鳶尾花數據集
from sklearn.model_selection import train_test_split # 切分數據集工具
from sklearn import tree # 決策樹工具
import pydotplus # 做圖工具
import io

iris=load_iris()
X = iris.data  # 獲取自變量
y = iris.target  # 獲取因變量
X_train, X_test, y_train ,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
clf = tree.DecisionTreeClassifier(max_depth=5)
clf.fit(X_train,y_train) # 訓練模型
print("score:", clf.score(X_test,y_test)) # 模型打分
# 生成決策樹圖片
dot_data = io.StringIO()
tree.export_graphviz(clf,out_file=dot_data, 
                     feature_names=iris.feature_names,
                     filled=True,rounded=True,
                     impurity=False)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

#fail
#open('a.jpg','wb').write(graph.create_jpg()) # 保存圖片

print('------------------------------------------------------------')	#60個

print('切分數據集與交叉驗證')

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=10)
X_train,X_test=train_test_split(X,test_size=0.3,random_state=10)

print('------------------------------------------------------------')	#60個

""" some fail
from sklearn.cross_validation import KFold
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.svm import SVC

iris = load_iris()
X_train,X_test,y_train,y_test=train_test_split(iris.data,iris.target,
                                               test_size=0.3,random_state=10)
num = 5 # 5折交叉驗證
train_preds = np.zeros(X_train.shape[0]) # 用於保存預測結果
test_preds = np.zeros((X_test.shape[0], num))
kf = KFold(len(X_train), n_folds = num, shuffle=True, random_state=0)
for i, (train_index, eval_index) in enumerate(kf):
    clf = SVC(C=1, gamma=0.125, kernel='rbf')
    clf.fit(X_train[train_index], y_train[train_index])
    train_preds[eval_index] += clf.predict(X_train[eval_index])
    test_preds[:,i] = clf.predict(X_test)
print(accuracy_score(y_train, train_preds)) # 返回結果: 0.971428571429
print(test_preds.mean(axis=1))

from sklearn.model_selection import cross_val_score # python 3使用
# from sklearn.cross_validation import cross_val_score # python 2 使用
print(cross_val_score(clf, iris.data, iris.target).mean())
"""
print('------------------------------------------------------------')	#60個

print('模型調參')

# 網格搜索
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_iris

iris = load_iris()
model = SVC(random_state=1)
param_grid = {'kernel':('linear', 'rbf'), 'C':[1, 2, 4], # 制定參數範圍
              'gamma':[0.125, 0.25, 0.5 ,1, 2, 4]}
gs = GridSearchCV(estimator=model, param_grid=param_grid, scoring='accuracy', 
                  cv=10, n_jobs=-1)
gs = gs.fit(iris.data, iris.target)
y_pred = gs.predict(iris.data)  # 預測
print(gs.best_score_)
print(gs.best_params_)

print('------------------------------------------------------------')	#60個

""" some fail
from sklearn.datasets import load_iris
from sklearn.cross_validation import cross_val_score
from hyperopt import hp,STATUS_OK,Trials,fmin,tpe
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def f(params): # 定義評價函數
    t = params['type']
    del params['type']
    if t == 'svm':
        clf = SVC(**params)
    elif t == 'randomforest':
        clf = RandomForestClassifier(**params)
    else:
        return 0
    acc = cross_val_score(clf, iris.data, iris.target).mean() 
    return {'loss': -acc, 'status': STATUS_OK} # 求最小值:準確率加負號

iris=load_iris()
space = hp.choice('classifier_type', [ # 定義可選參數
    {
        'type': 'svm',
        'C': hp.uniform('C', 0, 10.0),
        'kernel': hp.choice('kernel', ['linear', 'rbf']),
        'gamma': hp.uniform('gamma', 0, 20.0)
    },
    {
        'type': 'randomforest',
        'max_depth': hp.choice('max_depth', range(1,20)),
        'max_features': hp.choice('max_features', range(1,5)),
        'n_estimators': hp.choice('n_estimators', range(1,20)),
        'criterion': hp.choice('criterion', ["gini", "entropy"])
    }
])
best = fmin(f, space, algo=tpe.suggest, max_evals=100)
print('best:',best) 
"""
print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


