"""



"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import time
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


"""
# load_boston 已被移除 但可以試一下 從 warning 訊息

from sklearn import ensemble
from sklearn import datasets
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

boston = datasets.load_boston() # 讀取Sklearn自帶的數據集
X_train,X_test,y_train,y_test = train_test_split(boston.data, boston.target,
                                                 test_size=0.2,random_state=13)
params = {'n_estimators': 200, 'max_depth': 5, 
          'min_samples_split': 5,'learning_rate': 0.01,
          'loss': 'ls', 'random_state': 0}
clf = ensemble.GradientBoostingRegressor(**params)
clf.fit(X_train, y_train) # 訓練模型
print("MSE: %.2f" % mean_squared_error(y_test, clf.predict(X_test)))

test_score = []
for i, y_pred in enumerate(clf.staged_predict(X_test)):
    test_score.append(clf.loss_(y_test, y_pred)) # 計算測試集誤差
plt.plot(clf.train_score_, 'y-') # 黃色(淺色)
plt.plot(test_score, 'b-') # 藍色(深色)

plt.show()
"""

print("------------------------------------------------------------")  # 60個

""" 安裝 auto-sklearn fail
print('Auto-Sklearn')

#pip install auto-sklearn
import autosklearn.classification
import statsmodels.api as sm
import warnings
warnings.filterwarnings('ignore')
  
data = sm.datasets.anes96.load_pandas().data
label = 'vote'
features = [i for i in data.columns if i != label]
X_train = data[features]
y_train = data[label]
automl = autosklearn.classification.AutoSklearnClassifier(
    time_left_for_this_task=120, per_run_time_limit=120, # 兩分鐘
    include_estimators=["random_forest"])
automl.fit(X_train, y_train)
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

""" 一些 fail
print('Auto-Keras')

from keras.datasets import mnist
from autokeras import ImageClassifier
from autokeras.constant import Constant
import autokeras
from keras.utils import plot_model
    
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(x_train.shape + (1,))
x_test = x_test.reshape(x_test.shape + (1,))
clf = ImageClassifier(verbose=True, augment=False)
clf.fit(x_train, y_train, time_limit=500 * 60)
clf.final_fit(x_train, y_train, x_test, y_test, retrain=True)
y = clf.evaluate(x_test, y_test)
print(y * 100)
clf.export_keras_model('model.h5')
plot_model(clf, to_file='model.png')
"""

print("------------------------------------------------------------")  # 60個


print("學習曲線和驗證曲線")

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


def draw_curve(params, train_score, test_score):
    train_mean = np.mean(train_score, axis=1)  # 均值
    train_std = np.std(train_score, axis=1)  # 標準差
    test_mean = np.mean(test_score, axis=1)
    test_std = np.std(test_score, axis=1)
    plt.plot(params, train_mean, "--", color="g", label="training")
    plt.fill_between(
        params, train_mean + train_std, train_mean - train_std, alpha=0.2, color="g"
    )  # 以半透明方式繪圖區域
    plt.plot(params, test_mean, "o-", color="b", label="testing")
    plt.fill_between(
        params, test_mean + test_std, test_mean - test_std, alpha=0.2, color="b"
    )
    plt.grid()  # 顯示網格
    plt.legend()  # 顯示圖例文字
    plt.ylim(0.5, 1.05)  # 設定y軸顯示範圍
    plt.show()


from sklearn.model_selection import learning_curve

breast_cancer = datasets.load_breast_cancer()
X = breast_cancer.data
y = breast_cancer.target

clf = RandomForestClassifier()
params = np.linspace(0.1, 1.0, 10)  # 從0.1到1，切分成10份
train_sizes, train_score, test_score = learning_curve(
    clf, X, y, train_sizes=params, cv=10, scoring="accuracy"
)  # 10折交叉驗證
draw_curve(params, train_score, test_score)


from sklearn.model_selection import validation_curve

params = [10, 20, 40, 80, 160, 240]
train_score, test_score = validation_curve(
    RandomForestClassifier(),
    X,
    y,
    param_name="n_estimators",
    cv=10,
    scoring="accuracy",
    param_range=params,
)
draw_curve(params, train_score, test_score)

print("------------------------------------------------------------")  # 60個

# 數據集和數據處理

from pandas import Series, DataFrame

# 繪圖分析
import seaborn as sns

sns.set_style("whitegrid")

# 機器學習
from sklearn.linear_model import LogisticRegression  # 邏輯迴歸
from sklearn.svm import SVC, LinearSVC  # 支持向量機
from sklearn.ensemble import RandomForestClassifier  # 隨機森林

# from sklearn.neighbors import KneighborsClassifier # K近鄰
from sklearn.naive_bayes import GaussianNB  # 數據集和數據處理


print("------------------------------------------------------------")  # 60個

titanic_df = pd.read_csv("data/train.csv")
test_df = pd.read_csv("data/test.csv")
print(titanic_df.head())
print(titanic_df.info())
print(titanic_df.describe())


print("------------------------------------------------------------")  # 60個


facet = sns.FacetGrid(titanic_df, hue="Survived", aspect=4)
facet.map(sns.kdeplot, "Age", shade=True)
facet.set(xlim=(0, titanic_df["Age"].max()))
facet.add_legend()
plt.show()

