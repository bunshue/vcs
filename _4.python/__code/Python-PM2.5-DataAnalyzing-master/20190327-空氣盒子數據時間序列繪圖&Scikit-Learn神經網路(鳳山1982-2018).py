"""
20190327-空氣盒子數據時間序列繪圖&Scikit-Learn神經網路(鳳山1982-2018)

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

pd.set_option("display.max_rows", 1000)  # 設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000)  # 設定最大能顯示1000columns

df = pd.read_excel("data/鳳山.xlsx")
cc = df.head()
print(cc)

cc = df.columns
print(cc)

df["SO2"] = pd.to_numeric(df.SO2, errors="coerce")
df["CO"] = pd.to_numeric(df.CO, errors="coerce")
# df["CO2"] = pd.to_numeric(df.CO2, errors='coerce')
df["O3"] = pd.to_numeric(df.O3, errors="coerce")
df["PM25"] = pd.to_numeric(df.PM25, errors="coerce")
df["Nox"] = pd.to_numeric(df.Nox, errors="coerce")
df["NO"] = pd.to_numeric(df.NO, errors="coerce")
df["NO2"] = pd.to_numeric(df.NO2, errors="coerce")
df["THC"] = pd.to_numeric(df.THC, errors="coerce")
df["NMHC"] = pd.to_numeric(df.NMHC, errors="coerce")
df["CH4"] = pd.to_numeric(df.CH4, errors="coerce")
df["WindSpeed"] = pd.to_numeric(df.WindSpeed, errors="coerce")
df["TEMP"] = pd.to_numeric(df.TEMP, errors="coerce")
df["Humidity"] = pd.to_numeric(df.Humidity, errors="coerce")

cc = df.dtypes
print(cc)

plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = [16, 9]

x = df["Time"]
y = df["PM25"]
plt.plot(x, y)
plt.xlabel("年")
plt.ylabel("PM2.5值")
plt.title("PM2.5趨勢變化")
plt.show()

df["Time"] = pd.to_datetime(df["Time"])
df = df.rename(columns={"Time": "Date"})

cc = df.head()
print(cc)


def time_series(start, end):
    time_series_df = df[["Date", "PM25"]][(df["Date"] >= start) & (df["Date"] <= end)]
    x = time_series_df.Date
    y = time_series_df.PM25
    plt.plot(x, y)
    plt.xlabel("Time")
    plt.ylabel("PM2.5值")
    plt.title("PM2.5時間序列圖")
    return plt.show()


time_series("2017", "2018")

time_series("2010", "2018")

time_series("2008", "2018")

time_series("1982", "2018")

cc = df[["Date", "PM25"]][
    (df["Date"] >= "1982-01-01 01") & (df["Date"] <= "2018-11-01 04")
]
print(cc)

time_series("1997-04-01", "2018-11-01")

y = df["PM25"]
X = df.drop(["PM25", "Date"], axis=1)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=12
)
cc = X_train.shape, y_train.shape
print(cc)

cc = X_test.shape, y_test.shape
print(cc)

cc = X.columns
print(cc)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Create linear regression object
regr = LinearRegression()

regr.fit(X_train, y_train)

"""
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
         normalize=False)
"""
lin_pred = regr.predict(X_test)

linear_regression_score = regr.score(X_test, y_test)
cc = linear_regression_score
print(cc)

from math import sqrt

# The coefficients
print("Coefficients: \n", regr.coef_)
# The mean squared error
print("Root mean squared error: %.2f" % sqrt(mean_squared_error(y_test, lin_pred)))
# The absolute squared error
print("Mean absolute error: %.2f" % mean_absolute_error(y_test, lin_pred))
# Explained variance score: 1 is perfect prediction
print("R-squared: %.2f" % r2_score(y_test, lin_pred))

plt.scatter(y_test, lin_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("Linear Regression Predicted vs Actual")
plt.show()

from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Create MLPRegressor object
mlp = MLPRegressor()

mlp.fit(X_train, y_train)

"""
MLPRegressor(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(100,), learning_rate='constant',
       learning_rate_init=0.001, max_iter=200, momentum=0.9,
       n_iter_no_change=10, nesterovs_momentum=True, power_t=0.5,
       random_state=None, shuffle=True, solver='adam', tol=0.0001,
       validation_fraction=0.1, verbose=False, warm_start=False)
