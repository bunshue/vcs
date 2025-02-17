"""


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

# 19_2Donations_2linear-checkpoint

model_data = pd.read_csv("donations2.csv").drop(["ID", "TARGET_B"], axis=1)
cc = model_data.head()
print(cc)

model_data.dtypes
y = ["TARGET_D"]
var_c = [
    "GiftCnt36",
    "GiftCntAll",
    "GiftCntCard36",
    "GiftCntCardAll",
    "GiftTimeLast",
    "GiftTimeFirst",
    "PromCnt12",
    "PromCnt36",
    "PromCntAll",
    "PromCntCard12",
    "PromCntCard36",
    "PromCntCardAll",
    "StatusCatStarAll",
    "DemAge",
    "DemMedHomeValue",
    "DemPctVeterans",
    "DemMedIncome",
    "GiftAvgLast",
    "GiftAvg36",
    "GiftAvgAll",
    "GiftAvgCard36",
]
var_d = ["DemGender", "StatusCat96NK", "DemCluster", "DemHomeOwner"]
X = model_data[var_c + var_d]
Y = model_data[y]

# 连续型变量重要性筛选：

corr_s = abs(model_data[y + var_c].corr(method="spearman"))
corr_s = pd.DataFrame(corr_s.iloc[0, :])
corr_p = abs(model_data[y + var_c].corr(method="pearson"))
corr_p = pd.DataFrame(corr_p.iloc[0, :])
corr_sp = pd.concat([corr_s, corr_p], axis=1)
corr_sp.columns = ["spearman", "pearson"]
corr_sp[(corr_sp["spearman"] <= 0.1) & (corr_sp["pearson"] <= 0.1)]

var_c_s = set(var_c) - set(
    [
        "PromCnt12",
        "PromCnt36",
        "PromCntCard12",
        "DemAge",
        "DemPctVeterans",
        "DemMedIncome",
    ]
)
var_c_s = list(var_c_s)

# 离散型变量筛选：

import statsmodels.stats.anova as anova
from statsmodels.formula.api import ols

for i in var_d:
    formula = "TARGET_D ~ " + str(i)
    print(anova.anova_lm(ols(formula, data=model_data[var_d + ["TARGET_D"]]).fit()))

var_d_s = list(set(var_d) - set(["DemHomeOwner"]))
var_d_s

# ['DemCluster', 'StatusCat96NK', 'DemGender']

# 变量探索与变量变换（E）：

X = model_data[var_c_s + var_d_s].copy()
Y = model_data[y].copy()
model_data[var_c_s + var_d_s].head()

cc = X[var_c_s].describe().T
print(cc)

abs(
    (X[var_c_s].mode().iloc[0,] - X[var_c_s].median())
    / (X[var_c_s].quantile(0.75) - X[var_c_s].quantile(0.25))
)
X["PromCntAll"].hist()
plt.show()

X["DemMedHomeValue"].hist()
plt.show()

cc = X["DemMedHomeValue"].describe().T
print(cc)

cc = X["DemGender"].value_counts()
print(cc)

cc = X["StatusCat96NK"].value_counts()  # 有的水平数量太少
print(cc)

cc = X["DemCluster"].value_counts()[:10]
print(cc)

cc = X["DemMedHomeValue"].replace(0, np.nan, inplace=True)
print(cc)

# 变量的修改阶段（M）：

# 连续变量处理：

cc = 1 - (X.describe().T["count"]) / len(X)
print(cc)

GiftAvgCard36_fill = X["GiftAvgCard36"].median()
DemMedHomeValue_fill = X["DemMedHomeValue"].median()
X["GiftAvgCard36"].fillna(GiftAvgCard36_fill, inplace=True)
X["DemMedHomeValue"].fillna(DemMedHomeValue_fill, inplace=True)
skew_var_x = {}
for i in var_c_s:
    skew_var_x[i] = abs(X[i].skew())
skew = pd.Series(skew_var_x).sort_values(ascending=False)
print(skew)

var_x_ln = skew[skew >= 1].index
print(var_x_ln)

for i in var_x_ln:
    if min(X[i]) <= 0:
        X[i] = np.log(X[i] + abs(min(X[i])) + 0.01)
    else:
        X[i] = np.log(X[i])

skew_var_x = {}
for i in var_c_s:
    skew_var_x[i] = abs(X[i].skew())

skew = pd.Series(skew_var_x).sort_values(ascending=False)
print(skew)

# 分类变量处理：

DemC_group = model_data[["DemCluster", "TARGET_D"]].groupby(
    "DemCluster", as_index=False
)
DemC_C = (
    DemC_group["TARGET_D"]
    .agg({"mean": "mean", "count": "count", "median": "median"})
    .sort_values(["median", "mean"])
)
DemC_C["count_cumsum"] = DemC_C["count"].cumsum()
DemC_C["new_DemCluster"] = DemC_C["count_cumsum"].apply(
    lambda x: x // (len(model_data) / 10) + 1
)
DemC_C["new_DemCluster"] = DemC_C["new_DemCluster"].astype(int)
cc = DemC_C.head()
print(cc)

DemCluster_new_class = DemC_C[["DemCluster", "new_DemCluster"]].set_index("DemCluster")
X["DemCluster"] = X["DemCluster"].map(DemCluster_new_class.to_dict()["new_DemCluster"])
new_DemGender = {"F": 1, "M": 2, "U": 3}
X["DemGender"] = X["DemGender"].map(new_DemGender)
StatusCat96NK_group = model_data[["StatusCat96NK", "TARGET_D"]].groupby(
    "StatusCat96NK", as_index=False
)
StatusCat96NK_class = (
    StatusCat96NK_group["TARGET_D"]
    .agg({"mean": "mean", "count": "count", "median": "median"})
    .sort_values(["median", "mean"])
)
cc = StatusCat96NK_class
print(cc)

new_StatusCat96NK = {"S": 1, "A": 2, "E": 2, "N": 2, "F": 2, "L": 2}
X["StatusCat96NK"] = X["StatusCat96NK"].map(new_StatusCat96NK)
cc = X.head()
print(cc)

# 前向选择法筛选变量:

import statsmodels.formula.api as smf


def forward_selected(data, response):
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = 0.0, 0.0
    while remaining and current_score == best_new_score:
        scores_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {} + 1".format(response, " + ".join(selected + [candidate]))
            score = smf.ols(formula, data).fit().rsquared_adj
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates.pop()
        if current_score < best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
    formula = "{} ~ {} + 1".format(response, " + ".join(selected))
    model = smf.ols(formula, data).fit()
    return selected


XX = pd.concat([X[var_c_s + var_d_s], Y], axis=1)

final_var = forward_selected(XX, "TARGET_D")

var_c_s = list(set(var_c_s) & set(final_var))
print(var_c_s)

var_d_s = list(set(var_d_s) & set(final_var))
print(var_d_s)

model_final = pd.concat([X[var_d_s + var_c_s], Y], axis=1)
cc = model_final.columns
print(cc)

# 建立线性回归模型:

import statsmodels.api as sm
from statsmodels.formula.api import ols

X = model_final.iloc[:, :-1]
Y = model_final.iloc[:, -1]
formula = "TARGET_D ~ " + "+".join(final_var)
donation_model = ols(formula, model_final).fit()
print(donation_model.summary())


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
