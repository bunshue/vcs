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
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料


def show():
    return
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# 08_02_k_fold_cross_validation
# Scikit-learn K折交叉驗證法

from sklearn.preprocessing import StandardScaler

# 載入資料集
X, y = datasets.load_diabetes(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練

from sklearn.linear_model import LinearRegression

clf = sklearn.linear_model.LinearRegression()  # 函數學習機

clf.fit(X_train_std, y_train)

# 模型評分
print(f"R2={clf.score(X_test_std, y_test)}")
# R2=0.41738354865811345

# K折測試
from sklearn.model_selection import KFold

kf = KFold(n_splits=5)
for i, (train_index, test_index) in enumerate(kf.split(X_train_std)):
    print(f"Fold {i}:")
    print(f"  Train: index={train_index}")
    print(f"  Test:  index={test_index}")

# K折驗證
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

# 效能調校

from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV

lasso = Lasso(random_state=0, max_iter=10000)

# 正則化強度：3種選擇
alphas = np.logspace(-4, -0.5, 30)
# 強迫係數(權重)須為正數
positive = (True, False)
tuned_parameters = [{"alpha": alphas, "positive": positive}]

# 效能調校
clf = GridSearchCV(lasso, tuned_parameters, cv=5, refit=False)
clf.fit(X, y)

# cv_results_ : 具體用法模型不同參數下交叉驗證的結果
scores_mean = clf.cv_results_["mean_test_score"]
scores_std = clf.cv_results_["std_test_score"]
print("平均分數:\n", scores_mean, "\n標準差:\n", scores_std)

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
cc = index, clf.cv_results_["mean_test_score"][index], alphas[floor((index - 1) / 2)]
print(cc)

cc = clf.best_score_
print(cc)

# 以最佳參數組合重新訓練

clf = Lasso(random_state=0, max_iter=10000, alpha=0.07880462815669913, positive=False)
clf.fit(X_train_std, y_train)
cc = clf.score(X_test_std, y_test)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 08_03_pipeline_cross_validation

# Scikit-learn 管線測試

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score

# 載入資料集
X, y = datasets.load_diabetes(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 建立管線：特徵縮放、特徵萃取、模型訓練

pipe_lr = make_pipeline(
    StandardScaler(), PCA(n_components=5), Lasso(random_state=0, max_iter=10000)
)
pipe_lr.fit(X_train, y_train)

"""
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('pca', PCA(n_components=5)),
                ('lasso', Lasso(max_iter=10000, random_state=0))])
"""

# 模型評估

# y_pred = pipe_lr.predict(X_test)
print(f"R2={pipe_lr.score(X_test, y_test)}")

# 管線結合K折交叉驗證

from sklearn.model_selection import cross_val_score

scores = cross_val_score(estimator=pipe_lr, X=X_test, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.3f}, 標準差: {np.std(scores):.3f}")

# 管線結合K折交叉驗證、效能調校

from sklearn.model_selection import GridSearchCV

# 正則化強度：3種選擇
alphas = np.logspace(-4, -0.5, 30)
# 強迫係數(權重)須為正數
positive = (True, False)
tuned_parameters = [{"lasso__alpha": alphas, "lasso__positive": positive}]

# 效能調校
clf = GridSearchCV(pipe_lr, tuned_parameters, cv=5, refit=False)
clf.fit(X, y)

# cv_results_ : 具體用法模型不同參數下交叉驗證的結果
scores_mean = clf.cv_results_["mean_test_score"]
scores_std = clf.cv_results_["std_test_score"]
print("平均分數:\n", scores_mean, "\n標準差:\n", scores_std)

# 取得最佳參數組合
cc = clf.best_params_
print(cc)

# 驗證
from math import floor

index = np.argmax(clf.cv_results_["mean_test_score"])
cc = index, clf.cv_results_["mean_test_score"][index], clf.best_score_
print(cc)

# 以最佳參數組合重新訓練

pipe_lr = make_pipeline(
    StandardScaler(),
    PCA(n_components=5),
    Lasso(
        random_state=0,
        max_iter=10000,
        alpha=clf.best_params_["lasso__alpha"],
        positive=clf.best_params_["lasso__positive"],
    ),
)
pipe_lr.fit(X_train, y_train)
cc = pipe_lr.score(X_test, y_test)
print(cc)

from sklearn.pipeline import Pipeline

pipe_lr = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("pca", PCA(n_components=5)),
        (
            "lasso",
            Lasso(
                random_state=0,
                max_iter=10000,
                alpha=clf.best_params_["lasso__alpha"],
                positive=clf.best_params_["lasso__positive"],
            ),
        ),
    ]
)
pipe_lr.fit(X_train, y_train)
cc = pipe_lr.score(X_test, y_test)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 08_04_confusion_matrix

# 計算及繪製混淆矩陣

# 載入資料
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

# 繪製混淆矩陣
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_predictions(
    y_true, y_pred, labels=[1, 0], display_labels=["真", "偽"]
)

show()

# 方法 2
cm = confusion_matrix(y_true, y_pred, labels=[1, 0])
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["真", "偽"])
disp.plot()
show()

# 方法 3
fig, ax = plt.subplots(figsize=(5, 5))

# 顯示矩陣
ax.matshow(cm, cmap=plt.cm.Blues, alpha=0.3)

# 按 [1, 0] 順序
for i in range(cm.shape[0] - 1, -1, -1):
    for j in range(cm.shape[1] - 1, -1, -1):
        ax.text(x=j, y=i, s=cm[i, j], va="center", ha="center")

# 置換刻度
ax.set_xticks(range(cm.shape[0]), labels=["真", "偽"], fontsize=14)
ax.set_yticks(range(cm.shape[1]), labels=["真", "偽"], fontsize=14)

# 設定標籤
plt.xlabel("Predicted label", fontsize=16)
plt.ylabel("True label", fontsize=16)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 08_05_confusion_matrix_multiple-categories

# 計算及繪製多分類混淆矩陣

y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]

# 計算混淆矩陣
from sklearn.metrics import confusion_matrix

cc = confusion_matrix(y_true, y_pred)
print(cc)

# 繪製混淆矩陣
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_predictions(y_true, y_pred)
show()

# 方法 2
cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
show()

# 方法 3
fig, ax = plt.subplots(figsize=(5, 5))

# 顯示矩陣
ax.matshow(cm, cmap=plt.cm.Blues, alpha=0.3)

# 按 [1, 0] 順序
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(x=j, y=i, s=cm[i, j], va="center", ha="center")

# 置換刻度 NG
# ax.set_xticks(range(cm.shape[0]), fontsize=14)
# ax.set_yticks(range(cm.shape[1]), fontsize=14)

# 設定標籤
plt.xlabel("Predicted label", fontsize=16)
plt.ylabel("True label", fontsize=16)
show()

# 繪製混淆矩陣

from sklearn import svm

# 載入資料
ds = datasets.load_iris()
X, y = ds.data, ds.target

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# 模型訓練
clf = svm.SVC(kernel="linear", C=0.01).fit(X_train, y_train)

y_pred = clf.predict(X_test)

# 設定顯示小數點位數
np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
titles_options = [("正常的混淆矩陣", None), ("正規化混淆矩陣", "true")]

f, axes = plt.subplots(1, 2, figsize=(14, 5), sharey="row")
for i, (title, normalize) in enumerate(titles_options):
    cm = ConfusionMatrixDisplay.from_predictions(
        y_test,
        y_pred,
        ax=axes[i],
        cmap=plt.cm.Blues,
        display_labels=ds.target_names,
        normalize=normalize,
    )
    #     cm.plot(ax=axes[i])
    cm.ax_.set_title(title, fontsize=16)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 08_06_performance_metrics

# 計算及繪製混淆矩陣

df = pd.read_csv("C:/_git/vcs/_big_files/Scikit-learn_data/creditcard.csv")
cc = df.head()
print(cc)


# 觀察目標變數的各類別筆數

cc = df.Class.value_counts()
print(cc)

sns.countplot(x="Class", data=df)
show()

# 模型訓練與預測

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X, y = df.drop(["Time", "Amount", "Class"], axis=1), df["Class"]

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# 模型訓練
clf = LogisticRegression().fit(X_train, y_train)

# 預測
y_pred = clf.predict(X_test)

# 準確率
cc = accuracy_score(y_test, y_pred)
print(cc)

# 計算混淆矩陣

# 取得混淆矩陣的4個格子
from sklearn.metrics import confusion_matrix

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print(tn, fp, fn, tp)

# (71072, 10, 40, 80)

# 常用的效能衡量指標計算

print(f"準確率(Accuracy)={(tn+tp) / (tn+fp+fn+tp)}")
print(f"精確率(Precision)={(tp) / (fp+tp)}")
print(f"召回率(Recall)={(tp) / (fn+tp)}")
print(f"F1 score={(2*tp) / (2*tp+fp+fn)}")

"""
準確率(Accuracy)=0.9992977725344794
精確率(Precision)=0.8888888888888888
召回率(Recall)=0.6666666666666666
F1 score=0.7619047619047619
"""

# Scikit-learn 分類報表

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

# weighted average 驗算
cc = (1.00 * 71082 + 0.89 * 120) / (71082 + 120)
print(cc)

# 多類別的分類報表

# 3 類別
y_true = [0, 1, 2, 2, 2]
y_pred = [0, 0, 2, 2, 1]
print(classification_report(y_true, y_pred))

# 多類別的分類報表

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
# 08_07_ draw_roc

# 繪製ROC曲線

# 載入資料

df = pd.read_csv("./data/roc_test_data.csv")
print(df)

"""
繪製ROC曲線

    計算第二欄的真(1)與假(0)的個數，假設分別為P及N，Y軸切成P格，X軸切成N格，如下圖。
    以第一欄降冪排序，從大排到小。
    依序掃描第二欄，若是1，就往『上』畫一格，反之，若是0，就往『右』畫一格，直到最後一列，如下圖。
"""

# 計算P及N個數

# 計算第二欄的真(1)與假(0)的個數，假設分別為P及N
P = df[df["actual"] == 1].shape[0]
N = df[df["actual"] == 0].shape[0]
print(f"P={P}, N={N}")

# X、Y軸每一格的大小
cc = y_unit = 1 / P
print(cc)
cc = X_unit = 1 / N
print(cc)

# P=11, N=7

# 根據第1欄降冪排序

df2 = df.sort_values(by="predict", ascending=False)
print(df2)

# 掃描表格每一列，第二欄若是1，就往『上』畫一格，反之，若是0，就往『右』畫一格

X, y = [], []
current_X, current_y = 0, 0
for row in df2.itertuples():
    # 若是1，Y加1
    if row[2] == 1:
        current_y += y_unit
    else:  # 若是0，X加1
        current_X += X_unit
    # 儲存每一點X/Y座標
    X.append(current_X)
    y.append(current_y)

X = np.array(X)
y = np.array(y)
print(X, y)

# 繪製ROC曲線

plt.title("ROC 曲線")
plt.plot(X, y, color="orange")
plt.plot([0, 1], [0, 1], "r--")
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel("真陽率")
plt.xlabel("偽陽率")
show()

# Scikit-Learn 作法

