"""
OLS


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

import tensorflow as tf
from sklearn import datasets
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier  # 多層感知器分類器 函數學習機
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.models import model_from_json
from sklearn.metrics import accuracy_score
from time import time

import statsmodels.api as sm


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# # 线性回归模型与诊断
# 数据说明：本数据是一份汽车贷款数据

# |字段名|中文含义|
# |:--:|:--:|
# |id|id|
# |Acc|是否开卡(1=已开通)|
# |avg_exp|月均信用卡支出（元）|
# |avg_exp_ln|月均信用卡支出的自然对数|
# |gender|性别(男=1)|
# |Age|年龄|
# |Income|年收入（万元）|
# |Ownrent|是否自有住房（有=1；无=0)|
# |Selfempl|是否自谋职业(1=yes, 0=no)|
# |dist_home_val|所住小区房屋均价(万元)|
# |dist_avg_income|当地人均收入|
# |high_avg|高出当地平均收入|
# |edu_class|教育等级：小学及以下开通=0，中学=1，本科=2，研究生=3|

# get_ipython().magic('matplotlib inline')

print("------------------------------------------------------------")  # 60個

from statsmodels.formula.api import ols

raw = pd.read_csv(r"data/creditcard_exp.csv", skipinitialspace=True)
cc = raw.head()
print(cc)

exp = raw[raw["avg_exp"].notnull()].copy().iloc[:, 2:].drop("age2", axis=1)

exp_new = raw[raw["avg_exp"].isnull()].copy().iloc[:, 2:].drop("age2", axis=1)

exp.describe(include="all")


# 相关性分析
# 散点图

exp.plot("Income", "avg_exp", kind="scatter")
show()


exp[["Income", "avg_exp", "Age", "dist_home_val"]].corr(method="pearson")


# 线性回归算法
# 简单线性回归

lm_s = ols("avg_exp ~ Income+Age+dist_home_val", data=exp).fit()
cc = lm_s.summary()
print(cc)

# Predict-在原始数据集上得到预测值和残差

cc = lm_s.summary()
print(cc)

cc = pd.DataFrame([lm_s.predict(exp), lm_s.resid], index=["predict", "resid"]).T.head()
print(cc)

# 在待预测数据集上得到预测值

lm_s.predict(exp_new)[:5]  # 預測.predict


# 多元线性回归

lm_m = ols("avg_exp ~ Age + Income + dist_home_val + dist_avg_income", data=exp).fit()
cc = lm_m.summary()
print(cc)

# 多元线性回归的变量筛选


# forward select
def forward_select(data, response):
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = float("inf"), float("inf")
    while remaining:
        aic_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {}".format(response, " + ".join(selected + [candidate]))
            aic = ols(formula=formula, data=data).fit().aic
            aic_with_candidates.append((aic, candidate))
        aic_with_candidates.sort(reverse=True)
        best_new_score, best_candidate = aic_with_candidates.pop()
        if current_score > best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
            print("aic is {},continuing!".format(current_score))
        else:
            print("forward selection over!")
            break

    formula = "{} ~ {} ".format(response, " + ".join(selected))
    print("final formula is {}".format(formula))
    model = ols(formula=formula, data=data).fit()
    return model


data_for_select = exp[["avg_exp", "Income", "Age", "dist_home_val", "dist_avg_income"]]
lm_m = forward_select(data=data_for_select, response="avg_exp")
print(lm_m.rsquared)


# # 线性回归的诊断
# 残差分析

ana1 = lm_s


exp["Pred"] = ana1.predict(exp)  # 預測.predict
exp["resid"] = ana1.resid
exp.plot("Pred", "resid", kind="scatter")
show()

# 遇到异方差情况,教科书上会介绍使用加权最小二乘法，但是实际上最常用的是对被解释变量取对数
ana1 = ols("avg_exp ~ Income", exp).fit()
cc = ana1.summary()
print(cc)

ana2 = ols("avg_exp_ln ~ Income", exp).fit()
exp["Pred"] = ana2.predict(exp)  # 預測.predict
exp["resid"] = ana2.resid
exp.plot("Income", "resid", kind="scatter")
cc = ana2.summary()
print(cc)

show()


# 取对数会使模型更有解释意义

exp["Income_ln"] = np.log(exp["Income"])

ana3 = ols("avg_exp_ln ~ Income_ln", exp).fit()
exp["Pred"] = ana3.predict(exp)  # 預測.predict
exp["resid"] = ana3.resid
exp.plot("Income_ln", "resid", kind="scatter")
show()
cc = ana3.summary()
print(cc)

# 寻找最优的模型

r_sq = {
    "exp~Income": ana1.rsquared,
    "ln(exp)~Income": ana2.rsquared,
    "ln(exp)~ln(Income)": ana3.rsquared,
}
print(r_sq)

# 强影响点分析

exp["resid_t"] = (exp["resid"] - exp["resid"].mean()) / exp["resid"].std()


# Find outlier：

exp[abs(exp["resid_t"]) > 2]

# Drop outlier

exp2 = exp[abs(exp["resid_t"]) <= 2].copy()
ana4 = ols("avg_exp_ln ~ Income_ln", exp2).fit()
exp2["Pred"] = ana4.predict(exp2)  # 預測.predict
exp2["resid"] = ana4.resid
exp2.plot("Income", "resid", kind="scatter")
show()

ana4.rsquared


# statemodels包提供了更多强影响点判断指标

from statsmodels.stats.outliers_influence import OLSInfluence

cc = OLSInfluence(ana3).summary_frame().head()
print(cc)

# 增加变量
# 经过单变量线性回归的处理，我们基本对模型的性质有了一定的了解，接下来可以放入更多的连续型解释变量。在加入变量之前，要注意变量的函数形式转变。比如当地房屋均价、当地平均收入，其性质和个人收入一样，都需要取对数

exp2["dist_home_val_ln"] = np.log(exp2["dist_home_val"])
exp2["dist_avg_income_ln"] = np.log(exp2["dist_avg_income"])

ana5 = ols(
    """avg_exp_ln ~ Age + Income_ln + 
           dist_home_val_ln + dist_avg_income_ln""",
    exp2,
).fit()
cc = ana5.summary()
print(cc)

# 多重共线性分析

# Step regression is not always work.

ana5.bse  # The standard errors of the parameter estimates


# The function "statsmodels.stats.outliers_influence.variance_inflation_factor" uses "OLS" to fit data, and it will generates a wrong rsquared. So define it ourselves!


def vif(df, col_i):
    cols = list(df.columns)
    cols.remove(col_i)
    cols_noti = cols
    formula = col_i + "~" + "+".join(cols_noti)
    r2 = ols(formula, df).fit().rsquared
    return 1.0 / (1.0 - r2)


exog = exp2[["Income_ln", "dist_home_val_ln", "dist_avg_income_ln"]]

for i in exog.columns:
    print(i, "\t", vif(df=exog, col_i=i))


# Income_ln与dist_avg_income_ln具有共线性，使用“高出平均收入的比率”代替其中一个

exp2["high_avg_ratio"] = exp2["high_avg"] / exp2["dist_avg_income"]

exog1 = exp2[["high_avg_ratio", "dist_home_val_ln", "dist_avg_income_ln"]]

for i in exog1.columns:
    print(i, "\t", vif(df=exog1, col_i=i))

var_select = exp2[
    ["avg_exp_ln", "high_avg_ratio", "dist_home_val_ln", "dist_avg_income_ln"]
]
ana7 = forward_select(data=var_select, response="avg_exp_ln")
print(ana7.rsquared)

formula8 = """
avg_exp_ln ~ dist_avg_income_ln + dist_home_val_ln + 
C(gender) + C(Ownrent) + C(Selfempl) + C(edu_class)
"""
ana8 = ols(formula8, exp2).fit()
cc = ana8.summary()
print(cc)

formula9 = """
avg_exp_ln ~ dist_avg_income_ln + dist_home_val_ln + 
C(Selfempl) + C(gender):C(edu_class)
"""
ana9 = ols(formula9, exp2).fit()
cc = ana9.summary()
print(cc)


# 正则算法
# 岭回归

lmr = ols(
    "avg_exp ~ Income + dist_home_val + dist_avg_income", data=exp
).fit_regularized(alpha=1, L1_wt=0)

# L1_wt参数为0则使用岭回归，为1使用lasso


# LASSO算法

lmr1 = ols(
    "avg_exp ~ Age + Income + dist_home_val + dist_avg_income", data=exp
).fit_regularized(alpha=1, L1_wt=1)

# 使用scikit-learn进行正则化参数调优

from sklearn.preprocessing import StandardScaler

continuous_xcols = ["Age", "Income", "dist_home_val", "dist_avg_income"]  #  抽取连续变量
scaler = StandardScaler()  # 标准化
X = scaler.fit_transform(exp[continuous_xcols])
y = exp["avg_exp_ln"]

from sklearn.linear_model import RidgeCV

alphas = np.logspace(-2, 3, 100, base=10)

# Search the min MSE by CV
rcv = RidgeCV(alphas=alphas, store_cv_values=True)
rcv.fit(X, y)

print("The best alpha is {}".format(rcv.alpha_))
print("The r-square is {}".format(rcv.score(X, y)))
# Default score is rsquared

X_new = scaler.transform(exp_new[continuous_xcols])
np.exp(rcv.predict(X_new)[:5])  # 預測.predict

cv_values = rcv.cv_values_
n_fold, n_alphas = cv_values.shape

cv_mean = cv_values.mean(axis=0)
cv_std = cv_values.std(axis=0)
ub = cv_mean + cv_std / np.sqrt(n_fold)
lb = cv_mean - cv_std / np.sqrt(n_fold)

plt.semilogx(alphas, cv_mean, label="mean_score")
plt.fill_between(alphas, lb, ub, alpha=0.2)
plt.xlabel("$\\alpha$")
plt.ylabel("mean squared errors")
plt.legend(loc="best")
show()


cc = rcv.coef_
print(cc)

# 手动选择正则化系数——根据业务判断

# 岭迹图

from sklearn.linear_model import Ridge

ridge = Ridge()

coefs = []
for alpha in alphas:
    ridge.set_params(alpha=alpha)
    ridge.fit(X, y)
    coefs.append(ridge.coef_)

ax = plt.gca()

ax.plot(alphas, coefs)
ax.set_xscale("log")
plt.xlabel("alpha")
plt.ylabel("weights")
plt.title("Ridge coefficients as a function of the regularization")
plt.axis("tight")

show()

ridge.set_params(alpha=40)
ridge.fit(X, y)
ridge.coef_

cc = ridge.score(X, y)
print(cc)

# 预测
np.exp(ridge.predict(X_new)[:5])  # 預測.predict

# lasso
from sklearn.linear_model import LassoCV

lasso_alphas = np.logspace(-3, 0, 100, base=10)
lcv = LassoCV(alphas=lasso_alphas, cv=10)  # Search the min MSE by CV
lcv.fit(X, y)

print("The best alpha is {}".format(lcv.alpha_))
print("The r-square is {}".format(lcv.score(X, y)))
# Default score is rsquared

from sklearn.linear_model import Lasso

lasso = Lasso()
lasso_coefs = []
for alpha in lasso_alphas:
    lasso.set_params(alpha=alpha)
    lasso.fit(X, y)
    lasso_coefs.append(lasso.coef_)


ax = plt.gca()

ax.plot(lasso_alphas, lasso_coefs)
ax.set_xscale("log")
plt.xlabel("alpha")
plt.ylabel("weights")
plt.title("Lasso coefficients as a function of the regularization")
plt.axis("tight")

show()

print(lcv.coef_)

# 弹性网络

from sklearn.linear_model import ElasticNetCV

l1_ratio = [0.1, 0.5, 0.7, 0.9, 0.95, 0.99]

encv = ElasticNetCV(l1_ratio=l1_ratio)
encv.fit(X, y)

print("The best l1_ratio is {}".format(encv.l1_ratio_))
print("The best alpha is {}".format(encv.alpha_))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 线性回归

from statsmodels.formula.api import ols

"""
teleco_camp.csv 共有 9686 筆資料, 14 欄位
ID, Suc_flag, ARPU, PromCnt12, PromCnt36, PromCntMsg12, PromCntMsg36,Class,Age,Gender,HomeOwner,AvgARPU,AvgHomeValue,AvgIncome
12, 1,        50,   6,         10,        2, 3, 4, 51, M, H, 50, 33400,  39460
53, 0,          ,   5,         9,         1, 4, 3, 50, M, H, 49, 37600,  33545
67, 1,        25,   6,         11,        2, 4, 1, 51, F, H, 49, 100400, 42091
71, 1,        80,   7,         10,        2, 4, 1, 48, F, H, 47, 39900,  39313
"""

tele = pd.read_csv("data/teleco_camp.csv")

print(tele.shape)
print()
print(tele["ARPU"])
print()
cc = tele.describe(include="all")
print(cc)

#  抽取连续变量及分类变量以便后续使用
all_X = tele.columns[4:]
continuous_X = [
    "PromCnt12",
    "PromCnt36",
    "PromCntMsg12",
    "PromCntMsg36",
    "Age",
    "AvgARPU",
    "AvgHomeValue",
    "AvgIncome",
]
categorical_X = list(set(all_X) - set(continuous_X))

# 对字符串变量进行编码

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

tele["Gender"] = le.fit_transform(tele["Gender"])  # 对Gender进行自动编码

tele["HomeOwner"].replace({"H": 0, "U": 1}, inplace=True)

# 按ARPU是否为缺失值将数据分为两部分

arpu_known = tele[tele["ARPU"].notnull()].iloc[:, 3:].copy()
arpu_unknown = tele[tele["ARPU"].isnull()].iloc[:, 3:].copy()

print("已知的ARPU")
print("欄名columns")
cc = arpu_known.columns
print(cc)
print(type(arpu_known))
print(arpu_known.shape)
print(arpu_known)

print("未知的ARPU")
print(type(arpu_unknown))
print(arpu_unknown.shape)
print(arpu_unknown)

# 相关性分析

arpu_known.plot(kind="scatter", x="AvgHomeValue", y="AvgARPU")
show()

cc = arpu_known.corr(method="pearson")
print(cc)
"""
# 简单线性回归

