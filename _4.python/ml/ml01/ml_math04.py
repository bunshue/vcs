"""



"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
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

import time
import matplotlib
import seaborn as sns

#from __future__ import print_function

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_regression

X,y =make_regression(n_samples=100, n_features=3)

print(X.shape ,y.shape)

y=y.reshape((-1,1))

#(100, 3) (100,)

plt.figure(figsize=(9,4))

plt.plot(y,alpha=0.5,linewidth=3)

plt.show()

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X,y)

y_pred_sk = model.predict(X)

plt.figure(figsize=(9,4))

plt.plot(y, color = 'r')
plt.plot(y,alpha=0.8,linewidth=5 )

plt.plot(y_pred_sk, color = 'g')
plt.plot(y_pred_sk ,linewidth=1)

plt.legend()

plt.show()

def gd(X, y, theta, l_rate, iterations): 

    cost_history = [0] * iterations

    m = X.shape[0]

    for epoch in range(iterations):

        y_hat = X.dot(theta)

        loss = y_hat - y

        gradient = X.T.dot(loss)/m

        theta = theta - l_rate * gradient

        cost = np.dot(loss.T,loss)

        cost_history[epoch] = cost[0,0]

    return theta, cost_history

def sgd(X,y,theta, l_rate,iterations):

    cost_history =[0] * iterations

    for epoch in range(iterations):

        for i,row in enumerate(X):

            yhat = np.dot(row,theta)

            loss = yhat[0] - y[i]          

            theta = theta - l_rate  * loss * row.reshape((-1,1))

            cost_history[epoch] += loss ** 2

    return theta,cost_history

def predict(X,theta):

    return np.dot(X,theta)

theta = np.random.rand(X.shape[1],1)

iterations = 100

l_rate = 0.1

theta,cost_history = gd(X,y,theta,l_rate,iterations)

print(theta.T)

#array([[ 1.12259549, 64.22439151, 84.34968956]])

y_predict = predict(X,theta)

y_predict = predict(X,theta)

plt.figure(figsize=(9,4))

plt.plot(y, color = 'r')
plt.plot(y,alpha=0.3,linewidth=5)
plt.plot(y_predict, color = 'g')
plt.plot(y_predict,linewidth= 2)
plt.show()

print(model.coef_)

#array([[48.54597102, 82.31351886,  8.52184984]])

print('------------------------------------------------------------')	#60個

np.random.seed(3)
num_pos = 500
 
subset1 = np.random.multivariate_normal([0, 0], [[1, 0.6],[0.6, 1]], num_pos)
subset2 = np.random.multivariate_normal([0.5, 4], [[1, 0.6],[0.6, 1]], num_pos)
 
X = np.vstack((subset1, subset2))
y = np.hstack((np.zeros(num_pos), np.ones(num_pos)))
 
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()

print('------------------------------------------------------------')	#60個

from sklearn import linear_model

clf = linear_model.LogisticRegression()

clf.fit(X, y)

"""
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
,          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
,          penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
,          verbose=0, warm_start=False)
"""

y_pred = clf.predict(X)

print(np.sum(y_pred.reshape(-1,1)==y.reshape(-1,1))*1.0/len(y))

#0.99

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y,y_pred))

#[[495   5]
# [  5 495]]


print('------------------------------------------------------------')	#60個

#绘制分类边界

def plot_decision_boundary(pred_func, X, y, title):
    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole grid (get class for each grid point)
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # print(Z)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z,alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=40, alpha=0.8)
    plt.title(title)
    plt.show()

plot_decision_boundary(lambda x: clf.predict(x), X, y, "logistic regression prediction")

print('------------------------------------------------------------')	#60個

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def log_likelihood(X, y, theta):
    scores = np.dot(X, theta)
    ll = np.sum(  y * scores - np.log(1 + np.exp(scores)) )
    return ll

def logistic_regression(X,y,l_rate,iterations,add_intercept = True):
    if add_intercept:
        intercept = np.ones((X.shape[0], 1))
        X = np.hstack((intercept, X))
        
    theta = np.zeros(X.shape[1]).reshape(-1,1)
    y=y.reshape(-1,1)
    accu_history = [0] * iterations
    ll_history = [0.0] * iterations
    for epoch in range(iterations):
        x_theta = np.dot(X, theta)
        y_hat = sigmoid(x_theta)
        error = y  - y_hat 
        gradient = np.dot(X.T, error)
        theta = theta + l_rate*gradient
        preds = np.round( y_hat )      
        
        accu = np.sum(preds==y)*1.0/len(y)
        accu_history[epoch]=accu

        if( epoch % 100 == 0):
            print("After iter {}; accuracy: {}".format(epoch +1,  accu))
    return theta,accu_history

theta,accu = logistic_regression(X,y,1,2000)

print(accu)

print('------------------------------------------------------------')	#60個

plt.style.use('bmh')
colors = ['#A60628','#467821']
plt.cmap = matplotlib.colors.ListedColormap(colors)

matplotlib.rcParams['figure.figsize'] = (10.0, 6.0) 

np.random.seed(3)

num_pos = 500

# Bivariate normal distribution mean [0, 0] [0.5, 4], with a covariance matrix

subset1 = np.random.multivariate_normal([0, 0], [[1, 0.6],[0.6, 1]], num_pos)

subset2 = np.random.multivariate_normal([0.5, 4], [[1, 0.6],[0.6, 1]], num_pos)

X = np.vstack((subset1, subset2))

y = np.hstack((np.zeros(num_pos), np.ones(num_pos)))

plt.scatter(X[:, 0], X[:, 1], c=y,cmap=plt.cmap,marker='o',s=40)

plt.show()

from sklearn import linear_model

clf = linear_model.LogisticRegression()
clf.fit(X, y)
print(clf.intercept_, clf.coef_, clf.classes_)
#(array([-5.7268742]), array([[-1.43492343,  3.15471817]]), array([0., 1.]))

y_pred = clf.predict(X)
print(y_pred.shape)
print(np.sum(y_pred.reshape(-1,1)==y.reshape(-1,1))*1.0/len(y))

#(1000L,)
#0.99

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y,y_pred))
sns.heatmap(confusion_matrix(y,y_pred))
plt.show()
"""
[[495   5]

 [  5 495]]