from sklearn.metrics import roc_curve, roc_auc_score, auc

fpr, tpr, threshold = roc_curve(df["actual"], df["predict"])
print(f"偽陽率:\n{fpr}\n\n真陽率:\n{tpr}\n\n決策門檻:{threshold}")

"""
偽陽率:
[0.         0.         0.         0.14285714 0.14285714 0.28571429
 0.28571429 0.57142857 0.57142857 0.71428571 0.71428571 1.        ]

真陽率:
[0.         0.09090909 0.27272727 0.27272727 0.63636364 0.63636364
 0.81818182 0.81818182 0.90909091 0.90909091 1.         1.        ]

決策門檻:[1.99 0.99 0.8  0.73 0.56 0.48 0.42 0.32 0.22 0.11 0.1  0.03]
"""

# 繪製ROC曲線

auc1 = auc(fpr, tpr)
plt.title("ROC 曲線")
plt.plot(fpr, tpr, color="orange", label="AUC = %0.2f" % auc1)
plt.legend(loc="lower right")
plt.plot([0, 1], [0, 1], "r--")
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel("真陽率")
plt.xlabel("偽陽率")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 08_08_roc_breast_cancer

# 實作乳癌診斷，並繪製ROC曲線

data = datasets.load_breast_cancer()

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    data.data[:, :6], data.target, test_size=0.20
)

# 模型訓練

from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline

pipe = make_pipeline(StandardScaler(), SVC(probability=True))

pipe.fit(X_train, y_train)

"""
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('svc', SVC(probability=True))])
"""

# 模型預測

y_pred_proba = pipe.predict_proba(X_test)
cc = np.around(y_pred_proba, 2)
print(cc)

# 預測值(第2欄)與實際值合併

df = pd.DataFrame({"predict": np.around(y_pred_proba[:, 1], 2), "actual": y_test})
print(df)

# 依預測值降冪排序

df2 = df.sort_values(by="predict", ascending=False)
print(df2)

# 繪製ROC曲線

from sklearn.metrics import roc_curve, roc_auc_score, auc

fpr, tpr, threshold = roc_curve(df["actual"], df["predict"])
auc1 = auc(fpr, tpr)
plt.title("ROC 曲線")
plt.plot(fpr, tpr, color="orange", label="AUC = %0.2f" % auc1)
plt.legend(loc="lower right")
plt.plot([0, 1], [0, 1], "r--")
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel("真陽率")
plt.xlabel("偽陽率")
show()

cc = roc_auc_score(df2.actual, df2.predict)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 08_09_ credit_card_fraud_detection

# 信用卡詐欺偵測

# 載入資料

df = pd.read_csv("C:/_git/vcs/_big_files/Scikit-learn_data/creditcard.csv")
cc = df.head()
print(cc)

# 觀察目標變數的各類別筆數

cc = df.Class.value_counts()
print(cc)

sns.countplot(x="Class", data=df)
show()

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X, y = df.drop(["Time", "Amount", "Class"], axis=1), df["Class"]

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# 模型訓練
clf = LogisticRegression().fit(X_train, y_train)

# 預測
y_pred = clf.predict(X_test)

# 準確率
cc = accuracy_score(y_test, y_pred)
print(cc)

# K折交叉驗證

from sklearn.model_selection import cross_val_score

scores = cross_val_score(estimator=clf, X=X_test, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.3f}, 標準差: {np.std(scores):.3f}")

"""
K折分數: [0.99915742 0.99929785 0.9988764  0.9997191  0.99901685 0.99901685
 0.9991573  0.99957865 0.9988764  0.9994382 ]
平均值: 0.999, 標準差: 0.000
"""

# 分類報告

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

# 繪製ROC曲線

from sklearn.metrics import roc_curve, roc_auc_score, auc

y_pred_proba = clf.predict_proba(X_test)[:, 1]
fpr, tpr, threshold = roc_curve(y_test, y_pred_proba)
auc1 = auc(fpr, tpr)
plt.title("ROC 曲線")
plt.plot(fpr, tpr, color="orange", label="AUC = %0.2f" % auc1)
plt.legend(loc="lower right")
plt.plot([0, 1], [0, 1], "r--")
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel("真陽率")
plt.xlabel("偽陽率")
show()

# 從寬認定詐欺行為

y_pred_proba = clf.predict_proba(X_test)[:, 1]
y_pred = y_pred_proba >= 0.3
print(classification_report(y_test, y_pred))

# Over-sampling -- SMOTE

# !pip install -U imbalanced-learn

from imblearn.over_sampling import SMOTE
from imblearn.metrics import classification_report_imbalanced

print(df.Class.value_counts())
smote = SMOTE()
X_new, y_new = smote.fit_resample(X, y)
cc = len(y_new[y_new == 0]), len(y_new[y_new == 1])
print(cc)

# 模型訓練與評估

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X_new, y_new)

# 模型訓練
clf = LogisticRegression().fit(X_train, y_train)

# 預測
y_pred = clf.predict(X_test)

# 準確率
cc = accuracy_score(y_test, y_pred)
print(cc)

# K折交叉驗證

from sklearn.model_selection import cross_val_score

scores = cross_val_score(estimator=clf, X=X_test, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.3f}, 標準差: {np.std(scores):.3f}")

"""
K折分數: [0.94499156 0.94379572 0.94569499 0.94541362 0.94442881 0.94288126
 0.94231851 0.95040799 0.94336968 0.94379177]
平均值: 0.945, 標準差: 0.002
"""

# 分類報告

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

# imbalanced-learn 分類報告

from imblearn.metrics import classification_report_imbalanced

print(classification_report_imbalanced(y_test, y_pred))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_01_simple_kmeans_from_scratch
# 自行開發K-Means

# K-Means演算法類別


class Kmeans(object):
    # 訓練
    def fit(self, df, k=3):
        # 任意分成K組
        df["group"] = k - 1
        n = len(df) // 3
        # 前 k-1 組
        for i in range(k - 1):
            for j in range(n):
                df.loc[i * k + j, "group"] = i
        # print(df)

        # 重覆第EM步驟，直到資料所屬組別不再變動為止
        prev_df = pd.DataFrame()
        while not df.equals(prev_df):
            group_mean = df.groupby("group")["goals"].mean()
            print(group_mean)
            prev_df = df.copy()
            for i, row in prev_df.iterrows():
                df.loc[i, "group"] = np.argmin(np.abs(group_mean - row["goals"]))

        self.group_mean = group_mean
        return df

    # 預測
    def predict(self, x):
        return np.argmin(np.abs(self.group_mean - x))


# 載入資料集

df = pd.read_csv("./data/kmeans_data.csv")
print(df)

# 模型訓練

model = Kmeans()
clusters = model.fit(df)
print(clusters)

# 分組結果
grouped_df = clusters.groupby("group")
for key, item in grouped_df:
    print(f"group {key}:")
    print(item["player"].values, "\n")

# 預測

# 預測10個進球數
cc = model.predict(10)  # 第一組
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_02_kmeans_from_scratch

# 自行開發K-Means

# 歐幾里得距離函數


def euclidean(point, data):
    return np.sqrt(np.sum((point - data) ** 2, axis=1))


# K-Means演算法類別


class KMeans:
    def __init__(self, n_clusters=8, max_iter=300):
        self.n_clusters = n_clusters  # 組數
        self.max_iter = max_iter  # EM 最大次數

    # 訓練
    def fit(self, X_train):
        # 生成1個質心
        self.centroids = [random.choice(X_train)]
        # 生成其他 n-1 個質心
        for _ in range(self.n_clusters - 1):
            # Calculate distances from points to the centroids
            dists = np.sum(
                [euclidean(centroid, X_train) for centroid in self.centroids], axis=0
            )
            # 正規化
            dists /= np.sum(dists)
            # 依據距離作為機率，隨機產生質心
            new_centroid_idx = np.random.choice(range(len(X_train)), size=1, p=dists)[0]
            self.centroids += [X_train[new_centroid_idx]]

        iteration = 0
        prev_centroids = [np.zeros(X_train.shape[1])] * self.n_clusters
        while (
            np.not_equal(self.centroids, prev_centroids).any()
            and iteration < self.max_iter
        ):
            # 找到最近的質心
            sorted_points = [[] for _ in range(self.n_clusters)]
            for x in X_train:
                dists = euclidean(x, self.centroids)
                centroid_idx = np.argmin(dists)
                sorted_points[centroid_idx].append(x)

            # 尋找新質心
            prev_centroids = self.centroids
            self.centroids = [np.mean(cluster, axis=0) for cluster in sorted_points]
            for i, centroid in enumerate(self.centroids):
                # 如果組內沒有任何樣本點，沿用上次的質心
                if np.isnan(centroid).any():
                    self.centroids[i] = prev_centroids[i]
            iteration += 1
        # print(iteration)

    # 模型評估
    def evaluate(self, X):
        centroids = []
        centroid_idxs = []
        for x in X:
            dists = euclidean(x, self.centroids)
            centroid_idx = np.argmin(dists)
            centroids.append(self.centroids[centroid_idx])
            centroid_idxs.append(centroid_idx)

        return centroids, centroid_idxs


# 生成分類資料

from sklearn.datasets import make_blobs

X_train, true_labels = make_blobs(n_samples=100, centers=5, random_state=42)
plt.scatter(X_train[:, 0], X_train[:, 1])
show()

# 模型訓練

from sklearn.preprocessing import StandardScaler

# 標準化
X_train = StandardScaler().fit_transform(X_train)

# 訓練
CLUSTERS = 5  # 要分成的群數
kmeans = KMeans(n_clusters=CLUSTERS)
kmeans.fit(X_train)

# 模型評估

class_centers, classification = kmeans.evaluate(X_train)
sns.scatterplot(
    x=[X[0] for X in X_train],
    y=[X[1] for X in X_train],
    hue=true_labels,
    style=classification,
    palette="deep",
    legend=None,
)
plt.plot(
    [x for x, _ in kmeans.centroids],
    [y for _, y in kmeans.centroids],
    "*",
    markersize=20,
    color="r",
)
plt.title("k-means")
show()

# 鳶尾花資料集測試

X, y = datasets.load_iris(return_X_y=True)

# 標準化
X_train = StandardScaler().fit_transform(X)

# 訓練
CLUSTERS = 3  # 要分成的群數
kmeans = KMeans(n_clusters=CLUSTERS)
kmeans.fit(X_train)

# 7

# 模型評估

from sklearn.metrics import accuracy_score

_, y_pred = kmeans.evaluate(X_train)
print(accuracy_score(y, y_pred))

# 0.22

# 驗證

# 實際值
cc = ",".join([str(i) for i in y])
print(cc)

# 預測值
cc = ",".join([str(i) for i in y_pred])
print(cc)

p = pd.Series(y_pred)
print(p[p == 1].index)

p = pd.Series(y)
print(p[p == 0].index)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_06_agglomerative_hierarchical_clustering

# 凝聚階層集群(Agglomerative Hierarchical Clustering, AHC)

# 生成資料
np.random.seed(123)
variables = ["X", "Y", "Z"]
labels = ["ID_0", "ID_1", "ID_2", "ID_3", "ID_4"]