"""

# Score the model
neural_network_regression_score = mlp.score(X_test, y_test)
cc = neural_network_regression_score
print(cc)

# 0.5867267387294788

# Make predictions using the testing set
nnr_pred = mlp.predict(X_test)

# The mean squared error
print("Root mean squared error: %.2f" % sqrt(mean_squared_error(y_test, nnr_pred)))
# The absolute squared error
print("Mean absolute error: %.2f" % mean_absolute_error(y_test, nnr_pred))
# Explained variance score: 1 is perfect prediction
print("R-squared: %.2f" % r2_score(y_test, nnr_pred))

plt.scatter(y_test, nnr_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("Neural Network Regression Predicted vs Actual")
plt.show()

from sklearn.linear_model import Lasso

lasso = Lasso()

lasso.fit(X_train, y_train)

"""
Lasso(alpha=1.0, copy_X=True, fit_intercept=True, max_iter=1000,
   normalize=False, positive=False, precompute=False, random_state=None,
   selection='cyclic', tol=0.0001, warm_start=False)
"""

# Score the model
lasso_score = lasso.score(X_test, y_test)
cc = lasso_score
print(cc)

# 0.4229049346202005

# Make predictions using the testing set
lasso_pred = lasso.predict(X_test)

print("Root mean squared error: %.2f" % sqrt(mean_squared_error(y_test, lasso_pred)))

# Root mean squared error: 20.29

plt.scatter(y_test, lasso_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("Lasso Predicted vs Actual")
plt.show()

from sklearn.linear_model import ElasticNet

elasticnet = ElasticNet()

elasticnet.fit(X_train, y_train)

"""
ElasticNet(alpha=1.0, copy_X=True, fit_intercept=True, l1_ratio=0.5,
      max_iter=1000, normalize=False, positive=False, precompute=False,
      random_state=None, selection='cyclic', tol=0.0001, warm_start=False)
"""
elasticnet_score = elasticnet.score(X_test, y_test)
cc = elasticnet_score
print(cc)

# 0.41505193418487824

elasticnet_pred = elasticnet.predict(X_test)

# The mean squared error
print(
    "Root mean squared error: %.2f" % sqrt(mean_squared_error(y_test, elasticnet_pred))
)

# Root mean squared error: 20.43

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Create Random Forrest Regressor object
regr_rf = RandomForestRegressor(n_estimators=200, random_state=1234)

# Train the model using the training sets
regr_rf.fit(X_train, y_train)

"""
RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=None,
           max_features='auto', max_leaf_nodes=None,
           min_impurity_decrease=0.0, min_impurity_split=None,
           min_samples_leaf=1, min_samples_split=2,
           min_weight_fraction_leaf=0.0, n_estimators=200, n_jobs=None,
           oob_score=False, random_state=1234, verbose=0, warm_start=False)
"""

# Score the model
decision_forest_score = regr_rf.score(X_test, y_test)
cc = decision_forest_score
print(cc)

# 0.6199900888201892

# Make predictions using the testing set
regr_rf_pred = regr_rf.predict(X_test)

# The mean squared error
print("Root mean squared error: %.2f" % sqrt(mean_squared_error(y_test, regr_rf_pred)))
# The absolute squared error
print("Mean absolute error: %.2f" % mean_absolute_error(y_test, regr_rf_pred))
# Explained variance score: 1 is perfect prediction
print("R-squared: %.2f" % r2_score(y_test, regr_rf_pred))

cc = X.columns
print(cc)

features = X.columns
importances = regr_rf.feature_importances_
indices = np.argsort(importances)

plt.title("Feature Importances")
plt.barh(range(len(indices)), importances[indices], color="b", align="center")
plt.yticks(range(len(indices)), features[indices])
plt.xlabel("Relative Importance")
plt.show()

plt.scatter(y_test, regr_rf_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("Decision Forest Predicted vs Actual")
plt.show()

from sklearn.ensemble import ExtraTreesRegressor

extra_tree = ExtraTreesRegressor(n_estimators=200, random_state=1234)

extra_tree.fit(X_train, y_train)

"""
ExtraTreesRegressor(bootstrap=False, criterion='mse', max_depth=None,
          max_features='auto', max_leaf_nodes=None,
          min_impurity_decrease=0.0, min_impurity_split=None,
          min_samples_leaf=1, min_samples_split=2,
          min_weight_fraction_leaf=0.0, n_estimators=200, n_jobs=None,
          oob_score=False, random_state=1234, verbose=0, warm_start=False)
