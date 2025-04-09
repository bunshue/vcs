"""



"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import datetime
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

from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

import warnings

warnings.filterwarnings("once")

print("------------------------------------------------------------")  # 60個

import sklearn.metrics as metrics
import statsmodels.api as sm


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

# 日期时间

now = time.strptime("2016-07-20", "%Y-%m-%d")
print(now)

type(now)

cc = time.strftime("%Y-%m-%d", now)
print(cc)

someDay = datetime.date(1999, 2, 10)
anotherDay = datetime.date(1999, 2, 15)
deltaDay = anotherDay - someDay
print(deltaDay.days)

date_formate = "%Y-%m-%d"  # year-month-day
cc = time.strptime("2016-06-22", date_formate)
print(cc)

# 复数complex

cplx = (4 + 2j) * (3 + 0.2j)
print(cplx)


# ## 3.2 Python数据结构
# 列表（list）、元组（tuple）、集合（set）、字典（dict）

# 3.2.1 列表(list)

# 用来存储一连串元素的容器，列表用[]来表示，其中元素的类型可不相同。

students = ["ming", "hua", "li", "juan", "yun", 3]
print(students)

# 插入元素
students.append("han")  # 添加到尾部
students.extend(["long", "wan"])
print(students)

scores = [90, 80, 75, 66]
students.insert(1, scores)  # 添加到指定位置
print(students)

# 删除元素

print(students.pop(1))  # 该函数返回被弹出的元素，不传入参数则删除最后一个元素
print(students)

# 判断元素是否在列表中等

print("wan" in students)
print("han" not in students)

students.count("wan")

students.index("wan")

# 集合

studentsSet = set(students)
print(studentsSet)

studentsSet.add("xu")
print(studentsSet)

studentsSet.remove("xu")
print(studentsSet)

a = set("abcnmaaaaggsng")
print("a=", a)
b = set("cdfm")
print("b=", b)

# 交集
x = a & b
print("x=", x)
# 并集
y = a | b
print("y=", y)
# 差集
z = a - b
print("z=", z)
# 去除重复元素
new = set(a)
print(z)

k = {"name": "weiwei", "home": "guilin"}
print(k["home"])
print(k.keys())
print(k.values())

a = {
    "success": True,
    "reason_code": "200",
    "reason_desc": "获取成功",
    "rules": [
        {
            "rule_id": "1062274",
            "score": 7,
            "conditions": [
                {
                    "address_a_value": "南通市",
                    "address_a": "mobile_address",
                    "address_b": "true_ip_address",
                    "address_b_value": "南京市",
                    "type": "match_address",
                }
            ],
        }
    ],
}
print(a["success"])


# 添加、修改字典里面的项目

k["like"] = "music"
k["name"] = "guangzhou"
print(k)

# 2.2.5 列表、元组、集合、字典的互相转换

tuple(students)
list(k)

zl = zip(("A", "B", "C"), [1, 2, 3, 4])  # zip可以将列表、元组、集合、字典‘缝合’起来
print(zl)
print(type(zl))
print(dict(zl))

heights = {"Yao": 226, "Sharq": 216, "AI": 183}
for i in heights:
    print(i, heights[i])

# for key, value in heights.items():-Python3 不能使用dict.iteritems(),改为dict.items()
for key, value in heights.items():
    print(key, value)


# 匿名函数：高阶函数传入函数时，不需要显式地定义函数，直接传入匿名函数更方便
f = lambda x: x * x
f(4)

df = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "a", "b"], "data1": range(7)})
df.head(2)

df1 = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "a", "b"], "data1": range(7)})
df1.head(5)

df2 = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "a", "b"], "data1": range(7)})
cc = pd.crosstab(df2.key, df2.data1)
print(cc)

# ## 3.6 使用pandas读写数据

# pandas可以读取文本文件、json、数据库、Excel等文件
# 使用read_csv方法读取以逗号分隔的文本文件作为DataFrame，其它还有类似read_table, read_excel, read_html, read_sql等等方法

one = pd.read_csv("data/One.csv", sep=",")  # same
one = pd.read_csv("data/One.csv")
cc = one.head()
print(cc)


hsb2 = pd.read_table("data/hsb2.txt")
cc = hsb2.head()
print(cc)

html = pd.read_html(
    "http://www.fdic.gov/bank/individual/failed/banklist.html"
)  # Return a list
print(html)

# xls = pd.read_excel('hsb2.xlsx', sheetname=0) NG
xls = pd.read_excel("data/hsb2.xlsx")
cc = xls.head()
print(cc)

# df存檔  xls.to_csv("tmp_copyofhsb2.csv")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
RFM 是一種客戶分析模型，根據客戶的消費行為以進行客戶區分的一種方法。

RFM
Recency (最近一次交易)
Frequency (交易頻率)
Monetary (交易金額)

通過這三個消費行為的維度，對客戶進行分類，找出最有價值、最活躍的顧客，
同時也能對不同層級的客戶進行相對應的行銷活動，進而實現精準分群行銷。
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 1. 导入数据

trad_flow = pd.read_csv(r"data/RFM_TRAD_FLOW.csv", encoding="gbk")
cc = trad_flow.head(10)

print(cc)

# 2.通过 RFM方法 建立 模型

# 2.1 通过计算F反应客户对打折产品的偏好
F = trad_flow.groupby(["cumid", "type"])[["transID"]].count()
F.head()

F_trans = pd.pivot_table(F, index="cumid", columns="type", values="transID")
F_trans.head()

F_trans["Special_offer"] = F_trans["Special_offer"].fillna(0)
F_trans.head()

F_trans["interest"] = F_trans["Special_offer"] / (
    F_trans["Special_offer"] + F_trans["Normal"]
)
F_trans.head()

# 2.2 通过计算M反应客户的价值信息
M = trad_flow.groupby(["cumid", "type"])[["amount"]].sum()
M.head()

M_trans = pd.pivot_table(M, index="cumid", columns="type", values="amount")
M_trans["Special_offer"] = M_trans["Special_offer"].fillna(0)
M_trans["returned_goods"] = M_trans["returned_goods"].fillna(0)
M_trans["value"] = (
    M_trans["Normal"] + M_trans["Special_offer"] + M_trans["returned_goods"]
)
M_trans.head()

# 2.3 通过计算R反应客户是否为沉默客户
# 定义一个从文本转化为时间的函数
from datetime import datetime


def to_time(t):
    out_t = time.mktime(
        time.strptime(t, "%d%b%y:%H:%M:%S")
    )  ########此处修改为时间戳方便后面qcut函数分箱
    return out_t


a = "14JUN09:17:58:34"
print(to_time(a))

trad_flow["time_new"] = trad_flow.time.apply(to_time)
trad_flow.head()

R = trad_flow.groupby(["cumid"])[["time_new"]].max()
R.head()

# 3.构建模型，筛选目标客户

from sklearn import preprocessing

threshold = pd.qcut(F_trans["interest"], 2, retbins=True)[1][1]
binarizer = preprocessing.Binarizer(threshold=threshold)
interest_q = pd.DataFrame(
    binarizer.transform(F_trans["interest"].values.reshape(-1, 1))
)
interest_q.index = F_trans.index
interest_q.columns = ["interest"]

threshold = pd.qcut(M_trans["value"], 2, retbins=True)[1][1]
binarizer = preprocessing.Binarizer(threshold=threshold)
value_q = pd.DataFrame(binarizer.transform(M_trans["value"].values.reshape(-1, 1)))
value_q.index = M_trans.index
value_q.columns = ["value"]

threshold = pd.qcut(R["time_new"], 2, retbins=True)[1][1]
binarizer = preprocessing.Binarizer(threshold=threshold)
time_new_q = pd.DataFrame(binarizer.transform(R["time_new"].values.reshape(-1, 1)))
time_new_q.index = R.index
time_new_q.columns = ["time"]

analysis = pd.concat([interest_q, value_q, time_new_q], axis=1)

# analysis['rank']=analysis.interest_q+analysis.interest_q
analysis = analysis[["interest", "value", "time"]]
analysis.head()

label = {
    (0, 0, 0): "无兴趣-低价值-沉默",
    (1, 0, 0): "有兴趣-低价值-沉默",
    (1, 0, 1): "有兴趣-低价值-活跃",
    (0, 0, 1): "无兴趣-低价值-活跃",
    (0, 1, 0): "无兴趣-高价值-沉默",
    (1, 1, 0): "有兴趣-高价值-沉默",
    (1, 1, 1): "有兴趣-高价值-活跃",
    (0, 1, 1): "无兴趣-高价值-活跃",
}
analysis["label"] = analysis[["interest", "value", "time"]].apply(
    lambda x: label[(x[0], x[1], x[2])], axis=1
)
analysis.head()

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

# 导入数据和数据清洗

raw = pd.read_csv(r"data/creditcard_exp.csv", skipinitialspace=True)
raw.head()

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

pd.DataFrame([lm_s.predict(exp), lm_s.resid], index=["predict", "resid"]).T.head()


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

# 高级分类器：支持向量机(SVM)与凸优化

from scipy import stats

orgData = pd.read_csv("data/date_data.csv")
cc = orgData.describe()
print(cc)

# 提取如下字段进行建模

X = orgData.iloc[:, :4]
Y = orgData["Dated"]

# 資料分割
train_data, test_data, train_target, test_target = train_test_split(X, Y, test_size=0.2)

# 使用svm，建立支持向量机模型

from sklearn import svm

svcModel = svm.SVC(kernel="rbf", gamma=0.5, C=0.5, probability=True).fit(
    train_data, train_target
)

# 初步评估
test_est = svcModel.predict(test_data)  # 預測.predict
print(metrics.classification_report(test_target, test_est))  # 计算评估指标

# 进行标准化可以提升高斯核svm的表现

from sklearn import preprocessing

scaler = preprocessing.StandardScaler().fit(train_data)
train_scaled = scaler.transform(train_data)
test_scaled = scaler.transform(test_data)

svcModel1 = svm.SVC(kernel="rbf", gamma=0.5, C=0.5, probability=True).fit(
    train_scaled, train_target
)
test_est1 = svcModel1.predict(test_scaled)  # 預測.predict
print(metrics.classification_report(test_target, test_est1))  # 计算评估指标

# 选择最优模型

from sklearn.model_selection import ParameterGrid
from sklearn.model_selection import GridSearchCV

kernel = ("linear", "rbf")
gamma = np.arange(0.01, 1, 0.1)
CCC = np.arange(0.01, 1.0, 0.1)
grid = {"gamma": gamma, "C": CCC}

clf_search = GridSearchCV(estimator=svcModel1, param_grid=grid, cv=4)
clf_search.fit(train_scaled, train_target)

best_model = clf_search.best_estimator_
test_est2 = best_model.predict(test_scaled)  # 預測.predict
print(metrics.classification_report(test_target, test_est2))  # 计算评估指标

best_model

# 画出在svm模型中，两个变量的关系图，可以用于提升感性认识，但一般不能推广到大于两维的情况

train_x = train_scaled[:, 1:3]
train_y = train_target.values
h = 1.0  # step size in the mesh
CCC = 1.0  # SVM regularization parameter
svc = svm.SVC(kernel="linear", C=CCC).fit(train_x, train_y)
rbf_svc = svm.SVC(kernel="rbf", gamma=0.5, C=1).fit(train_x, train_y)
poly_svc = svm.SVC(kernel="poly", degree=3, C=CCC).fit(train_x, train_y)
lin_svc = svm.LinearSVC(C=CCC).fit(train_x, train_y)

# create a mesh to plot in
x_min, x_max = train_x[:, 0].min() - 1, train_x[:, 0].max() + 1
y_min, y_max = train_x[:, 1].min() - 1, train_x[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# title for the plots
titles = [
    "SVC with linear kernel",
    "LinearSVC (linear kernel)",
    "SVC with RBF kernel",
    "SVC with polynomial (degree 3) kernel",
]
plt.figure(figsize=(8, 8))
for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc)):
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    plt.subplot(2, 2, i + 1)
    plt.subplots_adjust(wspace=0.2, hspace=0.2)

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])  # 預測.predict

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.7)

    # Plot also the training points
    plt.scatter(train_x[:, 0], train_x[:, 1], c=train_y, cmap=plt.cm.coolwarm)
    plt.xlabel("Attractive")
    plt.ylabel("Assets")
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
第4讲 描述性统计分析基础

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

# 读取数据
camp = pd.read_csv("data/teleco_camp2.csv")

# 数据预处理
camp.dtypes

camp.describe(include="all")

camp["Suc_flag"] = camp["Suc_flag"].astype("category")
camp["Class"] = camp["Class"].astype("category")

# 3.1 描述性统计与探索型数据分析

# 1.分类变量分析

cc = camp["Suc_flag"].groupby(camp["Suc_flag"]).count()
print(cc)

# 2.连续变量分析
# 2.1.数据的集中趋势 ARPU的均值与中位数

fs = camp["ARPU"]  # 可以使用camp.ARPU
type(fs)

print("mean = %6.4f" % fs.mean())  # 求fs的均值
print("median = %6.4f" % fs.median())  # 求fs的中位数
print("quantiles\n", fs.quantile([0.25, 0.5, 0.75]))  # 求a的上下四分位数与中位数

fs.plot(kind="hist")
show()

# 2.2.数据的离散程度

# print ('mad = %6.4f' %fs.mad())      # 求平均绝对偏差 mad = np.abs(fs - fs.mean()).mean()
print("range = %6.4f" % (fs.max(skipna=True) - fs.min(skipna=True)))  # 求极差
print("var = %6.4f" % fs.var())  # 求方差
print("std = %6.4f" % fs.std())  # 求标准差

# 2.3.数据的偏度与峰度- ARPU:右偏

plt.hist(fs.dropna(), bins=15)
show()

print("skewness = %6.4f" % fs.skew(skipna=True))
print("kurtosis = %6.4f" % fs.kurt(skipna=True))
"""
#2.4.分布- 正态分布模拟函数

from scipy import stats

x = map(lambda x: x / 10., range(-40, 41))
norm = stats.norm.pdf(x, loc=0, scale=1) # 随机正态分布概率密度(均值为0，标准差为1)
plt.plot(x, norm)
show()

points = map(lambda x: x / 10.0, range(-40, 41))
plt.plot(points, stats.norm.cdf(points,loc=0, scale=1)) # 正态分布函数
show()

#卡方分布模拟

x = range(1, 31)
chi = stats.chi2.pdf(x, df=3, loc=0, scale=1) #生成自由度为3的卡方分布概率密度
plt.plot(x, chi)
show()

#t分布模拟

