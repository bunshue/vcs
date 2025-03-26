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

import warnings

warnings.filterwarnings("once")

print("------------------------------------------------------------")  # 60個

from common1 import *

import tensorflow as tf
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
from sklearn.model_selection import cross_val_score

from imblearn.metrics import classification_report_imbalanced

# 載入迴歸常見的評估指標
from sklearn.metrics import mean_squared_error  # 均方誤差 Mean Squared Error (MSE)
from sklearn.metrics import mean_absolute_error  # 平均絕對誤差 Mean Absolute Error (MAE)
from sklearn.metrics import f1_score  # F値
from sklearn.metrics import r2_score  # R-Squared擬合度, 決定係數
from sklearn.metrics import accuracy_score  # 正解率
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import roc_curve  # ROC曲線, AUC
from sklearn.metrics import roc_auc_score
from sklearn.metrics import auc
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score  # 適合率
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import recall_score  # 再現率
from sklearn.metrics import balanced_accuracy_score

from sklearn.datasets import make_blobs  # 生成分類資料
from sklearn.datasets import make_moons  # 生成非線性資料 上/下弦月資料
from sklearn.datasets import make_circles
from sklearn.datasets import make_classification
from sklearn.datasets import make_hastie_10_2

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
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import PolynomialFeatures

# from sklearn.preprocessing import Imputer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.feature_selection import f_classif
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.model_selection import PredefinedSplit
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer

import scipy
import xgboost as xgb

from sklearn import svm
from sklearn import cluster
from sklearn import decomposition
from sklearn import model_selection
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier  # 分類模型
from sklearn.ensemble import GradientBoostingClassifier  # 分類模型
from sklearn.ensemble import RandomForestRegressor  # 迴歸模型
from sklearn.ensemble import GradientBoostingRegressor  # 迴歸模型

from sklearn.decomposition import PCA


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Sklearn verion is {}".format(sklearn.__version__))

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

sns.histplot(y,kde=False)
plt.xlabel('售價區間')
plt.ylabel('賣出件數')
plt.title('統計 售價區間 / 賣出件數')
show()

sns.histplot(y, kde=True, fit=st.johnsonsu)
plt.title('使用 Johnson SU')
show()

sns.histplot(y, kde=False, fit=st.norm)
plt.title('使用 Normal')
show()

sns.histplot(y, kde=False, fit=st.lognorm)
plt.title('使用 Log Normal')
show()

#另一種查看是否服從正態分布的可視化方法

sns.histplot(y, fit=st.norm)
plt.title('使用 Normal')
show()

res = st.probplot(y, plot=plt)
plt.title('SalePrice')
show()

print('------------------------------')	#30個

#把房價做對數變換後再看
SalePrice_log = np.log(y)
 
#transformed histogram and normal probability plot
sns.histplot(SalePrice_log, fit=st.norm);
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
cc = norm.pdf(x=1.8, loc=1.6, scale=0.2)
print(cc)

cc = norm_prob(h, mu, sigma)
print(cc)

cc = loglikelihood(data, mu, sigma)
print(cc)

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


cc = df["Gender"][0]
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""

"""
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

y_pred = model.predict([[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]])  # 預測.predict
print("預測結果 :\n", y_pred, sep="")

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
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2)
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
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2)
# 訓練組8成, 測試組2成

x_train = x_train.fillna(data_all[features].mean()) # 空值填充訓練集
x_val = x_val.fillna(data_all[features].mean()) # 空值填充驗證集
x_test = test.fillna(data_all[features].mean()) # 空值填充測試集
x = x.fillna(data_all[features].mean()) # 空值填充全集

print('------------------------------------------------------------')	#60個

# 訓練模型

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
# 存圖 plt.savefig('tmp.png',dpi=300)

print('------------------------------------------------------------')	#60個

# 檢測干擾變量

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

# ShuffleSplit 随机排列交叉验证器

from sklearn.model_selection import ShuffleSplit

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [3, 4], [5, 6]])
y = np.array([1, 2, 1, 2, 1, 2])
rs = ShuffleSplit(n_splits=5, test_size=0.25, random_state=0)
cc = rs.get_n_splits(X)
print(cc)

print(rs)
ShuffleSplit(n_splits=5, random_state=0, test_size=0.25, train_size=None)
for train_index, test_index in rs.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)

rs = ShuffleSplit(n_splits=5, train_size=0.5, test_size=0.25, random_state=0)
for train_index, test_index in rs.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit


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


def plot_learning_curve(
    estimator,
    X,
    y,
    ylim=None,
    cv=None,
    n_jobs=1,
    train_sizes=np.linspace(0.1, 1.0, 5),
):
    if ylim is not None:
        plt.ylim(*ylim)
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


# 測試資料
N = 200
X = np.linspace(0, 1, N)
y = np.sqrt(X) + 0.2 * np.random.rand(N) - 0.1
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

# 為了讓學習曲線更平滑，交叉驗證數據集的得分計算 10 次，每次都重新選中 20% 的數據計算一遍
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=9487)

plt.figure(figsize=(14, 5))

plt.subplot(131)
degree = 1
plot_learning_curve(polynomial_model(degree), X, y, ylim=(0.75, 1.01), cv=cv)
plt.xlabel("Training examples")
plt.ylabel("Score")
plt.title("Learning Curves (Under Fitting)")

plt.subplot(132)
degree = 3
plot_learning_curve(polynomial_model(degree), X, y, ylim=(0.75, 1.01), cv=cv)
plt.xlabel("Training examples")
plt.ylabel("Score")
plt.title("Learning Curves")

plt.subplot(133)
degree = 10
plot_learning_curve(polynomial_model(degree), X, y, ylim=(0.75, 1.01), cv=cv)
plt.xlabel("Training examples")
plt.ylabel("Score")
plt.title("Learning Curves (Over Fitting)")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 各種 模型評估 方法")

label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)

print(label_true)
print(label_pred)

print("測試 Adjusted Rand-Index : adjusted_rand_score")

cc = metrics.adjusted_rand_score(label_true, label_pred)
print("Adjusted Rand-Index : %0.3f" % cc)

label_true = [1, 1, 3, 3, 2, 2]
label_pred = [3, 3, 2, 2, 1, 1]

cc = metrics.adjusted_rand_score(label_true, label_pred)
print("Adjusted Rand-Index : %0.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]

print("測試 Homogeneity : homogeneity_score")

cc = metrics.homogeneity_score(label_true, label_pred)
print("Homogeneity score : %0.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [0, 1, 2, 3]

cc = metrics.homogeneity_score(label_true, label_pred)
print("Homogeneity score : %0.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]

cc = metrics.homogeneity_score(label_true, label_pred)
print("Homogeneity score : %0.3f" % cc)

label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)

cc = metrics.homogeneity_score(label_true, label_pred)
print("Homogeneity score : %0.3f" % cc)

print("測試 Completeness : completeness_score")

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
cc = metrics.completeness_score(label_true, label_pred)
print("Completeness score : %0.3f" % cc)

label_true = [0, 1, 2, 3]
label_pred = [1, 1, 2, 2]
cc = metrics.completeness_score(label_true, label_pred)
print("Completeness score : %0.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
cc = metrics.completeness_score(label_true, label_pred)
print("Completeness score : %0.3f" % cc)

label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)

cc = metrics.completeness_score(label_true, label_pred)
print("Completeness score : %0.3f" % cc)

print("測試 V-measure : v_measure_score")

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
cc = metrics.v_measure_score(label_true, label_pred)
print("V-measure score : %0.3f" % cc)

label_true = [0, 1, 2, 3]
label_pred = [1, 1, 2, 2]
cc = metrics.v_measure_score(label_true, label_pred)
print("V-measure score : %0.3f" % cc)

cc = metrics.v_measure_score(label_pred, label_true)
print("V-measure score : %0.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
cc = metrics.v_measure_score(label_true, label_pred)
print("V-measure score : %0.3f" % cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 數據預處理（Data Preprocessing）

print("Imputer Imputation 插補法")

from sklearn.impute import SimpleImputer

# SimpleImputer 對於np.nan 採用mean
imp_mean = SimpleImputer(missing_values=np.nan, strategy="mean")

imp_mean.fit([[7, 2, 3], [4, np.nan, 6], [10, 5, 9]])

X = [[np.nan, 2, 3], [4, np.nan, 6], [10, np.nan, 9]]
XT = imp_mean.transform(X)

print("原陣列 :\n", X, sep="")
print("轉換後 :\n", XT, sep="")

print("------------------------------")  # 30個

print("OneHotEncoder 獨熱編碼")

onehotencoder = OneHotEncoder(handle_unknown="ignore")
X = [["Male", 1], ["Female", 3], ["Female", 2]]

print("原陣列 :\n", X, sep="")

onehotencoder.fit(X)

cc = onehotencoder.categories_
print("a")
print(cc)

cc = onehotencoder.transform([["Female", 1], ["Male", 4]]).toarray()
print("b")
print(cc)

cc = onehotencoder.inverse_transform([[0, 1, 1, 0, 0], [0, 0, 0, 1, 0]])
print("c")
print(cc)

cc = onehotencoder.get_feature_names_out(["gender", "group"])
print("d")
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" Data.csv 10筆資料 4個欄位
Country,Age,Salary,Purchased
France,44,72000,No
Spain,27,48000,Yes
Germany,30,54000,No
Spain,38,61000,No
Germany,40,,Yes
France,35,58000,Yes
Spain,,52000,No
France,48,79000,Yes
Germany,50,83000,No
France,37,67000,Yes
"""

