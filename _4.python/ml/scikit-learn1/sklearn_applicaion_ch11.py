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

#11_01_self_training

#自我訓練(Self-training)測試

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.semi_supervised import SelfTrainingClassifier

#載入資料集

X, y = datasets.load_iris(return_X_y=True)
X = X[:, :2]

#資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

#設定 30% 資料為沒有標註(-1)

rng = np.random.RandomState(0)
y_rand = rng.rand(y_train.shape[0])
y_30 = np.copy(y_train)
y_30[y_rand < 0.3] = -1
cc = np.count_nonzero(y_30==-1)
print(cc)

y_30_index = np.where(y_30==-1)[0]
print(y_30_index)

print(type(y_30_index))

#模型訓練

base_classifier = SVC(kernel="rbf", gamma=0.5, probability=True)
clf = SelfTrainingClassifier(base_classifier).fit(X_train, y_30)

#繪製決策邊界

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

plt.show()

#SVM 模型評估

base_classifier.fit(X_train, y_30)
cc = base_classifier.score(X_test, y_test)
print(cc)

#0.6666666666666666

#Self-training 模型評估

cc = clf.score(X_test, y_test)
print(cc)

#0.7666666666666667

#完整資料進行模型評估

rng = np.random.RandomState(42)
X, y = datasets.load_iris(return_X_y=True)
random_unlabeled_points = rng.rand(y.shape[0]) < 0.3
y[random_unlabeled_points] = -1

svc = SVC(probability=True, gamma="auto")
self_training_model = SelfTrainingClassifier(svc)
self_training_model.fit(X, y)

"""
SelfTrainingClassifier(base_estimator=SVC(gamma='auto', probability=True))
"""

svc.fit(X[y >= 0], y[y >= 0])
cc = svc.score(X, y)
print(cc)

#0.66

X, y = datasets.load_iris(return_X_y=True)
cc = self_training_model.score(X, y)
print(cc)

#0.9733333333333334

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#11_02_label_propagation

#標註傳播(Label propagation)測試

import numpy as np
from sklearn import datasets
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.semi_supervised import LabelPropagation

#載入資料集

X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, 
                           n_redundant=0, random_state=1)

#資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, 
                                            random_state=1, stratify=y)

#設定 50% 資料為沒有標註(-1)

X_train_lab, X_test_unlab, y_train_lab, y_test_unlab = train_test_split(
          X_train, y_train, test_size=0.5, random_state=1, stratify=y_train)
X_train_mixed = np.concatenate((X_train_lab, X_test_unlab))
nolabel = [-1 for _ in range(len(y_test_unlab))]
y_train_mixed = np.concatenate((y_train_lab, nolabel))
cc = y_train_mixed.shape
print(cc)

#(500,)

#Label propagation 模型訓練與評估

clf = LabelPropagation()
clf.fit(X_train_mixed, y_train_mixed)
cc = clf.score(X_test, y_test)
print(cc)

#0.856

#LogisticRegression 模型訓練與評估

from sklearn.linear_model import LogisticRegression

clf2 = LogisticRegression()
clf2.fit(X_train_lab, y_train_lab)
cc = clf2.score(X_test, y_test)
print(cc)

#0.848

#取得訓練資料標註

tran_labels = clf.transduction_
cc = tran_labels.shape
print(cc)
#(500,)

#再依Label propagation傳播結果進行模型訓練與評估

clf3  = LogisticRegression()
clf3.fit(X_train_mixed, tran_labels)
cc = clf3.score(X_test, y_test)
print(cc)
#0.862

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#11_03_label_spreading

#LabelSpreading 測試

import numpy as np
from sklearn import datasets
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.semi_supervised import LabelSpreading

#載入資料集

X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, 
                           n_redundant=0, random_state=1)

#資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, 
                                            random_state=1, stratify=y)

#設定 50% 資料為沒有標註(-1)

X_train_lab, X_test_unlab, y_train_lab, y_test_unlab = train_test_split(
          X_train, y_train, test_size=0.5, random_state=1, stratify=y_train)
X_train_mixed = np.concatenate((X_train_lab, X_test_unlab))
nolabel = [-1 for _ in range(len(y_test_unlab))]
y_train_mixed = np.concatenate((y_train_lab, nolabel))
cc = y_train_mixed.shape
print(cc)
#(500,)

#LabelSpreading 模型訓練與評估

clf = LabelSpreading()
clf.fit(X_train_mixed, y_train_mixed)
cc = clf.score(X_test, y_test)
print(cc)
#0.854

#LogisticRegression 模型訓練與評估

from sklearn.linear_model import LogisticRegression

