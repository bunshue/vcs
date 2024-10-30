"""
20190327-空氣盒子數據時間序列預測(全高雄1982-2018)

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

from matplotlib.pylab import rcParams

rcParams["figure.figsize"] = 20, 10

# for normalizing data
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 1))

df = pd.read_excel("data/TimeSeries_198211-201811.xlsx")

cc = df.head()
print(cc)

from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
mpl.rcParams["axes.unicode_minus"] = False

cc = df.shape
print(cc)

# setting index as date
df["Date"] = pd.to_datetime(df.Date, format="%Y-%m-%d")
df.index = df["Date"]

# plot
plt.figure(figsize=(16, 8))
plt.plot(df["PM25"], label="PM2.5時間序列圖")
plt.show()


# 移動平均

# creating dataframe with date and the target variable
data = df.sort_index(ascending=True, axis=0)
new_data = pd.DataFrame(index=range(0, len(df)), columns=["Date", "PM25"])

for i in range(0, len(data)):
    new_data["Date"][i] = data["Date"][i]
    new_data["PM25"][i] = data["PM25"][i]

# splitting into train and validation
train = new_data[:2825]
valid = new_data[2825:]

cc = new_data.shape, train.shape, valid.shape
print(cc)

train["Date"].min(), train["Date"].max(), valid["Date"].min(), valid["Date"].max()

# make predictions
preds = []
for i in range(0, 1211):
    a = train["PM25"][len(train) - 1211 + i :].sum() + sum(preds)
    b = a / 1211
    preds.append(b)

cc = np.any(new_data.isnull()) == True
print(cc)

valid["Predictions"] = 0
valid["Predictions"] = preds
plt.xlabel("年份")
plt.xlim((1900, 2030))
# plt.ylim((0, 80))
plt.title("PM2.5的移動平均分析")
plt.plot(train["PM25"])
plt.plot(valid[["PM25", "Predictions"]])
plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

# creating dataframe
data = df.sort_index(ascending=True, axis=0)
new_data = pd.DataFrame(index=range(0, len(df)), columns=["Date", "PM25"])
for i in range(0, len(data)):
    new_data["Date"][i] = data["Date"][i]
    new_data["PM25"][i] = data["PM25"][i]

# setting index
new_data.index = new_data.Date
new_data.drop("Date", axis=1, inplace=True)

# creating train and test sets
dataset = new_data.values

train = dataset[0:2825, :]
valid = dataset[2825:, :]

# converting dataset into x_train and y_train
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

x_train, y_train = [], []
for i in range(60, len(train)):
    x_train.append(scaled_data[i - 60 : i, 0])
    y_train.append(scaled_data[i, 0])
x_train, y_train = np.array(x_train), np.array(y_train)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# create and fit the LSTM network
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(1))

model.compile(loss="mean_squared_error", optimizer="adam")
model.fit(x_train, y_train, epochs=1, batch_size=1, verbose=2)

# predicting 246 values, using past 60 from the train data
inputs = new_data[len(new_data) - len(valid) - 60 :].values
inputs = inputs.reshape(-1, 1)
inputs = scaler.transform(inputs)

X_test = []
for i in range(60, inputs.shape[0]):
    X_test.append(inputs[i - 60 : i, 0])
X_test = np.array(X_test)

X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
PM25 = model.predict(X_test)
PM25 = scaler.inverse_transform(PM25)


train = new_data[:2825]
valid = new_data[2825:]
valid["Predictions"] = PM25
plt.plot(train["PM25"])
plt.plot(valid[["PM25", "Predictions"]])

plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