"""
extratree_score = extra_tree.score(X_test, y_test)
cc = extratree_score
print(cc)

# 0.7330015723201879

extratree_pred = extra_tree.predict(X_test)

print(
    "Root mean squared error: %.2f" % sqrt(mean_squared_error(y_test, extratree_pred))
)

# Root mean squared error: 13.80

features = X.columns
importances = extra_tree.feature_importances_
indices = np.argsort(importances)

plt.title("Feature Importances")
plt.barh(range(len(indices)), importances[indices], color="b", align="center")
plt.yticks(range(len(indices)), features[indices])
plt.xlabel("Relative Importance")
plt.show()

plt.scatter(y_test, extratree_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("Extra Trees Predicted vs Actual")
plt.show()

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Create Decision Tree Regressor object
tree_1 = DecisionTreeRegressor()

tree_2 = AdaBoostRegressor(DecisionTreeRegressor(), n_estimators=200, learning_rate=0.1)

# Train the model using the training sets
tree_1.fit(X_train, y_train)
tree_2.fit(X_train, y_train)

"""
AdaBoostRegressor(base_estimator=DecisionTreeRegressor(criterion='mse', max_depth=None, max_features=None,
           max_leaf_nodes=None, min_impurity_decrease=0.0,
           min_impurity_split=None, min_samples_leaf=1,
           min_samples_split=2, min_weight_fraction_leaf=0.0,
           presort=False, random_state=None, splitter='best'),
         learning_rate=0.1, loss='linear', n_estimators=200,
         random_state=None)
"""
# Score the decision tree model
cc = tree_1.score(X_test, y_test)
print(cc)

# 0.35116986832499186

# Score the boosted decision tree model
boosted_tree_score = tree_2.score(X_test, y_test)
cc = boosted_tree_score
print(cc)

# 0.7046849194129743

# Make predictions using the testing set
tree_1_pred = tree_1.predict(X_test)
tree_2_pred = tree_2.predict(X_test)

# The coefficients
print("Coefficients: \n", regr.coef_)
# The mean squared error
print("Root mean squared error: %.2f" % sqrt(mean_squared_error(y_test, tree_2_pred)))
# The absolute squared error
print("Mean absolute error: %.2f" % mean_absolute_error(y_test, tree_2_pred))
# Explained variance score: 1 is perfect prediction
print("R-squared: %.2f" % r2_score(y_test, tree_2_pred))

features = X.columns
importances = tree_2.feature_importances_
indices = np.argsort(importances)

plt.title("Feature Importances")
plt.barh(range(len(indices)), importances[indices], color="b", align="center")
plt.yticks(range(len(indices)), features[indices])
plt.xlabel("Relative Importance")
plt.show()

plt.scatter(y_test, tree_1_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("Decision Tree Predicted vs Actual")
plt.show()

plt.scatter(y_test, tree_2_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("Boosted Decision Tree Predicted vs Actual")
plt.show()

from xgboost.sklearn import XGBRegressor

# Fitting XGB regressor
xboost = XGBRegressor(n_estimators=200)

xboost.fit(X_train, y_train)

"""
XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
       colsample_bytree=1, gamma=0, importance_type='gain',
       learning_rate=0.1, max_delta_step=0, max_depth=3,
       min_child_weight=1, missing=None, n_estimators=200, n_jobs=1,
       nthread=None, objective='reg:linear', random_state=0, reg_alpha=0,
       reg_lambda=1, scale_pos_weight=1, seed=None, silent=True,
       subsample=1)
"""

xgb_score = xboost.score(X_test, y_test)
cc = xgb_score
print(cc)

# Predict
xboost_pred = xboost.predict(X_test)

print("Root mean squared error: %.2f" % sqrt(mean_squared_error(y_test, xboost_pred)))

# Root mean squared error: 16.99

plt.scatter(y_test, xboost_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("XGBoost Predicted vs Actual")
plt.show()

print("Scores:")
print("Linear regression score: ", linear_regression_score)
print("Neural network regression score: ", neural_network_regression_score)
print("Lasso regression score: ", lasso_score)
print("ElasticNet regression score: ", elasticnet_score)
print("Decision forest score: ", decision_forest_score)
print("Extra Trees score: ", extratree_score)
print("Boosted decision tree score: ", boosted_tree_score)
print("XGBoost score:", xgb_score)
print("\n")
print("RMSE:")
print("Linear regression RMSE: %.2f" % sqrt(mean_squared_error(y_test, lin_pred)))
print("Neural network RMSE: %.2f" % sqrt(mean_squared_error(y_test, nnr_pred)))
print("Lasso RMSE: %.2f" % sqrt(mean_squared_error(y_test, lasso_pred)))
print("ElasticNet RMSE: %.2f" % sqrt(mean_squared_error(y_test, elasticnet_pred)))
print("Decision forest RMSE: %.2f" % sqrt(mean_squared_error(y_test, regr_rf_pred)))
print("Extra Trees RMSE: %.2f" % sqrt(mean_squared_error(y_test, extratree_pred)))
print(
    "Boosted decision tree RMSE: %.2f" % sqrt(mean_squared_error(y_test, tree_2_pred))
)
print("XGBoost RMSE: %.2f" % sqrt(mean_squared_error(y_test, xboost_pred)))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