x = np.arange(-4, 4, 0.1)
student_t = stats.t.pdf(x, df=5, loc=0, scale=1)#生成自由度为5的t分布的概率密度值
norm = stats.norm.pdf(x, loc=0, scale=1)
plt.plot(x, student_t, 'b-')
plt.plot(x, norm, 'r--')
show()
"""
# 3.2 apply\map\groupby及其它相关

data = pd.DataFrame(data={"a": range(1, 11), "b": np.random.randn(10)})
data.T

data.apply(np.mean)  # 等价于data.mean()，是其完整形式

data.apply(lambda x: x.astype("str")).dtypes  # DataFrame没有astype方法，只有Series有

(data["a"] - data["a"].mean()) / data["a"].std()

data["a"].map(
    lambda x: (x - data["a"].mean()) / data["a"].std()
)  # 等价于(data['a']- data['a'].mean()) / data['a'].std()

data["a"].map(lambda x: int(str(x), base=16))  # 不支持“广播”时，可以使用map进行函数映射

# 分组-应用/聚合

key = [1, 2] * 5
print(key)

group1, group2 = data.groupby(key)  # 使用groupby可按照‘key’进行分组，‘key’需与待分组数据有同样长度
print(group1)
print(group2)

data.groupby(key).aggregate(np.mean)
# 聚合函数在各分组中进行聚合，是data.groupby(key).mean()的完整形式，可传入函数或字符串(sum/mean/median/std/var等)，也可传入列表

data.groupby(key).agg({"a": "sum", "b": "count"})  # agg可以在多列上使用不同的聚合函数

data.groupby(key).transform(np.mean)  # 转换函数可在各分组内进行运算，将结果广播到原数据中

data.groupby(key).apply(np.mean)  # apply是一般化的‘分组-应用/聚合’函数，更灵活地实现aggregate或transform的功能

# *练习：对camp数据集，按照客户级别汇总ARPU

camp["ARPU"].groupby(camp["Class"]).apply(lambda x: x.describe())

camp[["PromCnt12", "PromCnt36"]].groupby(camp["Suc_flag"]).mean()

# crosstab 和pivot_table

pd.crosstab(camp.Suc_flag, camp.Class)

camp.pivot_table(
    ["PromCnt12", "PromCnt36"], index="Suc_flag", columns="Class", aggfunc=np.mean
)  # index、columns、aggfunc参数均可传入列表

# 3.3绘图

# 散点图

camp.plot(x="AvgARPU", y="ARPU", kind="scatter")  # 散点图
plt.text(60, 1100, "ARPU VS AvgARPU")  # 加标签
show()

# 柱图/条形图、折线图

data.b.plot(kind="bar")  # 柱图
show()

data.b.plot(kind="line")  # 折线图
show()

# 直方图

camp[["PromCnt12", "PromCnt36"]].plot(stacked=False, kind="hist", alpha=0.3, bins=20)
camp[["PromCnt12", "PromCnt36"]].hist(alpha=0.8, bins=20, figsize=(10, 2))

# 饼图

gb = camp["Suc_flag"].groupby(camp["Suc_flag"]).count()
gb.plot(
    kind="pie",
    labels=["Yes", "No"],
    colors=["r", "g"],
    autopct="%.2f",
    fontsize=20,
    figsize=(6, 6),
)
show()

# 箱线图

camp[["PromCnt12", "Suc_flag"]].boxplot(by="Suc_flag")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def stack2dim(raw, i, j, rotation=0, location="upper right"):
    """
    此函数是为了画两个维度标准化的堆积柱状图
    raw为pandas的DataFrame数据框
    i、j为两个分类变量的变量名称，要求带引号，比如"school"
    rotation：水平标签旋转角度，默认水平方向，如标签过长，可设置一定角度，比如设置rotation = 40
    location：分类标签的位置，如果被主体图形挡住，可更改为'upper left'
    """
    data_raw = pd.crosstab(raw[i], raw[j])
    data = data_raw.div(data_raw.sum(1), axis=0)  # 交叉表转换成比率，为得到标准化堆积柱状图

    # 计算x坐标，及bar宽度
    createVar = locals()
    x = [0]  # 每个bar的中心x轴坐标
    width = []  # bar的宽度
    k = 0
    for n in range(len(data)):
        # 根据频数计算每一列bar的宽度
        createVar["width" + str(n)] = list(data_raw.sum(axis=1))[n] / sum(
            data_raw.sum(axis=1)
        )
        width.append(createVar["width" + str(n)])
        if n == 0:
            continue
        else:
            k += (
                createVar["width" + str(n - 1)] / 2
                + createVar["width" + str(n)] / 2
                + 0.05
            )
            x.append(k)

    # 以下是通过频率交叉表矩阵生成一串对应堆积图每一块位置数据的数组，再把数组转化为矩阵
    y_mat = []
    n = 0
    y_level = len(data.columns)
    for p in range(data.shape[0]):
        for q in range(data.shape[1]):
            n += 1
            y_mat.append(data.iloc[p, q])
            if n == data.shape[0] * data.shape[1]:
                break
            elif n % y_level != 0:
                y_mat.extend([0] * (len(data) - 1))
            elif n % y_level == 0:
                y_mat.extend([0] * len(data))

    y_mat = np.array(y_mat).reshape(-1, len(data))
    y_mat = pd.DataFrame(y_mat)  # bar图中的y变量矩阵，每一行是一个y变量

    # 通过x，y_mat中的每一行y，依次绘制每一块堆积图中的每一块图

    from matplotlib import cm

    cm_subsection = [level for level in range(y_level)]
    colors = [cm.Pastel1(color) for color in cm_subsection]

    bottom = [0] * y_mat.shape[1]
    createVar = locals()
    for row in range(len(y_mat)):
        createVar["a" + str(row)] = y_mat.iloc[row, :]
        color = colors[row % y_level]

        if row % y_level == 0:
            bottom = bottom = [0] * y_mat.shape[1]
            if math.floor(row / y_level) == 0:
                label = data.columns.name + ": " + str(data.columns[row])
                plt.bar(
                    x,
                    createVar["a" + str(row)],
                    width=width[math.floor(row / y_level)],
                    label=label,
                    color=color,
                )
            else:
                plt.bar(
                    x,
                    createVar["a" + str(row)],
                    width=width[math.floor(row / y_level)],
                    color=color,
                )
        else:
            if math.floor(row / y_level) == 0:
                label = data.columns.name + ": " + str(data.columns[row])
                plt.bar(
                    x,
                    createVar["a" + str(row)],
                    bottom=bottom,
                    width=width[math.floor(row / y_level)],
                    label=label,
                    color=color,
                )
            else:
                plt.bar(
                    x,
                    createVar["a" + str(row)],
                    bottom=bottom,
                    width=width[math.floor(row / y_level)],
                    color=color,
                )

        bottom += createVar["a" + str(row)]

    plt.title(j + " vs " + i)
    group_labels = [str(name) for name in data.index]
    plt.xticks(x, group_labels, rotation=rotation)
    plt.ylabel(j)
    plt.legend(shadow=True, loc=location)
    show()


# # 一、使用sndHsPr

import matplotlib

# get_ipython().magic('matplotlib inline')

snd = pd.read_csv("data/sndHsPr.csv")

snd["all_pr2"] = snd[["price", "AREA"]].apply(lambda x: x[0] * x[1], axis=1)
snd.head()

# 1、把dist變量重新編碼為中文，比如chaoyang改為朝陽區。1）先作頻次統計，然后繪制柱形圖圖展現每個區樣本的數量；

# 把dist變量重新編碼為中文，比如chaoyang改為朝陽區。

district = {
    "fengtai": "豐臺區",
    "haidian": "海淀區",
    "chaoyang": "朝陽區",
    "dongcheng": "東城區",
    "xicheng": "西城區",
    "shijingshan": "石景山區",
}
snd["district"] = snd.dist.map(district)
# snd_new = snd.drop('dist',axis = 1)
snd.head()

# 4.1 描述性統計與探索型數據分析
# 1單因子頻數:描述名義變量的分布

# snd.dist.value_counts()
snd.district.value_counts()
# type(snd.district.value_counts())
# snd.district.value_counts()/snd.district.count()

snd.district.value_counts().plot(kind="bar")
# snd.district.value_counts().plot(kind = 'pie')

# 2 單變量描述:描述連續變量的分布

snd.price.mean()

snd.price.median()

snd.price.std()

snd.price.skew()

snd.price.agg(["mean", "median", "sum", "std", "skew"])

snd.price.quantile([0.01, 0.5, 0.99])

snd.price.hist(bins=40)

# 4.2 描述統計方法大全
# 1.1表分析

sub_sch = pd.crosstab(snd.district, snd.school)
sub_sch

pd.crosstab(snd.dist, snd.subway).plot(kind="bar")

# pd.crosstab(snd.district,snd.school).plot(kind = 'bar')
t1 = pd.crosstab(snd.district, snd.school)
t1.plot(kind="bar", stacked=True)
type(t1)

sub_sch = pd.crosstab(snd.district, snd.school)
sub_sch["sum1"] = sub_sch.sum(1)
sub_sch.head()

sub_sch = sub_sch.div(sub_sch.sum1, axis=0)
sub_sch

sub_sch[[0, 1]].plot(kind="bar", stacked=True)

stack2dim(snd, i="district", j="school")

from pyecharts import Map

# from echarts-china-cities-pypkg import *
"""
官網給的解釋如下：
自從 0.3.2 開始，為了縮減項目本身的體積以及維持 pyecharts 項目的輕量化運行，pyecharts 將不再自帶地圖 js 文件。如用戶需要用到地圖圖表，可自行安裝對應的地圖文件包。下面介紹如何安裝。
全球國家地圖: echarts-countries-pypkg (1.9MB): 世界地圖和 213 個國家，包括中國地圖
中國省級地圖: echarts-china-provinces-pypkg (730KB)：23 個省，5 個自治區
中國市級地圖: echarts-china-cities-pypkg (3.8MB)：370 個中國城市:https://github.com/echarts-maps/echarts-china-cities-js
pip install echarts-countries-pypkg
pip install echarts-china-provinces-pypkg
pip install echarts-china-cities-pypkg
別注明，中國地圖在 echarts-countries-pypkg 里。
"""
snd_price = list(
    zip(
        snd.price.groupby(snd.district).mean().index,
        snd.price.groupby(snd.district).mean().values,
    )
)
attr, value = Map.cast(snd_price)
min_ = snd.price.groupby(snd.dist).mean().min()
max_ = snd.price.groupby(snd.dist).mean().max()

map = Map("北京各區房價", width=1200, height=600)
map.add(
    "",
    attr,
    value,
    maptype="北京",
    is_visualmap=True,
    visual_range=[min_, max_],
    visual_text_color="#000",
    is_label_show=True,
)
map.render()

# ![北京房價](北京各區房價.png)

# 1.2 分類匯總
snd.price.groupby(snd.district).mean().plot(kind="bar")

snd.price.groupby(snd.district).mean().sort_values(ascending=True).plot(kind="barh")

sns.boxplot(x="district", y="price", data=snd)

# 1.3 匯總表

snd.pivot_table(values="price", index="district", columns="school", aggfunc=np.mean)

snd.pivot_table(
    values="price", index="district", columns="school", aggfunc=np.mean
).plot(kind="bar")

# 1.4、兩個連續變量---使用area和price做散點圖，分析area是否影響單位面積房價

snd.plot.scatter(x="AREA", y="price")

# 1.5 雙軸圖 需要導入GDP數據

# 按年度匯總GDP，并計算GDP增長率。繪制雙軸圖。GDP為柱子，GDP增長率為線。

gdp = pd.read_csv("data/gdp_gdpcr.csv", encoding="gbk")
gdp.head()

x = list(gdp.year)
GDP = list(gdp.GDP)
GDPCR = list(gdp.GDPCR)
fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.bar(x, GDP)
ax1.set_ylabel("GDP")
ax1.set_title("GDP of China(2000-2017)")
ax1.set_xlim(2000, 2018)

ax2 = ax1.twinx()
ax2.plot(x, GDPCR, "r")
ax2.set_ylabel("Increase Ratio")
ax2.set_xlabel("Year")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

######################################################################################################################################
# 以下內容為第8章內容
# 3、對age按照5歲間隔分段，命名為age_group，用loss_flag對age_group作logit圖。
# 1）手工計算Logit,即WOE

from sklearn import tree
from sklearn.model_selection import cross_val_score


class WoE:
    """
    Basic functionality for WoE bucketing of continuous and discrete variables
    :param self.bins: DataFrame WoE transformed variable and all related statistics
    :param self.iv: Information Value of the transformed variable
    """

    def __init__(
        self,
        qnt_num=16,
        min_block_size=16,
        spec_values=None,
        v_type="c",
        bins=None,
        t_type="b",
    ):
        """
        :param qnt_num: Number of buckets (quartiles) for continuous variable split
        :param min_block_size: minimum number of observation in each bucket (continuous variables)
        :param spec_values: List or Dictionary {'label': value} of special values (frequent items etc.)
        :param v_type: 'c' for continuous variable, 'd' - for discrete
        :param bins: Predefined bucket borders for continuous variable split
        :t_type : Binary 'b' or continous 'c' target variable
        :return: initialized class
        """
        self.__qnt_num = qnt_num  # Num of buckets/quartiles
        self._predefined_bins = (
            None if bins is None else np.array(bins)
        )  # user bins for continuous variables
        self.type = v_type  # if 'c' variable should be continuous, if 'd' - discrete
        self._min_block_size = min_block_size  # Min num of observation in bucket
        self._gb_ratio = None  # Ratio of good and bad in the sample
        self.bins = None  # WoE Buckets (bins) and related statistics
        self.df = None  # Training sample DataFrame with initial data and assigned woe
        self.qnt_num = (
            None  # Number of quartiles used for continuous part of variable binning
        )
        self.t_type = t_type  # Type of target variable
        if (
            type(spec_values) == dict
        ):  # Parsing special values to dict for cont variables
            self.spec_values = {}
            for k, v in spec_values.items():
                if v.startswith("d_"):
                    self.spec_values[k] = v
                else:
                    self.spec_values[k] = "d_" + v
        else:
            if spec_values is None:
                self.spec_values = {}
            else:
                self.spec_values = {i: "d_" + str(i) for i in spec_values}

    def fit(self, x, y):
        """
        Fit WoE transformation
        :param x: continuous or discrete predictor
        :param y: binary target variable
        :return: WoE class
        """
        # Data quality checks
        if not isinstance(x, pd.Series) or not isinstance(y, pd.Series):
            raise TypeError("pandas.Series type expected")
        if not x.size == y.size:
            raise Exception("Y size don't match Y size")
        # Calc total good bad ratio in the sample
        t_bad = np.sum(y)
        if t_bad == 0 or t_bad == y.size:
            raise ValueError("There should be BAD and GOOD observations in the sample")
        if np.max(y) > 1 or np.min(y) < 0:
            raise ValueError("Y range should be between 0 and 1")
        # setting discrete values as special values
        if self.type == "d":
            sp_values = {i: "d_" + str(i) for i in x.unique()}
            if len(sp_values) > 100:
                raise type(
                    "DiscreteVarOverFlowError",
                    (Exception,),
                    {
                        "args": (
                            "Discrete variable with too many unique values (more than 100)",
                        )
                    },
                )
            else:
                if self.spec_values:
                    sp_values.update(self.spec_values)
                self.spec_values = sp_values
        # Make data frame for calculations
        df = pd.DataFrame({"X": x, "Y": y, "order": np.arange(x.size)})
        # Separating NaN and Special values
        df_sp_values, df_cont = self._split_sample(df)
        # # labeling data
        df_cont, c_bins = self._cont_labels(df_cont)
        df_sp_values, d_bins = self._disc_labels(df_sp_values)
        # getting continuous and discrete values together
        # self.df = df_sp_values.append(df_cont)
        # self.df = df_sp_values.append(df_cont, ignore_index=True)
        # print(df_sp_values.shape)
        # print(df_cont.shape)
        self.df = pd.concat([df_sp_values, df_cont], axis=0, ignore_index=True)

        # self.bins = d_bins.append(c_bins)
        # self.bins = d_bins.append(c_bins)
        self.bins = pd.concat([d_bins, c_bins], axis=0, ignore_index=True)

        # calculating woe and other statistics
        self._calc_stat()
        # sorting appropriately for further cutting in transform method
        self.bins.sort_values("bins", inplace=True)
        # returning to original observation order
        self.df.sort_values("order", inplace=True)
        self.df.set_index(x.index, inplace=True)
        return self

    def fit_transform(self, x, y):
        """
        Fit WoE transformation
        :param x: continuous or discrete predictor
        :param y: binary target variable
        :return: WoE transformed variable
        """
        self.fit(x, y)
        return self.df["woe"]

    def _split_sample(self, df):
        if self.type == "d":
            return df, None
        sp_values_flag = (
            df["X"].isin(self.spec_values.keys()).values | df["X"].isnull().values
        )
        df_sp_values = df[sp_values_flag].copy()
        df_cont = df[np.logical_not(sp_values_flag)].copy()
        return df_sp_values, df_cont

    def _disc_labels(self, df):
        df["labels"] = df["X"].apply(
            lambda x: self.spec_values[x]
            if x in self.spec_values.keys()
            else "d_" + str(x)
        )
        d_bins = pd.DataFrame({"bins": df["X"].unique()})
        d_bins["labels"] = d_bins["bins"].apply(
            lambda x: self.spec_values[x]
            if x in self.spec_values.keys()
            else "d_" + str(x)
        )
        return df, d_bins

    def _cont_labels(self, df):
        # check whether there is a continuous part
        if df is None:
            return None, None
        # Max buckets num calc
        self.qnt_num = (
            int(
                np.minimum(df["X"].unique().size / self._min_block_size, self.__qnt_num)
            )
            + 1
        )
        # cuts - label num for each observation, bins - quartile thresholds
        bins = None
        cuts = None
        if self._predefined_bins is None:
            try:
                cuts, bins = pd.qcut(df["X"], self.qnt_num, retbins=True, labels=False)
            except ValueError as ex:
                if ex.args[0].startswith("Bin edges must be unique"):
                    ex.args = (
                        "Please reduce number of bins or encode frequent items as special values",
                    ) + ex.args
                    raise
            bins = np.append((-float("inf"),), bins[1:-1])
        else:
            bins = self._predefined_bins
            if bins[0] != float("-Inf"):
                bins = np.append((-float("inf"),), bins)
            cuts = pd.cut(
                df["X"],
                bins=np.append(bins, (float("inf"),)),
                labels=np.arange(len(bins)).astype(str),
            )
        df["labels"] = cuts.astype(str)
        c_bins = pd.DataFrame(
            {"bins": bins, "labels": np.arange(len(bins)).astype(str)}
        )
        return df, c_bins

    def _calc_stat(self):
        # calculating WoE
        stat = (
            self.df.groupby("labels")["Y"]
            .agg(mean=np.mean, bad=np.count_nonzero, obs=np.size)
            .copy()
        )
        if self.t_type != "b":
            stat["bad"] = stat["mean"] * stat["obs"]
        stat["good"] = stat["obs"] - stat["bad"]
        t_good = np.maximum(stat["good"].sum(), 0.5)
        t_bad = np.maximum(stat["bad"].sum(), 0.5)
        stat["woe"] = stat.apply(self._bucket_woe, axis=1) + np.log(t_good / t_bad)
        iv_stat = (stat["bad"] / t_bad - stat["good"] / t_good) * stat["woe"]
        self.iv = iv_stat.sum()
        # adding stat data to bins
        self.bins = pd.merge(stat, self.bins, left_index=True, right_on=["labels"])
        label_woe = self.bins[["woe", "labels"]].drop_duplicates()
        self.df = pd.merge(self.df, label_woe, left_on=["labels"], right_on=["labels"])

    def transform(self, x):
        """
        Transforms input variable according to previously fitted rule
        :param x: input variable
        :return: DataFrame with transformed with original and transformed variables
        """
        if not isinstance(x, pd.Series):
            raise TypeError("pandas.Series type expected")
        if self.bins is None:
            raise Exception("Fit the model first, please")
        df = pd.DataFrame({"X": x, "order": np.arange(x.size)})
        # splitting to discrete and continous pars
        df_sp_values, df_cont = self._split_sample(df)

        # function checks existence of special values, raises error if sp do not exist in training set
        def get_sp_label(x_):
            if x_ in self.spec_values.keys():
                return self.spec_values[x_]
            else:
                str_x = "d_" + str(x_)
                if str_x in list(self.bins["labels"]):
                    return str_x
                else:
                    raise ValueError(
                        "Value " + str_x + " does not exist in the training set"
                    )

        # assigning labels to discrete part
        df_sp_values["labels"] = df_sp_values["X"].apply(get_sp_label)
        # assigning labels to continuous part
        c_bins = self.bins[self.bins["labels"].apply(lambda z: not z.startswith("d_"))]
        if not self.type == "d":
            cuts = pd.cut(
                df_cont["X"],
                bins=np.append(c_bins["bins"], (float("inf"),)),
                labels=c_bins["labels"],
            )
            df_cont["labels"] = cuts.astype(str)
        # Joining continuous and discrete parts
        # df = df_sp_values.append(df_cont)
        # df = df_sp_values.append(df_cont)
        df = pd.concat([df_sp_values, df_cont], axis=0, ignore_index=True)

        # assigning woe
        df = pd.merge(
            df, self.bins[["woe", "labels"]], left_on=["labels"], right_on=["labels"]
        )
        # returning to original observation order
        df.sort_values("order", inplace=True)
        return df.set_index(x.index)

    def merge(self, label1, label2=None):
        """
        Merge of buckets with given labels
        In case of discrete variable, both labels should be provided. As the result labels will be marget to one bucket.
        In case of continous variable, only label1 should be provided. It will be merged with the next label.
        :param label1: first label to merge
        :param label2: second label to merge
        :return:
        """
        spec_values = self.spec_values.copy()
        c_bins = self.bins[
            self.bins["labels"].apply(lambda x: not x.startswith("d_"))
        ].copy()
        if label2 is None and not label1.startswith(
            "d_"
        ):  # removing bucket for continuous variable
            c_bins = c_bins[c_bins["labels"] != label1]
        else:
            if not (label1.startswith("d_") and label2.startswith("d_")):
                raise Exception("Labels should be discrete simultaneously")
            bin1 = self.bins[self.bins["labels"] == label1]["bins"].iloc[0]
            bin2 = self.bins[self.bins["labels"] == label2]["bins"].iloc[0]
            spec_values[bin1] = label1 + "_" + label2
            spec_values[bin2] = label1 + "_" + label2
        new_woe = WoE(
            self.__qnt_num,
            self._min_block_size,
            spec_values,
            self.type,
            c_bins["bins"],
            self.t_type,
        )
        return new_woe.fit(self.df["X"], self.df["Y"])

    def plot(self):
        """
        Plot WoE transformation and default rates
        :return: plotting object
        """
        index = np.arange(self.bins.shape[0])
        bar_width = 0.8
        figsize = (6, 6)
        woe_fig = plt.figure(figsize=figsize)
        plt.title("Number of Observations and WoE per bucket")
        ax = woe_fig.add_subplot(111)
        ax.set_ylabel("Observations")
        plt.xticks(index + bar_width / 2, self.bins["labels"])
        plt.bar(index, self.bins["obs"], bar_width, color="b", label="Observations")
        ax2 = ax.twinx()
        ax2.set_ylabel("Weight of Evidence")
        ax2.plot(
            index + bar_width / 2,
            self.bins["woe"],
            "bo-",
            linewidth=4.0,
            color="r",
            label="WoE",
        )
        handles1, labels1 = ax.get_legend_handles_labels()
        handles2, labels2 = ax2.get_legend_handles_labels()
        handles = handles1 + handles2
        labels = labels1 + labels2
        plt.legend(handles, labels)
        woe_fig.autofmt_xdate()
        return woe_fig

    def optimize(self, criterion=None, fix_depth=None, max_depth=None, cv=3):
        """
        WoE bucketing optimization (continuous variables only)
        :param criterion: binary tree split criteria
        :param fix_depth: use tree of a fixed depth (2^fix_depth buckets)
        :param max_depth: maximum tree depth for a optimum cross-validation search
        :param cv: number of cv buckets
        :return: WoE class with optimized continuous variable split
        """
        if self.t_type == "b":
            tree_type = tree.DecisionTreeClassifier
        else:
            tree_type = tree.DecisionTreeRegressor
        m_depth = int(np.log2(self.__qnt_num)) + 1 if max_depth is None else max_depth
        cont = self.df["labels"].apply(lambda z: not z.startswith("d_"))
        x_train = np.array(self.df[cont]["X"])
        y_train = np.array(self.df[cont]["Y"])
        x_train = x_train.reshape(x_train.shape[0], 1)
        start = 1
        cv_scores = []
        if fix_depth is None:
            for i in range(start, m_depth):
                if criterion is None:
                    d_tree = tree_type(max_depth=i)
                else:
                    d_tree = tree_type(criterion=criterion, max_depth=i)
                scores = cross_val_score(d_tree, x_train, y_train, cv=cv)
                cv_scores.append(scores.mean())
            best = np.argmax(cv_scores) + start
        else:
            best = fix_depth
        final_tree = tree_type(max_depth=best)
        final_tree.fit(x_train, y_train)
        opt_bins = final_tree.tree_.threshold[final_tree.tree_.threshold > 0]
        opt_bins = np.sort(opt_bins)
        new_woe = WoE(
            self.__qnt_num,
            self._min_block_size,
            self.spec_values,
            self.type,
            opt_bins,
            self.t_type,
        )
        return new_woe.fit(self.df["X"], self.df["Y"])

    @staticmethod
    def _bucket_woe(x):
        t_bad = x["bad"]
        t_good = x["good"]
        t_bad = 0.5 if t_bad == 0 else t_bad
        t_good = 0.5 if t_good == 0 else t_good
        return np.log(t_bad / t_good)


""" 測試上面這個class
# Examples
if __name__ == "__main__":
    # Set target type: 'b' for default/non-default, 'c' for continous pd values
    t_type_ = "c"
    # Set sample size
    N = 300
    # Random variables
    x1 = np.random.rand(N)
    x2 = np.random.rand(N)
    if t_type_ == "b":
        y_ = np.where(
            np.random.rand(
                N,
            )
            + x1
            + x2
            > 2,
            1,
            0,
        )
    else:
        y_ = np.random.rand(N) + x1 + x2
        y_ = (y_ - np.min(y_)) / (np.max(y_) - np.min(y_)) / 2
    # Inserting special values
    x1[0:20] = float("nan")
    x1[30:50] = float(0)
    x1[60:80] = float(1)
    x2[0:20] = float("nan")
    # Initialize WoE object
    woe_def = WoE()
    woe = WoE(7, 30, spec_values={0: "0", 1: "1"}, v_type="c", t_type=t_type_)
    # Transform x1
    woe.fit(pd.Series(x1), pd.Series(y_))
    # Transform x2 using x1 transformation rules
    woe.transform(pd.Series(x2))
    # Optimize x1 transformation using tree with maximal depth = 5 (optimal depth is chosen by cross-validation)
    woe2 = woe.optimize(max_depth=5)
    # Merge discrete buckets
    woe3 = woe.merge("d_0", "d_1")
    # Merge 2 and 3 continuous buckets
    woe4 = woe3.merge("2")
    # Print Statistics
    print(woe.bins)
    # print(woe2.bins)
    # print(woe3.bins)
    print(woe4.bins)
    # Plot and show WoE graph
    woe.plot()
    show()
    woe2.plot()
    show()
