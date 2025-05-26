# coding: utf-8
# Conv2Dを使ったCNNの例

# CNN Model 9 - Multi Sigmoid
# Kerasとその他ライブラリをインポート
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Conv2D
from keras.utils import np_utils

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# Windows の場合は以下を追加
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# 畳み込みニューラルネットワーク→平滑化→全結合層の多値出力モデルを作成
model = Sequential()
model.add(Conv2D(filters=3, kernel_size=(3, 3), input_shape=(6, 6, 1), padding='same', name='Conv2D_1'))
model.add(Flatten(name='Flatten_1'))
model.add(Dense(units=10, activation='sigmoid', name='Dense_1'))

# SVG形式でモデルを表示
SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))