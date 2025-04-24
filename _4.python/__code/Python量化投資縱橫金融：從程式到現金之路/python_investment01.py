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

from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
'''
pd.set_option("display.max_rows",1000)
pd.set_option("display.max_columns",20)
#pd.set_option('precision',7)
pd.set_option('large_repr', 'truncate')

a=pd.read_csv('data/closeprice.csv',encoding='gbk',dtype={'ticker': str})
print(a)

data = pd.read_csv('data/closeprice.csv',encoding='gbk')
print(data.describe().T)

a=pd.read_csv('data//closeprice.csv',encoding='gbk')
print(a)


b={1:'银行',2:'房地产',4:'医药生物',5:'房地产',6:'采掘',7:'休闲服务',8:'机械设备'}

a['ind']=a.ticker.map(b)
print(a)

data = pd.DataFrame({'group': ['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'], 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
data.sort_values(by=['group','ounces'], ascending=[False, True], inplace=True)
print(data)

data = pd.DataFrame({'k1': ['one'] * 3 + ['two'] * 4, 'k2': [3, 2, 1, 3, 3, 4, 4]})
print(data)

cc = data.drop_duplicates()
print(cc)

cc = data.drop_duplicates(subset=['k1'],keep='last')
print(data)

cc = data[data.duplicated()]
print(data)

a=pd.read_csv('data/closeprice.csv',encoding='gbk')

cc = a.drop(['Unnamed: 0'],axis=1)
print(cc)

cc = a.drop('Unnamed: 0', axis='columns')
print(cc)

cc = a.replace(1,np.nan)
print(cc)

cc = a.rename(columns={'Unnamed: 0':'id'})
print(cc)

a=pd.read_csv('data/closeprice.csv',encoding='gbk')
print(a)

cc = a.loc[:,['ticker','closePrice']]
print(cc)

cc = a.iloc[:4,[1,4]]
print(cc)

cc = a[a.closePrice>10]
print(cc)

cc = a[(a.closePrice>10) & (a.ticker>3)]
print(cc)

cc = a[(a.closePrice>10)*1 + (a.ticker>3)*1==2]
print(cc)

bins=[4,9,10,20,30]
cat=pd.cut(a.closePrice,bins)
print(cat)

cc = pd.value_counts(cat)
print(cc)

group_names = ['low',  'Middle_1', 'Middle_2', 'high']
cc = pd.cut(a.closePrice, bins, labels=group_names)
print(cc)

df = pd.read_csv('data/20170930.csv', dtype={'ticker': str, 'holdingTicker':str,}, encoding='GBK')
df = df[['ticker', 'holdingTicker', 'marketValue', 'industryName1']]
print(df.head())

cc = df[['holdingTicker']].groupby(df['ticker']).count().tail()
print(cc)

cc = df[['holdingTicker']].groupby(df['industryName1']).count().sort_values('holdingTicker', ascending=False).head()
print(cc)

cc = df[['marketValue']].groupby(df['ticker']).sum().sort_values('marketValue', ascending=False).head()
print(cc)

def t_range(arr):
     return arr.max() - arr.min()

cc = df[['marketValue']].groupby(df['ticker']).agg(t_range).head()
print(cc)

cc = df[['marketValue']].groupby(df['ticker']).agg(['sum', 'max', t_range]).head()
print(cc)

cc = df[['marketValue', 'industryName1']].groupby(df['ticker']).agg ({'marketValue':[t_range],  'industryName1':['count']}).head()
print(cc)

cc = df.groupby('ticker').apply(lambda x: x[:3]).head(6)
print(cc)
'''
print("------------------------------------------------------------")  # 60個
#3.3 Scipy的初步使用
print("------------------------------------------------------------")  # 60個

import datetime as dt

data = pd.read_csv('data/data.csv', index_col='Date')
data.index = [dt.datetime.strptime(x, '%Y-%m-%d') for x in data.index]

cc = data.head()
print(cc)

data.plot(figsize=(10, 6))
plt.ylabel('涨跌幅')
show()

import statsmodels.api as sm

x = data['沪深300'].values
X = sm.add_constant(x)  #添加常数项
y = data['中国平安'].values

model = sm.OLS(y, X)
results = model.fit()
cc = results.params
print(cc)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='中国平安-沪深300')
plt.plot(x, results.fittedvalues, 'r--', label='ordinary least square')
plt.legend()
plt.xlabel('沪深300')
plt.ylabel('中国平安')
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

