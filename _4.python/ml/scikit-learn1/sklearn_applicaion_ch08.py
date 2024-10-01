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
print("------------------------------------------------------------")  # 60個

""" 久
#08_01_tensorflow_mnist

import tensorflow as tf

#載入 MNIST 手寫阿拉伯數字資料集

(x_train, y_train),(x_test, y_test) = tf.keras.datasets.mnist.load_data()

#特徵縮放

# 特徵縮放至 (0, 1) 之間
x_train, x_test = x_train / 255.0, x_test / 255.0

#模型訓練

# 建立模型
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

print('aa')
# 設定優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print('bb')
# 模型訓練，epochs：執行週期，validation_split：驗證資料佔 20%
model.fit(x_train, y_train, epochs=5, validation_split=0.2)


print('cc')
#模型評估
model.evaluate(x_test, y_test)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#08_02_k_fold_cross_validation
#Scikit-learn K折交叉驗證法

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np

#載入資料集
X, y = datasets.load_diabetes(return_X_y=True)

#資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

#特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

#模型訓練

from sklearn.linear_model import LinearRegression
clf = LinearRegression()
clf.fit(X_train_std, y_train)

#模型評分

print(f'R2={clf.score(X_test_std, y_test)}')

#R2=0.41738354865811345

#K折測試

from sklearn.model_selection import KFold

kf = KFold(n_splits=5)
for i, (train_index, test_index) in enumerate(kf.split(X_train_std)):
    print(f"Fold {i}:") 
    print(f"  Train: index={train_index}")
    print(f"  Test:  index={test_index}")

#K折驗證

score = []
for i, (train_index, test_index) in enumerate(kf.split(X_train_std)):
    X_new = X_train_std[train_index]
    y_new = y_train[train_index]
    clf.fit(X_new, y_new)
    score_fold = clf.score(X_train_std[test_index], y_train[test_index])
    score.append(score_fold)
    print(f"Fold {i} 分數: {np.mean(score)}") 
print(f"平均值: {np.mean(score)}")
print(f"標準差: {np.std(score)}")

#效能調校

from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV

lasso = Lasso(random_state=0, max_iter=10000)

# 正則化強度：3種選擇
alphas = np.logspace(-4, -0.5, 30)
# 強迫係數(權重)須為正數
positive = (True, False)
tuned_parameters = [{"alpha": alphas, 'positive':positive}]

# 效能調校
clf = GridSearchCV(lasso, tuned_parameters, cv=5, refit=False)
clf.fit(X, y)

scores_mean = clf.cv_results_["mean_test_score"]
scores_std = clf.cv_results_["std_test_score"]
print('平均分數:\n', scores_mean, '\n標準差:\n', scores_std)

# 取得最高分數
cc = np.max(clf.cv_results_["mean_test_score"])
print(cc)

# 參數組合
cc = clf.param_grid
print(cc)

# 取得最佳參數組合
cc = clf.best_params_
print(cc)

# 驗證
from math import floor
index = np.argmax(clf.cv_results_["mean_test_score"])
cc = index, clf.cv_results_["mean_test_score"][index], alphas[floor((index-1)/2)]
print(cc)

cc = clf.best_score_
print(cc)

#以最佳參數組合重新訓練

clf = Lasso(random_state=0, max_iter=10000, alpha=0.07880462815669913
            , positive=False)
clf.fit(X_train_std, y_train)
cc = clf.score(X_test_std, y_test)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#08_03_pipeline_cross_validation

#Scikit-learn 管線測試

import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score

#載入資料集
X, y = datasets.load_diabetes(return_X_y=True)

#資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

#建立管線：特徵縮放、特徵萃取、模型訓練

pipe_lr = make_pipeline(StandardScaler(),
                        PCA(n_components=5),
                        Lasso(random_state=0, max_iter=10000))
pipe_lr.fit(X_train, y_train)

"""
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('pca', PCA(n_components=5)),
                ('lasso', Lasso(max_iter=10000, random_state=0))])