X = np.random.random_sample([5, 3]) * 10
df = pd.DataFrame(X, columns=variables, index=labels)
print(df)

# 計算集群彼此間的距離

from scipy.spatial.distance import pdist, squareform

row_dist = pd.DataFrame(
    squareform(pdist(df, metric="euclidean")), columns=labels, index=labels
)
print(row_dist)

# 計算平均連結距離

from scipy.cluster.hierarchy import linkage

row_clusters = linkage(pdist(df, metric="euclidean"), method="average")
pd.DataFrame(
    row_clusters,
    columns=["row label 1", "row label 2", "distance", "no. of items in clust."],
    index=["cluster %d" % (i + 1) for i in range(row_clusters.shape[0])],
)

# 繪製樹狀圖(dendrogram)

from scipy.cluster.hierarchy import dendrogram

row_dendr = dendrogram(row_clusters, labels=labels)
plt.ylabel("歐幾里德距離", fontsize=14)
show()

# 繪製熱力圖

fig = plt.figure(figsize=(8, 8), facecolor="white")
axd = fig.add_axes([0.09, 0.1, 0.2, 0.6])  # x-pos, y-pos, width, height

# 樹狀圖顯示在左邊
row_dendr = dendrogram(row_clusters, orientation="left")

# 降冪排序
df_rowclust = df.iloc[row_dendr["leaves"][::-1]]

# 不顯示刻度
axd.set_xticks([])
axd.set_yticks([])

# 不顯示座標軸
for i in axd.spines.values():
    i.set_visible(False)

# 繪製熱力圖
axm = fig.add_axes([0.23, 0.1, 0.6, 0.6])  # x-pos, y-pos, width, height
cax = axm.matshow(df_rowclust, interpolation="nearest", cmap="hot_r")
fig.colorbar(cax)
axm.set_xticklabels([""] + list(df_rowclust.columns))
axm.set_yticklabels([""] + list(df_rowclust.index))
show()

# Scikit-learn AgglomerativeClustering

from sklearn.cluster import AgglomerativeClustering

# 分 3 類
ac = AgglomerativeClustering(n_clusters=3, metric="euclidean", linkage="complete")
labels = ac.fit_predict(X)
print("Cluster labels: %s" % labels)

# Cluster labels: [1 0 0 2 1]

# 分 2 類
ac = AgglomerativeClustering(n_clusters=2, metric="euclidean", linkage="complete")
labels = ac.fit_predict(X)
print("Cluster labels: %s" % labels)

# Cluster labels: [0 1 1 0 0]

# 使用鳶尾花資料集測試

from sklearn.datasets import load_iris


# 繪製樹狀圖
def plot_dendrogram(model, **kwargs):
    # 計算每個集群的筆數
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # 繪製樹狀圖
    dendrogram(linkage_matrix, **kwargs)


# 載入資料集
X, _ = load_iris(return_X_y=True)

# distance_threshold=0 表示會建立完整的樹狀圖(dendrogram)
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)

model = model.fit(X)
plt.title("Hierarchical Clustering Dendrogram")
plot_dendrogram(model, truncate_mode="level", p=3)  # 限制 3 層
plt.ylabel("歐幾里德距離", fontsize=14)
plt.xlabel("每個集群的筆數", fontsize=14)
show()

# 各種距離衡量方式的比較

from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import kneighbors_graph

# Generate sample data
n_samples = 1500
np.random.seed(0)
t = 1.5 * np.pi * (1 + 3 * np.random.rand(1, n_samples))
x = t * np.cos(t)
y = t * np.sin(t)


X = np.concatenate((x, y))
X += 0.7 * np.random.randn(2, n_samples)
X = X.T

# Create a graph capturing local connectivity. Larger number of neighbors
# will give more homogeneous clusters to the cost of computation
# time. A very large number of neighbors gives more evenly distributed
# cluster sizes, but may not impose the local manifold structure of
# the data
knn_graph = kneighbors_graph(X, 30, include_self=False)

for connectivity in (None, knn_graph):
    for n_clusters in (30, 3):
        plt.figure(figsize=(10, 4))
        for index, linkage in enumerate(("average", "complete", "ward", "single")):
            plt.subplot(1, 4, index + 1)
            model = AgglomerativeClustering(
                linkage=linkage, connectivity=connectivity, n_clusters=n_clusters
            )
            t0 = time.time()
            model.fit(X)
            elapsed_time = time.time() - t0
            plt.scatter(X[:, 0], X[:, 1], c=model.labels_, cmap=plt.cm.nipy_spectral)
            plt.title(
                "linkage=%s\n(time %.2fs)" % (linkage, elapsed_time),
                fontdict=dict(verticalalignment="top"),
            )
            plt.axis("equal")
            plt.axis("off")

            plt.subplots_adjust(bottom=0, top=0.89, wspace=0, left=0, right=1)
            plt.suptitle(
                "n_cluster=%i, connectivity=%r"
                % (n_clusters, connectivity is not None),
                size=17,
            )
            plt.tight_layout()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_07_dbscan_simple_test

# 以密度為基礎的集群(Density-based spatial clustering of applications with noise, DBSCAN)

from sklearn.cluster import DBSCAN

# 生成資料
X = np.array([[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]])
print(X)

# 模型訓練

model = DBSCAN(eps=3, min_samples=2).fit(X)
print(model.labels_)

# 生成更多資料，且非線性

from sklearn.datasets import make_moons

X, y = make_moons(n_samples=200, noise=0.05, random_state=0)
plt.scatter(X[:, 0], X[:, 1])
show()

# 模型訓練，繪製結果

db = DBSCAN(eps=0.2, min_samples=5, metric="euclidean")
y_pred = db.fit_predict(X)
plt.scatter(
    X[y_pred == 0, 0],
    X[y_pred == 0, 1],
    c="lightblue",
    marker="o",
    s=40,
    edgecolor="black",
    label="cluster 1",
)
plt.scatter(
    X[y_pred == 1, 0],
    X[y_pred == 1, 1],
    c="red",
    marker="s",
    s=40,
    edgecolor="black",
    label="cluster 2",
)
plt.legend()
show()

# 另一個範例，參閱Demo of DBSCAN clustering algorithm

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=750, centers=centers, cluster_std=0.4, random_state=0
)

X = StandardScaler().fit_transform(X)

# 繪製資料

plt.figure(figsize=(10, 8))
plt.scatter(X[:, 0], X[:, 1])
show()

# 模型訓練

labels = DBSCAN(eps=0.3, min_samples=10).fit_predict(X)

# 計算集群內樣本數、雜訊點個數
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print(f"集群數={n_clusters_}")
print(f"雜訊點個數={n_noise_}")

# 集群數=3
# 雜訊點個數=18

# 模型評估

from sklearn import metrics

print(f"Homogeneity: {metrics.homogeneity_score(labels_true, labels):.3f}")
print(f"Completeness: {metrics.completeness_score(labels_true, labels):.3f}")
print(f"V-measure: {metrics.v_measure_score(labels_true, labels):.3f}")
print(f"Adjusted Rand Index: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
print(
    "Adjusted Mutual Information:"
    f" {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}"
)
print(f"Silhouette Coefficient: {metrics.silhouette_score(X, labels):.3f}")

"""
Homogeneity: 0.953
Completeness: 0.883
V-measure: 0.917
Adjusted Rand Index: 0.952
Adjusted Mutual Information: 0.916
Silhouette Coefficient: 0.626
"""

# 繪製結果

plt.figure(figsize=(10, 8))
unique_labels = set(labels)
core_samples_mask = np.zeros_like(labels, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True

colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = labels == k

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=14,
    )

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=6,
    )

plt.title(f"Estimated number of clusters: {n_clusters_}")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_08_gmm_test
# GMM測試，程式修改自Python Data Science Handbook 範例05.12-Gaussian-Mixtures.ipynb

sns.set()

# 生成分類資料
from sklearn.datasets import make_blobs

X, y_true = make_blobs(n_samples=400, centers=4, cluster_std=0.60, random_state=0)
X = X[:, ::-1]  # 特徵互調順序，繪圖效果較佳
print(X[:10])

# 進行 K-Means 集群，並繪圖

from sklearn.cluster import KMeans

CLUSTERS = 4  # 要分成的群數
kmeans = KMeans(CLUSTERS, init="k-means++", n_init=10, random_state=0)

labels = kmeans.fit(X).predict(X)

plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis")

show()

# 繪製集群範圍

from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist


def plot_kmeans(kmeans, X, n_clusters=4, rseed=0, ax=None):
    labels = kmeans.fit_predict(X)

    # 繪製樣本點
    ax = ax or plt.gca()
    ax.axis("equal")
    ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis", zorder=2)

    # 以最大半徑繪製集群範圍
    centers = kmeans.cluster_centers_
    radii = [cdist(X[labels == i], [center]).max() for i, center in enumerate(centers)]
    for c, r in zip(centers, radii):
        ax.add_patch(
            plt.Circle(c, r, fc="#CCCCCC", lw=3, color="k", alpha=0.5, zorder=1)
        )


CLUSTERS = 4  # 要分成的群數
kmeans = KMeans(n_clusters=CLUSTERS, init="k-means++", n_init=10, random_state=0)
plot_kmeans(kmeans, X)
show()

# 生成長條型資料

rng = np.random.RandomState(13)
X_stretched = np.dot(X, rng.randn(2, 2))

CLUSTERS = 4  # 要分成的群數
kmeans = KMeans(n_clusters=CLUSTERS, init="k-means++", n_init=10, random_state=0)
plot_kmeans(kmeans, X_stretched)
show()

# 改用GMM

from sklearn.mixture import GaussianMixture

gmm = GaussianMixture(n_components=4).fit(X)
labels = gmm.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis")
show()

# 屬於各集群的機率

probs = gmm.predict_proba(X)
print(probs[:5].round(3))

# 繪製集群範圍

from matplotlib.patches import Ellipse


# 繪製橢圓
def draw_ellipse(position, covariance, ax=None, **kwargs):
    """Draw an ellipse with a given position and covariance"""
    ax = ax or plt.gca()

    # Convert covariance to principal axes
    if covariance.shape == (2, 2):
        U, s, Vt = np.linalg.svd(covariance)
        angle = np.degrees(np.arctan2(U[1, 0], U[0, 0]))
        width, height = 2 * np.sqrt(s)
    else:
        angle = 0
        width, height = 2 * np.sqrt(covariance)

    # Draw the Ellipse
    for nsig in range(1, 4):
        ax.add_patch(Ellipse(position, nsig * width, nsig * height, angle, **kwargs))


# 繪製GMM範圍
def plot_gmm(gmm, X, label=True, ax=None):
    ax = ax or plt.gca()
    labels = gmm.fit(X).predict(X)
    if label:
        ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis", zorder=2)
    else:
        ax.scatter(X[:, 0], X[:, 1], s=40, zorder=2)
    ax.axis("equal")

    # soft-edged sphere
    w_factor = 0.2 / gmm.weights_.max()
    for pos, covar, w in zip(gmm.means_, gmm.covariances_, gmm.weights_):
        draw_ellipse(pos, covar, alpha=w * w_factor)


gmm = GaussianMixture(n_components=4, random_state=42)
plot_gmm(gmm, X)
show()

