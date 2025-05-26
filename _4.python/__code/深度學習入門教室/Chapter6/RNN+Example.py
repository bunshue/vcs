# coding: utf-8
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

# Windows の場合は以下を追加
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# Numpyなどツールの読み込み
from keras.utils import to_categorical, np_utils
import numpy as np


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
word_index_prev = {'<PAD>': 0, '<START>': 1, '<UNK>': 2}

# IMDBデータを読み込み
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features, index_from=index_from)

# IMDBデータから単語情報を抽出
word_index = {word: (index + index_from) for word, index in imdb.get_word_index().items() if (index + index_from) < max_features}
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
data_valid = [t for s in x_train[train_reviews:train_reviews+valid_reviews] for t in s]

# バッチ処理のための関数定義
def batch_generator(data, batch_size, step_size):
    seg_len = len(data) // batch_size
    steps_per_epoch = seg_len // step_size
    data_seg_list = np.asarray([data[int(i*seg_len):int((i+1)*seg_len)] for i in range(batch_size)])
    data_seg_list
    i = 0
    while True:
        x = data_seg_list[:, int(i*step_size):int((i+1)*step_size)]
        y = np.asarray([to_categorical(data_seg_list[j, int(i*step_size+1):int((i+1)*step_size+1)], max_features) for j in range(batch_size)])
        yield x, y
        i += 1
        if i >= steps_per_epoch:
            i = 0

# LSTMを使ってモデルを設計
w = Input(shape=(step_size,), name='Input')
x = Embedding(input_dim=max_features, output_dim=embedding_size, name='Embedding')(w)
y = LSTM(units=rnn_units, return_sequences=True, dropout=0.5, recurrent_dropout=0.5, name='LSTM')(x)
w_next = TimeDistributed(Dense(units=max_features, activation='softmax', name='Dense'), name='TimeDistributed')(y)

# モデルを作成
model = Model(inputs=[w], outputs=[w_next])

# モデルの表示
SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))

# モデルのコンパイル
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# バッチ処理のデータセットを作成
gen_train = batch_generator(data_train, batch_size, step_size)
gen_valid = batch_generator(data_valid, batch_size, step_size)

# ステップ数を計算
steps_per_epoch_train = len(data_train) / batch_size / step_size
steps_per_epoch_valid = len(data_valid) / batch_size / step_size

# バッチ処理ごとにデータを学習
model.fit_generator(generator=gen_train, steps_per_epoch=steps_per_epoch_train, epochs=epochs,
                    validation_data=gen_valid, validation_steps=steps_per_epoch_valid)

# 次にくる単語を選ぶ関数
def sample(preds, temperature=1.0):
    preds = np.log(preds) / temperature
    preds = np.exp(preds) / np.sum(np.exp(preds))
    choices = range(len(preds))
    return np.random.choice(choices, p=preds)

# ランダムに文章を生成する関数
def sample_sentences(num_sentences, sample_sent_len = 20):
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
words = ["3",
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
        print('====', word)
        print_closest_words(word)