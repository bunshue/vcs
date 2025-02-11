

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

# 日期时间

now = time.strptime("2016-07-20", "%Y-%m-%d")
print(now)

type(now)

cc = time.strftime("%Y-%m-%d", now)
print(cc)

import datetime

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


# - 匿名函数：高阶函数传入函数时，不需要显式地定义函数，直接传入匿名函数更方便
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

# - pandas可以读取文本文件、json、数据库、Excel等文件
# - 使用read_csv方法读取以逗号分隔的文本文件作为DataFrame，其它还有类似read_table, read_excel, read_html, read_sql等等方法

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

# 写入文件
xls.to_csv("tmp_copyofhsb2.csv")


# 查看一下关键字有哪些，避免关键字做自定义标识符
import keyword

print(keyword.kwlist)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# # 逻辑回归
# 信用风险建模案例
##数据说明：本数据是一份汽车贷款违约数据
##名称---中文含义
##application_id---申请者ID
##account_number---帐户号
##bad_ind---是否违约
##vehicle_year---汽车购买时间
##vehicle_make---汽车制造商
##bankruptcy_ind---曾经破产标识
##tot_derog---五年内信用不良事件数量(比如手机欠费消号)
##tot_tr---全部帐户数量
##age_oldest_tr---最久账号存续时间(月)
##tot_open_tr---在使用帐户数量
##tot_rev_tr---在使用可循环贷款帐户数量(比如信用卡)
##tot_rev_debt---在使用可循环贷款帐户余额(比如信用卡欠款)
##tot_rev_line---可循环贷款帐户限额(信用卡授权额度)
##rev_util---可循环贷款帐户使用比例(余额/限额)
##fico_score---FICO打分
##purch_price---汽车购买金额(元)
##msrp---建议售价
##down_pyt---分期付款的首次交款
##loan_term---贷款期限(月)
##loan_amt---贷款金额
##ltv---贷款金额/建议售价*100
##tot_income---月均收入(元)
##veh_mileage---行使历程(Mile)
##used_ind---是否二手车
##weight---样本权重

from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

# pd.set_option('display.max_columns', None)
os.chdir(r"C:\_git\vcs\_4.python\__code\一書貫通-從資料科學橫入人工智慧領域")

# 导入数据和数据清洗

accepts = pd.read_csv("data/accepts.csv").dropna()


##衍生变量:
def divMy(x, y):
    if x == np.nan or y == np.nan:
        return np.nan
    elif y == 0:
        return -1
    else:
        return x / y


divMy(1, 2)

##历史负债收入比:tot_rev_line/tot_income
accepts["dti_hist"] = accepts[["tot_rev_line", "tot_income"]].apply(
    lambda x: divMy(x[0], x[1]), axis=1
)
##本次新增负债收入比:loan_amt/tot_income
accepts["dti_mew"] = accepts[["loan_amt", "tot_income"]].apply(
    lambda x: divMy(x[0], x[1]), axis=1
)
##本次贷款首付比例:down_pyt/loan_amt
accepts["fta"] = accepts[["down_pyt", "loan_amt"]].apply(
    lambda x: divMy(x[0], x[1]), axis=1
)
##新增债务比:loan_amt/tot_rev_debt
accepts["nth"] = accepts[["loan_amt", "tot_rev_debt"]].apply(
    lambda x: divMy(x[0], x[1]), axis=1
)
##新增债务额度比:loan_amt/tot_rev_line
accepts["nta"] = accepts[["loan_amt", "tot_rev_line"]].apply(
    lambda x: divMy(x[0], x[1]), axis=1
)

accepts.head()

# 分类变量的相关关系

# 交叉表

cross_table = pd.crosstab(accepts.used_ind, accepts.bad_ind, margins=True)
# cross_table = pd.crosstab(accepts.bankruptcy_ind,accepts.bad_ind, margins=True)

cross_table

# 列联表


def percConvert(ser):
    return ser / float(ser[-1])


cross_table.apply(percConvert, axis=1)

print(
    """chisq = %6.4f 
p-value = %6.4f
dof = %i 
expected_freq = %s"""
    % stats.chi2_contingency(cross_table.iloc[:2, :2])
)

# 逻辑回归

accepts.plot(x="age_oldest_tr", y="bad_ind", kind="scatter")

# 随机抽样，建立训练集与测试集

train = accepts.sample(frac=0.7, random_state=1234).copy()
test = accepts[~accepts.index.isin(train.index)].copy()
print(" 训练集样本量: %i \n 测试集样本量: %i" % (len(train), len(test)))

