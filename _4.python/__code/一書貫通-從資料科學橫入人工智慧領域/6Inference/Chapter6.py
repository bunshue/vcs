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

"""
第6讲 统计推断基础

    数据说明：本数据是地区房价增长率数据
    名称-中文含义
    dis_name-小区名称
    rate-房价同比增长率
"""

house_price_gr = pd.read_csv('house_price_gr.csv', encoding='gbk')
cc = house_price_gr.head()
print(cc)

#6.1 参数估计

#进行描述性统计分析

cc = house_price_gr.describe(include='all')
print(cc)

import seaborn as sns
from scipy import stats

sns.distplot(house_price_gr.rate, kde=True, fit=stats.norm) # Histograph
plt.show()

import statsmodels.api as sm
from matplotlib import pyplot as plt

fig = sm.qqplot(house_price_gr.rate, fit=True, line='45')
fig.show()
plt.show()


house_price_gr.plot(kind='box') # Box Plots
plt.show()

#置信度区间估计

se = house_price_gr.rate.std() / len(house_price_gr) ** 0.5
LB = house_price_gr.rate.mean() - 1.98 * se
UB = house_price_gr.rate.mean() + 1.98 * se
(LB, UB)

# 如果要求任意置信度下的置信区间的话，可以自己编一个函数
def confint(x, alpha=0.05):
    n = len(x)
    xb = x.mean()
    df = n-1
    tmp = (x.std() / n ** 0.5) * stats.t.ppf(1-alpha/2, df)
    return {'Mean': xb, 'Degree of Freedom':df, 'LB':xb-tmp, 'UB':xb+tmp}

confint(house_price_gr.rate, 0.05)

# 或者使用DescrStatsW
d1 = sm.stats.DescrStatsW(house_price_gr.rate)
d1.tconfint_mean(0.05) # 


#6.2 假设检验与单样本T检验
#当年住宅价格的增长率是否超过了10%的阈值

print('t-statistic=%6.4f, p-value=%6.4f, df=%s' %d1.ttest_mean(0.1))

#一般认为FICO高于690的客户信誉较高，请检验该产品的客户整体信用是否高于690

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

#导入数据

camp= pd.read_csv('tele_camp_ok.csv', skipinitialspace=True)
cc = camp.head()
print(cc)

#根据是否入网比较外呼次数

camp['PromCnt12'].groupby(camp['Suc_flag']).describe()

#第一步:方差齐次检验

Suc0 = camp[camp['Suc_flag'] == 0]['PromCnt12']
Suc1 = camp[camp['Suc_flag'] == 1]['PromCnt12']
leveneTestRes = stats.levene(Suc0, Suc1, center='median')
print('w-value=%6.4f, p-value=%6.4f' %leveneTestRes)

#第二步:T-test

stats.stats.ttest_ind(Suc0, Suc1, equal_var=False)
# Or Try: sm.stats.ttest_ind(gender0, gender1, usevar='pooled')

#6.4 方差分析

#单因素方差分析

pd.set_option('display.max_columns', None) # 设置显示所有列
camp.groupby('Class')[['PromCnt12']].describe().T

# 利用回归模型中的方差分析
import statsmodels.api as sm
from statsmodels.formula.api import ols

sm.stats.anova_lm(ols('PromCnt12 ~ C(Class)',data=camp).fit())

#多因素方差分析

# NG
sm.stats.anova_lm(ols('PromCnt12 ~ C(Class)+C(Age_group1)',data=camp).fit())

#6.5 相关分析

#散点图

camp.plot(x='AvgARPU', y='ARPU', kind='scatter')
plt.show()

#相关性分析:“spearman”,“pearson” 和 "kendall"

camp[['AvgARPU', 'ARPU']].corr(method='pearson')

#6.6卡方检验

cross_table = pd.crosstab(camp.Class, columns=camp.Suc_flag)
# Or try this: accepts.pivot_table(index='bankruptcy_ind',columns='bad_ind', values='application_id', aggfunc='count')
cc = cross_table
print(cc)

print('chisq = %6.4f\n p-value = %6.4f\n dof = %i\n expected_freq = %s'  %stats.chi2_contingency(cross_table))

 


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