"""

#模型評估

#y_pred = pipe_lr.predict(X_test)
print(f'R2={pipe_lr.score(X_test, y_test)}')

#管線結合K折交叉驗證

from sklearn.model_selection import cross_val_score

scores = cross_val_score(estimator=pipe_lr,
                         X=X_test,
                         y=y_test,
                         cv=10,
                         n_jobs=-1)
print(f'K折分數: %s' % scores)
print(f'平均值: {np.mean(scores):.3f}, 標準差: {np.std(scores):.3f}')

#管線結合K折交叉驗證、效能調校

from sklearn.model_selection import GridSearchCV

# 正則化強度：3種選擇
alphas = np.logspace(-4, -0.5, 30)
# 強迫係數(權重)須為正數
positive = (True, False)
tuned_parameters = [{"lasso__alpha": alphas, 'lasso__positive':positive}]

# 效能調校
clf = GridSearchCV(pipe_lr, tuned_parameters, cv=5, refit=False)
clf.fit(X, y)

scores_mean = clf.cv_results_["mean_test_score"]
scores_std = clf.cv_results_["std_test_score"]
print('平均分數:\n', scores_mean, '\n標準差:\n', scores_std)

# 取得最佳參數組合
cc = clf.best_params_
print(cc)

# 驗證
from math import floor
index = np.argmax(clf.cv_results_["mean_test_score"])
cc = index, clf.cv_results_["mean_test_score"][index], clf.best_score_
print(cc)

#以最佳參數組合重新訓練

pipe_lr = make_pipeline(StandardScaler(),
                        PCA(n_components=5),
                        Lasso(random_state=0, max_iter=10000,
                        alpha=clf.best_params_['lasso__alpha'],
                        positive=clf.best_params_['lasso__positive']))
pipe_lr.fit(X_train, y_train)
cc = pipe_lr.score(X_test, y_test)
print(cc)

from sklearn.pipeline import Pipeline

pipe_lr = Pipeline([('scaler', StandardScaler()),
                    ('pca', PCA(n_components=5)),
                    ('lasso', Lasso(random_state=0, max_iter=10000,
                    alpha=clf.best_params_['lasso__alpha'],
                    positive=clf.best_params_['lasso__positive']))])
pipe_lr.fit(X_train, y_train)
cc = pipe_lr.score(X_test, y_test)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#08_04_confusion_matrix

#計算及繪製混淆矩陣

#載入資料
y_true = [0, 0, 0, 1, 1, 1, 1, 1]
y_pred = [0, 1, 0, 1, 0, 1, 0, 1]

y_true = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
y_pred = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# 真實的資料
y_true = np.random.randint(2, size=100)

# 預測的資料
y_pred = np.random.randint(2, size=100)

# 計算混淆矩陣

from sklearn.metrics import confusion_matrix
cc = confusion_matrix(y_true, y_pred)
print(cc)

from sklearn.metrics import confusion_matrix
cc = confusion_matrix(y_true, y_pred, labels=[1, 0])
print(cc)

# 取得混淆矩陣的4個格子
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
cc = tn, fp, fn, tp
print(cc)

#繪製混淆矩陣
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

ConfusionMatrixDisplay.from_predictions(y_true, y_pred,
                              labels=[1, 0],           
                              display_labels=['真', '偽'])

plt.show()

# 方法 2
cm = confusion_matrix(y_true, y_pred, labels=[1, 0])
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=['真', '偽'])
disp.plot()
plt.show()

# 方法 3
fig, ax = plt.subplots(figsize=(5, 5))

# 顯示矩陣
ax.matshow(cm, cmap=plt.cm.Blues, alpha=0.3)

# 按 [1, 0] 順序
for i in range(cm.shape[0]-1, -1, -1):
    for j in range(cm.shape[1]-1, -1, -1):
        ax.text(x=j, y=i, s=cm[i, j], va='center', ha='center')

# 置換刻度        
ax.set_xticks(range(cm.shape[0]), labels=['真', '偽'], fontsize=14)
ax.set_yticks(range(cm.shape[1]), labels=['真', '偽'], fontsize=14)

# 設定標籤        
plt.xlabel('Predicted label', fontsize=16)
plt.ylabel('True label', fontsize=16)
plt.show()
 
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#08_05_confusion_matrix_multiple-categories

#計算及繪製多分類混淆矩陣

y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]

#計算混淆矩陣

from sklearn.metrics import confusion_matrix
cc = confusion_matrix(y_true, y_pred)
print(cc)

#繪製混淆矩陣

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

ConfusionMatrixDisplay.from_predictions(y_true, y_pred)
plt.show()

# 方法 2
cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

# 方法 3
fig, ax = plt.subplots(figsize=(5, 5))

# 顯示矩陣
ax.matshow(cm, cmap=plt.cm.Blues, alpha=0.3)

# 按 [1, 0] 順序
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(x=j, y=i, s=cm[i, j], va='center', ha='center')

# 置換刻度 NG
#ax.set_xticks(range(cm.shape[0]), fontsize=14)
#ax.set_yticks(range(cm.shape[1]), fontsize=14)

# 設定標籤        
plt.xlabel('Predicted label', fontsize=16)
plt.ylabel('True label', fontsize=16)
plt.show()

#繪製混淆矩陣

import numpy as np
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split

# 載入資料
ds = datasets.load_iris()
X, y = ds.data, ds.target

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# 模型訓練
clf = svm.SVC(kernel='linear', C=0.01).fit(X_train, y_train)

y_pred = clf.predict(X_test)

# 設定顯示小數點位數
np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
titles_options = [("正常的混淆矩陣", None),
                  ("正規化混淆矩陣", 'true')]

f, axes = plt.subplots(1, 2, figsize=(14, 5), sharey='row')
for i, (title, normalize) in enumerate(titles_options):
    cm = ConfusionMatrixDisplay.from_predictions(y_test, y_pred, ax=axes[i]
                            , cmap=plt.cm.Blues, display_labels=ds.target_names
                            , normalize=normalize)
#     cm.plot(ax=axes[i])
    cm.ax_.set_title(title, fontsize=16)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#08_06_performance_metrics

#計算及繪製混淆矩陣

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#載入資料

df = pd.read_csv('C:/_git/vcs/_big_files/Scikit-learn_data/creditcard.csv')
cc = df.head()
print(cc)


#觀察目標變數的各類別筆數

cc = df.Class.value_counts()
print(cc)

sns.countplot(x='Class', data=df)
plt.show()

#模型訓練與預測

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = df.drop(['Time', 'Amount', 'Class'], axis=1), df['Class']

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# 模型訓練
clf = LogisticRegression().fit(X_train, y_train)

# 預測
y_pred = clf.predict(X_test)

# 準確率
cc = accuracy_score(y_test, y_pred)
print(cc)

#計算混淆矩陣

# 取得混淆矩陣的4個格子
from sklearn.metrics import confusion_matrix

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print(tn, fp, fn, tp)

#(71072, 10, 40, 80)

#常用的效能衡量指標計算

print(f'準確率(Accuracy)={(tn+tp) / (tn+fp+fn+tp)}')
print(f'精確率(Precision)={(tp) / (fp+tp)}')
print(f'召回率(Recall)={(tp) / (fn+tp)}')
print(f'F1 score={(2*tp) / (2*tp+fp+fn)}')

"""
準確率(Accuracy)=0.9992977725344794
精確率(Precision)=0.8888888888888888
召回率(Recall)=0.6666666666666666
F1 score=0.7619047619047619
"""

#Scikit-learn 分類報表

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

# weighted average 驗算
cc = (1.00 * 71082 + 0.89 * 120) / (71082 + 120)
print(cc)

#多類別的分類報表

# 3 類別
y_true = [0, 1, 2, 2, 2]
y_pred = [0, 0, 2, 2, 1]
print(classification_report(y_true, y_pred))

#多類別的分類報表

# 3 類別
y_pred = [1, 2, 0]
y_true = [1, 1, 1]
print(classification_report(y_true, y_pred, labels=[1, 2, 3]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
ROC曲線
Receiver operating characteristic curve
接收者操作特徵曲線
"""
#08_07_ draw_roc