import datetime as dt
import statsmodels.api as sm

factor = np.random.rand(1000, 3)
Factor = sm.add_constant(factor)  #添加常数项
fac1 = factor[:, 0]  #因子1
fac2 = factor[:, 1]  #因子2
fac3 = factor[:, 2]  #因子3
e = np.random.random(1000)  #噪声
port = fac1 * 0.3 + fac2 * 0.7 + fac3 * 0.4 + e  #虚构投资组合及因子权重
model1 = sm.OLS(port, Factor)
results1 = model1.fit()
cc = results1.params
print(cc)

data1 = pd.read_csv('data/data1.csv')
cc = data1.head()
print(cc)

import scipy.interpolate as spi

X = data1.index  #定义数据点
Y = data1.values  #定义数据点
x = np.arange(0, len(data1), 0.15)  #定义观测点

ipo1 = spi.splrep(X,Y,k=1) #k 样条拟合顺序（1<=k<=5）
ipo3 = spi.splrep(X,Y,k=3)

iy1 = spi.splev(x,ipo1)
iy3 = spi.splev(x,ipo3)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,12))
ax1.plot(X, Y, label='沪深300')
ax1.plot(x, iy1, 'r.', label='插值点')
ax1.set_ylim(Y.min() - 10, Y.max() + 10)
ax1.set_ylabel('指数')
ax1.set_title('线性插值')
ax1.legend()
ax2.plot(X, Y, label='沪深300')
ax2.plot(x, iy3, 'r.', label='插值点')
ax2.set_ylim(Y.min() - 10, Y.max() + 10)
ax2.set_ylabel('指数')
ax2.set_title('三次样条插值')
ax2.legend()

show()

data2 = pd.read_csv('data/data2.csv', index_col='Date')
data2.index = [dt.datetime.strptime(x, '%Y-%m-%d') for x in data2.index]
cc = data2.head()
print(cc)

(data2 / data2.iloc[0]*100).plot(figsize=(10,6))
plt.xlabel('股价')
plt.legend(loc='upper left')
plt.grid(True)
show()

log_returns = np.log(data2.pct_change() + 1)
cc = log_returns.head()
print(cc)

log_returns.hist(bins=50, figsize=(10,6), layout=(2, 3))
show()

fig, axes = plt.subplots(3, 2, figsize=(10, 12))
for i in range(0, 3):
    for j in range(0, 2):
        sm.qqplot(log_returns.iloc[:, 2 * i + j].dropna(), line='s', ax=axes[i, j])
        axes[i, j].grid(True)
        axes[i, j].set_title(log_returns.columns[2 * i + j])
        axes[i, j].set_xlabel('理论分位数')
        axes[i, j].set_ylabel('样本分位数')
plt.subplots_adjust(wspace=0.3, hspace=0.4)

show()

cc = log_returns.mean()
print(cc)

number = 10000  #随机数维度
stock_num = len(log_returns.columns)
weights = np.random.rand(number, stock_num)
weights /= np.sum(weights, axis=1).reshape(number, 1)
prets = np.dot(weights, log_returns.mean()) * 252  #计算年化收益率
pvols = np.diag(np.sqrt(np.dot(weights, np.dot(log_returns.cov() * 252, weights.T))))  #计算年化风险

plt.figure(figsize=(10, 6))
plt.scatter(pvols, prets, c=prets / pvols, marker='o')
plt.grid(True)
plt.xlabel('预期波动率')
plt.ylabel('预期收益率')
plt.colorbar(label='夏普率')

show()

import scipy.optimize as sco

def statistics(weights):
    weights = np.array(weights)
    pret = np.sum(log_returns.mean() * weights * 252)
    pvols = np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 252, weights)))
    return np.array([pret, pvols, pret / pvols])

def min_sharpe(weights):
    return -statistics(weights)[2]

cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
bnds = tuple((0, 1) for x in range(stock_num))

opts = sco.minimize(min_sharpe, stock_num * [1 / stock_num], method='SLSQP', bounds=bnds, constraints=cons)
cc = opts['x'].round(3)
print(cc)

cc = statistics(opts['x'].round(3))
print(cc)

def min_volatility(weights):
    return statistics(weights)[1]

opts1 = sco.minimize(min_volatility, stock_num * [1 / stock_num], method='SLSQP', bounds=bnds, constraints=cons)
cc = opts1['x'].round(3)
print(cc)

