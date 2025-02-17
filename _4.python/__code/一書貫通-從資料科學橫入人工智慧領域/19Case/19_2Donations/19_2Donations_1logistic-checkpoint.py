"""
19_2Donations_1logistic-checkpoint

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

model_data=pd.read_csv("donations2.csv").drop(["ID","TARGET_D"], axis=1)
cc = model_data.head()
print(cc)


# 设置自变量及因变量：

model_data.dtypes
y = 'TARGET_B'
var_c = ["GiftCnt36","GiftCntAll","GiftCntCard36",
         "GiftCntCardAll","GiftTimeLast","GiftTimeFirst",
         "PromCnt12","PromCnt36","PromCntAll",
         "PromCntCard12","PromCntCard36","PromCntCardAll",
         "StatusCatStarAll","DemAge","DemMedHomeValue",
         "DemPctVeterans","DemMedIncome","GiftAvgLast",
         "GiftAvg36","GiftAvgAll","GiftAvgCard36"]
var_d = ['StatusCat96NK', 'DemHomeOwner', 'DemGender', 'DemCluster']
X = model_data[var_c + var_d].copy()
Y = model_data[y].copy()

#根据IV值筛选变量 - 分类变量：

from woe import WoE
iv_d = {}
for i in var_d:
    iv_d[i] = WoE(v_type='d').fit(X[i].copy(), Y.copy()).iv
pd.Series(iv_d).sort_values(ascending = False)

var_d_s = ['StatusCat96NK', 'DemCluster']

#根据IV值筛选变量-连续变量：

iv_c = {}
for i in var_c:
    iv_c[i] = WoE(v_type='c',t_type='b',qnt_num=3).fit(X[i],Y).iv 
sort_iv_c = pd.Series(iv_c).sort_values(ascending=False)
sort_iv_c

var_c_s = list(sort_iv_c[sort_iv_c > 0.02].index)
var_c_s

X = model_data[var_c_s + var_d_s].copy()
Y = model_data[y].copy()
cc = X[var_c_s].describe().T
print(cc)

#针对每个变量的E（探索）阶段:

cc = abs((X[var_c_s].mode().iloc[0,] - X[var_c_s].median()) /
    (X[var_c_s].quantile(0.75) - X[var_c_s].quantile(0.25)))
print(cc)


plt.hist(X["PromCntAll"], bins=20)
plt.show()


cc = len(X["DemCluster"].value_counts())
print(cc)

#针对有问题的变量进行修改的M（修改）阶段:

#连续变量的修改：

cc = 1 - (X.describe().T["count"]) / len(X)
print(cc)

fill_GiftAvgCard36 = X.GiftAvgCard36.median()
X.GiftAvgCard36.fillna(value=fill_GiftAvgCard36, inplace=True)

#分类变量的修改：

DemCluster_grp = model_data[['DemCluster','TARGET_B']].groupby('DemCluster',as_index = False)
DemC_C = DemCluster_grp['TARGET_B'].agg({'mean' : 'mean','count':'count'}).sort_values("mean")
DemC_C["count_cumsum"] = DemC_C["count"].cumsum()
DemC_C["new_DemCluster"] = DemC_C["count_cumsum"].apply(lambda x: x//(len(model_data)/10))
DemC_C["new_DemCluster"] = DemC_C["new_DemCluster"].astype(int)
cc = X.head()
print(cc)

X_rep = X.copy()
for i in var_d_s:X_rep[i+"_woe"] = WoE(v_type='d').fit_transform(X_rep[i],Y)
StatusCat96NK_woe = X_rep[["StatusCat96NK","StatusCat96NK_woe"]].drop_duplicates().set_index("StatusCat96NK").to_dict()
DemCluster_woe = X_rep[["DemCluster","DemCluster_woe"]].drop_duplicates().set_index("DemCluster").to_dict()
del X_rep["StatusCat96NK"]
del X_rep["DemCluster"]
X_rep.rename(columns={"StatusCat96NK_woe":"StatusCat96NK","DemCluster_woe":"DemCluster"},inplace=True)

#通过随机森林对变量的重要性进行筛选:

import sklearn.ensemble as ensemble
rfc = ensemble.RandomForestClassifier(criterion='entropy', n_estimators=3, max_features=0.5, min_samples_split=5)
rfc_model = rfc.fit(X_rep, Y)
rfc_model.feature_importances_
rfc_fi = pd.DataFrame()
rfc_fi["features"] = list(X.columns)
rfc_fi["importance"] = list(rfc_model.feature_importances_)
rfc_fi=rfc_fi.set_index("features",drop=True)
var_sort = rfc_fi.sort_values(by="importance",ascending=False)
var_sort.plot(kind="bar")
plt.show()

var_x = list(var_sort.importance[var_sort.importance > 0.02].index)
cc = var_x
print(cc)

#解释变量分布转换：

skew_var_x = {}
for i in var_x:
    skew_var_x[i] = abs(X_rep[i].skew())  
skew = pd.Series(skew_var_x).sort_values(ascending=False)
print(skew)

var_x_ln = skew.index[skew > 1]
print(var_x_ln)

for i in var_x_ln:
    if min(X_rep[i]) <= 0:
        X_rep[i] =np.log(X_rep[i] + abs(min(X_rep[i])) + 0.01)
    else:
        X_rep[i] =np.log(X_rep[i])

#变量压缩：

from VarSelec import Var_Select
from VarSelec import Var_Select_auto

X_rep_reduc = Var_Select_auto(X_rep,alphaMin=14,alphaMax=15, alphastep=0.5)
cc = X_rep_reduc.head()
print(cc)

cc = list(X_rep_reduc.columns)
print(cc)

#建立逻辑回归模型M（建模）阶段：

import sklearn.model_selection as model_selection
ml_data = model_selection.train_test_split(X_rep_reduc, Y, test_size=0.3, random_state=0)
train_data, test_data, train_target, test_target = ml_data
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
train_data = min_max_scaler.fit_transform(train_data)
test_data = min_max_scaler.fit_transform(test_data)
print(train_data)

import sklearn.linear_model as linear_model
logistic_model = linear_model.LogisticRegression(class_weight = None,
                                                 dual = False,
                                                 fit_intercept = True,
                                                 intercept_scaling = 1,
                                                 penalty = 'l1',
                                                 random_state = None,
                                                 tol = 0.001)

from sklearn.model_selection import ParameterGrid
from sklearn.model_selection import GridSearchCV

C = np.logspace(-3,0,20,base=10)
param_grid = {'C': C}
clf_cv = GridSearchCV(estimator=logistic_model, 
                      param_grid=param_grid, 
                      cv=5, 
                      scoring='roc_auc')
clf_cv.fit(train_data, train_target)

logistic_model = linear_model.LogisticRegression(C=clf_cv.best_params_["C"],
                                                 class_weight=None,
                                                 dual=False,
                                                 fit_intercept=True,
                                                 intercept_scaling=1,
                                                 penalty='l1',
                                                 random_state=None,
                                                 tol=0.001)
logistic_model.fit(train_data, train_target)

print(logistic_model.coef_)

import statsmodels.api as sm
import statsmodels.formula.api as smf

model=X_rep_reduc.join(train_target)
formula = "TARGET_B ~ " + "+".join(X_rep_reduc)
lg_m = smf.glm(formula=formula, data=model, family=sm.families.Binomial(sm.families.links.logit)).fit()
cc = lg_m.summary()
print(cc)

# ROC曲线：

test_est = logistic_model.predict(test_data)
train_est = logistic_model.predict(train_data)
test_est_p = logistic_model.predict_proba(test_data)[:,1]
train_est_p = logistic_model.predict_proba(train_data)[:,1]
import sklearn.metrics as metrics
fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, test_est_p)
fpr_train, tpr_train, th_train = metrics.roc_curve(train_target, train_est_p)
plt.figure(figsize=[6,6])
plt.plot(fpr_test, tpr_test)
plt.plot(fpr_train, tpr_train)
plt.title('ROC curve')
plt.show()

print('AUC = %6.4f' %metrics.auc(fpr_test, tpr_test))

#AUC = 0.6163

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