"""

#绘制分类边界
plt.style.use('bmh')
def plot_decision_boundary(pred_func, X, y, title):
    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole grid (get class for each grid point)
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # print(Z)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z,alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=40, alpha=0.8,cmap=plt.cmap)
    plt.title(title)
    plt.show()

# run on the training dataset with predict function

plot_decision_boundary(lambda x: clf.predict(x), X, y, "logistic regression prediction")

plt.show()

"""
d:\Anaconda2\lib\site-packages\numpy\ma\core.py:6442: MaskedArrayFutureWarning: In the future the default for ma.maximum.reduce will be axis=0, not the current None, to match np.maximum.reduce. Explicitly pass 0 or None to silence this warning.

  return self.reduce(a)

d:\Anaconda2\lib\site-packages\numpy\ma\core.py:6442: MaskedArrayFutureWarning: In the future the default for ma.minimum.reduce will be axis=0, not the current None, to match np.minimum.reduce. Explicitly pass 0 or None to silence this warning.

  return self.reduce(a)
"""

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def log_likelihood(X, y, theta):
    scores = np.dot(X, theta)
    ll = np.sum(  y * scores - np.log(1 + np.exp(scores)) )
    return ll

def logistic_regression(X,y,l_rate,iterations,add_intercept = True):
    if add_intercept:
        intercept = np.ones((X.shape[0], 1))
        X = np.hstack((intercept, X))
    theta = np.zeros(X.shape[1]).reshape(-1,1)
    y=y.reshape(-1,1)
    accu_history = [0] * iterations
    ll_history = [0.0] * iterations
    for epoch in range(iterations):
        x_theta = np.dot(X, theta)
        y_hat = sigmoid(x_theta)
        error = y  - y_hat 
        gradient = np.dot(X.T, error)
        theta = theta + l_rate*gradient
        preds = np.round( y_hat )      

        accu = np.sum(preds==y)*1.0/len(y)
        accu_history[epoch]=accu

        if( epoch % 5 == 0):
            print("After iter {}; accuracy: {}".format(epoch +1,  accu))

    return theta,accu_history

theta,accu = logistic_regression(X, y, 1, 500)

print(theta)

"""
array([[-599.88926069],
,       [-181.5414528 ],
,       [ 328.95859873]])
"""
print(accu)

print('------------------------------------------------------------')	#60個

"""
探索性数据分析（EDA）