lm_s = ols("ARPU ~ AvgARPU", data=arpu_known).fit()
cc = lm_s.summary()
print(cc)

# 多元线性回归

formula = "ARPU ~" + "+".join(continuous_X)
lm = ols(formula, data=arpu_known).fit()
cc = lm.summary()
print(cc)

# 线性回归的诊断

# 残差图

ana1 = lm_s

arpu_known["Pred"] = ana1.predict(arpu_known)  # 預測.predict
arpu_known["resid"] = ana1.resid
arpu_known.plot("AvgARPU", "resid", kind="scatter")
show()

# Find outlier

# standardize the resid
resid_mean = arpu_known["resid"].mean()
resid_std = arpu_known["resid"].std()

arpu_known["resid_t"] = (arpu_known["resid"] - resid_mean) / resid_std

cc = arpu_known[abs(arpu_known["resid_t"]) > 2].head()
print(cc)

# drop outlier

arpu_known2 = arpu_known[abs(arpu_known["resid_t"]) <= 2].copy()
ana2 = ols("ARPU ~ AvgARPU", arpu_known2).fit()
arpu_known2["Pred"] = ana2.predict(arpu_known2)  # 預測.predict
arpu_known2["resid"] = ana2.resid
arpu_known2.plot("AvgARPU", "resid", kind="scatter")
show()

