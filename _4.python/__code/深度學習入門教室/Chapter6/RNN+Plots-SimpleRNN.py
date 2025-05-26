# coding: utf-8
# SimpleRNN, LSTM, GRUを使ったRNNの例

# RNN Model 1 - SimpleRNN
# Kerasとその他ライブラリをインポート
from keras.models import Model
from keras.layers import Input, SimpleRNN

# SVGの表示に必要なライブラリのインポート
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# Windows の場合は以下を追加
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# ユニット数、ステップ数、入力次元数、入力データの形状を定義
units = 10
time_steps = 5
input_dim = 15
input_shape = (time_steps, input_dim)

# 再帰型ニューラルネットワークのモデルを作成
x = Input(shape=input_shape, name='Input')
y = SimpleRNN(units=units, activation='sigmoid', name='SimpleRNN_1')(x)
model = Model(inputs=[x], outputs=[y])

# SVG形式でモデルを表示 (図6-1-5)
SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))

# 再帰型ニューラルネットワークのモデルを作成、シーケンスを出力
y = SimpleRNN(units=units, activation='sigmoid', return_sequences=True, name='SimpleRNN_1')(x)
model = Model(inputs=[x], outputs=[y])

# SVG形式でモデルを表示 (図6-1-6)
SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))

# 再帰型ニューラルネットワークのモデルを作成、内部状態も出力
y, state = SimpleRNN(units=units, activation='sigmoid', return_state=True, name='SimpleRNN_1')(x)
model = Model(inputs=[x], outputs=[y])

# SVG形式でモデルを表示 (図6-1-7)
SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))