df = pd.read_csv("data/Data.csv")
# print(df) # 包含df之column與index
print("df之資料內容")
print(df.values)  # 不包含df之column與index 只有資料內容 10筆資料 4個欄位

# 不包括最後一欄的所有欄 前3欄
X = df.iloc[:, :-1].values

# 取出第4欄
Y = df.iloc[:, 3].values

print("X 前3欄 :\n", X, sep="")
print("Y 第4欄 :\n", Y, sep="")
print("X 第2 3欄 :\n", X[:, 1:3], sep="")

# 第三步：處理丟失數據

# 我們得到的數據很少是完整的。
# 數據可能因為各種原因丟失，為了不降低機器學習模型的性能，需要處理數據。
# 我們可以用整列的平均值或中間值替換丟失的數據。
# 我們用sklearn.preprocessing庫中的Imputer類完成這項任務。

# Step 3: Handling the missing data
# If you use the newest version of sklearn, use the lines of code commented out
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")

# axis=0表示按列進行
# imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
# print(imputer)
# print(X[ : , 1:3])

imputer = imputer.fit(X[:, 1:3])  # put the data we want to process in to this imputer
X[:, 1:3] = imputer.transform(X[:, 1:3])  # replace the np.nan with mean

# print(X[ : , 1:3])
print("------------------------------")  # 30個
print("Step 3: Handling the missing data")
print("step2")
print("X")
print(X)

""" another
第3步：處理丟失數據

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

print("------------------------------")  # 30個
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

print("------------------------------")  # 30個
print("Step 6: Feature Scaling")
print("X_train")
print(X_train)
print("X_test")
print(X_test)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/Social_Network_Ads.csv")

X = df.iloc[:, [2, 3]].values
y = df.iloc[:, 4].values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# Feature Scaling 特征縮放
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # STD特徵縮放
X_test = scaler.transform(X_test)  # STD特徵縮放

classifier = RandomForestClassifier(
    n_estimators=10, criterion="entropy", random_state=0
)

classifier.fit(X_train, y_train)  # 學習訓練.fit

y_pred = classifier.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred, sep="")

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
print("原df :\n", df, sep="")

print("使用 LabelEncoder")

labelencoder = LabelEncoder()

print("LabelEncoder size 字串 轉換 成 數字")
print('轉換前 df["size"] :\n', df["size"], sep="")

cc = labelencoder.fit_transform(df["size"])
print('轉換後 df["size"] :\n', cc, sep="")

cc = labelencoder.inverse_transform([1, 0, 2])
print("逆轉換 :\n", cc, sep="")

print("------------------------------")  # 30個
print("使用 Pandas Map, 對映")

size_mapping = {"XL": 3, "L": 2, "M": 1}

df["size"] = df["size"].map(size_mapping)
print("轉換後df :\n", df, sep="")

print("------------------------------")  # 30個
print("使用 獨熱編碼 OrdinalEncoder")

data = [["Male", 1], ["Female", 3], ["Female", 2]]
ordinalencoder = OrdinalEncoder()
cc = ordinalencoder.fit_transform(data)
print(cc)

print("使用 Pandas 之 獨熱編碼 OrdinalEncoder")

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

print("使用 獨熱編碼 OrdinalEncoder")

# 測試資料
X = [["Male", 1], ["Female", 3], ["Female", 2]]

# 轉換
onehotencoder = OneHotEncoder(handle_unknown="ignore")
X_new = onehotencoder.fit_transform(X)
cc = X_new.toarray()
print(cc)

# 類別
cc = onehotencoder.categories_
print(cc)

# 還原
cc = onehotencoder.inverse_transform(X_new)
print(cc)

# 指定欄位名稱
cc = onehotencoder.get_feature_names_out(["gender", "group"])
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
onehotencoder = OneHotEncoder(handle_unknown="ignore")
color_new = onehotencoder.fit_transform(df[["color"]])

# 指定欄位名稱
column_names = onehotencoder.get_feature_names_out(onehotencoder.feature_names_in_)

# 轉換
df_new = pd.DataFrame(color_new.toarray(), columns=column_names)
print(df_new)

# 刪除原欄位 'color'
df.drop(["color"], axis=1, inplace=True)

# 合併表格
df2 = pd.concat([df, df_new], axis=1)
print(df2)

# 儲存模型 joblib.dump(onehotencoder, "tmp_color.joblib")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
# 06_06_knn_book_recommender

# 以KNN演算法實作書籍推薦

# 書籍資料
books = pd.read_csv(
    "D:/_git/vcs/_big_files/Scikit-learn_data/BX-Books.csv",
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
    "D:/_git/vcs/_big_files/Scikit-learn_data/BX-Users.csv",
    sep=";",
    on_bad_lines="skip",
    encoding="latin-1",
)
users.columns = ["userID", "Location", "Age"]


# 評價資料
ratings = pd.read_csv(
    "D:/_git/vcs/_big_files/Scikit-learn_data/BX-Book-Ratings.csv",
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
# 存圖 plt.savefig("tmp_system2.png", bbox_inches="tight")

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
pd.set_option("display.float_format", lambda x: "%0.3f" % x)
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
model_knn.fit(us_canada_user_rating_matrix)  # 學習訓練.fit

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

# 依據 12 個特徵計算 相關係數
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

# 08_06_performance_metrics

# 計算及繪製混淆矩陣

"""
creditcard.csv 284807筆資料, 31欄位
"Time","V1","V2","V3","V4","V5","V6","V7","V8","V9","V10","V11","V12","V13","V14","V15","V16","V17","V18","V19","V20","V21","V22","V23","V24","V25","V26","V27","V28","Amount","Class"
0,-1.3598071336738,-0.0727811733098497,2.53634673796914,1.37815522427443,-0.338320769942518,0.462387777762292,0.239598554061257,0.0986979012610507,0.363786969611213,0.0907941719789316,-0.551599533260813,-0.617800855762348,-0.991389847235408,-0.311169353699879,1.46817697209427,-0.470400525259478,0.207971241929242,0.0257905801985591,0.403992960255733,0.251412098239705,-0.018306777944153,0.277837575558899,-0.110473910188767,0.0669280749146731,0.128539358273528,-0.189114843888824,0.133558376740387,-0.0210530534538215,149.62,"0"
0,1.19185711131486,0.26615071205963,0.16648011335321,0.448154078460911,0.0600176492822243,-0.0823608088155687,-0.0788029833323113,0.0851016549148104,-0.255425128109186,-0.166974414004614,1.61272666105479,1.06523531137287,0.48909501589608,-0.143772296441519,0.635558093258208,0.463917041022171,-0.114804663102346,-0.183361270123994,-0.145783041325259,-0.0690831352230203,-0.225775248033138,-0.638671952771851,0.101288021253234,-0.339846475529127,0.167170404418143,0.125894532368176,-0.00898309914322813,0.0147241691924927,2.69,"0"
1,-1.35835406159823,-1.34016307473609,1.77320934263119,0.379779593034328,-0.503198133318193,1.80049938079263,0.791460956450422,0.247675786588991,-1.51465432260583,0.207642865216696,0.624501459424895,0.066083685268831,0.717292731410831,-0.165945922763554,2.34586494901581,-2.89008319444231,1.10996937869599,-0.121359313195888,-2.26185709530414,0.524979725224404,0.247998153469754,0.771679401917229,0.909412262347719,-0.689280956490685,-0.327641833735251,-0.139096571514147,-0.0553527940384261,-0.0597518405929204,378.66,"0"