lg = smf.glm(
    "bad_ind ~ age_oldest_tr",
    data=train,
    family=sm.families.Binomial(sm.families.links.logit),
).fit()
lg.summary()

# 预测

train["proba"] = lg.predict(train)
test["proba"] = lg.predict(test)

test["proba"].head(10)

# 模型评估
# 设定阈值

test["prediction"] = (test["proba"] > 0.3).astype("int")

# 混淆矩阵

pd.crosstab(test.bad_ind, test.prediction, margins=True)

# 计算准确率

acc = sum(test["prediction"] == test["bad_ind"]) / np.float(len(test))
print("The accurancy is %.2f" % acc)

for i in np.arange(0.02, 0.3, 0.02):
    prediction = (test["proba"] > i).astype("int")
    confusion_matrix = pd.crosstab(prediction, test.bad_ind, margins=True)
    precision = confusion_matrix.ix[0, 0] / confusion_matrix.ix["All", 0]
    recall = confusion_matrix.ix[0, 0] / confusion_matrix.ix[0, "All"]
    Specificity = confusion_matrix.ix[1, 1] / confusion_matrix.ix[1, "All"]
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(
        "threshold: %s, precision: %.2f, recall:%.2f ,Specificity:%.2f , f1_score:%.2f"
        % (i, precision, recall, Specificity, f1_score)
    )

# - 绘制ROC曲线

import sklearn.metrics as metrics

fpr_test, tpr_test, th_test = metrics.roc_curve(test.bad_ind, test.proba)
fpr_train, tpr_train, th_train = metrics.roc_curve(train.bad_ind, train.proba)

plt.figure(figsize=[3, 3])
plt.plot(fpr_test, tpr_test, "b--")
plt.plot(fpr_train, tpr_train, "r-")
plt.title("ROC curve")
plt.show()

print("AUC = %.4f" % metrics.auc(fpr_test, tpr_test))

# 包含分类预测变量的逻辑回归

formula = """bad_ind ~ C(used_ind)"""

lg_m = smf.glm(
    formula=formula, data=train, family=sm.families.Binomial(sm.families.links.logit)
).fit()
lg_m.summary()


# 多元逻辑回归
# 向前法
def forward_select(data, response):
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = float("inf"), float("inf")
    while remaining:
        aic_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {}".format(response, " + ".join(selected + [candidate]))
            aic = (
                smf.glm(
                    formula=formula,
                    data=data,
                    family=sm.families.Binomial(sm.families.links.logit),
                )
                .fit()
                .aic
            )
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
    model = smf.glm(
        formula=formula, data=data, family=sm.families.Binomial(sm.families.links.logit)
    ).fit()
    return model


# 只有连续变量可以进行变量筛选，分类变量需要进行WOE转换才可以进行变量筛选
candidates = [
    "bad_ind",
    "tot_derog",
    "age_oldest_tr",
    "tot_open_tr",
    "rev_util",
    "fico_score",
    "loan_term",
    "ltv",
    "veh_mileage",
    "dti_hist",
    "dti_mew",
    "fta",
    "nth",
    "nta",
]
data_for_select = train[candidates]

lg_m1 = forward_select(data=data_for_select, response="bad_ind")
lg_m1.summary()

# Seemingly wrong when using 'statsmmodels.stats.outliers_influence.variance_inflation_factor'


def vif(df, col_i):
    from statsmodels.formula.api import ols

    cols = list(df.columns)
    cols.remove(col_i)
    cols_noti = cols
    formula = col_i + "~" + "+".join(cols_noti)
    r2 = ols(formula, df).fit().rsquared
    return 1.0 / (1.0 - r2)


candidates = [
    "bad_ind",
    "fico_score",
    "ltv",
    "age_oldest_tr",
    "tot_derog",
    "nth",
    "tot_open_tr",
    "veh_mileage",
    "rev_util",
]
exog = train[candidates].drop(["bad_ind"], axis=1)

for i in exog.columns:
    print(i, "\t", vif(df=exog, col_i=i))

train["proba"] = lg_m1.predict(train)
test["proba"] = lg_m1.predict(test)
import sklearn.metrics as metrics

fpr_test, tpr_test, th_test = metrics.roc_curve(test.bad_ind, test.proba)
fpr_train, tpr_train, th_train = metrics.roc_curve(train.bad_ind, train.proba)