"""


auto = pd.read_csv("data/auto_ins.csv", encoding="gbk")

auto.Loss = auto.Loss.map(lambda x: 1 if x > 0 else 0)

bins = [21, 26, 31, 36, 41, 46, 51, 56, 61, 67]
labels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
auto["age_group"] = pd.cut(auto.Age, bins, labels=labels, right=False)

log_tab = pd.crosstab(auto.age_group, auto.Loss)
log_tab

log_tab[["p0", "p1"]] = log_tab[[0, 1]].apply(lambda x: x / sum(x))
log_tab["log"] = log_tab[["p1", "p0"]].apply(lambda x: np.log(x[0] / x[-1]), axis=1)
log_tab

log_tab.log.plot()

woe = WoE(v_type="d")
woe.fit(auto.age_group, auto.Loss)
woe.plot()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
import sqlite3

print("------------------------------------------------------------")  # 60個

# 数据整合和数据清洗

# SQL语句介绍

sale = pd.read_csv("data/sale.csv", encoding="gbk")
cc = sale.head()
print(cc)

# SQL数据过滤与排序
# 选择表中指定列

con = sqlite3.connect(":memory:")  # 数据库连接
sale.to_sql("sale", con)  # 将DataFrame注册成可用sql查询的表
newTable = pd.read_sql_query(
    "select year, market, sale, profit from sale", con
)  # 也可使用read_sql
cc = newTable.head()
print(cc)

# 选择表中所有列

sqlResult = pd.read_sql_query("select * from sale", con)
cc = sqlResult.head()
print(cc)

# 删除重复的行

pd.read_sql_query("select DISTINCT  year from sale", con)

# 选择满足条件的行

pd.read_sql_query("select * from sale where year=2012 and market='东'", con)

# 对行进行排序

sql = """select year, market, sale, profit
      from sale
      order by year"""
pd.read_sql_query(sql, con)


# 4.2纵向连接表

# sql操作

one = pd.read_csv("data/One.csv")
one.to_sql("One", con, index=False)
print(one.T)

two = pd.read_csv("data/Two.csv")
two.to_sql("Two", con, index=False)
print(two.T)

# union 和 union all

union = pd.read_sql("select * from one UNION select * from two", con)
union_all = pd.read_sql("select * from one UNION ALL select * from two", con)
print(union.T)

print(union_all.T)

# except 和 intersect

exceptTable = pd.read_sql("select * from one EXCEPT select * from two", con)
intersectTable = pd.read_sql("select * from one INTERSECT select * from two", con)
print(exceptTable.T)

print(intersectTable.T)

# *练习： 多表纵向连接

# DataFrame操作

cc = pd.concat([one, two], axis=0, join="outer", ignore_index=True)  # 更多参数可查看文档或帮助
print(cc)

# 4.3 横向连接表

# sql操作

table1 = pd.read_csv("data/Table1.csv")
table1.to_sql("table1", con, index=False)
cc = table1.head()
print(cc)

table2 = pd.read_csv("data/Table2.csv")
table2.to_sql("table2", con, index=False)
cc = table2.head()
print(cc)

# 笛卡尔积

pd.read_sql("select * from table1, table2", con)

# 内连接（使用inner join或使用where子句）

pd.read_sql("select * from table1 as a inner join table2 as b on a.id=b.id", con)
# pd.read_sql("select * from table1 as a, table2 as b where a.id=b.id", con)

# 左连接

pd.read_sql("select * from table1 as a left join table2 as b on a.id=b.id", con)

# DataFrame操作

pd.merge(table1, table2, on="id", how="left")  # 参数设置可查看帮助

# 按索引连接

table1.join(table2, how="outer", lsuffix="t1", rsuffix="t2")  # 参数设置可查看帮助

# 4.4 数据清洗

# 发现数据问题类型

camp = pd.read_csv("data/teleco_camp_orig.csv")
cc = camp.head()
print(cc)

# 脏数据或数据不正确

plt.hist(camp["AvgIncome"], bins=20)
# Try this: accepts['purch_price'].plot(kind='hist')
# And this: sns.histplot(accepts['purch_price'], kde=True, fit=stats.norm)
# should scipy.stats first
show()

# 这里的0值应该是缺失值
camp["AvgIncome"] = camp["AvgIncome"].replace({0: np.NaN})
# 像这种外部获取的数据要比较小心，经常出现意义不清晰或这错误值。AvgHomeValue也有这种情况
camp["AvgHomeValue"] = camp["AvgHomeValue"].replace({0: np.NaN})
camp["Age"] = camp["Age"].replace({0: np.NaN})
cc = camp.head(8)
print(cc)

cc = camp["AvgIncome"].describe(include="all")
print(cc)

# 数据不一致- 这个问题需要详细的结合描述统计进行变量说明核对

# 数据重复

cc = camp["dup"] = camp.duplicated()  # 生成重复标识变量
print(cc)

cc = camp.dup.head()
print(cc)

# 本数据没有重复记录，此处只是示例
camp_dup = camp[camp["dup"] == True]  # 把有重复的数据保存出来，以备核查
camp_nodup = camp[camp["dup"] == False]  # 注意与camp.drop_duplicates()的区别
cc = camp_nodup.head()
print(cc)

cc = camp["dup1"] = camp["ID"].duplicated()  # 按照主键进行重复记录标识
print(cc)

# accepts['fico_score'].duplicated() # 没有实际意义

# 缺失值处理

cc = camp.describe()
print(cc)
# 如果count数量少于样本量，说明存在缺失
# 缺失最多的两个变量是Age和AvgIncome,缺失了大概20%。

vmean = camp["Age"].mean(axis=0, skipna=True)
camp["Age_empflag"] = camp["Age"].isnull()
camp["Age"] = camp["Age"].fillna(vmean)
camp["Age"].describe()

vmean = camp["AvgHomeValue"].mean(axis=0, skipna=True)
camp["AvgHomeValue_empflag"] = camp["AvgHomeValue"].isnull()
camp["AvgHomeValue"] = camp["AvgHomeValue"].fillna(vmean)
camp["AvgHomeValue"].describe()

vmean = camp["AvgIncome"].mean(axis=0, skipna=True)
camp["AvgIncome_empflag"] = camp["AvgIncome"].isnull()
camp["AvgIncome"] = camp["AvgIncome"].fillna(vmean)
camp["AvgIncome"].describe()

"""
其他有缺失变量请自行填补，找到一个有缺失的分类变量，使用众数进行填补
多重插补：sklearn.preprocessing.Imputer仅可用于填补均值、中位数、众数，多重插补可考虑使用Orange、impute、Theano等包
多重插补的处理有两个要点：1、被解释变量有缺失值的观测不能填补，只能删除；2、只对放入模型的解释变量进行插补。

