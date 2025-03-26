"""

xgboost


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

from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123
)

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
