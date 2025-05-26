"""
深度學習入門教室

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

from common1 import *
import scipy
import sklearn.linear_model
from sklearn import datasets
from sklearn import metrics
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_classification
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score  # Cross Validation
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier  # 隨機森林分類函數學習機
from sklearn.ensemble import RandomForestRegressor  # 隨機森林函數學習機
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from matplotlib.colors import ListedColormap


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Chapter3\Matplotlib+example.py

# 出力データの準備
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# グラフの描画
fig, ax = plt.subplots()
ax.plot(t, s)

# グラフのラベルとグリッドを描画
ax.set(
    xlabel="time (s)", ylabel="voltage (mV)", title="About as simple as it gets, folks"
)
ax.grid()

show()

print("------------------------------------------------------------")  # 60個

# Chapter3\Sequential.py

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import np_utils
import numpy as np

# ダミーデータ
data = np.random.random((1000, 784))
labels = np.random.randint(10, size=(1000, 1))
labels = np_utils.to_categorical(labels, 10)

model = Sequential()
model.add(Dense(64, activation="relu", input_dim=784))
model.add(Dense(64, activation="relu"))
model.add(Dense(10, activation="softmax"))

# モデルのコンパイル
model.compile(
    optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"]
)

# 学習を行う
model.fit(data, labels)

print("------------------------------------------------------------")  # 60個

# Chapter3\Dogs+vs.+Cat.py

# Dogs vs. Cats

# 必要なライブラリの読込
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
from PIL import Image

# 学習済みモデルVGG16の読込
model = VGG16(weights="imagenet")


# 画像判定のための関数
def predict(filename, featuresize):
    img = image.load_img(filename, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    preds = model.predict(preprocess_input(x))
    results = decode_predictions(preds, top=featuresize)[0]
    return results


# 画像表示のための関数
def showimg(filename, title, i):
    im = Image.open(filename)
    im_list = np.asarray(im)
    plt.subplot(2, 5, i)
    plt.title(title)
    plt.axis("off")
    plt.imshow(im_list)


# 画像を判定
filename = "train/cat.3591.jpg"
plt.figure(figsize=(20, 10))
for i in range(1):
    showimg(filename, "query", i + 1)

show()

results = predict(filename, 10)
for result in results:
    print(result)

# 画像を判定
filename = "train/dog.8035.jpg"
plt.figure(figsize=(20, 10))
for i in range(1):
    showimg(filename, "query", i + 1)

show()

results = predict(filename, 10)
for result in results:
    print(result)

print("------------------------------------------------------------")  # 60個

# Chapter4\MNIST+Example.py

# MNISTサンプル

# Kerasをインポート
import keras

# MINISTのデータの他、必要なモジュールをインポート
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop
from keras.callbacks import EarlyStopping, CSVLogger

# バッチサイズ、クラス数、エポック数を定義
batch_size = 128
num_classes = 10
epochs = 20

# MNISTデータを読込
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# MNISTデータのうち10枚だけ表示
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.title("M_%d" % i)
    plt.axis("off")
    plt.imshow(x_train[i].reshape(28, 28), cmap=None)
show()

# 画像サイズを正規化
x_train = x_train.reshape(60000, 784).astype("float32")
x_test = x_test.reshape(10000, 784).astype("float32")
x_train /= 255
x_test /= 255
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# 確認のために表示
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

# モデルを作成
model = Sequential()
model.add(Dense(512, input_shape=(784,)))
model.add(Activation("relu"))
model.add(Dropout(0.2))
model.add(Dense(512))
model.add(Activation("relu"))
model.add(Dropout(0.2))
model.add(Dense(10))
model.add(Activation("softmax"))

# サマリーを出力
model.summary()

# モデルのコンパイル
model.compile(
    loss="categorical_crossentropy", optimizer=RMSprop(), metrics=["accuracy"]
)

es = EarlyStopping(monitor="val_loss", patience=2)
csv_logger = CSVLogger("training.log")
hist = model.fit(
    x_train,
    y_train,
    batch_size=batch_size,
    epochs=epochs,
    verbose=1,
    validation_split=0.1,
    callbacks=[es, csv_logger],
)

# 学習を実行
score = model.evaluate(x_test, y_test, verbose=0)
print("test loss:", score[0])
print("test acc:", score[1])


# 学習結果を表示
loss = hist.history["loss"]
val_loss = hist.history["val_loss"]
epochs = len(loss)
plt.plot(range(epochs), loss, marker=".", label="loss(training data)")
plt.plot(range(epochs), val_loss, marker=".", label="val_loss(evaluationdata)")
plt.legend(loc="best")
plt.grid()
plt.xlabel("epoch")
plt.ylabel("loss")
show()

print("------------------------------------------------------------")  # 60個

# Chapter5\CNN+Plots-binarysigm.py

# Conv2Dを使ったCNNの例

# CNN Model 8 - Binary Sigmoid
# Kerasとその他ライブラリをインポート
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Conv2D
from keras.utils import np_utils

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# 畳み込みニューラルネットワーク→平滑化→全結合層の二値出力モデルを作成
model = Sequential()
model.add(
    Conv2D(
        filters=3,
        kernel_size=(3, 3),
        input_shape=(6, 6, 1),
        padding="same",
        name="Conv2D_1",
    )
)
model.add(Flatten(name="Flatten_1"))
model.add(Dense(units=1, activation="sigmoid", name="Dense_1"))

# SVG形式でモデルを表示
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

print("------------------------------------------------------------")  # 60個

# Chapter5\CNN+Plots-flattenanddense.py

# Conv2Dを使ったCNNの例

# CNN Model 7 - Flatten and Dense
# Kerasとその他ライブラリをインポート
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Conv2D
from keras.utils import np_utils

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# 畳み込みニューラルネットワークの出力を1次元に平滑化して全結合層に渡すモデルを作成
model = Sequential()
model.add(
    Conv2D(
        filters=3,
        kernel_size=(3, 3),
        input_shape=(6, 6, 1),
        padding="same",
        name="Conv2D_1",
    )
)
model.add(Flatten(name="Flatten_1"))
model.add(Dense(units=10, activation="softmax", name="Dense_1"))

# SVG形式でモデルを表示
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

print("------------------------------------------------------------")  # 60個

# Chapter5\CNN+Plots-multisigm.py

# Conv2Dを使ったCNNの例

# CNN Model 9 - Multi Sigmoid
# Kerasとその他ライブラリをインポート
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Conv2D
from keras.utils import np_utils

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# 畳み込みニューラルネットワーク→平滑化→全結合層の多値出力モデルを作成
model = Sequential()
model.add(
    Conv2D(
        filters=3,
        kernel_size=(3, 3),
        input_shape=(6, 6, 1),
        padding="same",
        name="Conv2D_1",
    )
)
model.add(Flatten(name="Flatten_1"))
model.add(Dense(units=10, activation="sigmoid", name="Dense_1"))

# SVG形式でモデルを表示
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

print("------------------------------------------------------------")  # 60個

# Chapter5\CNN+Plots-onelayter.py

# Conv2Dを使ったCNNの例

# CNN Model 1 - one layer
# Kerasとその他ライブラリをインポート
from keras.models import Sequential, Model
from keras.layers import Conv2D
from keras.utils import np_utils

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# 畳み込みニューラルネットワークのモデルを作成
model = Sequential()
model.add(Conv2D(filters=3, kernel_size=(3, 3), input_shape=(6, 6, 1), name="Conv2D_1"))

# SVG形式でモデルを表示
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

print("------------------------------------------------------------")  # 60個

# Chapter5\CNN+Plots-pooling.py

# Conv2Dを使ったCNNの例

# CNN Model 6 - Pooling
# Kerasとその他ライブラリをインポート
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# 活性化関数を ReLU にした畳み込みニューラルネットワークのモデルを作成
model = Sequential()
model.add(
    Conv2D(
        filters=3, kernel_size=(3, 3), input_shape=(6, 6, 1), strides=2, name="Conv2D_1"
    )
)
model.add(MaxPooling2D(pool_size=(2, 2), name="MaxPooling2D_1"))

# SVG形式でモデルを表示
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

print("------------------------------------------------------------")  # 60個

# Chapter5\CNN+Plots-ReLU.py

# Conv2Dを使ったCNNの例

# CNN Model 5 - ReLU
# Kerasとその他ライブラリをインポート
from keras.models import Sequential, Model
from keras.layers import Activation, Conv2D
from keras.utils import np_utils

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# 活性化関数を ReLU にした畳み込みニューラルネットワークのモデルを作成
model = Sequential()
model.add(
    Conv2D(
        filters=3,
        kernel_size=(3, 3),
        input_shape=(6, 6, 1),
        activation="relu",
        name="Conv2D_1",
    )
)

# SVG形式でモデルを表示
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

print("------------------------------------------------------------")  # 60個

# Chapter5\CNN+Plots-twolayers.py

# Conv2Dを使ったCNNの例

# CNN Model 2 - two layers
# Kerasとその他ライブラリをインポート
from keras.models import Sequential, Model
from keras.layers import Conv2D
from keras.utils import np_utils

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# 2層の畳み込みニューラルネットワークのモデルを作成
model = Sequential()
model.add(Conv2D(filters=3, kernel_size=(3, 3), input_shape=(6, 6, 1), name="Conv2D_1"))
model.add(Conv2D(filters=2, kernel_size=(3, 3), name="Conv2D_2"))

# SVG形式でモデルを表示
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

print("------------------------------------------------------------")  # 60個

# Chapter5\CNN+Plots-twostrides.py

# Conv2Dを使ったCNNの例

# CNN Model 4 - two strides
# Kerasとその他ライブラリをインポート
from keras.models import Sequential, Model
from keras.layers import Conv2D
from keras.utils import np_utils

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# ストライド2の畳み込みニューラルネットワークのモデルを作成
model = Sequential()
model.add(
    Conv2D(
        filters=3, kernel_size=(3, 3), input_shape=(6, 6, 1), strides=2, name="Conv2D_1"
    )
)

# SVG形式でモデルを表示
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

print("------------------------------------------------------------")  # 60個

# Chapter5\CNN+Plots-zeropadding.py

# Conv2Dを使ったCNNの例

# CNN Model 3 - zero padding
# Kerasとその他ライブラリをインポート
from keras.models import Sequential, Model
from keras.layers import Conv2D
from keras.utils import np_utils

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# パディングつき畳み込みニューラルネットワークのモデルを作成
model = Sequential()
model.add(
    Conv2D(
        filters=3,
        kernel_size=(3, 3),
        input_shape=(6, 6, 1),
        padding="same",
        name="Conv2D_1",
    )
)

# SVG形式でモデルを表示
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

print("------------------------------------------------------------")  # 60個

# Chapter5\CNN+Train-dropout.py

# CNNを使った学習の例

# CNN Train 2 - dropout
# Kerasとその他ライブラリをインポート
import keras
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Conv2D, Dropout
from keras.utils import np_utils
from keras.optimizers import SGD

# 早期終了のための Callbacks とデータ処理に必要な Numpy をインポート
import keras.callbacks as callbacks
import numpy as np

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# ランダムな数値でダミーデータを用意
x_train = np.random.random((100, 6, 6, 1))
y_train = keras.utils.to_categorical(
    np.random.randint(10, size=(100, 1)), num_classes=10
)
x_test = np.random.random((20, 6, 6, 1))
y_test = keras.utils.to_categorical(np.random.randint(10, size=(20, 1)), num_classes=10)

# ドロップアウトを追加して畳み込みニューラルネットワークのモデルを作成
model = Sequential()
model.add(Conv2D(filters=3, kernel_size=(3, 3), input_shape=(6, 6, 1), name="Conv2D_1"))
model.add(Dropout(rate=0.5, name="Dropout_1"))
model.add(Flatten(name="Flatten_1"))
model.add(Dense(units=10, activation="softmax", name="Dense_1"))

# シーケンスを出力
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

# 早期終了を設定
earlyStopping = callbacks.EarlyStopping(monitor="val_loss", patience=5)

# モデルのコンパイル
model.compile(loss="mean_squared_error", optimizer="sgd")
model.fit(
    x_train,
    y_train,
    batch_size=32,
    epochs=10,
    callbacks=[earlyStopping],
    validation_split=0.2,
)

print("------------------------------------------------------------")  # 60個

# Chapter5\CNN+Train-example.py

# CNNを使った学習の例

# CNN Train 1
# Kerasとその他ライブラリをインポート
import keras
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Conv2D
from keras.utils import np_utils
from keras.optimizers import SGD

# 早期終了のための Callbacks とデータ処理に必要な Numpy をインポート
import keras.callbacks as callbacks
import numpy as np

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# ランダムな数値でダミーデータを用意
x_train = np.random.random((100, 6, 6, 1))
y_train = keras.utils.to_categorical(
    np.random.randint(10, size=(100, 1)), num_classes=10
)
x_test = np.random.random((20, 6, 6, 1))
y_test = keras.utils.to_categorical(np.random.randint(10, size=(20, 1)), num_classes=10)

# 畳み込みニューラルネットワークのモデルを作成
model = Sequential()
model.add(
    Conv2D(
        filters=3,
        kernel_size=(3, 3),
        input_shape=(6, 6, 1),
        kernel_initializer="lecun_uniform",
        name="Conv2D_1",
    )
)
model.add(Flatten(name="Flatten_1"))
model.add(Dense(units=10, activation="softmax", name="Dense_1"))

# シーケンスを出力
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

# 早期終了を設定
earlyStopping = callbacks.EarlyStopping(monitor="val_loss", patience=5)

# モデルのコンパイル
model.compile(loss="mean_squared_error", optimizer="sgd")
model.fit(
    x_train,
    y_train,
    batch_size=32,
    epochs=10,
    callbacks=[earlyStopping],
    validation_split=0.2,
)

print("------------------------------------------------------------")  # 60個

# Chapter6\RNN+Example.py

# 再帰型ニューラルネットワークの例

# Kerasで使うライブラリの読み込み
from keras.models import Sequential, Model
from keras.layers import Input, Embedding, LSTM, Dense
from keras.layers.wrappers import TimeDistributed

# IMDBデータセットの読み込み
from keras.datasets import imdb

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# Numpyなどツールの読み込み
from keras.utils import to_categorical, np_utils

# データ数、特徴数、ベクトルの次元数、ステップ数など
train_reviews = 5000
valid_reviews = 100
max_features = 5000
embedding_size = 256
step_size = 5
batch_size = 32
index_from = 2
rnn_units = 128
epochs = 2
word_index_prev = {"<PAD>": 0, "<START>": 1, "<UNK>": 2}

# IMDBデータを読み込み
(x_train, y_train), (x_test, y_test) = imdb.load_data(
    num_words=max_features, index_from=index_from
)

# IMDBデータから単語情報を抽出
word_index = {
    word: (index + index_from)
    for word, index in imdb.get_word_index().items()
    if (index + index_from) < max_features
}
word_index.update(word_index_prev)

# 単語情報から辞書を作成
index_word = {index: word for word, index in word_index.items()}


# 文章を表示する関数
def print_sentence(sentence):
    for index in sentence:
        print(index_word[index], end=" ")
    print()


# 最初の１文を表示
print_sentence(x_train[0])

# 学習データとテストデータに分ける
data_train = [t for s in x_train[:train_reviews] for t in s]
data_valid = [
    t for s in x_train[train_reviews : train_reviews + valid_reviews] for t in s
]


# バッチ処理のための関数定義
def batch_generator(data, batch_size, step_size):
    seg_len = len(data) // batch_size
    steps_per_epoch = seg_len // step_size
    data_seg_list = np.asarray(
        [data[int(i * seg_len) : int((i + 1) * seg_len)] for i in range(batch_size)]
    )
    data_seg_list
    i = 0
    while True:
        x = data_seg_list[:, int(i * step_size) : int((i + 1) * step_size)]
        y = np.asarray(
            [
                to_categorical(
                    data_seg_list[
                        j, int(i * step_size + 1) : int((i + 1) * step_size + 1)
                    ],
                    max_features,
                )
                for j in range(batch_size)
            ]
        )
        yield x, y
        i += 1
        if i >= steps_per_epoch:
            i = 0


# LSTMを使ってモデルを設計
w = Input(shape=(step_size,), name="Input")
x = Embedding(input_dim=max_features, output_dim=embedding_size, name="Embedding")(w)
y = LSTM(
    units=rnn_units,
    return_sequences=True,
    dropout=0.5,
    recurrent_dropout=0.5,
    name="LSTM",
)(x)
w_next = TimeDistributed(
    Dense(units=max_features, activation="softmax", name="Dense"),
    name="TimeDistributed",
)(y)

# モデルを作成
model = Model(inputs=[w], outputs=[w_next])

# モデルの表示
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

# モデルのコンパイル
model.compile(
    optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"]
)

# バッチ処理のデータセットを作成
gen_train = batch_generator(data_train, batch_size, step_size)
gen_valid = batch_generator(data_valid, batch_size, step_size)

# ステップ数を計算
steps_per_epoch_train = len(data_train) / batch_size / step_size
steps_per_epoch_valid = len(data_valid) / batch_size / step_size

# バッチ処理ごとにデータを学習
model.fit_generator(
    generator=gen_train,
    steps_per_epoch=steps_per_epoch_train,
    epochs=epochs,
    validation_data=gen_valid,
    validation_steps=steps_per_epoch_valid,
)


# 次にくる単語を選ぶ関数
def sample(preds, temperature=1.0):
    preds = np.log(preds) / temperature
    preds = np.exp(preds) / np.sum(np.exp(preds))
    choices = range(len(preds))
    return np.random.choice(choices, p=preds)


# ランダムに文章を生成する関数
def sample_sentences(num_sentences, sample_sent_len=20):
    for x_test_i in x_test[:num_sentences]:
        x = np.zeros((1, step_size))
        sentence = x_test_i[:step_size]

        for i in range(sample_sent_len):
            for j, index in enumerate(sentence[-step_size:]):
                x[0, j] = index
            preds = model.predict(x)[0][-1]
            next_index = sample(preds)
            sentence.append(next_index)

        print_sentence(sentence)


# ランダムに文章を抽出
sample_sentences(num_sentences=20, sample_sent_len=15)

# weightを正規化
norm_weights = np_utils.normalize(model.get_weights()[0])


# 近い意味の単語を表示する関数
def print_closest_words(word, nb_closest=10):
    index = word_index[word]
    distances = np.dot(norm_weights, norm_weights[index])
    c_indexes = np.argsort(np.squeeze(distances))[-nb_closest:][::-1]
    for c_index in c_indexes:
        print(index_word[c_index], distances[c_index])


# 近い意味の単語を表示
words = [
    "3",
    "two",
    "great",
    "money",
    "years",
    "look",
    "own",
    "us",
    "using",
]

for word in words:
    if word in word_index:
        print("====", word)
        print_closest_words(word)

print("------------------------------------------------------------")  # 60個

# Chapter6\RNN+Plots-GRU.py

# SimpleRNN, LSTM, GRUを使ったRNNの例

# RNN Model 3 - GRU
# Kerasとその他ライブラリをインポート
from keras.models import Model
from keras.layers import Input, GRU

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# ユニット数、ステップ数、入力次元数、入力データの形状を定義
units = 10
time_steps = 5
input_dim = 15
input_shape = (time_steps, input_dim)

# 再帰型ニューラルネットワークのモデルを作成
x = Input(shape=input_shape, name="Input")
y = GRU(units=units, activation="sigmoid", name="GRU_1")(x)
model = Model(inputs=[x], outputs=[y])

# SVG形式でモデルを表示 (図6-3-2)
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

# 再帰型ニューラルネットワークのモデルを作成、シーケンスを出力
y = GRU(units=units, activation="sigmoid", return_sequences=True, name="GRU_1")(x)
model = Model(inputs=[x], outputs=[y])

# SVG形式でモデルを表示 (図6-3-3)
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

# 再帰型ニューラルネットワークのモデルを作成、内部状態も出力
y, state = GRU(units=units, activation="sigmoid", return_state=True, name="GRU_1")(x)
model = Model(inputs=[x], outputs=[y])

# SVG形式でモデルを表示 (図6-3-4)
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

print("------------------------------------------------------------")  # 60個

# Chapter6\RNN+Plots-LSTM.py

# SimpleRNN, LSTM, GRUを使ったRNNの例

# RNN Model 2 - LSTM
# Kerasとその他ライブラリをインポート
from keras.models import Model
from keras.layers import Input, LSTM

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# ユニット数、ステップ数、入力次元数、入力データの形状を定義
units = 10
time_steps = 5
input_dim = 15
input_shape = (time_steps, input_dim)

# 再帰型ニューラルネットワークのモデルを作成
x = Input(shape=input_shape, name="Input")
y = LSTM(units=units, activation="sigmoid", name="LSTM_1")(x)
model = Model(inputs=[x], outputs=[y])

# SVG形式でモデルを表示 (図6-2-2)
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

# 再帰型ニューラルネットワークのモデルを作成、シーケンスを出力
y = LSTM(units=units, activation="sigmoid", return_sequences=True, name="LSTM_1")(x)
model = Model(inputs=[x], outputs=[y])

# SVG形式でモデルを表示 (図6-2-3)
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

# 再帰型ニューラルネットワークのモデルを作成、内部状態も出力
x = Input(shape=input_shape, name="Input")
y, state_1, state_2 = LSTM(
    units=units, activation="sigmoid", return_state=True, name="LSTM_1"
)(x)
model = Model(inputs=[x], outputs=[y])

# SVG形式でモデルを表示 (図6-2-4)
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

print("------------------------------------------------------------")  # 60個

# Chapter6\RNN+Plots-SimpleRNN.py

# SimpleRNN, LSTM, GRUを使ったRNNの例

# RNN Model 1 - SimpleRNN
# Kerasとその他ライブラリをインポート
from keras.models import Model
from keras.layers import Input, SimpleRNN

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# ユニット数、ステップ数、入力次元数、入力データの形状を定義
units = 10
time_steps = 5
input_dim = 15
input_shape = (time_steps, input_dim)

# 再帰型ニューラルネットワークのモデルを作成
x = Input(shape=input_shape, name="Input")
y = SimpleRNN(units=units, activation="sigmoid", name="SimpleRNN_1")(x)
model = Model(inputs=[x], outputs=[y])

# SVG形式でモデルを表示 (図6-1-5)
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

# 再帰型ニューラルネットワークのモデルを作成、シーケンスを出力
y = SimpleRNN(
    units=units, activation="sigmoid", return_sequences=True, name="SimpleRNN_1"
)(x)
model = Model(inputs=[x], outputs=[y])

# SVG形式でモデルを表示 (図6-1-6)
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

# 再帰型ニューラルネットワークのモデルを作成、内部状態も出力
y, state = SimpleRNN(
    units=units, activation="sigmoid", return_state=True, name="SimpleRNN_1"
)(x)
model = Model(inputs=[x], outputs=[y])

# SVG形式でモデルを表示 (図6-1-7)
SVG(model_to_dot(model, show_shapes=True).create(prog="dot", format="svg"))

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
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------")  # 30個