"Time",
"V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10",
"V11","V12","V13","V14","V15","V16","V17","V18","V19","V20",
"V21","V22","V23","V24","V25","V26","V27","V28",
"Amount","Class"
"""

df = pd.read_csv("D:/_git/vcs/_big_files/Scikit-learn_data/creditcard.csv")
cc = df.head()
print(cc)

# 觀察目標變數的各類別筆數

cc = df.Class.value_counts()
print(cc)

sns.countplot(x="Class", data=df)
show()

# 模型訓練與預測

X = df.drop(["Time", "Amount", "Class"], axis=1)
y = df["Class"]

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 模型訓練
clf = LogisticRegression()

clf.fit(X_train, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred, sep="")

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

df = pd.read_csv("D:/_git/vcs/_big_files/Scikit-learn_data/creditcard.csv")
cc = df.head()
print(cc)

# 觀察目標變數的各類別筆數

cc = df.Class.value_counts()
print(cc)

sns.countplot(x="Class", data=df)
show()

X = df.drop(["Time", "Amount", "Class"], axis=1)
y = df["Class"]

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 模型訓練
clf = LogisticRegression()

clf.fit(X_train, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred, sep="")

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

y_pred = clf.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred, sep="")

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

X, y = make_moons(n_samples=200, noise=0.05)
plt.scatter(X[:, 0], X[:, 1])
show()

# 模型訓練，繪製結果

db = DBSCAN(eps=0.2, min_samples=5, metric="euclidean")

y_pred = db.fit_predict(X)
print("預測結果 :\n", y_pred, sep="")

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
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4)

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

X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0)

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
X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0)

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

# 資料分割, 使用特殊的資料分割函數
from surprise.model_selection import train_test_split

# 切分為訓練及測試資料，測試資料佔 20%
trainset, testset = train_test_split(data, test_size=0.2)

# 恢復原本的函數
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

# 模型訓練

# 使用 KNN 演算法
model = KNNBasic()

# 訓練
model.fit(trainset)  # 學習訓練.fit

# 模型評分

# 測試
predictions = model.test(testset)

# 計算 RMSE
accuracy.rmse(predictions)

# RMSE: 0.9874

# SVD

model = SVD()

model.fit(trainset)  # 學習訓練.fit

predictions = model.test(testset)

accuracy.rmse(predictions)

# RMSE: 0.9405

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

y_pred = [0, 1, 0, 0]
y_true = [0, 1, 0, 1]

accuracy_score(y_true, y_pred)

# The overall precision an recall
precision_score(y_true, y_pred)
recall_score(y_true, y_pred)

# Recalls on individual classes: SEN & SPC
recalls = recall_score(y_true, y_pred, average=None)
recalls[0]  # is the recall of class 0: specificity
recalls[1]  # is the recall of class 1: sensitivity

# Balanced accuracy
b_acc = recalls.mean()

# The overall precision an recall on each individual class
p, r, f, s = precision_recall_fscore_support(y_true, y_pred)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Area Under Curve (AUC) of Receiver operating characteristic (ROC)

score_pred = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
y_true = np.array([0, 0, 0, 0, 1, 1, 1, 1])
thres = 0.9
y_pred = (score_pred > thres).astype(int)

print("With a threshold of %.2f, the rule always predict 0. Predictions:" % thres)
print(y_pred)

accuracy_score(y_true, y_pred)

# The overall precision an recall on each individual class
r = recall_score(y_true, y_pred, average=None)
print(
    "Recalls on individual classes are:",
    r,
    "ie, 100% of specificity, 0% of sensitivity",
)

# However AUC=1 indicating a perfect separation of the two classes
auc = roc_auc_score(y_true, score_pred)
print("But the AUC of %.2f demonstrate a good classes separation." % auc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Python如何分解SVD(奇異值分解)

在这个示例中，我们首先创建了一个矩阵 ( A )，然後使用numpy.linalg.svd函数对其进行SVD分解。
函数返回三个矩阵：( U )、( Sigma ) 和 ( V^T )。
需要注意的是，numpy.linalg.svd返回的 ( Sigma ) 是一个向量，而不是一个对角矩阵。

#一、使用NumPy库的linalg.svd函数
#二、使用Scipy库的linalg.svd函数
"""

A = np.array([[1, 0, 0, 0, 2], [0, 0, 3, 0, 0], [0, 0, 0, 0, 0], [0, 4, 0, 0, 0]])
print("A矩陣 :")
print(A)
print(A.shape)

# 使用NumPy进行SVD分解
U, Sigma, VT = np.linalg.svd(A)

# 使用Scipy进行SVD分解
U, Sigma, VT = scipy.linalg.svd(A)