EDA指对已有的数据用可视化等手段探索数据的结构和规律的一种数据分析方法，其目的是最大化对数据的直觉，完成这个事情的方法是结合统计学的图形以各种形式展现出来。

在深入机器学习或统计建模之前，EDA是一个重要的步骤，这是因为它提供了为现有问题开发适当模型并正确解释其结果所需的来龙去脉。

EDA通常涉及以下几种方法的组合：

.原始数据集中每个字段的单变量可视化和汇总统计

.数据集中每个变量与感兴趣目标变量之间的关系的双变量可视化和汇总统计

.多元可视化以了解数据中不同字段之间的交互作用

.降维以了解数据,通过将数据折叠成几个小数据点让观察值聚类成有区别的小组，可以更容易地识别行为模式

"""

import scipy.stats as stats
import sklearn.linear_model as linear_model
# import xgboost as xgb
# from sklearn.cross_validation import KFold
# from IPython.display import HTML, display
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# pd.options.display.max_rows = 1000
# pd.options.display.max_columns = 20

print('------------------------------------------------------------')	#60個

train = pd.read_csv('data/houseprice.csv')
print(train.head(3))

print('------------------------------------------------------------')	#60個

print(u'训练数据集基本信息')

# print(train.info())

print(train.shape)

#训练数据集基本信息
#(1460, 81)

#1.1 首先，区分出数据中的数值型变量和类别型变量
#数值型变量

quantitative = [f for f in train.columns if train.dtypes[f] != 'object']
quantitative.remove('SalePrice')
quantitative.remove('Id')

#类别型变量

qualitative = [f for f in train.columns if train.dtypes[f] == 'object']

ccs = ['FullBath', 'HalfBath', 'TotRmsAbvGrd', 'Fireplaces', 'GarageYrBlt', 'GarageCars','OverallQual']
for col in ccs:
    if col in quantitative:
        quantitative.remove(col)
    if not col in qualitative:
        qualitative.append(col)

print(u'训练集样本数量：{}'.format(train.shape[0]))
print(u'数值型变量共有：{}'.format(len(quantitative)))
print(u'类别型变量共有：{}'.format(len(qualitative)))

"""
训练集样本数量：1460
数值型变量共有：29
类别型变量共有：50
"""
#1.2查看缺失值的分布情况

missing = train.isnull().sum()/train.shape[0]
print(missing.head(3))

missing = missing[missing > 0]
print(u'有缺失值的变量共有：{}'.format(len(missing)))

missing.sort_values(inplace=True)
print(u'缺失率超过50%的有{}个'.format(len(missing[missing>=0.5])))

print(missing[missing>=0.5])

missing.plot.bar(figsize=(6,4))

plt.show()
"""
Id            0.0
MSSubClass    0.0
MSZoning      0.0
dtype: float64
有缺失值的变量共有：19
缺失率超过50%的有4个
Fence          0.807534
Alley          0.937671
MiscFeature    0.963014
PoolQC         0.995205
dtype: float64
"""

#可以直接删除这几个变量

missing_cols = missing[missing>=0.5].index.tolist()

for col in missing_cols :
    if col in quantitative: 
        quantitative.remove(col)
    if col in qualitative:
        qualitative.remove(col)

print(u'数值型变量共有：{}'.format(len(quantitative)))
print(u'类别型变量共有：{}'.format(len(qualitative)))        

#数值型变量共有：29
#类别型变量共有：46

#2 数值型变量
#2.1 查看目标变量saleprice是否服从正态分布

import scipy.stats as st

y = train['SalePrice']

plt.figure(1)
sns.distplot(y,kde=False)
plt.show()

plt.figure(2)
plt.title('Johnson SU')
sns.distplot(y, kde=True, fit=st.johnsonsu)
plt.show()

plt.figure(3)
plt.title('Normal')
sns.distplot(y, kde=False, fit=st.norm)
plt.show()

plt.figure(4)
plt.title('Log Normal')
sns.distplot(y, kde=False, fit=st.lognorm)
plt.show()

#另一种查看是否服从正态分布的可视化方法
sns.distplot(train['SalePrice'], fit=st.norm)
plt.show()

res = st.probplot(train['SalePrice'], plot=plt)
plt.show()

#把房价做对数变换后再看
SalePrice_log = np.log(train['SalePrice'])
#transformed histogram and normal probability plot
sns.distplot(SalePrice_log, fit=st.norm)
plt.show()


res = st.probplot(SalePrice_log, plot=plt)
print(res)

plt.show()


"""
((array([-3.30513952, -3.04793228, -2.90489705, ...,  2.90489705,
,          3.04793228,  3.30513952]),
,  array([ 10.46024211,  10.47194981,  10.54270639, ...,  13.34550693,
,          13.5211395 ,  13.53447303])),
, (0.39826223081618845, 12.024050901109383, 0.99537614756366088))

显然，房价本身不服从正态分布，是不能直接用来做回归建模的。但是经过对数转换之后，就好了很多。
对于其它的数值型变量，也同样要做分布的正态性检验.
检验方法就用：夏皮罗-威尔克(Shapiro-Wilk)法检验数据正态性,即W检验。
"""

check_normality = lambda x: stats.shapiro(x.fillna(0))[1] < 0.01

normal = pd.DataFrame(train[quantitative])
normal = normal.apply(check_normality)
print(normal.sort_values(ascending=False).head(4))

normal = normal<0.01
print(not normal.any())

"""
YrSold          True
LowQualFinSF    True
LotFrontage     True
LotArea         True
dtype: bool
True

可以发现所有的数值型变量都没能通过正态性分布检验，都需要做转换。
我们可以把所有的数值型变量的分布曲线都画出来，从可视化角度进一步验证这个判断
"""

f = pd.melt(train, value_vars=quantitative)
g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False)
g = g.map(sns.distplot, "value")
plt.show()

df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})
print(df)

pd.melt(df, id_vars=['A'], value_vars=['B', 'C'])
print(df)

#看起来TotalBsmtSF, KitchenAbvGr, LotFrontage, LotArea这几个变量似乎更适合做些变型，以使其服从正态分布。
#2.2 异常值分析
#对saleprice做标准化后再看

saleprice_scaled = StandardScaler().fit_transform(train['SalePrice'][:,np.newaxis]);
low_range = saleprice_scaled[saleprice_scaled[:,0].argsort()][:10]
high_range= saleprice_scaled[saleprice_scaled[:,0].argsort()][-10:]
print('outer range (low) of the distribution:')
print(low_range)
print('\nouter range (high) of the distribution:')
print(high_range)

"""
outer range (low) of the distribution:

[[-1.83870376]

 [-1.83352844]

 [-1.80092766]

 [-1.78329881]

 [-1.77448439]

 [-1.62337999]

 [-1.61708398]

 [-1.58560389]

 [-1.58560389]

 [-1.5731    ]]



outer range (high) of the distribution:

[[ 3.82897043]

 [ 4.04098249]

 [ 4.49634819]

 [ 4.71041276]

 [ 4.73032076]

 [ 5.06214602]

 [ 5.42383959]

 [ 5.59185509]

 [ 7.10289909]

 [ 7.22881942]]

d:\Anaconda2\lib\site-packages\sklearnutils\validation.py:420: DataConversionWarning: Data with input dtype int64 was converted to float64 by StandardScaler.
  warnings.warn(msg, DataConversionWarning)

d:\Anaconda2\lib\site-packages\sklearnutils\validation.py:420: DataConversionWarning: Data with input dtype int64 was converted to float64 by StandardScaler.
  warnings.warn(msg, DataConversionWarning)
"""

#低房价并没有太多异常，但是高房价有两个超过了7，虽然不一定是异常值，但是要小心
#2.3 查看数值型变量和待预测变量之间的相关性
#常用pearson相关系数，它是用有前提条件，并且是有局限的——判断线性相关，非线性相关它是无能为力的。
#Spearman相关系数 vs pearson相关系数的优点：对于数据分布没有要求。也叫秩和。

def spearman(frame, features):
    spr = pd.DataFrame()
    spr['feature'] = features
    spr['spearman'] = [frame[f].corr(frame['SalePrice'], 'spearman') for f in features]
    spr = spr.sort_values('spearman')
    plt.figure(figsize=(6, 0.2*len(features)))
    sns.barplot(data=spr, y='feature', x='spearman', orient='h')
    return spr

features = quantitative

spr = spearman(train, features)
plt.show()


#删除相关系数小于0.3的变量

print(u'数值型变量共有：{}'.format(len(quantitative)))
print(u'类别型变量共有：{}'.format(len(qualitative))) 

for col in spr[abs(spr['spearman'])<0.3].feature:
    if col in quantitative:
        quantitative.remove(col)

print(u'数值型变量共有：{}'.format(len(quantitative)))
print(u'类别型变量共有：{}'.format(len(qualitative))) 

"""
数值型变量共有：29
类别型变量共有：46
数值型变量共有：12
类别型变量共有：46
"""

#2.4 用散点图观察数值型变量之间的关系

#scatterplot

from copy import copy

sns.set(font_scale=2)
cols1 = copy(quantitative)
cols1.append('SalePrice')
#plt.figure('a')
sns.pairplot(train[cols1].fillna(0.), height = 2.5)
plt.show()

#scatterplot

sns.set(font_scale=2)

cols1 = copy(quantitative[:6])

cols1.append('SalePrice')

#plt.figure('b')

sns.pairplot(train[cols1].fillna(0.), height = 2.5)

cols2 =copy(quantitative[6:])

cols2.append('SalePrice')

#plt.figure('c')

sns.pairplot(train[cols2].fillna(0.), height = 2.5)

plt.show()

"""
3.类别型变量

对于类别型的变量，要观察目标变量（sale_price）在类别的各个取值上的分布情况；用分组箱线图

对于类别型变量的缺失值，不再用0填充，而是用一个特殊的值'Missing'填充。
"""

for c in qualitative:
    train[c] = train[c].astype('category')
    if train[c].isnull().any():
        train[c] = train[c].cat.add_categories(['MISSING'])
        train[c] = train[c].fillna('MISSING')

def boxplot(x, y, **kwargs):
    sns.boxplot(x=x, y=y)
    x=plt.xticks(rotation=90)

f = pd.melt(train, id_vars=['SalePrice'], value_vars=qualitative)
#g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False, size=5)
g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False)
g = g.map(boxplot, "value", "SalePrice")

plt.show()

"""
看起来像LotConfig、LandSlope这样的变量，对于房价的影响似乎不大。 Neighborhood对房价有影响。 然后每个类别的不同子类之间看起来似乎也有差别。 overallQual的值太多。

具体到一个分类指标和数值型变量之间的相关关系，我们可以用方差分析进行检查。
3.2 方差分析
"""

def anova(frame):
    anv = pd.DataFrame()
    anv['feature'] = qualitative
    pvals = []
    for c in qualitative:
        samples = []
        for cls in frame[c].unique():
            s = frame[frame[c] == cls]['SalePrice'].values
            samples.append(s)
        pval = stats.f_oneway(*samples)[1]
        pvals.append(pval)
    anv['pval'] = pvals
    return anv.sort_values('pval')

a = anova(train)
a['disparity'] = np.log(1./a['pval'].values)
sns.barplot(data=a, x='feature', y='disparity')
x=plt.xticks(rotation=90)
plt.show()


"""
这里我们用了方差分析，来看每一个类别变量和预测变量Sale_price之间是否有相关关系。

因为我们最后得到了个p值，p>0.05说明样本的分组之间没有显著性差异，

p值越小说明差异越显著。

因为我们想用一个类似于“变异度”的指标——“差异度”，我们希望这个指标越大，说明差异越明显。也就是想要一个同向变化的指标，所以对p值取了个倒数。仅此而已。
3.3 对于这些分类变量的每个值做正确编码

另一种编码方式是OneHotEncoding或者dummy
"""

def encode(frame, feature):
    ordering = pd.DataFrame()
    ordering['val'] = frame[feature].unique()
    ordering.index = ordering.val
    ordering['spmean'] = frame[[feature, 'SalePrice']].groupby(feature).mean()['SalePrice']
    ordering = ordering.sort_values('spmean')
    ordering['ordering'] = range(1, ordering.shape[0]+1)
    ordering = ordering['ordering'].to_dict()

    for cat, o in ordering.items():
        frame.loc[frame[feature] == cat, feature+'_E'] = o

qual_encoded = []
for q in qualitative:  
    encode(train, q)
    qual_encoded.append(q+'_E')

print(qual_encoded)

"""
['MSZoning_E', 'Street_E', 'LotShape_E', 'LandContour_E', 'Utilities_E', 'LotConfig_E', 'LandSlope_E', 'Neighborhood_E', 'Condition1_E', 'Condition2_E', 'BldgType_E', 'HouseStyle_E', 'RoofStyle_E', 'RoofMatl_E', 'Exterior1st_E', 'Exterior2nd_E', 'MasVnrType_E', 'ExterQual_E', 'ExterCond_E', 'Foundation_E', 'BsmtQual_E', 'BsmtCond_E', 'BsmtExposure_E', 'BsmtFinType1_E', 'BsmtFinType2_E', 'Heating_E', 'HeatingQC_E', 'CentralAir_E', 'Electrical_E', 'KitchenQual_E', 'Functional_E', 'FireplaceQu_E', 'GarageType_E', 'GarageFinish_E', 'GarageQual_E', 'GarageCond_E', 'PavedDrive_E', 'SaleType_E', 'SaleCondition_E', 'FullBath_E', 'HalfBath_E', 'TotRmsAbvGrd_E', 'Fireplaces_E', 'GarageYrBlt_E', 'GarageCars_E', 'OverallQual_E']
"""
print(train.head(3))

"""
, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
	Id	MSSubClass	MSZoning	LotFrontage	LotArea	Street	Alley	LotShape	LandContour	Utilities	...	PavedDrive_E	SaleType_E	SaleCondition_E	FullBath_E	HalfBath_E	TotRmsAbvGrd_E	Fireplaces_E	GarageYrBlt_E	GarageCars_E	OverallQual_E
0	1	60	RL	65.0	8450	Pave	NaN	Reg	Lvl	AllPub	...	3.0	5.0	5.0	3.0	3.0	8.0	1.0	86.0	3.0	7.0
1	2	20	RL	80.0	9600	Pave	NaN	Reg	Lvl	AllPub	...	3.0	5.0	5.0	3.0	2.0	5.0	2.0	57.0	3.0	6.0
2	3	60	RL	68.0	11250	Pave	NaN	IR1	Lvl	AllPub	...	3.0	5.0	5.0	3.0	3.0	5.0	2.0	91.0	3.0	7.0
,

3 rows × 127 columns
,

"""

print(train['GarageQual_E'].value_counts())

"""
4.0    1311
,2.0      81
,3.0      48
,5.0      14
,6.0       3
,1.0       3
,Name: GarageQual_E, dtype: int64

3.4.查看衍生变量和房价的Spearman相关性

对于相关性的检测我们使用的是Spearman correlation，这种检验方法的好处是即使是非线性相关也能检测出来。
"""

sns.set(font_scale=1.2)
def spearman(frame, features):
    spr = pd.DataFrame()
    spr['feature'] = features
    spr['spearman'] = [frame[f].corr(frame['SalePrice'], 'spearman') for f in features]
    spr = spr.sort_values('spearman')
    plt.figure(figsize=(6, 0.2*len(features)))
    sns.barplot(data=spr, y='feature', x='spearman', orient='h')

features =  qual_encoded
spearman(train, features)
plt.show()

"""
显然，OverallQual和房价的关系最明显。房子的邻居和位置看起来也是有影响的。
3.5 观察变量之间的相关性

回归模型对于变量共线的容忍度差，所以，我们需要考虑变量之间的相关性。用相关系数矩阵的热力图即可。
"""

sns.set(font_scale=1)

plt.figure(1)

corr = train[quantitative+['SalePrice']].corr('spearman')

sns.heatmap(corr,cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10})

plt.show()

# from functools import partial
# # my_heatmap=partial(sns.heatmap,cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)

plt.figure(2)
corr = train[qual_encoded+['SalePrice']].corr()
sns.heatmap(corr,cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10})

plt.show()

plt.figure(3)
corr = pd.DataFrame(np.zeros([len(quantitative)+1, len(qual_encoded)+1]), index=quantitative+['SalePrice'], columns=qual_encoded+['SalePrice'])
for q1 in quantitative+['SalePrice']:
    for q2 in qual_encoded+['SalePrice']:
        corr.loc[q1, q2] = train[q1].corr(train[q2])

sns.heatmap(corr,cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10})

plt.show()

"""
3.6 观察所有变量（包括衍生变量）和目标变量之间的关系

现在所有类别型变量也做了重新编码，编码成数值型。所有所有的特征都可以看作是数值型的了。于是，我们可以再次全景式观察变量和目标变量之间的关系。
"""

def pairplot(x, y, **kwargs):
    ax = plt.gca()
    ts = pd.DataFrame({'time': x, 'val': y})
    ts = ts.groupby('time').mean()
    ts.plot(ax=ax)
    plt.xticks(rotation=90)

#画散点图
sns.set(style="ticks", color_codes=True)

f = pd.melt(train, id_vars=['SalePrice'], value_vars=quantitative+qual_encoded)
#g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False, size=5)
g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False)
g = g.map(pairplot, "value", "SalePrice")

plt.show()

"""
看起来，YearBuild、1stFlrSF, 2ndFlrSF, Neighborhood_E There are lots of nonlinearities this may be the cause why some variables wont be selected by Lasso/Lars. Some factors like YearBuilt, 1stFlrSF, 2ndFlrSF, Neighborhood_E look like they would benefit from adding quadratic term to regression. But on the other hand this will most probably provoke overfit.

观察的结果提示我们，有些变量可以尝试做些变换，比如平方变换。
4.高级内容

考虑数据本身是否分群，如果分群，就可以用分段回归。

接下来，考虑是否可以分段进行回归。

我们把房价200000作为分界点，之下的作为普通住宅，之上的作为豪宅，然后看看在这样分开后，那些数值型变量的均值有多大差异。
"""

features = quantitative
standard = train[train['SalePrice'] < 200000]
pricey = train[train['SalePrice'] >= 200000]

diff = pd.DataFrame()
diff['feature'] = features
diff['difference'] = [(pricey[f].fillna(0.).mean() - standard[f].fillna(0.).mean())/(standard[f].fillna(0.).mean())
                      for f in features]

sns.barplot(data=diff, x='feature', y='difference')
x=plt.xticks(rotation=90)

print(diff)

plt.show()

"""
, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
	feature	difference
0	MSSubClass	-0.150366
1	LotFrontage	0.238321
2	LotArea	0.536645
3	OverallQual	0.361440
4	OverallCond	-0.047635
5	YearBuilt	0.015026
6	YearRemodAdd	0.010197
7	MasVnrArea	2.029480
8	BsmtFinSF1	0.729316
9	BsmtFinSF2	-0.023328
10	BsmtUnfSF	0.410808
11	TotalBsmtSF	0.515235
12	1stFlrSF	0.396664
13	2ndFlrSF	0.978444
14	LowQualFinSF	-0.298300
15	GrLivArea	0.512153
16	BsmtFullBath	0.577215
17	BsmtHalfBath	-0.487756
18	FullBath	0.424714
19	HalfBath	0.684120
20	BedroomAbvGr	0.092859
21	KitchenAbvGr	-0.050115
22	TotRmsAbvGrd	0.257338
23	Fireplaces	1.102258
24	GarageYrBlt	0.090733
25	GarageCars	0.550690
26	GarageArea	0.596397
27	WoodDeckSF	0.950341
28	OpenPorchSF	1.314906
29	EnclosedPorch	-0.479096
30	3SsnPorch	0.881312
31	ScreenPorch	0.623489
32	PoolArea	2.213669
33	MiscVal	-0.559517
34	MoSold	0.052589
35	YrSold	-0.000021
,

我们用tnse方法，把每个高维样本映射到二维平面上的点。

然后我们对样本做标准化处理，处理之后做PCA，提取前30个主成分。也就是把样本的特征降维到30个特征。

对这30个特征的样本聚类，聚成5类。

在把这5类用可视化的方法会出来，看看是否有聚集趋势。
"""

features = quantitative + qual_encoded
model = TSNE(n_components=2, random_state=0, perplexity=50)
X = train[features].fillna(0.).values
tsne = model.fit_transform(X)

std = StandardScaler()
s = std.fit_transform(X)
pca = PCA(n_components=40)
pca.fit(s)
pc = pca.transform(s)
kmeans = KMeans(n_clusters=5)
kmeans.fit(pc)

fr = pd.DataFrame({'tsne1': tsne[:,0], 'tsne2': tsne[:, 1], 'cluster': kmeans.labels_})
sns.lmplot(data=fr, x='tsne1', y='tsne2', hue='cluster', fit_reg=False)

plt.show()

print(np.sum(pca.explained_variance_ratio_))

"""
0.846903058622

看起来聚集趋势并不明显，所以分段回归的意义似乎不大。

另外40个主成分能解释84%的方差。
"""

y = train['SalePrice'].values
def johnson(y):
    gamma, eta, epsilon, lbda = stats.johnsonsu.fit(y)
    yt = gamma + eta*np.arcsinh((y-epsilon)/lbda)
    return yt, gamma, eta, epsilon, lbda

def johnson_inverse(y, gamma, eta, epsilon, lbda):
    return lbda*np.sinh((y-gamma)/eta) + epsilon

yt, g, et, ep, l = johnson(y)
yt2 = johnson_inverse(yt, g, et, ep, l)

plt.figure(1)
sns.distplot(yt)

plt.figure(2)
sns.distplot(yt2)

plt.show()

#5.最后建模

def error(actual, predicted):
    actual = np.log(actual)
    predicted = np.log(predicted)
    return np.sqrt(np.sum(np.square(actual-predicted))/len(actual))

def log_transform(feature):
    train[feature] = np.log1p(train[feature].values)

def quadratic(feature):
    train[feature+'2'] = train[feature]**2

#下面这些特征做log转化    
log_transform('GrLivArea')
log_transform('1stFlrSF')
log_transform('2ndFlrSF')
log_transform('TotalBsmtSF')
log_transform('LotArea')
log_transform('LotFrontage')
log_transform('KitchenAbvGr')
log_transform('GarageArea')

#下面这些特征取平方转换
#quadratic('OverallQual') fail
quadratic('YearBuilt')
quadratic('YearRemodAdd')
quadratic('TotalBsmtSF')
quadratic('2ndFlrSF')
quadratic('Neighborhood_E')
quadratic('RoofMatl_E')
quadratic('GrLivArea')

qdr = ['OverallQual2', 'YearBuilt2', 'YearRemodAdd2', 'TotalBsmtSF2',
        '2ndFlrSF2', 'Neighborhood_E2', 'RoofMatl_E2', 'GrLivArea2']

#下面这些特征做二值化
train['HasBasement'] = train['TotalBsmtSF'].apply(lambda x: 1 if x > 0 else 0)
train['HasGarage'] = train['GarageArea'].apply(lambda x: 1 if x > 0 else 0)
train['Has2ndFloor'] = train['2ndFlrSF'].apply(lambda x: 1 if x > 0 else 0)
train['HasMasVnr'] = train['MasVnrArea'].apply(lambda x: 1 if x > 0 else 0)
train['HasWoodDeck'] = train['WoodDeckSF'].apply(lambda x: 1 if x > 0 else 0)
train['HasPorch'] = train['OpenPorchSF'].apply(lambda x: 1 if x > 0 else 0)
train['HasPool'] = train['PoolArea'].apply(lambda x: 1 if x > 0 else 0)
train['IsNew'] = train['YearBuilt'].apply(lambda x: 1 if x > 2000 else 0)

boolean = ['HasBasement', 'HasGarage', 'Has2ndFloor', 'HasMasVnr', 'HasWoodDeck',
            'HasPorch', 'HasPool', 'IsNew']

features = quantitative + qual_encoded + boolean + qdr
lasso = linear_model.LassoLarsCV(max_iter=10000)

""" NG
# sklearn中要求X，y都是矩阵形式，而不是数据框
X = train[features].fillna(0.).values
Y = train['SalePrice'].values

lasso.fit(X, np.log(Y))

#反log1p变换
Ypred = np.exp(lasso.predict(X))
print(error(Y, Ypred))

"""


"""

d:\Anaconda2\lib\site-packages\sklearn\linear_model\least_angle.py:334: ConvergenceWarning: Early stopping the lars path, as the residues are small and the current value of alpha is no longer well controlled. 87 iterations, alpha=8.170e-04, previous alpha=2.386e-06, with an active set of 70 regressors.

  ConvergenceWarning)

d:\Anaconda2\lib\site-packages\sklearn\linear_model\least_angle.py:334: ConvergenceWarning: Early stopping the lars path, as the residues are small and the current value of alpha is no longer well controlled. 79 iterations, alpha=6.065e-04, previous alpha=1.923e-06, with an active set of 70 regressors.

  ConvergenceWarning)

0.12548614477031952

​"""

print('作業完成')

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個








