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

""" 不知道在演什麼

#MLflow 測試
#載入相關套件

from sklearn import datasets
import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import mlflow
import mlflow.sklearn

#載入資料集

X, y = datasets.load_diabetes(return_X_y=True)

#資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

#模型訓練與評估

# 定義模型參數
alpha = 1
l1_ratio = 1

with mlflow.start_run():
    # 模型訓練
    model = ElasticNet(alpha = alpha,
                       l1_ratio = l1_ratio)
    model.fit(X_train,y_train)
    
    # 模型評估
    pred = model.predict(X_test)
    rmse = mean_squared_error(pred, y_test)
    abs_error = mean_absolute_error(pred, y_test)
    r2 = r2_score(pred, y_test)
    
    # MLflow 記錄
    mlflow.log_param('alpha', alpha)
    mlflow.log_param('l1_ratio', l1_ratio)
    mlflow.log_metric('rmse', rmse)
    mlflow.log_metric('abs_error', abs_error)
    mlflow.log_metric('r2', r2)
    
    # MLflow 記錄模型
    mlflow.sklearn.log_model(model, "model")


#模型評估

mlflow.sklearn.log_model(model, "model")
"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

#乳癌診斷預測

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#載入資料集

ds = datasets.load_breast_cancer()

#2. 資料清理、資料探索與分析

# 資料集說明
print(ds.DESCR)

import pandas as pd
df = pd.DataFrame(ds.data, columns=ds.feature_names)
print(df)

y = ds.target
print(y)

print(ds.target_names)

# 觀察資料集彙總資訊
cc = df.info()
print(df)

# 描述統計量
df.describe()

# 箱型圖
import seaborn as sns
sns.boxplot(data=df)
plt.show()


# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

print("繪圖")

# y 各類別資料筆數統計
import seaborn as sns
sns.countplot(x=y)
plt.show()

# 以Pandas函數統計各類別資料筆數
cc = pd.Series(y).value_counts()
print(cc)

#3. 不須進行特徵工程

#4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

print(y_train)

#特徵縮放

scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

#5. 選擇演算法

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

#6. 模型訓練

clf.fit(X_train_std, y_train)

"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

#7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

print("計算準確率")
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

# 混淆矩陣
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred)
                              , display_labels=ds.target_names)
disp.plot()
plt.show()

#8. 模型評估，暫不進行

#9. 模型佈署

# 模型存檔
import joblib

joblib.dump(clf, 'tmp_cancer_model.joblib')
joblib.dump(scaler, 'tmp_cancer_scaler.joblib');



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()