plt.figure(figsize=[3, 3])
plt.plot(fpr_test, tpr_test, "b--")
plt.plot(fpr_train, tpr_train, "r-")
plt.title("ROC curve")
plt.show()

print("AUC = %.4f" % metrics.auc(fpr_test, tpr_test))

# 目前vehicle_year、vehicle_make、bankruptcy_ind、used_ind这些分类变量无法通过逐步变量筛选法
# 解决方案：
# 1、逐一根据显著性测试
# 2、使用决策树等方法筛选变量，但是多分类变量需要事先进行变量概化
# 3、使用WOE转换，多分类变量也需要事先进行概化，使用scorecardpy包中的woe算法可以自动进行概化
# 使用第一种方法
# formula = '''bad_ind ~ fico_score+ltv+age_oldest_tr+tot_derog+nth+tot_open_tr+veh_mileage+rev_util+C(used_ind)+C(vehicle_year)+C(bankruptcy_ind)'''
formula = """bad_ind ~ fico_score+ltv+age_oldest_tr+tot_derog+nth+tot_open_tr+veh_mileage+rev_util+C(bankruptcy_ind)"""
lg_m = smf.glm(
    formula=formula, data=train, family=sm.families.Binomial(sm.families.links.logit)
).fit()
lg_m.summary()

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

import statsmodels.api as sm
from statsmodels.formula.api import ols

# 导入数据和数据清洗

raw = pd.read_csv(r"data/creditcard_exp.csv", skipinitialspace=True)
raw.head()

exp = raw[raw["avg_exp"].notnull()].copy().iloc[:, 2:].drop("age2", axis=1)

exp_new = raw[raw["avg_exp"].isnull()].copy().iloc[:, 2:].drop("age2", axis=1)

exp.describe(include="all")


# ### 相关性分析
# 散点图

exp.plot("Income", "avg_exp", kind="scatter")
plt.show()


exp[["Income", "avg_exp", "Age", "dist_home_val"]].corr(method="pearson")


# ## 线性回归算法
# ### 简单线性回归

lm_s = ols("avg_exp ~ Income+Age+dist_home_val", data=exp).fit()
cc = lm_s.summary()
print(cc)

# Predict-在原始数据集上得到预测值和残差

cc = lm_s.summary()
print(cc)

pd.DataFrame([lm_s.predict(exp), lm_s.resid], index=["predict", "resid"]).T.head()


# 在待预测数据集上得到预测值

lm_s.predict(exp_new)[:5]


# ### 多元线性回归

lm_m = ols("avg_exp ~ Age + Income + dist_home_val + dist_avg_income", data=exp).fit()
cc = lm_m.summary()
print(cc)

# ### 多元线性回归的变量筛选


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
# ### 残差分析

ana1 = lm_s


exp["Pred"] = ana1.predict(exp)
exp["resid"] = ana1.resid
exp.plot("Pred", "resid", kind="scatter")
plt.show()

# 遇到异方差情况,教科书上会介绍使用加权最小二乘法，但是实际上最常用的是对被解释变量取对数
ana1 = ols("avg_exp ~ Income", exp).fit()
cc = ana1.summary()
print(cc)

ana2 = ols("avg_exp_ln ~ Income", exp).fit()
exp["Pred"] = ana2.predict(exp)
exp["resid"] = ana2.resid
exp.plot("Income", "resid", kind="scatter")
cc = ana2.summary()
print(cc)

plt.show()


# 取对数会使模型更有解释意义

exp["Income_ln"] = np.log(exp["Income"])

ana3 = ols("avg_exp_ln ~ Income_ln", exp).fit()
exp["Pred"] = ana3.predict(exp)
exp["resid"] = ana3.resid
exp.plot("Income_ln", "resid", kind="scatter")
plt.show()
cc = ana3.summary()
print(cc)

# 寻找最优的模型

r_sq = {
    "exp~Income": ana1.rsquared,
    "ln(exp)~Income": ana2.rsquared,
    "ln(exp)~ln(Income)": ana3.rsquared,
}
print(r_sq)

# ### 强影响点分析

exp["resid_t"] = (exp["resid"] - exp["resid"].mean()) / exp["resid"].std()


# Find outlier：

exp[abs(exp["resid_t"]) > 2]

# Drop outlier

exp2 = exp[abs(exp["resid_t"]) <= 2].copy()
ana4 = ols("avg_exp_ln ~ Income_ln", exp2).fit()
exp2["Pred"] = ana4.predict(exp2)
exp2["resid"] = ana4.resid
exp2.plot("Income", "resid", kind="scatter")
plt.show()