# 使用 GMM對長條型資料進行集群

gmm = GaussianMixture(n_components=4, covariance_type="full", random_state=42)
plot_gmm(gmm, X_stretched)
show()

# 測試非線性資料

from sklearn.datasets import make_moons

Xmoon, ymoon = make_moons(200, noise=0.05, random_state=0)
plt.scatter(Xmoon[:, 0], Xmoon[:, 1])
show()

# GMM 集群：設定2個集群

gmm2 = GaussianMixture(n_components=2, covariance_type="full", random_state=0)
plot_gmm(gmm2, Xmoon)
show()

# GMM 集群：設定16個集群

gmm16 = GaussianMixture(n_components=16, covariance_type="full", random_state=0)
plot_gmm(gmm16, Xmoon, label=False)
show()

# 以模型生成資料

Xnew, _ = gmm16.sample(400)
plt.scatter(Xnew[:, 0], Xnew[:, 1])
show()

# 以AIC/BIC決定最佳集群數量

n_components = np.arange(1, 21)
models = [
    GaussianMixture(n, covariance_type="full", random_state=0).fit(Xmoon)
    for n in n_components
]

plt.plot(n_components, [m.bic(Xmoon) for m in models], label="BIC")
plt.plot(n_components, [m.aic(Xmoon) for m in models], label="AIC")
plt.legend(loc="best")
plt.xlabel("n_components")
show()

# 生成手寫阿拉伯數字

from sklearn.datasets import load_digits

digits = load_digits()
cc = digits.data.shape
print(cc)

# (1797, 64)

# 顯示前 100 筆手寫阿拉伯數字


def plot_digits(data):
    fig, ax = plt.subplots(
        10, 10, figsize=(8, 8), subplot_kw=dict(xticks=[], yticks=[])
    )
    fig.subplots_adjust(hspace=0.05, wspace=0.05)
    for i, axi in enumerate(ax.flat):
        im = axi.imshow(data[i].reshape(8, 8), cmap="binary")
        im.set_clim(0, 16)


plot_digits(digits.data)
show()

# 降維

from sklearn.decomposition import PCA

pca = PCA(0.99, whiten=True)
data = pca.fit_transform(digits.data)
print(data.shape)

# (1797, 41)

# 以AIC決定最佳集群數量

n_components = np.arange(50, 210, 10)
models = [GaussianMixture(n, covariance_type="full") for n in n_components]
aics = [model.fit(data).aic(data) for model in models]
plt.plot(n_components, aics)
show()

# 以AIC決定最佳集群數量=110
# 設定集群數量=110

gmm = GaussianMixture(110, covariance_type="full", random_state=0)
gmm.fit(data)
print(gmm.converged_)

# True

# Now we can draw samples of 100 new points within this 41-dimensional projected space, using the GMM as a generative model:

# 生成100個樣本

data_new, _ = gmm.sample(100)
digits_new = pca.inverse_transform(data_new)
plot_digits(digits_new)
show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_09_image_compression

# 影像壓縮(Image Compression)

from sklearn.utils import shuffle
from sklearn.datasets import load_sample_image
from sklearn.cluster import KMeans

# 載入測試圖片

flower = load_sample_image("flower.jpg")
plt.axis("off")
plt.imshow(flower)

show()

# 存檔
plt.imsave("tmp_flower.jpg", flower)

# 正規化、取得圖片寬高及顏色維度、將寬高轉為一維

# 正規化
flower = np.array(flower, dtype=np.float64) / 255

# 取得圖片寬高及顏色維度
w, h, d = tuple(flower.shape)

# 將寬高轉為一維
image_array = np.reshape(flower, (w * h, d))
print(w, h, d)

# (427, 640, 3)

# 模型訓練及預測

# 隨機抽樣1000個像素
image_sample = shuffle(image_array, random_state=42)[:1000]

# K-Means模型訓練， 設定64個集群
CLUSTERS = 64  # 要分成的群數
kmeans = KMeans(n_clusters=CLUSTERS, random_state=42).fit(image_sample)

# 對所有像素進行集群
labels = kmeans.predict(image_array)

# 重建影像的函數


def reconstruct_image(cluster_centers, labels, w, h):
    d = cluster_centers.shape[1]
    image = np.zeros((w, h, d))
    label_index = 0
    for i in range(w):
        for j in range(h):
            # 以質心取代原圖像顏色
            image[i][j] = cluster_centers[labels[label_index]]
            label_index += 1
    return image


# 比較原圖與減色後的圖片

plt.figure(figsize=(14, 7))

# 原圖
plt.subplot(1, 2, 1)
plt.axis("off")
plt.title("原圖")
plt.imshow(flower)

plt.subplot(1, 2, 2)
plt.axis("off")
plt.title("重建的影像")
plt.imshow(reconstruct_image(kmeans.cluster_centers_, labels, w, h))
show()

# 再使用K-Means，設定4個集群

# K-Means模型訓練， 設定4個集群
CLUSTERS = 4  # 要分成的群數
kmeans = KMeans(n_clusters=CLUSTERS, random_state=42).fit(image_sample)

# 對所有像素進行集群
labels = kmeans.predict(image_array)

plt.figure(figsize=(14, 7))
# 原圖
plt.subplot(1, 2, 1)
plt.axis("off")
plt.title("原圖")
plt.imshow(flower)

plt.subplot(1, 2, 2)
plt.axis("off")
plt.title("重建的影像")
plt.imshow(reconstruct_image(kmeans.cluster_centers_, labels, w, h))
show()

# 存檔
plt.imsave(
    "tmp_flower_kmeans.jpg", reconstruct_image(kmeans.cluster_centers_, labels, w, h)
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_10_customer_segmentation
# 客戶區隔(Customer segmentation)

# 載入資料集
df = pd.read_csv(
    "C:/_git/vcs/_big_files/Scikit-learn_data/invoice.csv", encoding="ISO-8859-1"
)

# 只分析英國的顧客
df = df[df.Country == "United Kingdom"]
cc = df.head()
print(cc)

# 描述統計量
# df.describe().T

# 資料清理

# 移除非購買記錄

# 移除數量<=0的交易記錄
df = df[df["Quantity"] > 0]

# 移除單價<=0的交易記錄
df = df[df["UnitPrice"] > 0]
print(df.Quantity.describe())
cc = df.UnitPrice.describe()
print(cc)

# 刪除 Missing Value
df.dropna(subset=["CustomerID"], inplace=True)

# 檢查 Missing Value
cc = df.isnull().sum()
print(cc)

# 找出資料集的最近購買日期

# 找出資料集的最近購買日期
print(df["InvoiceDate"].max())

# 日期轉 YYYY-MM-DD
cc = df["date"] = pd.DatetimeIndex(df.InvoiceDate).date
print(cc)

# 計算 Recency

# 計算每個顧客的最近購買日期
recency_df = df.groupby(["CustomerID"], as_index=False)["date"].max()
recency_df.columns = ["CustomerID", "LastPurchaseDate"]

# 計算每個顧客的上次消費的日期距今天數
now = df["date"].max()
recency_df["Recency"] = recency_df.LastPurchaseDate.apply(lambda x: (now - x).days)
cc = recency_df.head()
print(cc)

recency_df.drop(columns=["LastPurchaseDate"], inplace=True)

# 計算 Frequency

# 計算每個顧客的消費次數
frequency_df = df.copy()
frequency_df.drop_duplicates(
    subset=["CustomerID", "InvoiceNo"], keep="first", inplace=True
)
frequency_df = frequency_df.groupby("CustomerID", as_index=False)["InvoiceNo"].count()
frequency_df.columns = ["CustomerID", "Frequency"]
cc = frequency_df.head()
print(cc)

# 計算 Monetary

# 計算每個顧客的累計消費金額
df["Total_cost"] = df["UnitPrice"] * df["Quantity"]
monetary_df = df.groupby("CustomerID", as_index=False)["Total_cost"].sum()
monetary_df.columns = ["CustomerID", "Monetary"]
cc = monetary_df.head()
print(cc)

# 合併 RFM

rf = recency_df.merge(frequency_df, left_on="CustomerID", right_on="CustomerID")
rfm = rf.merge(monetary_df, left_on="CustomerID", right_on="CustomerID")
rfm.set_index("CustomerID", inplace=True)
cc = rfm.head()
print(cc)

# 驗算

cc = df[df.CustomerID == 12346.0]
print(cc)

import datetime as dt

now = dt.date(2011, 12, 9)
cc = (now - dt.date(2011, 1, 18)).days == 325
print(cc)

# True

# 使用K-Means進行集群

from sklearn.cluster import KMeans

# 複製資料
rfm_segmentation = rfm.copy()

# 轉折判斷法
Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i, init="k-means++", n_init="auto") for i in Nc]
for i in range(len(kmeans)):
    kmeans[i].fit(rfm_segmentation)
score = [kmeans[i].score(rfm_segmentation) for i in range(len(kmeans))]
wcss = [kmeans[i].inertia_ for i in range(len(kmeans))]

plt.plot(Nc, score)
plt.xticks(range(0, 20, 2))
plt.xlabel("Number of Clusters")
plt.ylabel("Score")
plt.title("Elbow Curve")
show()

plt.plot(Nc, wcss)
plt.xticks(range(0, 20, 2))
plt.xlabel("Number of Clusters")
plt.ylabel("wcss")
plt.title("Elbow Curve")
show()

# 分成3群

X = rfm_segmentation.copy()
kmeans = KMeans(
    n_clusters=3, init="k-means++", n_init=10, max_iter=300, random_state=0
).fit(X)

# 新增欄位，加入集群代碼
rfm_segmentation["cluster"] = kmeans.labels_

# 觀看集群 0 的前 10 筆資料
cc = rfm_segmentation[rfm_segmentation.cluster == 0].head(10)
print(cc)

# 計算每群筆數

cc = rfm_segmentation["cluster"].value_counts()
print(cc)

# 輪廓係數

from sklearn.metrics import silhouette_samples

y_km = rfm_segmentation["cluster"]
cluster_labels = np.unique(y_km)
n_clusters = cluster_labels.shape[0]
silhouette_vals = silhouette_samples(X, y_km, metric="euclidean")
cc = silhouette_vals
print(cc)

# 繪製輪廓圖

from matplotlib import cm

# 輪廓圖
y_ax_lower, y_ax_upper = 0, 0
yticks = []
for i, c in enumerate(cluster_labels):
    c_silhouette_vals = silhouette_vals[y_km == c]
    c_silhouette_vals.sort()
    y_ax_upper += len(c_silhouette_vals)
    color = cm.jet(float(i) / n_clusters)
    plt.barh(
        range(y_ax_lower, y_ax_upper),
        c_silhouette_vals,
        height=1.0,
        edgecolor="none",
        color=color,
    )

    yticks.append((y_ax_lower + y_ax_upper) / 2.0)
    y_ax_lower += len(c_silhouette_vals)

# 輪廓係數平均數的垂直線
silhouette_avg = np.mean(silhouette_vals)
plt.axvline(silhouette_avg, color="red", linestyle="--")

plt.yticks(yticks, cluster_labels + 1)
plt.ylabel("集群", fontsize=14)
plt.xlabel("輪廓係數", fontsize=14)
plt.tight_layout()
show()

