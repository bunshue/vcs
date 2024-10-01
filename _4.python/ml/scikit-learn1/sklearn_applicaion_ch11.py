"""
Scikit-learn 詳解與企業應用_機器學習最佳入門與實戰

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
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#11_06_shap_test

#SHAP套件測試
#An introduction to explainable AI with Shapley values

import numpy as np
import pandas as pd
import shap
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

#載入資料集

df = pd.read_csv('./data/ca_housing.csv')
cc = df.head()
print(cc)

#資料清理

# 刪除 missing value
df.dropna(inplace=True)

X = df.drop(['median_house_value', 'ocean_proximity'], axis=1)
y = df['median_house_value']

#模型訓練與評估

# scaler = StandardScaler()
# X2 = scaler.fit_transform(X)
# X = pd.DataFrame(X2, columns=X.columns)

model = LinearRegression()
model.fit(X, y)
print("Model coefficients:")
for i in range(X.shape[1]):
    print(X.columns[i], "=", model.coef_[i].round(5))

#單一特徵影響力

feature_name = "median_income"
X100 = shap.utils.sample(X, 100)
shap.partial_dependence_plot(
    feature_name, model.predict, X100, ice=False,
    model_expected_value=True, feature_expected_value=True
)

#衡量特徵Shapley value

sample_ind = 20  # 第 21 筆資料
explainer = shap.Explainer(model.predict, X100)
shap_values = explainer(X)
shap.partial_dependence_plot(
    feature_name, model.predict, X100, model_expected_value=True,
    feature_expected_value=True, ice=False,
    shap_values=shap_values[sample_ind:sample_ind+1,:]
)

#Exact explainer: 20434it [01:32, 205.74it/s]                                                                           

#以單一特徵所有資料的Shapley value繪製散佈圖

shap.plots.scatter(shap_values[:,feature_name])
plt.show()

#單一資料的特徵影響力(Local Feature Importance)

cc = X.iloc[sample_ind]
print(cc)

shap.plots.waterfall(shap_values[sample_ind], max_display=14)
plt.show()

#加法模型(Generalized additive models, GAM)

# !pip install interpret

import interpret.glassbox

# 使用 Boosting 演算法
model_ebm = interpret.glassbox.ExplainableBoostingRegressor(interactions=0)
model_ebm.fit(X, y)

# 加法模型 Shapley value
explainer_ebm = shap.Explainer(model_ebm.predict, X100)
shap_values_ebm = explainer_ebm(X)

# 特徵影響力
fig,ax = shap.partial_dependence_plot(
    feature_name, model_ebm.predict, X100, model_expected_value=True,
    feature_expected_value=True, show=False, ice=False,
    shap_values=shap_values_ebm[sample_ind:sample_ind+1,:] # 第 21 筆資料
)
plt.show()

shap.plots.scatter(shap_values_ebm[:,feature_name])
plt.show()

shap.plots.waterfall(shap_values_ebm[sample_ind])
plt.show()

shap.plots.beeswarm(shap_values_ebm)
plt.show()

shap.plots.bar(shap_values_ebm)
plt.show()

shap.initjs()
shap.plots.force(shap_values_ebm[sample_ind])

"""
Visualization omitted, Javascript library not loaded!
Have you run `initjs()` in this notebook? If this notebook was from another user you must also trust this notebook (File -> Trust notebook). If you are viewing this notebook on github the Javascript has been stripped for security. If you are using JupyterLab this error is because a JupyterLab extension has not yet been written.
"""



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