噪声值处理

盖帽法
"""


def blk(floor, root):  # 'blk' will return a function
    def f(x):
        if x < floor:
            x = floor
        elif x > root:
            x = root
        return x

    return f


q1 = camp["Age"].quantile(0.01)  # 计算百分位数
q99 = camp["Age"].quantile(0.99)
blk_tot = blk(floor=q1, root=q99)  # 'blk_tot' is a function
camp["Age"] = camp["Age"].map(blk_tot)
cc = camp["Age"].describe()
print(cc)

# 分箱（等深，等宽）
# 分箱法——等宽分箱

camp["Age_group1"] = pd.qcut(camp["Age"], 4)  # 这里以age_oldest_tr字段等宽分为4段
cc = camp.Age_group1.head()
print(cc)

# 分箱法——等深分箱

camp["Age_group2"] = pd.cut(camp["Age"], 4)  # 这里以age_oldest_tr字段等宽分为4段
cc = camp.Age_group2.head()
print(cc)

# df存檔 camp.to_csv("tmp_tele_camp_ok.csv")

print("------------------------------------------------------------")  # 60個
# Pandas
print("------------------------------------------------------------")  # 60個

# # 第5章 数据整合和数据清洗
# pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

# 数据整合

# 5.1.1 行列操作

# 1. 单列

sample = pd.DataFrame(np.random.randn(4, 5), columns=["a", "b", "c", "d", "e"])
sample

sample["a"]

sample.loc[:, "a"]

sample[["a"]]

# 2. 选择多行和多列
sample.iloc[0:2, 0:2]

# 3. 创建、删除列
sample["new_col1"] = sample["a"] - sample["b"]
sample

sample_new = sample.assign(
    new_col2=sample["a"] - sample["b"], new_col3=sample["a"] + sample["b"]
)
sample_new

sample.drop("a", axis=1)

# 条件查询

sample = pd.DataFrame(
    {
        "name": ["Bob", "Lindy", "Mark", "Miki", "Sully", "Rose"],
        "score": [98, 78, 87, 77, 65, 67],
        "group": [1, 1, 1, 2, 1, 2],
    }
)
sample

# 单条件

# sample.score > 70
sample[sample.score > 70]

# 多条件

sample[(sample.score > 70) & (sample.group == 1)]


# 3. 使用query

# sample.query('score > 90')
sample.query("(group ==2) |(group == 1)")

# 4. 其他

# NG
# sample[sample["score"].between(70, 80, inclusive=True)]

sample[sample["name"].isin(["Bob", "Lindy"])]

sample[sample["name"].str.contains("[M]+")]

# 横向连接

df1 = pd.DataFrame({"id": [1, 2, 3], "col1": ["a", "b", "c"]})
df2 = pd.DataFrame({"id": [4, 3], "col2": ["d", "e"]})

# 1. 内连接

df1.merge(df2, how="inner", left_on="id", right_on="id")

# 2. 外连接

df1.merge(df2, how="left", on="id")

# 3. 行索引连接

df1 = pd.DataFrame({"id1": [1, 2, 3], "col1": ["a", "b", "c"]}, index=[1, 2, 3])
df2 = pd.DataFrame({"id2": [1, 2, 3], "col2": ["aa", "bb", "cc"]}, index=[1, 3, 2])

pd.concat([df1, df2], axis=1)
# df1.join(df2)

# 纵向合并

df1 = pd.DataFrame(
    {"id": [1, 1, 1, 2, 3, 4, 6], "col": ["a", "a", "b", "c", "v", "e", "q"]}
)
df2 = pd.DataFrame({"id": [1, 2, 3, 3, 5], "col": ["x", "y", "z", "v", "w"]})

pd.concat([df1, df2], ignore_index=True, axis=0)

pd.concat([df1, df2], ignore_index=True).drop_duplicates()

df3 = df1.rename(columns={"col": "new_col"})

pd.concat([df1, df3], ignore_index=True).drop_duplicates()

# 排序

# 1. 排序

sample = pd.DataFrame(
    {
        "name": ["Bob", "Lindy", "Mark", "Miki", "Sully", "Rose"],
        "score": [98, 78, 87, 77, 77, np.nan],
        "group": [1, 1, 1, 2, 1, 2],
    }
)

sample

sample.sort_values("score", ascending=False, na_position="last")

sample.sort_values(["group", "score"])

# 分组汇总

sample = pd.read_csv("data/sample.csv", encoding="gbk")
sample.head()

sample.groupby("class")[["math"]].max()

sample.groupby(["grade", "class"])[["math"]].mean()

# NG sample.groupby(["grade"])["math", "chinese"].mean()

sample.groupby("class")["math"].agg(["mean", "min", "max"])

# NG df = sample.groupby(["grade", "class"])["math", "chinese"].agg(["min", "max"])
# df

# 拆分、堆叠列

table = pd.DataFrame(
    {
        "cust_id": [10001, 10001, 10002, 10002, 10003],
        "type": ["Normal", "Special_offer", "Normal", "Special_offer", "Special_offer"],
        "Monetary": [3608, 420, 1894, 3503, 4567],
    }
)

pd.pivot_table(table, index="cust_id", columns="type", values="Monetary")

pd.pivot_table(
    table,
    index="cust_id",
    columns="type",
    values="Monetary",
    fill_value=0,
    aggfunc="sum",
)

table1 = pd.pivot_table(
    table,
    index="cust_id",
    columns="type",
    values="Monetary",
    fill_value=0,
    aggfunc=np.sum,
).reset_index()
table1

pd.melt(
    table1,
    id_vars="cust_id",
    value_vars=["Normal", "Special_offer"],
    value_name="Monetary",
    var_name="TYPE",
)

# 赋值与条件赋值

# 1. 赋值

sample = pd.DataFrame(
    {
        "name": ["Bob", "Lindy", "Mark", "Miki", "Sully", "Rose"],
        "score": [99, 78, 999, 77, 77, np.nan],
        "group": [1, 1, 1, 2, 1, 2],
    }
)

sample.score.replace(999, np.nan)

sample.replace({"score": {999: np.nan}, "name": {"Bob": np.nan}})

# 2. 条件赋值


def transform(row):
    if row["group"] == 1:
        return "class1"
    elif row["group"] == 2:
        return "class2"


sample.apply(transform, axis=1)

sample.assign(class_n=sample.apply(transform, axis=1))

sample = sample.copy()
sample.loc[sample.group == 1, "class_n"] = "class1"
sample.loc[sample.group == 2, "class_n"] = "class2"

print("------------------------------------------------------------")  # 60個
# SQL
print("------------------------------------------------------------")  # 60個

# # 第5章 数据整合和数据清洗

# ## 5.1 SQL语句介绍

# SQL2数据过滤与排序
# 选择表中指定列

sale = pd.read_csv("data/sale.csv", encoding="gbk")

con = sqlite3.connect(":memory:")  # 数据库连接
sale.to_sql("sale", con)  # 将DataFrame注册成可用sql查询的表
newTable = pd.read_sql_query(
    "select year, market, sale, profit from sale", con
)  # 也可使用read_sql
newTable.head()


# 选择表中所有列

sqlResult = pd.read_sql_query("select * from sale", con)
sqlResult.head()


# 删除重复的行

pd.read_sql_query("select DISTINCT  year from sale", con)

# 选择满足条件的行

pd.read_sql_query("select * from sale where market in ('东','西') and year=2012", con)

# 对行进行排序

sql = """select year, market, sale, profit
      from sale
      order by  sale desc"""
pd.read_sql_query(sql, con)

# ## 5.2纵向连接表
# sql操作

one = pd.read_csv("data/One.csv")
one.to_sql("One", con, index=False)
one.T

two = pd.read_csv("data/Two.csv")
two.to_sql("Two", con, index=False)
two.T

# union 和 union all

union = pd.read_sql("select * from one UNION select * from two", con)
union_all = pd.read_sql("select * from one UNION ALL select * from two", con)
union.T

union_all.T

# except 和 intersect

exceptTable = pd.read_sql("select * from one EXCEPT select * from two", con)
intersectTable = pd.read_sql("select * from one INTERSECT select * from two", con)
exceptTable.T

intersectTable.T

# *练习： 多表纵向连接

# DataFrame操作

pd.concat([one, two], axis=0, join="outer", ignore_index=True)  # 更多参数可查看文档或帮助

# ## 5.3 横向连接表
# sql操作

table1 = pd.read_csv("data/Table1.csv")
table1.to_sql("table1", con, index=False)
table1.head()

table2 = pd.read_csv("data/Table2.csv")
table2.to_sql("table2", con, index=False)
table2.head()

# 笛卡尔积

pd.read_sql("select * from table1, table2", con)

# 内连接（使用inner join或使用where子句）

pd.read_sql("select * from table1 as a inner join table2 as b on a.id=b.id", con)
# pd.read_sql("select * from table1 as a, table2 as b where a.id=b.id", con)

# 左连接

pd.read_sql("select * from table1 as a left join table2 as b on a.id=b.id", con)

print("------------------------------------------------------------")  # 60個
# cleaning
print("------------------------------------------------------------")  # 60個

# 数据整合和数据清洗

# 数据清洗

# 发现数据问题类型

camp = pd.read_csv("data/teleco_camp_orig.csv")
camp.head()

# 脏数据或数据不正确

plt.hist(camp["AvgIncome"], bins=20, density=True)  # 查看分布情况
camp["AvgIncome"].describe(include="all")
show()

plt.hist(camp["AvgHomeValue"], bins=20, density=True)  # 查看分布情况
camp["AvgHomeValue"].describe(include="all")
show()

# 这里的0值应该是缺失值
camp["AvgIncome"] = camp["AvgIncome"].replace({0: np.NaN})
# 像这种外部获取的数据要比较小心，经常出现意义不清晰或这错误值。AvgHomeValue也有这种情况
plt.hist(
    camp["AvgIncome"],
    bins=20,
    density=True,
    range=(camp.AvgIncome.min(), camp.AvgIncome.max()),
)  # 由于数据中存在缺失值,需要指定绘图的值域

camp["AvgIncome"].describe(include="all")

camp["AvgHomeValue"] = camp["AvgHomeValue"].replace({0: np.NaN})

plt.hist(
    camp["AvgHomeValue"],
    bins=20,
    density=True,
    range=(camp.AvgHomeValue.min(), camp.AvgHomeValue.max()),
)  # 由于数据中存在缺失值,需要指定绘图的值域

camp["AvgHomeValue"].describe(include="all")

# 数据不一致-
# 这个问题需要详细的结合描述统计进行变量说明核对

# 数据重复

camp["dup"] = camp.duplicated()  # 生成重复标识变量
camp.dup.head()

# 本数据没有重复记录，此处只是示例
camp_dup = camp[camp["dup"] == True]  # 把有重复的数据保存出来，以备核查
camp_nodup = camp[camp["dup"] == False]  # 注意与camp.drop_duplicates()的区别
camp_nodup.head()

camp["dup1"] = camp["ID"].duplicated()  # 按照主键进行重复记录标识
# accepts['fico_score'].duplicated() # 没有实际意义

# * 缺失值处理

camp.describe()
# 如果count数量少于样本量，说明存在缺失
# 缺失最多的两个变量是Age和AvgIncome,缺失了大概20%。

vmean = camp["Age"].mean(axis=0, skipna=True)
camp["Age_empflag"] = camp["Age"].isnull()
camp["Age"] = camp["Age"].fillna(vmean)
camp["Age"].describe()

vmean = camp["AvgHomeValue"].mean(axis=0, skipna=True)
camp["AvgHomeValue_empflag"] = camp["AvgHomeValue"].isnull()
camp["AvgHomeValue"] = camp["AvgHomeValue"].fillna(vmean)
camp["AvgHomeValue"].describe()

vmean = camp["AvgIncome"].mean(axis=0, skipna=True)
camp["AvgIncome_empflag"] = camp["AvgIncome"].isnull()
camp["AvgIncome"] = camp["AvgIncome"].fillna(vmean)
camp["AvgIncome"].describe()

# 其他有缺失变量请自行填补，找到一个有缺失的分类变量，使用众数进行填补
# 多重插补：sklearn.preprocessing.Imputer仅可用于填补均值、中位数、众数，多重插补可考虑使用Orange、impute、Theano等包
# 多重插补的处理有两个要点：1、被解释变量有缺失值的观测不能填补，只能删除；2、只对放入模型的解释变量进行插补。

# 噪声值处理
# 盖帽法


def blk(floor, root):  # 'blk' will return a function
    def f(x):
        if x < floor:
            x = floor
        elif x > root:
            x = root
        return x

    return f


q1 = camp["Age"].quantile(0.01)  # 计算百分位数
q99 = camp["Age"].quantile(0.99)
blk_tot = blk(floor=q1, root=q99)  # 'blk_tot' is a function
camp["Age"] = camp["Age"].map(blk_tot)
camp["Age"].describe()

# 分箱（等深，等宽）
# 分箱法——等宽分箱

camp["Age_group1"] = pd.qcut(camp["Age"], 4)  # 这里以age_oldest_tr字段等宽分为4段
camp.Age_group1.head()

# 分箱法——等深分箱

camp["Age_group2"] = pd.cut(camp["Age"], 4)  # 这里以age_oldest_tr字段等宽分为4段
camp.Age_group2.head()

# df存檔 camp.to_csv("tmp_tele_camp_ok.csv")

print("------------------------------------------------------------")  # 60個
# reshape
print("------------------------------------------------------------")  # 60個

# # 第5章 数据整合和数据清洗
# pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

# ## 5.1　数据整合

# 行列操作

# 1. 单列

# 拆分、堆叠列

table = pd.DataFrame(
    {
        "cust_id": [10001, 10001, 10002, 10002, 10003],
        "type": ["Normal", "Special_offer", "Normal", "Special_offer", "Special_offer"],
        "Monetary": [3608, 420, 1894, 3503, 4567],
    }
)


table

result = pd.pivot_table(table, index="cust_id", columns="type", values="Monetary")

pd.pivot_table(
    table,
    index="cust_id",
    columns="type",
    values="Monetary",
    fill_value=0,
    aggfunc="sum",
)

table1 = pd.pivot_table(
    table,
    index="cust_id",
    columns="type",
    values="Monetary",
    fill_value=0,
    aggfunc=np.sum,
).reset_index()
table1

pd.melt(
    table1,
    id_vars="cust_id",
    value_vars=["Normal", "Special_offer"],
    value_name="Monetary",
    var_name="TYPE",
)

# # 第5章3 RFM
# pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

# 1. 导入数据

# 無檔案??
trad_flow = pd.read_csv("data/RFM_TRAD_FLOW.csv", encoding="gbk")
trad_flow.head(10)

# 2.计算 RFM

M = trad_flow.groupby(["cumid", "type"])[["amount"]].sum()

M_trans = pd.pivot_table(M, index="cumid", columns="type", values="amount")

F = trad_flow.groupby(["cumid", "type"])[["transID"]].count()
F.head()

F_trans = pd.pivot_table(F, index="cumid", columns="type", values="transID")
F_trans.head()

R = trad_flow.groupby(["cumid", "type"])[["time"]].max()
R.head()

# R_trans=pd.pivot_table(R,index='cumid',columns='type',values='time')
# R_trans.head()

# 3.衡量客户对打折商品的偏好

M_trans["Special_offer"] = M_trans["Special_offer"].fillna(0)

M_trans["spe_ratio"] = M_trans["Special_offer"] / (
    M_trans["Special_offer"] + M_trans["Normal"]
)
M_rank = M_trans.sort_values("spe_ratio", ascending=False, na_position="last").head()

M_rank["spe_ratio_group"] = pd.qcut(M_rank["spe_ratio"], 4)  # 这里以age_oldest_tr字段等宽分为4段
M_rank.head()

print("------------------------------------------------------------")  # 60個
# sampling
print("------------------------------------------------------------")  # 60個


def get_sample(df, sampling="simple_random", k=1, stratified_col=None):
    """
    对输入的 dataframe 进行抽样的函数

    参数:
        - df: 输入的数据框 pandas.dataframe 对象

        - sampling:抽样方法 str
            可选值有 ["simple_random", "stratified", "systematic"]
            按顺序分别为: 简单随机抽样、分层抽样、系统抽样

        - k: 抽样个数或抽样比例 int or float
            (int, 则必须大于0; float, 则必须在区间(0,1)中)
            如果 0 < k < 1 , 则 k 表示抽样对于总体的比例
            如果 k >= 1 , 则 k 表示抽样的个数；当为分层抽样时，代表每层的样本量

        - stratified_col: 需要分层的列名的列表 list
            只有在分层抽样时才生效

    返回值:
        pandas.dataframe 对象, 抽样结果
    """
    from functools import reduce

    len_df = len(df)
    if k <= 0:
        raise AssertionError("k不能为负数")
    elif k >= 1:
        assert isinstance(k, int), "选择抽样个数时, k必须为正整数"
        sample_by_n = True
        if sampling == "stratified":
            alln = (
                k * df.groupby(by=stratified_col)[stratified_col[0]].count().count()
            )  # 有问题的
            # alln=k*df[stratified_col].value_counts().count()
            if alln >= len_df:
                raise AssertionError("请确认k乘以层数不能超过总样本量")
    else:
        sample_by_n = False
        if sampling in ("simple_random", "systematic"):
            k = math.ceil(len_df * k)

    # print(k)

    if sampling == "simple_random":
        print("使用简单随机抽样")
        idx = random.sample(range(len_df), k)
        res_df = df.iloc[idx, :].copy()
        return res_df

    elif sampling == "systematic":
        print("使用系统抽样")
        step = len_df // k + 1  # step=len_df//k-1
        start = 0  # start=0
        idx = range(len_df)[start::step]  # idx=range(len_df+1)[start::step]
        res_df = df.iloc[idx, :].copy()
        # print("k=%d,step=%d,idx=%d"%(k,step,len(idx)))
        return res_df

    elif sampling == "stratified":
        assert stratified_col is not None, "请传入包含需要分层的列名的列表"
        assert all(np.in1d(stratified_col, df.columns)), "请检查输入的列名"

        grouped = df.groupby(by=stratified_col)[stratified_col[0]].count()
        if sample_by_n == True:
            group_k = grouped.map(lambda x: k)
        else:
            group_k = grouped.map(lambda x: math.ceil(x * k))

        res_df = pd.DataFrame(columns=df.columns)
        for df_idx in group_k.index:
            df1 = df
            if len(stratified_col) == 1:
                df1 = df1[df1[stratified_col[0]] == df_idx]
            else:
                for i in range(len(df_idx)):
                    df1 = df1[df1[stratified_col[i]] == df_idx[i]]
            idx = random.sample(range(len(df1)), group_k[df_idx])
            group_df = df1.iloc[idx, :].copy()
            res_df = pd.concat([res_df, group_df], axis=0, ignore_index=True)
        return res_df

    else:
        raise AssertionError("sampling is illegal")


clients = pd.read_csv("data/clients.csv", encoding="gbk")
# clients["district_id_c"]=clients["district_id"].map(lambda x:"id"+str(x))

# 在每个地区分别用简单随机抽样、分层抽样、系统抽样，三种方式抽取样本

# 简单随机抽样
# 简单随机抽样-按数量取
srn = get_sample(clients, sampling="simple_random", k=22, stratified_col=None)
# 简单随机抽样-按百分比取
srp = get_sample(clients, sampling="simple_random", k=0.1, stratified_col=None)

# 分层抽样
# 分层抽样-按每层数量取
strn = get_sample(clients, sampling="stratified", k=2, stratified_col=["district_id"])
# 分层抽样-按每层百分比取
strp = get_sample(clients, sampling="stratified", k=0.1, stratified_col=["district_id"])

# 系统抽样
# 系统抽样-按数量取
sysn = get_sample(clients, sampling="systematic", k=4, stratified_col=None)
# 系统抽样-按百分比取
sysp = get_sample(clients, sampling="systematic", k=0.1, stratified_col=None)

print("------------------------------------------------------------")  # 60個
# RFM2
print("------------------------------------------------------------")  # 60個

# # 第5章3 RFM
# pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

trad_flow = pd.read_csv("data/RFM_TRAD_FLOW.csv", encoding="gbk")
trad_flow.head()

# 2.计算 RFM

# 先将非标准字符串时间格式化为时间数组，再转换为时间戳便于计算
trad_flow["time"] = trad_flow["time"].map(
    lambda x: time.mktime(time.strptime(x, "%d%b%y:%H:%M:%S"))
)

# 查找每个购物ID每个销售类型下的最近时间
R = trad_flow.groupby(["cumid", "type"])[["time"]].max()

# 转化为透视表
R_trans = pd.pivot_table(R, index="cumid", columns="type", values="time")

# 用最久远的购物时间替换缺失值
R_trans[["Special_offer", "returned_goods"]] = R_trans[
    ["Special_offer", "returned_goods"]
].apply(lambda x: x.replace(np.nan, min(x)), axis=0)
R_trans["R_max"] = R_trans[["Normal", "Presented", "Special_offer"]].apply(
    lambda x: max(x), axis=1
)

R_trans.head()

# 对购物频率按照购物ID和购物类型进行汇总统计
F = trad_flow.groupby(["cumid", "type"])[["transID"]].count()

# 转化为透视表
F_trans = pd.pivot_table(F, index="cumid", columns="type", values="transID")

# 用0填补缺失值
F_trans[["Special_offer", "returned_goods"]] = F_trans[
    ["Special_offer", "returned_goods"]
].fillna(0)

# 将退货的频数转化为负数
F_trans["returned_goods"] = F_trans["returned_goods"].map(lambda x: -x)

# 求每个购物ID的购物总次数
F_trans["F_total"] = F_trans.apply(lambda x: sum(x), axis=1)

F_trans.head()

# 对购物金额按照购物ID和购物类型进行汇总统计
M = trad_flow.groupby(["cumid", "type"])[["amount"]].sum()

# 转化为透视表
M_trans = pd.pivot_table(M, index="cumid", columns="type", values="amount")

# 用0填补缺失值
M_trans[["Special_offer", "returned_goods"]] = M_trans[
    ["Special_offer", "returned_goods"]
].fillna(0)

# 求每个购物ID的购物总金额
M_trans["M_total"] = M_trans.apply(lambda x: sum(x), axis=1)

M_trans.head()

# 合并表
RFM = pd.concat([R_trans["R_max"], F_trans["F_total"], M_trans["M_total"]], axis=1)
# RFM三个维度等宽分箱打分
RFM["R_score"] = pd.cut(RFM.R_max, 3, labels=[1, 2, 3], precision=2)
RFM["F_score"] = pd.cut(RFM.F_total, 3, labels=[1, 2, 3], precision=2)
RFM["M_score"] = pd.cut(RFM.M_total, 3, labels=[1, 2, 3], precision=2)

print("依據 R_score F_score M_score 三欄位, 建立 Label 欄位")


# RFM各三类，总共有27种组合，为方便营销简化分类为8种
def score_label(a, b, c):
    """
    a: 'R_score'
    b: 'F_score'
    c: 'M_score'
    """
    if a == 3 and b == 3 and c == 3:
        return "重要价值客户"
    elif a == 3 and (b in [1, 2]) and c == 3:
        return "重要发展客户"
    elif (a in [1, 2]) and b == 3 and c == 3:
        return "重要保持客户"
    elif (a in [1, 2]) and (b in [1, 2]) and c == 3:
        return "重要挽留客户"
    elif a == 3 and b == 3 and (c in [1, 2]):
        return "一般价值客户"
    elif a == 3 and (b in [1, 2]) and (c in [1, 2]):
        return "一般发展客户"
    elif (a in [1, 2]) and b == 3 and (c in [1, 2]):
        return "一般保持客户"
    elif (a in [1, 2]) and (b in [1, 2]) and (c in [1, 2]):
        return "一般挽留客户"


cc = RFM.head()
print("貼標籤前 :\n", cc, sep="")

# 为每个购物ID贴标签
RFM["Label"] = RFM[["R_score", "F_score", "M_score"]].apply(
    lambda x: score_label(x[0], x[1], x[2]), axis=1
)

cc = RFM.head()
print("貼標籤後 :\n", cc, sep="")

# '重要价值客户'：消费额度高，购物频率高，最近购物时间也较近——该类客户是重要且忠实的大客户，要细心维护。
# '重要发展客户'：消费额度高，购物频率不高，最近购物时间较近——该类客户只是购物频率不高，有巨大的挖掘潜力，可根据该客户以往购物信息，进行个性
#                 化推荐，并发放购物优惠券刺激消费，增加客户粘性。
# '重要保持客户'：消费额度高，购物频率高，但最近购物时间较远——该类客户最近一次购物时间较久远，可能是快要流失的重要客户，可以让客户沟通了解其
#                 是不是哪项环节不够人性化体验不好，导致购物频率过低。
# '重要挽留客户'：消费额度高，购物频率不高，最近购物时间也较远——该类客户可能是已经流失的重要客户，如果还能联系上，可跟进了解其流失原因，对有
#                 相似客户特征的群体进行预警，针对性改进。
# '一般价值客户'：消费额度不高，购物频率高，最近购物时间也较近——该类客户对我们的产品感兴趣，很活跃，但购物金额过低，可能是价格敏感性客户，可
#                 对其组合金融产品增加其购买力。
# '一般发展客户'：消费额度不高，购物频率不高，最近购物时间较近——该类客户可能是我们的新晋客户，对我们的服务和产品进行试探性体验，可多留意此类
#                 客户，进行邮件短信关怀及时发送优惠信息。
# '一般保持客户'：消费额度不高，购物频率高，最近购物时间较远——该类客户可能是快要流失的一般客户，可进行一般性低成本营销。
# '一般挽留客户'：消费额度不高，购物频率不高，最近购物时间也较远——该类客户不是我们的目标客户，经费有限可忽略此类客户。

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

# 导入数据

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

# chapter6_creditcard_exp.py

# # 第6讲 统计推断基础
# 数据说明：本数据是地区房价增长率数据
# 名称-中文含义
# dis_name-小区名称
# rate-房价同比增长率

house_price_gr = pd.read_csv(r"data/house_price_gr.csv", encoding="gbk")
house_price_gr.head()

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
# 导入数据
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


# chapter6_tele_camp_ok.py

# # 第6讲 统计推断基础
# 数据说明：本数据是地区房价增长率数据
# 名称-中文含义
# dis_name-小区名称
# rate-房价同比增长率

house_price_gr = pd.read_csv(r"data/house_price_gr.csv", encoding="gbk")
house_price_gr.head()

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

# 导入数据
camp = pd.read_csv(r"data/tele_camp_ok.csv", skipinitialspace=True)
camp.head()

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
"""
主成分分析

