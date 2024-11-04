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
camp= pd.read_csv('teleco_camp.csv')

# 数据预处理
camp.dtypes

camp.describe(include='all')

camp['Suc_flag'] = camp['Suc_flag'].astype('category')
camp['Class'] = camp['Class'].astype('category')

#3.1 描述性统计与探索型数据分析

#1.分类变量分析

cc = camp['Suc_flag'].groupby(camp['Suc_flag']).count()
print(cc)

#2.连续变量分析
#2.1.数据的集中趋势 ARPU的均值与中位数

fs = camp['ARPU'] # 可以使用camp.ARPU 
type(fs)

print('mean = %6.4f' %fs.mean())                     # 求fs的均值
print('median = %6.4f' %fs.median() )                # 求fs的中位数
print('quantiles\n', fs.quantile([0.25, 0.5, 0.75])) # 求a的上下四分位数与中位数

fs.plot(kind='hist')
plt.show()

#2.2.数据的离散程度

#print ('mad = %6.4f' %fs.mad())      # 求平均绝对偏差 mad = np.abs(fs - fs.mean()).mean()
print ('range = %6.4f' %(fs.max(skipna=True) - fs.min(skipna=True))) # 求极差
print ('var = %6.4f' %fs.var())   # 求方差
print ('std = %6.4f' %fs.std())   # 求标准差

#2.3.数据的偏度与峰度- ARPU:右偏

plt.hist(fs.dropna(), bins=15)
plt.show()

print ('skewness = %6.4f' %fs.skew(skipna=True))
print ('kurtosis = %6.4f' %fs.kurt(skipna=True))
"""
#2.4.分布- 正态分布模拟函数

from scipy import stats

x = map(lambda x: x / 10., range(-40, 41))
norm = stats.norm.pdf(x, loc=0, scale=1) # 随机正态分布概率密度(均值为0，标准差为1)
plt.plot(x, norm)
plt.show()

points = map(lambda x: x / 10.0, range(-40, 41))
plt.plot(points, stats.norm.cdf(points,loc=0, scale=1)) # 正态分布函数
plt.show()

#卡方分布模拟

x = range(1, 31)
chi = stats.chi2.pdf(x, df=3, loc=0, scale=1) #生成自由度为3的卡方分布概率密度
plt.plot(x, chi)
plt.show()

#t分布模拟

x = np.arange(-4, 4, 0.1)
student_t = stats.t.pdf(x, df=5, loc=0, scale=1)#生成自由度为5的t分布的概率密度值
norm = stats.norm.pdf(x, loc=0, scale=1)
plt.plot(x, student_t, 'b-')
plt.plot(x, norm, 'r--')
plt.show()
"""
#3.2 apply\map\groupby及其它相关

data = pd.DataFrame(data={'a':range(1,11), 'b':np.random.randn(10)})
data.T

data.apply(np.mean) # 等价于data.mean()，是其完整形式

data.apply(lambda x: x.astype('str')).dtypes # DataFrame没有astype方法，只有Series有

(data['a']- data['a'].mean()) / data['a'].std()

data['a'].map(lambda x: (x - data['a'].mean()) / data['a'].std())  # 等价于(data['a']- data['a'].mean()) / data['a'].std()

data['a'].map(lambda x: int(str(x), base=16))  # 不支持“广播”时，可以使用map进行函数映射

#分组-应用/聚合

key = [1, 2] * 5
print(key)

group1, group2 = data.groupby(key) # 使用groupby可按照‘key’进行分组，‘key’需与待分组数据有同样长度
print(group1)
print(group2)

data.groupby(key).aggregate(np.mean) 
# 聚合函数在各分组中进行聚合，是data.groupby(key).mean()的完整形式，可传入函数或字符串(sum/mean/median/std/var等)，也可传入列表

data.groupby(key).agg({'a': 'sum', 'b':'count'}) # agg可以在多列上使用不同的聚合函数

data.groupby(key).transform(np.mean) # 转换函数可在各分组内进行运算，将结果广播到原数据中

data.groupby(key).apply(np.mean) # apply是一般化的‘分组-应用/聚合’函数，更灵活地实现aggregate或transform的功能

#*练习：对camp数据集，按照客户级别汇总ARPU

camp['ARPU'].groupby(camp['Class']).apply(lambda x: x.describe())

camp[['PromCnt12','PromCnt36']].groupby(camp['Suc_flag']).mean()

#crosstab 和pivot_table

pd.crosstab(camp.Suc_flag, camp.Class)

camp.pivot_table(['PromCnt12','PromCnt36'], 
                    index='Suc_flag', columns='Class', aggfunc=np.mean) # index、columns、aggfunc参数均可传入列表

#3.3绘图

#散点图

camp.plot(x='AvgARPU', y='ARPU', kind='scatter') #散点图
plt.text(60, 1100, 'ARPU VS AvgARPU') # 加标签
plt.show()

#柱图/条形图、折线图

data.b.plot(kind='bar') # 柱图
plt.show()

data.b.plot(kind='line') # 折线图
plt.show()

#直方图

camp[['PromCnt12','PromCnt36']].plot(stacked=False, kind='hist', alpha=0.3, bins=20)
camp[['PromCnt12','PromCnt36']].hist(alpha=0.8, bins=20, figsize=(10, 2))

#饼图

gb = camp['Suc_flag'].groupby(camp['Suc_flag']).count()
gb.plot(kind='pie',labels=['Yes', 'No'], colors=['r', 'g'], autopct='%.2f', fontsize=20, figsize=(6, 6))
plt.show()

#箱线图

camp[['PromCnt12','Suc_flag']].boxplot(by='Suc_flag')
plt.show()
 


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