cc = statistics(opts1['x'].round(3))
print(cc)

def min_return(weights):
    return -statistics(weights)[0]

opts2 = sco.minimize(min_return, stock_num * [1 / stock_num], method='SLSQP', bounds=bnds, constraints=cons)
cc = opts2['x'].round(3)
print(cc)

cc = statistics(opts2['x'].round(3))
print(cc)

trets=np.linspace(0.04, 0.18, 50)
tvols=[]
for tret in  trets:
    cons1=({'type': 'eq', 'fun': lambda x: statistics(x)[0] - tret}, 
          {'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    res=sco.minimize(min_volatility, stock_num * [1 / stock_num], 
                     method='SLSQP', bounds = bnds, constraints = cons1)
    tvols.append(res['fun'])
tvols=np.array(tvols)

plt.figure(figsize=(10,6))
plt.scatter(pvols, prets, 
            c=prets / pvols, marker='o')  
plt.scatter(tvols, trets, 
            c=trets / tvols, marker='x', s=100)  
plt.plot(statistics(opts['x'])[1], statistics(opts['x'])[0],
         '*', markersize=15, label='最大夏普率组合')
plt.plot(statistics(opts1['x'])[1], statistics(opts1['x'])[0], 
         '*', markersize=15, label='最小波动率组合')
plt.plot(statistics(opts2['x'])[1], statistics(opts2['x'])[0], 
         '*', markersize=15, label='最大收益率组合')
plt.grid(True)
plt.xlabel('预期波动率')
plt.ylabel('预期收益率')
plt.colorbar(label='夏普率')
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
#3.5 Seaborn的使用
print("------------------------------------------------------------")  # 60個

import matplotlib as mpl

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

sinplot()

show()

sns.set_style({"font.sans-serif":['Microsoft JhengHei', 'Microsoft JhengHei']})  #显示中文
sinplot()

show()

plt.figure(figsize=(12, 8))
sns.set_context('paper')
plt.subplot(221)
sinplot()
plt.title('paper')
sns.set_context('talk')
plt.subplot(222)
sinplot()
plt.title('talk')
sns.set_context('poster')
plt.subplot(223)
sinplot()
plt.title('poster')
sns.set_context('notebook')
plt.subplot(224)
sinplot()
plt.title('notebook')

show()

plt.figure(figsize=(12, 8))
sns.set_palette("muted")
plt.subplot(221)
sinplot()
plt.title('循环')
sns.set_palette("Blues_d")
plt.subplot(222)
sinplot()
plt.title('渐变（深-浅）')
sns.set_palette("Blues")
plt.subplot(223)
sinplot()
plt.title('渐变（浅-深）')
sns.set_palette("RdBu")
plt.subplot(224)
sinplot()
plt.title('混合（红-蓝）')

show()

size = 1000
rn1 = np.random.standard_normal(size)

sns.set_palette("muted")
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))
ax1.hist(rn1, bins=25)
ax1.set_title('fig1')
sns.histplot(rn1, bins=25, kde=False, ax=ax2)
ax2.set_title('fig2')
sns.histplot(rn1, bins=25, kde=True, ax=ax3)
ax3.set_title('fig3')
sns.histplot(rn1, bins=25, kde=True, rug=True, ax=ax4)
ax4.set_title('fig4')

show()

""" NG
rn2 = pd.read_csv('data/data.csv', index_col='Date')
sns.jointplot(rn2['沪深300'], rn2['中国平安'], size=8)
show()

sns.lmplot('沪深300', '中国平安', data = rn2, size=8)
show()

sns.jointplot(rn2['沪深300'], rn2['中国平安'], kind='reg', size=8)
show()
"""

rn3 = pd.read_csv('data/data2.csv', index_col='Date')  #读取数据
rn3_rets = np.log(rn3.pct_change() + 1)  #计算对数收益率
rn3_rets.index = [str(x)[5 : 7] for x in rn3_rets.index]  #将Date转换为月份
rn3_group = rn3_rets.groupby(rn3_rets.index).sum()  #数据聚合，得到每个月的总收益率
rn3_group.index.name = '月份'
rn3_group.columns.name = '股票'

print(rn3_group)

plt.figure(figsize=(10, 8))
sns.heatmap(rn3_group, annot=True,  linewidths=.5)

show()

sns.pairplot(rn3_rets.dropna())

show()

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


