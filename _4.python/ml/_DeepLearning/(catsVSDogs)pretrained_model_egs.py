"""
(catsVSDogs)pretrained_model_egs

https://github.com/beetrandahiya/Cats-VS-Dogs/blob/master/(catsVSDogs)pretrained_model_egs.ipynb

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

import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from tensorflow.keras.utils import to_categorical  # One-Hot Encoding

from matplotlib.colors import ListedColormap

from sklearn import tree

import warnings

warnings.filterwarnings("ignore")


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import tensorflow as tf

keras = tf.keras

import tensorflow_datasets as tfds

tfds.disable_progress_bar()

(raw_train, raw_validation, raw_test), metadata = tfds.load(
    "cats_vs_dogs",
    split=["train[:80%]", "train[80%:90%]", "train[90%:]"],
    with_info=True,
    as_supervised=True,
)


get_label_name = metadata.features["label"].int2str

for image, label in raw_train.take(5):
    plt.figure()
    plt.imshow(image)
    plt.title(get_label_name(label))
    print("取得動物 :", get_label_name(label))


IMG_SIZE = 160


def format_example(image, label):
    image = tf.cast(image, tf.float32)
    image = (image / 127.5) - 1
    image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
    return image, label


train = raw_train.map(format_example)
validation = raw_validation.map(format_example)
test = raw_test.map(format_example)

for image, label in train.take(5):
    plt.figure()
    plt.imshow(image)
    plt.title(get_label_name(label))
    print("取得動物 :", get_label_name(label))


BATCH_SIZE = 32
SHUFFLE_BUFFER_SIZE = 1000
train_batches = train.shuffle(SHUFFLE_BUFFER_SIZE).batch(BATCH_SIZE)
validation_batches = validation.batch(BATCH_SIZE)
test_batches = test.batch(BATCH_SIZE)

IMG_SHAPE = (IMG_SIZE, IMG_SIZE, 3)

base_model = tf.keras.applications.MobileNetV2(
    input_shape=IMG_SHAPE, include_top=False, weights="imagenet"
)

# base_model.summary()

base_model.trainable = False

# base_model.summary()

global_avg_layer = tf.keras.layers.GlobalAveragePooling2D()
pred_layer = keras.layers.Dense(1)

model = tf.keras.Sequential([base_model, global_avg_layer, pred_layer])

# model.summary()

base_learn_rate = 0.0001

model.compile(
    optimizer=tf.keras.optimizers.RMSprop(learning_rate=base_learn_rate),
    loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
    metrics=["accuracy"],
)


history = model.fit(train_batches, epochs=1, validation_data=validation_batches)

model.save("tmp_dogs_vs_cats.h5")

predictions = model.predict(test_batches)

i = 0
for image, label in test.take(6):
    print(i)
    plt.figure()
    plt.imshow(image)
    if predictions[i] > 0:
        plt.title("預測 : 狗")
    elif predictions[i] < 0:
        plt.title("預測 : 貓")
    i += 1

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