clf2 = LogisticRegression()
clf2.fit(X_train_lab, y_train_lab)
cc = clf2.score(X_test, y_test)
print(cc)

#0.848

#取得訓練資料標註

tran_labels = clf.transduction_
cc = tran_labels.shape
print(cc)
#(500,)

#再依LabelSpreading傳播結果進行模型訓練與評估

clf3  = LogisticRegression()
clf3.fit(X_train_mixed, tran_labels)
cc = clf3.score(X_test, y_test)
print(cc)

#0.858

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#11_04_label_propagation_digits_active_learning

#Label Propagation digits active learning

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import datasets
from sklearn.semi_supervised import LabelSpreading
from sklearn.metrics import classification_report, confusion_matrix

#載入資料集

digits = datasets.load_digits()
rng = np.random.RandomState(0)
indices = np.arange(len(digits.data))
rng.shuffle(indices)

# 取前 330 筆資料
X = digits.data[indices[:330]]
y = digits.target[indices[:330]]
images = digits.images[indices[:330]]

# 參數設定
n_total_samples = len(y)
n_labeled_points = 40    # 初始取40筆標註資料
max_iterations = 5       # 5 個執行週期

unlabeled_indices = np.arange(n_total_samples)[n_labeled_points:]
cc = len(unlabeled_indices)
print(cc)

#Label propagation 模型訓練與評估

f = plt.figure()
for i in range(max_iterations):
    y_train = np.copy(y)
    y_train[unlabeled_indices] = -1

    # LabelSpreading 模型訓練
    lp_model = LabelSpreading(gamma=0.25, max_iter=20)
    lp_model.fit(X, y_train)

    # 預測
    predicted_labels = lp_model.transduction_[unlabeled_indices]
    true_labels = y[unlabeled_indices]

    print(f"Iteration {i} {70 * '_'}")
    print(
        f"Label Spreading model: {n_labeled_points} labeled & " +
        f"{n_total_samples - n_labeled_points} unlabeled ({n_total_samples} total)"
    )
    
    if i==0 or i==max_iterations-1:
        print(classification_report(true_labels, predicted_labels))

    print("Confusion matrix")
    cm = confusion_matrix(true_labels, predicted_labels, labels=lp_model.classes_)
    print(cm)

    # 計算熵，以找出最不確定的五筆資料
    pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
    uncertainty_index = np.argsort(pred_entropies)[::-1]
    uncertainty_index = uncertainty_index[
        np.in1d(uncertainty_index, unlabeled_indices)
    ][:5]

    # 記錄最不確定的五筆資料
    delete_indices = np.array([], dtype=int)
    f.text(
        0.05,
        (1 - (i + 1) * 0.183),
        f"model {i + 1}\n\nfit with\n{n_labeled_points} labels",
        size=10,
    )
    for index, image_index in enumerate(uncertainty_index):
        image = images[image_index]

        sub = f.add_subplot(5, 5, index + 1 + (5 * i))
        sub.imshow(image, cmap=plt.cm.gray_r, interpolation="none")
        sub.set_title(
            f"predict: {lp_model.transduction_[image_index]}\ntrue: {y[image_index]}",
            size=10,
        )
        sub.axis("off")

        # 將最不確定的五筆資料加入待刪除的陣列
        (delete_index,) = np.where(unlabeled_indices == image_index)
        delete_indices = np.concatenate((delete_indices, delete_index))

    # 將最不確定的五筆資料加入標註資料
    unlabeled_indices = np.delete(unlabeled_indices, delete_indices)
    n_labeled_points += len(uncertainty_index)

print("\n最不確定的五筆資料：")
plt.subplots_adjust(left=0.2, bottom=0.03, right=0.9, top=0.9, wspace=0.2, hspace=0.85)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#  11_05_shapley_value_from_scratch

# 自行計算 Shapley value
#How to calculate shapley values from scratch

import random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn import datasets

#載入資料

X, y = datasets.load_breast_cancer(return_X_y=True, as_frame=True)

#資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#模型訓練

clf = make_pipeline(StandardScaler(), LogisticRegression())
clf.fit(X_train.values, y_train)

"""
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('logisticregression', LogisticRegression())])
"""

#自行計算第16個特徵的Shapley value

