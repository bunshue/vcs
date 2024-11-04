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

#线性回归

import statsmodels.api as sm
from statsmodels.formula.api import ols

pd.set_option('display.max_columns', None)

#数据准备

tele = pd.read_csv('teleco_camp.csv')
cc = tele.describe(include='all')
print(cc)

#  抽取连续变量及分类变量以便后续使用
all_X = tele.columns[4:]
continuous_X = ['PromCnt12', 'PromCnt36', 'PromCntMsg12', 
                'PromCntMsg36', 'Age', 'AvgARPU', 'AvgHomeValue', 'AvgIncome']
categorical_X = list(set(all_X) - set(continuous_X))

#对字符串变量进行编码

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
tele['Gender'] = le.fit_transform(tele['Gender'])    # 对Gender进行自动编码

tele['HomeOwner'].replace({'H': 0, 'U': 1}, inplace=True)

#按ARPU是否为缺失值将数据分为两部分

arpu_known = tele[tele['ARPU'].notnull()].iloc[:, 3:].copy()
arpu_unknown = tele[tele['ARPU'].isnull()].iloc[:, 3:].copy()

#相关性分析

arpu_known.plot('ARPU', 'AvgARPU', kind='scatter')
plt.show()

cc = arpu_known.corr(method='pearson')
print(cc)

#简单线性回归

lm_s = ols('ARPU ~ AvgARPU', data=arpu_known).fit()
cc = lm_s.summary()
print(cc)

# 多元线性回归

formula = 'ARPU ~' + '+'.join(continuous_X)
lm = ols(formula, data=arpu_known).fit()
cc = lm.summary()
print(cc)

#线性回归的诊断

#残差图

ana1 = lm_s

arpu_known['Pred'] = ana1.predict(arpu_known)
arpu_known['resid'] = ana1.resid
arpu_known.plot('AvgARPU', 'resid',kind='scatter')
plt.show()

#Find outlier

# standardize the resid
resid_mean = arpu_known['resid'].mean(); resid_std = arpu_known['resid'].std()

arpu_known['resid_t'] = (arpu_known['resid'] - resid_mean) / resid_std

cc = arpu_known[abs(arpu_known['resid_t']) > 2].head()
print(cc)


#drop outlier

arpu_known2 = arpu_known[abs(arpu_known['resid_t']) <= 2].copy()
ana2 = ols('ARPU ~ AvgARPU', arpu_known2).fit()
arpu_known2['Pred'] = ana2.predict(arpu_known2)
arpu_known2['resid'] = ana2.resid
arpu_known2.plot('AvgARPU', 'resid', kind='scatter')
plt.show()

cc = ana2.rsquared
print(cc)

# statemodels包提供了更多强影响点判断指标
from statsmodels.stats.outliers_influence import OLSInfluence

cc = OLSInfluence(ana1).summary_frame().head()
print(cc)

#增加连续变量

#多元线性回归的变量筛选

# 定义向前选择法变量筛选函数
def forward_select(data, response):
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = float('inf'), float('inf')
    while remaining:
        aic_with_candidates=[]
        for candidate in remaining:
            formula = "{} ~ {}".format(response,' + '.join(selected + [candidate]))
            aic = ols(formula=formula, data=data).fit().aic
            aic_with_candidates.append((aic, candidate))
        aic_with_candidates.sort(reverse=True)
        best_new_score, best_candidate=aic_with_candidates.pop()
        if current_score > best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
            print ('aic is {},continuing!'.format(current_score))
        else:        
            print ('forward selection over!')
            break
    formula = "{} ~ {} ".format(response,' + '.join(selected))
    print('final formula is {}'.format(formula))
    model = ols(formula=formula, data=data).fit()
    return(selected, model)

candidate_var = list(continuous_X)
candidate_var.append('ARPU')
data_for_select = arpu_known2[candidate_var]

selected_var, lm_m = forward_select(data=data_for_select, response='ARPU')  #  前向法选择变量
print(lm_m.rsquared)

#多重共线性分析


def vif(df, col_i):
    cols = list(df.columns)
    cols.remove(col_i)
    cols_noti = cols
    formula = col_i + '~' + '+'.join(cols_noti)
    r2 = ols(formula, df).fit().rsquared
    return 1. / (1. - r2)

exog = arpu_known2[selected_var]

for i in exog.columns:
    print(i, '\t', vif(df=exog, col_i=i))

#增加分类变量

selected_var.extend(['C(Class)', 'C(Gender)'])
formula2 = 'ARPU ~' + '+'.join(selected_var)
ana3 = ols(formula2, arpu_known2).fit()
cc = ana3.summary()
print(cc)

#增加交互效应

selected_var.append('C(Class):C(Gender)')
formula3 = 'ARPU ~' + '+'.join(selected_var)
ana4 = ols(formula3, arpu_known2).fit()
cc = ana4.summary()
print(cc)

selected_var.remove('C(Gender)')
selected_var.remove('C(Class):C(Gender)')
selected_var.remove('Age')

formula4 = 'ARPU ~' + '+'.join(selected_var)
ana5 = ols(formula4, arpu_known2).fit()
cc = ana5.summary()
print(cc)

#正则算法

#岭回归

reg_var = list(continuous_X)
reg_var.extend(['C(Class)', 'C(Gender)', 'C(Class):C(Gender)', 'C(HomeOwner)'])
formula5 = 'ARPU ~' + '+'.join(reg_var)
lmr = ols(formula5, data=arpu_known2).fit_regularized(alpha=0.01, L1_wt=0)
cc = lmr.summary()
print(cc)
# L1_wt参数为0则使用岭回归，为1使用lasso

#LASSO算法

lml = ols(formula5, data=arpu_known2).fit_regularized(alpha=0.01, L1_wt=0)
cc = lml.summary()
print(cc)

#scikit-learn中正则化参数调优

#哑变量变换

from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder()
dummies = enc.fit_transform(arpu_known2[['Gender', 'HomeOwner', 'Class']]).toarray()

X = arpu_known2[continuous_X].join(pd.DataFrame(dummies, index=arpu_known2.index))
y = arpu_known2[['ARPU', ]]

#搜索最优正则化系数

from sklearn.linear_model import RidgeCV

alphas = np.logspace(-3, 2, 100, base=10)#linspace

rcv = RidgeCV(alphas=alphas, store_cv_values=True) # Search the min MSE by CV
rcv.fit(X, y)

print('The best alpha is {}'.format(rcv.alpha_))
print('The r-square is {}'.format(rcv.score(X,y))) # Default score is rsquared

#预测

cc = rcv.predict(X)[:5]
print(cc)

dummies_new = enc.transform(arpu_unknown[['Gender', 'HomeOwner', 'Class']]).toarray()
X_new = arpu_unknown[continuous_X].join(pd.DataFrame(dummies_new, index=arpu_unknown.index))

cc = rcv.predict(X_new)[:5]
print(cc)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