#繪製ROC曲線

import numpy as np
import matplotlib.pyplot as plt

#載入資料

import pandas as pd

df=pd.read_csv('./data/roc_test_data.csv')
print(df)

"""
繪製ROC曲線

    計算第二欄的真(1)與假(0)的個數，假設分別為P及N，Y軸切成P格，X軸切成N格，如下圖。
    以第一欄降冪排序，從大排到小。
    依序掃描第二欄，若是1，就往『上』畫一格，反之，若是0，就往『右』畫一格，直到最後一列，如下圖。
"""

#計算P及N個數

# 計算第二欄的真(1)與假(0)的個數，假設分別為P及N
P= df[df['actual']==1].shape[0]
N= df[df['actual']==0].shape[0]
print(f'P={P}, N={N}')

# X、Y軸每一格的大小
cc = y_unit=1/P
print(cc)
cc = X_unit=1/N
print(cc)

#P=11, N=7

#根據第1欄降冪排序

df2=df.sort_values(by='predict', ascending=False)
print(df2)

#掃描表格每一列，第二欄若是1，就往『上』畫一格，反之，若是0，就往『右』畫一格

X, y=[], []
current_X, current_y = 0, 0
for row in df2.itertuples():
    # 若是1，Y加1
    if row[2] == 1:
        current_y+=y_unit
    else: # 若是0，X加1
        current_X+=X_unit
    # 儲存每一點X/Y座標
    X.append(current_X)
    y.append(current_y)