x = X_test.iloc[0] # 第一筆測試資料
j = 15   # 第16個特徵
M = 1000 # 測試 1000 次
n_features = len(x)
marginal_contributions = []
feature_idxs = list(range(n_features))
feature_idxs.remove(j)
for _ in range(M):
    # 抽樣訓練資料一筆資料
    z = X_train.sample(1).values[0]
    # 所有組合
    x_idx = random.sample(feature_idxs, min(max(int(0.2*n_features), 
                            random.choice(feature_idxs)), int(0.8*n_features)))
    z_idx = [idx for idx in feature_idxs if idx not in x_idx]
    
    # 含第16個特徵的X，在組合內以測試資料填入，不在組合內以訓練資料填入
    x_plus_j = np.array([x[i] if i in x_idx + [j] else z[i] for i in range(n_features)])
    # 不含第16個特徵的X
    x_minus_j = np.array([z[i] if i in z_idx + [j] else x[i] for i in range(n_features)])
    
    # 計算邊際貢獻(marginal contribution)
    marginal_contribution = clf.predict_proba(x_plus_j.reshape(1, -1))[0][1] - \
            clf.predict_proba(x_minus_j.reshape(1, -1))[0][1]
    marginal_contributions.append(marginal_contribution)
    
# 計算邊際貢獻平均值    
phi_j_x = sum(marginal_contributions) / len(marginal_contributions)  
print(f"Shaply value for feature {j}: {phi_j_x:.5}")

#Shaply value for feature 15: 0.010254

cc = X.columns[j]
print(cc)

#'compactness error'

#以 SHAP 套件驗證

import shap

explainer = shap.KernelExplainer(clf.predict_proba, X_train.values)
shap_values = explainer.shap_values(x)
print(f"Shaply value calulated from shap: {shap_values[1][j]:.5}")

#Using 455 background data samples could cause slower run times. Consider using shap.sample(data, K) or shap.kmeans(data, K) to summarize the background as K samples.

#Shaply value calulated from shap: 0.01366

# -----------------------------------------------------------------

#範例2. 自行計算 Shapley value
#載入套件

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree

#載入資料

with open('./data/housing.data', encoding='utf8') as f:
    data = f.readlines()
all_fields = []
for line in data:
    line2 = line[1:].replace('   ', ' ').replace('  ', ' ')
    fields = []
    for item in line2.split(' '):
        fields.append(float(item.strip()))
        if len(fields) == 14:
            all_fields.append(fields)
df = pd.DataFrame(all_fields)
df.columns = 'CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV'.split(',')
cc = df.head()
print(cc)

#模型訓練

y = df['MEDV']
df = df[['RM', 'LSTAT', 'DIS', 'NOX']]

clf = DecisionTreeRegressor(max_depth=3)
clf.fit(df, y)
fig = plt.figure(figsize=(20, 5))
ax = fig.add_subplot(111)
_ = plot_tree(clf, ax=ax, feature_names=df.columns)
plt.show()

#以 SHAP 套件計算 Shapley value

import shap
import tabulate

explainer = shap.TreeExplainer(clf)
shap_values = explainer.shap_values(df[:1]) # 第一筆資料
print(tabulate.tabulate(pd.DataFrame(
    {'shap_value': shap_values.squeeze(),
     'feature_value': df[:1].values.squeeze()}, index=df.columns),
                        tablefmt="github", headers="keys"))

#Shapley value + Y平均數 = 預測值

cc = shap_values.sum() + y.mean(), clf.predict(df[:1])[0]
print(cc)

#(22.905200000000004, 22.9052)

#自行計算 Shapley value

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
        else: # go right
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
print(tabulate.tabulate(pd.DataFrame(
    {'shap_value': shap_values.squeeze(),
     'my_shap': [compute_shap(clf, df[:1].T.squeeze(), x) for x in df.columns],
     'feature_value': df[:1].values.squeeze()
    }, index=df.columns), tablefmt="github", headers="keys"))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#11_06_shap_test

#SHAP套件測試
#An introduction to explainable AI with Shapley values

import numpy as np
import pandas as pd
import shap
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

#載入資料集

df = pd.read_csv('./data/ca_housing.csv')
cc = df.head()
print(cc)

#資料清理

# 刪除 missing value
df.dropna(inplace=True)

X = df.drop(['median_house_value', 'ocean_proximity'], axis=1)
y = df['median_house_value']

#模型訓練與評估

# scaler = StandardScaler()
# X2 = scaler.fit_transform(X)
# X = pd.DataFrame(X2, columns=X.columns)

model = LinearRegression()
model.fit(X, y)
print("Model coefficients:")
for i in range(X.shape[1]):
    print(X.columns[i], "=", model.coef_[i].round(5))

#單一特徵影響力

feature_name = "median_income"
X100 = shap.utils.sample(X, 100)
shap.partial_dependence_plot(
    feature_name, model.predict, X100, ice=False,
    model_expected_value=True, feature_expected_value=True
)

#衡量特徵Shapley value