print("U矩阵 :")
print(U)
print(U.shape)

print("Sigma对角矩阵 :")
print(Sigma)
print(Sigma.shape)

print("VT矩阵 :")
print(VT)
print(VT.shape)

"""
#五、SVD分解的应用
5.1 数据降维
SVD在数据降维中有广泛的应用。
通过SVD分解，我们可以将高维数据映射到低维空间，从而减少计算复杂度和存储空间。
以下是一个使用SVD进行数据降维的示例：
"""
from sklearn.decomposition import TruncatedSVD

X = np.random.rand(100, 50)

# 使用TruncatedSVD进行数据降维
svd = TruncatedSVD(n_components=10)

X_reduced = svd.fit_transform(X)

print("原始数据形状：", X.shape)
print("降维後数据形状：", X_reduced.shape)

"""
5.2 图像压缩
SVD在图像压缩中也有重要应用。
通过SVD分解，我们可以将图像数据表示为低秩矩阵，从而减少存储空间和传输带宽。
以下是一个使用SVD进行图像压缩的示例：
"""

from skimage import io

# 读取图像
# filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'
filename = "data/circle.bmp"
image = io.imread(filename, as_gray=True)

# 使用NumPy进行SVD分解
U, Sigma, VT = np.linalg.svd(image)

# 选择前k个奇异值进行图像压缩
k = 50

compressed_image = np.dot(U[:, :k], np.dot(np.diag(Sigma[:k]), VT[:k, :]))

# 显示原图和压缩後的图像
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap="gray")

plt.subplot(1, 2, 2)
plt.title("Compressed Image")
plt.imshow(compressed_image, cmap="gray")

show()

# 在这个示例中，我们首先读取了一张灰度图像，
# 然後使用NumPy的numpy.linalg.svd函数对其进行SVD分解。
# 通过选择前 ( k ) 个奇异值，我们可以重构出压缩後的图像。