cc = ana2.rsquared
print(cc)

# statemodels包提供了更多强影响点判断指标
from statsmodels.stats.outliers_influence import OLSInfluence

cc = OLSInfluence(ana1).summary_frame().head()
print(cc)

# 增加连续变量

# 多元线性回归的变量筛选


# 定义向前选择法变量筛选函数
def forward_select(data, response):
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = float("inf"), float("inf")
    while remaining:
        aic_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {}".format(response, " + ".join(selected + [candidate]))
            aic = ols(formula=formula, data=data).fit().aic
            aic_with_candidates.append((aic, candidate))
        aic_with_candidates.sort(reverse=True)
        best_new_score, best_candidate = aic_with_candidates.pop()
        if current_score > best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
            print("aic is {},continuing!".format(current_score))
        else:
            print("forward selection over!")
            break
    formula = "{} ~ {} ".format(response, " + ".join(selected))
    print("final formula is {}".format(formula))
    model = ols(formula=formula, data=data).fit()
    return (selected, model)


candidate_var = list(continuous_X)
candidate_var.append("ARPU")
data_for_select = arpu_known2[candidate_var]

selected_var, lm_m = forward_select(data=data_for_select, response="ARPU")  #  前向法选择变量
print(lm_m.rsquared)

# 多重共线性分析