sample_ind = 20  # 第 21 筆資料
explainer = shap.Explainer(model.predict, X100)
shap_values = explainer(X)
shap.partial_dependence_plot(
    feature_name, model.predict, X100, model_expected_value=True,
    feature_expected_value=True, ice=False,
    shap_values=shap_values[sample_ind:sample_ind+1,:]
)

#Exact explainer: 20434it [01:32, 205.74it/s]                                                                           

#以單一特徵所有資料的Shapley value繪製散佈圖

shap.plots.scatter(shap_values[:,feature_name])
plt.show()

#單一資料的特徵影響力(Local Feature Importance)

cc = X.iloc[sample_ind]
print(cc)

shap.plots.waterfall(shap_values[sample_ind], max_display=14)
plt.show()

#加法模型(Generalized additive models, GAM)

# !pip install interpret

import interpret.glassbox

# 使用 Boosting 演算法
model_ebm = interpret.glassbox.ExplainableBoostingRegressor(interactions=0)
model_ebm.fit(X, y)

# 加法模型 Shapley value
explainer_ebm = shap.Explainer(model_ebm.predict, X100)
shap_values_ebm = explainer_ebm(X)

# 特徵影響力
fig,ax = shap.partial_dependence_plot(
    feature_name, model_ebm.predict, X100, model_expected_value=True,
    feature_expected_value=True, show=False, ice=False,
    shap_values=shap_values_ebm[sample_ind:sample_ind+1,:] # 第 21 筆資料
)
plt.show()

shap.plots.scatter(shap_values_ebm[:,feature_name])
plt.show()

shap.plots.waterfall(shap_values_ebm[sample_ind])
plt.show()

shap.plots.beeswarm(shap_values_ebm)
plt.show()

shap.plots.bar(shap_values_ebm)
plt.show()

shap.initjs()
shap.plots.force(shap_values_ebm[sample_ind])

"""
Visualization omitted, Javascript library not loaded!
Have you run `initjs()` in this notebook? If this notebook was from another user you must also trust this notebook (File -> Trust notebook). If you are viewing this notebook on github the Javascript has been stripped for security. If you are using JupyterLab this error is because a JupyterLab extension has not yet been written.
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_07_mlflow_test

#MLflow 測試

from sklearn import datasets
import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import mlflow
import mlflow.sklearn

#載入資料集

X, y = datasets.load_diabetes(return_X_y=True)

#資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

#模型訓練與評估

# 定義模型參數
alpha = 1
l1_ratio = 1

with mlflow.start_run():
    # 模型訓練
    model = ElasticNet(alpha = alpha,
                       l1_ratio = l1_ratio)
    model.fit(X_train,y_train)
    
    # 模型評估
    pred = model.predict(X_test)
    rmse = mean_squared_error(pred, y_test)
    abs_error = mean_absolute_error(pred, y_test)
    r2 = r2_score(pred, y_test)
    
    # MLflow 記錄
    mlflow.log_param('alpha', alpha)
    mlflow.log_param('l1_ratio', l1_ratio)
    mlflow.log_metric('rmse', rmse)
    mlflow.log_metric('abs_error', abs_error)
    mlflow.log_metric('r2', r2)
    
    # MLflow 記錄模型
    mlflow.sklearn.log_model(model, "model")

#2023/01/28 10:05:26 WARNING mlflow.utils.environment: Encountered an unexpected error while inferring pip requirements (model URI: C:\WINDOWS\TEMP\tmpxl4956z4\model\model.pkl, flavor: sklearn), fall back to return ['scikit-learn==1.2.0', 'cloudpickle==1.6.0']. Set logging level to DEBUG to see the full traceback.

#模型評估
""" NG
cc = mlflow.sklearn.log_model(lr, "model")
print(cc)

#平均分數: 0.9303030303030303, 標準差: 0.08393720596645175
"""

#使用迴歸模型

from sklearn.linear_model import RidgeCV
from sklearn.svm import LinearSVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.preprocessing import StandardScaler

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

estimators = [
    ('lr', RidgeCV()),
    ('svr', LinearSVR(random_state=42))
]

model = StackingRegressor(
    estimators=estimators,
    final_estimator=RandomForestRegressor(n_estimators=10, random_state=42))
model.fit(X_train_std, y_train)
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X_test_std, y_test, cv=10)
print(f'平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}')

#平均分數: 0.12143159519945441, 標準差: 0.4732757387323812

svc = LinearSVR()
svc.fit(X_train_std, y_train)
from sklearn.model_selection import cross_val_score
scores = cross_val_score(svc, X_test_std, y_test, cv=10)
print(f'平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}')

#平均分數: -1.0399780386178537, 標準差: 0.36412901584183494

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