某金融服务公司为了了解贷款客户的信用程度，评价客户的信用等级，采用信用评级常用的5C方法，说明客户违约的可能性。

    品格：指客户的名誉；
    能力：指客户的偿还能力；
    资本：指客户的财务势力和财务状况；
    担保：指对申请贷款项担保的覆盖程度；
    环境：指外部经济、政策环境对客户的影响。
    每个单项都是由专家打分给出的。
"""

loan = pd.read_csv("data/Loan_aply.csv")
cc = loan.head()
print(cc)

# plt.figure(figsize=(2, 2))
plt.scatter(loan["X1"], loan["X2"])
plt.title("Scatter")

show()


sns.pairplot(loan.loc[:, "X1":])
show()

# 计算相关系数矩阵

cc = loan.loc[:, "X1":].corr(method="pearson")
print(cc)

# 初次查看主成分的解释方差占比

from sklearn.decomposition import PCA

pca = PCA()
pca.fit(loan.loc[:, "X1":])

print(pca.explained_variance_ratio_)

# [ 0.84585431  0.08914623  0.04259067  0.01663007  0.00577872]

print(pca.components_)

"""
[[ 0.46881402  0.48487556  0.47274449  0.46174663  0.32925948]
 [ 0.83061232 -0.32991571  0.02117417 -0.43090441 -0.12293025]
 [ 0.0214065   0.0148012  -0.4127194  -0.24084475  0.87805421]
 [ 0.25465387 -0.28771993 -0.58858207  0.70628304 -0.0842856 ]
 [ 0.15808149  0.75700032 -0.50921327 -0.2104032  -0.31367674]]
