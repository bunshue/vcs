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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

'''
from pandas import DataFrame
df = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
print(df)


print (__name__)


if __name__=="__main__":
     print ("It's main")
else:
     print ("It's not main")


import pandas

cc = dir(pandas)
print(cc)


'''


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


import numpy.random as npr

npr.rand(3, 2)

a = 2
b = 4
npr.rand(3, 2) * (b - a) + a

size = 1000
rn1 = npr.rand(size, 2)
rn2 = npr.randn(size)
rn3 = npr.randint(0, 10, size)
rang = [0, 10, 20, 30, 40]
rn4 = npr.choice(rang, size = size)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows = 2, ncols = 2, figsize = (8, 8))
ax1.hist(rn1, bins = 25, stacked = True)
ax1.set_title('rand')
ax1.set_ylabel('frequency')
ax1.grid(True)
ax2.hist(rn2, bins = 25)
ax2.set_title('randn')
ax2.grid(True)
ax3.hist(rn3, bins = 25)
ax3.set_title('randint')
ax3.set_ylabel('frequency')
ax3.grid(True)
ax4.hist(rn4, bins = 25)
ax4.set_title('choice')
ax4.grid(True)

plt.show()

sys.exit()

'''
rn5 = npr.binomial(100, 0.3, size)
rn6 = npr.normal(10, 20, size)
rn7 = npr.chisquare(0.5, size)
rn8 = npr.poisson(2.0, size)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows = 2, ncols = 2, figsize = (10, 10))
ax1.hist(rn5, bins = 25)
ax1.set_title('binomial')
ax1.set_ylabel('frequency')
ax1.grid(True)
ax2.hist(rn6, bins = 25)
ax2.set_title('normal')
ax2.grid(True)
ax3.hist(rn7, bins = 25)
ax3.set_title('chisquare')
ax3.set_ylabel('frequency')
ax3.grid(True)
ax4.hist(rn8, bins = 25)
ax4.set_title('poisson')
ax4.grid(True)

3.2 Pandas的使用

obj = pd.Series([40, 12, -3, 25])

obj

0    40
1    12
2    -3
3    25
dtype: int64

obj[0]

40

obj.index

RangeIndex(start=0, stop=4, step=1)

obj.values

array([40, 12, -3, 25], dtype=int64)

obj = pd.Series([40, 12, -3, 25],index=['a','b','c','d'])

obj

a    40
b    12
c    -3
d    25
dtype: int64

obj['c']

-3

obj[obj>15]

a    40
d    25
dtype: int64

obj.describe()

count     4.000000
mean     18.500000
std      18.339393
min      -3.000000
25%       8.250000
50%      18.500000
75%      28.750000
max      40.000000
dtype: float64

obj.mean()

18.5

obj.to_dict()

{'a': 40, 'b': 12, 'c': -3, 'd': 25}

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

df

	one 	two
a 	1.0 	1.0
b 	2.0 	2.0
c 	3.0 	3.0
d 	NaN 	4.0

pd.set_option("display.max_rows",1000)
pd.set_option("display.max_columns",20)
pd.set_option('precision',7)
pd.set_option('large_repr', 'truncate')

a=pd.read_csv('closeprice.csv',encoding='gbk',dtype={'ticker': str})

a

	Unnamed: 0 	ticker 	secShortName 	tradeDate 	closePrice
0 	0 	000001 	平安银行 	2017-06-20 	9.12
1 	1 	000002 	万科A 	2017-06-20 	21.03
2 	2 	000004 	国农科技 	2017-06-20 	27.03
3 	3 	000005 	世纪星源 	2017-06-20 	5.45
4 	4 	000006 	深振业A 	2017-06-20 	8.87
5 	5 	000007 	全新好 	2017-06-20 	15.87

a.to_excel('closeprice.xls')

data = pd.read_csv('closeprice.csv',encoding='gbk')

data.describe().T

	count 	mean 	std 	min 	25% 	50% 	75% 	max
Unnamed: 0 	6.0 	2.5000000 	1.8708287 	0.00 	1.2500 	2.500 	3.75 	5.00
ticker 	6.0 	4.1666667 	2.3166067 	1.00 	2.5000 	4.500 	5.75 	7.00
closePrice 	6.0 	14.5616667 	8.2950550 	5.45 	8.9325 	12.495 	19.74 	27.03

data.info()

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 5 columns):
Unnamed: 0      6 non-null int64
ticker          6 non-null int64
secShortName    6 non-null object
tradeDate       6 non-null object
closePrice      6 non-null float64
dtypes: float64(1), int64(2), object(2)
memory usage: 320.0+ bytes

a=pd.read_csv('closeprice.csv',encoding='gbk')

a

	Unnamed: 0 	ticker 	secShortName 	tradeDate 	closePrice
0 	0 	1 	平安银行 	2017-06-20 	9.12
1 	1 	2 	万科A 	2017-06-20 	21.03
2 	2 	4 	国农科技 	2017-06-20 	27.03
3 	3 	5 	世纪星源 	2017-06-20 	5.45
4 	4 	6 	深振业A 	2017-06-20 	8.87
5 	5 	7 	全新好 	2017-06-20 	15.87

b={1:'银行',2:'房地产',4:'医药生物',5:'房地产',6:'采掘',7:'休闲服务',8:'机械设备'}

a['ind']=a.ticker.map(b)

a

	Unnamed: 0 	ticker 	secShortName 	tradeDate 	closePrice 	ind
0 	0 	1 	平安银行 	2017-06-20 	9.12 	银行
1 	1 	2 	万科A 	2017-06-20 	21.03 	房地产
2 	2 	4 	国农科技 	2017-06-20 	27.03 	医药生物
3 	3 	5 	世纪星源 	2017-06-20 	5.45 	房地产
4 	4 	6 	深振业A 	2017-06-20 	8.87 	采掘
5 	5 	7 	全新好 	2017-06-20 	15.87 	休闲服务

data = pd.DataFrame({'group': ['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'], 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
data.sort_values(by=['group','ounces'], ascending=[False, True], inplace=True)

data

	group 	ounces
6 	c 	3.0
7 	c 	5.0
8 	c 	6.0
3 	b 	6.0
4 	b 	7.5
5 	b 	8.0
1 	a 	3.0
0 	a 	4.0
2 	a 	12.0

data = pd.DataFrame({'k1': ['one'] * 3 + ['two'] * 4, 'k2': [3, 2, 1, 3, 3, 4, 4]})

data

	k1 	k2
0 	one 	3
1 	one 	2
2 	one 	1
3 	two 	3
4 	two 	3
5 	two 	4
6 	two 	4

data.drop_duplicates()

	k1 	k2
0 	one 	3
1 	one 	2
2 	one 	1
3 	two 	3
5 	two 	4

data.drop_duplicates(subset=['k1'],keep='last')

	k1 	k2
2 	one 	1
6 	two 	4

data[data.duplicated()]

	k1 	k2
4 	two 	3
6 	two 	4

a=pd.read_csv('closeprice.csv',encoding='gbk')

a.drop(['Unnamed: 0'],axis=1)

	ticker 	secShortName 	tradeDate 	closePrice
0 	1 	平安银行 	2017-06-20 	9.12
1 	2 	万科A 	2017-06-20 	21.03
2 	4 	国农科技 	2017-06-20 	27.03
3 	5 	世纪星源 	2017-06-20 	5.45
4 	6 	深振业A 	2017-06-20 	8.87
5 	7 	全新好 	2017-06-20 	15.87

a.drop('Unnamed: 0', axis='columns')

	ticker 	secShortName 	tradeDate 	closePrice
0 	1 	平安银行 	2017-06-20 	9.12
1 	2 	万科A 	2017-06-20 	21.03
2 	4 	国农科技 	2017-06-20 	27.03
3 	5 	世纪星源 	2017-06-20 	5.45
4 	6 	深振业A 	2017-06-20 	8.87
5 	7 	全新好 	2017-06-20 	15.87

a.replace(1,np.nan)

	Unnamed: 0 	ticker 	secShortName 	tradeDate 	closePrice
0 	0.0 	NaN 	平安银行 	2017-06-20 	9.12
1 	NaN 	2.0 	万科A 	2017-06-20 	21.03
2 	2.0 	4.0 	国农科技 	2017-06-20 	27.03
3 	3.0 	5.0 	世纪星源 	2017-06-20 	5.45
4 	4.0 	6.0 	深振业A 	2017-06-20 	8.87
5 	5.0 	7.0 	全新好 	2017-06-20 	15.87

a.rename(columns={'Unnamed: 0':'id'})

	id 	ticker 	secShortName 	tradeDate 	closePrice
0 	0 	1 	平安银行 	2017-06-20 	9.12
1 	1 	2 	万科A 	2017-06-20 	21.03
2 	2 	4 	国农科技 	2017-06-20 	27.03
3 	3 	5 	世纪星源 	2017-06-20 	5.45
4 	4 	6 	深振业A 	2017-06-20 	8.87
5 	5 	7 	全新好 	2017-06-20 	15.87

a=pd.read_csv('closeprice.csv',encoding='gbk')
a

	Unnamed: 0 	ticker 	secShortName 	tradeDate 	closePrice
0 	0 	1 	平安银行 	2017-06-20 	9.12
1 	1 	2 	万科A 	2017-06-20 	21.03
2 	2 	4 	国农科技 	2017-06-20 	27.03
3 	3 	5 	世纪星源 	2017-06-20 	5.45
4 	4 	6 	深振业A 	2017-06-20 	8.87
5 	5 	7 	全新好 	2017-06-20 	15.87

a.loc[:,['ticker','closePrice']]

	ticker 	closePrice
0 	1 	9.12
1 	2 	21.03
2 	4 	27.03
3 	5 	5.45
4 	6 	8.87
5 	7 	15.87

a.iloc[:4,[1,4]]

	ticker 	closePrice
0 	1 	9.12
1 	2 	21.03
2 	4 	27.03
3 	5 	5.45

a.ix[:4,['ticker','closePrice']]


See the documentation here:
http://pandas.pydata.org/pandas-docs/stable/indexing.html#deprecate_ix
  """Entry point for launching an IPython kernel.

	ticker 	closePrice
0 	1 	9.12
1 	2 	21.03
2 	4 	27.03
3 	5 	5.45
4 	6 	8.87

a[a.closePrice>10]

	Unnamed: 0 	ticker 	secShortName 	tradeDate 	closePrice
1 	1 	2 	万科A 	2017-06-20 	21.03
2 	2 	4 	国农科技 	2017-06-20 	27.03
5 	5 	7 	全新好 	2017-06-20 	15.87

a[(a.closePrice>10) & (a.ticker>3)]

	Unnamed: 0 	ticker 	secShortName 	tradeDate 	closePrice
2 	2 	4 	国农科技 	2017-06-20 	27.03
5 	5 	7 	全新好 	2017-06-20 	15.87

a[(a.closePrice>10)*1 + (a.ticker>3)*1==2]

	Unnamed: 0 	ticker 	secShortName 	tradeDate 	closePrice
2 	2 	4 	国农科技 	2017-06-20 	27.03
5 	5 	7 	全新好 	2017-06-20 	15.87

bins=[4,9,10,20,30]
cat=pd.cut(a.closePrice,bins)
cat

0     (9, 10]
1    (20, 30]
2    (20, 30]
3      (4, 9]
4      (4, 9]
5    (10, 20]
Name: closePrice, dtype: category
Categories (4, interval[int64]): [(4, 9] < (9, 10] < (10, 20] < (20, 30]]

pd.value_counts(cat)

(20, 30]    2
(4, 9]      2
(10, 20]    1
(9, 10]     1
Name: closePrice, dtype: int64

group_names = ['low',  'Middle_1', 'Middle_2', 'high']

pd.cut(a.closePrice, bins, labels=group_names)

0    Middle_1
1        high
2        high
3         low
4         low
5    Middle_2
Name: closePrice, dtype: category
Categories (4, object): [Middle_1 < Middle_2 < high < low]

df = pd.read_csv('20170930.csv', dtype={'ticker': str, 'holdingTicker':str,}, encoding='GBK')
df = df[['ticker', 'holdingTicker', 'marketValue', 'industryName1']]
df.head()

	ticker 	holdingTicker 	marketValue 	industryName1
0 	000001 	002236 	237401519.41 	电子
1 	000001 	000568 	216279076.20 	食品饮料
2 	000001 	300156 	160320000.00 	公用事业
3 	000001 	603799 	153879981.00 	有色金属
4 	000001 	600056 	151963791.62 	医药生物

df[['holdingTicker']].groupby(df['ticker']).count().tail()

	holdingTicker
ticker 	
740101 	10
750001 	10
750005 	10
762001 	10
770001 	10

df[['holdingTicker']].groupby(df['industryName1']).count().sort_values('holdingTicker', ascending=False).head()

	holdingTicker
industryName1 	
银行 	4666
电子 	3850
食品饮料 	3539
非银金融 	3306
医药生物 	2950

df[['marketValue']].groupby(df['ticker']).sum().sort_values('marketValue', ascending=False).head()

	marketValue
ticker 	
510050 	1.8185643e+10
001683 	9.2226736e+09
001772 	7.9835313e+09
150201 	7.6500959e+09
150200 	7.6500959e+09

def t_range(arr):
     return arr.max() - arr.min()

df[['marketValue']].groupby(df['ticker']).agg(t_range).head()

	marketValue
ticker 	
000001 	134945823.19
000003 	1820900.00
000004 	1820900.00
000005 	0.00
000007 	745400.00

df[['marketValue']].groupby(df['ticker']).agg(['sum', 'max', t_range]).head()

	marketValue
	sum 	max 	t_range
ticker 			
000001 	1.5172431e+09 	237401519.41 	134945823.19
000003 	5.3427065e+06 	1978000.00 	1820900.00
000004 	5.3427065e+06 	1978000.00 	1820900.00
000005 	1.2771440e+06 	1277144.00 	0.00
000007 	8.2668800e+06 	1287000.00 	745400.00

df[['marketValue', 'industryName1']].groupby(df['ticker']).agg ({'marketValue':[t_range],  'industryName1':['count']}).head()

	marketValue 	industryName1
	t_range 	count
ticker 		
000001 	134945823.19 	10
000003 	1820900.00 	4
000004 	1820900.00 	4
000005 	0.00 	1
000007 	745400.00 	10

df.groupby('ticker').apply(lambda x: x[:3]).head(6)

		ticker 	holdingTicker 	marketValue 	industryName1
ticker 					
000001 	0 	000001 	002236 	237401519.41 	电子
1 	000001 	000568 	216279076.20 	食品饮料
2 	000001 	300156 	160320000.00 	公用事业
000003 	10 	000003 	600622 	1978000.00 	房地产
11 	000003 	600884 	1930106.52 	电子
12 	000003 	600036 	1277500.00 	银行
3.3 Scipy的初步使用

import datetime as dt

plt.rcParams['font.sans-serif']=['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False  #用来正常显示负号

data = pd.read_csv('data.csv', index_col='Date')
data.index = [dt.datetime.strptime(x, '%Y-%m-%d') for x in data.index]

data.head()

	沪深300 	中国平安
2015-06-23 	0.03214 	0.0496
2015-06-24 	0.01965 	0.0052
2015-06-25 	-0.03557 	-0.0287
2015-06-26 	-0.07868 	-0.0605
2015-06-29 	-0.03336 	-0.0119

data.plot(figsize=(10, 6))
plt.ylabel('涨跌幅')

<matplotlib.text.Text at 0x21ab8007ac8>

import statsmodels.api as sm

x = data['沪深300'].values
X = sm.add_constant(x)  #添加常数项
y = data['中国平安'].values

model = sm.OLS(y, X)
results = model.fit()
results.params

array([ 0.00095063,  0.80946537])

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='中国平安-沪深300')
plt.plot(x, results.fittedvalues, 'r--', label='ordinary least square')
plt.legend()
plt.xlabel('沪深300')
plt.ylabel('中国平安')
plt.grid(True)

import numpy.random as npr

factor = npr.rand(1000, 3)
Factor = sm.add_constant(factor)  #添加常数项
fac1 = factor[:, 0]  #因子1
fac2 = factor[:, 1]  #因子2
fac3 = factor[:, 2]  #因子3
e = npr.random(1000)  #噪声
port = fac1 * 0.3 + fac2 * 0.7 + fac3 * 0.4 + e  #虚构投资组合及因子权重
model1 = sm.OLS(port, Factor)
results1 = model1.fit()
results1.params

array([ 0.53531625,  0.22141331,  0.70291227,  0.40377034])

data1 = pd.read_csv('data1.csv')
data1.head()

	沪深300
0 	3424.1940
1 	3424.1669
2 	3485.6581
3 	3480.4345
4 	3492.8845

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

<matplotlib.legend.Legend at 0x21ab81b1908>

data2 = pd.read_csv('data2.csv', index_col='Date')
data2.index = [dt.datetime.strptime(x, '%Y-%m-%d') for x in data2.index]
data2.head()

	平安银行 	万科A 	格力电器 	华东医药 	东方雨虹 	宇通客车
2011-01-04 	5.491 	7.418 	7.004 	15.301 	9.705 	5.859
2011-01-05 	5.460 	7.444 	6.934 	16.316 	9.945 	5.748
2011-01-06 	5.419 	7.452 	6.957 	16.175 	10.017 	6.224
2011-01-07 	5.624 	7.494 	6.823 	15.583 	9.664 	6.305
2011-01-10 	5.477 	7.368 	6.726 	15.037 	9.462 	6.299

(data2 / data2.iloc[0]*100).plot(figsize=(10,6))
plt.xlabel('股价')
plt.legend(loc='upper left')
plt.grid(True)

log_returns = np.log(data2.pct_change() + 1)
log_returns.head()

	平安银行 	万科A 	格力电器 	华东医药 	东方雨虹 	宇通客车
2011-01-04 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN
2011-01-05 	-0.0056616 	0.0034989 	-0.0100446 	0.0642280 	0.0244287 	-0.0191270
2011-01-06 	-0.0075375 	0.0010741 	0.0033115 	-0.0086794 	0.0072137 	0.0795608
2011-01-07 	0.0371319 	0.0056202 	-0.0194491 	-0.0372863 	-0.0358760 	0.0129302
2011-01-10 	-0.0264856 	-0.0169564 	-0.0143186 	-0.0356667 	-0.0211239 	-0.0009521

log_returns.hist(bins=50, figsize=(10,6), layout=(2, 3))

fig, axes = plt.subplots(3, 2, figsize=(10, 12))
for i in range(0, 3):
    for j in range(0, 2):
        sm.qqplot(log_returns.iloc[:, 2 * i + j].dropna(), line='s', ax=axes[i, j])
        axes[i, j].grid(True)
        axes[i, j].set_title(log_returns.columns[2 * i + j])
        axes[i, j].set_xlabel('理论分位数')
        axes[i, j].set_ylabel('样本分位数')
plt.subplots_adjust(wspace=0.3, hspace=0.4)

log_returns.mean()

平安银行    0.0001880
万科A     0.0000825
格力电器    0.0007412
华东医药    0.0005016
东方雨虹    0.0002330
宇通客车    0.0005662
dtype: float64

number = 10000  #随机数维度
stock_num = len(log_returns.columns)
weights = npr.rand(number, stock_num)
weights /= np.sum(weights, axis=1).reshape(number, 1)
prets = np.dot(weights, log_returns.mean()) * 252  #计算年化收益率
pvols = np.diag(np.sqrt(np.dot(weights, np.dot(log_returns.cov() * 252, weights.T))))  #计算年化风险

plt.figure(figsize=(10, 6))
plt.scatter(pvols, prets, c=prets / pvols, marker='o')
plt.grid(True)
plt.xlabel('预期波动率')
plt.ylabel('预期收益率')
plt.colorbar(label='夏普率')

<matplotlib.colorbar.Colorbar at 0x21abb9835f8>

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
opts['x'].round(3)

array([ 0.   ,  0.   ,  0.521,  0.227,  0.   ,  0.251])

statistics(opts['x'].round(3))

array([ 0.16181374,  0.23682582,  0.68326054])

def min_volatility(weights):
    return statistics(weights)[1]

opts1 = sco.minimize(min_volatility, stock_num * [1 / stock_num], method='SLSQP', bounds=bnds, constraints=cons)
opts1['x'].round(3)

array([ 0.109,  0.199,  0.171,  0.255,  0.044,  0.221])

statistics(opts1['x'].round(3))

array([ 0.10758601,  0.21346307,  0.50400293])

def min_return(weights):
    return -statistics(weights)[0]

opts2 = sco.minimize(min_return, stock_num * [1 / stock_num], method='SLSQP', bounds=bnds, constraints=cons)
opts2['x'].round(3)

array([ 0.,  0.,  1.,  0.,  0.,  0.])

statistics(opts2['x'].round(3))

array([ 0.18677101,  0.31284775,  0.59700289])

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

<matplotlib.legend.Legend at 0x21aba896cf8>

3.5 Seaborn的使用

import matplotlib as mpl

plt.rcParams['font.sans-serif']=['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False  #用来正常显示负号

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

sinplot()

sns.set_style({"font.sans-serif":['Microsoft YaHei', 'SimHei']})  #显示中文
sinplot()

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

<matplotlib.text.Text at 0x21abd01b470>

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

<matplotlib.text.Text at 0x21abd1d1240>

import numpy.random as npr

size = 1000
rn1 = npr.standard_normal(size)

sns.set_palette("muted")
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))
ax1.hist(rn1, bins=25)
ax1.set_title('fig1')
sns.distplot(rn1, bins=25, kde=False, ax=ax2)
ax2.set_title('fig2')
sns.distplot(rn1, bins=25, kde=True, ax=ax3)
ax3.set_title('fig3')
sns.distplot(rn1, bins=25, kde=True, rug=True, ax=ax4)
ax4.set_title('fig4')

<matplotlib.text.Text at 0x21abd5794e0>

rn2 = pd.read_csv('data.csv', index_col='Date')

sns.jointplot(rn2['沪深300'], rn2['中国平安'], size=8)

<seaborn.axisgrid.JointGrid at 0x21abd35aeb8>

sns.lmplot('沪深300', '中国平安', data = rn2, size=8)

<seaborn.axisgrid.FacetGrid at 0x21abbe707b8>

sns.jointplot(rn2['沪深300'], rn2['中国平安'], kind='reg', size=8)

<seaborn.axisgrid.JointGrid at 0x21abec84f60>

rn3 = pd.read_csv('data2.csv', index_col='Date')  #读取数据
rn3_rets = np.log(rn3.pct_change() + 1)  #计算对数收益率
rn3_rets.index = [str(x)[5 : 7] for x in rn3_rets.index]  #将Date转换为月份
rn3_group = rn3_rets.groupby(rn3_rets.index).sum()  #数据聚合，得到每个月的总收益率
rn3_group.index.name = '月份'
rn3_group.columns.name = '股票'

rn3_group

股票 	平安银行 	万科A 	格力电器 	华东医药 	东方雨虹 	宇通客车
月份 						
01 	0.2232092 	0.0401755 	-0.0051509 	-0.1014440 	-0.1956839 	0.3263316
02 	0.1292791 	-0.0203437 	0.2687811 	0.0349293 	0.0352995 	0.1846648
03 	-0.2420345 	0.1394470 	0.0789179 	-0.0064670 	-0.3323231 	-0.1962433
04 	0.1371384 	0.0575301 	0.0218907 	-0.0882394 	0.1600025 	-0.0152448
05 	0.0633844 	0.1952293 	0.0880885 	0.1976538 	0.3433602 	0.0156413
06 	-0.3340361 	-0.1583731 	-0.0647462 	0.0218633 	0.0232485 	0.0565611
07 	-0.0273451 	-0.0205192 	0.1285418 	0.2108194 	-0.0206509 	-0.0820939
08 	0.0103378 	-0.1467318 	-0.1603021 	0.0537295 	0.0856823 	-0.0496981
09 	-0.0138445 	-0.1041274 	0.0161983 	0.0052901 	-0.0724317 	-0.0571362
10 	0.2178464 	0.0954068 	0.2129939 	0.0894890 	0.2496864 	-0.0893401
11 	-0.1341805 	-0.1248136 	-0.0975519 	-0.1418785 	0.0432905 	0.1675221
12 	0.1249945 	0.1149980 	0.1223092 	0.1370343 	-0.1277578 	0.2050415

plt.figure(figsize=(10, 8))
sns.heatmap(rn3_group, annot=True,  linewidths=.5)

<matplotlib.axes._subplots.AxesSubplot at 0x21abf6a60b8>

sns.pairplot(rn3_rets.dropna())

<seaborn.axisgrid.PairGrid at 0x21abe947278>

Scikit-learn的初步使用

import sklearn
sklearn.__version__

'0.18.1'

import sklearn 
import re
from sklearn import cross_validation
import sklearn.tree as tree

data=pd.read_excel('loan.xlsx')
target=data['Type']
data.drop('Type',axis='columns',inplace=True)
train_data,test_data,train_target,test_target=cross_validation. train_test_split(data,target,test_size=0.4,train_size=0.6,random_state=12345)
clf_1=tree.DecisionTreeClassifier(criterion='entropy')
clf_1.fit(train_data,train_target)
train_est=clf_1.predict(train_data)
train_est_p=clf_1.predict_proba(train_data)[:,1]

test_est=clf_1.predict(test_data)
test_est

array([1, 1, 1, 1, 0, 0], dtype=int64)

from sklearn import metrics
print(metrics.accuracy_score(test_target, test_est))

0.5

print(metrics.confusion_matrix(test_target, test_est))

[[2 3]
 [0 1]]

import sklearn.svm as svm
clf_2=svm.SVC()
clf_2.fit(train_data,train_target)
train_est=clf_2.predict(train_data)
test_est=clf_2.predict(test_data)

from sklearn import metrics
print(metrics.accuracy_score(test_target, test_est))
print(metrics.confusion_matrix(test_target, test_est))

0.666666666667
[[3 2]
 [0 1]]

from sklearn.naive_bayes import GaussianNB
clf_3=GaussianNB()
clf_3.fit(train_data,train_target)
train_est=clf_3.predict(train_data)
test_est=clf_3.predict(test_data)

from sklearn import metrics
print(metrics.accuracy_score(test_target, test_est))
print(metrics.confusion_matrix(test_target, test_est))

0.5
[[2 3]
 [0 1]]

from sklearn.neural_network import MLPClassifier
clf_4=MLPClassifier()
clf_4.fit(train_data,train_target)
train_est=clf_4.predict(train_data)
test_est=clf_4.predict(test_data)


from sklearn import metrics
print(metrics.accuracy_score(test_target, test_est))
print(metrics.confusion_matrix(test_target, test_est))

1.0
[[5 0]
 [0 1]]

from sklearn.metrics import accuracy_score

y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]
print(accuracy_score(y_true, y_pred))
print(accuracy_score(y_true, y_pred, normalize=False))

0.5
2

from sklearn.metrics import confusion_matrix

y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
confusion_matrix(y_true, y_pred)

y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]
confusion_matrix(y_true, y_pred, labels=["ant", "bird", "cat"])

from sklearn import metrics

y = np.array([1, 1, 2, 2])
scores = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)
print(fpr)
print(tpr)
print(thresholds)

[ 0.   0.5  0.5  1. ]
[ 0.5  0.5  1.   1. ]
[ 0.8   0.4   0.35  0.1 ]

plt.plot(fpr,tpr)

[<matplotlib.lines.Line2D at 0x21ac03074a8>]

from sklearn.metrics import recall_score
y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]
recall_score(y_true, y_pred, average='macro')  # doctest: +ELLIPSIS

0.33333333333333331

recall_score(y_true, y_pred, average='micro')

0.33333333333333331

recall_score(y_true, y_pred, average='weighted')

0.33333333333333331

recall_score(y_true, y_pred, average=None)

array([ 1.,  0.,  0.])

3.7 SQLAlchemy与常用数据库的连接

# 本节代码需要连接数据库，如果你电脑上没有数据库，运行会报错

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

engine = create_engine('mysql://root:123@127.0.0.1:3306/test?charset=utf8') 

---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-48-a66d0a2a0ca0> in <module>()
----> 1 engine = create_engine('mysql://root:123@127.0.0.1:3306/test?charset=utf8')


ModuleNotFoundError: No module named 'MySQLdb'

pd.read_sql('select * from data', engine)

pd.read_sql('data',engine)

df = pd.DataFrame([[5, '永辉超市', 11], [6, '华夏幸福', 34]], 
      columns=['ID', 'stockname', 'price'], 
      index=range(2))
df

df.to_sql('data', engine, index=False, if_exists='append')

pd.read_sql('data',engine)

df.to_sql('t_data', engine, index=False, if_exists='append')

pd.read_sql('t_data',engine)

df1 = pd.DataFrame(np.arange(20000).reshape(10000, 2), index=range(10000), columns=['key', 'value'])
r = df1.to_dict('records')

df1.to_sql('f_data', engine, index=False, if_exists='append')
pd.read_sql('f_data', engine).tail()

#下面这两句话就完成了ORM映射，Base.classes.XXXX就是映射的类  
# Base.metadata.tables['XXX']就是相应的表  
Base = automap_base()  
Base.prepare(engine, reflect = True)  
f_data = Base.metadata.tables['f_data']

engine.execute(f_data.insert(), r)  
pd.read_sql('f_data', engine).tail()




'''

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

