"""
20190327-空氣盒子數據Scikit-Learn各種演算法比較(全高雄)

使用的演算法
Linear regression,
Neural network,
Lasso,
ElasticNet,
Decision forest,
Extra Trees,
Boosted,
decisiontree,
XGBoost

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
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.neural_network import MLPRegressor
from xgboost.sklearn import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

print("------------------------------------------------------------")  # 60個

pd.set_option("display.max_rows", 1000)  # 設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000)  # 設定最大能顯示1000columns
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
# 指定默認字形：解決plot不能顯示中文問題
mpl.rcParams["axes.unicode_minus"] = False

print("------------------------------------------------------------")  # 60個

df = pd.read_excel("data/KH-1982-2018.xlsx")
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

X = df.drop(["PM25"], axis=1)
y = df.drop(["CO"], axis=1) # ???

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print(X.shape)
print(y.shape)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# 載入線性迴歸，並訓練模型
linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)

lin_pred = linear_regression.predict(X_test)

linear_regression_score = linear_regression.score(X_test, y_test)
cc = linear_regression_score
print(cc)

# 0.9101721045818417

# The coefficients
print("Coefficients: \n", linear_regression.coef_)
# The mean squared error
print("Root mean squared error: %.2f" % math.sqrt(mean_squared_error(y_test, lin_pred)))
# The absolute squared error
print("Mean absolute error: %.2f" % mean_absolute_error(y_test, lin_pred))
# Explained variance score: 1 is perfect prediction
print("R-squared: %.2f" % r2_score(y_test, lin_pred))

plt.scatter(y_test, lin_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("Linear Regression Predicted vs Actual")

plt.show()

print("------------------------------------------------------------")  # 60個

print("使用 多層感知機(Multi-Layer Perceptron, MLP)")

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

# 0.8532397997401182

# Make predictions using the testing set
nnr_pred = mlp.predict(X_test)

# The mean squared error
print("Root mean squared error: %.2f" % math.sqrt(mean_squared_error(y_test, nnr_pred)))
# The absolute squared error
print("Mean absolute error: %.2f" % mean_absolute_error(y_test, nnr_pred))
# Explained variance score: 1 is perfect prediction
print("R-squared: %.2f" % r2_score(y_test, nnr_pred))

plt.scatter(y_test, nnr_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("Neural Network Regression Predicted vs Actual")

plt.show()

print("------------------------------")  # 30個

"""
最小絕對值收斂和選擇算子、套索算法
Lasso算法(least absolute shrinkage and selection operator）
"""
lasso = Lasso()

lasso.fit(X_train, y_train)

Lasso(
    alpha=1.0,
    copy_X=True,
    fit_intercept=True,
    max_iter=1000,
    #normalize=False,
    positive=False,
    precompute=False,
    random_state=None,
    selection="cyclic",
    tol=0.0001,
    warm_start=False,
)

# Score the model
lasso_score = lasso.score(X_test, y_test)
cc = lasso_score
print(cc)

# 0.8873130463758103

# Make predictions using the testing set
lasso_pred = lasso.predict(X_test)

print("Root mean squared error: %.2f" % math.sqrt(mean_squared_error(y_test, lasso_pred)))

# Root mean squared error: 4.19

plt.scatter(y_test, lasso_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("Lasso Predicted vs Actual")

plt.show()

print("------------------------------")  # 30個

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

# 0.888862421794889

elasticnet_pred = elasticnet.predict(X_test)

# The mean squared error
print(
    "Root mean squared error: %.2f" % math.sqrt(mean_squared_error(y_test, elasticnet_pred))
)

# Root mean squared error: 4.16

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

# 0.9023960871039343

# Make predictions using the testing set
regr_rf_pred = regr_rf.predict(X_test)

# The mean squared error
print("Root mean squared error: %.2f" % math.sqrt(mean_squared_error(y_test, regr_rf_pred)))
# The absolute squared error
print("Mean absolute error: %.2f" % mean_absolute_error(y_test, regr_rf_pred))
# Explained variance score: 1 is perfect prediction
print("R-squared: %.2f" % r2_score(y_test, regr_rf_pred))

features = X.columns
importances = regr_rf.feature_importances_
indices = np.argsort(importances)

plt.title("Feature Importances")
plt.barh(range(len(indices)), importances[indices], color="b", align="center")
plt.yticks(range(len(indices)), features[indices])
plt.xlabel("Relative Importance")

plt.show()

print("------------------------------")  # 30個

plt.scatter(y_test, regr_rf_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("Decision Forest Predicted vs Actual")

plt.show()

print("------------------------------")  # 30個

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

# 0.9167571974098775

extratree_pred = extra_tree.predict(X_test)

print(
    "Root mean squared error: %.2f" % math.sqrt(mean_squared_error(y_test, extratree_pred))
)

# Root mean squared error: 3.60

features = X.columns
importances = extra_tree.feature_importances_
indices = np.argsort(importances)

plt.title("Feature Importances")
plt.barh(range(len(indices)), importances[indices], color="b", align="center")
plt.yticks(range(len(indices)), features[indices])
plt.xlabel("Relative Importance")

plt.show()

print("------------------------------")  # 30個

plt.scatter(y_test, extratree_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("Extra Trees Predicted vs Actual")

plt.show()

print("------------------------------------------------------------")  # 60個

# Create Decision Tree Regressor object
tree_1 = DecisionTreeRegressor()
# NG tree_2 = AdaBoostRegressor(DecisionTreeRegressor(), n_estimators=200, learning_rate=0.1)

# Train the model using the training sets
tree_1.fit(X_train, y_train)
# NG tree_2.fit(X_train, y_train)

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

# 0.8654467934849918

"""NG 
# Score the boosted decision tree model
boosted_tree_score = tree_2.score(X_test, y_test)
cc = boosted_tree_score
print(cc)
# 0.892229896203619

# Make predictions using the testing set
"""
tree_1_pred = tree_1.predict(X_test)

"""
#tree_2_pred = tree_2.predict(X_test)

# The coefficients
print("Coefficients: \n", regr.coef_)
# The mean squared error
print("Root mean squared error: %.2f" % math.sqrt(mean_squared_error(y_test, tree_2_pred)))
# The absolute squared error
print("Mean absolute error: %.2f" % mean_absolute_error(y_test, tree_2_pred))
# Explained variance score: 1 is perfect prediction
print("R-squared: %.2f" % r2_score(y_test, tree_2_pred))
"""

"""
Coefficients: 
 [ -0.69840943  -9.00508323   0.24863781 -29.59666709  28.86570143
  30.59322777 -89.85269969 119.62046794 106.26429001   2.18980547
  -1.2112113   -0.13323809]
Root mean squared error: 4.09
Mean absolute error: 3.09
R-squared: 0.89
"""

""" NG
features = X.columns
importances = tree_2.feature_importances_
indices = np.argsort(importances)

plt.title("Feature Importances")
plt.barh(range(len(indices)), importances[indices], color="b", align="center")
plt.yticks(range(len(indices)), features[indices])
plt.xlabel("Relative Importance")

plt.show()
"""
print("------------------------------------------------------------")  # 60個

plt.scatter(y_test, tree_1_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("Decision Tree Predicted vs Actual")

plt.show()

print("------------------------------------------------------------")  # 60個

""" NG
plt.scatter(y_test, tree_2_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("Boosted Decision Tree Predicted vs Actual")

plt.show()
"""
print("------------------------------------------------------------")  # 60個

# kilo 不能用 xgboost
# Fitting XGB regressor
xboost = XGBRegressor(n_estimators=200)

xboost.fit(X_train, y_train)

xgb_score = xboost.score(X_test, y_test)
cc = xgb_score
print(cc)

# 0.8902505097601974

# Predict
xboost_pred = xboost.predict(X_test)

print("Root mean squared error: %.2f" % math.sqrt(mean_squared_error(y_test, xboost_pred)))

# Root mean squared error: 4.13

plt.scatter(y_test, xboost_pred)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.title("XGBoost Predicted vs Actual")

plt.show()

print("------------------------------------------------------------")  # 60個

print("Scores:")
print("Linear regression score: ", linear_regression_score)
print("Neural network regression score: ", neural_network_regression_score)
print("Lasso regression score: ", lasso_score)
print("ElasticNet regression score: ", elasticnet_score)
print("Decision forest score: ", decision_forest_score)
print("Extra Trees score: ", extratree_score)
#print("Boosted decision tree score: ", boosted_tree_score)
print("XGBoost score:", xgb_score)
print("\n")
print("RMSE:")
print("Linear regression RMSE: %.2f" % math.sqrt(mean_squared_error(y_test, lin_pred)))
print("Neural network RMSE: %.2f" % math.sqrt(mean_squared_error(y_test, nnr_pred)))
print("Lasso RMSE: %.2f" % math.sqrt(mean_squared_error(y_test, lasso_pred)))
print("ElasticNet RMSE: %.2f" % math.sqrt(mean_squared_error(y_test, elasticnet_pred)))
print("Decision forest RMSE: %.2f" % math.sqrt(mean_squared_error(y_test, regr_rf_pred)))
print("Extra Trees RMSE: %.2f" % math.sqrt(mean_squared_error(y_test, extratree_pred)))
# NG print("Boosted decision tree RMSE: %.2f" % math.sqrt(mean_squared_error(y_test, tree_2_pred)))
print("XGBoost RMSE: %.2f" % math.sqrt(mean_squared_error(y_test, xboost_pred)))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


#plt.style.use("ggplot")
#plt.rcParams["figure.figsize"] = [16, 9]



print("------------------------------")  # 30個
