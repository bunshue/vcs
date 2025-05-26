# coding: utf-8
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

# Windows の場合は以下を追加
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# ランダムな数値でダミーデータを用意
x_train = np.random.random((100, 6, 6, 1))
y_train = keras.utils.to_categorical(np.random.randint(10, size=(100, 1)), num_classes=10)
x_test = np.random.random((20, 6, 6, 1))
y_test = keras.utils.to_categorical(np.random.randint(10, size=(20, 1)), num_classes=10)

# 畳み込みニューラルネットワークのモデルを作成
model = Sequential()
model.add(Conv2D(filters=3, kernel_size=(3, 3), input_shape=(6, 6, 1), kernel_initializer='lecun_uniform', name='Conv2D_1'))
model.add(Flatten(name='Flatten_1'))
model.add(Dense(units=10, activation='softmax', name='Dense_1'))

# シーケンスを出力
SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))

# 早期終了を設定
earlyStopping = callbacks.EarlyStopping(monitor='val_loss', patience=5)

# モデルのコンパイル
model.compile(loss='mean_squared_error', optimizer='sgd')
model.fit(x_train, y_train, batch_size=32, epochs=10, callbacks=[earlyStopping], validation_split=0.2)