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

# 20190407-空氣盒子數據Keras深度學習實作

df = pd.read_excel("data/KH-1982-2018b.xlsx")

# df.dtypes

# 轉換資料型態成float
df["PM25"] = df["PM25"].astype(float)

# 查看資料狀態
cc = df.describe(include="all")
print(cc)

# 分割資料，X為前12項；Y為第13項，且為數值
X = df.iloc[:, 0:12]
y = df.iloc[:, 12].values

# 進行資料前處理，轉換資料尺度
from sklearn.preprocessing import MinMaxScaler

sc = MinMaxScaler()
X = sc.fit_transform(X)
y = y.reshape(-1, 1)
y = sc.fit_transform(y)

# 分成測試與訓練集(80%:20%)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 進行Keras的深度學習
from keras import Sequential  # 使用順序模型
from keras.layers import Dense


def build_regressor():
    # 建立輸入層
    regressor = Sequential()
    regressor.add(
        Dense(128, kernel_initializer="normal", input_dim=12, activation="relu")
    )  # 增加神經層12層
    # 建立隱藏層
    regressor.add(Dense(256, kernel_initializer="normal", activation="relu"))
    regressor.add(Dense(256, kernel_initializer="normal", activation="relu"))
    regressor.add(Dense(256, kernel_initializer="normal", activation="relu"))
    # 建立輸出層:1
    regressor.add(Dense(1, kernel_initializer="normal", activation="linear"))
    # 編譯神經網路
    regressor.compile(
        optimizer="adam", loss="mean_squared_error", metrics=["mae", "accuracy"]
    )
    return regressor


""" no module
from keras.wrappers.scikit_learn import KerasRegressor

regressor = KerasRegressor(build_fn=build_regressor, batch_size=32, epochs=160)

results = regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

loss_and_metrics = model.evaluate(X_train, y_train, batch_size=128)
print(loss_and_metrics)

fig, ax = plt.subplots()
ax.scatter(y_test, y_pred)
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "k--", lw=4)
ax.set_xlabel("Measured")
ax.set_ylabel("Predicted")
plt.show()

y_pred = model.predict(X_test)

range_x = range(1, len(y_pred) + 1)
plt.figure(figsize=(12, 6))
plt.plot(range_x, y_pred, "--o", alpha=0.5, label="Predictions")
plt.plot(range_x, y_test, "-o", alpha=0.8, label="Real")
plt.title("Predictions V.S. Real")
plt.legend()
plt.show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 20190328-空氣盒子數據TensorFlow深度學習實作(台南1982-2018)

# 時間序列繪圖

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_excel("data/Tainan_198211-201811.xlsx")

# 檢查屬性
cc = df.dtypes
print(cc)

# 屬性轉換
df["SO2"] = pd.to_numeric(df.SO2, errors="coerce")
df["CO"] = pd.to_numeric(df.CO, errors="coerce")
df["CO2"] = pd.to_numeric(df.CO2, errors="coerce")
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

cc = df.head(10)
print(cc)

cc = df.dtypes
print(cc)

cc = df.corr()[["PM25"]].sort_values("PM25")
print(cc)

X = df[
    [
        "SO2",
        "CO",
        "CO2",
        "O3",
        "Nox",
        "NO",
        "NO2",
        "THC",
        "NMHC",
        "CH4",
        "WindSpeed",
        "TEMP",
        "Humidity",
    ]
]

y = df["PM25"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=12
)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

"""
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
         normalize=False)
