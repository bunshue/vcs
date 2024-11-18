"""
我們終於要介紹三大神經網路的最後一個, 也就是 RNN。
RNN 有不少的變型, 例如 LSTM 和 GRU 等等, 不過我們都通稱叫 RNN。
RNN 是一種「有記憶」的神經網路, 非常適合時間序列啦, 或是不定長度的輸入資料。

我們來看看怎麼樣用 RNN 做電影評論的「情意分析」,
也就是知道一則評論究竟是「正評」還是「負評」。

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

# 1. 讀入深度學習套件

from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM

# from tensorflow.keras.datasets import imdb
from keras.datasets import imdb

# 2. 讀入數據
# 讀入 IMDB 電影數據庫影評的部份。

# 要注意這裡我們限制只選「最常用」1 萬字, 也就是超過這範圍的就當不存在。
# 這是文字分析常會做的事。
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)

print("訓練總筆數:", len(x_train))
print("測試總筆數:", len(x_test))

# 25000
# 25000

print(len(x_train[0]))

# 218

print(len(x_train[1]))

# 189

print(y_train[0])

# 1

print(y_train[1])

# 0

# 輸入資料部份
# 我們來看一下輸入部份長什麼樣子?

for n in x_train[24999]:
    print(n, end=" ")
# 注意這其實是一個 list 而不是 array, 原因是每筆資料 (每段影評) 長度自然是不一樣的! 我們檢查一下前 10 筆的長度就可以知道。

print(len(x_train[24999]))

# 153

print(len(x_train[9982]))

# 156

print(len(x_train[9487]))

# 104
# 最後要說明的是, 在每筆輸入資料的數字都代表英文的一個單字。編號方式是在我們資料庫裡所有文字的排序: 也就是出現頻率越高, 代表的數字就越小。


# 3. 資料處理
x_train = sequence.pad_sequences(x_train, maxlen=100)
x_test = sequence.pad_sequences(x_test, maxlen=100)

# 4. step 01: 打造一個函數學習機

model = Sequential()
model.add(Embedding(10000, 128))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation="sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

print("檢視神經網路")
model.summary()  # 檢視神經網路

# (128+128+1)*4*128 = 131584

# 學習訓練.fit
model.fit(x_train, y_train, batch_size=32, epochs=10, validation_data=(x_test, y_test))

model_json = model.to_json()
open("imdb_model_architecture.json", "w").write(model_json)
model.save_weights("imdb_model_weights.h5")

print("------------------------------------------------------------")  # 60個

# new~~~~~~


# 輸出資料部份
# 輸出方面應該很容易想像, 我們來看看前 10 筆。
# 結果自然就是 0 (負評) 或 1 (正評)。

print(y_train[:10])

# array([1, 0, 0, 1, 0, 0, 1, 0, 1, 0])

print(y_train[24999])

# 0

# 送入神經網路的輸入處理
# 雖然 RNN 是可以處理不同長度的輸入, 在寫程式時我們還是要
# 1.設輸入文字長度的上限
# 2.把每段文字都弄成一樣長, 太短的後面補上 0

from keras.preprocessing import sequence

x_train = sequence.pad_sequences(x_train, maxlen=150)
x_test = sequence.pad_sequences(x_test, maxlen=150)

print(x_train.shape)

# (25000, 150)

# 至此我們可以來寫我們的第一個 RNN 了!

# 09-03 打造你的 RNN
"""
這裡我們選用 LSTM, 基本上用哪種 RNN 寫法都是差不多的!
決定神經網路架構

    先將 10000 維的文字壓到 N 維
    然後用 K 個 LSTM 神經元做隱藏層
    最後一個 output, 直接用 sigmoid 送出

建構我們的神經網路

文字我們用 1-hot 表示是很標準的方式, 不過要注意的是, 因為我們指定要 1 萬個字, 所以每個字是用 1 萬維的向量表示! 這一來很浪費記憶空間, 二來字和字間基本上是沒有關係的。我們可以用某種「合理」的方式, 把字壓到比較小的維度, 這些向量又代表某些意思 (比如說兩個字代表的向量角度小表相關程度大) 等等。

這聽來很複雜的事叫 "word embedding", 而事實上 Keras 會幫我們做。我們只需告訴 Keras 原來最大的數字是多少 (10000), 還有我們打算壓到幾維 (N)。
"""

N = 3  # 文字要壓到 N 維
K = 12  # LSTM 有 K 個神經元

from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM

model = Sequential()

model.add(Embedding(10000, N))

# LSTM 層, 我們做 K 個 LSTM Cells。

model.add(LSTM(K))

# 單純透過 sigmoid 輸出。

model.add(Dense(1, activation="sigmoid"))

# 組裝

# 這次我們用 binary_crossentropy 做我們的 loss function, 另外用一個很潮的 Adam 學習法。

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

print("檢視神經網路")
model.summary()  # 檢視神經網路

# (4*7 + 4)*K = 128

# 09-04 訓練

"""
我們用的 embedding 中, 會被 batch_size 影響輸入。輸入的 shape 會是

(batch_size, 每筆上限)

