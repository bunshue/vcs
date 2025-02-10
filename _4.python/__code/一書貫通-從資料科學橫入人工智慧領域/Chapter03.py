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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