"""
1. 什么是SVD分解？
SVD分解是奇异值分解（Singular Value Decomposition）的缩写，
是一种矩阵分解的方法。它将一个矩阵分解为三个矩阵的乘积，
分别是左奇异矩阵、奇异值矩阵和右奇异矩阵。
2. 如何在Python中进行SVD分解？
在Python中，可以使用NumPy库来进行SVD分解。首先，需要导入NumPy库，
然後使用numpy.linalg.svd()函数进行分解。
例如，如果有一个矩阵A，可以使用以下代码进行SVD分解：
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
U, S, V = np.linalg.svd(A)

3. SVD分解有什么应用场景？
SVD分解在数据分析和机器学习中有广泛的应用。
它可以用于降维，帮助去除数据中的噪声和冗余信息，从而提取出数据的主要特征。
此外，SVD分解还可以用于图像压缩、推荐系统、文本挖掘等领域。
通过SVD分解，我们可以对复杂的数据进行简化和分析，从而得到更有用的信息。
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

bv = np.array([10, 20, 30, 40, 50])  # business volume(營業額)
tax = 0.2 * bv  # Tax
bp = 0.1 * bv + np.array([-0.1, 0.2, 0.1, -0.2, 0.1])  # business potential(商機)

X = np.column_stack([bv, tax])
beta_star = np.array([0.1, 0])  # true solution

# Since tax and bv are correlated, there is an infinite number of linear combinations
# leading to the same prediction.

# 10 times the bv then subtract it 9 times using the tax variable:
beta_medium = np.array([0.1 * 10, -0.1 * 9 * (1 / 0.2)])

# 100 times the bv then subtract it 99 times using the tax variable:
beta_large = np.array([0.1 * 100, -0.1 * 99 * (1 / 0.2)])

print("L2 norm of coefficients:")
print("small : %.2f" % (np.sum(beta_star**2)))
print("medium :%.2f" % (np.sum(beta_medium**2)))
print("large : %.2f." % (np.sum(beta_large**2)))

print("However all models provide the exact same predictions.")
assert np.all(np.dot(X, beta_star) == np.dot(X, beta_medium))
assert np.all(np.dot(X, beta_star) == np.dot(X, beta_large))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# linear_classification

# 線性判別分析, Linear discriminant analysis, LDA

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# Dataset 2 two multivariate normal
n_samples, n_features = 100, 2
mean0, mean1 = np.array([0, 0]), np.array([0, 2])
Cov = np.array([[1, 0.8], [0.8, 1]])

X0 = np.random.multivariate_normal(mean0, Cov, n_samples)
X1 = np.random.multivariate_normal(mean1, Cov, n_samples)
X = np.vstack([X0, X1])
y = np.array([0] * X0.shape[0] + [1] * X1.shape[0])


# LDA with scikit-learn
lda = LDA()

proj = lda.fit(X, y).transform(X)  # 學習訓練.fit

y_pred_lda = lda.predict(X)  # 預測.predict

errors = y_pred_lda != y
print("Nb errors=%i, error rate=%.2f" % (errors.sum(), errors.sum() / len(y_pred_lda)))

print("------------------------------")  # 30個


# Logistic regression
def logistic(x):
    return 1 / (1 + np.exp(-x))


x = np.linspace(-6, 6, 100)
plt.plot(x, logistic(x))
plt.grid(True)
plt.title("Logistic (sigmoid)")

logreg = sklearn.linear_model.LogisticRegression().fit(X, y)  # 學習訓練.fit

# This class implements regularized logistic regression.
# C is the Inverse of regularization strength.
# Large value => no regularization.

logreg.fit(X, y)  # 學習訓練.fit

y_pred_logreg = logreg.predict(X)  # 預測.predict

errors = y_pred_logreg != y
print(
    "Nb errors=%i, error rate=%.2f" % (errors.sum(), errors.sum() / len(y_pred_logreg))
)
print(logreg.coef_)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Dataset with some correlation
N = 100  # n_samples, 樣本數
M = 10  # n_features, 特徵數(資料的維度)
print("make_classification,", N, "個樣本, ", M, "個特徵")
X, y = datasets.make_classification(
    n_samples=N,
    n_features=M,
    n_informative=5,
    n_redundant=3,
    n_classes=2,
    shuffle=False,
)

lr = sklearn.linear_model.LogisticRegression().fit(X, y)  # 學習訓練.fit

l2 = sklearn.linear_model.LogisticRegression(penalty="l2", C=0.1).fit(
    X, y
)  # lambda = 1 / C!  # 學習訓練.fit

# use solver 'saga' to handle L1 penalty
l1 = sklearn.linear_model.LogisticRegression(penalty="l1", C=0.1, solver="saga").fit(
    X, y
)  # lambda = 1 / C!  # 學習訓練.fit

l1l2 = sklearn.linear_model.LogisticRegression(
    penalty="elasticnet", C=0.1, l1_ratio=0.5, solver="saga"
).fit(
    X, y
)  # lambda = 1 / C!  # 學習訓練.fit

df = pd.DataFrame(
    np.vstack((lr.coef_, l2.coef_, l1.coef_, l1l2.coef_)),
    index=["lr", "l2", "l1", "l1l2"],
)
print(df)

print("------------------------------")  # 30個

# Ridge Fisher's linear classification (L2-regularization)
# Ridge logistic regression (L2-regularization)

lrl2 = sklearn.linear_model.LogisticRegression(penalty="l2", C=0.1)
# This class implements regularized logistic regression. C is the Inverse of regularization strength.
# Large value => no regularization.

lrl2.fit(X, y)  # 學習訓練.fit

y_pred_l2 = lrl2.predict(X)  # 預測.predict

prob_pred_l2 = lrl2.predict_proba(X)

print("Probas of 5 first samples for class 0 and class 1:")
print(prob_pred_l2[:5, :])

print("Coef vector:")
print(lrl2.coef_)

# Retrieve proba from coef vector
probas = 1 / (1 + np.exp(-(np.dot(X, lrl2.coef_.T) + lrl2.intercept_))).ravel()
print("Diff", np.max(np.abs(prob_pred_l2[:, 1] - probas)))

errors = y_pred_l2 != y
print("Nb errors=%i, error rate=%.2f" % (errors.sum(), errors.sum() / len(y)))

print("------------------------------")  # 30個

# Lasso logistic regression (L1-regularization)

lrl1 = sklearn.linear_model.LogisticRegression(
    penalty="l1", C=0.1, solver="saga"
)  # lambda = 1 / C!

# This class implements regularized logistic regression. C is the Inverse of regularization strength.
# Large value => no regularization.

lrl1.fit(X, y)  # 學習訓練.fit

y_pred_lrl1 = lrl1.predict(X)  # 預測.predict

errors = y_pred_lrl1 != y
print("Nb errors=%i, error rate=%.2f" % (errors.sum(), errors.sum() / len(y_pred_lrl1)))

print("Coef vector:")
print(lrl1.coef_)

print("------------------------------")  # 30個

svmlin = svm.LinearSVC(C=0.1)

# Remark: by default LinearSVC uses squared_hinge as loss
svmlin.fit(X, y)  # 學習訓練.fit

y_pred_svmlin = svmlin.predict(X)  # 預測.predict

errors = y_pred_svmlin != y
print(
    "Nb errors=%i, error rate=%.2f" % (errors.sum(), errors.sum() / len(y_pred_svmlin))
)
print("Coef vector:")
print(svmlin.coef_)

print("------------------------------")  # 30個

svmlinl1 = svm.LinearSVC(penalty="l1", dual=False)
# Remark: by default LinearSVC uses squared_hinge as loss

svmlinl1.fit(X, y)  # 學習訓練.fit

y_pred_svmlinl1 = svmlinl1.predict(X)  # 預測.predict

errors = y_pred_svmlinl1 != y
print(
    "Nb errors=%i, error rate=%.2f"
    % (errors.sum(), errors.sum() / len(y_pred_svmlinl1))
)
print("Coef vector:")
print(svmlinl1.coef_)

print("------------------------------")  # 30個

# Use SGD solver
enetlog = sklearn.linear_model.SGDClassifier(
    loss="log_loss", penalty="elasticnet", alpha=0.1, l1_ratio=0.5
)

enetlog.fit(X, y)  # 學習訓練.fit

# Or saga solver:
# enetloglike = sklearn.linear_model.LogisticRegression(penalty='elasticnet',
#                                    C=.1, l1_ratio=0.5, solver='saga')

enethinge = sklearn.linear_model.SGDClassifier(
    loss="hinge", penalty="elasticnet", alpha=0.1, l1_ratio=0.5
)

enethinge.fit(X, y)  # 學習訓練.fit

print("Hinge loss and logistic loss provide almost the same predictions.")
print("Confusion matrix")
confusion_matrix(enetlog.predict(X), enethinge.predict(X))

print("Decision_function log x hinge losses:")
_ = plt.plot(enetlog.decision_function(X), enethinge.decision_function(X), "o")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 500  # n_samples, 樣本數
M = 5  # n_features, 特徵數(資料的維度)
print("make_classification,", N, "個樣本, ", M, "個特徵")
X, y = datasets.make_classification(
    n_samples=N,
    n_features=M,
    n_informative=2,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    shuffle=False,
)

print(*["#samples of class %i = %i;" % (lev, np.sum(y == lev)) for lev in np.unique(y)])

print("# No Reweighting balanced dataset")
lr_inter = sklearn.linear_model.LogisticRegression(C=1)

lr_inter.fit(X, y)  # 學習訓練.fit

p, r, f, s = precision_recall_fscore_support(y, lr_inter.predict(X))

print("SPC: %0.3f; SEN: %0.3f" % tuple(r))
print("# => The predictions are balanced in sensitivity and specificity\n")

# Create imbalanced dataset, by subsampling sample of class 0: keep only 10% of
# class 0's samples and all class 1's samples.
n0 = int(np.rint(np.sum(y == 0) / 20))
subsample_idx = np.concatenate((np.where(y == 0)[0][:n0], np.where(y == 1)[0]))
Ximb = X[subsample_idx, :]
yimb = y[subsample_idx]
print(
    *[
        "#samples of class %i = %i;" % (lev, np.sum(yimb == lev))
        for lev in np.unique(yimb)
    ]
)

print("# No Reweighting on imbalanced dataset")
lr_inter = sklearn.linear_model.LogisticRegression(C=1)

lr_inter.fit(Ximb, yimb)  # 學習訓練.fit

p, r, f, s = precision_recall_fscore_support(yimb, lr_inter.predict(Ximb))

print("SPC: %0.3f; SEN: %0.3f" % tuple(r))
print("# => Sensitivity >> specificity\n")

print("# Reweighting on imbalanced dataset")
lr_inter_reweight = sklearn.linear_model.LogisticRegression(
    C=1, class_weight="balanced"
)

lr_inter_reweight.fit(Ximb, yimb)  # 學習訓練.fit

p, r, f, s = precision_recall_fscore_support(yimb, lr_inter_reweight.predict(Ximb))
print("SPC: %0.3f; SEN: %0.3f" % tuple(r))
print("# => The predictions are balanced in sensitivity and specificity\n")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Scikit-learn processing pipelines

# Standardization of input features

n_samples, n_features, n_features_info = 100, 5, 3
X = np.random.randn(n_samples, n_features)
beta = np.zeros(n_features)
beta[:n_features_info] = 1
Xbeta = np.dot(X, beta)
eps = np.random.randn(n_samples)
y = Xbeta + eps

X[:, 0] *= 1e6  # inflate the first feature
X[:, 1] += 1e6  # bias the second feature
y = 100 * y + 1000  # bias and scale the output

print("== Linear regression: scaling is not required ==")
model = sklearn.linear_model.LinearRegression()

model.fit(X, y)  # 學習訓練.fit

print("Coefficients:", model.coef_, model.intercept_)
print("Test R2:%.2f" % cross_val_score(estimator=model, X=X, y=y, cv=5).mean())

print("== Lasso without scaling ==")
model = sklearn.linear_model.LassoCV(cv=3)

model.fit(X, y)  # 學習訓練.fit

print("Coefficients:", model.coef_, model.intercept_)
print("Test R2:%.2f" % cross_val_score(estimator=model, X=X, y=y, cv=5).mean())

print("== Lasso with scaling ==")
model = sklearn.linear_model.LassoCV(cv=3)
scaler = preprocessing.StandardScaler()

Xc = scaler.fit(X).transform(X)

model.fit(Xc, y)  # 學習訓練.fit

print("Coefficients:", model.coef_, model.intercept_)
print("Test R2:%.2f" % cross_val_score(estimator=model, X=Xc, y=y, cv=5).mean())

# Scikit-learn pipelines

# Standardization of input features

model = make_pipeline(
    preprocessing.StandardScaler(), sklearn.linear_model.LassoCV(cv=3)
)

model = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        ("lassocv", sklearn.linear_model.LassoCV(cv=3)),
    ]
)

scores = cross_val_score(estimator=model, X=X, y=y, cv=5)
print("Test  r2:%.2f" % scores.mean())

# Features selection

n_samples, n_features, n_features_info = 100, 100, 3
X = np.random.randn(n_samples, n_features)
beta = np.zeros(n_features)
beta[:n_features_info] = 1
Xbeta = np.dot(X, beta)
eps = np.random.randn(n_samples)
y = Xbeta + eps

X[:, 0] *= 1e6  # inflate the first feature
X[:, 1] += 1e6  # bias the second feature
y = 100 * y + 1000  # bias and scale the output

model = Pipeline(
    [
        ("anova", SelectKBest(f_regression, k=3)),
        ("lm", sklearn.linear_model.LinearRegression()),
    ]
)
scores = cross_val_score(estimator=model, X=X, y=y, cv=5)
print("Anova filter + linear regression, test  r2:%.2f" % scores.mean())

model = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        ("lassocv", sklearn.linear_model.LassoCV(cv=3)),
    ]
)
scores = cross_val_score(estimator=model, X=X, y=y, cv=5)
print("Standardize + Lasso, test  r2:%.2f" % scores.mean())

# Regression pipelines with CV for parameters selection

# Datasets
N = 100  # n_samples, 樣本數
M = 100  # n_features, 特徵數(資料的維度)
T = 1  # n_targets, 標籤類別
NOISE = 20  # noise, 分散程度

print("make_regression,", N, "個樣本, ", M, "個特徵")

X, y, coef = datasets.make_regression(
    n_samples=N,
    n_features=M,
    noise=NOISE,
    n_informative=5,
    random_state=9487,
    coef=True,
)

# Use this to tune the noise parameter such that snr < 5
print("SNR:", np.std(np.dot(X, coef)) / NOISE)

print("=============================")
print("== Basic linear regression ==")
print("=============================")

scores = cross_val_score(
    estimator=sklearn.linear_model.LinearRegression(), X=X, y=y, cv=5
)
print("Test  r2:%.2f" % scores.mean())

print("==============================================")
print("== Scaler + anova filter + ridge regression ==")
print("==============================================")

anova_ridge = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        ("selectkbest", SelectKBest(f_regression)),
        ("ridge", sklearn.linear_model.Ridge()),
    ]
)
param_grid = {
    "selectkbest__k": np.arange(10, 110, 10),
    "ridge__alpha": [0.001, 0.01, 0.1, 1, 10, 100],
}

# Expect execution in ipython, for python remove the %time
print("----------------------------")
print("-- Parallelize inner loop --")
print("----------------------------")

anova_ridge_cv = GridSearchCV(anova_ridge, cv=5, param_grid=param_grid, n_jobs=-1)
cores = cross_val_score(estimator=anova_ridge_cv, X=X, y=y, cv=5)
print("Test r2:%.2f" % scores.mean())

print("----------------------------")
print("-- Parallelize outer loop --")
print("----------------------------")

anova_ridge_cv = GridSearchCV(anova_ridge, cv=5, param_grid=param_grid)
scores = cross_val_score(estimator=anova_ridge_cv, X=X, y=y, cv=5, n_jobs=-1)
print("Test r2:%.2f" % scores.mean())


print("=====================================")
print("== Scaler + Elastic-net regression ==")
print("=====================================")

alphas = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
l1_ratio = [0.1, 0.5, 0.9]

print("----------------------------")
print("-- Parallelize outer loop --")
print("----------------------------")

enet = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        ("enet", sklearn.linear_model.ElasticNet(max_iter=10000)),
    ]
)
param_grid = {"enet__alpha": alphas, "enet__l1_ratio": l1_ratio}
enet_cv = GridSearchCV(enet, cv=5, param_grid=param_grid)
scores = cross_val_score(estimator=enet_cv, X=X, y=y, cv=5, n_jobs=-1)
print("Test r2:%.2f" % scores.mean())

print("-----------------------------------------------")
print("-- Parallelize outer loop + built-in CV      --")
print("-- Remark: scaler is only done on outer loop --")
print("-----------------------------------------------")

enet_cv = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        (
            "enet",
            sklearn.linear_model.ElasticNetCV(
                max_iter=10000, l1_ratio=l1_ratio, alphas=alphas, cv=3
            ),
        ),
    ]
)

scores = cross_val_score(estimator=enet_cv, X=X, y=y, cv=5)
print("Test r2:%.2f" % scores.mean())


# Classification pipelines with CV for parameters selection

# Datasets
N = 100  # n_samples, 樣本數
M = 100  # n_features, 特徵數(資料的維度)
print("make_classification,", N, "個樣本, ", M, "個特徵")
X, y = datasets.make_classification(
    n_samples=N, n_features=M, n_informative=5, random_state=9487
)


def balanced_acc(estimator, X, y, **kwargs):
    # Balanced acuracy scorer
    return recall_score(y, estimator.predict(X), average=None).mean()


print("=============================")
print("== Basic logistic regression ==")
print("=============================")

scores = cross_val_score(
    estimator=sklearn.linear_model.LogisticRegression(
        C=1e8, class_weight="balanced", solver="lbfgs"
    ),
    X=X,
    y=y,
    cv=5,
    scoring=balanced_acc,
)
print("Test  bACC:%.2f" % scores.mean())

print("=======================================================")
print("== Scaler + anova filter + ridge logistic regression ==")
print("=======================================================")

anova_ridge = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        ("selectkbest", SelectKBest(f_classif)),
        (
            "ridge",
            sklearn.linear_model.LogisticRegression(
                penalty="l2", class_weight="balanced", solver="lbfgs"
            ),
        ),
    ]
)
param_grid = {
    "selectkbest__k": np.arange(10, 110, 10),
    "ridge__C": [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000],
}


# Expect execution in ipython, for python remove the %time
print("----------------------------")
print("-- Parallelize inner loop --")
print("----------------------------")

anova_ridge_cv = GridSearchCV(
    anova_ridge, cv=5, param_grid=param_grid, scoring=balanced_acc, n_jobs=-1
)
scores = cross_val_score(estimator=anova_ridge_cv, X=X, y=y, cv=5, scoring=balanced_acc)
print("Test bACC:%.2f" % scores.mean())

print("----------------------------")
print("-- Parallelize outer loop --")
print("----------------------------")

anova_ridge_cv = GridSearchCV(
    anova_ridge, cv=5, param_grid=param_grid, scoring=balanced_acc
)
scores = cross_val_score(
    estimator=anova_ridge_cv, X=X, y=y, cv=5, scoring=balanced_acc, n_jobs=-1
)
print("Test bACC:%.2f" % scores.mean())

print("========================================")
print("== Scaler + lasso logistic regression ==")
print("========================================")

Cs = np.array([0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000])
alphas = 1 / Cs
l1_ratio = [0.1, 0.5, 0.9]

print("----------------------------")
print("-- Parallelize outer loop --")
print("----------------------------")

lasso = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        (
            "lasso",
            sklearn.linear_model.LogisticRegression(
                penalty="l1", class_weight="balanced"
            ),
        ),
    ]
)
param_grid = {"lasso__C": Cs}
enet_cv = GridSearchCV(lasso, cv=5, param_grid=param_grid, scoring=balanced_acc)
""" NG
scores = cross_val_score(estimator=enet_cv, X=X, y=y, cv=5,\
                               scoring=balanced_acc, n_jobs=-1)