X=np.array(X)        
y=np.array(y)    
print(X, y)

#繪製ROC曲線

plt.title('ROC 曲線')
plt.plot(X, y, color = 'orange')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('真陽率')
plt.xlabel('偽陽率')
plt.show()

#Scikit-Learn 作法

from sklearn.metrics import roc_curve, roc_auc_score, auc

fpr, tpr, threshold = roc_curve(df['actual'], df['predict'])
print(f'偽陽率:\n{fpr}\n\n真陽率:\n{tpr}\n\n決策門檻:{threshold}')

"""
偽陽率:
[0.         0.         0.         0.14285714 0.14285714 0.28571429
 0.28571429 0.57142857 0.57142857 0.71428571 0.71428571 1.        ]

真陽率:
[0.         0.09090909 0.27272727 0.27272727 0.63636364 0.63636364
 0.81818182 0.81818182 0.90909091 0.90909091 1.         1.        ]

決策門檻:[1.99 0.99 0.8  0.73 0.56 0.48 0.42 0.32 0.22 0.11 0.1  0.03]
"""

#繪製ROC曲線

auc1 = auc(fpr, tpr)
plt.title('ROC 曲線')
plt.plot(fpr, tpr, color = 'orange', label = 'AUC = %0.2f' % auc1)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('真陽率')
plt.xlabel('偽陽率')
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#08_08_roc_breast_cancer

#實作乳癌診斷，並繪製ROC曲線

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import datasets

#載入資料

data = datasets.load_breast_cancer()

#資料分割

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(data.data[:,:6], data.target, test_size=0.20)

#模型訓練

from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline

pipe = make_pipeline(StandardScaler(), SVC(probability=True))

pipe.fit(X_train, y_train)

"""
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('svc', SVC(probability=True))])
"""

#模型預測

y_pred_proba = pipe.predict_proba(X_test)
cc = np.around(y_pred_proba, 2)
print(cc)

#預測值(第2欄)與實際值合併

df = pd.DataFrame({'predict':np.around(y_pred_proba[:,1], 2), 'actual':y_test})
print(df)

#依預測值降冪排序