也就是 (32,100) 輸出是 (32,100,128), 其中 128 是我們決定要壓成幾維的向量。
"""

# 學習訓練.fit
model.fit(x_train, y_train, batch_size=32, epochs=5)

# 09-05 檢視結果
# 分數
# 我們照例來看看測試資料的分數。

score = model.evaluate(x_test, y_test)
print(f"測試資料的 loss = {score[0]}")
print(f"測試資正確率 = {score[1]}")

# 測試資料的 loss = 0.36388471513748166
# 測試資正確率 = 0.852400004863739

# 儲存結果
# 這裡有 8 成我們可以正確分辨, 看來還不差, 照例我們把結果存檔。

model_json = model.to_json()

open("imdb_model_arch.json", "w").write(model_json)

model.save_weights("imdb_model_weights.h5")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

sequence_length = 10  # 特徵資料個數
split = 0.95  # 訓練資料比率

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告
filename = "twstock_all.csv"
df = pd.read_csv(filename, encoding="big5")  # 以pandas讀取檔案
ddprice = pd.DataFrame(df["收盤價"])

data_all = np.array(df).astype(float)  # 轉為浮點型別矩陣
scaler = MinMaxScaler()
data_all = scaler.fit_transform(data_all)  # 將數據縮放為0~1之間
data = []
for i in range(len(data_all) - sequence_length - 1):
    data.append(data_all[i : i + sequence_length + 1])  # 每筆data資料有11欄
reshaped_data = np.array(data).astype("float64")
x = reshaped_data[:, :-1]  # 第1至第10個欄位為特徵
y = reshaped_data[:, -1]  # 第11個欄位為label
split_boundary = int(reshaped_data.shape[0] * split)  # 分離資料
train_x = x[:split_boundary]  # 訓練特徵資料
test_x = x[split_boundary:]  # test特徵資料
train_y = y[:split_boundary]  # 訓練label資料
test_y = y[split_boundary:]  # test的label資料

model = Sequential()
model.add(LSTM(input_shape=(10, 1), units=256, unroll=False))  # LSTM層
model.add(Dense(units=1))  # 輸出層：1 個神經元
model.compile(loss="mse", optimizer="adam", metrics=["accuracy"])
model.fit(train_x, train_y, batch_size=100, epochs=300, validation_split=0.1, verbose=2)
predict = model.predict(test_x)
predict = np.reshape(predict, (predict.size,))  # 轉換為1維矩陣
predict = scaler.inverse_transform([[i] for i in predict_y])  # 還原
test_y = scaler.inverse_transform(test_y)  # 還原

plt.plot(predict, "b:")  # 預測
plt.plot(test_y, "r-")  # 收盤價
plt.legend(["predict", "realdata"])
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

sequence_length = 10  # 特徵資料個數
split = 0.95  # 訓練資料比率

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告
filename = "twstock_all.csv"
df = pd.read_csv(filename, encoding="big5")  # 以pandas讀取檔案
dfprice = pd.DataFrame(df["收盤價"])

data_all = np.array(dfprice).astype(float)  # 轉為浮點型別矩陣
scaler = MinMaxScaler()
data_all = scaler.fit_transform(data_all)  # 將數據縮放為0~1之間
data = []
for i in range(len(data_all) - sequence_length):
    data.append(data_all[i : i + sequence_length + 1])  # 每筆data資料有11欄
reshaped_data = np.array(data).astype("float64")
x = reshaped_data[:, :-1]  # 第1至第10個欄位為特徵
y = reshaped_data[:, -1]  # 第11個欄位為Label
split_boundary = int(reshaped_data.shape[0] * split)  # 分離資料
train_x = x[:split_boundary]  # 訓練特徵資料
test_x = x[split_boundary:]  # test特徵資料
train_y = y[:split_boundary]  # 訓練label資料
test_y = y[split_boundary:]  # test的label資料

model = Sequential()
model.add(LSTM(input_shape=(sequence_length, 1), units=256, unroll=False))  # LSTM層
model.add(Dense(units=1))  # 輸出層：1個神經元
model.compile(loss="mse", optimizer="adam", metrics=["accuracy"])
model.fit(train_x, train_y, batch_size=100, epochs=300, validation_split=0.1, verbose=2)

print("將 模型存檔 存成 h5")
model.save("tmp_stock_rnn_model.h5")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model

sequence_length = 10  # 特徵資料個數
split = 0.95  # 訓練資料比率

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告
filename = "twstock_all.csv"
df = pd.read_csv(filename, encoding="big5")  # 以pandas讀取檔案
dfprice = pd.DataFrame(df["收盤價"])

data_all = np.array(dfprice).astype(float)  # 轉為浮點型別矩陣
scaler = MinMaxScaler()
data_all = scaler.fit_transform(data_all)  # 將數據縮放為0~1之間
data = []
for i in range(len(data_all) - sequence_length):
    data.append(data_all[i : i + sequence_length + 1])  # 每筆data資料有11欄
reshaped_data = np.array(data).astype("float64")
x = reshaped_data[:, :-1]  # 第1至第10個欄位為特徵
y = reshaped_data[:, -1]  # 第11個欄位為label
split_boundary = int(reshaped_data.shape[0] * split)  # 分離資料
train_x = x[:split_boundary]  # 訓練特徵資料
test_x = x[split_boundary:]  # test特徵資料
train_y = y[:split_boundary]  # 訓練label資料
test_y = y[split_boundary:]  # test的label資料

model = load_model("tmp_stock_rnn_model.h5")

predict = model.predict(test_x)
predict = np.reshape(predict, (predict.size,))  # 轉換為1維矩陣
predict = scaler.inverse_transform([[i] for i in predict])  # 還原
test_y = scaler.inverse_transform(test_y)  # 還原

plt.plot(predict, "b:")  # 預測
plt.plot(test_y, "r-")  # 收盤價
plt.legend(["predict", "realdata"])
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