"""
y_pred = regressor.predict(X_test)

df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})

df1 = df.head(20)

print(df1)

df1.plot(kind="bar", figsize=(8, 6))
plt.grid(which="major", linestyle="-", linewidth="0.5", color="green")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")
plt.show()

from sklearn.metrics import mean_absolute_error, median_absolute_error

print("The Explained Variance: %.2f" % regressor.score(X_test, y_test))
print("The Mean Absolute Error: %.2f " % mean_absolute_error(y_test, y_pred))
print("The Median Absolute Error: %.2f " % median_absolute_error(y_test, y_pred))

# 神經網路

import tensorflow as tf
from sklearn.metrics import (
    explained_variance_score,
    mean_absolute_error,
    median_absolute_error,
)
from sklearn.model_selection import train_test_split

df = pd.read_excel("data/Tainan_198211-201811.xlsx")
# execute the describe() function and transpose the output so that it doesn't overflow the width of the screen
cc = df.describe().T
print(cc)

df.info()  # 這樣就已經把資料集彙總資訊印出來

X = df[
    [
        "SO2",
        "CO",
        "O3",
        "CO2",
        "Nox",
        "NO",
        "NO2",
        "THC",
        "NMHC",
        "CH4",
        "WindSpeed",
        "TEMP",
        "Humidity",
    ]
]

y = df["PM25"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=23
)

X_test, X_val, y_test, y_val = train_test_split(
    X_test, y_test, test_size=0.5, random_state=23
)

X_train.shape, X_test.shape, X_val.shape
print(
    "Training instances   {}, Training features   {}".format(
        X_train.shape[0], X_train.shape[1]
    )
)
print(
    "Validation instances {}, Validation features {}".format(
        X_val.shape[0], X_val.shape[1]
    )
)
print(
    "Testing instances    {}, Testing features    {}".format(
        X_test.shape[0], X_test.shape[1]
    )
)

feature_cols = [tf.feature_column.numeric_column(col) for col in X.columns]

regressor = tf.estimator.DNNRegressor(
    feature_columns=feature_cols, hidden_units=[50, 50], model_dir="tf_wx_model"
)


def wx_input_fn(X, y=None, num_epochs=None, shuffle=True, batch_size=400):
    return tf.estimator.inputs.pandas_input_fn(
        x=X, y=y, num_epochs=num_epochs, shuffle=shuffle, batch_size=batch_size
    )


"""
wx_input_fn(X, y=None, num_epochs=None, shuffle=True, batch_size=400)

evaluations = []  
STEPS = 400  
for i in range(100):  
    regressor.train(input_fn=wx_input_fn(X_train, y=y_train), steps=STEPS)
    evaluations.append(regressor.evaluate(input_fn=wx_input_fn(X_val,
                                                               y_val,
                                                               num_epochs=1,
                                                               shuffle=False)))

cc = evaluations[0]
print(cc)

# manually set the parameters of the figure to and appropriate size
plt.rcParams['figure.figsize'] = [14, 10]

loss_values = [ev['loss'] for ev in evaluations]  
training_steps = [ev['global_step'] for ev in evaluations]

plt.scatter(x=training_steps, y=loss_values)  
plt.xlabel('Training steps (Epochs = steps / 2)')  
plt.ylabel('Loss (SSE)')  
plt.show()  

pred = regressor.predict(input_fn=wx_input_fn(X_test,  
                                              num_epochs=1,
                                              shuffle=False))
predictions = np.array([p['predictions'][0] for p in pred])

print("The Explained Variance: %.2f" % explained_variance_score(  
                                            y_test, predictions))  
print("The Mean Absolute Error: %.2f " % mean_absolute_error(  
                                            y_test, predictions))  
print("The Median Absolute Error: %.2f " % median_absolute_error(  
                                            y_test, predictions))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 20190327-空氣盒子數據TensorFlow深度學習實作(鳳山)

# 時間序列繪圖
# 初始環境設定

df = pd.read_excel("data/鳳山.xlsx")  # 共有 417 筆資料
"""
cc = df.head(10)
print(cc)

#資料長度
print(len(df))
print(len(df["PM25"]))

df.info() # 這樣就已經把資料集彙總資訊印出來

cc = df.describe()
print(cc)
"""

print("檢查屬性")
cc = df.dtypes
print(cc)

print("屬性轉換")
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

cc = df.head(10)
print(cc)

