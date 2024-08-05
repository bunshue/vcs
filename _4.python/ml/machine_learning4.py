"""

必學！Python 資料科學‧機器學習最強套件 scikit-learn 1

"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import os
import time
import random

print('------------------------------------------------------------')	#60個

print('產生測試資料 並畫出')

from sklearn.datasets import make_blobs

N = 500
print('產生', N, '筆資料 2維 2群')
dx, dy = make_blobs(n_samples = N, n_features = 2, centers = 2, random_state = 0)

print(dx.shape)
print(dy.shape)
#print(dx)
#print(dy)

plt.scatter(dx.T[0], dx.T[1], c = dy, cmap = 'Dark2')
plt.title('dx的分佈狀況, dy是用顏色表示')
plt.grid(True)

plt.show()

print('------------------------------------------------------------')	#60個

#StandardScaler
#將資料常態分布化，平均值會變為0, 標準差變為1，使離群值影響降低
#MinMaxScaler與StandardScaler類似

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

N = 500
print('產生', N, '筆資料 2維 2群')
dx, dy = make_blobs(n_samples = N, n_features = 2, centers = 2, random_state = 0)

dx_std = StandardScaler().fit_transform(dx)

plt.scatter(dx_std.T[0], dx_std.T[1], c = dy, cmap = 'Dark2')
plt.grid(True)

plt.show()

#分割訓練資料集和測試資料集
from sklearn.model_selection import train_test_split

dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size = 0.2, random_state = 0)

print(dx.shape)
print(dx_train.shape)
print(dx_test.shape)

print(dy.shape)
print(dy_train.shape)
print(dy_test.shape)

#k 最近鄰演算法 (KNN)
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(dx_train, dy_train)
predictions = knn.predict(dx_test)

print(dy_test)
print(predictions)
print(knn.score(dx_train, dy_train))
print(knn.score(dx_test, dy_test))

sys.exit()

print('------------------------------------------------------------')	#60個

#邏輯斯迴歸 (logistic regression)

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

print('產生500筆資料 2維 2群')
dx, dy = make_blobs(n_samples = 500, n_features = 2, centers = 2, random_state = 0)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size = 0.2, random_state = 0)

log_reg = LogisticRegression()
log_reg.fit(dx_train, dy_train)
predictions = log_reg.predict(dx_test)

print(log_reg.score(dx_train, dy_train))
print(log_reg.score(dx_test, dy_test))

print('------------------------------------------------------------')	#60個

#線性支援向量機 (Linear SVM)

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

print('產生500筆資料 2維 2群')
dx, dy = make_blobs(n_samples = 500, n_features = 2, centers = 2, random_state = 0)
dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size = 0.2, random_state = 0)

linear_svm = LinearSVC()
linear_svm.fit(dx_train, dy_train)
predictions = linear_svm.predict(dx_test)

print(linear_svm.score(dx_train, dy_train))
print(linear_svm.score(dx_test, dy_test))

print('------------------------------------------------------------')	#60個

#非線性 SVM

from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC

dx, dy = make_moons(n_samples = 500, noise = 0.15, random_state = 0)

dx_train, dx_test, dy_train, dy_test = train_test_split(StandardScaler().fit_transform(dx), dy, test_size = 0.2, random_state = 0)

linear_svm = LinearSVC()

linear_svm.fit(dx_train, dy_train)

predictions = linear_svm.predict(dx_test)

svm = SVC()

svm.fit(dx_train, dy_train)

predictions = svm.predict(dx_test)

print(linear_svm.score(dx_train, dy_train))

print(linear_svm.score(dx_test, dy_test))

print(svm.score(dx_train, dy_train))

print(svm.score(dx_test, dy_test))

print('------------------------------------------------------------')	#60個

#決策樹 (decision tree)

from sklearn.datasets import load_iris

dx, dy = load_iris(return_X_y = True)

print(dx[0])
print(dy[0])

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

dx, dy = load_iris(return_X_y = True)

dx_train, dx_test, dy_train, dy_test = train_test_split(dx, dy, test_size = 0.2, random_state = 0)

tree = DecisionTreeClassifier()

tree.fit(dx_train, dy_train)

predictions = tree.predict(dx_test)

print(tree.score(dx_train, dy_train))

print(tree.score(dx_test, dy_test))

print('------------------------------------------------------------')	#60個

#隨機森林 (random forest)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

dx, dy = load_iris(return_X_y = True)

dx_train, dx_test, dy_train, dy_test = train_test_split(dx, dy, test_size = 0.2, random_state = 0)

forest = RandomForestClassifier()

forest.fit(dx_train, dy_train)

predictions = forest.predict(dx_test)

print(forest.score(dx_train, dy_train))

print(forest.score(dx_test, dy_test))

print('------------------------------------------------------------')	#60個

#k-fold 交叉驗證法

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

dx, dy = load_wine(return_X_y = True)
dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size = 0.2, random_state = 0)

forest = RandomForestClassifier()

forest.fit(dx_train, dy_train)

val_score = cross_val_score(forest, dx_train, dy_train, cv = 5)

predictions = forest.predict(dx_test)

print(forest.score(dx_train, dy_train).round(3))

print(val_score.mean().round(3))

print(forest.score(dx_test, dy_test) .round(3))

print('------------------------------------------------------------')	#60個

#產生預測結果報告

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

dx, dy = load_wine(return_X_y = True)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size = 0.2, random_state = 0)

forest = RandomForestClassifier()

forest.fit(dx_train, dy_train)

predictions = forest.predict(dx_test)

print(forest.score(dx_train, dy_train).round(3))

print(forest.score(dx_test, dy_test).round(3))

print(classification_report(dy_test, predictions))

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

#13-1-1 最近 k 鄰數量：n_neighbors

from sklearn.datasets import load_breast_cancer #匯入資料集
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt #匯入 matplotlib

#取得特徵與標籤資料

dx, dy = load_breast_cancer(return_X_y = True) 

dx_train, dx_test, dy_train, dy_test = train_test_split(dx, dy, test_size = 0.2, random_state = 0)

cv_scores = [] #用來收集交叉驗證準確率的 list

test_scores = [] #用來收集測試集準確率的 list

x = np.arange(10) + 1 #圖表 X 軸 (KNN 模型的 k 值)

for k in x:
    knn = KNeighborsClassifier(n_neighbors = k).fit(dx_train, dy_train)
    cv_scores.append(cross_val_score(knn, dx_train, dy_train, cv = 5).mean())
    test_scores.append(knn.score(dx_test, dy_test))

plt.title('KNN hyperparameter')
plt.plot(x, cv_scores, label = 'CV score') #繪製交叉驗證折線圖
plt.plot(x, test_scores, label = 'Test score') #繪製測試集預測折線圖
plt.xlabel('k neighbors')
plt.ylabel('accuracy (%)')
plt.legend()
plt.grid(True)
plt.show()

print('------------------------------------------------------------')	#60個

#13-1-2 用 GridSearchCV 自動搜尋最佳 k 值

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt

dx, dy = load_breast_cancer(return_X_y = True)
dx_train, dx_test, dy_train, dy_test = train_test_split(dx, dy, test_size = 0.2, random_state = 0)

param_grid = {'n_neighbors': np.arange(10) + 1} #要網格搜尋的參數
model = GridSearchCV(KNeighborsClassifier(), param_grid)
model.fit(dx_train, dy_train) #用最佳模型來做訓練

print('Best params:', model.best_params_) #傳回最佳參數
print('CV score:', model.best_score_.round(3))
print('Test score:', model.score(dx_test, dy_test).round(3))

print('------------------------------------------------------------')	#60個

#13-2-1 邏輯斯迴歸的 C：常規化強度

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

dx, dy = load_breast_cancer(return_X_y = True)
dx_std = StandardScaler().fit_transform(dx) #資料標準化
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size = 0.2, random_state = 0)

cv_scores = []
test_scores = []

x = [10 ** n for n in range(-4, 5)]

x_str = [str(n) for n in x] #X 軸各數值『名稱』

for c in x:
    log_reg = LogisticRegression(C = c, max_iter = 1000).fit(dx_train, dy_train)
    cv_scores.append(cross_val_score(log_reg, dx_train, dy_train,cv = 5).mean())
    test_scores.append(log_reg.score(dx_test, dy_test))

plt.title('Logistic Regression hyperparameter')
plt.plot(x_str, cv_scores, label = 'CV score')
plt.plot(x_str, test_scores, label = 'Test score')
plt.xlabel('C')
plt.ylabel('accuracy (%)')
plt.legend()
plt.grid(True)

plt.show()

print('------------------------------------------------------------')	#60個

#13-2-2 線性 SVC 的 C：常規化強度

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import LinearSVC
import numpy as np
import matplotlib.pyplot as plt

dx, dy = load_breast_cancer(return_X_y = True)
dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size = 0.2, random_state = 0)

cv_scores = []
test_scores = []

x = [10 ** n for n in range(-4, 5)]
x_str = [str(n) for n in x]

for c in x:
    linear_svc = LinearSVC(C = c, max_iter = 10000).fit(dx_train, dy_train)
    cv_scores.append(cross_val_score(linear_svc, dx_train, dy_train, cv = 5).mean())
    test_scores.append(linear_svc.score(dx_test, dy_test))

plt.title('Linear SVM hyperparameter')
plt.plot(x_str, cv_scores, label = 'CV score')
plt.plot(x_str, test_scores, label = 'Test score')
plt.xlabel('C')
plt.ylabel('accuracy (%)')
plt.legend()
plt.grid(True)
plt.show()

print('------------------------------------------------------------')	#60個

#13-3-1 C, gamma 與 kernel 參數

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import matplotlib.pyplot as plt

dx, dy = load_breast_cancer(return_X_y = True)
dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size = 0.2, random_state = 0)

x = [10 ** n for n in range(-2, 3)]

param_grid = {'C': x,
              'gamma': x,
              'kernel': ['linear', 'rbf', 'poly', 'sigmoid']}

model = GridSearchCV(SVC(), param_grid)
model.fit(dx_train, dy_train)

print('Best params: ', model.best_params_)
print('CV score:', model.best_score_.round(3))
print('Test score:', model.score(dx_test, dy_test).round(3))

print('------------------------------------------------------------')	#60個

#13-3-2 使用 RandomizedSearchCV 更快速尋找較適當的參數

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.model_selection import RandomizedSearchCV
import numpy as np
import matplotlib.pyplot as plt

dx, dy = load_breast_cancer(return_X_y = True)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size = 0.2, random_state = 0)

param_grid = {'C': np.linspace(1, 100, 100),
              'gamma': np.linspace(0.01, 1, 100),
              'kernel': ['linear', 'rbf', 'poly', 'sigmoid']}

model = RandomizedSearchCV(SVC(), param_grid, n_iter = 100)
model.fit(dx_train, dy_train)

print('Best params:', model.best_params_)
print('CV score:', model.best_score_.round(3))
print('Test score:', model.score(dx_test, dy_test).round(3))

print('------------------------------------------------------------')	#60個

#13-4-1 決策樹的最大深度：max_depth

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import matplotlib.pyplot as plt

dx, dy = load_breast_cancer(return_X_y = True)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size = 0.2, random_state = 0)

cv_scores = []

test_scores = []

x = np.arange(12) + 1

x_str = [str(n) for n in x]

for d in x:
    tree = DecisionTreeClassifier(max_depth = d).fit(dx_train, dy_train)
    cv_scores.append(cross_val_score(tree, dx_train, dy_train, cv = 5).mean())
    test_scores.append(tree.score(dx_test, dy_test))

plt.title('Decision Tree hyperparameter')
plt.plot(x_str, cv_scores, label = 'CV score')
plt.plot(x_str, test_scores, label = 'Test score')
plt.xlabel('Max depth')
plt.ylabel('accuracy (%)')
plt.legend()
plt.grid(True)
plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

dx, dy = load_breast_cancer(return_X_y = True)
feature_names = list(load_breast_cancer().feature_names)

dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size = 0.2, random_state = 0)

model = DecisionTreeClassifier(max_depth = 3).fit(dx_train, dy_train)

print(export_text(model, feature_names = feature_names))

print('------------------------------------------------------------')	#60個

#13-4-2 隨機森林的規模 n_estimators 與亂數種子 random_state

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt

dx, dy = load_breast_cancer(return_X_y = True)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size = 0.2, random_state = 0)

cv_scores = []
test_scores = []

x = (np.arange(10) + 1) * 50
x_str = [str(n) for n in x]

for t in x:
  tree = RandomForestClassifier(n_estimators = t, max_depth = 3,random_state = 0)
  tree.fit(dx_train, dy_train)
  cv_scores.append(cross_val_score(tree, dx_train, dy_train,cv = 5).mean())
  test_scores.append(tree.score(dx_test, dy_test))

plt.title('Random Forest hyperparameter')
plt.plot(x_str, cv_scores, label = 'CV score')
plt.plot(x_str, test_scores, label = 'Test score')
plt.xlabel('Number of trees')
plt.ylabel('accuracy (%)')
plt.legend()
plt.grid(True)
plt.show()

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



