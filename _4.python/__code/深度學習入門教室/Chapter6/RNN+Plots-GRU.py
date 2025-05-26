# coding: utf-8
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
x = Input(shape=input_shape, name='Input')
y = GRU(units=units, activation='sigmoid', name='GRU_1')(x)
model = Model(inputs=[x], outputs=[y])

# SVG形式でモデルを表示 (図6-3-2)
SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))

# 再帰型ニューラルネットワークのモデルを作成、シーケンスを出力
y = GRU(units=units, activation='sigmoid', return_sequences=True, name='GRU_1')(x)
model = Model(inputs=[x], outputs=[y])

# SVG形式でモデルを表示 (図6-3-3)
SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))

# 再帰型ニューラルネットワークのモデルを作成、内部状態も出力
y, state = GRU(units=units, activation='sigmoid', return_state=True, name='GRU_1')(x)
model = Model(inputs=[x], outputs=[y])

# SVG形式でモデルを表示 (図6-3-4)
SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))