ana4.rsquared


# statemodels包提供了更多强影响点判断指标

from statsmodels.stats.outliers_influence import OLSInfluence

cc = OLSInfluence(ana3).summary_frame().head()
print(cc)

# ### 增加变量
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

# ### 多重共线性分析

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


# ## 正则算法
# ### 岭回归

lmr = ols(
    "avg_exp ~ Income + dist_home_val + dist_avg_income", data=exp
).fit_regularized(alpha=1, L1_wt=0)

# L1_wt参数为0则使用岭回归，为1使用lasso


# LASSO算法

lmr1 = ols(
    "avg_exp ~ Age + Income + dist_home_val + dist_avg_income", data=exp
).fit_regularized(alpha=1, L1_wt=1)

# ### 使用scikit-learn进行正则化参数调优

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
np.exp(rcv.predict(X_new)[:5])

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
plt.show()


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

plt.show()

ridge.set_params(alpha=40)
ridge.fit(X, y)
ridge.coef_


cc = ridge.score(X, y)
print(cc)

# 预测

np.exp(ridge.predict(X_new)[:5])

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

plt.show()

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

import statsmodels.api as sm
from statsmodels.formula.api import ols

pd.set_option("display.max_columns", None)

# 数据准备

tele = pd.read_csv("data/teleco_camp.csv")
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

# 相关性分析

arpu_known.plot("ARPU", "AvgARPU", kind="scatter")
plt.show()

cc = arpu_known.corr(method="pearson")
print(cc)

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

arpu_known["Pred"] = ana1.predict(arpu_known)
arpu_known["resid"] = ana1.resid
arpu_known.plot("AvgARPU", "resid", kind="scatter")
plt.show()

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
arpu_known2["Pred"] = ana2.predict(arpu_known2)
arpu_known2["resid"] = ana2.resid
arpu_known2.plot("AvgARPU", "resid", kind="scatter")
plt.show()

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

cc = rcv.predict(X)[:5]
print(cc)

dummies_new = enc.transform(arpu_unknown[["Gender", "HomeOwner", "Class"]]).toarray()
X_new = arpu_unknown[continuous_X].join(
    pd.DataFrame(dummies_new, index=arpu_unknown.index)
)

cc = rcv.predict(X_new)[:5]
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 第11讲 分类器
# KNN

from scipy import stats
import sklearn.model_selection as cross_validation

orgData = pd.read_csv("date_data2.csv")
cc = orgData.describe()
print(cc)

# 选取自变量

X = orgData.ix[:, :4]
Y = orgData[["Dated"]]
X.head()

# 极值标准化, MMS特徵縮放
from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
X_scaled = min_max_scaler.fit_transform(X)

cc = X_scaled[1:5]
print(cc)

# 划分训练集和测试集

train_data, test_data, train_target, test_target = cross_validation.train_test_split(
    X_scaled, Y, test_size=0.2, train_size=0.8, random_state=123
)  # 划分训练集和测试集

# 建模

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)  # 默认欧氏距离
model.fit(train_data, train_target.values.flatten())
test_est = model.predict(test_data)

# 验证

import sklearn.metrics as metrics

print(metrics.confusion_matrix(test_target, test_est, labels=[0, 1]))  # 混淆矩阵
print(metrics.classification_report(test_target, test_est))

model.score(test_data, test_target)

# 选择k值

for k in range(1, 15):
    k_model = KNeighborsClassifier(n_neighbors=k)
    k_model.fit(train_data, train_target.values.flatten())
    score = k_model.score(test_data, test_target)
    print(k, "\t", score)

# 交叉验证选择k值

# 應該也是改成 sklearn.model_selection
from sklearn.grid_search import ParameterGrid
from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import KFold

n_samples = len(train_data)
kf = KFold(n=n_samples, n_folds=3)
grid = ParameterGrid({"n_neighbors": [range(1, 15)]})
estimator = KNeighborsClassifier()
gridSearchCV = GridSearchCV(estimator, grid, cv=kf)
gridSearchCV.fit(train_data, train_target.values.flatten())
gridSearchCV.cv_results_  # cv_results_ : 具體用法模型不同參數下交叉驗證的結果

gridSearchCV.best_params_

best = gridSearchCV.best_estimator_
best.score(test_data, test_target)

# 练习：试一试哪些参数会影响结果

# 朴素贝叶斯