print("Test bACC:%.2f" % scores.mean())
"""

print("-----------------------------------------------")
print("-- Parallelize outer loop + built-in CV      --")
print("-- Remark: scaler is only done on outer loop --")
print("-----------------------------------------------")

lasso_cv = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        (
            "lasso",
            sklearn.linear_model.LogisticRegressionCV(Cs=Cs, scoring=balanced_acc),
        ),
    ]
)

scores = cross_val_score(estimator=lasso_cv, X=X, y=y, cv=5)
print("Test bACC:%.2f" % scores.mean())

print("=============================================")
print("== Scaler + Elasticnet logistic regression ==")
print("=============================================")

print("----------------------------")
print("-- Parallelize outer loop --")
print("----------------------------")

enet = Pipeline(
    [
        ("standardscaler", preprocessing.StandardScaler()),
        (
            "enet",
            sklearn.linear_model.SGDClassifier(
                loss="log",
                penalty="elasticnet",
                alpha=0.0001,
                l1_ratio=0.15,
                class_weight="balanced",
            ),
        ),
    ]
)

param_grid = {"enet__alpha": alphas, "enet__l1_ratio": l1_ratio}

enet_cv = GridSearchCV(enet, cv=5, param_grid=param_grid, scoring=balanced_acc)
""" NG
scores = cross_val_score(estimator=enet_cv, X=X, y=y, cv=5, scoring=balanced_acc, n_jobs=-1)
print("Test bACC:%.2f" % scores.mean())
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# **Regression**