fig, axis1 = plt.subplots(1, 1, figsize=(18, 4))
average_age = titanic_df[["Age", "Survived"]].groupby(["Age"], as_index=False).mean()
sns.barplot(x="Age", y="Survived", data=average_age)
plt.show()


print("------------------------------------------------------------")  # 60個


def get_person(passenger):  # 小於16歲的分類爲兒童
    age, sex = passenger
    return "child" if age < 16 else sex


def conv(df):
    df["Person"] = df[["Age", "Sex"]].apply(get_person, axis=1)  # 組合特徵
    df["Fare"] = df["Fare"].fillna(df["Fare"].mean())  # 缺失值填充爲均值
    df["Embarked"] = df["Embarked"].fillna("S")  # 缺失值填充爲S
    df["Fare"] = df["Fare"].astype(int)  # 類型轉換

    person_dummies = pd.get_dummies(df["Person"])  # onehot編碼
    person_dummies.columns = ["Child", "Female", "Male"]
    df = df.join(person_dummies)  # 連接原數據與onehot數據
    df = df.drop(
        ["PassengerId", "Name", "Ticket", "Person", "Sex", "Embarked", "Cabin", "Age"],
        axis=1,
    )  # 刪除非數據型特徵
    return df


titanic_df = conv(titanic_df)
test_df = conv(test_df)

print("------------------------------------------------------------")  # 60個

# 生成模型所需的訓練集和測試集
X_train = titanic_df.drop("Survived", axis=1)
Y_train = titanic_df["Survived"]
X_test = test_df.copy()

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()  # 初始化模型
logreg.fit(X_train, Y_train)  # 訓練模型
print(logreg.score(X_train, Y_train))  # 模型評分
Y_pred = logreg.predict(X_test)  # 預測

print("------------------------------------------------------------")  # 60個

"""
實際數據請從天池競賽平臺下載
https://tianchi.aliyun.com/competition/gameList/activeList
https://tianchi.aliyun.com/competition/activeList
"""

import datetime
from pandas.api.types import is_numeric_dtype  # 用於判斷特徵類型
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier  # 分類模型
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor  # 迴歸模型
from sklearn.model_selection import cross_val_score, train_test_split  # 切分數據集
from sklearn.metrics import mean_squared_error  # 評價函數

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
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.25, random_state=0)
x_train = x_train.fillna(x.mean()) # 空值填充訓練集
x_val = x_val.fillna(x.mean()) # 空值填充驗證集
x_test = test.fillna(x.mean()) # 空值填充測試集
x = x.fillna(x.mean()) # 空值填充全集


print('------------------------------------------------------------')	#60個

# 訓練模型生成提交數據

#clf = RandomForestRegressor(criterion='mse', random_state=0) # 隨機森林迴歸
#clf = GradientBoostingClassifier(criterion='mse',random_state=0) # GBDT分類
clf = GradientBoostingRegressor(criterion='mse', random_state=0) # GBDT迴歸

if True: # 用於本地測試
    clf.fit(x_train, y_train)
    mse = mean_squared_error(y_val, [round(i) for i in clf.predict(x_val)])
    print("MSE: %.4f" % mse)
else: # 用於遠程提交
    clf.fit(x, y) # 全量數據訓練
    df = pd.DataFrame()
    df['id'] = test.id
    df['happiness'] = clf.predict(x_test[features])
    df.to_csv('out/submit_{}.csv'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')),index=False)

print('------------------------------------------------------------')	#60個

import datetime
from pandas.api.types import is_numeric_dtype # 用於判斷特徵類型
from sklearn.model_selection import cross_val_score, train_test_split # 切分數據集
from sklearn.metrics import mean_squared_error # 評價函數

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
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.25, random_state=0)
x_train = x_train.fillna(data_all[features].mean()) # 空值填充訓練集
x_val = x_val.fillna(data_all[features].mean()) # 空值填充驗證集
x_test = test.fillna(data_all[features].mean()) # 空值填充測試集
x = x.fillna(data_all[features].mean()) # 空值填充全集

print('------------------------------------------------------------')	#60個

# 訓練模型

import xgboost as xgb
from sklearn.cross_validation import KFold

def my_eval(preds, train): # 自定義評價函數
    score = mean_squared_error(train.get_label(), preds)
    return 'myeval', score

my_params = {"booster":'gbtree','eta': 0.005, 'max_depth': 6, 'subsample': 0.7, 
              'colsample_bytree': 0.8, 'objective': 'reg:linear', 'eval_metric': 'rmse', 
              'silent': True, 'nthread': 4} # 模型參數

train_preds = np.zeros(len(data)) # 用於保存預測結果
test_preds = np.zeros(len(test))
kf = KFold(len(data), n_folds = 5, shuffle=True, random_state=0) # 5折交叉驗證
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
    clf = GradientBoostingRegressor(criterion='mse', random_state=0)
    clf.fit(x_train[features_new], y_train)
    mse = mean_squared_error(y_val, [round(i) for i in clf.predict(x_val[features_new])])
    if mse < baseline:
        print("remove", i, "MSE: %.4f" % mse)

"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