"""

pca1 = PCA(n_components=1, whiten=True)
pca1.fit(loan.loc[:, "X1":])

"""
PCA(copy=True, iterated_power='auto', n_components=1, random_state=None,
  svd_solver='auto', tol=0.0, whiten=True)
"""
# 将打分结果和原始数据联结

score = pd.DataFrame(
    pca1.transform(loan.loc[:, "X1":]),
    columns=[
        "score",
    ],
)
loan.join(score).sort_values(by="score", ascending=False)

print(pca1.components_)

# 数据标准化的方法 http://www.cnblogs.com/chaosimple/p/4153167.html

# 因子分析
"""
    cities_10记录了十个沿海省份的经济指标

变量 	含义
X1 	GDP
X2 	人均GDP
X3 	工业增加值
X4 	第三产业增加值
X5 	固定资产投资
X6 	基本建设投资
X7 	社会消费品零售总额
X8 	海关出口总额
X9 	地方财政收入
"""

cities = pd.read_csv("data/cities_10.csv", encoding="gbk")
print(cities)

cc = cities.loc[:, "X1":].corr(method="pearson").head()
print(cc)

from sklearn.preprocessing import scale

scale_cities = scale(cities.loc[:, "X1":])
pca_c = PCA(n_components=3, whiten=True).fit(scale_cities)
pca_c.explained_variance_ratio_

# array([ 0.80112955,  0.12214932,  0.0607924 ])

pca_c1 = PCA(n_components=2, whiten=True).fit(scale_cities)
pd.DataFrame(pca_c1.components_)

# sklearn中的因子分析是极大似然法,不推荐使用

from sklearn.decomposition import FactorAnalysis

fa = FactorAnalysis(n_components=2).fit(scale_cities)
pd.DataFrame(fa.components_)


cities_scores = pd.DataFrame(fa.transform(scale_cities), columns=["total", "avg"])
cities[["AREA"]].join(cities_scores)

# 对通信消费数据profile_telecom进行因子分析

profile = pd.read_csv("data/profile_telecom.csv")
cc = profile.head()
print(cc)

data = profile.loc[:, "cnt_call":]
cc = data.corr(method="pearson")
print(cc)

# 对数据进行标准化

from sklearn.preprocessing import scale

data_scaled = scale(data)

telecom_pca = PCA(n_components=2, whiten=True).fit(data_scaled)
telecom_pca.explained_variance_ratio_


telecom_pca.components_


telecom_pca.transform(data_scaled)


telecom_fa = FactorAnalysis(n_components=2).fit(data_scaled)
cc = pd.DataFrame(fa.components_).T
print(cc)

# 奇异值分解

A = np.matrix(
    [[5, 5, 0, 5], [5, 0, 3, 4], [3, 4, 0, 3], [0, 0, 5, 3], [5, 4, 4, 5], [5, 4, 5, 5]]
)

U, s, VH = np.linalg.svd(A)
print(U.shape, s.shape, VH.shape)

# (6, 6) (4,) (4, 4)

# plt.figure(figsize=[3, 2])
plt.plot(s)
show()

S = np.diag(s[:2])
UU = U[:, :2]

bob_T = np.matrix([5, 5, 0, 0, 0, 5])

bob_T.dot(UU).dot(np.linalg.inv(S))

# matrix([[-0.37752201,  0.08020351]])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# MDS

# 使用美国各大城市距离数据CITY_DISTANCE

df = pd.read_csv("data/CITY_DISTANCE.csv", skipinitialspace=True)
print(df)

df_filled = df.fillna(0)
distance_array = np.array(df_filled.iloc[:, 1:])
cities = distance_array + distance_array.T
# pd.DataFrame(cities)

# 建模

from sklearn.manifold import MDS

mds = MDS(n_components=2, dissimilarity="precomputed", random_state=123)
mds.fit_transform(cities)
mds.stress_

# 350.0770309073701

mds.embedding_


# 绘制感知图

x = mds.embedding_[:, 0]
y = mds.embedding_[:, 1]
plt.scatter(x, y)
for a, b, s in zip(x, y, df["City"]):
    plt.text(a, b, s, fontsize=12)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
X1 品格：指客户的名誉；
X2 能力：指客户的偿还能力；
X3 资本：指客户的财务实力和财务状况；
X4 担保：指对申请贷款项担保的覆盖程度；
X5 环境：指外部经济、政策环境对客户的影响
"""
# 一、主成分分析

# 引入数据

model_data = pd.read_csv("data/Loan_aply.csv", encoding="gbk")
model_data.head()

data = model_data.loc[:, "X1":]
data.head()

# 查看相关系数矩阵，判定做变量降维的必要性（非必须）

corr_matrix = data.corr(method="pearson")

# 做主成分之前，进行中心标准化

from sklearn import preprocessing

data = preprocessing.scale(data)
# 使用sklearn的主成分分析，用于判断保留主成分的数量

from sklearn.decomposition import PCA

"""说明：1、第一次的n_components参数应该设的大一点
   说明：2、观察explained_variance_ratio_和explained_variance_的取值变化，建议explained_variance_ratio_累积大于0.85，explained_variance_需要保留的最后一个主成分大于0.8，
"""
pca = PCA(n_components=4)
pca.fit(data)
print(pca.explained_variance_)  # 建议保留1个主成分
print(pca.explained_variance_ratio_)  # 建议保留1个主成分

pca = PCA(n_components=1).fit(data)  # 综上,2个主成分
newdata = pca.fit_transform(data)
citi10_pca = model_data.join(pd.DataFrame(newdata))

# 通过主成分在每个变量上的权重的绝对值大小，确定每个主成分的代表性

pd.DataFrame(pca.components_).T

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# correspondence analysis

"""
变量 	说明 	        标签
NO 	编号 	        -
salary 	收入 	        1:[0 1000], 2:[1000 3000], 3:[3001 5000], 4:[5001 7000], 5:[7001 9000], 6:>9000
educ 	教育程度 	1:高中以下, 2:大专, 3:本科, 4:大于硕士
freq 	频次 	        1:1次, 2:2-3次, 3:4-5次, 4:6-8次, 5:9-12次, 6:>13次
compan 	购物原因 	1:家人,2:情人, 3:朋友, 4: 同学, 5:客户, 6:无聊
purpose 目的 	        1:享受, 2:陪同异性, 3:生活用品, 4:公事, 5:无聊
average 单次平均消费 	1:小于50, 2:[50 99], 3: [100,149], 4:[150 199], 5:≥200
"""

df = pd.read_csv("data/shopping.csv")
cc = df.head()
print(cc)

purpose_dict = {
    1: "enjoyment",
    2: "opposite sex",
    3: "daily use",
    4: "business",
    5: "no reason",
}
average_dict = {1: "<50", 2: "[50 99]", 3: "[100 149]", 4: "[150 199]", 5: ">200"}
df.purpose.replace(purpose_dict, inplace=True)
df.average.replace(average_dict, inplace=True)

cross_table = pd.crosstab(df.purpose, df.average)
cross_table

from numpy.linalg import svd


class CA(object):
    """Simple corresondence analysis.

    Inputs
    ------
    ct : array_like, shape (n_samples, n_features)
      Two-way contingency table, training set, where `n_samples`
      is the number of samples and `n_features` is the number of features.

    Attributes
    ------
    F_ : array, shape (n_features, K)
      principal coordinates of columns. Where `K` = min(`n_features`, `n_samples`).

    G_ : array, shape (n_samples, K)
      principal coordinates of rows. Where `K` = min(`n_features`, `n_samples`).

    explained_variance_ratio_ : array, shape(K, )
      Percentage of variance explained by each of the selected components.

    Notes
    -----
    The implementation follows that presented in 'Correspondence
    Analysis in R, with Two- and Three-dimensional Graphics: The ca
    Package,' Journal of Statistical Software, May 2007, Volume 20,
    Issue 3.
    """

    def __init__(self, cross_table):
        N = np.matrix(cross_table, dtype=float)

        # correspondence matrix from contingency table
        P = N / N.sum()

        # row and column marginal totals of P as vectors
        r = P.sum(axis=1)
        c = P.sum(axis=0).T

        # diagonal matrices of row/column sums
        D_r_rsq = np.diag(1.0 / np.sqrt(r.A1))
        D_c_rsq = np.diag(1.0 / np.sqrt(c.A1))

        # the matrix of standarized residuals
        Z = D_r_rsq * (P - r * c.T) * D_c_rsq

        # compute the SVD
        U, D_a, V = svd(Z, full_matrices=False)
        D_a = np.asmatrix(np.diag(D_a))
        V = V.T

        # principal coordinates of columns
        F = D_c_rsq * V * D_a

        # principal coordinates of rows
        G = D_r_rsq * U * D_a

        # standard coordinates of rows
        X = D_r_rsq * U

        # standard coordinates of columns
        Y = D_c_rsq * V

        eigenvals = np.diagonal(D_a) ** 2
        explained_variance_ratio = eigenvals.cumsum() / eigenvals.sum()

        # the total variance of the data matrix
        inertia = sum(
            [
                (P[i, j] - r[i, 0] * c[j, 0]) ** 2 / (r[i, 0] * c[j, 0])
                for i in range(N.shape[0])
                for j in range(N.shape[1])
            ]
        )  # equals np.power(S, 2).sum() or eigenvalus.sum() or np.trace(S.T * S)

        self.F_ = F.A
        self.G_ = G.A
        self.inertia_ = inertia
        self.eigenvals_ = eigenvals
        self.explained_variance_ratio_ = explained_variance_ratio


ca = CA(cross_table)

print(ca.explained_variance_ratio_)

# [ 0.51057984  0.92001143  0.96850523  1.          1.        ]

# R型和Q型分析的特征向量（加权后）

F = ca.F_
G = ca.G_

print(F[:, :2])

# 绘制感知图

for i, s in enumerate(cross_table.columns):
    x, y = F[i, 0], F[i, 1]
    plt.plot(x, y, "bo")
    plt.text(x, y, s, va="bottom", ha="left", color="b")

for i, s in enumerate(cross_table.index):
    x, y = G[i, 0], G[i, 1]
    plt.plot(x, y, "r^")
    plt.text(x, y, s, va="bottom", ha="left", color="r")


show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# PDA
"""
第十三讲 信息压缩

-- 第一部分 连续变量压缩

    AvgIncome 当地人均收入
    ID 员工ID
    gender 性别
    Dept 部门
    performance 绩效总分
    adaptation 适应总分
    emotion 情绪总分
"""

from sklearn.decomposition import PCA, FactorAnalysis, FastICA
from sklearn import preprocessing

model_data = pd.read_csv("data/staff_performances.csv")
cc = model_data.head()
print(cc)

data = model_data.loc[:, "performance":]
cc = data.head()
print(cc)

cc = data.describe().T
print(cc)

plt.scatter(model_data["performance"], model_data["adaptation"])
plt.title("Scatter")
show()

sns.pairplot(data)
show()

# 计算相关系数矩阵

corr_matrix = data.corr(method="pearson")
# corr_matrix = corr_matrix.abs()
print(corr_matrix)

# 初次查看主成分的解释方差占比

pca = PCA(n_components=3, whiten=True)
newData = pca.fit_transform(data)
pca.explained_variance_ratio_

pca.components_

pca = PCA(n_components=1, whiten=True)
newData = pca.fit_transform(data)
print(newData.T)

# 将打分结果和原始数据联结

score = pd.DataFrame(newData)
data_new = model_data.join(score)
cc = data_new.head()
print(cc)

# data_new.sort(0)
""" 要改
/home/quant/anaconda2/lib/python2.7/site-packages/ipykernel/__main__.py:1: FutureWarning: sort(columns=....) is deprecated, use sort_values(by=.....)
  if __name__ == '__main__':
"""
# 数据标准化的方法 http://www.cnblogs.com/chaosimple/p/4153167.html

model_data = pd.read_csv("data/cities_10.csv", encoding="gbk")
model_data.head()
data = model_data.loc[:, "X1":]
cc = data.head()
print(cc)

sns.pairplot(data)
show()

corr_matrix = data.corr(method="pearson")
# corr_matrix = corr_matrix.abs()
cc = corr_matrix
print(cc)

pca = PCA(n_components=3, whiten=True)
newData = pca.fit(data)
cc = pd.DataFrame(pca.components_).T
print(cc)

fa = FactorAnalysis(n_components=3)
newData = fa.fit(data)
cc = pd.DataFrame(fa.components_).T
print(cc)

model_data = pd.read_csv("data/profile_telecom.csv")
cc = model_data.head()
print(cc)

data = model_data.loc[:, "cnt_call":]
cc = data.head()
print(cc)

sns.pairplot(data)
show()

corr_matrix = data.corr(method="pearson")
# corr_matrix = corr_matrix.abs()
cc = corr_matrix
print(cc)

pca = PCA(n_components=3, whiten=True)
newData = pca.fit(data)
cc = pd.DataFrame(pca.components_).T
print(cc)

# 对数据进行标准化

# data_scaled = (data - np.mean(data, 0)) / (np.std(data))#归一化，因为FactorAnalysis没有white选项
data_scaled = preprocessing.scale(data + 0.0)  # 归一化，但是只能用于浮点类型变量
cc = pd.DataFrame(data_scaled).head()
print(cc)

fa = FactorAnalysis(n_components=3)
newData = fa.fit(data_scaled)
cc = pd.DataFrame(fa.components_).T
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# chapter13_2 PCA_FCA_Varselect_city10