N = 50  # n_samples, 樣本數
M = 100  # n_features, 特徵數(資料的維度)
T = 1  # n_targets, 標籤類別
NOISE = 10  # noise, 分散程度

print("make_regression,", N, "個樣本, ", M, "個特徵")

X, y, coef = datasets.make_regression(
    n_samples=N,
    n_features=M,
    noise=NOISE,
    n_informative=2,
    random_state=9487,
    coef=True,
)

print("== Ridge (L2 penalty) ==")
model = sklearn.linear_model.RidgeCV(cv=3)
scores = cross_val_score(estimator=model, X=X, y=y, cv=5)
print("Test  r2:%.2f" % scores.mean())

print("== Lasso (L1 penalty) ==")
model = sklearn.linear_model.LassoCV(n_jobs=-1, cv=3)
scores = cross_val_score(estimator=model, X=X, y=y, cv=5)
print("Test  r2:%.2f" % scores.mean())

print("== ElasticNet (L1 penalty) ==")
model = sklearn.linear_model.ElasticNetCV(l1_ratio=[0.1, 0.5, 0.9], n_jobs=-1, cv=3)
scores = cross_val_score(estimator=model, X=X, y=y, cv=5)
print("Test  r2:%.2f" % scores.mean())

# Regression dataset where first 2 features are predictives
np.random.seed(0)
n_features = 5
n_features_info = 2
n_samples = 100
X = np.random.randn(100, 5)
beta = np.zeros(n_features)
beta[:n_features_info] = 1
Xbeta = np.dot(X, beta)
eps = np.random.randn(n_samples)
y = Xbeta + eps

# Random permutations

# Fit model on all data (!! risk of overfit)
model = sklearn.linear_model.RidgeCV()

model.fit(X, y)  # 學習訓練.fit

print("Coefficients on all data:")
print(model.coef_)

# Random permutation loop
nperm = 1000  # !! Should be at least 1000 (to assess a p-value at 1%)
scores_names = ["r2"]
scores_perm = np.zeros((nperm + 1, len(scores_names)))
coefs_perm = np.zeros((nperm + 1, X.shape[1]))

scores_perm[0, :] = r2_score(y, model.predict(X))
coefs_perm[0, :] = model.coef_

orig_all = np.arange(X.shape[0])
for perm_i in range(1, nperm + 1):
    model.fit(X, np.random.permutation(y))  # 學習訓練.fit
    y_pred = model.predict(X).ravel()  # 預測.predict
    scores_perm[perm_i, :] = r2_score(y, y_pred)
    coefs_perm[perm_i, :] = model.coef_

# One-tailed empirical p-value
pval_pred_perm = np.sum(scores_perm >= scores_perm[0]) / scores_perm.shape[0]
pval_coef_perm = np.sum(coefs_perm >= coefs_perm[0, :], axis=0) / coefs_perm.shape[0]

print("R2 p-value: %0.3f" % pval_pred_perm)
print("Coeficients p-values:", np.round(pval_coef_perm, 3))

# Compute p-values corrected for multiple comparisons using FWER max-T
# (Westfall and Young, 1993) procedure.

pval_coef_perm_tmax = (
    np.array(
        [
            np.sum(coefs_perm.max(axis=1) >= coefs_perm[0, j])
            for j in range(coefs_perm.shape[1])
        ]
    )
    / coefs_perm.shape[0]
)
print("P-values with FWER (Westfall and Young) correction")
print(pval_coef_perm_tmax)

# Plot distribution of third coefficient under null-hypothesis
# Coeffitients 0 and 1 are significantly different from 0.


def hist_pvalue(perms, ax, name):
    """Plot statistic distribution as histogram.

    Paramters
    ---------
    perms: 1d array, statistics under the null hypothesis.
           perms[0] is the true statistic .
    """
    # Re-weight to obtain distribution
    pval = np.sum(perms >= perms[0]) / perms.shape[0]
    weights = np.ones(perms.shape[0]) / perms.shape[0]
    ax.hist(
        [perms[perms >= perms[0]], perms],
        histtype="stepfilled",
        bins=100,
        label="p-val<%0.3f" % pval,
        weights=[weights[perms >= perms[0]], weights],
    )
    ax.axvline(x=perms[0], color="k", linewidth=2)  # , label="observed statistic")
    ax.set_ylabel(name)
    ax.legend()
    return ax


n_coef = coefs_perm.shape[1]
fig, axes = plt.subplots(n_coef, 1, figsize=(12, 9))
for i in range(n_coef):
    hist_pvalue(coefs_perm[:, i], axes[i], str(i))

_ = axes[-1].set_xlabel("Coefficient distribution under null hypothesis")


# Bootstrap loop
nboot = 100  # !! Should be at least 1000
scores_names = ["r2"]
scores_boot = np.zeros((nboot, len(scores_names)))
coefs_boot = np.zeros((nboot, X.shape[1]))