print("檢查屬性")
cc = df.dtypes
print(cc)

ax = df.plot(x="Time", y="PM25")
ax.set_xlabel("每月變化")
ax.set_title("1982年11月至2018年11月之PM2.5趨勢變化圖")

plt.show()

print("------------------------------------------------------------")  # 60個

ax = df.plot(x="Time", y="SO2")
ax.set_xlabel("每月變化")
ax.set_title("1982年11月至2018年11月之SO2趨勢變化圖")

plt.show()

print("------------------------------------------------------------")  # 60個

ax = df.plot(x="Time", y="NO2")
ax.set_xlabel("每月變化")
ax.set_title("1982年11月至2018年11月之NO2趨勢變化圖")

plt.show()

print("------------------------------------------------------------")  # 60個

cc = df.corr()[["PM25"]].sort_values("PM25")
print(cc)

X = df[
    [
        "SO2",
        "CO",
        "O3",
        "Nox",
        "NO",
        "NO2",
        "THC",
        "NMHC",
        "CH4",
        "WindSpeed",
        "TEMP",
        "Humidity",
    ]
]

y = df["PM25"]

# 將資料分成訓練組及測試組
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=12
)  # 訓練組8成, 測試組2成

print(X.shape)
print(y.shape)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# 載入線性迴歸，並訓練模型
from sklearn.linear_model import LinearRegression

linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)

y_pred = linear_regression.predict(X_test)

df = pd.DataFrame({"測試資料": y_test, "預測結果": y_pred})

df1 = df.head(20)

print(df1)

df1.plot(kind="bar", figsize=(8, 6))
plt.grid(which="major", linestyle="-", linewidth="0.5", color="green")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")
plt.show()

# 載入迴歸常見的評估指標
from sklearn import metrics

print("評估 測試資料 與 預測結果 的差異")
from sklearn.metrics import mean_absolute_error, median_absolute_error

print("The Explained Variance: %.2f" % linear_regression.score(X_test, y_test))
print("The Mean Absolute Error: %.2f " % mean_absolute_error(y_test, y_pred))
print("The Median Absolute Error: %.2f " % median_absolute_error(y_test, y_pred))

# 神經網路

import tensorflow as tf
from sklearn.metrics import (
    explained_variance_score,
    mean_absolute_error,
    median_absolute_error,
)

df = pd.read_excel("data/鳳山.xlsx")  # 共有 417 筆資料
# execute the describe() function and transpose the output so that it doesn't overflow the width of the screen
cc = df.describe().T
print(cc)

df.info()  # 這樣就已經把資料集彙總資訊印出來

X = df[
    [
        "SO2",
        "CO",
        "O3",
        "Nox",
        "NO",
        "NO2",
        "THC",
        "NMHC",
        "CH4",
        "WindSpeed",
        "TEMP",
        "Humidity",
    ]
]
y = df["PM25"]

# 將資料分成訓練組及測試組
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=23
)  # 訓練組8成, 測試組2成

X_test, X_val, y_test, y_val = train_test_split(
    X_test, y_test, test_size=0.5, random_state=23
)  # 訓練組5成, 測試組5成

cc = X_train.shape, X_test.shape, X_val.shape
print(cc)

print(
    "Training instances   {}, Training features   {}".format(
        X_train.shape[0], X_train.shape[1]
    )
)
print(
    "Validation instances {}, Validation features {}".format(
        X_val.shape[0], X_val.shape[1]
    )
)
print(
    "Testing instances    {}, Testing features    {}".format(
        X_test.shape[0], X_test.shape[1]
    )
)

feature_cols = [tf.feature_column.numeric_column(col) for col in X.columns]

regressor = tf.estimator.DNNRegressor(
    feature_columns=feature_cols, hidden_units=[50, 50], model_dir="tf_wx_model"
)

""" NG
def wx_input_fn(X, y=None, num_epochs=None, shuffle=True, batch_size=400):
    return tf.estimator.inputs.pandas_input_fn(
        x=X, y=y, num_epochs=num_epochs, shuffle=shuffle, batch_size=batch_size
    )


wx_input_fn(X, y=None, num_epochs=None, shuffle=True, batch_size=400)

evaluations = []
STEPS = 400
for i in range(100):
    regressor.train(input_fn=wx_input_fn(X_train, y=y_train), steps=STEPS)
    evaluations.append(
        regressor.evaluate(
            input_fn=wx_input_fn(X_val, y_val, num_epochs=1, shuffle=False)
        )
    )
cc = evaluations[0]
print(cc)

# manually set the parameters of the figure to and appropriate size
plt.rcParams["figure.figsize"] = [14, 10]

loss_values = [ev["loss"] for ev in evaluations]
training_steps = [ev["global_step"] for ev in evaluations]

plt.scatter(x=training_steps, y=loss_values)
plt.xlabel("Training steps (Epochs = steps / 2)")
plt.ylabel("Loss (SSE)")
plt.show()

pred = regressor.predict(input_fn=wx_input_fn(X_test, num_epochs=1, shuffle=False))
predictions = np.array([p["predictions"][0] for p in pred])

print("The Explained Variance: %.2f" % explained_variance_score(y_test, predictions))
print("The Mean Absolute Error: %.2f " % mean_absolute_error(y_test, predictions))
print("The Median Absolute Error: %.2f " % median_absolute_error(y_test, predictions))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 0327-使用TensorFlow的神經網路_PM25(全高雄1982至2018)

# 時間序列繪圖

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

filename = "data/KH-1982-2018.xlsx"
df = pd.read_excel(filename)

# 檢查屬性
cc = df.dtypes
print(cc)

# 屬性轉換
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

cc = df.head(10)
print(cc)

cc = df.dtypes
print(cc)

cc = df.corr()[["PM25"]].sort_values("PM25")
print(cc)

X = df[
    [
        "SO2",
        "CO",
        "O3",
        "Nox",
        "NO",
        "NO2",
        "THC",
        "NMHC",
        "CH4",
        "WindSpeed",
        "TEMP",
        "Humidity",
    ]
]

y = df["PM25"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=12
)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

"""
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
         normalize=False)
"""
y_pred = regressor.predict(X_test)

df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})

df1 = df.head(20)

print(df1)

df1.plot(kind="bar", figsize=(8, 6))
plt.grid(which="major", linestyle="-", linewidth="0.5", color="green")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")
plt.show()

from sklearn.metrics import mean_absolute_error, median_absolute_error

print("The Explained Variance: %.2f" % regressor.score(X_test, y_test))
print("The Mean Absolute Error: %.2f " % mean_absolute_error(y_test, y_pred))
print("The Median Absolute Error: %.2f " % median_absolute_error(y_test, y_pred))

# 神經網路
import tensorflow as tf
from sklearn.metrics import (
    explained_variance_score,
    mean_absolute_error,
    median_absolute_error,
)
from sklearn.model_selection import train_test_split

filename = "data/KH-1982-2018.xlsx"
df = pd.read_excel(filename)
# execute the describe() function and transpose the output so that it doesn't overflow the width of the screen
cc = df.describe().T
print(cc)

df.info()  # 這樣就已經把資料集彙總資訊印出來

X = df[
    [
        "SO2",
        "CO",
        "O3",
        "Nox",
        "NO",
        "NO2",
        "THC",
        "NMHC",
        "CH4",
        "WindSpeed",
        "TEMP",
        "Humidity",
    ]
]

y = df["PM25"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=23
)

X_test, X_val, y_test, y_val = train_test_split(
    X_test, y_test, test_size=0.5, random_state=23
)

X_train.shape, X_test.shape, X_val.shape
print(
    "Training instances   {}, Training features   {}".format(
        X_train.shape[0], X_train.shape[1]
    )
)
print(
    "Validation instances {}, Validation features {}".format(
        X_val.shape[0], X_val.shape[1]
    )
)
print(
    "Testing instances    {}, Testing features    {}".format(
        X_test.shape[0], X_test.shape[1]
    )
)

feature_cols = [tf.feature_column.numeric_column(col) for col in X.columns]

regressor = tf.estimator.DNNRegressor(
    feature_columns=feature_cols, hidden_units=[50, 50], model_dir="tf_wx_model"
)

"""
def wx_input_fn(X, y=None, num_epochs=None, shuffle=True, batch_size=400):  
    return tf.compat.v1.estimator.inputs.pandas_input_fn(x=X,
                                               y=y,
                                               num_epochs=num_epochs,
                                               shuffle=shuffle,
                                               batch_size=batch_size)

# tf.estimator.inputs.numpy_input_fn替换为tf.compat.v1.estimator.inputs.numpy_input_fn

wx_input_fn(X, y=None, num_epochs=None, shuffle=True, batch_size=400)

evaluations = []  

STEPS = 400  
for i in range(100):  
    regressor.train(input_fn=wx_input_fn(X_train, y=y_train), steps=STEPS)
    evaluations.append(regressor.evaluate(input_fn=wx_input_fn(X_val,
                                                               y_val,
                                                               num_epochs=1,
                                                               shuffle=False)))

cc = evaluations[0]
print(cc)

# manually set the parameters of the figure to and appropriate size
plt.rcParams['figure.figsize'] = [14, 10]

loss_values = [ev['loss'] for ev in evaluations]  
training_steps = [ev['global_step'] for ev in evaluations]

plt.scatter(x=training_steps, y=loss_values)  
plt.xlabel('Training steps (Epochs = steps / 2)')  
plt.ylabel('Loss (SSE)')  
plt.show()  

pred = regressor.predict(input_fn=wx_input_fn(X_test,  
                                              num_epochs=1,
                                              shuffle=False))
predictions = np.array([p['predictions'][0] for p in pred])

print("The Explained Variance: %.2f" % explained_variance_score(  
                                            y_test, predictions))  
print("The Mean Absolute Error: %.2f " % mean_absolute_error(  
                                            y_test, predictions))  
print("The Median Absolute Error: %.2f " % median_absolute_error(  
                                            y_test, predictions))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 0328-使用TensorFlow的神經網路_PM25(屏東1982至2018)

# 時間序列繪圖

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from pylab import mpl

df = pd.read_excel("data/Pintung_198211-201811.xlsx")

# 檢查屬性
# df.dtypes

# 屬性轉換

df["SO2"] = pd.to_numeric(df.SO2, errors="coerce")
df["CO"] = pd.to_numeric(df.CO, errors="coerce")
df["CO2"] = pd.to_numeric(df.CO2, errors="coerce")
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

cc = df.head(10)
print(cc)

# df.dtypes

cc = df.corr()[["PM25"]].sort_values("PM25")
print(cc)

X = df[
    [
        "SO2",
        "CO",
        "CO2",
        "O3",
        "Nox",
        "NO",
        "NO2",
        "THC",
        "NMHC",
        "CH4",
        "WindSpeed",
        "TEMP",
        "Humidity",
    ]
]
y = df["PM25"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=12
)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})

df1 = df.head(20)

print(df1)


df1.plot(kind="bar", figsize=(8, 6))
plt.grid(which="major", linestyle="-", linewidth="0.5", color="green")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")
plt.show()

from sklearn.metrics import mean_absolute_error, median_absolute_error

print("The Explained Variance: %.2f" % regressor.score(X_test, y_test))
print("The Mean Absolute Error: %.2f " % mean_absolute_error(y_test, y_pred))
print("The Median Absolute Error: %.2f " % median_absolute_error(y_test, y_pred))
"""
The Explained Variance: 0.60
The Mean Absolute Error: 8.29 
The Median Absolute Error: 5.86 
"""

# 神經網路

import tensorflow as tf
from sklearn.metrics import (
    explained_variance_score,
    mean_absolute_error,
    median_absolute_error,
)
from sklearn.model_selection import train_test_split

df = pd.read_excel("data/Pintung_198211-201811.xlsx")
# execute the describe() function and transpose the output so that it doesn't overflow the width of the screen
cc = df.describe().T
print(cc)

# df.info()

X = df[
    [
        "SO2",
        "CO",
        "O3",
        "CO2",
        "Nox",
        "NO",
        "NO2",
        "THC",
        "NMHC",
        "CH4",
        "WindSpeed",
        "TEMP",
        "Humidity",
    ]
]
y = df["PM25"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=23
)
X_test, X_val, y_test, y_val = train_test_split(
    X_test, y_test, test_size=0.5, random_state=23
)

X_train.shape, X_test.shape, X_val.shape
print(
    "Training instances   {}, Training features   {}".format(
        X_train.shape[0], X_train.shape[1]
    )
)
print(
    "Validation instances {}, Validation features {}".format(
        X_val.shape[0], X_val.shape[1]
    )
)
print(
    "Testing instances    {}, Testing features    {}".format(
        X_test.shape[0], X_test.shape[1]
    )
)

"""
Training instances   732, Training features   13
Validation instances 92, Validation features 13
Testing instances    91, Testing features    13
"""

feature_cols = [tf.feature_column.numeric_column(col) for col in X.columns]

regressor = tf.estimator.DNNRegressor(
    feature_columns=feature_cols, hidden_units=[50, 50], model_dir="tf_wx_model"
)


def wx_input_fn(X, y=None, num_epochs=None, shuffle=True, batch_size=400):
    return tf.estimator.inputs.pandas_input_fn(
        x=X, y=y, num_epochs=num_epochs, shuffle=shuffle, batch_size=batch_size
    )


""" NG
wx_input_fn(X, y=None, num_epochs=None, shuffle=True, batch_size=400)


evaluations = []  
STEPS = 400  
for i in range(100):  
    regressor.train(input_fn=wx_input_fn(X_train, y=y_train), steps=STEPS)
    evaluations.append(regressor.evaluate(input_fn=wx_input_fn(X_val,
                                                               y_val,
                                                               num_epochs=1,
                                                               shuffle=False)))


cc = evaluations[0]
print(cc)
"""

"""
{'average_loss': 19.30102,
 'label/mean': 13.228261,
 'loss': 1775.6938,
 'prediction/mean': 13.002814,
 'global_step': 400}
"""

"""
# manually set the parameters of the figure to and appropriate size
plt.rcParams['figure.figsize'] = [14, 10]

loss_values = [ev['loss'] for ev in evaluations]  
training_steps = [ev['global_step'] for ev in evaluations]

plt.scatter(x=training_steps, y=loss_values)  
plt.xlabel('Training steps (Epochs = steps / 2)')  
plt.ylabel('Loss (SSE)')  
plt.show()  

pred = regressor.predict(input_fn=wx_input_fn(X_test,  
                                              num_epochs=1,
                                              shuffle=False))
predictions = np.array([p['predictions'][0] for p in pred])

print("The Explained Variance: %.2f" % explained_variance_score(  
                                            y_test, predictions))  
print("The Mean Absolute Error: %.2f " % mean_absolute_error(  
                                            y_test, predictions))  
print("The Median Absolute Error: %.2f " % median_absolute_error(  
                                            y_test, predictions))
"""

"""
INFO:tensorflow:Calling model_fn.
INFO:tensorflow:Done calling model_fn.
INFO:tensorflow:Graph was finalized.
INFO:tensorflow:Restoring parameters from tf_wx_model\model.ckpt-40000
INFO:tensorflow:Running local_init_op.
INFO:tensorflow:Done running local_init_op.
The Explained Variance: 0.84
The Mean Absolute Error: 3.48 
The Median Absolute Error: 1.29 
"""

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
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