"""
X1	GDP
X2	人均GDP
X3	工业增加值
X4	第三产业增加值
X5	固定资产投资
X6	基本建设投资
X7	社会消费品零售总额
X8	海关出口总额
X9	地方财政收入
"""
# 一、主成分分析

# 引入数据

model_data = pd.read_csv("data/cities_10.csv", encoding="gbk")
model_data.head()

data = model_data.loc[:, "X1":]
data.head()

# 查看相关系数矩阵，判定做变量降维的必要性（非必须）

corr_matrix = data.corr(method="pearson")

# 做主成分之前，进行中心标准化

from sklearn import preprocessing

data = preprocessing.scale(data)
# 使用sklearn的主成分分析，用于判断保留主成分的数量

from sklearn.decomposition import PCA

"""说明：1、第一次的n_components参数应该设的大一点
   说明：2、观察explained_variance_ratio_和explained_variance_的取值变化，建议explained_variance_ratio_累积大于0.85，explained_variance_需要保留的最后一个主成分大于0.8，
"""
pca = PCA(n_components=3)
pca.fit(data)
print(pca.explained_variance_)  # 建议保留2个主成分
print(pca.explained_variance_ratio_)  # 建议保留2个主成分

pca = PCA(n_components=2).fit(data)  # 综上,2个主成分
newdata = pca.fit_transform(data)
# 通过主成分在每个变量上的权重的绝对值大小，确定每个主成分的代表性
pd.DataFrame(pca.components_).T
# 第一个主成分在第2个变量权重低,其余均高
# 第二个主成分在第2个变量权重高,其余均低
#############################################################################################
# 二、因子分析
# 因子分析的概念很多，作为刚入门的人，我们可以认为因子分析是主成分分析的延续

# pip install fa_kit

from fa_kit import FactorAnalysis
from fa_kit import plotting as fa_plotting

fa = FactorAnalysis.load_data_samples(data, preproc_demean=True, preproc_scale=True)
fa.extract_components()

# 设定提取主成分的方式。默认为“broken_stick”方法，建议使用“top_n”法

fa.find_comps_to_retain(method="top_n", num_keep=2)
# 通过最大方差法进行因子旋转

pd.DataFrame(fa.comps["rot"])  # 查看因子权重
fa.rotate_components(method="varimax")
fa_plotting.graph_summary(fa)
# - 说明：可以通过第三张图观看每个因子在每个变量上的权重，权重越高，代表性越强

# 获取因子得分

# 到目前还没有与PCA中fit_transform类似的函数，因此只能手工计算因子
# 以下是矩阵相乘的方式计算因子：因子=原始数据（n*k）*权重矩阵(k*num_keep)
fas = pd.DataFrame(fa.comps["rot"])
data = pd.DataFrame(data)  # 注意data数据需要标准化
fa_score = pd.DataFrame(np.dot(data, fas))

# 第三步：根据因子得分进行数据分析

a = fa_score.rename(columns={0: "Gross", 1: "Avg"})
citi10_fa = model_data.join(a)

# df存檔 citi10_fa.to_csv("data/citi10_fa.csv")

x = citi10_fa["Gross"]
y = citi10_fa["Avg"]
label = citi10_fa["AREA"]
plt.scatter(x, y)
for a, b, l in zip(x, y, label):
    plt.text(a, b + 0.1, "%s." % l, ha="center", va="bottom", fontsize=14)

show()

#############################################################################################
# 三、变量筛选
# 以下是变量选择的完整函数
# 以下是变量选择的完整函数
# 基于SparsePCA的算法还不是很稳定,尤其是当数据本身保留几个变量都处于模棱两个的时候,
# 该算法并不能达到人为调整的效果。而且并不能保证每次保留的变量是一致的（原因1、SparsePCA：本身就具有随机性；2、脚本中也随机抽样的），
# 只能保证保留的变量是不相关的
# 其特点只是比较省人力，可以自动化运行


def Var_Select(orgdata, k, alphaMax=10, alphastep=0.2):
    """
    orgdata-需要信息压缩的数据框
    k-预期最大需要保留的最大变量个数，实际保留数量不能多于这个数值
    alphaMax-SparsePCA算法惩罚项的最大值,一般要到5才会取得比较理想的结果
    alphastep-SparsePCA算法惩罚项递增的步长
    """
    # step1:当数据量过大时，为了减少不必要的耗时
    if orgdata.iloc[:, 1].count() > 5000:
        data = orgdata.sample(5000)
    else:
        data = orgdata
    # step2:引入所需要的包，并且对数据进行标准化
    from sklearn import preprocessing
    from sklearn.decomposition import SparsePCA

    # from functools import reduce
    data = preprocessing.scale(data)
    n_components = k
    # pca_n = list()
    # step3:进行SparsePCA计算，选择合适的惩罚项alpha，当恰巧每个原始变量只在一个主成分上有权重时，停止循环
    for i in np.arange(0.1, alphaMax, alphastep):
        pca_model = SparsePCA(n_components=n_components, alpha=i)
        pca_model.fit(data)
        pca = pd.DataFrame(pca_model.components_).T
        n = data.shape[1] - sum(sum(np.array(pca != 0)))  ####计算系数不为0的数量
        if n == 0:
            global best_alpha
            best_alpha = i
            break
    # step4:根据上一步得到的惩罚项的取值，估计SparsePCA，并得到稀疏主成分得分
    pca_model = SparsePCA(n_components=n_components, alpha=best_alpha)
    pca_model.fit(data)
    pca = pd.DataFrame(pca_model.components_).T
    data = pd.DataFrame(data)
    score = pd.DataFrame(pca_model.fit_transform(data))
    # step6:计算原始变量与主成分之间的1-R方值
    r = []
    R_square = []
    for xk in range(data.shape[1]):  # xk输入变量个数
        for paj in range(n_components):  # paj主成分个数
            r.append(abs(np.corrcoef(data.iloc[:, xk], score.iloc[:, paj])[0, 1]))
            r_max1 = max(r)
            r.remove(r_max1)
            r.append(-2)
            r_max2 = max(r)
            R_square.append((1 - r_max1**2) / (1 - r_max2**2))

    R_square = abs(
        pd.DataFrame(np.array(R_square).reshape((data.shape[1], n_components)))
    )
    var_list = []
    # print(R_square)
    # step7:每个主成分中，选出原始变量的1-R方值最小的。
    for i in range(n_components):
        vmin = R_square[i].min()
        # print(R_square[i])
        # print(vmin)
        # print(R_square[R_square[i] == min][i])
        var_list.append(R_square[R_square[i] == vmin][i].index)

    news_ids = []
    for id in var_list:
        if id not in news_ids:
            news_ids.append(id)
    print(news_ids)
    data_vc = orgdata.iloc[:, np.array(news_ids).reshape(len(news_ids))]
    return data_vc


model_data = pd.read_csv("data/cities_10.csv", encoding="gbk")
model_data.head()
data = model_data.loc[:, "X1":]