def vif(df, col_i):
    cols = list(df.columns)
    cols.remove(col_i)
    cols_noti = cols
    formula = col_i + "~" + "+".join(cols_noti)
    r2 = ols(formula, df).fit().rsquared
    return 1.0 / (1.0 - r2)


exog = arpu_known2[selected_var]

for i in exog.columns:
    print(i, "\t", vif(df=exog, col_i=i))

# 增加分类变量

selected_var.extend(["C(Class)", "C(Gender)"])
formula2 = "ARPU ~" + "+".join(selected_var)
ana3 = ols(formula2, arpu_known2).fit()
cc = ana3.summary()
print(cc)

# 增加交互效应

selected_var.append("C(Class):C(Gender)")
formula3 = "ARPU ~" + "+".join(selected_var)
ana4 = ols(formula3, arpu_known2).fit()
cc = ana4.summary()
print(cc)

selected_var.remove("C(Gender)")
selected_var.remove("C(Class):C(Gender)")
selected_var.remove("Age")

formula4 = "ARPU ~" + "+".join(selected_var)
ana5 = ols(formula4, arpu_known2).fit()
cc = ana5.summary()
print(cc)

# 正则算法

# 岭回归

reg_var = list(continuous_X)
reg_var.extend(["C(Class)", "C(Gender)", "C(Class):C(Gender)", "C(HomeOwner)"])
formula5 = "ARPU ~" + "+".join(reg_var)
lmr = ols(formula5, data=arpu_known2).fit_regularized(alpha=0.01, L1_wt=0)
cc = lmr.summary()
print(cc)
# L1_wt参数为0则使用岭回归，为1使用lasso