df2=df.sort_values(by='predict', ascending=False)
print(df2)

#繪製ROC曲線

from sklearn.metrics import roc_curve, roc_auc_score, auc

fpr, tpr, threshold = roc_curve(df['actual'], df['predict'])
auc1 = auc(fpr, tpr)
plt.title('ROC 曲線')
plt.plot(fpr, tpr, color = 'orange', label = 'AUC = %0.2f' % auc1)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('真陽率')
plt.xlabel('偽陽率')
plt.show()

cc = roc_auc_score(df2.actual, df2.predict)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#08_09_ credit_card_fraud_detection

#信用卡詐欺偵測

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#載入資料

df = pd.read_csv('C:/_git/vcs/_big_files/Scikit-learn_data/creditcard.csv')
cc = df.head()
print(cc)

#觀察目標變數的各類別筆數

cc = df.Class.value_counts()
print(cc)

sns.countplot(x='Class', data=df)
plt.show()

#模型訓練與評估

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = df.drop(['Time', 'Amount', 'Class'], axis=1), df['Class']

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# 模型訓練
clf = LogisticRegression().fit(X_train, y_train)

# 預測
y_pred = clf.predict(X_test)

# 準確率
cc = accuracy_score(y_test, y_pred)
print(cc)

#K折交叉驗證

from sklearn.model_selection import cross_val_score

scores = cross_val_score(estimator=clf,
                         X=X_test,
                         y=y_test,
                         cv=10,
                         n_jobs=-1)
print(f'K折分數: %s' % scores)
print(f'平均值: {np.mean(scores):.3f}, 標準差: {np.std(scores):.3f}')

"""
K折分數: [0.99915742 0.99929785 0.9988764  0.9997191  0.99901685 0.99901685
 0.9991573  0.99957865 0.9988764  0.9994382 ]
平均值: 0.999, 標準差: 0.000
"""

#分類報告

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

#繪製ROC曲線

from sklearn.metrics import roc_curve, roc_auc_score, auc

y_pred_proba = clf.predict_proba(X_test)[:,1]
fpr, tpr, threshold = roc_curve(y_test, y_pred_proba)
auc1 = auc(fpr, tpr)
plt.title('ROC 曲線')
plt.plot(fpr, tpr, color = 'orange', label = 'AUC = %0.2f' % auc1)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('真陽率')
plt.xlabel('偽陽率')
plt.show()

#從寬認定詐欺行為

y_pred_proba = clf.predict_proba(X_test)[:,1]
y_pred = y_pred_proba >= 0.3
print(classification_report(y_test, y_pred))

#Over-sampling -- SMOTE

# !pip install -U imbalanced-learn

from imblearn.over_sampling import SMOTE
from imblearn.metrics import classification_report_imbalanced

print(df.Class.value_counts())
smote = SMOTE()
X_new, y_new = smote.fit_resample(X, y)
cc = len(y_new[y_new==0]), len(y_new[y_new==1])
print(cc)

#模型訓練與評估

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X_new, y_new)

# 模型訓練
clf = LogisticRegression().fit(X_train, y_train)

# 預測
y_pred = clf.predict(X_test)

# 準確率
cc = accuracy_score(y_test, y_pred)
print(cc)

#K折交叉驗證

from sklearn.model_selection import cross_val_score

scores = cross_val_score(estimator=clf,
                         X=X_test,
                         y=y_test,
                         cv=10,
                         n_jobs=-1)
print(f'K折分數: %s' % scores)
print(f'平均值: {np.mean(scores):.3f}, 標準差: {np.std(scores):.3f}')

"""
K折分數: [0.94499156 0.94379572 0.94569499 0.94541362 0.94442881 0.94288126
 0.94231851 0.95040799 0.94336968 0.94379177]
平均值: 0.945, 標準差: 0.002
"""

#分類報告

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

#imbalanced-learn 分類報告

from imblearn.metrics import classification_report_imbalanced
print(classification_report_imbalanced(y_test, y_pred))


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