# 依據輪廓分數找最佳集群數量

# 測試 2~20 群的分數
from sklearn.metrics import silhouette_score

silhouette_score_list = []
print("1輪廓分數:")
for i in range(2, 21):
    km = KMeans(n_clusters=i, init="k-means++", n_init=10, max_iter=300, random_state=0)
    km.fit(X)
    y_km = km.fit_predict(X)
    silhouette_score_list.append(silhouette_score(X, y_km))
    print(f"{i}:{silhouette_score_list[-1]:.2f}")

print(f"最大值 {np.argmax(silhouette_score_list)+2}: {np.max(silhouette_score_list):.2f}")

for i in range(2, 21):
    print(i)
    CLUSTERS = i  # 要分成的群數
    km = KMeans(
        n_clusters=CLUSTERS, init="k-means++", n_init=10, max_iter=300, random_state=0
    ).fit(X)

    # 新增欄位，加入集群代碼
    y_km = km.labels_
    cluster_labels = np.unique(y_km)
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(X, y_km, metric="euclidean")

    # 輪廓圖
    y_ax_lower, y_ax_upper = 0, 0
    yticks = []
    for i, c in enumerate(cluster_labels):
        c_silhouette_vals = silhouette_vals[y_km == c]
        c_silhouette_vals.sort()
        y_ax_upper += len(c_silhouette_vals)
        color = cm.jet(float(i) / n_clusters)
        plt.barh(
            range(y_ax_lower, y_ax_upper),
            c_silhouette_vals,
            height=1.0,
            edgecolor="none",
            color=color,
        )

        yticks.append((y_ax_lower + y_ax_upper) / 2.0)
        y_ax_lower += len(c_silhouette_vals)

    # 輪廓係數平均數的垂直線
    silhouette_avg = np.mean(silhouette_vals)
    plt.axvline(silhouette_avg, color="red", linestyle="--")

    plt.yticks(yticks, cluster_labels + 1)
    plt.ylabel("集群", fontsize=14)
    plt.xlabel("輪廓係數", fontsize=14)
    plt.tight_layout()
    show()

# RFM 分組


# 四分位數分組
def RScore(x, p, d):
    if x <= d[p][0.25]:
        return 1
    elif x <= d[p][0.50]:
        return 2
    elif x <= d[p][0.75]:
        return 3
    else:
        return 4


def FMScore(x, p, d):
    if x <= d[p][0.25]:
        return 4
    elif x <= d[p][0.50]:
        return 3
    elif x <= d[p][0.75]:
        return 2
    else:
        return 1


# 四分位數(quantile)
quantile = rfm.quantile(q=[0.25, 0.5, 0.75])
print(quantile)

cc = quantile.to_dict()
print(cc)

# RFM依四分位數給分

rfm_segmentation["R_Quartile"] = rfm_segmentation["Recency"].apply(
    RScore, args=("Recency", quantile)
)
rfm_segmentation["F_Quartile"] = rfm_segmentation["Frequency"].apply(
    FMScore, args=("Frequency", quantile)
)
rfm_segmentation["M_Quartile"] = rfm_segmentation["Monetary"].apply(
    FMScore, args=("Monetary", quantile)
)
cc = rfm_segmentation.head()
print(cc)

# 合併 RFM 分數
rfm_segmentation["RFMScore"] = (
    rfm_segmentation.R_Quartile.map(str)
    + rfm_segmentation.F_Quartile.map(str)
    + rfm_segmentation.M_Quartile.map(str)
)
cc = rfm_segmentation.head()
print(cc)

# 計算 RFM 總分
rfm_segmentation["Total_score"] = (
    rfm_segmentation["R_Quartile"]
    + rfm_segmentation["F_Quartile"]
    + rfm_segmentation["M_Quartile"]
)

cc = rfm_segmentation.head()
print(cc)

print("客戶篩選：")
print("Best Customers: ", len(rfm_segmentation[rfm_segmentation["RFMScore"] == "111"]))
print("Loyal Customers: ", len(rfm_segmentation[rfm_segmentation["F_Quartile"] == 1]))
print("Big Spenders: ", len(rfm_segmentation[rfm_segmentation["M_Quartile"] == 1]))
print("Almost Lost: ", len(rfm_segmentation[rfm_segmentation["RFMScore"] == "134"]))
print("Lost Customers: ", len(rfm_segmentation[rfm_segmentation["RFMScore"] == "344"]))
print(
    "Lost Cheap Customers: ",
    len(rfm_segmentation[rfm_segmentation["RFMScore"] == "444"]),
)
"""
客戶篩選：
Best Customers:  423
Loyal Customers:  791
Big Spenders:  980
Almost Lost:  31
Lost Customers:  187
Lost Cheap Customers:  396
"""
# 依分數顯示客戶名單
cc = rfm_segmentation.sort_values(
    by=["RFMScore", "Monetary"], ascending=[True, False]
).head(10)
print(cc)

# 依RFM級數顯示每一組的平均消費金額
cc = rfm_segmentation.groupby("RFMScore")["Monetary"].mean().head(10)
print(cc)

# 依RFM總分顯示每一組的平均消費金額
cc = rfm_segmentation.groupby("Total_score")["Monetary"].mean()

# 依RFM總分作圖，總分 3,4,5 有最高消費金額
rfm_segmentation.groupby("Total_score")["Monetary"].mean().plot(
    kind="bar", colormap="Blues_r"
)
show()

# 依RFM總分作圖，總分 3,4,5 有最高消費次數
rfm_segmentation.groupby("Total_score")["Frequency"].mean().plot(
    kind="bar", colormap="Blues_r"
)
show()

# 依RFM總分作圖，總分 10,11,12 Recency最高
rfm_segmentation.groupby("Total_score")["Recency"].mean().plot(
    kind="bar", colormap="Blues_r"
)
show()

# 依據輪廓分數找最佳集群數量

# 測試 2~20 群的分數
from sklearn.metrics import silhouette_score

X = rfm_segmentation[["R_Quartile", "F_Quartile", "M_Quartile"]]
silhouette_score_list = []
print("2輪廓分數:")
for i in range(2, 21):
    print(i)
    CLUSTERS = i  # 要分成的群數
    km = KMeans(
        n_clusters=CLUSTERS, init="k-means++", n_init=10, max_iter=300, random_state=0
    )
    km.fit(X)
    y_km = km.fit_predict(X)
    silhouette_score_list.append(silhouette_score(X, y_km))
    print(f"{i}:{silhouette_score_list[-1]:.2f}")

print(f"最大值 {np.argmax(silhouette_score_list)+2}: {np.max(silhouette_score_list):.2f}")

for i in range(2, 21):
    print(i)
    CLUSTERS = i  # 要分成的群數
    km = KMeans(
        n_clusters=CLUSTERS, init="k-means++", n_init=10, max_iter=300, random_state=0
    ).fit(X)

    # 新增欄位，加入集群代碼
    y_km = km.labels_
    cluster_labels = np.unique(y_km)
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(X, y_km, metric="euclidean")

    # 輪廓圖
    y_ax_lower, y_ax_upper = 0, 0
    yticks = []
    for i, c in enumerate(cluster_labels):
        c_silhouette_vals = silhouette_vals[y_km == c]
        c_silhouette_vals.sort()
        y_ax_upper += len(c_silhouette_vals)
        color = cm.jet(float(i) / n_clusters)
        plt.barh(
            range(y_ax_lower, y_ax_upper),
            c_silhouette_vals,
            height=1.0,
            edgecolor="none",
            color=color,
        )

        yticks.append((y_ax_lower + y_ax_upper) / 2.0)
        y_ax_lower += len(c_silhouette_vals)

    # 輪廓係數平均數的垂直線
    silhouette_avg = np.mean(silhouette_vals)
    plt.axvline(silhouette_avg, color="red", linestyle="--")

    plt.yticks(yticks, cluster_labels + 1)
    plt.ylabel("集群", fontsize=14)
    plt.xlabel("輪廓係數", fontsize=14)
    plt.tight_layout()
    show()

# 分成4個集群

CLUSTERS = 4  # 要分成的群數
kmeans = KMeans(n_clusters=CLUSTERS, random_state=0).fit(X)

# 新增欄位，加入集群代碼
rfm_segmentation["cluster"] = kmeans.labels_

# 觀看集群 0 的前 10 筆資料
cc = rfm_segmentation[rfm_segmentation.cluster == 0].head(10)
print(cc)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors

fig = plt.figure(figsize=(12, 8))
dx = fig.add_subplot(111, projection="3d")
colors = ["green", "blue", "red", "yellow"]

for i in range(rfm_segmentation.cluster.nunique()):
    dx.scatter(
        rfm_segmentation[rfm_segmentation.cluster == i].R_Quartile,
        rfm_segmentation[rfm_segmentation.cluster == i].F_Quartile,
        rfm_segmentation[rfm_segmentation.cluster == i].M_Quartile,
        c=colors[i],
        label="Cluster " + str(i),
        s=10,
        alpha=1.0,
    )

dx.set_xlabel("Recency", fontsize=14)
dx.set_ylabel("Frequency", fontsize=14)
dx.set_zlabel("Monetary", fontsize=14)
dx.legend(fontsize=12)
plt.tight_layout()
show()

cc = rfm_segmentation.cluster.value_counts()
print(cc)

cc = rfm_segmentation.groupby("cluster")[
    ["R_Quartile", "F_Quartile", "M_Quartile", "Total_score"]
].mean()
print(cc)

# 結論
# 集群 1為VIP，其他依序為3、2、0。

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_01_error_rate

# 整體學習的錯誤率計算

from scipy.special import comb

# 計算整體學習的錯誤率


def ensemble_error(n_classifier, error):
    k_start = int(math.ceil(n_classifier / 2.0))
    probs = [
        comb(n_classifier, k) * error**k * (1 - error) ** (n_classifier - k)
        for k in range(k_start, n_classifier + 1)
    ]
    return sum(probs)


cc = ensemble_error(n_classifier=11, error=0.25)
print(cc)

# 0.03432750701904297

# 測試各種錯誤率，並繪圖

error_range = np.arange(0.0, 1.01, 0.01)
ens_errors = [ensemble_error(n_classifier=11, error=error) for error in error_range]

# 修正中文亂碼
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

plt.plot(error_range, ens_errors, label="整體學習", linewidth=2)

plt.plot(error_range, error_range, linestyle="--", label="個別模型", linewidth=2)

plt.title("錯誤率比較", fontsize=18)
plt.xlabel("個別模型錯誤率", fontsize=14)
plt.ylabel("整體學習錯誤率", fontsize=14)
plt.legend(loc="upper left", fontsize=14)
plt.grid(alpha=0.5)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_02_majority_voting
# 多數決演算法(VotingClassifier)測試