# LASSO算法

lml = ols(formula5, data=arpu_known2).fit_regularized(alpha=0.01, L1_wt=0)
cc = lml.summary()
print(cc)

# scikit-learn中正则化参数调优

# 哑变量变换

from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder()
dummies = enc.fit_transform(arpu_known2[["Gender", "HomeOwner", "Class"]]).toarray()

X = arpu_known2[continuous_X].join(pd.DataFrame(dummies, index=arpu_known2.index))
y = arpu_known2[
    [
        "ARPU",
    ]
]

# 搜索最优正则化系数

from sklearn.linear_model import RidgeCV

alphas = np.logspace(-3, 2, 100, base=10)  # linspace

rcv = RidgeCV(alphas=alphas, store_cv_values=True)  # Search the min MSE by CV
rcv.fit(X, y)

print("The best alpha is {}".format(rcv.alpha_))
print("The r-square is {}".format(rcv.score(X, y)))  # Default score is rsquared

# 预测
cc = rcv.predict(X)[:5]  # 預測.predict
print(cc)

dummies_new = enc.transform(arpu_unknown[["Gender", "HomeOwner", "Class"]]).toarray()
X_new = arpu_unknown[continuous_X].join(
    pd.DataFrame(dummies_new, index=arpu_unknown.index)
)

cc = rcv.predict(X_new)[:5]  # 預測.predict
print(cc)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# creditcard_exp.py

# # 第6讲 统计推断基础
# 数据说明：本数据是地区房价增长率数据
# 名称-中文含义
# dis_name-小区名称
# rate-房价同比增长率

house_price_gr = pd.read_csv(r"data/house_price_gr.csv", encoding="gbk")
cc = house_price_gr.head()
print(cc)

# ## 6.1 参数估计
# 进行描述性统计分析

house_price_gr.describe(include="all")

# Histograph

# get_ipython().magic('matplotlib inline')

from scipy import stats

sns.histplot(house_price_gr.rate, kde=True)  # Histograph
show()

# Q-Q

fig = sm.qqplot(house_price_gr.rate, fit=True, line="45")
# fig.show()

# Box Plots

house_price_gr.plot(kind="box")  # Box Plots

# 置信度区间估计

se = house_price_gr.rate.std() / len(house_price_gr) ** 0.5
LB = house_price_gr.rate.mean() - 1.98 * se
UB = house_price_gr.rate.mean() + 1.98 * se
(LB, UB)


# 如果要求任意置信度下的置信区间的话，可以自己编一个函数
def confint(x, alpha=0.05):
    n = len(x)
    xb = x.mean()
    df = n - 1
    tmp = (x.std() / n**0.5) * stats.t.ppf(1 - alpha / 2, df)
    return {"Mean": xb, "Degree of Freedom": df, "LB": xb - tmp, "UB": xb + tmp}


confint(house_price_gr.rate, 0.05)


# 或者使用DescrStatsW
d1 = sm.stats.DescrStatsW(house_price_gr.rate)
d1.tconfint_mean(0.05)  #

# ## 6.2 假设检验与单样本T检验
# 当年住宅价格的增长率是否超过了10%的阈值

d1 = sm.stats.DescrStatsW(house_price_gr.rate)
print("t-statistic=%6.4f, p-value=%6.4f, df=%s" % d1.ttest_mean(0.1))


# ## 6.3 两样本T检验
# 数据说明：本数据是一份汽车贷款数据

# |字段名|中文含义|
# |:--:|:--:|
# |id|id|
# |Acc|是否开卡(1=已开通)|
# |avg_exp|月均信用卡支出（元）|
# |avg_exp_ln|月均信用卡支出的自然对数|
# |gender|性别(男=1)|
# |Age|年龄|
# |Income|年收入（万元）|
# |Ownrent|是否自有住房（有=1；无=0)|
# |Selfempl|是否自谋职业(1=yes, 0=no)|
# |dist_home_val|所住小区房屋均价(万元)|
# |dist_avg_income|当地人均收入|
# |high_avg|高出当地平均收入|
# |edu_class|教育等级：小学及以下开通=0，中学=1，本科=2，研究生=3|