Varseled_data = Var_Select(data, k=2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# chapter13_3 PCA_FCA_Varselect_bank

"""
CNT_TBM 柜台交易次数	
CNT_ATM ATM机交易次数
CNT_POS POS机交易次数	
CNT_CSC 有偿服务次数

"""
# 一、主成分分析

# 引入数据

model_data = pd.read_csv("data/profile_bank.csv")
data = model_data.loc[:, "CNT_TBM":"CNT_CSC"]

# 查看相关系数矩阵，判定做变量降维的必要性（非必须）

corr_matrix = data.corr(method="pearson")
# corr_matrix = data.corr(method='spearman')

# 做主成分之前，进行中心标准化

from sklearn import preprocessing

data = preprocessing.scale(data)
# 使用sklearn的主成分分析，用于判断保留主成分的数量

from sklearn.decomposition import PCA

"""说明：1、第一次的n_components参数应该设的大一点
   说明：2、观察explained_variance_ratio_和explained_variance_的取值变化，建议explained_variance_ratio_累积大于0.85，explained_variance_需要保留的最后一个主成分大于0.8，
"""
pca = PCA(n_components=3)
pca.fit(data)
print(pca.explained_variance_)  # 建议保留2个主成分
print(pca.explained_variance_ratio_)  # 建议保留3个主成分

pca = PCA(n_components=3).fit(data)  # 综上,2个主成分
newdata = pca.fit_transform(data)

# 通过主成分在每个变量上的权重的绝对值大小，确定每个主成分的代表性

pd.DataFrame(pca.components_).T
# 第一个主成分在第3个变量权重差不多高
# 第二个主成分在第1个变量权重高,其余均低
# 第三个主成分在第4个变量权重高,其余均低
#############################################################################################
# 二、因子分析
# 因子分析的概念很多，作为刚入门的人，我们可以认为因子分析是主成分分析的延续

from fa_kit import FactorAnalysis
from fa_kit import plotting as fa_plotting

fa = FactorAnalysis.load_data_samples(data, preproc_demean=True, preproc_scale=True)
fa.extract_components()

# 设定提取主成分的方式。默认为“broken_stick”方法，建议使用“top_n”法

fa.find_comps_to_retain(method="top_n", num_keep=3)
# 通过最大方差法进行因子旋转

pd.DataFrame(fa.comps["rot"])  # 查看因子权重
fa.rotate_components(method="varimax")
fa_plotting.graph_summary(fa)
# - 说明：可以通过第三张图观看每个因子在每个变量上的权重，权重越高，代表性越强

# 获取因子得分

# 到目前还没有与PCA中fit_transform类似的函数，因此只能手工计算因子
# 以下是矩阵相乘的方式计算因子：因子=原始数据（n*k）*权重矩阵(k*num_keep)
fas = pd.DataFrame(fa.comps["rot"])
data = pd.DataFrame(data)  # 注意data数据需要标准化
fa_score = pd.DataFrame(np.dot(data, fas))

# 第三步：根据因子得分进行数据分析

a = fa_score.rename(columns={0: "Gross", 1: "Avg"})
profile_bank_fa = model_data.join(a)

#############################################################################################
# 三、变量筛选
# 以下是变量选择的完整函数
# 基于SparsePCA的算法还不是很稳定,尤其是当数据本身保留几个变量都处于模棱两个的时候,
# 该算法并不能达到人为调整的效果。而且并不能保证每次保留的变量是一致的（原因1、SparsePCA：本身就具有随机性；2、脚本中也随机抽样的），
# 只能保证保留的变量是不相关的
# 其特点只是比较省人力，可以自动化运行


def Var_Select(orgdata, k, alphaMax=10, alphastep=0.2):
    """
    orgdata-需要信息压缩的数据框
    k-预期最大需要保留的最大变量个数，实际保留数量不能多于这个数值
    alphaMax-SparsePCA算法惩罚项的最大值,一般要到5才会取得比较理想的结果
    alphastep-SparsePCA算法惩罚项递增的步长
    """
    # step1:当数据量过大时，为了减少不必要的耗时
    if orgdata.iloc[:, 1].count() > 5000:
        data = orgdata.sample(5000)
    else:
        data = orgdata
    # step2:引入所需要的包，并且对数据进行标准化
    from sklearn import preprocessing
    from sklearn.decomposition import SparsePCA

    # from functools import reduce
    data = preprocessing.scale(data)
    n_components = k
    # pca_n = list()
    # step3:进行SparsePCA计算，选择合适的惩罚项alpha，当恰巧每个原始变量只在一个主成分上有权重时，停止循环
    for i in np.arange(0.1, alphaMax, alphastep):
        pca_model = SparsePCA(n_components=n_components, alpha=i)
        pca_model.fit(data)
        pca = pd.DataFrame(pca_model.components_).T
        n = data.shape[1] - sum(sum(np.array(pca != 0)))  ####计算系数不为0的数量
        if n == 0:
            global best_alpha
            best_alpha = i
            break
    # step4:根据上一步得到的惩罚项的取值，估计SparsePCA，并得到稀疏主成分得分
    pca_model = SparsePCA(n_components=n_components, alpha=best_alpha)
    pca_model.fit(data)
    pca = pd.DataFrame(pca_model.components_).T
    data = pd.DataFrame(data)
    score = pd.DataFrame(pca_model.fit_transform(data))
    # step6:计算原始变量与主成分之间的1-R方值
    r = []
    R_square = []
    for xk in range(data.shape[1]):  # xk输入变量个数
        for paj in range(n_components):  # paj主成分个数
            r.append(abs(np.corrcoef(data.iloc[:, xk], score.iloc[:, paj])[0, 1]))
            r_max1 = max(r)
            r.remove(r_max1)
            r.append(-2)
            r_max2 = max(r)
            R_square.append((1 - r_max1**2) / (1 - r_max2**2))

    R_square = abs(
        pd.DataFrame(np.array(R_square).reshape((data.shape[1], n_components)))
    )
    var_list = []
    # print(R_square)
    # step7:每个主成分中，选出原始变量的1-R方值最小的。
    for i in range(n_components):
        vmin = R_square[i].min()
        # print(R_square[i])
        # print(vmin)
        # print(R_square[R_square[i] == min][i])
        var_list.append(R_square[R_square[i] == vmin][i].index)

    news_ids = []
    for id in var_list:
        if id not in news_ids:
            news_ids.append(id)
    print(news_ids)
    data_vc = orgdata.iloc[:, np.array(news_ids).reshape(len(news_ids))]
    return data_vc


model_data = pd.read_csv("data/profile_bank.csv")
data = model_data.loc[:, "CNT_TBM":"CNT_CSC"]

Varseled_data = Var_Select(data, k=3, alphaMax=10)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# chapter13_4 Varselect_creditcard_exp


def Var_Select(orgdata, k, alphaMax=10, alphastep=0.2):
    """
    orgdata-需要信息压缩的数据框
    k-预期最大需要保留的最大变量个数，实际保留数量不能多于这个数值
    alphaMax-SparsePCA算法惩罚项的最大值,一般要到5才会取得比较理想的结果
    alphastep-SparsePCA算法惩罚项递增的步长
    """
    # step1:当数据量过大时，为了减少不必要的耗时
    if orgdata.iloc[:, 1].count() > 5000:
        data = orgdata.sample(5000)
    else:
        data = orgdata
    # step2:引入所需要的包，并且对数据进行标准化
    from sklearn import preprocessing
    from sklearn.decomposition import SparsePCA

    # from functools import reduce
    data = preprocessing.scale(data)
    n_components = k
    # pca_n = list()
    # step3:进行SparsePCA计算，选择合适的惩罚项alpha，当恰巧每个原始变量只在一个主成分上有权重时，停止循环
    for i in np.arange(0.1, alphaMax, alphastep):
        pca_model = SparsePCA(n_components=n_components, alpha=i)
        pca_model.fit(data)
        pca = pd.DataFrame(pca_model.components_).T
        n = data.shape[1] - sum(sum(np.array(pca != 0)))  ####计算系数不为0的数量
        if n == 0:
            global best_alpha
            best_alpha = i
            break
    # step4:根据上一步得到的惩罚项的取值，估计SparsePCA，并得到稀疏主成分得分
    pca_model = SparsePCA(n_components=n_components, alpha=best_alpha)
    pca_model.fit(data)
    pca = pd.DataFrame(pca_model.components_).T
    data = pd.DataFrame(data)
    score = pd.DataFrame(pca_model.fit_transform(data))
    # step6:计算原始变量与主成分之间的1-R方值
    r = []
    R_square = []
    for xk in range(data.shape[1]):  # xk输入变量个数
        for paj in range(n_components):  # paj主成分个数
            r.append(abs(np.corrcoef(data.iloc[:, xk], score.iloc[:, paj])[0, 1]))
            r_max1 = max(r)
            r.remove(r_max1)
            r.append(-2)
            r_max2 = max(r)
            R_square.append((1 - r_max1**2) / (1 - r_max2**2))

    R_square = abs(
        pd.DataFrame(np.array(R_square).reshape((data.shape[1], n_components)))
    )
    var_list = []
    # print(R_square)
    # step7:每个主成分中，选出原始变量的1-R方值最小的。
    for i in range(n_components):
        vmin = R_square[i].min()
        # print(R_square[i])
        # print(vmin)
        # print(R_square[R_square[i] == min][i])
        var_list.append(R_square[R_square[i] == vmin][i].index)

    news_ids = []
    for id in var_list:
        if id not in news_ids:
            news_ids.append(id)
    print(news_ids)
    data_vc = orgdata.iloc[:, np.array(news_ids).reshape(len(news_ids))]
    return data_vc


model_data = pd.read_csv("data/creditcard_exp.csv")
model_data.head()
data = model_data.loc[:, "gender":]

Varseled_data = Var_Select(data, k=5)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# varselect_bank

model_data = pd.read_csv("data/profile_bank.csv")
data = model_data.loc[:, "CNT_TBM":"CNT_CSC"]
k = 3
alphaMax = 5
alphastep = 0.2

from sklearn import preprocessing
from sklearn.decomposition import SparsePCA
from functools import reduce

data = preprocessing.scale(data)
n_components = k
pca_n = list()

pca_model = SparsePCA(n_components=n_components, alpha=5)
pca_model.fit(data)

pca = pd.DataFrame(pca_model.components_).T

n = data.shape[1] - sum(sum(np.array(pca != 0)))

best_alpha = 5
pca_model = SparsePCA(n_components=n_components, alpha=best_alpha)
pca_model.fit(data)
pca = pd.DataFrame(pca_model.components_).T
data = pd.DataFrame(data)
score = pd.DataFrame(pca_model.fit_transform(data))

r = []
R_square = []
for xk in range(data.shape[1]):  # xk输入变量个数
    for paj in range(n_components):  # paj主成分个数
        r.append(abs(np.corrcoef(data.iloc[:, xk], score.iloc[:, paj])[0, 1]))
        r_max1 = max(r)
        r.remove(r_max1)
        r.append(-2)
        r_max2 = max(r)
        R_square.append((1 - r_max1**2) / (1 - r_max2**2))

R = abs(pd.DataFrame(np.array(r).reshape((data.shape[1], n_components))))
R_square = abs(pd.DataFrame(np.array(R_square).reshape((data.shape[1], n_components))))
var_list = []
# print(R_square)

for i in range(n_components):
    vmin = R_square[i].min()
    print(R_square[i])
    print(vmin)
    print(R_square[R_square[i] == min][i])
    var_list.append(R_square[R_square[i] == vmin][i].index[0])

news_ids = []
for id in var_list:
    if id not in news_ids:
        news_ids.append(id)
print(news_ids)
orgdata = model_data.loc[:, "CNT_TBM":"CNT_CSC"]
data_vc = orgdata.iloc[:, np.array(news_ids).reshape(len(news_ids))]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 第十四讲 聚类
# 1、层次聚类

import scipy
import scipy.cluster.hierarchy as sch
from scipy.cluster.vq import vq, kmeans, whiten
from sklearn import metrics
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn import cluster

print("------------------------------------------------------------")  # 60個

# 导入数据
orgData = pd.read_csv("data/cities_10.csv", index_col="AREA", encoding="gbk")
orgData.head()
# orgData.describe()

# 标准化
x_scaled = preprocessing.scale(orgData + 0.0)  # 归一化，但是只能用于浮点类型变量
pd.DataFrame(x_scaled).head()

# 变量压缩
pca = PCA(n_components=2)
newData = pca.fit_transform(x_scaled)
cc = pca.explained_variance_ratio_
print(cc)

print(newData)

# 1. 层次聚类
# 生成点与点之间的距离矩阵,这里用的欧氏距离:
disMat = sch.distance.pdist(newData, "euclidean")
# 进行层次聚类:
Z = sch.linkage(disMat, method="average")
# 将层级聚类结果以树状图表示出来并保存为plot_dendrogram.png
P = sch.dendrogram(Z)
# 存檔 plt.savefig('tmp_plot_dendrogram1.png')

# 2、K-means聚类

iris = pd.read_csv("data/iris_one_book.csv")
x = iris.loc[:, "Sepal.Length":"Petal.Width"]
y = iris["Species"]

# 归一化的使用说明 http://www.cnblogs.com/chaosimple/p/4153167.html

x_scaled = preprocessing.scale(x + 0.0)  # 归一化，但是只能用于浮点类型变量
cc = pd.DataFrame(x_scaled).head()
print(cc)

pca = PCA(n_components=3)
newData = pca.fit_transform(x_scaled)
cc = pca.explained_variance_ratio_
print(cc)

score = pd.DataFrame(newData)
cc = score.head()
print(cc)

# http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans

from sklearn.cluster import KMeans

kmeans = cluster.KMeans(n_clusters=3)  # MiniBatchKMeans()分批处理
# kmeans = cluster.KMeans(n_clusters=3, init='random', n_init=1)
result = kmeans.fit(x_scaled)
print(result)

cc = result.labels_
print(cc)

lo = plt.scatter(
    score[0][result.labels_ == 0], score[1][result.labels_ == 0], marker="x"
)
lo = plt.scatter(
    score[0][result.labels_ == 1], score[1][result.labels_ == 1], marker="o"
)
lo = plt.scatter(
    score[0][result.labels_ == 2], score[1][result.labels_ == 2], marker="+"
)

# 聚类效果评估
# Silhouette Coefficient
# http://scikit-learn.org/stable/modules/clustering.html#clustering

# 計算輪廓分數
cc = metrics.silhouette_score(x_scaled, result.labels_, metric="euclidean")
# print("分", CLUSTERS, "群, 計算輪廓分數:", cc)
print("計算輪廓分數:", cc)

# Adjusted Rand index
# http://scikit-learn.org/stable/modules/clustering.html#clustering

cc = metrics.adjusted_rand_score(y, result.labels_)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# chapter14_1 Hclus_FCA_city10.py

# 第十四讲 聚类

# 层次聚类

# 第一步：手动测试主成分数量

model_data = pd.read_csv("data/cities_10.csv", encoding="gbk")
model_data.head()

data = model_data.loc[:, "X1":]
data.head()

# 查看相关系数矩阵，判定做变量降维的必要性（非必须）

corr_matrix = data.corr(method="pearson")
# corr_matrix = corr_matrix.abs()
corr_matrix

# 做主成分之前，进行中心标准化

from sklearn import preprocessing

data = preprocessing.scale(data)

# 使用sklearn的主成分分析，用于判断保留主成分的数量

from sklearn.decomposition import PCA

# 说明：1、第一次的n_components参数应该设的大一点
# 说明：2、观察explained_variance_ratio_和explained_variance_的取值变化，建议explained_variance_ratio_累积大于0.85，explained_variance_需要保留的最后一个主成分大于0.8，

pca = PCA(n_components=3)
newData = pca.fit(data)
print(pca.explained_variance_)
print(pca.explained_variance_ratio_)

# 第二步：根据主成分分析确定需要保留的主成分数量，进行因子分析

# 导入包，并对输入的数据进行主成分提取。为保险起见，data需要进行中心标准化

from fa_kit import FactorAnalysis
from fa_kit import plotting as fa_plotting

fa = FactorAnalysis.load_data_samples(data, preproc_demean=True, preproc_scale=True)
fa.extract_components()

# 设定提取主成分的方式。默认为“broken_stick”方法，建议使用“top_n”法

fa.find_comps_to_retain(method="top_n", num_keep=2)

# 通过最大方差法进行因子旋转

fa.rotate_components(method="varimax")
fa_plotting.graph_summary(fa)

# 说明：可以通过第三张图观看每个因子在每个变量上的权重，权重越高，代表性越强

# 获取因子得分

pd.DataFrame(fa.comps["rot"])

fas = pd.DataFrame(fa.comps["rot"])
data = pd.DataFrame(data)
score = pd.DataFrame(np.dot(data, fas))

# 第三步：根据因子得分进行数据分析

a = score.rename(columns={0: "Gross", 1: "Avg"})
citi10_fa = model_data.join(a)

# df存檔 citi10_fa.to_csv("data/citi10_fa.csv")

x = citi10_fa["Gross"]
y = citi10_fa["Avg"]
label = citi10_fa["AREA"]
plt.scatter(x, y)
for a, b, l in zip(x, y, label):
    plt.text(a, b + 0.1, "%s." % l, ha="center", va="bottom", fontsize=14)

show()

import scipy.cluster.hierarchy as sch

# 1. 层次聚类
# 生成点与点之间的距离矩阵,这里用的欧氏距离:
disMat = sch.distance.pdist(citi10_fa[["Gross", "Avg"]], "euclidean")
# 进行层次聚类:
Z = sch.linkage(disMat, method="ward")
# 将层级聚类结果以树状图表示出来并保存为plot_dendrogram.png
P = sch.dendrogram(
    Z, labels=["辽宁", "山东", "河北", "天津", "江苏", "上海", "浙江", "福建", "广东", "广西"]
)
# 存檔 plt.savefig('tmp_plot_dendrogram2.png')

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Kmeans_FA_bank.py

# K-means聚类分析

# 手动测试主成分数量

model_data = pd.read_csv("data/profile_bank.csv")
data = model_data.loc[:, "CNT_TBM":"CNT_CSC"]
data.head()

# 查看相关系数矩阵，判定做变量降维的必要性（非必须）

corr_matrix = data.corr(method="pearson")
# corr_matrix = corr_matrix.abs()
corr_matrix

# 做主成分之前，进行中心标准化

from sklearn import preprocessing

data = preprocessing.scale(data)

# 使用sklearn的主成分分析，用于判断保留主成分的数量

from sklearn.decomposition import PCA

# 说明：1、第一次的n_components参数应该设的大一点
# 说明：2、观察explained_variance_ratio_和explained_variance_的取值变化，建议explained_variance_ratio_累积大于0.85，explained_variance_需要保留的最后一个主成分大于0.8，

pca = PCA(n_components=3)
newData = pca.fit(data)
print(pca.explained_variance_)
print(pca.explained_variance_ratio_)

# 通过主成分在每个变量上的权重的绝对值大小，确定每个主成分的代表性

pd.DataFrame(pca.components_).T

# 第二步：根据主成分分析确定需要保留的主成分数量，进行因子分析

# 导入包，并对输入的数据进行主成分提取。为保险起见，data需要进行中心标准化

from fa_kit import FactorAnalysis
from fa_kit import plotting as fa_plotting

fa = FactorAnalysis.load_data_samples(data, preproc_demean=True, preproc_scale=True)
fa.extract_components()

# 设定提取主成分的方式。默认为“broken_stick”方法，建议使用“top_n”法

fa.find_comps_to_retain(method="top_n", num_keep=3)

# 通过最大方差法进行因子旋转

fa.rotate_components(method="varimax")
fa_plotting.graph_summary(fa)

# 说明：可以通过第三张图观看每个因子在每个变量上的权重，权重越高，代表性越强

# 获取因子得分

pd.DataFrame(fa.comps["rot"])

fas = pd.DataFrame(fa.comps["rot"])
data = pd.DataFrame(data)
score = pd.DataFrame(np.dot(data, fas))

# 第三步：根据因子得分进行数据分析

fa_scores = score.rename(columns={0: "ATM_POS", 1: "TBM", 2: "CSC"})
fa_scores.head()

# 第四步：使用因子得分进行k-means聚类

# k-means聚类的第一种方式：不进行变量分布的正态转换--用于寻找异常值

# 查看变量的偏度

var = ["ATM_POS", "TBM", "CSC"]
skew_var = {}
for i in var:
    skew_var[i] = abs(fa_scores[i].skew())
    skew = pd.Series(skew_var).sort_values(ascending=False)
skew

# 进行k-means聚类

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3)  # MiniBatchKMeans()分批处理
# kmeans = cluster.KMeans(n_clusters=3, init='random', n_init=1)
result = kmeans.fit(fa_scores)
# print(result)

# 对分类结果进行解读

model_data_l = model_data.join(pd.DataFrame(result.labels_))
model_data_l = model_data_l.rename(columns={0: "clustor"})
model_data_l.head()

import matplotlib

# get_ipython().magic('matplotlib inline')
model_data_l.clustor.value_counts().plot(kind="pie")
show()

# k-means聚类的第二种方式：进行变量分布的正态转换--用于客户细分

# 进行变量分布的正态转换

from sklearn import preprocessing

quantile_transformer = preprocessing.QuantileTransformer(
    output_distribution="normal", random_state=0
)
fa_scores_trans = quantile_transformer.fit_transform(fa_scores)
fa_scores_trans = pd.DataFrame(fa_scores_trans)
fa_scores_trans = fa_scores_trans.rename(columns={0: "ATM_POS", 1: "TBM", 2: "CSC"})
fa_scores_trans.head()

var = ["ATM_POS", "TBM", "CSC"]
skew_var = {}
for i in var:
    skew_var[i] = abs(fa_scores_trans[i].skew())
    skew = pd.Series(skew_var).sort_values(ascending=False)
skew

# 进行k-means聚类

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3)  # MiniBatchKMeans()分批处理
# kmeans = cluster.KMeans(n_clusters=3, init='random', n_init=1)
result = kmeans.fit(fa_scores_trans)
# print(result)

# 对分类结果进行解读

model_data_l = model_data.join(pd.DataFrame(result.labels_))
model_data_l = model_data_l.rename(columns={0: "clustor"})
model_data_l.head()


import matplotlib

# get_ipython().magic('matplotlib inline')
model_data_l.clustor.value_counts().plot(kind="pie")
show()

from sklearn import tree

clf = tree.DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    min_samples_split=100,
    min_samples_leaf=100,
    random_state=12345,
)  # 当前支持计算信息增益和GINI
clf.fit(model_data, result.labels_)

import pydotplus
from IPython.display import Image  # 用IPython
import sklearn.tree as tree

# 決策樹可視化存檔
dot_data = tree.export_graphviz(
    clf,
    out_file=None,
    feature_names=model_data.columns,
    class_names=["0", "1", "2"],
    filled=True,
)

graph = pydotplus.graph_from_dot_data(dot_data)
# Image(graph.create_png())   # 用IPython顯示圖片

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


# 查看一下关键字有哪些，避免关键字做自定义标识符
import keyword

print(keyword.kwlist)


# .ix改 .loc


# normed 改成 density

# In[19]:
