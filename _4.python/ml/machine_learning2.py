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

import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

print("------------------------------------------------------------")  # 60個

from common1 import *

# import tensorflow as tf
import joblib
import pickle
import matplotlib
import matplotlib as mpl

import sklearn
import sklearn.linear_model
from sklearn import metrics
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

# from imblearn.metrics import classification_report_imbalanced
from sklearn.model_selection import cross_val_score

# 載入迴歸常見的評估指標
from sklearn.metrics import mean_squared_error  # 均方誤差 Mean Squared Error (MSE)
from sklearn.metrics import mean_absolute_error  # 平均絕對誤差 Mean Absolute Error (MAE)
from sklearn.metrics import r2_score  # R-Squared擬合度, 決定係數
from sklearn.metrics import accuracy_score  # 正解率
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve  # ROC曲線, AUC
from sklearn.metrics import roc_auc_score
from sklearn.metrics import auc
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score  # 適合率
from sklearn.metrics import recall_score  # 再現率
from sklearn.metrics import f1_score  # F値
from sklearn.metrics import ConfusionMatrixDisplay

from sklearn.datasets import make_blobs  # 生成分類資料
from sklearn.datasets import make_moons  # 生成非線性資料 上/下弦月資料
from sklearn.datasets import make_classification
from sklearn.datasets import make_hastie_10_2
from sklearn.datasets import make_circles

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


def show():
    return
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 搬到 獨立小程式

"""
X = np.array([i * np.pi / 180 for i in range(0, 370, 10)])
#y = np.sin(X) + np.random.normal(0, 0.15, len(X))
y = np.sin(X)

data = pd.DataFrame(np.column_stack([X, y]), columns = ['x', 'y'])
#data.head(10)
print(data)
plt.scatter(data['x'], data['y'], s = 30)

show()

for i in range(2, 16):
    colname = 'x_%d'%i      
    data[colname] = data['x'] ** i

tt = data.head()
print(tt)

print('------------------------------')	#30個


def linear_regression(data, power, models_to_plot):
    print('power =', power)
    #initialize predictors:
    predictors = ['x']
    if power >= 2:
        predictors.extend(['x_%d'%i for i in range(2, power + 1)])
    
    # 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
    linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機
    
    linear_regression.fit(data[predictors],data['y'])  # 學習訓練.fit
    
    y_pred = linear_regression.predict(data[predictors])  # 預測.predict
    
    #Return the result in pre-defined format
    rss = sum((y_pred-data['y']) ** 2)
    ret = [rss]
    ret.extend([linear_regression.intercept_])
    ret.extend(linear_regression.coef_)
    
    #Check if a plot is to be made for the entered power
    if power in models_to_plot:
        print(power)
        print(models_to_plot[power])
        plt.subplot(models_to_plot[power])
        plt.tight_layout()
        plt.plot(data['x'], y_pred, lw = 3)
        plt.plot(data['x'], data['y'], '.')
        plt.title('Plot for power: %d , RSS: %.2f' % (power, rss))
    
    return ret

#Initialize a dataframe to store the results:
col = ['rss','intercept'] + ['coef_x_%d' % i for i in range(1, 16)]
ind = ['model_pow_%d' % i for i in range(1, 16)]

coef_matrix_simple = pd.DataFrame(index = ind, columns = col)
print('1111')
print(coef_matrix_simple)

#Define the powers for which a plot is required:
models_to_plot = {1:231,3:232,6:233,9:234,12:235,15:236}

#Iterate through all powers and assimilate results
for i in range(1,16):
    print("i =", i)
    coef_matrix_simple.iloc[i-1,0:i+2] = linear_regression(data, power=i, models_to_plot=models_to_plot)

show()

print('------------------------------')	#30個

#Set the display format to be scientific for ease of analysis
pd.options.display.float_format = '{:,.2g}'.format

print('2222')
print(coef_matrix_simple)

print('------------------------------')	#30個

# Ridge Regression 嶺迴歸

#L2 Normalization Ridge Regression

def ridge_regression(data, predictors, alpha, models_to_plot={}):
    #ridgereg = Ridge(alpha=alpha,normalize=True)
    ridgereg = Ridge(alpha=alpha)
    ridgereg.fit(data[predictors],data['y'])  # 學習訓練.fit
    y_pred = ridgereg.predict(data[predictors])  # 預測.predict
    
    #Return the result in pre-defined format
    rss = sum((y_pred-data['y'])**2)
    ret = [rss]
    ret.extend([ridgereg.intercept_])
    ret.extend(ridgereg.coef_)


    #Check if a plot is to be made for the entered alpha
    if alpha in models_to_plot:
        plt.subplot(models_to_plot[alpha])
        plt.tight_layout()
        plt.plot(data['x'],y_pred,lw=3)
        plt.plot(data['x'],data['y'],'.')
        plt.title('Plot for alpha: %.3g ,RSS : %.2f'%(alpha,rss))
    return ret


#Initialize predictors to be set of 15 powers of x
predictors=['x']
predictors.extend(['x_%d'%i for i in range(2,16)])

#Set the different values of alpha to be tested
alpha_ridge = [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2, 1, 5, 10, 20]

#Initialize the dataframe for storing coefficients.
col = ['rss','intercept'] + ['coef_x_%d'%i for i in range(1,16)]
ind = ['alpha_%.2g'%alpha_ridge[i] for i in range(0,10)]
coef_matrix_ridge = pd.DataFrame(index=ind, columns=col)

models_to_plot = {1e-15:231, 1e-10:232, 1e-4:233, 1e-3:234, 1e-2:235, 5:236}
for i in range(10):
    coef_matrix_ridge.iloc[i,] = ridge_regression(data, predictors, alpha_ridge[i], models_to_plot)

show()        

print('------------------------------')	#30個

pd.options.display.float_format = '{:,.2g}'.format
tt = coef_matrix_ridge

print(tt)

print('------------------------------')	#30個

#有多少個系數為0

coef_matrix_ridge.apply(lambda x: sum(X.values==0),axis=1)#maybe X

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD

corpus = ["Python is popular in machine learning",
         "Distributed system is important in big data analysis",
        "Machine learning is theoretical foundation of data mining",
        "Learning Python is fun",
        "Playing soccer is fun",
        "Many data scientists like playing soccer",
        "Chinese men's soccer team failed again",
        "Thirty two soccer teams enter World Cup finals"]

vectorizer = CountVectorizer(min_df=1, stop_words="english")
data = vectorizer.fit_transform(corpus)
vectorizer.get_feature_names_out()

tt = pd.DataFrame(data.toarray(), index=corpus, columns=vectorizer.get_feature_names_out()).head(10)
print(tt)

print('------------------------------')	#30個

#Singular value decomposition and LSA
model = TruncatedSVD(2)
data_n = model.fit_transform(data)
data_n = Normalizer(copy=False).fit_transform(data_n)
print(data_n)

tt = pd.DataFrame(data_n, index = corpus, columns = ["component_1", "component_2"])
print(tt)

xs = data_n[:,0]
ys = data_n[:,1]

plt.figure(figsize=(4,4))

ax = plt.gca()
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])

plt.scatter(xs, ys)
plt.xlabel('First principal component')
plt.ylabel('Second principal component')
plt.title('Plot of points agains LSA principal components')

show()

print('------------------------------')	#30個

similarity = np.asarray(np.asmatrix(data_n) * np.asmatrix(data_n).T)
tt = pd.DataFrame(similarity, index = corpus, columns = corpus).head(10)
print(tt)

print(similarity)
 
sns.heatmap(similarity, cmap = 'Reds')

show()

print(pd.DataFrame(model.components_,index=['component_1','component_2'],columns=vectorizer.get_feature_names_out()).T)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
print('房價, 共 1460 筆資料 81欄位')

import scipy.stats as stats

train = pd.read_csv(u'data/houseprice.csv') # 共 1460 筆資料 81欄位
print(len(train))
print(train.shape)
print(train.head(3))

y = train['SalePrice']

sns.histplot(y)
plt.xlabel('售價區間')
plt.ylabel('賣出件數')
plt.title('統計 售價區間 / 賣出件數')
show()

#另一種查看是否服從正態分布的可視化方法
import scipy.stats as st

res = st.probplot(y, plot=plt)
plt.ylabel('售價區間')
plt.xlabel('賣出件數')
plt.title('統計 售價區間 / 賣出件數')
show()

sns.distplot(y,kde=False)
plt.xlabel('售價區間')
plt.ylabel('賣出件數')
plt.title('統計 售價區間 / 賣出件數')
show()

sns.distplot(y, kde=True, fit=st.johnsonsu)
plt.title('使用 Johnson SU')
show()

sns.distplot(y, kde=False, fit=st.norm)
plt.title('使用 Normal')
show()

sns.distplot(y, kde=False, fit=st.lognorm)
plt.title('使用 Log Normal')
show()

#另一種查看是否服從正態分布的可視化方法

sns.distplot(y, fit=st.norm)
plt.title('使用 Normal')
show()

res = st.probplot(y, plot=plt)
plt.title('SalePrice')
show()

print('------------------------------')	#30個

#把房價做對數變換后再看
SalePrice_log = np.log(y)
 
#transformed histogram and normal probability plot
sns.distplot(SalePrice_log, fit=st.norm);
plt.title('使用 Normal')
#plt.title('SalePrice log')
show()

#另一種查看是否服從正態分布的可視化方法
res = st.probplot(SalePrice_log, plot=plt)
print(res)
plt.title('SalePrice log')
show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
from scipy.stats import norm


def norm_prob(x, mu, sigma):
    p = norm(mu, sigma).cdf(x + 0.0001) - norm(mu, sigma).cdf(x - 0.0001)
    return p


def loglikelihood(data, mu, sigma):
    l = 0.0
    for x in data:
        l -= np.log(norm_prob(x, mu, sigma))
    return l


N = 1000
mu, sigma = 1.6, 0.2

h = 1.8

#rvs: 隨機變量
data = norm.rvs(loc=mu, scale=sigma, size=N)
#print(data)

bins = 50  # 束
plt.hist(data, bins=bins)
plt.title('normal distribution')
show()

#pdf: 概率密度函數
tt = norm.pdf(x=1.8, loc=1.6, scale=0.2)
print(tt)

tt = norm_prob(h, mu, sigma)
print(tt)

tt = loglikelihood(data, mu, sigma)
print(tt)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

neg_data = "data/neg.csv"
pos_data = "data/pos.csv"

import codecs
import jieba

corpus = []
with codecs.open(neg_data, encoding="utf-8") as f:
    for line in f:
        words = list(jieba.cut(line.replace("|", "")))
        corpus.append(" ".join(words))

neg_df = pd.DataFrame()
neg_df["content"] = corpus
neg_df["label"] = 0

corpus2 = []
with codecs.open(pos_data, encoding="utf-8") as f:
    for line in f:
        words = list(jieba.cut(line.replace("|", "")))
        corpus2.append(" ".join(words))

pos_df = pd.DataFrame()
pos_df["content"] = corpus2
pos_df["label"] = 1

tt = neg_df.head(5)
print(tt)

tt = pos_df.head(5)
print(tt)

corpus_df = pd.concat((neg_df, pos_df))

tt = corpus_df.head(5)
print(tt)

print('------------------------------')	#30個

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
counts = cv.fit_transform(corpus_df["content"].values)

from sklearn.naive_bayes import MultinomialNB

classifier = MultinomialNB()

targets = corpus_df["label"].values

classifier.fit(counts, targets)  # 學習訓練.fit

examples = ["這 本 書 真差", "這個 電影 還 可 以"]
example_counts = cv.transform(examples)
predictions = classifier.predict(example_counts)  # 預測.predict

print('預測結果 :', predictions)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 1. 建立空的df
df = pd.DataFrame()

# 2. 增加 Gender 欄位 目標欄位
df["Gender"] = [
    "male",
    "male",
    "male",
    "male",
    "female",
    "female",
    "female",
    "female",
]

# 3. 增加 4欄位 為 feature variables
df["Height"] = [6, 5.92, 5.58, 5.92, 5, 5.5, 5.42, 5.75]
df["Weight"] = [180, 190, 170, 165, 100, 150, 130, 150]
df["Size"] = [12, 11, 12, 10, 6, 8, 7, 9]
df["Team"] = ["i100", "i100", "i500", "i100", "i500", "i100", "i500", "i100"]

print("df:\n", df)

print("------------------------------")  # 30個

df1 = (
    df.groupby(["Team", "Gender"]).size().rename("cnt").reset_index().set_index("Team")
)
print("df1:\n", df1)

df2 = pd.DataFrame(df.groupby(["Team"]).size().rename("total"))
print("df2:\n", df2)

df3 = df1.merge(df2, left_index=True, right_index=True)
df3["p"] = df3["cnt"] * 1.0 / df3["total"]
df3 = df3.reset_index()
print("df3:\n", df3)

print("------------------------------")  # 30個


def p_x_given_y_1(team, gender):
    return df3["p"][df3["Team"] == team][df3["Gender"] == gender].values[0]


print("p_x_given_y_1")
print(p_x_given_y_1("i100", "female"))
# 0.4

print("------------------------------")  # 30個

# 計算先驗
# Number of i100
n_i100 = df["Team"][df["Team"] == "i100"].count()
print("n_i100 的個數 :", n_i100)

# Number of i500
n_i500 = df["Team"][df["Team"] == "i500"].count()
print("n_i500 的個數 :", n_i500)

# Total rows
total_ppl = df["Team"].count()
print("全部列數 :", n_i100)

# Number of males divided by the total rows
P_i100 = n_i100 * 1.0 / total_ppl

# Number of females divided by the total rows
P_i500 = n_i500 * 1.0 / total_ppl

print("P_i100 :", P_i100)
print("P_i500 :", P_i500)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 計算高斯分布的概率

# 1. 建立空的df
df = pd.DataFrame()

# Create some feature values for this single row
# 2. 增加 Gender 欄位 目標欄位 ??
# 3. 增加 4欄位 為 feature variables ??
df["Height"] = [6]
df["Weight"] = [130]
df["Size"] = [8]
df["Gender"] = ["female"]

print("df:\n", df)


def p_x_given_y_2(x, mean_y, variance_y):
    # Input the arguments into a probability density function
    p = (
        1
        / (np.sqrt(2 * np.pi * variance_y))
        * np.exp((-((x - mean_y) ** 2)) / (2 * variance_y))
    )
    return p


tt = df["Gender"][0]
print(tt)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""

"""
from sklearn.preprocessing import PolynomialFeatures

train_size = 20
test_size = 12
train_X = np.random.uniform(low=0, high=1.2, size=train_size)
test_X = np.random.uniform(low=0.1, high=1.3, size=test_size)
train_y = np.sin(train_X * 2 * np.pi) + np.random.normal(0, 0.2, train_size)
test_y = np.sin(test_X * 2 * np.pi) + np.random.normal(0, 0.2, test_size)

poly = PolynomialFeatures(6)  # 次數は6

train_poly_X = poly.fit_transform(train_X.reshape(train_size, 1))
test_poly_X = poly.fit_transform(test_X.reshape(test_size, 1))

model = Ridge(alpha=1.0)

model.fit(train_poly_X, train_y)  # 學習訓練.fit

train_pred_y = model.predict(train_poly_X)  # 預測.predict
test_pred_y = model.predict(test_poly_X)  # 預測.predict
print(mean_squared_error(train_pred_y, train_y))
print(mean_squared_error(test_pred_y, test_y))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.naive_bayes import MultinomialNB

# 6個row的訓練資料
X_train = [
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
]
# 6個row的訓練目標
y_train = [1, 1, 1, 0, 0, 0]

model = MultinomialNB()

model.fit(X_train, y_train)  # 學習訓練.fit

#預測
y_pred = model.predict([[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]])  # 預測.predict
print(y_pred)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.decomposition import TruncatedSVD

data = [
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
]
n_components = 2  # 潛在変數の數

model = TruncatedSVD(n_components=n_components)

model.fit(data)  # 學習訓練.fit

print(model.transform(data))  # 変換したデータ
print(model.explained_variance_ratio_)  # 寄與率
print(sum(model.explained_variance_ratio_))  # 累積寄與率
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" import fail
from sklearn.datasets import samples_generator
from sklearn.manifold import LocallyLinearEmbedding

data, color = samples_generator.make_swiss_roll(n_samples=1500)
n_neighbors = 12 # 近傍點の數 
n_components = 2 # 削減後の次元數

model = LocallyLinearEmbedding(n_neighbors=n_neighbors,

n_components=n_components)

model.fit(data)  # 學習訓練.fit

print(model.transform(data)) # 変換したデータ
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 安裝 auto-sklearn fail
print('Auto-Sklearn')

#pip install auto-sklearn

import autosklearn.classification
import statsmodels.api as sm
  
data = sm.datasets.anes96.load_pandas().data
label = 'vote'
features = [i for i in data.columns if i != label]
X_train = data[features]
y_train = data[label]
automl = autosklearn.classification.AutoSklearnClassifier(
    time_left_for_this_task=120, per_run_time_limit=120, # 兩分鐘
    include_estimators=["random_forest"])
automl.fit(X_train, y_train)  # 學習訓練.fit
print(automl.score(X_train, y_train))
"""

print("------------------------------------------------------------")  # 60個

""" 安裝 auto-ml fail
print('Auto-ML')

#pip install auto-ml

from auto_ml import Predictor
import statsmodels.api as sm

data = sm.datasets.anes96.load_pandas().data
column_descriptions = {
    'vote': 'output',
    'TVnews': 'categorical',
    'educ': 'categorical',
    'income': 'categorical',
}

ml_predictor = Predictor(type_of_estimator='classifier', 
                         column_descriptions=column_descriptions)
model = ml_predictor.train(data)
model.score(data, data.vote)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
實際數據請從天池競賽平臺下載
https://tianchi.aliyun.com/competition/gameList/activeList
https://tianchi.aliyun.com/competition/activeList
"""

from pandas.api.types import is_numeric_dtype  # 用於判斷特徵類型
from sklearn.ensemble import RandomForestClassifier  # 分類模型
from sklearn.ensemble import GradientBoostingClassifier  # 分類模型
from sklearn.ensemble import RandomForestRegressor  # 迴歸模型
from sklearn.ensemble import GradientBoostingRegressor  # 迴歸模型

"""
無csv資料
data = pd.read_csv('data/happiness_train_min.csv', encoding='gb2312')

test = pd.read_csv('data/happiness_test_min.csv', encoding='gb2312')

print(data.columns.tolist()) # 查看所有特徵
print(data.dtypes) # 查看各特徵類型

print('------------------------------------------------------------')	#60個

# 特徵工程

features = []
label = 'happiness' # 目標變量

for col in data.columns:
    if not is_numeric_dtype(data[col]): # 非數值型特徵
        print(col, data[col].dtype)
        print(data[col].unique()[:5])
    elif col != label and col != 'id': # 加入可直接代入模型的特徵
        features.append(col)
        
x = data[features] # 自變量
y = data[label] # 目標變量

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=9487)
# 訓練組8成, 測試組2成

x_train = x_train.fillna(x.mean()) # 空值填充訓練集
x_val = x_val.fillna(x.mean()) # 空值填充驗證集
x_test = test.fillna(x.mean()) # 空值填充測試集
x = x.fillna(x.mean()) # 空值填充全集

print('------------------------------------------------------------')	#60個

# 訓練模型生成提交數據

#clf = RandomForestRegressor(criterion='mse', random_state=9487) # 隨機森林迴歸
#clf = GradientBoostingClassifier(criterion='mse',random_state=9487) # GBDT分類
clf = GradientBoostingRegressor(criterion='mse', random_state=9487) # GBDT迴歸

if True: # 用於本地測試
    clf.fit(x_train, y_train)  # 學習訓練.fit
    mse = mean_squared_error(y_val, [round(i) for i in clf.predict(x_val)])
    print("MSE: %.4f" % mse)
else: # 用於遠程提交
    clf.fit(x, y) # 全量數據訓練  # 學習訓練.fit
    df = pd.DataFrame()
    df['id'] = test.id
    df['happiness'] = clf.predict(x_test[features])
    df.to_csv('out/submit_{}.csv'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')),index=False)

print('------------------------------------------------------------')	#60個

from pandas.api.types import is_numeric_dtype # 用於判斷特徵類型

data = pd.read_csv('data/happiness_train_min.csv', encoding='gb2312')
test = pd.read_csv('data/happiness_test_min.csv', encoding='gb2312')

print('------------------------------------------------------------')	#60個

# 特徵工程

def get_mean(fea, data, test): # 同時變換訓練集和測試集
    arr1 = data[fea].unique()
    arr2 = test[fea].unique()
    arr3 = list(arr1)
    arr3.extend(arr2) # 有的數據只出現在訓練集或測試集中
    arr4 = list(set(arr3))
    dic = {}
    for x in arr4:
        dic[x] = data[data[fea] == x][label].mean() # 取其因變量均值
    data[fea] = data[fea].apply(lambda x: dic[x]) # 數據替換
    test[fea] = test[fea].apply(lambda x: dic[x])
    return data,test

label = 'happiness' # 目標變量
features = []

data, test = get_mean('city', data, test)
data, test = get_mean('invest_other', data, test)
data, test = get_mean('province', data, test)

for col in data.columns:
    if not is_numeric_dtype(data[col]): # 非數值型特徵
        continue
    elif col != label and col != 'id' and col not in ['public_service_7']: # 去掉干擾特徵
        features.append(col)
        data[col] = data[col].apply(lambda x: np.nan if x < 0 else x) # 優化點一
        test[col] = test[col].apply(lambda x: np.nan if x < 0 else x)

data_all = pd.concat([data,test]) # 優化點二
data = data[data['happiness'] > 0] # 去掉因變量缺失的數據
x = data[features] # 自變量
y = data[label] # 目標變量

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=9487)
# 訓練組8成, 測試組2成

x_train = x_train.fillna(data_all[features].mean()) # 空值填充訓練集
x_val = x_val.fillna(data_all[features].mean()) # 空值填充驗證集
x_test = test.fillna(data_all[features].mean()) # 空值填充測試集
x = x.fillna(data_all[features].mean()) # 空值填充全集

print('------------------------------------------------------------')	#60個

# 訓練模型

import xgboost as xgb
from sklearn.model_selection import KFold

def my_eval(preds, train): # 自定義評價函數
    score = mean_squared_error(train.get_label(), preds)
    return 'myeval', score

my_params = {"booster":'gbtree','eta': 0.005, 'max_depth': 6, 'subsample': 0.7, 
              'colsample_bytree': 0.8, 'objective': 'reg:linear', 'eval_metric': 'rmse', 
              'silent': True, 'nthread': 4} # 模型參數

train_preds = np.zeros(len(data)) # 用於保存預測結果
test_preds = np.zeros(len(test))
kf = KFold(len(data), n_folds = 5, shuffle=True, random_state=9487) # 5折交叉驗證
for fold, (trn_idx, val_idx) in enumerate(kf):
    print("fold {}".format(fold+1))
    train_data = xgb.DMatrix(data[features].iloc[trn_idx], data[label].iloc[trn_idx]) # 訓練集
    val_data = xgb.DMatrix(data[features].iloc[val_idx], data[label].iloc[val_idx]) # 驗證集
    watchlist = [(train_data, 'train'), (val_data, 'valid_data')]
    clf = xgb.train(dtrain=train_data, num_boost_round=5000, evals=watchlist, 
               early_stopping_rounds=200, verbose_eval=100, 
               params=my_params,feval = my_eval)
    train_preds[val_idx] = clf.predict(xgb.DMatrix(data[features].iloc[val_idx]),
               ntree_limit=clf.best_ntree_limit)
    test_preds += clf.predict(xgb.DMatrix(test[features]), 
               ntree_limit=clf.best_ntree_limit) / kf.n_folds
print("CV score: {:<8.8f}".format(mean_squared_error(train_preds, data[label])))

df = pd.DataFrame() # 生成提交結果
df['id'] = test.id
df['happiness'] = test_preds
df.to_csv('out/submit_{}.csv'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')),index=False)

print('------------------------------------------------------------')	#60個

fig,ax = plt.subplots()
fig.set_size_inches(40,6)
xgb.plot_tree(clf, ax=ax, num_trees=0) # 顯示模型中的第一棵樹
plt.savefig('tmp.png',dpi=300)

print('------------------------------------------------------------')	#60個

# 檢測干擾變量

from sklearn.ensemble import GradientBoostingRegressor

baseline = 0.4887 # 誤差baseline
for i in features:
    features_new = [x for x in features if x != i]
    clf = GradientBoostingRegressor(criterion='mse', random_state=9487)
    clf.fit(x_train[features_new], y_train)  # 學習訓練.fit
    mse = mean_squared_error(y_val, [round(i) for i in clf.predict(x_val[features_new])])
    if mse < baseline:
        print("remove", i, "MSE: %.4f" % mse)

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
from scipy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer


def similarity_tfidf(s1, s2):
    def add_space(s):
        return " ".join(list(s))

    s1, s2 = add_space(s1), add_space(s2)

    cv = TfidfVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()

    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))


string1 = "漢堡蛋"
string2 = "我要一份漢堡蛋"
# string2 = '請給我來一份漢堡蛋'
# string2 = '你是一個漢堡蛋嗎?'

result = similarity_tfidf(string1, string2)

print("相似度 : ", result)
if result > 0.2:
    print("OK, 一個漢堡蛋")
else:
    print("Sorry, 無法接受訂餐")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 200

X = np.linspace(0, 1, N)
y = np.sqrt(X) + 0.2 * np.random.rand(N) - 0.1

X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures


def polynomial_model(degree=1):
    polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
    linear_regression = LinearRegression()
    pipeline = Pipeline(
        [
            ("polynomial_features", polynomial_features),
            ("linear_regression", linear_regression),
        ]
    )
    return pipeline


print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit


def plot_learning_curve(
    estimator,
    title,
    X,
    y,
    ylim=None,
    cv=None,
    n_jobs=1,
    train_sizes=np.linspace(0.1, 1.0, 5),
):
    """
    Generate a simple plot of the test and training learning curve.
    Parameters
    ----------
    estimator : object type that implements the "fit" and "predict" methods
        An object of that type which is cloned for each validation.

    title : string
        Title for the chart.

    X : array-like, shape (n_samples, n_features)
        Training vector, where n_samples is the number of samples and
        n_features is the number of features.

    y : array-like, shape (n_samples) or (n_samples, n_features), optional
        Target relative to X for classification or regression;
        None for unsupervised learning.

    ylim : tuple, shape (ymin, ymax), optional
        Defines minimum and maximum yvalues plotted.

    cv : int, cross-validation generator or an iterable, optional
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:
          - None, to use the default 3-fold cross-validation,
          - integer, to specify the number of folds.
          - An object to be used as a cross-validation generator.
          - An iterable yielding train/test splits.

        For integer/None inputs, if ``y`` is binary or multiclass,
        :class:`StratifiedKFold` used. If the estimator is not a classifier
        or if ``y`` is neither binary nor multiclass, :class:`KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validators that can be used here.

    n_jobs : integer, optional
        Number of jobs to run in parallel (default 1).
    """
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes
    )
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(
        train_sizes,
        train_scores_mean - train_scores_std,
        train_scores_mean + train_scores_std,
        alpha=0.1,
        color="r",
    )
    plt.fill_between(
        train_sizes,
        test_scores_mean - test_scores_std,
        test_scores_mean + test_scores_std,
        alpha=0.1,
        color="g",
    )
    plt.plot(train_sizes, train_scores_mean, "o--", color="r", label="Training score")
    plt.plot(
        train_sizes, test_scores_mean, "o-", color="g", label="Cross-validation score"
    )

    plt.legend(loc="best")
    return plt


# 為了讓學習曲線更平滑，交叉驗證數據集的得分計算 10 次，每次都重新選中 20% 的數據計算一遍
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=9487)
titles = [
    "Learning Curves (Under Fitting)",
    "Learning Curves",
    "Learning Curves (Over Fitting)",
]
degrees = [1, 3, 10]

plt.figure(figsize=(18, 4))
for i in range(len(degrees)):
    plt.subplot(1, 3, i + 1)
    plot_learning_curve(
        polynomial_model(degrees[i]), titles[i], X, y, ylim=(0.75, 1.01), cv=cv
    )

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_files

""" 缺資料
print("loading train dataset ...")
t = time.time()
news_train = load_files('datasets/mlcomp/379/train')
print("summary: {0} documents in {1} categories.".format(
    len(news_train.data), len(news_train.target_names)))
print("done in {0} seconds".format(time.time() - t))

from sklearn.feature_extraction.text import TfidfVectorizer

print("vectorizing train dataset ...")
t = time.time()
vectorizer = TfidfVectorizer(encoding='latin-1')
X_train = vectorizer.fit_transform((d for d in news_train.data))
print("n_samples: %d, n_features: %d" % X_train.shape)
print("number of non-zero features in sample [{0}]: {1}".format(
    news_train.filenames[0], X_train[0].getnnz()))
print("done in {0} seconds".format(time.time() - t))

print("------------------------------")  # 30個

from sklearn.naive_bayes import MultinomialNB

print("traning models ...".format(time.time() - t))
t = time.time()
y_train = news_train.target

clf = MultinomialNB(alpha=0.0001)

clf.fit(X_train, y_train)

train_score = clf.score(X_train, y_train)
print("train score: {0}".format(train_score))
print("done in {0} seconds".format(time.time() - t))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 缺資料
print("loading test dataset ...")
t = time.time()
news_test = load_files('datasets/mlcomp/379/test')
print("summary: {0} documents in {1} categories.".format(
    len(news_test.data), len(news_test.target_names)))
print("done in {0} seconds".format(time.time() - t))

print("------------------------------")  # 30個

print("vectorizing test dataset ...")
t = time.time()
X_test = vectorizer.transform((d for d in news_test.data))
y_test = news_test.target
print("n_samples: %d, n_features: %d" % X_test.shape)
print("number of non-zero features in sample [{0}]: {1}".format(
    news_test.filenames[0], X_test[0].getnnz()))
print("done in %fs" % (time.time() - t))

print("------------------------------")  # 30個

pred = clf.predict(X_test[0])
print("predict: {0} is in category {1}".format(
    news_test.filenames[0], news_test.target_names[pred[0]]))
print("actually: {0} is in category {1}".format(
    news_test.filenames[0], news_test.target_names[news_test.target[0]]))

print("------------------------------")  # 30個

print("predicting test dataset ...")
t = time.time()
pred = clf.predict(X_test)
print("done in %fs" % (time.time() - t))

print("------------------------------")  # 30個

print("classification report on test set for classifier:")
print(clf)
print(classification_report(y_test, pred,
                            target_names=news_test.target_names))

print("------------------------------")  # 30個

cm = confusion_matrix(y_test, pred)
print("confusion matrix:")
print(cm)

print("------------------------------")  # 30個

# Show confusion matrix
plt.figure(figsize=(8, 8))
plt.title('Confusion matrix of the classifier')
ax = plt.gca()                                  
ax.spines['right'].set_color('none')            
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.matshow(cm, fignum=1, cmap='gray')
plt.colorbar()

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
X, y = make_blobs(
    n_samples=200,
    n_features=2,
    centers=4,
    cluster_std=1,
    center_box=(-10.0, 10.0),
    shuffle=True,
    random_state=9487,
)

plt.figure(figsize=(6, 4))
plt.xticks(())
plt.yticks(())
plt.scatter(X[:, 0], X[:, 1], s=20, marker="o")

show()

print("------------------------------")  # 30個

n_clusters = 3
kmean = KMeans(n_clusters=n_clusters)

kmean.fit(X)

print("kmean: k={}, cost={}".format(n_clusters, int(kmean.score(X))))

labels = kmean.labels_
centers = kmean.cluster_centers_
markers = ["o", "^", "*"]
colors = ["r", "b", "y"]

plt.figure(figsize=(6, 4))
plt.xticks(())
plt.yticks(())

# 畫樣本
for c in range(n_clusters):
    cluster = X[labels == c]
    plt.scatter(cluster[:, 0], cluster[:, 1], marker=markers[c], s=20, c=colors[c])
# 畫出中心點
plt.scatter(centers[:, 0], centers[:, 1], marker="o", c="white", alpha=0.9, s=300)
for i, c in enumerate(centers):
    plt.scatter(c[0], c[1], marker="$%d$" % i, s=50, c=colors[i])

show()

print("------------------------------")  # 30個


def fit_plot_kmean_model(n_clusters, X):
    plt.xticks(())
    plt.yticks(())

    # 使用 k-均值算法進行擬合
    kmean = KMeans(n_clusters=n_clusters)
    kmean.fit_predict(X)

    labels = kmean.labels_
    centers = kmean.cluster_centers_
    markers = ["o", "^", "*", "s"]
    colors = ["r", "b", "y", "k"]

    # 計算成本
    score = kmean.score(X)
    plt.title("k={}, score={}".format(n_clusters, (int)(score)))

    # 畫樣本
    for c in range(n_clusters):
        cluster = X[labels == c]
        plt.scatter(cluster[:, 0], cluster[:, 1], marker=markers[c], s=20, c=colors[c])
    # 畫出中心點
    plt.scatter(centers[:, 0], centers[:, 1], marker="o", c="white", alpha=0.9, s=300)
    for i, c in enumerate(centers):
        plt.scatter(c[0], c[1], marker="$%d$" % i, s=50, c=colors[i])


n_clusters = [2, 3, 4]

plt.figure(figsize=(10, 3))
for i, c in enumerate(n_clusters):
    plt.subplot(1, 3, i + 1)
    fit_plot_kmean_model(c, X)

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_files

""" NG 無檔案
print("loading documents ...")
t = time.time()
docs = load_files('datasets/clustering/data')
print("summary: {0} documents in {1} categories.".format(
    len(docs.data), len(docs.target_names)))
print("done in {0} seconds".format(time.time() - t))

from sklearn.feature_extraction.text import TfidfVectorizer

max_features = 20000
print("vectorizing documents ...")
t = time.time()
vectorizer = TfidfVectorizer(max_df=0.4, 
                             min_df=2, 
                             max_features=max_features, 
                             encoding='latin-1')
X = vectorizer.fit_transform((d for d in docs.data))
print("n_samples: %d, n_features: %d" % X.shape)
print("number of non-zero features in sample [{0}]: {1}".format(
    docs.filenames[0], X[0].getnnz()))
print("done in {0} seconds".format(time.time() - t))

print("------------------------------")  # 30個

print("clustering documents ...")
t = time.time()
n_clusters = 4
kmean = KMeans(n_clusters=n_clusters, 
               max_iter=100,
               tol=0.01,
               verbose=1,
               n_init=3)
kmean.fit(X)
print("kmean: k={}, cost={}".format(n_clusters, int(kmean.inertia_)))
print("done in {0} seconds".format(time.time() - t))

print(len(kmean.labels_))

cc = kmean.labels_[1000:1010]
print(cc)

cc = docs.filenames[1000:1010]
print(cc)

print('------------------------------')	#30個

print("Top terms per cluster:")

order_centroids = kmean.cluster_centers_.argsort()[:, ::-1]

terms = vectorizer.get_feature_names_out()
for i in range(n_clusters):
    print("Cluster %d:" % i, end='')
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind], end='')
    print()

a = np.array([[20, 10, 30, 40], [100, 300, 200, 400], [1, 5, 3, 2]])
cc = a.argsort()[:, ::-1]
print(cc)

a = np.array([10, 30, 20, 40])
cc = a.argsort()[::-1]
print(cc)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)
cc = metrics.adjusted_rand_score(label_true, label_pred)
print("Adjusted Rand-Index for random sample: %.3f" % cc)

label_true = [1, 1, 3, 3, 2, 2]
label_pred = [3, 3, 2, 2, 1, 1]
cc = metrics.adjusted_rand_score(label_true, label_pred)
print("Adjusted Rand-Index for same structure sample: %.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
cc = metrics.homogeneity_score(label_true, label_pred)
print("Homogeneity score for same structure sample: %.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [0, 1, 2, 3]
cc = metrics.homogeneity_score(label_true, label_pred)
print("Homogeneity score for each cluster come from only one class: %.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]

cc = metrics.homogeneity_score(label_true, label_pred)
print("Homogeneity score for each cluster come from two class: %.3f" % cc)

label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)
cc = metrics.homogeneity_score(label_true, label_pred)
print("Homogeneity score for random sample: %.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
cc = metrics.completeness_score(label_true, label_pred)
print("Completeness score for same structure sample: %.3f" % cc)

label_true = [0, 1, 2, 3]
label_pred = [1, 1, 2, 2]
cc = metrics.completeness_score(label_true, label_pred)
print("Completeness score for each class assign to only one cluster: %.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
cc = metrics.completeness_score(label_true, label_pred)
print("Completeness score for each class assign to two class: %.3f" % cc)
label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)
cc = metrics.completeness_score(label_true, label_pred)
print("Completeness score for random sample: %.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
cc = metrics.v_measure_score(label_true, label_pred)
print("V-measure score for same structure sample: %.3f" % cc)

label_true = [0, 1, 2, 3]
label_pred = [1, 1, 2, 2]
cc = metrics.v_measure_score(label_true, label_pred)
print("V-measure score for each class assign to only one cluster: %.3f" % cc)
cc = metrics.v_measure_score(label_pred, label_true)
print("V-measure score for each class assign to only one cluster: %.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
cc = metrics.v_measure_score(label_true, label_pred)
print("V-measure score for each class assign to two class: %.3f" % cc)

"""
labels = docs.target
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels, kmean.labels_))
print("Completeness: %0.3f" % metrics.completeness_score(labels, kmean.labels_))
print("V-measure: %0.3f" % metrics.v_measure_score(labels, kmean.labels_))
print("Adjusted Rand-Index: %.3f"
      % metrics.adjusted_rand_score(labels, kmean.labels_))

#[平均]輪廓係數 silhouette_score
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, kmean.labels_, sample_size=1000))
"""

print("------------------------------------------------------------")  # 60個

# 數據預處理（Data Preprocessing）

print("Sklearn verion is {}".format(sklearn.__version__))

from sklearn.impute import SimpleImputer

# This block is an example used to learn SimpleImputer
imp_mean = SimpleImputer(missing_values=np.nan, strategy="mean")

imp_mean.fit([[7, 2, 3], [4, np.nan, 6], [10, 5, 9]])

X = [[np.nan, 2, 3], [4, np.nan, 6], [10, np.nan, 9]]
print(imp_mean.transform(X))

enc = OneHotEncoder(handle_unknown="ignore")
X = [["Male", 1], ["Female", 3], ["Female", 2]]

enc.fit(X)

cc = enc.categories_
print(cc)

cc = enc.transform([["Female", 1], ["Male", 4]]).toarray()
print(cc)

cc = enc.inverse_transform([[0, 1, 1, 0, 0], [0, 0, 0, 1, 0]])
print(cc)

cc = enc.get_feature_names_out(["gender", "group"])
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

dataset = pd.read_csv("data/Data.csv")

# 不包括最后一列的所有列
X = dataset.iloc[:, :-1].values  # //.iloc[行，列]

# 取最后一列
Y = dataset.iloc[:, 3].values  # : 全部行 or 列；[a]第a行 or 列
# [a,b,c]第 a,b,c 行 or 列

print("X")
print(X)
print("Y")
print(Y)
print(X[:, 1:3])

# 第三步：處理丟失數據

# 我們得到的數據很少是完整的。
# 數據可能因為各種原因丟失，為了不降低機器學習模型的性能，需要處理數據。
# 我們可以用整列的平均值或中間值替換丟失的數據。
# 我們用sklearn.preprocessing庫中的Imputer類完成這項任務。

# Step 3: Handling the missing data
# If you use the newest version of sklearn, use the lines of code commented out
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")

# from sklearn.preprocessing import Imputer
# axis=0表示按列進行
# imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
# print(imputer)
# print(X[ : , 1:3])

imputer = imputer.fit(X[:, 1:3])  # put the data we want to process in to this imputer
X[:, 1:3] = imputer.transform(X[:, 1:3])  # replace the np.nan with mean

# print(X[ : , 1:3])
print("---------------------")
print("Step 3: Handling the missing data")
print("step2")
print("X")
print(X)

""" another
第3步：處理丟失數據

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[ : , 1:3])
X[ : , 1:3] = imputer.transform(X[ : , 1:3])
"""

# Step 4: Encoding categorical data
# 第四步：解析分類數據
# 分類數據指的是含有標簽值而不是數字值的變量。取值范圍通常是固定的。
# 例如"Yes"和"No"不能用于模型的數學計算，所以需要解析成數字。
# 為實現這一功能，我們從sklearn.preprocessing庫導入LabelEncoder類。

"""
labelencoder_X = LabelEncoder()
X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])
"""

# labelencoder_X = LabelEncoder()
# X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])
# Creating a dummy variable
# print(X)
ct = ColumnTransformer([("", OneHotEncoder(), [0])], remainder="passthrough")
X = ct.fit_transform(X)
# onehotencoder = OneHotEncoder(categorical_features = [0])
# X = onehotencoder.fit_transform(X).toarray()

labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)

print("---------------------")
print("Step 4: Encoding categorical data")
print("X")
print(X)
print("Y")
print(Y)

""" another
創建虛擬變量

onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y =  labelencoder_Y.fit_transform(Y)
"""

# Step 5: Splitting the datasets into training sets and Test sets
# 第五步：拆分數據集為測試集合和訓練集合
# 把數據集拆分成兩個：一個是用來訓練模型的訓練集合，另一個是用來驗證模型的測試集合。
# 兩者比例一般是80:20。
# 我們導入sklearn.model_selection庫中的train_test_split()方法。

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
# 訓練組8成, 測試組2成

# 第六步：特征縮放
# 第6步：特征量化
# Step 6: Feature Scaling
# 大部分模型算法使用兩點間的歐氏距離表示，
# 但此特征在幅度、單位和范圍姿態問題上變化很大。
# 在距離計算中，高幅度的特征比低幅度特征權重更大。
# 可用特征標準化或Z值歸一化解決。
# 導入sklearn.preprocessing庫的StandardScalar類。

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # STD特徵縮放
X_test = scaler.transform(X_test)  # STD特徵縮放

print("---------------------")
print("Step 6: Feature Scaling")
print("X_train")
print(X_train)
print("X_test")
print(X_test)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("邏輯迴歸(Logistic Regression)")

dataset = pd.read_csv("data/Social_Network_Ads.csv")

X = dataset.iloc[:, [2, 3]].values
Y = dataset.iloc[:, 4].values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
# 訓練組8成, 測試組2成

# 特征縮放 Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # STD特徵縮放
X_test = scaler.transform(X_test)  # STD特徵縮放

# 第二步：邏輯回歸模型

# 該項工作的庫將會是一個線性模型庫，之所以被稱為線性是因為邏輯回歸是一個線性分類器，
# 這意味著我們在二維空間中，我們兩類用戶（購買和不購買）將被一條直線分割。
# 然后導入邏輯回歸類。下一步我們將創建該類的對象，它將作為我們訓練集的分類器。

# 將邏輯回歸應用于訓練集
# Fitting Logistic Regression to the Training set

classifier = LogisticRegression()

classifier.fit(X_train, y_train)  # 學習訓練.fit

# Predicting the Test set results
# 第3步：預測
# 預測測試集結果

y_pred = classifier.predict(X_test)

# 第4步：評估預測

# 我們預測了測試集。 現在我們將評估邏輯回歸模型是否正確的學習和理解。
# 因此這個混淆矩陣將包含我們模型的正確和錯誤的預測。

# 生成混淆矩陣(Confusion Matrix)
cm = confusion_matrix(y_test, y_pred)

print(cm)  # print confusion_matrix
print(classification_report(y_test, y_pred))  # print classification report

from matplotlib.colors import ListedColormap

X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(("red", "green")),
)
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        c=ListedColormap(("red", "green"))(i),
        label=j,
    )

plt.title(" LOGISTIC(Training set)")
plt.xlabel(" Age")
plt.ylabel(" Estimated Salary")
plt.legend()

show()

X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)

plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(("red", "green")),
)
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        c=ListedColormap(("red", "green"))(i),
        label=j,
    )

plt.title(" LOGISTIC(Test set)")
plt.xlabel(" Age")
plt.ylabel(" Estimated Salary")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

dataset = pd.read_csv("data/Social_Network_Ads.csv")

X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # STD特徵縮放
X_test = scaler.transform(X_test)  # STD特徵縮放

# Fitting Decision Tree Classification to the Training set
from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier(criterion="entropy", random_state=0)

classifier.fit(X_train, y_train)  # 學習訓練.fit

# Predicting the Test set results
y_pred = classifier.predict(X_test)

cm = confusion_matrix(y_test, y_pred)

# Visualising the Training set results
from matplotlib.colors import ListedColormap

X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(("red", "green")),
)
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        c=ListedColormap(("red", "green"))(i),
        label=j,
    )
plt.title("Decision Tree Classification (Training set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()

show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap

X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(("red", "green")),
)
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        c=ListedColormap(("red", "green"))(i),
        label=j,
    )
plt.title("Decision Tree Classification (Test set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

dataset = pd.read_csv("data/Social_Network_Ads.csv")

X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# Feature Scaling 特征縮放
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # STD特徵縮放
X_test = scaler.transform(X_test)  # STD特徵縮放

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(
    n_estimators=10, criterion="entropy", random_state=0
)

classifier.fit(X_train, y_train)  # 學習訓練.fit

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# 生成混淆矩陣(Confusion Matrix)，也稱作誤差矩陣

cm = confusion_matrix(y_test, y_pred)

from matplotlib.colors import ListedColormap

X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(("red", "green")),
)
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        c=ListedColormap(("red", "green"))(i),
        label=j,
    )
plt.title("Random Forest Classification (Training set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()

show()

from matplotlib.colors import ListedColormap

X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(("red", "green")),
)
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        c=ListedColormap(("red", "green"))(i),
        label=j,
    )
plt.title("Random Forest Classification (Test set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 要先對數據集中的圖片進行處理，可能需要進行的任務有圖像尺寸統一、顏色處理等

import cv2
from tqdm import tqdm

# 數據集的路徑
DATADIR = "C:/_git/vcs/_big_files/kagglecatsanddogs_5340_1000/PetImages/"
DATADIR = "C:/_git/vcs/_big_files/kagglecatsanddogs_5340_800/PetImages/"

CATEGORIES = ["Dog", "Cat"]

for category in CATEGORIES:
    path = os.path.join(DATADIR, category)  # 創建路徑
    for img in os.listdir(path):  # 迭代遍歷每個圖片
        img_array = cv2.imread(
            os.path.join(path, img), cv2.IMREAD_GRAYSCALE
        )  # 轉化成array
        plt.imshow(img_array, cmap="gray")  # 轉換成圖像展示
        show()

        break  # 我們作為演示只展示一張，所以直接break了
    break  # 同上


# 看下array中存儲的圖像數據：
# print(img_array)

print("看下array的形狀")
print(img_array.shape)

# 我們可以看到這是一張很大的圖片，并且擁有RGB3個通道，這并不是我們想要的，
# 所以接下來我們將要進行的操作會使圖像變小，并且只剩下灰度：

print("resize")
IMG_SIZE = 100

new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
plt.imshow(new_array, cmap="gray")
show()

# 接下來，我們將要創建所有這些培訓數據，但是，首先，我們應該留出一些圖像進行最終測試。
# 我將手動創建一個名為Testing的目錄，然后在其中創建2個目錄，一個用于Dog，一個用于Cat。
# 從這里開始，我將把Dog和Cat的前15張圖像移到訓練版本中。確保移動它們，而不是復制。我們將使用它進行最終測試。

print("訓練資料")
training_data = []


def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)  # 得到分類，其中 0=dog 1=cat

        for img in tqdm(os.listdir(path)):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # 大小轉換
                training_data.append([new_array, class_num])  # 加入訓練數據中
            except Exception as e:  # 為了保證輸出是整潔的
                pass
            # except OSError as e:
            #    print("OSErrroBad img most likely", e, os.path.join(path,img))
            # except Exception as e:
            #    print("general exception", e, os.path.join(path,img))


"""
#以下 久
create_training_data()

print(len(training_data))

# 我們有大約25,000張圖片。
# 我們要做的一件事是確保我們的數據是平衡的。在這個數據集的情況下，
# 我可以看到數據集開始時是平衡的。平衡，我的意思是每個班級都有相同數量的例子（相同數量的狗和貓）。
# 如果不平衡，您要么將類權重傳遞給模型，以便它可以適當地測量誤差，或者通過將較大的集修剪為與較小集相同的大小來平衡樣本。
# 現在數據集中要么全是dog要么全是cat，因此接下來要引入隨機：

random.shuffle(training_data)

# 我們的training_data是一個列表，這意味著它是可變的，所以它現在很好地改組了。
# 我們可以通過迭代幾個初始樣本并打印出類來確認這一點：

for sample in training_data[:10]:
    print(sample[1])

# 現在可以看到已經是0、1交替了，我們可以開始我們的模型了：

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

# 讓我們保存這些數據，這樣我們就不需要每次想要使用神經網絡模型時繼續計算它：

pickle_out = open("tmp_X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("tmp_y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()
# We can always load it in to our current script, or a totally new one by doing:

pickle_in = open("tmp_X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle", "rb")
y = pickle.load(pickle_in)

# 現在我們已經拿出了數據集，我們已經準備好覆蓋卷積神經網絡，并用我們的數據進行分類。
# 以上就是這次的關于數據集操作的全部任務。

#基礎知識
#基本的CNN結構如下： Convolution(卷積) -> Pooling(池化) -> Convolution -> Pooling -> Fully Connected Layer(全連接層) -> Output
#Convolution（卷積）是獲取原始數據并從中創建特征映射的行為。
#Pooling(池化)是下采樣，通常以“max-pooling”的形式，我們選擇一個區域，然后在該區域中取最大值，這將成為整個區域的新值。
#Fully Connected Layers(全連接層)是典型的神經網絡，其中所有節點都“完全連接”。卷積層不像傳統的神經網絡那樣完全連接。
#卷積：我們將采用某個窗口，并在該窗口中查找要素,該窗口的功能現在只是新功能圖中的一個像素大小的功能，但實際上我們將有多層功能圖。
#接下來，我們將該窗口滑過并繼續該過程,繼續此過程，直到覆蓋整個圖像。
#池化：最常見的池化形式是“最大池化”，其中我們簡單地獲取窗口中的最大值，并且該值成為該區域的新值。
#全連接層：每個卷積和池化步驟都是隱藏層。在此之后，我們有一個完全連接的層，然后是輸出層。
#完全連接的層是典型的神經網絡（多層感知器）類型的層，與輸出層相同。
#注意 本次代碼中所需的X.pickle和y.pickle為上一篇的輸出，路徑請根據自己的情況更改！

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D

pickle_in = open("tmp_X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle", "rb")
y = pickle.load(pickle_in)

X = X / 255.0

model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors

model.add(Dense(64))

model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
"""

""" 久
model.fit(X, y, batch_size=32, epochs=3, validation_split=0.3)  # 學習訓練.fit

#在僅僅三個epoches之后，我們的驗證準確率為71％。
#如果我們繼續進行更多的epoches，我們可能會做得更好，但我們應該討論我們如何知道我們如何做。
#為了解決這個問題，我們可以使用TensorFlow附帶的TensorBoard，它可以幫助您在訓練模型時可視化模型。
#我們將在下一個教程中討論TensorBoard以及對我們模型的各種調整！

# 這是Python，TensorFlow和Keras教程系列的深度學習基礎知識的第4部分。
# 在這一部分，我們將討論的是TensorBoard。
# TensorBoard是一個方便的應用程序，允許您在瀏覽器中查看模型或模型的各個方面。
# 我們將TensorBoard與Keras一起使用的方式是通過Keras回調。實際上有很多Keras回調，你可以自己制作。

from tensorflow.keras.callbacks import TensorBoard

# Using TensorFlow backend.
# 創建TensorBoard回調對象
NAME = "Cats-vs-dogs-CNN"

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

#最終，你會希望獲得更多的自定義NAME，但現在這樣做。
#因此，這將保存模型的訓練數據logs/NAME，然后由TensorBoard讀取。
#最后，我們可以通過將它添加到.fit方法中來將此回調添加到我們的模型中，
#例如：
#model.fit(X, y,
#          batch_size=32,
#          epochs=3,
#          validation_split=0.3,
#          callbacks=[tensorboard])  # 學習訓練.fit
#請注意，這callbacks是一個列表。您也可以將其他回調傳遞到此列表中。
#我們的模型還沒有定義，所以現在讓我們把它們放在一起：

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard

# more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.

NAME = "Cats-vs-dogs-CNN"

pickle_in = open("tmp_X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle", "rb")
y = pickle.load(pickle_in)

X = X / 255.0

model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation("sigmoid"))

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=["accuracy"],
)

model.fit(X, y, batch_size=32, epochs=3, validation_split=0.3, callbacks=[tensorboard])  # 學習訓練.fit

#運行此之后，您應該有一個名為的新目錄logs。我們現在可以使用tensorboard從這個目錄中可視化初始結果。
#打開控制臺，切換到工作目錄，然后鍵入：tensorboard --logdir=logs/。
#您應該看到一個通知：TensorBoard 1.10.0 at http://H-PC:6006 (Press CTRL+C to quit)“h-pc”是您機器的名稱。
#打開瀏覽器并前往此地址。你應該看到類似的東西：

# 現在我們可以看到我們的模型隨著時間的推移。讓我們改變模型中的一些東西。
# 首先，我們從未在密集層中添加激活。另外，讓我們嘗試整體較小的模型：

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard

# more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.

NAME = "Cats-vs-dogs-64x2-CNN"

pickle_in = open("tmp_X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle", "rb")
y = pickle.load(pickle_in)

X = X / 255.0

model = Sequential()

model.add(Conv2D(64, (3, 3), input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation("relu"))

model.add(Dense(1))
model.add(Activation("sigmoid"))

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=["accuracy"],
)

model.fit(X, y, batch_size=32, epochs=10, validation_split=0.3, callbacks=[tensorboard])  # 學習訓練.fit

# 除此之外，我還改名為NAME = "Cats-vs-dogs-64x2-CNN"。
# 不要忘記這樣做，否則你會偶然附加到你以前的型號的日志，它看起來不太好。我們現在檢查TensorBoard：

#看起來更好！但是，您可能會立即注意到驗證丟失的形狀。
#損失是衡量錯誤的標準，看起來很明顯，在我們的第四個時代之后，事情開始變得糟糕。
#有趣的是，我們的驗證準確性仍然持續，但我想它最終會開始下降。
#更可能的是，第一件遭受的事情確實是你的驗證損失。這應該提醒你，你幾乎肯定會開始過度適應。
#這種情況發生的原因是該模型不斷嘗試減少樣本損失。
#在某些時候，模型不是學習關于實際數據的一般事物，而是開始只記憶輸入數據。
#如果你繼續這樣做，是的，樣本中的“準確性”會上升，但你的樣本，以及你試圖為模型提供的任何新數據可能會表現得很差。
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 類別變數編碼
# 測試資料

df = pd.DataFrame(
    [
        ["green", "M", 10.1, "class1"],
        ["red", "L", 13.5, "class2"],
        ["blue", "XL", 15.3, "class1"],
    ]
)

df.columns = ["color", "size", "price", "classlabel"]
print("原df")
print(df)

encoder = LabelEncoder()

print("size 字串 轉換 成 數字")
print('轉換前 df["size"]')
print(df["size"])
cc = encoder.fit_transform(df["size"])
print('轉換後 df["size"]')
print(cc)

cc = encoder.inverse_transform([1, 0, 2])
print("逆轉換")
print(cc)

print("使用 Pandas Map, 對映")

size_mapping = {"XL": 3, "L": 2, "M": 1}

df["size"] = df["size"].map(size_mapping)
print("轉換後df")
print(df)

from sklearn.preprocessing import OrdinalEncoder

data = [["Male", 1], ["Female", 3], ["Female", 2]]
encoder = OrdinalEncoder()
cc = encoder.fit_transform(data)
print(cc)

# One Hot Encoding with Pandas

df = pd.DataFrame(
    [
        ["green", "M", 10.1, "class1"],
        ["red", "L", 13.5, "class2"],
        ["blue", "XL", 15.3, "class1"],
    ]
)
df.columns = ["color", "size", "price", "classlabel"]

cc = pd.get_dummies(df, columns=["color"], prefix="is", prefix_sep="_")
print(cc)

# pandas v1.5 above
df2 = pd.get_dummies(df, columns=["color"], prefix="is", prefix_sep="_")
cc = pd.from_dummies(df2[["is_blue", "is_green", "is_red"]], sep="_")
print(cc)

# 測試資料
X = [["Male", 1], ["Female", 3], ["Female", 2]]

# 轉換
encoder = OneHotEncoder(handle_unknown="ignore")
X_new = encoder.fit_transform(X)
cc = X_new.toarray()
print(cc)

# 類別
cc = encoder.categories_
print(cc)

# 還原
cc = encoder.inverse_transform(X_new)
print(cc)

# 指定欄位名稱
cc = encoder.get_feature_names_out(["gender", "group"])
print(cc)

# 完整的表格處理程序

df = pd.DataFrame(
    [
        ["green", "M", 10.1, "class1"],
        ["red", "L", 13.5, "class2"],
        ["blue", "XL", 15.3, "class1"],
    ]
)
df.columns = ["color", "size", "price", "classlabel"]

# One-hot Encoding
encoder = OneHotEncoder(handle_unknown="ignore")
color_new = encoder.fit_transform(df[["color"]])

# 指定欄位名稱
column_names = encoder.get_feature_names_out(encoder.feature_names_in_)

# 轉換
df_new = pd.DataFrame(color_new.toarray(), columns=column_names)
print(df_new)

# 刪除原欄位 'color'
df.drop(["color"], axis=1, inplace=True)

# 合併表格
df2 = pd.concat([df, df_new], axis=1)
print(df2)

joblib.dump(encoder, "tmp_color.joblib")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 頻率轉換、合併多個表格

import yfinance as yf

# 下載每日股價

df_quote = yf.download("1101.TW", start="2020-01-01", end="2022-11-30")
df_quote.tail()

print("轉換為月頻率")

df_quote_new = df_quote.resample("ME").mean()
print(df_quote_new)

print("讀取月營收資料")

df_monthly_sales = pd.read_csv("./data/stock_monthly_sales.csv")
cc = df_monthly_sales.head()
print(cc)

print("轉換日期格式")

df_quote_new = df_quote.reset_index()
df_quote_new.Date = df_quote_new.Date
df_quote_new.Date = df_quote_new.Date.map(lambda x: str(x)[:4] + str(x)[5:7])
print(df_quote_new)

print("合併2個表格")

# 轉換日期資料型態，讓2個表格的日期資料型態一致
df_monthly_sales["年月"] = df_monthly_sales["年月"].astype("str")

# 合併2個表格
df = pd.merge(
    left=df_monthly_sales,
    right=df_quote_new,
    left_on="年月",
    right_on="Date",
    how="inner",
)
df = df[["Date", "單月營收", "Adj Close"]]

# 欄位改名
df.rename({"單月營收": "sales"}, axis=1, inplace=True)
print(df)

print("計算股價與月營收關聯度")

cc = df[["sales", "Adj Close"]].corr()
print(cc)

print("營收公布日期晚一個月")

df_monthly_sales["單月營收"] = df_monthly_sales["單月營收"].shift(-1)
df = pd.merge(
    left=df_monthly_sales,
    right=df_quote_new,
    left_on="年月",
    right_on="Date",
    how="inner",
)
df = df[["Date", "單月營收", "Adj Close"]]
df.rename({"單月營收": "sales"}, axis=1, inplace=True)
df.dropna(inplace=True)

cc = df[["sales", "Adj Close"]].corr()
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
import nltk
nltk.download('wordnet')
"""
print("------------------------------------------------------------")  # 60個

# spam_classification_with_tfidf
# 垃圾信分類

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import WordNetLemmatizer
from wordcloud import WordCloud
import re

mails = pd.read_csv("./data/spam.csv", encoding="latin-1")
cc = mails.head()
print(cc)

# 資料整理
mails.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1, inplace=True)
cc = mails.head()
print(cc)

mails.rename(columns={"v1": "label", "v2": "message"}, inplace=True)
cc = mails.head()
print(cc)

cc = mails["label"].value_counts()
print(cc)

mails["label"] = mails["label"].map({"ham": 0, "spam": 1})
cc = mails.head()
print(cc)

# 設定停用詞
import string

stopword_list = set(stopwords.words("english") + list(string.punctuation))
# 詞形還原(Lemmatization)
lem = WordNetLemmatizer()


# 前置處理(Preprocessing)
def preprocess(text, is_lower_case=True):
    if is_lower_case:
        text = text.lower()
    tokens = word_tokenize(text)
    tokens = [token.strip() for token in tokens if len(token) > 1 and token != "..."]
    filtered_tokens = [token for token in tokens if token not in stopword_list]
    filtered_tokens = [lem.lemmatize(token) for token in filtered_tokens]
    filtered_text = " ".join(filtered_tokens)
    return filtered_text


mails["message"] = mails["message"].map(preprocess)
cc = mails.head()
print(cc)

# 文字雲

# 凸顯垃圾信的常用單字
spam_words = " ".join(list(mails[mails["label"] == 1]["message"]))
spam_wc = WordCloud(width=512, height=512).generate(spam_words)
plt.figure(figsize=(10, 8), facecolor="k")
plt.imshow(spam_wc)
plt.axis("off")
plt.tight_layout(pad=0)
show()

# 找出正常信件的常用單字
ham_words = " ".join(list(mails[mails["label"] == 0]["message"]))
ham_wc = WordCloud(width=512, height=512).generate(ham_words)
plt.figure(figsize=(10, 8), facecolor="k")
plt.imshow(ham_wc)
plt.axis("off")
plt.tight_layout(pad=0)
show()

# 使用 SciKit-learn TF-IDF

mails_message, labels = mails["message"].values, mails["label"].values
mails_message = mails_message.astype(str)

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(mails_message)
print(tfidf_matrix.shape)

# (5572, 8111)

cc = tfidf_vectorizer.get_feature_names_out()
print(cc)

no = 0
for i in tfidf_matrix.toarray()[0]:
    if i > 0.0:
        no += 1
print(no)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    tfidf_matrix.toarray(), labels, test_size=0.2
)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = LogisticRegression()

clf.fit(X_train, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test)  # 預測.predict
cc = accuracy_score(y_pred, y_test)
print(cc)
# 0.9668161434977578

print(classification_report(y_test, y_pred))

print("混淆矩陣")
cc = confusion_matrix(y_test, y_pred)
print(cc)

# 測試

message_processed_list = (
    "I cant pick the phone right now. Pls send a message",
    "Congratulations ur awarded $500",
    "Thanks for your subscription to Ringtone UK your mobile will be charged",
    "Oops, I'll let you know when my roommate's done",
    "FreeMsg Hey there darling it's been 3 week's now and no word back! I'd like some fun you up for it still? Tb ok! XxX std chgs to send, 憯1.50 to rcv",
    "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's",
)
X_new = tfidf_vectorizer.transform(message_processed_list)
cc = clf.predict(X_new.toarray())  # 預測.predict
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_01_logistic_regression_validation

# 證明 Exp(log(x)) = x

for i in range(1, 101):
    assert round(math.e ** math.log(i), 6) == i

# 證明 log(1/x) = - log(x)

for i in range(1, 101):
    assert round(math.log(i), 6) == -round(math.log(1 / i), 6)

cc = math.log(100), -math.log(1 / 100)
print(cc)

# 計算羅吉斯函數的上限與下限

from sympy import *

x = symbols("x")
expr = 1 / (1 + np.e ** (-x))
limit(expr, x, -1000), limit(expr, x, np.inf)

# 不使用 limit

cc = 1 / (np.e**np.inf)
print(cc)

# 繪製羅吉斯函數
x = np.linspace(-6, 6, 101)
y = 1 / (1 + np.e ** (-x))
plt.plot(x, y)
plt.axhline(0, linestyle="-.", c="r")
plt.axhline(1, linestyle="-.", c="r")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_03_logistic_regression_attrition

# 員工流失預測

df = pd.read_csv("./data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

cc = df.isna().sum()
print(cc)

# 觀察資料集彙總資訊

df.info()  # 這樣就已經把資料集彙總資訊印出來

# 描述統計量
cc = df.describe()
print(cc)

# y 各類別資料筆數統計
sns.countplot(x=df["Attrition"])
show()

# 以Pandas函數統計各類別資料筆數
cc = df["Attrition"].value_counts()
print(cc)

print("檢查與時間有關的特徵相關性")

# 設定關聯度上限為 0.4
max_corr = 0.4
time_params = [
    "Age",
    "TotalWorkingYears",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager",
]
# 計算關聯度
corr_df = df[time_params].corr().round(2)

# 繪製熱力圖
plt.figure(figsize=(8, 5))
mask = np.zeros_like(corr_df)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(
        corr_df, mask=mask, vmax=max_corr, square=True, annot=True, cmap="YlGnBu"
    )
show()

# 刪除欄位
df.drop(
    {
        "TotalWorkingYears",
        "YearsInCurrentRole",
        "YearsSinceLastPromotion",
        "YearsWithCurrManager",
    },
    axis=1,
    inplace=True,
)

print("檢查與薪資(Salary)有關的特徵相關性")

salary_params = [
    "DailyRate",
    "HourlyRate",
    "MonthlyIncome",
    "MonthlyRate",
    "PercentSalaryHike",
    "StockOptionLevel",
]
# 計算關聯度
corr_df = df[salary_params].corr().round(2)

# 繪製熱力圖
plt.figure(figsize=(8, 5))
mask = np.zeros_like(corr_df)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(
        corr_df, mask=mask, vmax=max_corr, square=True, annot=True, cmap="YlGnBu"
    )
show()


print("找出所有類別變數，並顯示其類別")

df.select_dtypes("object").head()
print("Levels of categories: ")
for key in df.select_dtypes("object").keys():
    print(key, ":", df[key].unique())

print("進行One-hot encoding")

df2 = pd.get_dummies(
    df,
    columns=df.select_dtypes("object").keys(),
    prefix=df.select_dtypes("object").keys(),
)
cc = df2.keys()
print(cc)

print("刪除One-hot encoding的第一個類別欄位(base category)")

df2.drop(
    {
        "Attrition_No",
        "BusinessTravel_Non-Travel",
        "Department_Human Resources",
        "EducationField_Human Resources",
        "Gender_Female",
        "MaritalStatus_Single",
        "OverTime_No",
    },
    axis=1,
    inplace=True,
)
cont_vars = df2.select_dtypes("int").keys()
""" NG
dummies= df2.select_dtypes('uint8').keys().drop('Attrition_Yes') # 刪除目標變數(Y) 
print(dummies)
"""
print("指定特徵(X)及目標變數(Y)")

X = df2.drop("Attrition_Yes", axis=1)
y = df2["Attrition_Yes"]

# 3. 不須進行特徵工程

# 4. 資料分割

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法、6. 模型訓練

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 7. 模型評分

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 90.14%

# 混淆矩陣
print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

""" NG
#statsmodels 作法

import statsmodels.api as sm

model=sm.Logit(y_train, X_train)
result=model.fit()
print(result.summary())

#顯示權重資訊

stat_df=pd.DataFrame({'coefficients':result.params, 'p-value': result.pvalues,
                      'odds_ratio': np.exp(result.params)})
print(stat_df)

print("篩選重要的特徵變數")

significant_params=stat_df[stat_df['p-value']<=0.05].index
print(significant_params)

print("勝負比(Odds)")

cc = stat_df.loc[significant_params].sort_values('odds_ratio', ascending=False)['odds_ratio']
print(cc)
      
print("最後底定的模型：只保留重要的特徵變數")

y=df2['Attrition_Yes']
X=df2[significant_params]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model=sm.Logit(y_train,X_train)
result=model.fit()
print(result.summary())
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_06_knn_book_recommender

# 以KNN演算法實作書籍推薦

# 書籍資料
books = pd.read_csv(
    "C:/_git/vcs/_big_files/Scikit-learn_data/BX-Books.csv",
    sep=";",
    on_bad_lines="skip",
    low_memory=False,
    encoding="latin-1",
)
books.columns = [
    "ISBN",
    "bookTitle",
    "bookAuthor",
    "yearOfPublication",
    "publisher",
    "imageUrlS",
    "imageUrlM",
    "imageUrlL",
]

# 讀者資料
users = pd.read_csv(
    "C:/_git/vcs/_big_files/Scikit-learn_data/BX-Users.csv",
    sep=";",
    on_bad_lines="skip",
    encoding="latin-1",
)
users.columns = ["userID", "Location", "Age"]


# 評價資料
ratings = pd.read_csv(
    "C:/_git/vcs/_big_files/Scikit-learn_data/BX-Book-Ratings.csv",
    sep=";",
    on_bad_lines="skip",
    encoding="latin-1",
)
ratings.columns = ["userID", "ISBN", "bookRating"]

# 資料探索與分析

# 評價資料筆數
print(ratings.shape)

cc = ratings.head(10)
print(cc)

# 評價筆數繪圖
plt.rc("font", size=15)
sns.countplot(x="bookRating", data=ratings)
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")

show()

print("大部份書籍都未被評價")

print("書籍資料筆數")
print(books.shape)

print("讀者資料筆數")
print(users.shape)

print("讀者年齡分析")

users.Age.hist(bins=[0, 10, 20, 30, 40, 50, 100])
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig("tmp_system2.png", bbox_inches="tight")
show()

print("最多人評分的書籍")

rating_count = pd.DataFrame(ratings.groupby("ISBN")["bookRating"].count())
top_rating = rating_count.sort_values("bookRating", ascending=False).head()
print(top_rating)

print("最多人評分的書籍明細")

most_rated_books = pd.DataFrame(top_rating.index, index=np.arange(5), columns=["ISBN"])
most_rated_books_summary = pd.merge(most_rated_books, books, on="ISBN")
print(most_rated_books_summary)

print("書籍評價的平均得分")

average_rating = pd.DataFrame(ratings.groupby("ISBN")["bookRating"].mean())
average_rating["ratingCount"] = pd.DataFrame(
    ratings.groupby("ISBN")["bookRating"].count()
)
cc = average_rating.sort_values("ratingCount", ascending=False).head()
print(cc)


# 觀察: 最多人評分書籍的平均得分並沒有相對比較高
# 為確保統計顯著性，只保留讀者評分超過200次者，書籍評分超過100次者

counts1 = ratings["userID"].value_counts()
ratings = ratings[ratings["userID"].isin(counts1[counts1 >= 200].index)]
counts = ratings["bookRating"].value_counts()
ratings = ratings[ratings["bookRating"].isin(counts[counts >= 100].index)]

# User-Item matrix

ratings_pivot = ratings.pivot(index="userID", columns="ISBN").bookRating
userID = ratings_pivot.index
ISBN = ratings_pivot.columns
print(ratings_pivot.shape)
cc = ratings_pivot.head()
print(cc)

# 任選一本書 0316666343，計算與其他書籍的相關係數

test_book = "0316666343"
bones_ratings = ratings_pivot[test_book]
# 計算與其他書籍的相關係數
similar_to_bones = ratings_pivot.corrwith(bones_ratings)
corr_bones = pd.DataFrame(similar_to_bones, columns=["pearsonR"])
corr_bones.dropna(inplace=True)

# 結合書籍評價的平均得分
corr_summary = corr_bones.join(average_rating["ratingCount"])

# 只保留評價的平均得分>=300
high_corr_book = (
    corr_summary[corr_summary["ratingCount"] >= 300]
    .sort_values("pearsonR", ascending=False)
    .head(10)
)
print(high_corr_book)

# 取得書名

# 取得書名，扣除自己，取前9名
books_corr_to_bones = pd.DataFrame(
    high_corr_book.index[1:], index=np.arange(9), columns=["ISBN"]
)
corr_books = pd.merge(books_corr_to_bones, books, on="ISBN")
print(corr_books)

# KNN

# 合併評價表及書籍基本資料
combine_book_rating = pd.merge(ratings, books, on="ISBN")
columns = [
    "yearOfPublication",
    "publisher",
    "bookAuthor",
    "imageUrlS",
    "imageUrlM",
    "imageUrlL",
]
combine_book_rating = combine_book_rating.drop(columns, axis=1)
cc = combine_book_rating.head()
print(cc)

# 去除未評價書籍
combine_book_rating = combine_book_rating.dropna(axis=0, subset=["bookTitle"])
# 統計書籍的評價次數
book_ratingCount = (
    combine_book_rating.groupby(by=["bookTitle"])["bookRating"]
    .count()
    .reset_index()
    .rename(columns={"bookRating": "totalRatingCount"})[
        ["bookTitle", "totalRatingCount"]
    ]
)
cc = book_ratingCount.head()
print(cc)

# 合併評價次數及書籍基本資料
rating_with_totalRatingCount = combine_book_rating.merge(
    book_ratingCount, left_on="bookTitle", right_on="bookTitle", how="left"
)
cc = rating_with_totalRatingCount.head()
print(cc)

# 顯示評價次數的統計量
pd.set_option("display.float_format", lambda x: "%.3f" % x)
print(book_ratingCount["totalRatingCount"].describe())

# 顯示百分位數
print(book_ratingCount["totalRatingCount"].quantile(np.arange(0.9, 1, 0.01)))

# 熱門書籍：只有1%的書籍有超過50次的評分

# 篩選有超過50次評分的書籍
popularity_threshold = 50
rating_popular_book = rating_with_totalRatingCount.query(
    "totalRatingCount >= @popularity_threshold"
)
cc = rating_popular_book.head()
print(cc)

# 合併熱門書籍及讀者基本資料，使用美國及加拿大資料

# 合併熱門書籍及讀者基本資料
combined = rating_popular_book.merge(
    users, left_on="userID", right_on="userID", how="left"
)

# 只考慮美國及加拿大讀者
us_canada_user_rating = combined[combined["Location"].str.contains("usa|canada")]
us_canada_user_rating = us_canada_user_rating.drop("Age", axis=1)
cc = us_canada_user_rating.head()
print(cc)

print(us_canada_user_rating.shape)

# KNN模型訓練

from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# 去除重複值
us_canada_user_rating = us_canada_user_rating.drop_duplicates(["userID", "bookTitle"])
# 產生商品與讀者的樞紐分析表，會有很多 null value，均以0替代
us_canada_user_rating_pivot = us_canada_user_rating.pivot(
    index="bookTitle", columns="userID", values="bookRating"
).fillna(0)
# csr_matrix：壓縮稀疏矩陣，加速矩陣計算
us_canada_user_rating_matrix = csr_matrix(us_canada_user_rating_pivot.values)

# 找出相似商品，X為每一個讀者的評分
model_knn = NearestNeighbors(metric="cosine", algorithm="brute")
model_knn.fit(us_canada_user_rating_matrix)

# 測試

# 隨機抽取一件商品作預測
query_index = np.random.choice(us_canada_user_rating_pivot.shape[0])
distances, indices = model_knn.kneighbors(
    np.array(us_canada_user_rating_pivot.iloc[query_index, :]).reshape(1, -1),
    n_neighbors=6,
)

# 顯示最相似的前5名商品，並顯示距離(相似性)
for i in range(0, len(distances.flatten())):
    if i == 0:  # 第一筆是自己
        print(f"{us_canada_user_rating_pivot.index[query_index]} 的推薦:")
    else:
        print(
            f"{i}: {us_canada_user_rating_pivot.index[indices.flatten()[i]]}"
            + f", 距離: {distances.flatten()[i]:.2f}:"
        )

# SVD 矩陣分解(Matrix Factorization)

# User-Item Matrix
us_canada_user_rating_pivot2 = us_canada_user_rating.pivot(
    index="userID", columns="bookTitle", values="bookRating"
).fillna(0)
cc = us_canada_user_rating_pivot2.head()
print(cc)

cc = us_canada_user_rating_pivot2.shape
print(cc)

X = us_canada_user_rating_pivot2.values.T
print(X.shape)

# TruncatedSVD 降維至 12 個

# 萃取 12 個特徵
from sklearn.decomposition import TruncatedSVD

SVD = TruncatedSVD(n_components=12, random_state=17)
matrix = SVD.fit_transform(X)
print(matrix.shape)

# 依據 12 個特徵計算相關係數
corr = np.corrcoef(matrix)
print(corr.shape)

# 測試

# 取得 "The Green Mile" 書籍索引值
us_canada_book_list = list(us_canada_user_rating_pivot2.columns)
coffey_hands = us_canada_book_list.index("The Green Mile")
print("The Green Mile 書籍索引值:", coffey_hands)

# 依照索引值找出與其他書的相關係數
corr_coffey_hands = corr[coffey_hands]
print(corr_coffey_hands)

# 列出相關係數 > 80% 的書籍
us_canada_book_title = us_canada_user_rating_pivot2.columns
cc = list(us_canada_book_title[(corr_coffey_hands >= 0.8)])
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_11_naive_bayes_spam

# 垃圾信分類

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import WordNetLemmatizer
from wordcloud import WordCloud
import re

mails = pd.read_csv("./data/spam.csv", encoding="latin-1")
cc = mails.head()
print(cc)

# 資料整理
mails.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1, inplace=True)
cc = mails.head()
print(cc)

mails.rename(columns={"v1": "label", "v2": "message"}, inplace=True)
cc = mails.head()
print(cc)

cc = mails["label"].value_counts()
print(cc)

mails["label"] = mails["label"].map({"ham": 0, "spam": 1})
cc = mails.head()
print(cc)

# 設定停用詞
import string

stopword_list = set(stopwords.words("english") + list(string.punctuation))
# 詞形還原(Lemmatization)
lem = WordNetLemmatizer()


# 前置處理(Preprocessing)
def preprocess(text, is_lower_case=True):
    if is_lower_case:
        text = text.lower()
    tokens = word_tokenize(text)
    tokens = [token.strip() for token in tokens if len(token) > 1 and token != "..."]
    filtered_tokens = [token for token in tokens if token not in stopword_list]
    filtered_tokens = [lem.lemmatize(token) for token in filtered_tokens]
    filtered_text = " ".join(filtered_tokens)
    return filtered_text


mails["message"] = mails["message"].map(preprocess)
cc = mails.head()
print(cc)

# 文字雲

# 凸顯垃圾信的常用單字
spam_words = " ".join(list(mails[mails["label"] == 1]["message"]))
spam_wc = WordCloud(width=512, height=512).generate(spam_words)
plt.figure(figsize=(10, 8), facecolor="k")
plt.imshow(spam_wc)
plt.axis("off")
plt.tight_layout(pad=0)
show()

# 找出正常信件的常用單字
ham_words = " ".join(list(mails[mails["label"] == 0]["message"]))
ham_wc = WordCloud(width=512, height=512).generate(ham_words)
plt.figure(figsize=(10, 8), facecolor="k")
plt.imshow(ham_wc)
plt.axis("off")
plt.tight_layout(pad=0)
show()

# 使用 SciKit-learn TF-IDF

mails_message, labels = mails["message"].values, mails["label"].values
mails_message = mails_message.astype(str)

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(mails_message)
print(tfidf_matrix.shape)

# (5572, 8114)

cc = tfidf_vectorizer.get_feature_names_out()
print(cc)

no = 0
for i in tfidf_matrix.toarray()[0]:
    if i > 0.0:
        no += 1
print(no)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    tfidf_matrix.toarray(), labels, test_size=0.2
)
# 模型訓練

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(X_train, y_train)

# 模型評分

y_pred = clf.predict(X_test)
cc = accuracy_score(y_pred, y_test)
print(cc)
# 0.895067264573991

print(classification_report(y_test, y_pred))

cc = confusion_matrix(y_test, y_pred)
print(cc)

# 測試

message_processed_list = (
    "I cant pick the phone right now. Pls send a message",
    "Congratulations ur awarded $500",
    "Thanks for your subscription to Ringtone UK your mobile will be charged",
    "Oops, I'll let you know when my roommate's done",
    "FreeMsg Hey there darling it's been 3 week's now and no word back! I'd like some fun you up for it still? Tb ok! XxX std chgs to send, 憯1.50 to rcv",
    "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's",
)
X_new = tfidf_vectorizer.transform(message_processed_list)
cc = clf.predict(X_new.toarray())
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_09_scikit-learn_decision_tree_regression

# Scikit-learn迴歸樹測試

from sklearn.tree import DecisionTreeRegressor

# 生成隨機資料

rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))

# 訓練兩個模型

regr_1 = DecisionTreeRegressor(max_depth=2)
regr_1.fit(X, y)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_2.fit(X, y)

# DecisionTreeRegressor(max_depth=5)

# 預測

X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)

# 模型繪圖

plt.scatter(X, y, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(X_test, y_1, color="cornflowerblue", label="max_depth=2", linewidth=2)
plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 08_06_performance_metrics

# 計算及繪製混淆矩陣

df = pd.read_csv("C:/_git/vcs/_big_files/Scikit-learn_data/creditcard.csv")
cc = df.head()
print(cc)

# 觀察目標變數的各類別筆數

cc = df.Class.value_counts()
print(cc)

sns.countplot(x="Class", data=df)
show()

# 模型訓練與預測

X, y = df.drop(["Time", "Amount", "Class"], axis=1), df["Class"]

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 模型訓練
clf = LogisticRegression()

clf.fit(X_train, y_train)  # 學習訓練.fit

# 預測
y_pred = clf.predict(X_test)

# 準確率
cc = accuracy_score(y_test, y_pred)
print(cc)

# 計算混淆矩陣

# 取得混淆矩陣的4個格子

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print(tn, fp, fn, tp)

# (71072, 10, 40, 80)

# 常用的效能衡量指標計算

print(f"準確率(Accuracy)={(tn+tp) / (tn+fp+fn+tp)}")
print(f"精確率(Precision)={(tp) / (fp+tp)}")
print(f"召回率(Recall)={(tp) / (fn+tp)}")
print(f"F1 score={(2*tp) / (2*tp+fp+fn)}")

"""
準確率(Accuracy)=0.9992977725344794
精確率(Precision)=0.8888888888888888
召回率(Recall)=0.6666666666666666
F1 score=0.7619047619047619
"""

# Scikit-learn 分類報表

print(classification_report(y_test, y_pred))

# weighted average 驗算
cc = (1.00 * 71082 + 0.89 * 120) / (71082 + 120)
print(cc)

# 多類別的分類報表

# 3 類別
y_true = [0, 1, 2, 2, 2]
y_pred = [0, 0, 2, 2, 1]
print(classification_report(y_true, y_pred))

# 多類別的分類報表

# 3 類別
y_pred = [1, 2, 0]
y_true = [1, 1, 1]
print(classification_report(y_true, y_pred, labels=[1, 2, 3]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
ROC曲線
Receiver operating characteristic curve
接收者操作特徵曲線
"""
# 08_07_ draw_roc

# 繪製ROC曲線

# 載入資料

df = pd.read_csv("./data/roc_test_data.csv")
print(df)

"""
繪製ROC曲線
    計算第二欄的真(1)與假(0)的個數，假設分別為P及N，Y軸切成P格，X軸切成N格，如下圖。
    以第一欄降冪排序，從大排到小。
    依序掃描第二欄，若是1，就往『上』畫一格，反之，若是0，就往『右』畫一格，直到最後一列，如下圖。
"""

# 計算P及N個數

# 計算第二欄的真(1)與假(0)的個數，假設分別為P及N
P = df[df["actual"] == 1].shape[0]
N = df[df["actual"] == 0].shape[0]
print(f"P={P}, N={N}")

# X、Y軸每一格的大小
cc = y_unit = 1 / P
print(cc)
cc = X_unit = 1 / N
print(cc)

# P=11, N=7

# 根據第1欄降冪排序

df2 = df.sort_values(by="predict", ascending=False)
print(df2)

# 掃描表格每一列，第二欄若是1，就往『上』畫一格，反之，若是0，就往『右』畫一格

X, y = [], []
current_X, current_y = 0, 0
for row in df2.itertuples():
    # 若是1，Y加1
    if row[2] == 1:
        current_y += y_unit
    else:  # 若是0，X加1
        current_X += X_unit
    # 儲存每一點X/Y座標
    X.append(current_X)
    y.append(current_y)

X = np.array(X)
y = np.array(y)
print(X, y)

# 繪製ROC曲線

plt.title("ROC 曲線")
plt.plot(X, y, color="orange")
plt.plot([0, 1], [0, 1], "r--")
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel("真陽率")
plt.xlabel("偽陽率")
show()

# Scikit-Learn 作法

fpr, tpr, threshold = roc_curve(df["actual"], df["predict"])
print(f"偽陽率:\n{fpr}\n\n真陽率:\n{tpr}\n\n決策門檻:{threshold}")

"""
偽陽率:
[0.         0.         0.         0.14285714 0.14285714 0.28571429
 0.28571429 0.57142857 0.57142857 0.71428571 0.71428571 1.        ]

真陽率:
[0.         0.09090909 0.27272727 0.27272727 0.63636364 0.63636364
 0.81818182 0.81818182 0.90909091 0.90909091 1.         1.        ]

決策門檻:[1.99 0.99 0.8  0.73 0.56 0.48 0.42 0.32 0.22 0.11 0.1  0.03]
"""

# 繪製ROC曲線

auc1 = auc(fpr, tpr)
plt.title("ROC 曲線")
plt.plot(fpr, tpr, color="orange", label="AUC = %0.2f" % auc1)
plt.legend(loc="lower right")
plt.plot([0, 1], [0, 1], "r--")
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel("真陽率")
plt.xlabel("偽陽率")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 08_09_ credit_card_fraud_detection

# 信用卡詐欺偵測

# 載入資料

df = pd.read_csv("C:/_git/vcs/_big_files/Scikit-learn_data/creditcard.csv")
cc = df.head()
print(cc)

# 觀察目標變數的各類別筆數

cc = df.Class.value_counts()
print(cc)

sns.countplot(x="Class", data=df)
show()

X, y = df.drop(["Time", "Amount", "Class"], axis=1), df["Class"]

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 模型訓練
clf = LogisticRegression()

clf.fit(X_train, y_train)  # 學習訓練.fit

# 預測
y_pred = clf.predict(X_test)

# 準確率
cc = accuracy_score(y_test, y_pred)
print(cc)

# K折交叉驗證
scores = cross_val_score(estimator=clf, X=X_test, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.3f}, 標準差: {np.std(scores):.3f}")

"""
K折分數: [0.99915742 0.99929785 0.9988764  0.9997191  0.99901685 0.99901685
 0.9991573  0.99957865 0.9988764  0.9994382 ]
平均值: 0.999, 標準差: 0.000
"""

# 分類報告
print(classification_report(y_test, y_pred))

# 繪製ROC曲線
y_pred_proba = clf.predict_proba(X_test)[:, 1]
fpr, tpr, threshold = roc_curve(y_test, y_pred_proba)
auc1 = auc(fpr, tpr)
plt.title("ROC 曲線")
plt.plot(fpr, tpr, color="orange", label="AUC = %0.2f" % auc1)
plt.legend(loc="lower right")
plt.plot([0, 1], [0, 1], "r--")
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel("真陽率")
plt.xlabel("偽陽率")
show()

# 從寬認定詐欺行為

y_pred_proba = clf.predict_proba(X_test)[:, 1]
y_pred = y_pred_proba >= 0.3
print(classification_report(y_test, y_pred))

# Over-sampling -- SMOTE

# !pip install -U imbalanced-learn

from imblearn.over_sampling import SMOTE

print(df.Class.value_counts())
smote = SMOTE()
X_new, y_new = smote.fit_resample(X, y)
cc = len(y_new[y_new == 0]), len(y_new[y_new == 1])
print(cc)

# 模型訓練與評估

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X_new, y_new)

# 模型訓練
clf = LogisticRegression()

clf.fit(X_train, y_train)  # 學習訓練.fit

# 預測
y_pred = clf.predict(X_test)

# 準確率
cc = accuracy_score(y_test, y_pred)
print(cc)

# K折交叉驗證
scores = cross_val_score(estimator=clf, X=X_test, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.3f}, 標準差: {np.std(scores):.3f}")

"""
K折分數: [0.94499156 0.94379572 0.94569499 0.94541362 0.94442881 0.94288126
 0.94231851 0.95040799 0.94336968 0.94379177]
平均值: 0.945, 標準差: 0.002
"""

# 分類報告
print(classification_report(y_test, y_pred))

# imbalanced-learn 分類報告
print(classification_report_imbalanced(y_test, y_pred))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_07_dbscan_simple_test

# 以密度為基礎的集群(Density-based spatial clustering of applications with noise, DBSCAN)

from sklearn.cluster import DBSCAN

# 生成資料
X = np.array([[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]])
print(X)

# 模型訓練

model = DBSCAN(eps=3, min_samples=2)

model.fit(X)  # 學習訓練.fit
print(model.labels_)

X, y = make_moons(n_samples=200, noise=0.05, random_state=9487)
plt.scatter(X[:, 0], X[:, 1])
show()

# 模型訓練，繪製結果

db = DBSCAN(eps=0.2, min_samples=5, metric="euclidean")

y_pred = db.fit_predict(X)

plt.scatter(
    X[y_pred == 0, 0],
    X[y_pred == 0, 1],
    c="lightblue",
    marker="o",
    s=40,
    edgecolor="black",
    label="cluster 1",
)
plt.scatter(
    X[y_pred == 1, 0],
    X[y_pred == 1, 1],
    c="red",
    marker="s",
    s=40,
    edgecolor="black",
    label="cluster 2",
)
plt.legend()
show()

# 另一個範例，參閱Demo of DBSCAN clustering algorithm

centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=750, centers=centers, cluster_std=0.4, random_state=9487
)

X = StandardScaler().fit_transform(X)

# 繪製資料
plt.figure(figsize=(10, 8))
plt.scatter(X[:, 0], X[:, 1])
show()

# 模型訓練
labels = DBSCAN(eps=0.3, min_samples=10).fit_predict(X)

# 計算集群內樣本數、雜訊點個數
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print(f"集群數={n_clusters_}")
print(f"雜訊點個數={n_noise_}")

# 集群數=3
# 雜訊點個數=18

# 模型評估
print(f"Homogeneity: {metrics.homogeneity_score(labels_true, labels):.3f}")
print(f"Completeness: {metrics.completeness_score(labels_true, labels):.3f}")
print(f"V-measure: {metrics.v_measure_score(labels_true, labels):.3f}")
print(f"Adjusted Rand Index: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
print(
    "Adjusted Mutual Information:"
    f" {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}"
)

# [平均]輪廓係數 silhouette_score
print(f"Silhouette Coefficient: {metrics.silhouette_score(X, labels):.3f}")

"""
Homogeneity: 0.953
Completeness: 0.883
V-measure: 0.917
Adjusted Rand Index: 0.952
Adjusted Mutual Information: 0.916
Silhouette Coefficient: 0.626
"""

# 繪製結果

plt.figure(figsize=(10, 8))
unique_labels = set(labels)
core_samples_mask = np.zeros_like(labels, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True

colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = labels == k

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=14,
    )

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=6,
    )

plt.title(f"Estimated number of clusters: {n_clusters_}")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 整體學習的錯誤率計算

from scipy.special import comb

# 計算整體學習的錯誤率


def ensemble_error(n_classifier, error):
    k_start = int(math.ceil(n_classifier / 2.0))
    probs = [
        comb(n_classifier, k) * error**k * (1 - error) ** (n_classifier - k)
        for k in range(k_start, n_classifier + 1)
    ]
    return sum(probs)


cc = ensemble_error(n_classifier=11, error=0.25)
print(cc)

# 0.03432750701904297

# 測試各種錯誤率，並繪圖

error_range = np.arange(0.0, 1.01, 0.01)
ens_errors = [ensemble_error(n_classifier=11, error=error) for error in error_range]

# 修正中文亂碼
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

plt.plot(error_range, ens_errors, label="整體學習", linewidth=2)

plt.plot(error_range, error_range, linestyle="--", label="個別模型", linewidth=2)

plt.title("錯誤率比較", fontsize=18)
plt.xlabel("個別模型錯誤率", fontsize=14)
plt.ylabel("整體學習錯誤率", fontsize=14)
plt.legend(loc="upper left", fontsize=14)
plt.grid(alpha=0.5)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 標註傳播(Label propagation)測試

from sklearn.semi_supervised import LabelPropagation

X, y = make_classification(
    n_samples=1000, n_features=2, n_informative=2, n_redundant=0, random_state=9487
)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, stratify=y)

# 設定 50% 資料為沒有標註(-1)
X_train_lab, X_test_unlab, y_train_lab, y_test_unlab = train_test_split(
    X_train, y_train, test_size=0.5, stratify=y_train
)
X_train_mixed = np.concatenate((X_train_lab, X_test_unlab))
nolabel = [-1 for _ in range(len(y_test_unlab))]
y_train_mixed = np.concatenate((y_train_lab, nolabel))
cc = y_train_mixed.shape
print(cc)

# (500,)

# Label propagation 模型訓練與評估

clf = LabelPropagation()

clf.fit(X_train_mixed, y_train_mixed)  # 學習訓練.fit

cc = clf.score(X_test, y_test)
print(cc)

# 0.856

clf2 = LogisticRegression()

clf2.fit(X_train_lab, y_train_lab)  # 學習訓練.fit

cc = clf2.score(X_test, y_test)
print(cc)

# 0.848

# 取得訓練資料標註

tran_labels = clf.transduction_
cc = tran_labels.shape
print(cc)
# (500,)

# 再依Label propagation傳播結果進行模型訓練與評估

clf3 = LogisticRegression()

clf3.fit(X_train_mixed, tran_labels)  # 學習訓練.fit

cc = clf3.score(X_test, y_test)
print(cc)
# 0.862

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# LabelSpreading 測試

from sklearn.semi_supervised import LabelSpreading

# 載入資料集
X, y = make_classification(
    n_samples=1000, n_features=2, n_informative=2, n_redundant=0, random_state=9487
)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, stratify=y)

# 設定 50% 資料為沒有標註(-1)

X_train_lab, X_test_unlab, y_train_lab, y_test_unlab = train_test_split(
    X_train, y_train, test_size=0.5, random_state=1, stratify=y_train
)
X_train_mixed = np.concatenate((X_train_lab, X_test_unlab))
nolabel = [-1 for _ in range(len(y_test_unlab))]
y_train_mixed = np.concatenate((y_train_lab, nolabel))
cc = y_train_mixed.shape
print(cc)
# (500,)

# LabelSpreading 模型訓練與評估

clf = LabelSpreading()

clf.fit(X_train_mixed, y_train_mixed)  # 學習訓練.fit

cc = clf.score(X_test, y_test)
print(cc)
# 0.854

clf2 = LogisticRegression()

clf2.fit(X_train_lab, y_train_lab)  # 學習訓練.fit

cc = clf2.score(X_test, y_test)
print(cc)

# 0.848

# 取得訓練資料標註

tran_labels = clf.transduction_
cc = tran_labels.shape
print(cc)
# (500,)

# 再依LabelSpreading傳播結果進行模型訓練與評估

clf3 = LogisticRegression()

clf3.fit(X_train_mixed, tran_labels)  # 學習訓練.fit

cc = clf3.score(X_test, y_test)
print(cc)
# 0.858

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 自行計算 Shapley value

from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import plot_tree

# 載入資料

with open("./data/housing.data", encoding="utf8") as f:
    data = f.readlines()
all_fields = []
for line in data:
    line2 = line[1:].replace("   ", " ").replace("  ", " ")
    fields = []
    for item in line2.split(" "):
        fields.append(float(item.strip()))
        if len(fields) == 14:
            all_fields.append(fields)
df = pd.DataFrame(all_fields)
df.columns = "CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV".split(",")
cc = df.head()
print(cc)

# 模型訓練

y = df["MEDV"]
df = df[["RM", "LSTAT", "DIS", "NOX"]]

clf = DecisionTreeRegressor(max_depth=3)

clf.fit(df, y)  # 學習訓練.fit

fig = plt.figure(figsize=(20, 5))
ax = fig.add_subplot(111)
_ = plot_tree(clf, ax=ax, feature_names=df.columns)
show()

# 以 SHAP 套件計算 Shapley value

import shap
import tabulate

explainer = shap.TreeExplainer(clf)
shap_values = explainer.shap_values(df[:1])  # 第一筆資料
print(
    tabulate.tabulate(
        pd.DataFrame(
            {
                "shap_value": shap_values.squeeze(),
                "feature_value": df[:1].values.squeeze(),
            },
            index=df.columns,
        ),
        tablefmt="github",
        headers="keys",
    )
)

# Shapley value + Y平均數 = 預測值

cc = shap_values.sum() + y.mean(), clf.predict(df[:1])[0]
print(cc)

# (22.905200000000004, 22.9052)

# 自行計算 Shapley value

from itertools import combinations
import scipy


# 計算特定組合的邊際貢獻
def pred_tree(clf, coalition, row, node=0):
    left_node = clf.tree_.children_left[node]
    right_node = clf.tree_.children_right[node]
    is_leaf = left_node == right_node

    if is_leaf:
        return clf.tree_.value[node].squeeze()

    feature = row.index[clf.tree_.feature[node]]
    if feature in coalition:
        if row.loc[feature] <= clf.tree_.threshold[node]:
            # go left
            return pred_tree(clf, coalition, row, node=left_node)
        else:  # go right
            return pred_tree(clf, coalition, row, node=right_node)

    # take weighted average of left and right
    wl = clf.tree_.n_node_samples[left_node] / clf.tree_.n_node_samples[node]
    wr = clf.tree_.n_node_samples[right_node] / clf.tree_.n_node_samples[node]
    value = wl * pred_tree(clf, coalition, row, node=left_node)
    value += wr * pred_tree(clf, coalition, row, node=right_node)
    return value


# 計算特定組合的平均邊際貢獻
def make_value_function(clf, row, col):
    def value(c):
        marginal_gain = pred_tree(clf, c + [col], row) - pred_tree(clf, c, row)
        num_coalitions = scipy.special.comb(len(row) - 1, len(c))
        return marginal_gain / num_coalitions

    return value


# 各種組合
def make_coalitions(row, col):
    rest = [x for x in row.index if x != col]
    for i in range(len(rest) + 1):
        for x in combinations(rest, i):
            yield list(x)


# 計算 Shapley value
def compute_shap(clf, row, col):
    v = make_value_function(clf, row, col)
    return sum([v(coal) / len(row) for coal in make_coalitions(row, col)])


# 顯示 Shapley value
print(
    tabulate.tabulate(
        pd.DataFrame(
            {
                "shap_value": shap_values.squeeze(),
                "my_shap": [
                    compute_shap(clf, df[:1].T.squeeze(), x) for x in df.columns
                ],
                "feature_value": df[:1].values.squeeze(),
            },
            index=df.columns,
        ),
        tablefmt="github",
        headers="keys",
    )
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_07_surprise_test

# Surprise 測試

from surprise import SVD
from surprise import KNNBasic
from surprise import Dataset
from surprise import accuracy

# 載入內建 movielens-100k 資料集
data = Dataset.load_builtin("ml-100k")
print("user id\titem id\trating\ttimestamp")
cc = data.raw_ratings[:10]
print(cc)

# 資料分割

from surprise.model_selection import train_test_split

# 切分為訓練及測試資料，測試資料佔 20%
trainset, testset = train_test_split(data, test_size=0.2)

# 模型訓練

# 使用 KNN 演算法
model = KNNBasic()

# 訓練
model.fit(trainset)

# 模型評分

# 測試
predictions = model.test(testset)

# 計算 RMSE
accuracy.rmse(predictions)

# RMSE: 0.9874

# SVD

model = SVD()
model.fit(trainset)
predictions = model.test(testset)
accuracy.rmse(predictions)

# RMSE: 0.9405

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 一個很大的範例 ST
"""
探索性數據分析（EDA）

EDA指對已有的數據用可視化等手段探索數據的結構和規律的一種數據分析方法，
其目的是最大化對數據的直覺，完成這個事情的方法是結合統計學的圖形以各種形式展現出來。
在深入機器學習或統計建模之前，EDA是一個重要的步驟，
這是因為它提供了為現有問題開發適當模型并正確解釋其結果所需的來龍去脈。
EDA通常涉及以下幾種方法的組合：
.原始數據集中每個字段的單變量可視化和匯總統計
.數據集中每個變量與感興趣目標變量之間的關系的雙變量可視化和匯總統計
.多元可視化以了解數據中不同字段之間的交互作用
.降維以了解數據,通過將數據折疊成幾個小數據點讓觀察值聚類成有區別的小組，
可以更容易地識別行為模式
"""

import scipy.stats as stats
import sklearn.linear_model as linear_model

# import xgboost as xgb
from sklearn.model_selection import KFold
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

# 共 1460 筆資料, 81 欄位
train = pd.read_csv("data/houseprice.csv")

print("訓練數據集基本信息")
# many print(train.info())
print("train.shape :", train.shape)  # 1460 X 81

# 前幾筆資料 print(train.head())

# 1.1 首先，區分出數據中的數值型變量和類別型變量
# 數值型變量

quantitative = [f for f in train.columns if train.dtypes[f] != "object"]
quantitative.remove("SalePrice")
quantitative.remove("Id")

print("quantitative len :", len(quantitative))

# 類別型變量
qualitative = [f for f in train.columns if train.dtypes[f] == "object"]

ccs = [
    "FullBath",
    "HalfBath",
    "TotRmsAbvGrd",
    "Fireplaces",
    "GarageYrBlt",
    "GarageCars",
    "OverallQual",
]
for col in ccs:
    if col in quantitative:
        quantitative.remove(col)
    if not col in qualitative:
        qualitative.append(col)

print("訓練集樣本數量：{}".format(train.shape[0]))  # 1460
print("數值型變量共有：{}".format(len(quantitative)))  # 29
print("類別型變量共有：{}".format(len(qualitative)))  # 50

# 1.2查看缺失值的分布情況

missing = train.isnull().sum() / train.shape[0]

print("missing資料")
print(missing.head())

missing = missing[missing > 0]
print("有缺失值的變量共有 : {}".format(len(missing)))  # 19

missing.sort_values(inplace=True)
print("缺失率超過50%的有 {} 個".format(len(missing[missing >= 0.5])))  # 5

print(missing[missing >= 0.5])

missing.plot.bar()
plt.title("有缺失值的變量")
show()

print("可以直接刪除這幾個變量")

missing_cols = missing[missing >= 0.5].index.tolist()

for col in missing_cols:
    if col in quantitative:
        quantitative.remove(col)
    if col in qualitative:
        qualitative.remove(col)

print("數值型變量共有：{}".format(len(quantitative)))  # 29
print("類別型變量共有：{}".format(len(qualitative)))  # 45

# 2 數值型變量
# 2.1 查看目標變量saleprice是否服從正態分布

import scipy.stats as st

y = train["SalePrice"]

sns.distplot(y, kde=False)
plt.title("預設方法")
show()

sns.distplot(y, kde=True, fit=st.johnsonsu)
plt.title("使用 Johnson SU")
show()

sns.distplot(y, kde=False, fit=st.norm)
plt.title("使用 Normal")
show()

sns.distplot(y, kde=False, fit=st.lognorm)
plt.title("使用 Log Normal")
show()

# 另一種查看是否服從正態分布的可視化方法
sns.distplot(train["SalePrice"], fit=st.norm)
plt.title("使用 Normal")
show()

res = st.probplot(train["SalePrice"], plot=plt)
show()

# 把房價做對數變換后再看
SalePrice_log = np.log(train["SalePrice"])
# transformed histogram and normal probability plot
sns.distplot(SalePrice_log, fit=st.norm)
show()

res = st.probplot(SalePrice_log, plot=plt)
print(res)

show()

"""
((array([-3.30513952, -3.04793228, -2.90489705, ...,  2.90489705,
,          3.04793228,  3.30513952]),
,  array([ 10.46024211,  10.47194981,  10.54270639, ...,  13.34550693,
,          13.5211395 ,  13.53447303])),
, (0.39826223081618845, 12.024050901109383, 0.99537614756366088))

顯然，房價本身不服從正態分布，是不能直接用來做回歸建模的。但是經過對數轉換之后，就好了很多。
對于其它的數值型變量，也同樣要做分布的正態性檢驗.
檢驗方法就用：夏皮羅-威爾克(Shapiro-Wilk)法檢驗數據正態性,即W檢驗。
"""

check_normality = lambda x: stats.shapiro(x.fillna(0))[1] < 0.01

normal = pd.DataFrame(train[quantitative])
normal = normal.apply(check_normality)

print(normal.sort_values(ascending=False).head(4))

normal = normal < 0.01
print(not normal.any())

"""
YrSold          True
LowQualFinSF    True
LotFrontage     True
LotArea         True
dtype: bool
True

可以發現所有的數值型變量都沒能通過正態性分布檢驗，都需要做轉換。
我們可以把所有的數值型變量的分布曲線都畫出來，從可視化角度進一步驗證這個判斷
"""

f = pd.melt(train, value_vars=quantitative)
g = sns.FacetGrid(f, col="variable", col_wrap=2, sharex=False, sharey=False)
g = g.map(sns.distplot, "value")
show()

df = pd.DataFrame(
    {"A": {0: "a", 1: "b", 2: "c"}, "B": {0: 1, 1: 3, 2: 5}, "C": {0: 2, 1: 4, 2: 6}}
)
print(df)

pd.melt(df, id_vars=["A"], value_vars=["B", "C"])
print(df)

# 看起來TotalBsmtSF, KitchenAbvGr, LotFrontage, LotArea這幾個變量似乎更適合做些變型，以使其服從正態分布。
# 2.2 異常值分析
# 對saleprice做標準化后再看

"""
# NG
saleprice_scaled = StandardScaler().fit_transform(train["SalePrice"][:, np.newaxis])
low_range = saleprice_scaled[saleprice_scaled[:, 0].argsort()][:10]
high_range = saleprice_scaled[saleprice_scaled[:, 0].argsort()][-10:]
print("outer range (low) of the distribution:")
print(low_range)
print("\nouter range (high) of the distribution:")
print(high_range)
"""

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

"""

# 低房價并沒有太多異常，但是高房價有兩個超過了7，雖然不一定是異常值，但是要小心
# 2.3 查看數值型變量和待預測變量之間的相關性
# 常用pearson相關系數，它是用有前提條件，并且是有局限的——判斷線性相關，非線性相關它是無能為力的。
# Spearman相關系數 vs pearson相關系數的優點：對于數據分布沒有要求。也叫秩和。


def spearman(frame, features):
    spr = pd.DataFrame()
    spr["feature"] = features
    spr["spearman"] = [frame[f].corr(frame["SalePrice"], "spearman") for f in features]
    spr = spr.sort_values("spearman")
    plt.figure(figsize=(6, 0.2 * len(features)))
    sns.barplot(data=spr, y="feature", x="spearman", orient="h")
    return spr


features = quantitative

spr = spearman(train, features)
show()

# 刪除相關系數小于0.3的變量

print("數值型變量共有：{}".format(len(quantitative)))
print("類別型變量共有：{}".format(len(qualitative)))

for col in spr[abs(spr["spearman"]) < 0.3].feature:
    if col in quantitative:
        quantitative.remove(col)

print("數值型變量共有：{}".format(len(quantitative)))
print("類別型變量共有：{}".format(len(qualitative)))

"""
數值型變量共有：29
類別型變量共有：46
數值型變量共有：12
類別型變量共有：46
"""

# 2.4 用散點圖觀察數值型變量之間的關系
# scatterplot

from copy import copy

sns.set(font_scale=2)
cols1 = copy(quantitative)
cols1.append("SalePrice")
sns.pairplot(train[cols1].fillna(0.0), height=2.5)
show()

# scatterplot

sns.set(font_scale=2)

cols1 = copy(quantitative[:6])

cols1.append("SalePrice")

sns.pairplot(train[cols1].fillna(0.0), height=2.5)

cols2 = copy(quantitative[6:])

cols2.append("SalePrice")

sns.pairplot(train[cols2].fillna(0.0), height=2.5)

show()

"""
3.類別型變量
對于類別型的變量，要觀察目標變量（sale_price）在類別的各個取值上的分布情況；用分組箱線圖
對于類別型變量的缺失值，不再用0填充，而是用一個特殊的值'Missing'填充。
"""

for c in qualitative:
    train[c] = train[c].astype("category")
    if train[c].isnull().any():
        train[c] = train[c].cat.add_categories(["MISSING"])
        train[c] = train[c].fillna("MISSING")


def boxplot(x, y, **kwargs):
    sns.boxplot(x=x, y=y)
    x = plt.xticks(rotation=90)


f = pd.melt(train, id_vars=["SalePrice"], value_vars=qualitative)
# g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False, size=5)
g = sns.FacetGrid(f, col="variable", col_wrap=2, sharex=False, sharey=False)
g = g.map(boxplot, "value", "SalePrice")

show()

"""
看起來像LotConfig、LandSlope這樣的變量，對于房價的影響似乎不大。
Neighborhood對房價有影響。然后每個類別的不同子類之間看起來似乎也有差別。
overallQual的值太多。

具體到一個分類指標和數值型變量之間的相關關系，我們可以用方差分析進行檢查。
3.2 方差分析
"""


def anova(frame):
    anv = pd.DataFrame()
    anv["feature"] = qualitative
    pvals = []
    for c in qualitative:
        samples = []
        for cls in frame[c].unique():
            s = frame[frame[c] == cls]["SalePrice"].values
            samples.append(s)
        pval = stats.f_oneway(*samples)[1]
        pvals.append(pval)
    anv["pval"] = pvals
    return anv.sort_values("pval")


a = anova(train)
a["disparity"] = np.log(1.0 / a["pval"].values)
sns.barplot(data=a, x="feature", y="disparity")
x = plt.xticks(rotation=90)
show()


"""
這里我們用了方差分析，來看每一個類別變量和預測變量Sale_price之間是否有相關關系。
因為我們最后得到了個p值，p>0.05說明樣本的分組之間沒有顯著性差異，
p值越小說明差異越顯著。
因為我們想用一個類似于“變異度”的指標——“差異度”，
我們希望這個指標越大，說明差異越明顯。也就是想要一個同向變化的指標，所以對p值取了個倒數。
僅此而已。
3.3 對于這些分類變量的每個值做正確編碼
另一種編碼方式是OneHotEncoding或者dummy
"""


def encode(frame, feature):
    ordering = pd.DataFrame()
    ordering["val"] = frame[feature].unique()
    ordering.index = ordering.val
    ordering["spmean"] = (
        frame[[feature, "SalePrice"]].groupby(feature).mean()["SalePrice"]
    )
    ordering = ordering.sort_values("spmean")
    ordering["ordering"] = range(1, ordering.shape[0] + 1)
    ordering = ordering["ordering"].to_dict()

    for cat, o in ordering.items():
        frame.loc[frame[feature] == cat, feature + "_E"] = o


qual_encoded = []
for q in qualitative:
    encode(train, q)
    qual_encoded.append(q + "_E")

print(qual_encoded)

"""
['MSZoning_E', 'Street_E', 'LotShape_E', 'LandContour_E', 'Utilities_E', 'LotConfig_E', 'LandSlope_E', 'Neighborhood_E', 'Condition1_E', 'Condition2_E', 'BldgType_E', 'HouseStyle_E', 'RoofStyle_E', 'RoofMatl_E', 'Exterior1st_E', 'Exterior2nd_E', 'MasVnrType_E', 'ExterQual_E', 'ExterCond_E', 'Foundation_E', 'BsmtQual_E', 'BsmtCond_E', 'BsmtExposure_E', 'BsmtFinType1_E', 'BsmtFinType2_E', 'Heating_E', 'HeatingQC_E', 'CentralAir_E', 'Electrical_E', 'KitchenQual_E', 'Functional_E', 'FireplaceQu_E', 'GarageType_E', 'GarageFinish_E', 'GarageQual_E', 'GarageCond_E', 'PavedDrive_E', 'SaleType_E', 'SaleCondition_E', 'FullBath_E', 'HalfBath_E', 'TotRmsAbvGrd_E', 'Fireplaces_E', 'GarageYrBlt_E', 'GarageCars_E', 'OverallQual_E']
"""
print(train.head(3))

"""
	Id	MSSubClass	MSZoning	LotFrontage	LotArea	Street	Alley	LotShape	LandContour	Utilities	...	PavedDrive_E	SaleType_E	SaleCondition_E	FullBath_E	HalfBath_E	TotRmsAbvGrd_E	Fireplaces_E	GarageYrBlt_E	GarageCars_E	OverallQual_E
0	1	60	RL	65.0	8450	Pave	NaN	Reg	Lvl	AllPub	...	3.0	5.0	5.0	3.0	3.0	8.0	1.0	86.0	3.0	7.0
1	2	20	RL	80.0	9600	Pave	NaN	Reg	Lvl	AllPub	...	3.0	5.0	5.0	3.0	2.0	5.0	2.0	57.0	3.0	6.0
2	3	60	RL	68.0	11250	Pave	NaN	IR1	Lvl	AllPub	...	3.0	5.0	5.0	3.0	3.0	5.0	2.0	91.0	3.0	7.0
,

3 rows × 127 columns
,

"""

print(train["GarageQual_E"].value_counts())

"""
4.0    1311
,2.0      81
,3.0      48
,5.0      14
,6.0       3
,1.0       3
,Name: GarageQual_E, dtype: int64

3.4.查看衍生變量和房價的Spearman相關性
對于相關性的檢測我們使用的是Spearman correlation，
這種檢驗方法的好處是即使是非線性相關也能檢測出來。
"""

sns.set(font_scale=1.2)


def spearman(frame, features):
    spr = pd.DataFrame()
    spr["feature"] = features
    spr["spearman"] = [frame[f].corr(frame["SalePrice"], "spearman") for f in features]
    spr = spr.sort_values("spearman")
    plt.figure(figsize=(6, 0.2 * len(features)))
    sns.barplot(data=spr, y="feature", x="spearman", orient="h")


features = qual_encoded
spearman(train, features)
show()

"""
顯然，OverallQual和房價的關系最明顯。房子的鄰居和位置看起來也是有影響的。
3.5 觀察變量之間的相關性
回歸模型對于變量共線的容忍度差，所以，我們需要考慮變量之間的相關性。
用相關系數矩陣的熱力圖即可。
"""

sns.set(font_scale=1)

corr = train[quantitative + ["SalePrice"]].corr("spearman")

sns.heatmap(corr, cbar=True, annot=True, square=True, fmt=".2f", annot_kws={"size": 10})

show()

# from functools import partial
# # my_heatmap=partial(sns.heatmap,cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)

corr = train[qual_encoded + ["SalePrice"]].corr()
sns.heatmap(corr, cbar=True, annot=True, square=True, fmt=".2f", annot_kws={"size": 10})

show()

corr = pd.DataFrame(
    np.zeros([len(quantitative) + 1, len(qual_encoded) + 1]),
    index=quantitative + ["SalePrice"],
    columns=qual_encoded + ["SalePrice"],
)
for q1 in quantitative + ["SalePrice"]:
    for q2 in qual_encoded + ["SalePrice"]:
        corr.loc[q1, q2] = train[q1].corr(train[q2])

sns.heatmap(corr, cbar=True, annot=True, square=True, fmt=".2f", annot_kws={"size": 10})

show()

"""
3.6 觀察所有變量（包括衍生變量）和目標變量之間的關系
現在所有類別型變量也做了重新編碼，編碼成數值型。所有所有的特征都可以看作是數值型的了。
于是，我們可以再次全景式觀察變量和目標變量之間的關系。
"""


def pairplot(x, y, **kwargs):
    ax = plt.gca()
    ts = pd.DataFrame({"time": x, "val": y})
    ts = ts.groupby("time").mean()
    ts.plot(ax=ax)
    plt.xticks(rotation=90)


# 畫散點圖
sns.set(style="ticks", color_codes=True)

f = pd.melt(train, id_vars=["SalePrice"], value_vars=quantitative + qual_encoded)
# g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False, size=5)
g = sns.FacetGrid(f, col="variable", col_wrap=2, sharex=False, sharey=False)
g = g.map(pairplot, "value", "SalePrice")

show()

"""
看起來，YearBuild、1stFlrSF, 2ndFlrSF, Neighborhood_E There are lots of nonlinearities this may be the cause why some variables wont be selected by Lasso/Lars. Some factors like YearBuilt, 1stFlrSF, 2ndFlrSF, Neighborhood_E look like they would benefit from adding quadratic term to regression. But on the other hand this will most probably provoke overfit.

觀察的結果提示我們，有些變量可以嘗試做些變換，比如平方變換。

4.高級內容

考慮數據本身是否分群，如果分群，就可以用分段回歸。

接下來，考慮是否可以分段進行回歸。

我們把房價200000作為分界點，之下的作為普通住宅，之上的作為豪宅，
然后看看在這樣分開后，那些數值型變量的均值有多大差異。
"""

features = quantitative
standard = train[train["SalePrice"] < 200000]
pricey = train[train["SalePrice"] >= 200000]

diff = pd.DataFrame()
diff["feature"] = features
diff["difference"] = [
    (pricey[f].fillna(0.0).mean() - standard[f].fillna(0.0).mean())
    / (standard[f].fillna(0.0).mean())
    for f in features
]

sns.barplot(data=diff, x="feature", y="difference")
x = plt.xticks(rotation=90)

print(diff)

show()

"""
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

我們用tnse方法，把每個高維樣本映射到二維平面上的點。
然后我們對樣本做標準化處理，處理之后做PCA，提取前30個主成分。也就是把樣本的特征降維到30個特征。
對這30個特征的樣本聚類，聚成5類。
在把這5類用可視化的方法會出來，看看是否有聚集趨勢。
"""

features = quantitative + qual_encoded
model = TSNE(n_components=2, random_state=0, perplexity=50)
X = train[features].fillna(0.0).values
tsne = model.fit_transform(X)

std = StandardScaler()
s = std.fit_transform(X)

pca = PCA(n_components=40)

pca.fit(s)  # 學習訓練.fit

pc = pca.transform(s)

kmeans = KMeans(n_clusters=5)

kmeans.fit(pc)  # 學習訓練.fit

fr = pd.DataFrame({"tsne1": tsne[:, 0], "tsne2": tsne[:, 1], "cluster": kmeans.labels_})

sns.lmplot(data=fr, x="tsne1", y="tsne2", hue="cluster", fit_reg=False)

show()

print(np.sum(pca.explained_variance_ratio_))

"""
0.846903058622
看起來聚集趨勢并不明顯，所以分段回歸的意義似乎不大。
另外40個主成分能解釋84%的方差。
"""

y = train["SalePrice"].values


def johnson(y):
    gamma, eta, epsilon, lbda = stats.johnsonsu.fit(y)
    yt = gamma + eta * np.arcsinh((y - epsilon) / lbda)
    return yt, gamma, eta, epsilon, lbda


def johnson_inverse(y, gamma, eta, epsilon, lbda):
    return lbda * np.sinh((y - gamma) / eta) + epsilon


yt, g, et, ep, l = johnson(y)
yt2 = johnson_inverse(yt, g, et, ep, l)

sns.distplot(yt)
show()

sns.distplot(yt2)
show()

# 5.最后建模


def error(actual, predicted):
    actual = np.log(actual)
    predicted = np.log(predicted)
    return np.sqrt(np.sum(np.square(actual - predicted)) / len(actual))


def log_transform(feature):
    train[feature] = np.log1p(train[feature].values)


def quadratic(feature):
    train[feature + "2"] = train[feature] ** 2


# 下面這些特征做log轉化
log_transform("GrLivArea")
log_transform("1stFlrSF")
log_transform("2ndFlrSF")
log_transform("TotalBsmtSF")
log_transform("LotArea")
log_transform("LotFrontage")
log_transform("KitchenAbvGr")
log_transform("GarageArea")

# 下面這些特征取平方轉換
# quadratic('OverallQual') fail
quadratic("YearBuilt")
quadratic("YearRemodAdd")
quadratic("TotalBsmtSF")
quadratic("2ndFlrSF")
quadratic("Neighborhood_E")
quadratic("RoofMatl_E")
quadratic("GrLivArea")

qdr = [
    "OverallQual2",
    "YearBuilt2",
    "YearRemodAdd2",
    "TotalBsmtSF2",
    "2ndFlrSF2",
    "Neighborhood_E2",
    "RoofMatl_E2",
    "GrLivArea2",
]

# 下面這些特征做二值化
train["HasBasement"] = train["TotalBsmtSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasGarage"] = train["GarageArea"].apply(lambda x: 1 if x > 0 else 0)
train["Has2ndFloor"] = train["2ndFlrSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasMasVnr"] = train["MasVnrArea"].apply(lambda x: 1 if x > 0 else 0)
train["HasWoodDeck"] = train["WoodDeckSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasPorch"] = train["OpenPorchSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasPool"] = train["PoolArea"].apply(lambda x: 1 if x > 0 else 0)
train["IsNew"] = train["YearBuilt"].apply(lambda x: 1 if x > 2000 else 0)

boolean = [
    "HasBasement",
    "HasGarage",
    "Has2ndFloor",
    "HasMasVnr",
    "HasWoodDeck",
    "HasPorch",
    "HasPool",
    "IsNew",
]

features = quantitative + qual_encoded + boolean + qdr
lasso = linear_model.LassoLarsCV(max_iter=10000)

""" NG
# sklearn中要求X，y都是矩陣形式，而不是數據框
X = train[features].fillna(0.).values
Y = train['SalePrice'].values

lasso.fit(X, np.log(Y))  # 學習訓練.fit

#反log1p變換
Ypred = np.exp(lasso.predict(X))  # 預測.predict
print(error(Y, Ypred))

"""
# 一個很大的範例 SP

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# plt.rcParams['figure.figsize'] = 12, 8

np.random.seed(10)  # Setting seed for reproducability


# 以下OK 可搬出

""" NG
print("混同行列")

cm = confusion_matrix(y, y_pred)
print(cm)

print("------------------------------")  # 30個

print("正解率")
accuracy_score(y, y_pred)

print("------------------------------")  # 30個

print("適合率")
precision_score(y, y_pred)

print("------------------------------")  # 30個

print("再現率")
recall_score(y, y_pred)

print("------------------------------")  # 30個

print("F値")
f1_score(y, y_pred)

print("------------------------------")  # 30個

print("予測確率")
logistic_regression.predict_proba(X)

print("------------------------------")  # 30個

y_pred2 = (logistic_regression.predict_proba(X)[:, 1] > 0.1).astype(np.int)
print(confusion_matrix(y, y_pred2))

print(accuracy_score(y, y_pred2))
print(recall_score(y, y_pred2))

print("------------------------------")  # 30個

print("ROC曲線・AUC")
probas = logistic_regression.predict_proba(X)
fpr, tpr, thresholds = roc_curve(y, probas[:, 1])

print("------------------------------")  # 30個

plt.style.use("fivethirtyeight")

fig, ax = plt.subplots()
fig.set_size_inches(4.8, 5)

ax.step(fpr, tpr, "gray")
ax.fill_between(fpr, tpr, 0, color="skyblue", alpha=0.8)
ax.set_xlabel("False Positive Rate")
ax.set_ylabel("True Positive Rate")
ax.set_facecolor("xkcd:white")
show()

print("------------------------------")  # 30個

roc_auc_score(y, probas[:, 1])

print("------------------------------")  # 30個

print("平均二乗誤差")
mean_squared_error(y, y_pred)

print("------------------------------")  # 30個

print("決定係數")
print(r2_score(y, y_pred))

print("------------------------------")  # 30個

print("異なるアルゴリズムを利用した場合との比較")

from sklearn.svm import SVR

model_svr_linear = SVR(C=0.01, kernel="linear")

model_svr_linear.fit(X, y)  # 學習訓練.fit

y_svr_pred = model_svr_linear.predict(X)  # 預測.predict
print(y_svr_pred)

"""
fig, ax = plt.subplots()
ax.scatter(X, y, color="pink", marker="s", label="data set")
ax.plot(X, y_pred, color="blue", label="regression curve")
ax.plot(X, y_svr_pred, color="red", label="SVR")
ax.legend()
show()
"""

print(mean_squared_error(y, y_svr_pred))  # 平均二乗誤差
print(r2_score(y, y_svr_pred))  # 決定係數
print(model_svr_linear.coef_)  # 傾き
print(model_svr_linear.intercept_)  # 切片

print("------------------------------")  # 30個

print("ハイパーパラメータの設定")

model_svr_rbf = SVR(C=1.0, kernel="rbf")

model_svr_rbf.fit(X, y)  # 學習訓練.fit

y_svr_pred = model_svr_rbf.predict(X)  # 預測.predict
print(mean_squared_error(y, y_svr_pred))  # 平均二乗誤差
print(r2_score(y, y_svr_pred))  # 決定係數

train_X, test_X = X[:400], X[400:]
train_y, test_y = y[:400], y[400:]

model_svr_rbf_1 = SVR(C=1.0, kernel="rbf")

model_svr_rbf_1.fit(train_X, train_y)  # 學習訓練.fit

test_y_pred = model_svr_rbf_1.predict(test_X)  # 預測.predict
print(mean_squared_error(test_y, test_y_pred))  # 平均二乗誤差
print(r2_score(test_y, test_y_pred))  # 決定係數

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""

print("------------------------------------------------------------")  # 60個


print("------------------------------")  # 30個


# pd.options.display.max_rows = 1000
# pd.options.display.max_columns = 20


missing.plot.bar(figsize=(6, 4))

plt.figure(1)


# 繪圓點, 圓點用黑色外框
plt.scatter(data[:, 0], data[:, 1], marker="o", edgecolor="black")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
# 可搬出

"""
data/test3.csv
性別,尺寸,價格
male,XL,800
female,M,400
not specified,XXL,300
male,L,500
female,S,700
female,XS,850
"""

df = pd.read_csv("data/test3.csv")
print(df)

label_encoder = preprocessing.LabelEncoder()
df["性別"] = label_encoder.fit_transform(df["性別"])
print(df)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