creditcard = pd.read_csv(r"data/creditcard_exp.csv", skipinitialspace=True)

creditcard["Income"].groupby(creditcard["Acc"]).describe()

# 第一步:方差齐次检验

Suc0 = creditcard[creditcard["Acc"] == 0]["Income"]
Suc1 = creditcard[creditcard["Acc"] == 1]["Income"]
leveneTestRes = stats.levene(Suc0, Suc1, center="median")
print("w-value=%6.4f, p-value=%6.4f" % leveneTestRes)
# 第二步:T-test

stats.stats.ttest_ind(Suc0, Suc1, equal_var=False)
# Or Try: sm.stats.ttest_ind(gender0, gender1, usevar='pooled')
# 测试一下性别对是月均消费的作用.
# 注意对缺失值得处理
# creditcard['avg_exp'].groupby(creditcard['gender']).describe()
# female= creditcard[creditcard['gender'] == 0]['avg_exp'].dropna()
# male = creditcard[creditcard['gender'] == 1]['avg_exp'].dropna()
# leveneTestRes = stats.levene(female, male, center='median')
# print('w-value=%6.4f, p-value=%6.4f' %leveneTestRes)
# stats.stats.ttest_ind(female, male, equal_var=True)

# ## 6.4 方差分析
# 单因素方差分析

pd.set_option("display.max_columns", None)  # 设置显示所有列
creditcard.groupby("edu_class")[["avg_exp"]].describe().T

# 利用回归模型中的方差分析
from statsmodels.formula.api import ols

sm.stats.anova_lm(ols("avg_exp ~ C(edu_class)", data=creditcard).fit())

# 多因素方差分析

# 不考虑交互相

sm.stats.anova_lm(ols("avg_exp ~ C(edu_class)+C(gender)", data=creditcard).fit())
# 考虑交互相
sm.stats.anova_lm(
    ols(
        "avg_exp ~ C(edu_class)+C(gender)+C(edu_class)*C(gender)", data=creditcard
    ).fit()
)

# ## 6.5 相关分析
# 散点图

creditcard.plot(x="Income", y="avg_exp", kind="scatter")
# 当发现散点图有发散的趋势时，首先需要对Y取对数，而且还应该尝试对X也取对数

creditcard.plot(x="Income", y="avg_exp_ln", kind="scatter")
# 相关性分析:“spearman”,“pearson” 和 "kendall"
# creditcard['Income_ln']=np.log(creditcard['Income'])
creditcard[["avg_exp_ln", "Income"]].corr(method="pearson")

# ## 6.6卡方检验

cross_table = pd.crosstab(creditcard.edu_class, columns=creditcard.Acc)
# Or try this: accepts.pivot_table(index='bankruptcy_ind',columns='bad_ind', values='application_id', aggfunc='count')
cross_table

cross_table_rowpct = cross_table.div(cross_table.sum(1), axis=0)
cross_table_rowpct