cc = orgData.head()
print(cc)

orgData1 = orgData.ix[:, -3:]

orgData1.income_rank = orgData1.income_rank.astype("category")
orgData1.describe(include="all")

(
    train_data1,
    test_data1,
    train_target1,
    test_target1,
) = cross_validation.train_test_split(
    orgData1, Y, test_size=0.3, train_size=0.7, random_state=123
)

# 建模

from sklearn.naive_bayes import BernoulliNB

NB = BernoulliNB(alpha=1)
NB.fit(train_data1, train_target1.values.flatten())
test_est1 = NB.predict(test_data1)

# 验证

print(metrics.classification_report(test_target1, test_est1))

NB.score(train_data1, train_target1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import sklearn.model_selection as cross_validation

os.chdir(r"D:\Python_book\11KNNNB")
pd.set_option("display.max_columns", None)


# In[ ]:


orgData = pd.read_csv("date_data2.csv")
# # 朴素贝叶斯

# In[ ]:


orgData.head()


# In[ ]:

Y = orgData[["Dated"]]
orgData1 = orgData.ix[:, -3:]

orgData1.income_rank = orgData1.income_rank.astype("category")
orgData1.describe(include="all")


# In[ ]:


(
    train_data1,
    test_data1,
    train_target1,
    test_target1,
) = cross_validation.train_test_split(
    orgData1, Y, test_size=0.3, train_size=0.7, random_state=123
)

# - 建模

from sklearn.naive_bayes import BernoulliNB

NB = BernoulliNB(alpha=1)
NB.fit(train_data1, train_target1.values.flatten())
test_est1 = NB.predict(test_data1)

# - 验证

import sklearn.metrics as metrics

print(metrics.classification_report(test_target1, test_est1))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 第12讲 高级分类器：支持向量机( SVM)与凸优化

from scipy import stats
import sklearn.model_selection as cross_validation

orgData = pd.read_csv("date_data2.csv")
cc = orgData.describe()
print(cc)

# 提取如下字段进行建模

X = orgData.ix[:, :4]
Y = orgData["Dated"]

# 构建训练集和测试集

train_data, test_data, train_target, test_target = cross_validation.train_test_split(
    X, Y, test_size=0.4, train_size=0.6, random_state=123
)  # 划分训练集和测试集

# 使用svm，建立支持向量机模型

from sklearn import svm

svcModel = svm.SVC(kernel="rbf", gamma=0.5, C=0.5, probability=True).fit(
    train_data, train_target
)

# 初步评估

import sklearn.metrics as metrics

test_est = svcModel.predict(test_data)
print(metrics.classification_report(test_target, test_est))  # 计算评估指标

# 进行标准化可以提升高斯核svm的表现

from sklearn import preprocessing

scaler = preprocessing.StandardScaler().fit(train_data)
train_scaled = scaler.transform(train_data)
test_scaled = scaler.transform(test_data)

svcModel1 = svm.SVC(kernel="rbf", gamma=0.5, C=0.5, probability=True).fit(
    train_scaled, train_target
)
test_est1 = svcModel1.predict(test_scaled)
print(metrics.classification_report(test_target, test_est1))  # 计算评估指标

# 选择最优模型

from sklearn.grid_search import ParameterGrid, GridSearchCV

kernel = ("linear", "rbf")
gamma = np.arange(0.01, 1, 0.1)
C = np.arange(0.01, 1.0, 0.1)
grid = {"gamma": gamma, "C": C}

clf_search = GridSearchCV(estimator=svcModel1, param_grid=grid, cv=4)
clf_search.fit(train_scaled, train_target)

best_model = clf_search.best_estimator_
test_est2 = best_model.predict(test_scaled)
print(metrics.classification_report(test_target, test_est2))  # 计算评估指标

best_model

# 画出在svm模型中，两个变量的关系图，可以用于提升感性认识，但一般不能推广到大于两维的情况

train_x = train_scaled[:, 1:3]
train_y = train_target.values
h = 1.0  # step size in the mesh
C = 1.0  # SVM regularization parameter
svc = svm.SVC(kernel="linear", C=C).fit(train_x, train_y)
rbf_svc = svm.SVC(kernel="rbf", gamma=0.5, C=1).fit(train_x, train_y)
poly_svc = svm.SVC(kernel="poly", degree=3, C=C).fit(train_x, train_y)
lin_svc = svm.LinearSVC(C=C).fit(train_x, train_y)

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

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

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

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
