"""

xgboost

XGBoost 梯度提升法函式庫

"""

print("------------------------------------------------------------")  # 60個

# 共同
import re
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

from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# 使用分類模型

from xgboost import XGBClassifier

X, y = datasets.load_breast_cancer(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = XGBClassifier()

model.fit(X_train, y_train)  # 學習訓練.fit

scores = cross_val_score(model, X_test, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: 0.9484848484848485, 標準差: 0.05626498372008225

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# XGBoost測試
#!pip install xgboost -U

"""
Requirement already satisfied: xgboost in c:\anaconda3\lib\site-packages (1.6.1)
Collecting xgboost
  Downloading xgboost-1.7.3-py3-none-win_amd64.whl (89.1 MB)
     ---------------------------------------- 89.1/89.1 MB 8.7 MB/s eta 0:00:00
Requirement already satisfied: numpy in c:\anaconda3\lib\site-packages (from xgboost) (1.23.5)
Requirement already satisfied: scipy in c:\anaconda3\lib\site-packages (from xgboost) (1.9.3)
Installing collected packages: xgboost
  Attempting uninstall: xgboost
    Found existing installation: xgboost 1.6.1
    Uninstalling xgboost-1.6.1:
      Successfully uninstalled xgboost-1.6.1
Successfully installed xgboost-1.7.3
"""

X, y = datasets.load_diabetes(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練
from xgboost import XGBRegressor

model = XGBRegressor()

model.fit(X_train, y_train)  # 學習訓練.fit

"""
XGBRegressor(base_score=None, booster=None, callbacks=None,
             colsample_bylevel=None, colsample_bynode=None,
             colsample_bytree=None, early_stopping_rounds=None,
             enable_categorical=False, eval_metric=None, feature_types=None,
             gamma=None, gpu_id=None, grow_policy=None, importance_type=None,
             interaction_constraints=None, learning_rate=None, max_bin=None,
             max_cat_threshold=None, max_cat_to_onehot=None,
             max_delta_step=None, max_depth=None, max_leaves=None,
             min_child_weight=None, missing=nan, monotone_constraints=None,
             n_estimators=100, n_jobs=None, num_parallel_tree=None,
             predictor=None, random_state=None, ...)
"""

# 模型評估

from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X_test, y_test, cv=10, scoring="neg_mean_squared_error")
print(scores)

# 平均分數與標準差

print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: -5473.1857409034155, 標準差: 3004.388074594913

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
20190408-空氣盒子數據Scikit-Learn XGBoost實作

"""
print("------------------------------------------------------------")  # 60個

df = pd.read_excel("data/KH-1982-2018b.xlsx")
cc = df.head(10)
print(cc)

# 資料長度
print(len(df))
print(len(df["PM25"]))

df.info()  # 這樣就已經把結果印出來

cc = df.describe()
print(cc)

print(df.keys())
print(df.shape)

import xgboost as xgb
from sklearn.metrics import mean_squared_error

X, y = df.iloc[:, :-1], df.iloc[:, -1]

data_dmatrix = xgb.DMatrix(data=X, label=y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

xg_reg = xgb.XGBRegressor(
    objective="reg:linear",
    colsample_bytree=0.3,
    learning_rate=0.1,
    max_depth=5,
    alpha=10,
    n_estimators=10,
)

xg_reg.fit(X_train, y_train)

preds = xg_reg.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, preds))
print("RMSE: %f" % (rmse))

# RMSE: 9.892907

params = {
    "objective": "reg:linear",
    "colsample_bytree": 0.3,
    "learning_rate": 0.1,
    "max_depth": 5,
    "alpha": 10,
}

cv_results = xgb.cv(
    dtrain=data_dmatrix,
    params=params,
    nfold=3,
    num_boost_round=50,
    early_stopping_rounds=10,
    metrics="rmse",
    as_pandas=True,
    seed=123,
)

cc = cv_results.head()
print(cc)

print((cv_results["test-rmse-mean"]).tail(1))

xg_reg = xgb.train(params=params, dtrain=data_dmatrix, num_boost_round=10)

xgb.plot_importance(xg_reg)
plt.rcParams["figure.figsize"] = [15, 6]
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''


# 提取特徵
def prepare(df):
    if len(df.columns) == 7:
        df = df.rename(
            columns={
                0: "uid",
                1: "mid",
                2: "datetime",
                3: "f",
                4: "c",
                5: "l",
                6: "content",
            }
        )
    else:
        df = df.rename(columns={0: "uid", 1: "mid", 2: "datetime", 3: "content"})
    df["datetime"] = pd.to_datetime(df["datetime"])
    df["weekday"] = df["datetime"].apply(lambda x: x.weekday())
    df["hour"] = df["datetime"].apply(lambda x: x.hour)
    return df


def check_ads(x):
    if x is np.nan:
        return 0
    if x.find("快的打車") != -1:
        return 1
    if x.find("紅包") != -1:
        return 1
    if x.find("領取") != -1:
        return 1
    if x.find("你也來試試手氣") != -1:
        return 1
    if x.find("超讚的文件") != -1:
        return 1
    if x.find("鏈接下載") != -1:
        return 1
    if x.find("開始報名") != -1:
        return 1
    return 0


def check_share(x):
    if x is np.nan:
        return 0
    if x.find("我分享了") != -1:
        return 1
    if x.find("分享自") != -1:
        return 1
    if x.find("我上傳了") != -1:
        return 1
    if x.find("我更新了") != -1:
        return 1
    if x.find("照片到專輯") != -1:
        return 1
    return 0


def check_IT(x):
    if x is np.nan:
        return 0
    if x.find("IT") != -1:
        return 1
    if x.find("CSDN") != -1:
        return 1
    return 0


# 手動提取關鍵字特徵
def add_features(data):
    data["content"] = data["content"].fillna("")
    data["c_has_link"] = data["content"].str.contains("http", na=False).astype(int)
    data["c_has_at"] = data["content"].str.contains("@", na=False).astype(int)
    data["c_has_ex"] = data["content"].str.contains("\[", na=False).astype(int)
    # new
    data["c_has_video"] = data["content"].str.contains("視頻", na=False).astype(int)
    data["c_has_ads"] = data["content"].apply(check_ads)
    data["c_has_share"] = data["content"].apply(check_share)
    data["c_has_it"] = data["content"].apply(check_IT)
    data["c_has_topic"] = data["content"].apply(
        lambda x: 0 if len(re.compile(r"[#【《](.*?)[#】》]", re.S).findall(x)) == 0 else 1
    )
    return data


# 本地評分
def do_score(real_data, predict_data):
    d_f = ((predict_data["f"] - real_data["f"]) / (real_data["f"] + 5.0)).apply(
        lambda x: abs(x)
    )
    d_c = ((predict_data["c"] - real_data["c"]) / (real_data["c"] + 3.0)).apply(
        lambda x: abs(x)
    )
    d_l = ((predict_data["l"] - real_data["l"]) / (real_data["l"] + 3.0)).apply(
        lambda x: abs(x)
    )
    count_i = real_data["f"] + real_data["l"] + real_data["c"]
    precision = 1 - 0.5 * d_f - 0.25 * d_c - 0.25 * d_l
    sign = np.sign(precision - 0.8).apply(lambda x: 0 if x == -1 else 1)
    count_i[count_i > 100] = 100
    count_1 = sum((count_i + 1) * sign)
    count_2 = sum(count_i + 1)
    return count_1 / count_2


"""
weibo_train_data2.txt 1999筆資料 7欄位
d38e9bed5d98110dc2489d0d1cac3c2a	7d45833d9865727a88b960b0603c19f6	2015-02-23 17:41:29	0	0	0	麗江旅遊(sz002033)#股票##炒股##財經##理財##投資#推薦包贏股，盈利對半分成，不算本金，羣：46251412
fa13974743d3fe6ff40d21b872325e9e	8169f1d45051e08ef213bf1106b1225d	2015-02-14 12:49:58	0	0	0	#丁辰靈的紅包#掙錢是一種能力，搶紅包拼的是技術。我搶到了丁辰靈 和@闞洪巖 一起發出的現金紅包，幸福感爆棚！情人節，一起來和粉絲紅包約個會吧╮ (￣ 3￣) ╭http://t.cn/RZDIVjf
da534fe87e7a52777bee5c30573ed5fd	68cd0258c31c2c525f94febea2d9523b	2015-03-31 13:58:06	0	0	0	淘寶網這些傻逼。。。氣的勞資有火沒地兒發~尼瑪，你們都瞎了
e06a22b7e065e559a1f0bf7841a85c51	00b9f86b4915aedb7db943c54fd19d59	2015-06-11 20:39:57	0	4	3	看點不能說的，你們都懂[笑cry]
f9828598f9664d4e347ef2048ce17734	c7f6f66044c0c5a3330e2c5371be6824	2015-03-10 18:02:38	0	0	0	111多張
d80f3d3c5c1d658e82b837a4dd1af849	bfc0819b83ec59ce767287077f2b3507	2015-02-13 01:09:41	0	0	0	有生之年！我最喜歡的up主跟我的三體勾搭到一起了！幸福感爆棚！ @黑桐谷歌  http://t.cn/RwGp4wk


"""

# 讀訓練數據
data = pd.read_csv("data/weibo_train_data2.txt", sep="\t", header=None)
data = prepare(data)
data = add_features(data)

# 切分訓練集和驗證集
train, val = train_test_split(data, test_size=0.2, random_state=0)
val = val.reset_index(drop=True)

# 按用戶分組
if True:
    grp = train.groupby("uid")
    user_data = pd.DataFrame()
    user_data["f"] = grp["f"].mean()
    user_data["c"] = grp["c"].mean()
    user_data["l"] = grp["l"].mean()
else:
    user_data = pd.read_csv("train_user.csv")
user_data_2 = user_data.rename(columns={"l": "avg_l", "c": "avg_c", "f": "avg_f"})
print(user_data.head())

print("------------------------------")  # 30個

# 模型訓練
import xgboost as xgb


def testme_f(preds, dtrain):
    labels = pd.Series(dtrain.get_label())
    tmp = pd.DataFrame()
    d = ((preds - labels) / (labels + 5.0)).apply(lambda x: abs(x))
    count_i = labels
    precision = 1 - d
    sign = np.sign(precision - 0.8).apply(lambda x: 0 if x == -1 else 1)
    count_i[count_i > 50] = 50
    count_1 = sum((count_i + 1) * sign)
    count_2 = sum(count_i + 1)
    return "testme", 1 - count_1 / count_2


def testme_lc(preds, dtrain):
    labels = pd.Series(dtrain.get_label())
    tmp = pd.DataFrame()
    d = ((preds - labels) / (labels + 3.0)).apply(lambda x: abs(x))
    count_i = labels
    precision = 1 - d
    sign = np.sign(precision - 0.8).apply(lambda x: 0 if x == -1 else 1)
    count_i[count_i > 25] = 25
    count_1 = sum((count_i + 1) * sign)
    count_2 = sum(count_i + 1)
    return "testme", 1 - count_1 / count_2


def calc(grp1, grp2, features, key, params, feval):
    train_X = grp1[features]
    train_Y = grp1[key]
    val_X = grp2[features]
    val_Y = grp2[key]
    dtrain = xgb.DMatrix(train_X, train_Y)
    dval = xgb.DMatrix(val_X, val_Y)
    watchlist = [(dtrain, "train"), (dval, "val")]
    model = xgb.train(
        params,
        dtrain,
        evals=watchlist,
        feval=feval,
        num_boost_round=200,
        early_stopping_rounds=10,
    )
    model.save_model("tmp_model_" + key)
    dic = model.get_fscore()
    dic2 = sorted(dic.items(), key=lambda d: d[1], reverse=True)
    print("feature importance", dic2)
    return model


params = {
    "max_depth": 7,
    "subsample": 0.7,
    "eta": 0.05,
    "seed": 5,
    "objective": "reg:linear",
}

print("------------------------------")  # 30個

print("開始使用 jieba")
# 提取關鍵詞
import jieba

print(data.shape)
tmp = data.sample(n=1000)  # df 隨機抽出1000筆

print(tmp.shape)

print(tmp.head())

arr = tmp["content"].unique()

print(type(arr))


print(len(arr))
arr_all = []
for i in arr:
    arr = jieba.cut(i, cut_all=True)
    arr_zh = [
        i
        for i in arr
        if len(re.findall(r"^[#\+a-z0-9A-Z\\-_]+$", i, re.M)) == 0 and len(i) > 1
    ]
    arr_all.extend(arr_zh)
print(len(arr_all))

result = pd.value_counts(arr_all)
arr_word = []
for key, value in result.items():
    if value > 5:
        arr_word.append(key)
print(arr_word)

print("------------------------------")  # 30個

# 從文字中提取特徵
from scipy import stats


def get_dic(arr_word, dst, count, data):
    print(len(arr_word))
    dic_key = {}
    for idx, i in enumerate(arr_word):
        df1 = data[data["content"].str.contains(i) == False]
        df2 = data[data["content"].str.contains(i) == True]
        ret2 = stats.levene(df1[dst], df2[dst])
        if ret2[1] < 0.05:
            dic_key[i] = [ret2[1], df2[dst].mean(), len(df2)]
            print(idx, i, dic_key[i], len(dic_key))
            if len(dic_key) > count:
                break
    return dic_key


dic_key_f = get_dic(arr_word, "f", 100, data[:100000])
dic_key_c = get_dic(arr_word, "c", 50, data[:100000])
dic_key_l = get_dic(arr_word, "l", 100, data[:100000])

print("------------------------------")  # 30個

val = pd.merge(val, user_data_2, on="uid", how="left")
train = pd.merge(train, user_data_2, on="uid", how="left")


# 生成新模型
def calc_dic(train, val, dst, dic):
    train_new = train.copy()
    for key in dic.keys():
        # print(key)
        train_new[key] = (
            train["content"].str.contains(key).apply(lambda x: 1 if x else 0)
        )
    val_new = val.copy()
    for key in dic.keys():
        val_new[key] = val["content"].str.contains(key).apply(lambda x: 1 if x else 0)
    features = [
        "weekday",
        "hour",
        "c_has_link",
        "c_has_at",
        "c_has_ex",
        "c_has_video",
        "c_has_ads",
        "c_has_share",
        "c_has_it",
        "avg_l",
        "avg_c",
        "avg_f",
        "c_has_topic",
    ]
    features_new = features + list(dic.keys())
    model = calc(train_new, val_new, features_new, dst, params, testme_f)
    return model


model_f = calc_dic(train, val, "f", dic_key_f)
model_c = calc_dic(train, val, "c", dic_key_c)
model_l = calc_dic(train, val, "l", dic_key_l)

# 保存模型
dic = {}
dic["model_f"] = model_f
dic["model_c"] = model_c
dic["model_l"] = model_l
dic["dic_key_f"] = dic_key_f
dic["dic_key_c"] = dic_key_c
dic["dic_key_l"] = dic_key_l
dic["user_data_2"] = user_data_2

""" import fail
from sklearn.externals import joblib
joblib.dump(dic, 'model.pkl')
"""

print("------------------------------")  # 30個


def do_pred(model, val, dic):
    val_new = val.copy()
    for key in dic.keys():
        val_new[key] = val["content"].str.contains(key).apply(lambda x: 1 if x else 0)
    features = [
        "weekday",
        "hour",
        "c_has_link",
        "c_has_at",
        "c_has_ex",
        "c_has_video",
        "c_has_ads",
        "c_has_share",
        "c_has_it",
        "avg_l",
        "avg_c",
        "avg_f",
        "c_has_topic",
    ]
    features_new = features + list(dic.keys())
    tmp = val_new[features_new]
    dtest = xgb.DMatrix(tmp)
    out = model.predict(dtest)
    out = pd.Series(out).apply(lambda x: int(x))
    return out


def do_pred_all(df):
    out = df.copy()
    out["f"] = do_pred(model_f, df, dic_key_f)
    out["l"] = do_pred(model_l, df, dic_key_l)
    out["c"] = do_pred(model_c, df, dic_key_c)
    return out


# 對驗證集預測
out = do_pred_all(val)
print(do_score(val, out))

# 預測並生成提交數據
test = pd.read_csv("data/weibo_predict_data.txt", sep="\t", header=None)
test = prepare(test)
test = add_features(test)
test = pd.merge(test, user_data_2, on="uid", how="left")
test = test.fillna(0)
out = do_pred_all(test)
out["ss"] = (
    out["f"].astype(str) + "," + out["c"].astype(str) + "," + out["l"].astype(str)
)
out = out[["uid", "mid", "ss"]]
print(out.shape)
print(out.head())
out.to_csv("tmp_result_190624.txt", index=False, header=None, sep="\t")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import xgboost as xgb

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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