orig_all = np.arange(X.shape[0])
for boot_i in range(nboot):
    boot_tr = np.random.choice(orig_all, size=len(orig_all), replace=True)
    boot_te = np.setdiff1d(orig_all, boot_tr, assume_unique=False)
    Xtr, ytr = X[boot_tr, :], y[boot_tr]
    Xte, yte = X[boot_te, :], y[boot_te]
    model.fit(Xtr, ytr)  # 學習訓練.fit
    y_pred = model.predict(Xte).ravel()  # 預測.predict
    scores_boot[boot_i, :] = r2_score(yte, y_pred)
    coefs_boot[boot_i, :] = model.coef_

# Compute Mean, SE, CI
# Coeffitients 0 and 1 are significantly different from 0.

scores_boot = pd.DataFrame(scores_boot, columns=scores_names)
scores_stat = scores_boot.describe(percentiles=[0.975, 0.5, 0.025])

print(
    "r-squared: Mean=%.2f, SE=%.2f, CI=(%.2f %.2f)"
    % tuple(scores_stat.loc[["mean", "std", "2.5%", "97.5%"], "r2"])
)

coefs_boot = pd.DataFrame(coefs_boot)
coefs_stat = coefs_boot.describe(percentiles=[0.975, 0.5, 0.025])
print("Coefficients distribution")
print(coefs_stat)

# Plot coefficient distribution

df = pd.DataFrame(coefs_boot)
staked = pd.melt(df, var_name="Variable", value_name="Coef. distribution")
sns.set_theme(style="whitegrid")
ax = sns.violinplot(x="Variable", y="Coef. distribution", data=staked)
_ = ax.axhline(0, ls="--", lw=2, color="black")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("一個很大的範例 ST")
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

sns.histplot(y, kde=False)
plt.title("預設方法")
show()
""" 不能使用參數fit
sns.histplot(y, kde=True, fit=st.johnsonsu)
plt.title("使用 Johnson SU")
show()

sns.histplot(y, kde=False, fit=st.norm)
plt.title("使用 Normal")
show()

sns.histplot(y, kde=False, fit=st.lognorm)
plt.title("使用 Log Normal")
show()

# 另一種查看是否服從正態分布的可視化方法
sns.histplot(train["SalePrice"], fit=st.norm)
plt.title("使用 Normal")
show()
"""
res = st.probplot(train["SalePrice"], plot=plt)
show()

# 把房價做對數變換後再看
SalePrice_log = np.log(train["SalePrice"])

# transformed histogram and normal probability plot
# 不能使用參數fit
# sns.histplot(SalePrice_log, fit=st.norm)
# show()

res = st.probplot(SalePrice_log, plot=plt)
print(res)

show()

"""
((array([-3.30513952, -3.04793228, -2.90489705, ...,  2.90489705,
,          3.04793228,  3.30513952]),
,  array([ 10.46024211,  10.47194981,  10.54270639, ...,  13.34550693,
,          13.5211395 ,  13.53447303])),
, (0.39826223081618845, 12.024050901109383, 0.99537614756366088))

顯然，房價本身不服從正態分布，是不能直接用來做回歸建模的。但是經過對數轉換之後，就好了很多。
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
# 對saleprice做標準化後再看

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
Neighborhood對房價有影響。然後每個類別的不同子類之間看起來似乎也有差別。
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
因為我們最後得到了個p值，p>0.05說明樣本的分組之間沒有顯著性差異，
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

# 相關係數
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
看起來，YearBuild、1stFlrSF, 2ndFlrSF, Neighborhood_E
There are lots of nonlinearities this may be the cause
why some variables wont be selected by Lasso/Lars.
Some factors like YearBuilt, 1stFlrSF, 2ndFlrSF, Neighborhood_E
look like they would benefit from adding quadratic term to regression.
But on the other hand this will most probably provoke overfit.

觀察的結果提示我們，有些變量可以嘗試做些變換，比如平方變換。

4.高級內容

考慮數據本身是否分群，如果分群，就可以用分段回歸。

接下來，考慮是否可以分段進行回歸。

我們把房價200000作為分界點，之下的作為普通住宅，之上的作為豪宅，
然後看看在這樣分開後，那些數值型變量的均值有多大差異。
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


我們用tnse方法，把每個高維樣本映射到二維平面上的點。
然後我們對樣本做標準化處理，處理之後做PCA，提取前30個主成分。也就是把樣本的特征降維到30個特征。
對這30個特征的樣本聚類，聚成5類。
在把這5類用可視化的方法會出來，看看是否有聚集趨勢。
"""

from sklearn.manifold import TSNE

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
    gamma, eta, epsilon, lbda = stats.johnsonsu.fit(y)  # 學習訓練.fit
    yt = gamma + eta * np.arcsinh((y - epsilon) / lbda)
    return yt, gamma, eta, epsilon, lbda


def johnson_inverse(y, gamma, eta, epsilon, lbda):
    return lbda * np.sinh((y - gamma) / eta) + epsilon


yt, g, et, ep, l = johnson(y)
yt2 = johnson_inverse(yt, g, et, ep, l)

sns.histplot(yt)
show()

sns.histplot(yt2)
show()

# 5.最後建模


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
print("一個很大的範例 SP")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
""" tfnn引用錯誤
import tfnn

bank_data = pd.read_csv("data/bank-full.csv", sep=";")

data = tfnn.Data(bank_data.iloc[:, :-1], bank_data.iloc[:, -1])
data.encode_cat_y(inplace=True)
data.encode_cat_x(inplace=True)
network = tfnn.ClfNetwork(
    data.xs.shape[1],
    data.ys.shape[1],
)
data = network.normalizer.minmax_fit(data, -1, 1)
train_data, test_data = data.train_test_split()
network.add_hidden_layer(50, activator=tfnn.nn.relu)
network.add_output_layer(activator=None)
network.set_optimizer(tfnn.train.GradientDescentOptimizer(0.0001))
evaluator = tfnn.Evaluator(network)

for i in range(1000):
    b_xs, b_ys = train_data.next_batch(100, loop=True)
    network.run_step(b_xs, b_ys)
    if i % 50 == 0:
        print(evaluator.compute_accuracy(test_data.xs, test_data.ys))
# print(test_data.ys.iloc[:,0].value_counts())
print(network.predict(test_data.xs.iloc[20:30, :]))  # 預測.predict
print(test_data.ys.iloc[20:30, :])
"""
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

# X -= X.mean(axis=0)  # Centering is required

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

# Encoding categorical features

# get_dummies 是 利用pandas實現one-hot-encoding(獨熱編碼)的方式
print(pd.get_dummies(["A", "B", "C", "A", "B", "D"]))

df = pd.DataFrame([["green", "A"], ["red", "B"], ["blue", "A"]])

df.columns = ["color", "class"]

print("get_dummies前 :")
print(df)

print("get_dummies後 :")
df2 = pd.get_dummies(df)
print(df2)

print("可以对指定列进行get_dummies")

df3 = pd.get_dummies(df.color)
print(df3)

print("将指定列进行get_dummies 後合并到元数据中")

df4 = df.join(pd.get_dummies(df.color))
print(df4)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# [平均]輪廓係數 silhouette_score
print(
    "Silhouette Coefficient: %0.3f"
    % metrics.silhouette_score(X, kmean.labels_, sample_size=1000)
)


print("預測結果 :\n", y_pred, sep="")