# 載入資料集
X, y = datasets.load_breast_cancer(return_X_y=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練

from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.naive_bayes import GaussianNB

estimators = [("svc", SVC()), ("rf", RandomForestClassifier()), ("nb", GaussianNB())]
clf = VotingClassifier(estimators)
clf.fit(X_train_std, y_train)  # 學習訓練.fit

"""
VotingClassifier(estimators=[('svc', SVC()), ('rf', RandomForestClassifier()),
                             ('nb', GaussianNB())])
"""

# 模型評估

# 計算準確率
print(f"{clf.score(X_test_std, y_test)*100:.2f}%")
# 97.37%

# 個別模型評估

svc = SVC()

svc.fit(X_train_std, y_train)  # 學習訓練.fit
print(f"{svc.score(X_test_std, y_test)*100:.2f}%")

# 98.25%

rf = RandomForestClassifier()

rf.fit(X_train_std, y_train)  # 學習訓練.fit
print(f"{rf.score(X_test_std, y_test)*100:.2f}%")
# 98.25%

nb = GaussianNB()

nb.fit(X_train_std, y_train)  # 學習訓練.fit
print(f"{nb.score(X_test_std, y_test)*100:.2f}%")
# 93.86%

# 模型預測
cc = clf.predict(X_test_std)
print(cc)

# 交叉驗證

from sklearn.model_selection import cross_val_score

scores = cross_val_score(estimator=clf, X=X_test_std, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [0.91666667 1.         0.91666667 0.91666667 0.90909091 1.
 0.90909091 0.90909091 1.         1.        ]
平均值: 0.95, 標準差: 0.04
"""

scores = cross_val_score(estimator=svc, X=X_test_std, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [0.91666667 1.         0.91666667 1.         0.90909091 1.
 0.90909091 0.90909091 1.         1.        ]
平均值: 0.96, 標準差: 0.04
"""

scores = cross_val_score(estimator=rf, X=X_test_std, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [0.83333333 0.91666667 0.91666667 0.91666667 1.         1.
 1.         1.         1.         1.        ]
平均值: 0.96, 標準差: 0.06
"""

scores = cross_val_score(estimator=nb, X=X_test_std, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [1.         1.         0.91666667 0.91666667 0.90909091 1.
 0.81818182 0.90909091 1.         1.        ]
平均值: 0.95, 標準差: 0.06
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_03_bagging_classifier

# Bagging演算法測試

# 載入資料集
X, y = datasets.load_breast_cancer(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練

from sklearn.ensemble import BaggingClassifier
from sklearn.naive_bayes import GaussianNB

base_estimator = GaussianNB()

clf = BaggingClassifier(estimator=base_estimator, n_estimators=50)

clf.fit(X_train_std, y_train)  # 學習訓練.fit

"""
BaggingClassifier(estimator=GaussianNB(), n_estimators=50)
"""

# 模型評估

# 計算準確率
print(f"{clf.score(X_test_std, y_test)*100:.2f}%")
# 90.35%

# 個別模型評估
nb = GaussianNB()

nb.fit(X_train_std, y_train)  # 學習訓練.fit
print(f"{nb.score(X_test_std, y_test)*100:.2f}%")
# 90.35%

# 模型預測

cc = clf.predict(X_test_std)
print(cc)

# 交叉驗證

from sklearn.model_selection import cross_val_score

clf2 = BaggingClassifier(estimator=base_estimator, n_estimators=50)
scores = cross_val_score(estimator=clf2, X=X_test_std, y=y_test, cv=10, n_jobs=-1)

print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [0.83333333 0.75       0.91666667 0.83333333 0.90909091 0.90909091
 1.         1.         0.90909091 1.        ]
平均值: 0.91, 標準差: 0.08
"""
scores = cross_val_score(
    estimator=GaussianNB(), X=X_test_std, y=y_test, cv=10, n_jobs=-1
)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [0.83333333 0.66666667 0.91666667 0.83333333 0.81818182 0.90909091
 1.         1.         0.90909091 1.        ]
平均值: 0.89, 標準差: 0.10
"""

# 使用較複雜的資料集

from sklearn.datasets import make_classification

# 生成隨機分類資料
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    flip_y=0.3,
    random_state=5,
    shuffle=False,
)

# BaggingClassifier 交叉驗證
base_estimator = GaussianNB()
clf3 = BaggingClassifier(estimator=base_estimator)
scores = cross_val_score(estimator=clf3, X=X, y=y, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [0.63 0.89 0.91 0.92 0.53 0.57 0.82 0.73 0.79 0.56]
平均值: 0.73, 標準差: 0.14
"""
scores = cross_val_score(estimator=base_estimator, X=X, y=y, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [0.63 0.89 0.9  0.93 0.54 0.58 0.82 0.72 0.79 0.56]
平均值: 0.74, 標準差: 0.14
"""

# 參數調校

# explore bagging ensemble k for knn effect on performance
from numpy import mean
from numpy import std
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.neighbors import KNeighborsClassifier


# get the dataset
def get_dataset():
    X, y = make_classification(
        n_samples=1000, n_features=20, n_informative=15, n_redundant=5, random_state=5
    )
    return X, y


# get a list of models to evaluate
def get_models():
    models = dict()
    # evaluate k values from 1 to 20
    for i in range(1, 21):
        # define the base model
        base = KNeighborsClassifier(n_neighbors=i)
        # define the ensemble model
        models[str(i)] = BaggingClassifier(base)
    return models


# evaluate a given model using cross-validation
def evaluate_model(model, X, y):
    # define the evaluation procedure
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    # evaluate the model and collect the results
    scores = cross_val_score(model, X, y, scoring="accuracy", cv=cv, n_jobs=-1)
    return scores


# define dataset
X, y = get_dataset()
# get the models to evaluate
models = get_models()
# evaluate the models and store results
results, names = list(), list()
for name, model in models.items():
    # evaluate the model
    scores = evaluate_model(model, X, y)
    # store the results
    results.append(scores)
    names.append(name)
    # summarize the performance along the way
    print(">%s %.3f (%.3f)" % (name, mean(scores), std(scores)))
# plot model performance for comparison
plt.boxplot(results, labels=names, showmeans=True)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_04_adaboost_from_scratch

# 自行開發Adaboost

# 載入資料集
X, y = datasets.load_breast_cancer(return_X_y=True)
y[y == 0] = -1
# X, y = datasets.make_hastie_10_2()
print(y)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 建立Adaboost模型


# 計算錯誤率
def get_error_rate(pred, Y):
    return sum(pred != Y) / float(len(Y))


# Adaboost模型
def Adaboost(Y_train, X_train, Y_test, X_test, M, clf):
    n_train, n_test = len(X_train), len(X_test)
    # 初始化權重(weights)，每一筆資料權重都一樣
    w = np.ones(n_train) / n_train
    # 預測初始值為 0
    pred_train, pred_test = [np.zeros(n_train), np.zeros(n_test)]

    # 訓練 M 次
    for i in range(M):
        # 訓練
        clf.fit(X_train, Y_train, sample_weight=w)  # 學習訓練.fit
        pred_train_i = clf.predict(X_train)
        pred_test_i = clf.predict(X_test)

        # 更新權重，預測正確為 1，預測錯誤為 -1
        miss = [int(x) for x in (pred_train_i != Y_train)]
        miss2 = [x if x == 1 else -1 for x in miss]
        # 計算分類錯誤率
        err_m = np.dot(w, miss) / sum(w)
        # 計算 θ
        theta_m = 0.5 * np.log((1 - err_m) / float(err_m))
        # 權重更新
        w = np.multiply(w, np.exp([float(x) * theta_m for x in miss2]))
        # 累加至預測值
        pred_train = [
            sum(x) for x in zip(pred_train, [x * theta_m for x in pred_train_i])
        ]
        pred_test = [sum(x) for x in zip(pred_test, [x * theta_m for x in pred_test_i])]

    # np.sign：returns -1 if x < 0, 0 if x==0, 1 if x > 0
    pred_train, pred_test = np.sign(pred_train), np.sign(pred_test)
    # 回傳訓練及測試資料的錯誤率
    return get_error_rate(pred_train, Y_train), get_error_rate(pred_test, Y_test)


# 模型訓練

from sklearn.tree import DecisionTreeClassifier

# max_depth 一定要設定
weak_learner = DecisionTreeClassifier(max_depth=3)
pred = Adaboost(y_train, X_train, y_test, X_test, 50, weak_learner)

# 模型評估

# 計算準確率
print(f"{(1-pred[1])*100:.2f}%")
# 97.37%

# 個別模型評估
weak_learner.fit(X_train, y_train)  # 學習訓練.fit
print(f"{weak_learner.score(X_test, y_test)*100:.2f}%")
# 93.86%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_06_gradient_boost

# 自行開發『梯度提升決策樹』(Gradient Boosting Decision Tree)

# 載入資料集
X, y = datasets.load_diabetes(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 建立Gradient Boost模型
from sklearn.tree import DecisionTreeRegressor


class GradientBooster:
    # 初始化
    def __init__(
        self,
        max_depth=8,
        min_samples_split=5,
        min_samples_leaf=5,
        max_features=3,
        lr=0.1,
        num_iter=1000,
    ):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.max_features = max_features
        self.lr = lr
        self.num_iter = num_iter
        self.y_mean = 0

    # 計算 MSE
    def __calculate_loss(self, y, y_pred):
        loss = (1 / len(y)) * 0.5 * np.sum(np.square(y - y_pred))
        return loss

    # 計算梯度
    def __take_gradient(self, y, y_pred):
        grad = -(y - y_pred)
        return grad

    # 單一模型訓練
    def __create_base_model(self, X, y):
        base = DecisionTreeRegressor(
            criterion="squared_error",
            max_depth=self.max_depth,
            min_samples_split=self.min_samples_split,
            min_samples_leaf=self.min_samples_leaf,
            max_features=self.max_features,
        )
        base.fit(X, y)  # 學習訓練.fit
        return base

    # 預測
    def predict(self, models, X):
        pred_0 = np.array([self.y_mean] * X.shape[0])
        pred = pred_0  # .reshape(len(pred_0),1)

        # 加法模型預測
        for i in range(len(models)):
            temp = models[i].predict(X)
            pred -= self.lr * temp

        return pred

    # 模型訓練
    def train(self, X, y):
        models = []
        losses = []
        self.y_mean = np.mean(y)
        pred = np.array([np.mean(y)] * len(y))

        # 加法模型訓練
        for epoch in range(self.num_iter):
            loss = self.__calculate_loss(y, pred)
            losses.append(loss)
            grads = self.__take_gradient(y, pred)
            base = self.__create_base_model(X, grads)
            r = base.predict(X)
            pred -= self.lr * r
            models.append(base)

        return models, losses, pred


# 模型訓練

G = GradientBooster()
models, losses, pred = G.train(X_train, y_train)

# 繪製損失函數

sns.set_style("darkgrid")
ax = sns.lineplot(x=range(1000), y=losses)
ax.set(xlabel="Epoch", ylabel="Loss", title="Loss vs Epoch")
show()

# 模型評估

from sklearn.metrics import mean_squared_error

y_pred = G.predict(models, X_test)
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# RMSE: 62.47630199377564

# 個別模型評估

model = DecisionTreeRegressor(
    max_depth=8, min_samples_split=5, min_samples_leaf=5, max_features=3
)

model.fit(X_train, y_train)  # 學習訓練.fit

y_pred = model.predict(X_test)
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# RMSE: 75.54768636162939

# Scikit-learn GradientBoostingRegressor 模型評估

from sklearn.ensemble import GradientBoostingRegressor

model = GradientBoostingRegressor(
    n_estimators=1000,
    criterion="squared_error",
    max_depth=8,
    min_samples_split=5,
    min_samples_leaf=5,
    max_features=3,
)

model.fit(X_train, y_train)  # 學習訓練.fit

y_pred = model.predict(X_test)
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# RMSE: 60.69114783838949

# Scikit-learn GradientBoostingClassifier 模型評估

from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier

X, y = make_hastie_10_2(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = GradientBoostingClassifier(
    n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0
).fit(
    X_train, y_train
)  # 學習訓練.fit

cc = clf.score(X_test, y_test)
print(cc)

# 0.9229166666666667

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_07_xgboost

# XGBoost測試

#!pip install xgboost -U

"""
Requirement already satisfied: xgboost in c:\anaconda3\lib\site-packages (1.6.1)
Collecting xgboost
  Downloading xgboost-1.7.3-py3-none-win_amd64.whl (89.1 MB)
     ---------------------------------------- 89.1/89.1 MB 8.7 MB/s eta 0:00:00
Requirement already satisfied: numpy in c:\anaconda3\lib\site-packages (from xgboost) (1.23.5)
Requirement already satisfied: scipy in c:\anaconda3\lib\site-packages (from xgboost) (1.9.3)
Installing collected packages: xgboost
  Attempting uninstall: xgboost
    Found existing installation: xgboost 1.6.1
    Uninstalling xgboost-1.6.1:
      Successfully uninstalled xgboost-1.6.1
Successfully installed xgboost-1.7.3

"""

# 載入資料集
X, y = datasets.load_diabetes(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練
from xgboost import XGBRegressor

model = XGBRegressor()

model.fit(X_train, y_train)  # 學習訓練.fit

"""
XGBRegressor(base_score=None, booster=None, callbacks=None,
             colsample_bylevel=None, colsample_bynode=None,
             colsample_bytree=None, early_stopping_rounds=None,
             enable_categorical=False, eval_metric=None, feature_types=None,
             gamma=None, gpu_id=None, grow_policy=None, importance_type=None,
             interaction_constraints=None, learning_rate=None, max_bin=None,
             max_cat_threshold=None, max_cat_to_onehot=None,
             max_delta_step=None, max_depth=None, max_leaves=None,
             min_child_weight=None, missing=nan, monotone_constraints=None,
             n_estimators=100, n_jobs=None, num_parallel_tree=None,
             predictor=None, random_state=None, ...)
"""

# 模型評估

from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X_test, y_test, cv=10, scoring="neg_mean_squared_error")
print(scores)

# 平均分數與標準差

print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: -5473.1857409034155, 標準差: 3004.388074594913


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用分類模型

from xgboost import XGBClassifier

X, y = datasets.load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = XGBClassifier()

model.fit(X_train, y_train)  # 學習訓練.fit

scores = cross_val_score(model, X_test, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: 0.9484848484848485, 標準差: 0.05626498372008225

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_08_stacking
# 堆疊(Stacking)測試

# 載入資料集
X, y = datasets.load_breast_cancer(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import StackingClassifier


def get_models():
    models = []
    models.append(("knn", KNeighborsClassifier()))
    models.append(("cart", DecisionTreeClassifier()))
    models.append(("svm", SVC()))
    models.append(("bayes", GaussianNB()))
    return models


estimators = get_models()
model = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression())

model.fit(X_train, y_train)  # 學習訓練.fit

"""
StackingClassifier(estimators=[('knn', KNeighborsClassifier()),
                               ('cart', DecisionTreeClassifier()),
                               ('svm', SVC()), ('bayes', GaussianNB())],
                   final_estimator=LogisticRegression())
"""

# 模型評估

from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X_test, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: 0.9303030303030303, 標準差: 0.08393720596645175


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用迴歸模型

from sklearn.linear_model import RidgeCV
from sklearn.svm import LinearSVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.preprocessing import StandardScaler

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

estimators = [("lr", RidgeCV()), ("svr", LinearSVR(random_state=42))]

model = StackingRegressor(
    estimators=estimators,
    final_estimator=RandomForestRegressor(n_estimators=10, random_state=42),
)

model.fit(X_train_std, y_train)  # 學習訓練.fit

scores = cross_val_score(model, X_test_std, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")
# 平均分數: 0.12143159519945441, 標準差: 0.4732757387323812

svc = LinearSVR()

svc.fit(X_train_std, y_train)  # 學習訓練.fit

scores = cross_val_score(svc, X_test_std, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: -1.0399780386178537, 標準差: 0.36412901584183494

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_01_self_training

# 自我訓練(Self-training)測試

from sklearn.svm import SVC
from sklearn.semi_supervised import SelfTrainingClassifier

# 載入資料集

X, y = datasets.load_iris(return_X_y=True)
X = X[:, :2]

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 設定 30% 資料為沒有標註(-1)

rng = np.random.RandomState(0)
y_rand = rng.rand(y_train.shape[0])
y_30 = np.copy(y_train)
y_30[y_rand < 0.3] = -1
cc = np.count_nonzero(y_30 == -1)
print(cc)

y_30_index = np.where(y_30 == -1)[0]
print(y_30_index)

print(type(y_30_index))

# 模型訓練

base_classifier = SVC(kernel="rbf", gamma=0.5, probability=True)
clf = SelfTrainingClassifier(base_classifier).fit(X_train, y_30)  # 學習訓練.fit

# 繪製決策邊界

# 建立 mesh grid
x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

# 每個標籤不同顏色(RGB)
color_map = {-1: (1, 1, 1), 0: (0, 0, 0.9), 1: (1, 0, 0), 2: (0.8, 0.6, 0)}
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# 繪製等高線
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
plt.axis("off")

# 繪製實際點
colors = [color_map[y] for y in y_30]
plt.scatter(X_train[:, 0], X_train[:, 1], c=colors, edgecolors="black")

show()

# SVM 模型評估
base_classifier.fit(X_train, y_30)  # 學習訓練.fit
cc = base_classifier.score(X_test, y_test)
print(cc)
# 0.6666666666666666

# Self-training 模型評估
cc = clf.score(X_test, y_test)
print(cc)
# 0.7666666666666667

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 完整資料進行模型評估

rng = np.random.RandomState(42)
X, y = datasets.load_iris(return_X_y=True)
random_unlabeled_points = rng.rand(y.shape[0]) < 0.3
y[random_unlabeled_points] = -1

svc = SVC(probability=True, gamma="auto")

self_training_model = SelfTrainingClassifier(svc)

self_training_model.fit(X, y)  # 學習訓練.fit

"""
SelfTrainingClassifier(base_estimator=SVC(gamma='auto', probability=True))
"""

svc.fit(X[y >= 0], y[y >= 0])  # 學習訓練.fit
cc = svc.score(X, y)
print(cc)

# 0.66

X, y = datasets.load_iris(return_X_y=True)
cc = self_training_model.score(X, y)
print(cc)

# 0.9733333333333334

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_02_label_propagation

# 標註傳播(Label propagation)測試

import numpy as np
from sklearn.datasets import make_classification
from sklearn.semi_supervised import LabelPropagation

# 載入資料集

X, y = make_classification(
    n_samples=1000, n_features=2, n_informative=2, n_redundant=0, random_state=1
)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=1, stratify=y
)

# 設定 50% 資料為沒有標註(-1)

X_train_lab, X_test_unlab, y_train_lab, y_test_unlab = train_test_split(
    X_train, y_train, test_size=0.5, random_state=1, stratify=y_train
)
X_train_mixed = np.concatenate((X_train_lab, X_test_unlab))
nolabel = [-1 for _ in range(len(y_test_unlab))]
y_train_mixed = np.concatenate((y_train_lab, nolabel))
cc = y_train_mixed.shape
print(cc)

# (500,)

# Label propagation 模型訓練與評估

clf = LabelPropagation()

clf.fit(X_train_mixed, y_train_mixed)  # 學習訓練.fit

cc = clf.score(X_test, y_test)
print(cc)

# 0.856

# LogisticRegression 模型訓練與評估

from sklearn.linear_model import LogisticRegression

clf2 = LogisticRegression()

clf2.fit(X_train_lab, y_train_lab)  # 學習訓練.fit

cc = clf2.score(X_test, y_test)
print(cc)

# 0.848

# 取得訓練資料標註

tran_labels = clf.transduction_
cc = tran_labels.shape
print(cc)
# (500,)

# 再依Label propagation傳播結果進行模型訓練與評估

clf3 = LogisticRegression()

clf3.fit(X_train_mixed, tran_labels)  # 學習訓練.fit

cc = clf3.score(X_test, y_test)
print(cc)
# 0.862

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_03_label_spreading

# LabelSpreading 測試

import numpy as np
from sklearn.datasets import make_classification
from sklearn.semi_supervised import LabelSpreading

# 載入資料集

X, y = make_classification(
    n_samples=1000, n_features=2, n_informative=2, n_redundant=0, random_state=1
)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=1, stratify=y
)

# 設定 50% 資料為沒有標註(-1)

X_train_lab, X_test_unlab, y_train_lab, y_test_unlab = train_test_split(
    X_train, y_train, test_size=0.5, random_state=1, stratify=y_train
)
X_train_mixed = np.concatenate((X_train_lab, X_test_unlab))
nolabel = [-1 for _ in range(len(y_test_unlab))]
y_train_mixed = np.concatenate((y_train_lab, nolabel))
cc = y_train_mixed.shape
print(cc)
# (500,)

# LabelSpreading 模型訓練與評估

clf = LabelSpreading()

clf.fit(X_train_mixed, y_train_mixed)  # 學習訓練.fit

cc = clf.score(X_test, y_test)
print(cc)
# 0.854

# LogisticRegression 模型訓練與評估

from sklearn.linear_model import LogisticRegression

clf2 = LogisticRegression()

clf2.fit(X_train_lab, y_train_lab)  # 學習訓練.fit

cc = clf2.score(X_test, y_test)
print(cc)

# 0.848

# 取得訓練資料標註

tran_labels = clf.transduction_
cc = tran_labels.shape
print(cc)
# (500,)

# 再依LabelSpreading傳播結果進行模型訓練與評估

clf3 = LogisticRegression()

clf3.fit(X_train_mixed, tran_labels)  # 學習訓練.fit

cc = clf3.score(X_test, y_test)
print(cc)
# 0.858

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#  11_05_shapley_value_from_scratch

# 自行計算 Shapley value
# How to calculate shapley values from scratch

import random
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# 載入資料

X, y = datasets.load_breast_cancer(return_X_y=True, as_frame=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練

clf = make_pipeline(StandardScaler(), LogisticRegression())

clf.fit(X_train.values, y_train)  # 學習訓練.fit

"""
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('logisticregression', LogisticRegression())])
"""

# 自行計算第16個特徵的Shapley value

x = X_test.iloc[0]  # 第一筆測試資料
j = 15  # 第16個特徵
M = 1000  # 測試 1000 次
n_features = len(x)
marginal_contributions = []
feature_idxs = list(range(n_features))
feature_idxs.remove(j)
for _ in range(M):
    # 抽樣訓練資料一筆資料
    z = X_train.sample(1).values[0]
    # 所有組合
    x_idx = random.sample(
        feature_idxs,
        min(
            max(int(0.2 * n_features), random.choice(feature_idxs)),
            int(0.8 * n_features),
        ),
    )
    z_idx = [idx for idx in feature_idxs if idx not in x_idx]

    # 含第16個特徵的X，在組合內以測試資料填入，不在組合內以訓練資料填入
    x_plus_j = np.array([x[i] if i in x_idx + [j] else z[i] for i in range(n_features)])
    # 不含第16個特徵的X
    x_minus_j = np.array(
        [z[i] if i in z_idx + [j] else x[i] for i in range(n_features)]
    )

    # 計算邊際貢獻(marginal contribution)
    marginal_contribution = (
        clf.predict_proba(x_plus_j.reshape(1, -1))[0][1]
        - clf.predict_proba(x_minus_j.reshape(1, -1))[0][1]
    )
    marginal_contributions.append(marginal_contribution)

# 計算邊際貢獻平均值
phi_j_x = sum(marginal_contributions) / len(marginal_contributions)
print(f"Shaply value for feature {j}: {phi_j_x:.5}")

# Shaply value for feature 15: 0.010254

cc = X.columns[j]
print(cc)

#'compactness error'

# 以 SHAP 套件驗證

import shap

explainer = shap.KernelExplainer(clf.predict_proba, X_train.values)
shap_values = explainer.shap_values(x)

""" NG
print(f"Shaply value calulated from shap: {shap_values[1][j]:.5}")
"""

# Using 455 background data samples could cause slower run times.
# Consider using shap.sample(data, K) or shap.kmeans(data, K) to summarize the background as K samples.

# Shaply value calulated from shap: 0.01366

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 範例2. 自行計算 Shapley value
# 載入套件

from sklearn.tree import DecisionTreeRegressor, plot_tree

# 載入資料

with open("./data/housing.data", encoding="utf8") as f:
    data = f.readlines()
all_fields = []
for line in data:
    line2 = line[1:].replace("   ", " ").replace("  ", " ")
    fields = []
    for item in line2.split(" "):
        fields.append(float(item.strip()))
        if len(fields) == 14:
            all_fields.append(fields)
df = pd.DataFrame(all_fields)
df.columns = "CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV".split(",")
cc = df.head()
print(cc)

# 模型訓練

y = df["MEDV"]
df = df[["RM", "LSTAT", "DIS", "NOX"]]

clf = DecisionTreeRegressor(max_depth=3)

clf.fit(df, y)  # 學習訓練.fit

fig = plt.figure(figsize=(20, 5))
ax = fig.add_subplot(111)
_ = plot_tree(clf, ax=ax, feature_names=df.columns)
show()

# 以 SHAP 套件計算 Shapley value

import shap
import tabulate

explainer = shap.TreeExplainer(clf)
shap_values = explainer.shap_values(df[:1])  # 第一筆資料
print(
    tabulate.tabulate(
        pd.DataFrame(
            {
                "shap_value": shap_values.squeeze(),
                "feature_value": df[:1].values.squeeze(),
            },
            index=df.columns,
        ),
        tablefmt="github",
        headers="keys",
    )
)

# Shapley value + Y平均數 = 預測值

cc = shap_values.sum() + y.mean(), clf.predict(df[:1])[0]
print(cc)

# (22.905200000000004, 22.9052)

# 自行計算 Shapley value

from itertools import combinations
import scipy


# 計算特定組合的邊際貢獻
def pred_tree(clf, coalition, row, node=0):
    left_node = clf.tree_.children_left[node]
    right_node = clf.tree_.children_right[node]
    is_leaf = left_node == right_node

    if is_leaf:
        return clf.tree_.value[node].squeeze()

    feature = row.index[clf.tree_.feature[node]]
    if feature in coalition:
        if row.loc[feature] <= clf.tree_.threshold[node]:
            # go left
            return pred_tree(clf, coalition, row, node=left_node)
        else:  # go right
            return pred_tree(clf, coalition, row, node=right_node)

    # take weighted average of left and right
    wl = clf.tree_.n_node_samples[left_node] / clf.tree_.n_node_samples[node]
    wr = clf.tree_.n_node_samples[right_node] / clf.tree_.n_node_samples[node]
    value = wl * pred_tree(clf, coalition, row, node=left_node)
    value += wr * pred_tree(clf, coalition, row, node=right_node)
    return value


# 計算特定組合的平均邊際貢獻
def make_value_function(clf, row, col):
    def value(c):
        marginal_gain = pred_tree(clf, c + [col], row) - pred_tree(clf, c, row)
        num_coalitions = scipy.special.comb(len(row) - 1, len(c))
        return marginal_gain / num_coalitions

    return value


# 各種組合
def make_coalitions(row, col):
    rest = [x for x in row.index if x != col]
    for i in range(len(rest) + 1):
        for x in combinations(rest, i):
            yield list(x)


# 計算 Shapley value
def compute_shap(clf, row, col):
    v = make_value_function(clf, row, col)
    return sum([v(coal) / len(row) for coal in make_coalitions(row, col)])


# 顯示 Shapley value
print(
    tabulate.tabulate(
        pd.DataFrame(
            {
                "shap_value": shap_values.squeeze(),
                "my_shap": [
                    compute_shap(clf, df[:1].T.squeeze(), x) for x in df.columns
                ],
                "feature_value": df[:1].values.squeeze(),
            },
            index=df.columns,
        ),
        tablefmt="github",
        headers="keys",
    )
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_06_shap_test

# SHAP套件測試
# An introduction to explainable AI with Shapley values

import shap
from sklearn.preprocessing import StandardScaler

# 載入資料集

df = pd.read_csv("./data/ca_housing.csv")
cc = df.head()
print(cc)

# 資料清理

# 刪除 missing value
df.dropna(inplace=True)

X = df.drop(["median_house_value", "ocean_proximity"], axis=1)
y = df["median_house_value"]

# 模型訓練與評估

# scaler = StandardScaler()
# X2 = scaler.fit_transform(X)
# X = pd.DataFrame(X2, columns=X.columns)

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)  # 學習訓練.fit

print("Model coefficients:")
print(X.shape)
print(X.shape[1])
for i in range(X.shape[1]):
    print(X.columns[i], "=", linear_regression.coef_[i].round(5))

# 單一特徵影響力

feature_name = "median_income"
X100 = shap.utils.sample(X, 100)
shap.partial_dependence_plot(
    feature_name,
    linear_regression.predict,
    X100,
    ice=False,
    model_expected_value=True,
    feature_expected_value=True,
)

# 衡量特徵Shapley value

sample_ind = 20  # 第 21 筆資料
explainer = shap.Explainer(linear_regression.predict, X100)
shap_values = explainer(X)
shap.partial_dependence_plot(
    feature_name,
    linear_regression.predict,
    X100,
    model_expected_value=True,
    feature_expected_value=True,
    ice=False,
    shap_values=shap_values[sample_ind : sample_ind + 1, :],
)

# Exact explainer: 20434it [01:32, 205.74it/s]

# 以單一特徵所有資料的Shapley value繪製散佈圖

shap.plots.scatter(shap_values[:, feature_name])
show()

# 單一資料的特徵影響力(Local Feature Importance)

cc = X.iloc[sample_ind]
print(cc)

shap.plots.waterfall(shap_values[sample_ind], max_display=14)
show()

# 加法模型(Generalized additive models, GAM)

# !pip install interpret

import interpret.glassbox

# 使用 Boosting 演算法
model_ebm = interpret.glassbox.ExplainableBoostingRegressor(interactions=0)

model_ebm.fit(X, y)  # 學習訓練.fit

# 加法模型 Shapley value
explainer_ebm = shap.Explainer(model_ebm.predict, X100)
shap_values_ebm = explainer_ebm(X)

# 特徵影響力
fig, ax = shap.partial_dependence_plot(
    feature_name,
    model_ebm.predict,
    X100,
    model_expected_value=True,
    feature_expected_value=True,
    show=False,
    ice=False,
    shap_values=shap_values_ebm[sample_ind : sample_ind + 1, :],  # 第 21 筆資料
)
show()

shap.plots.scatter(shap_values_ebm[:, feature_name])
show()

shap.plots.waterfall(shap_values_ebm[sample_ind])
show()

shap.plots.beeswarm(shap_values_ebm)
show()

shap.plots.bar(shap_values_ebm)
show()

shap.initjs()
shap.plots.force(shap_values_ebm[sample_ind])

print("ddddddd")
sys.exit()

"""
Visualization omitted, Javascript library not loaded!
Have you run `initjs()` in this notebook? If this notebook was from another user you must also trust this notebook (File -> Trust notebook). If you are viewing this notebook on github the Javascript has been stripped for security. If you are using JupyterLab this error is because a JupyterLab extension has not yet been written.
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_07_mlflow_test

# MLflow 測試

import warnings
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import ElasticNet
import mlflow
import mlflow.sklearn

# 載入資料集

X, y = datasets.load_diabetes(return_X_y=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練與評估

# 定義模型參數
alpha = 1
l1_ratio = 1

with mlflow.start_run():
    # 模型訓練
    model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio)

    model.fit(X_train, y_train)  # 學習訓練.fit

    # 模型評估
    pred = model.predict(X_test)
    rmse = mean_squared_error(pred, y_test)
    abs_error = mean_absolute_error(pred, y_test)
    r2 = r2_score(pred, y_test)

    # MLflow 記錄
    mlflow.log_param("alpha", alpha)
    mlflow.log_param("l1_ratio", l1_ratio)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("abs_error", abs_error)
    mlflow.log_metric("r2", r2)

    # MLflow 記錄模型
    mlflow.sklearn.log_model(model, "model")

# 2023/01/28 10:05:26 WARNING mlflow.utils.environment: Encountered an unexpected error while inferring pip requirements (model URI: C:\WINDOWS\TEMP\tmpxl4956z4\model\model.pkl, flavor: sklearn), fall back to return ['scikit-learn==1.2.0', 'cloudpickle==1.6.0']. Set logging level to DEBUG to see the full traceback.

# 模型評估
""" NG
cc = mlflow.sklearn.log_model(lr, "model")
print(cc)

#平均分數: 0.9303030303030303, 標準差: 0.08393720596645175
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用迴歸模型

from sklearn.linear_model import RidgeCV
from sklearn.svm import LinearSVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.preprocessing import StandardScaler

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

estimators = [("lr", RidgeCV()), ("svr", LinearSVR(random_state=42))]

model = StackingRegressor(
    estimators=estimators,
    final_estimator=RandomForestRegressor(n_estimators=10, random_state=42),
)
model.fit(X_train_std, y_train)  # 學習訓練.fit

from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X_test_std, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: 0.12143159519945441, 標準差: 0.4732757387323812

svc = LinearSVR()

svc.fit(X_train_std, y_train)  # 學習訓練.fit
from sklearn.model_selection import cross_val_score

scores = cross_val_score(svc, X_test_std, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: -1.0399780386178537, 標準差: 0.36412901584183494

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
print("------------------------------------------------------------")  # 60個