print(
    "chisq = %6.4f\n p-value = %6.4f\n dof = %i\n expected_freq = %s"
    % stats.chi2_contingency(cross_table)
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
第6讲 统计推断基础
    数据说明：本数据是地区房价增长率数据
    名称-中文含义
    dis_name-小区名称
    rate-房价同比增长率
"""

house_price_gr = pd.read_csv("data/house_price_gr.csv", encoding="gbk")
cc = house_price_gr.head()
print(cc)

# 6.1 参数估计

# 进行描述性统计分析

cc = house_price_gr.describe(include="all")
print(cc)

from scipy import stats

sns.histplot(house_price_gr.rate, kde=True)  # Histograph

fig = sm.qqplot(house_price_gr.rate, fit=True, line="45")
# fig.show()

house_price_gr.plot(kind="box")  # Box Plots

# 置信度区间估计

se = house_price_gr.rate.std() / len(house_price_gr) ** 0.5
LB = house_price_gr.rate.mean() - 1.98 * se
UB = house_price_gr.rate.mean() + 1.98 * se
(LB, UB)


# 如果要求任意置信度下的置信区间的话，可以自己编一个函数
def confint(x, alpha=0.05):
    n = len(x)
    xb = x.mean()
    df = n - 1
    tmp = (x.std() / n**0.5) * stats.t.ppf(1 - alpha / 2, df)
    return {"Mean": xb, "Degree of Freedom": df, "LB": xb - tmp, "UB": xb + tmp}


confint(house_price_gr.rate, 0.05)

# 或者使用DescrStatsW
d1 = sm.stats.DescrStatsW(house_price_gr.rate)
d1.tconfint_mean(0.05)  #

# 6.2 假设检验与单样本T检验
# 当年住宅价格的增长率是否超过了10%的阈值

print("t-statistic=%6.4f, p-value=%6.4f, df=%s" % d1.ttest_mean(0.1))

# 一般认为FICO高于690的客户信誉较高，请检验该产品的客户整体信用是否高于690

"""
6.3 两样本T检验

    数据集描述与属性说明
    ID 客户编号
    Suc_flag 成功入网标识
    ARPU 入网后ARPU
    PromCnt12 12个月内的营销次数
    PromCnt36 36个月内的营销次数
    PromCntMsg12 12个月内发短信的次数
    PromCntMsg36 36个月内发短信的次数
    Class 客户重要性等级(根据前运营商消费情况)
    Age 年龄
    Gender 性别
    HomeOwner 是否拥有住房
    AvgARPU 当地平均ARPU
    AvgHomeValue 当地房屋均价
    AvgIncome 当地人均收入
"""

camp = pd.read_csv("data/tele_camp_okaaa.csv", skipinitialspace=True)
cc = camp.head()
print(cc)

# 根据是否入网比较外呼次数

camp["PromCnt12"].groupby(camp["Suc_flag"]).describe()

# 第一步:方差齐次检验

Suc0 = camp[camp["Suc_flag"] == 0]["PromCnt12"]
Suc1 = camp[camp["Suc_flag"] == 1]["PromCnt12"]
leveneTestRes = stats.levene(Suc0, Suc1, center="median")
print("w-value=%6.4f, p-value=%6.4f" % leveneTestRes)

# 第二步:T-test

stats.stats.ttest_ind(Suc0, Suc1, equal_var=False)
# Or Try: sm.stats.ttest_ind(gender0, gender1, usevar='pooled')

# 6.4 方差分析

# 单因素方差分析

pd.set_option("display.max_columns", None)  # 设置显示所有列
camp.groupby("Class")[["PromCnt12"]].describe().T

# 利用回归模型中的方差分析
from statsmodels.formula.api import ols

sm.stats.anova_lm(ols("PromCnt12 ~ C(Class)", data=camp).fit())

# 多因素方差分析

# NG
# sm.stats.anova_lm(ols('PromCnt12 ~ C(Class)+C(Age_group1)',data=camp).fit())

# 6.5 相关分析

# 散点图

camp.plot(x="AvgARPU", y="ARPU", kind="scatter")
show()

# 相关性分析:“spearman”,“pearson” 和 "kendall"

camp[["AvgARPU", "ARPU"]].corr(method="pearson")

# 6.6卡方检验

cross_table = pd.crosstab(camp.Class, columns=camp.Suc_flag)
# Or try this: accepts.pivot_table(index='bankruptcy_ind',columns='bad_ind', values='application_id', aggfunc='count')
cc = cross_table
print(cc)

print(
    "chisq = %6.4f\n p-value = %6.4f\n dof = %i\n expected_freq = %s"
    % stats.chi2_contingency(cross_table)
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# tele_camp_ok.py

# # 第6讲 统计推断基础
# 数据说明：本数据是地区房价增长率数据
# 名称-中文含义
# dis_name-小区名称
# rate-房价同比增长率

house_price_gr = pd.read_csv(r"data/house_price_gr.csv", encoding="gbk")
cc = house_price_gr.head()
print(cc)

# ## 6.1 参数估计
# 进行描述性统计分析

house_price_gr.describe(include="all")

# Histograph

# get_ipython().magic('matplotlib inline')

from scipy import stats

sns.histplot(house_price_gr.rate, kde=True)  # Histograph

# Q-Q

fig = sm.qqplot(house_price_gr.rate, fit=True, line="45")
# fig.show()

# Box Plots

house_price_gr.plot(kind="box")  # Box Plots

# 置信度区间估计

se = house_price_gr.rate.std() / len(house_price_gr) ** 0.5
LB = house_price_gr.rate.mean() - 1.98 * se
UB = house_price_gr.rate.mean() + 1.98 * se
(LB, UB)


# 如果要求任意置信度下的置信区间的话，可以自己编一个函数
def confint(x, alpha=0.05):
    n = len(x)
    xb = x.mean()
    df = n - 1
    tmp = (x.std() / n**0.5) * stats.t.ppf(1 - alpha / 2, df)
    return {"Mean": xb, "Degree of Freedom": df, "LB": xb - tmp, "UB": xb + tmp}


confint(house_price_gr.rate, 0.05)

# 或者使用DescrStatsW
d1 = sm.stats.DescrStatsW(house_price_gr.rate)
d1.tconfint_mean(0.05)

# ## 6.2 假设检验与单样本T检验
# 当年住宅价格的增长率是否超过了10%的阈值

d1 = sm.stats.DescrStatsW(house_price_gr.rate)
print("t-statistic=%6.4f, p-value=%6.4f, df=%s" % d1.ttest_mean(0.1))
# 一般认为FICO高于690的客户信誉较高，请检验该产品的客户整体信用是否高于690


# ## 6.3 两样本T检验
# 数据集描述与属性说明
# ID	客户编号
# Suc_flag	成功入网标识
# ARPU	入网后ARPU
# PromCnt12	12个月内的营销次数
# PromCnt36	36个月内的营销次数
# PromCntMsg12	12个月内发短信的次数
# PromCntMsg36	36个月内发短信的次数
# Class	客户重要性等级(根据前运营商消费情况)
# Age	年龄
# Gender	性别
# HomeOwner	是否拥有住房
# AvgARPU	当地平均ARPU
# AvgHomeValue	当地房屋均价
# AvgIncome	当地人均收入

camp = pd.read_csv(r"data/tele_camp_ok.csv", skipinitialspace=True)
cc = camp.head()
print(cc)

# 检验当地客户平均客户价值对是否入网的影响

camp["AvgARPU"].groupby(camp["Suc_flag"]).describe()

# 第一步:方差齐次检验

Suc0 = camp[camp["Suc_flag"] == 0]["AvgARPU"]
Suc1 = camp[camp["Suc_flag"] == 1]["AvgARPU"]
leveneTestRes = stats.levene(Suc0, Suc1, center="median")
print("w-value=%6.4f, p-value=%6.4f" % leveneTestRes)

# 第二步:T-test

stats.stats.ttest_ind(Suc0, Suc1, equal_var=False)
# Or Try: sm.stats.ttest_ind(gender0, gender1, usevar='pooled')

# 测试一下营销次数对是否响应的作用.
# camp['PromCnt12'].groupby(camp['Suc_flag']).describe()
# Suc0 = camp[camp['Suc_flag'] == 0]['PromCnt12']
# Suc1 = camp[camp['Suc_flag'] == 1]['PromCnt12']
# leveneTestRes = stats.levene(Suc0, Suc1, center='median')
# print('w-value=%6.4f, p-value=%6.4f' %leveneTestRes)
# stats.stats.ttest_ind(Suc0, Suc1, equal_var=False)

# ## 6.4 方差分析
# 单因素方差分析

pd.set_option("display.max_columns", None)  # 设置显示所有列
camp.groupby("Class")[["ARPU"]].describe().T

# 利用回归模型中的方差分析
from statsmodels.formula.api import ols

sm.stats.anova_lm(ols("ARPU ~ C(Class)", data=camp).fit())

# 多因素方差分析

# 不考虑交互相

sm.stats.anova_lm(ols("ARPU ~ C(Class)+C(Gender)", data=camp).fit())
# 考虑交互相
sm.stats.anova_lm(ols("ARPU ~ C(Class)+C(Gender)+C(Class)*C(Gender)", data=camp).fit())

# ## 6.5 相关分析
# 散点图

camp.plot(x="AvgARPU", y="ARPU", kind="scatter")

camp["AvgARPU_ln"] = np.log(camp["AvgARPU"])
camp["ARPU_ln"] = np.log(camp["ARPU"])

camp.plot(x="AvgARPU_ln", y="ARPU_ln", kind="scatter")
# 相关性分析:“spearman”,“pearson” 和 "kendall"

camp[["AvgARPU_ln", "ARPU_ln"]].corr(method="pearson")

# ## 6.6卡方检验

cross_table = pd.crosstab(camp.Class, columns=camp.Suc_flag)
# Or try this: accepts.pivot_table(index='bankruptcy_ind',columns='bad_ind', values='application_id', aggfunc='count')
cross_table

cross_table_rowpct = cross_table.div(cross_table.sum(1), axis=0)
cross_table_rowpct

print(
    "chisq = %6.4f\n p-value = %6.4f\n dof = %i\n expected_freq = %s"
    % stats.chi2_contingency(cross_table)
)

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
