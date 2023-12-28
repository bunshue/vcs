import sys

import pandas as pd

print('------------------------------------------------------------')	#60個

"""
手動下載
https://storage.googleapis.com/tensorflow/keras-applications/resnet/resnet50_weights_tf_dim_ordering_tf_kernels.h5
https://storage.googleapis.com/tensorflow/keras-applications/resnet/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5
https://storage.googleapis.com/tensorflow/keras-applications/inception_v3/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5
https://storage.googleapis.com/tensorflow/keras-applications/xception/xception_weights_tf_dim_ordering_tf_kernels_notop.h5
放在
~/.keras/models/
或
C:/Users/070601/.keras/models/
之下
"""

'''
#from keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import ResNet50
#from keras.preprocessing import image
from keras.utils import image_utils

#from keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

model = ResNet50(weights='imagenet') 
print(model.summary()) # 顯示模型基本信息

img_path = 'elephant.jpg' 
#img = image.load_img(img_path, target_size=(224, 224))
img = image_utils.load_img(img_path, target_size=(224, 224))
#x = image.img_to_array(img)
x = image_utils.img_to_array(img)
x = np.expand_dims(x, axis=0) 
x = preprocess_input(x) 

preds = model.predict(x) 
print('Predicted:', decode_predictions(preds, top=3)[0])

print('------------------------------------------------------------')	#60個

"""
使用keras下載訓練好的模型（下載每個模型幾十分鐘）, 並用模型對提取圖片的特徵。
訓練集25000張圖式片， 測試集12500張圖片，用三個模型, 如果不使用GPU，約8小時以上。
本例中只使用了幾百張圖片, 花十幾分鍾跑一遍整體流程。 想訓練所有， 只需增加圖片數據即可。
"""

from keras.models import *
from keras.layers import *
from keras.applications import *
from keras.preprocessing.image import *
import h5py
import warnings

warnings.filterwarnings('ignore')

def get_features(MODEL, width, height, lambda_func=None):
    input_tensor = Input((height, width, 3))
    x = input_tensor
    if lambda_func:
        x = Lambda(lambda_func)(x)

    base_model = MODEL(input_tensor=x, weights='imagenet', include_top=False)
    model = Model(base_model.input, GlobalAveragePooling2D()(base_model.output))

    gen = ImageDataGenerator()
    # 注意 train 和 test 是圖片存儲路徑
    train_generator = gen.flow_from_directory("train", (width, height), shuffle=False,
                                              batch_size=16)
    test_generator = gen.flow_from_directory("test", (width, height), shuffle=False,
                                             batch_size=16, class_mode=None)
    # 不同的keras版本變量名略有不同，如: train_generator.samples train_generator.samples...
    train = model.predict_generator(train_generator, train_generator.samples)
    test = model.predict_generator(test_generator, test_generator.samples)

    """ some error
    with h5py.File("data_%s.h5"%MODEL.func_name) as h:
        h.create_dataset("train", data=train)
        h.create_dataset("test", data=test)
        h.create_dataset("label", data=train_generator.classes)
    """

get_features(ResNet50, 224, 224)
get_features(InceptionV3, 299, 299, inception_v3.preprocess_input)
get_features(Xception, 299, 299, xception.preprocess_input)


print('------------------------------------------------------------')	#60個


# 訓練模型並預測，此處使用了深度學習模型，也可以換成機器學習模型

import h5py
import numpy as np
from sklearn.utils import shuffle
from keras.models import *
from keras.layers import *

np.random.seed(12345678)
X_train = []
X_test = []

"""
for filename in ["data_ResNet50.h5", "data_Xception.h5", "data_InceptionV3.h5"]:
    with h5py.File(filename, 'r') as h:
        X_train.append(np.array(h['train']))
        X_test.append(np.array(h['test']))
        y_train = np.array(h['label'])

X_train = np.concatenate(X_train, axis=1)
X_test = np.concatenate(X_test, axis=1)
X_train, y_train = shuffle(X_train, y_train)

input_tensor = Input(X_train.shape[1:])
x = Dropout(0.5)(input_tensor)
x = Dense(1, activation='sigmoid')(x)
model = Model(input_tensor, x)

model.compile(optimizer='adadelta',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, batch_size=128, nb_epoch=8, validation_split=0.2)
y_pred = model.predict(X_test, verbose=1)
y_pred = y_pred.clip(min=0.005, max=0.995)

print('------------------------------------------------------------')	#60個

# 用迭代訓練過程中的錯誤率做圖

import matplotlib.pyplot as plt

def plot_training(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    epochs = range(len(acc))
    plt.plot(epochs, acc, 'b')
    plt.plot(epochs, val_acc, 'r')
    plt.legend(["acc", "val_acc"], loc='best')
    plt.title('Training and validation accuracy')
    plt.show()
    loss = history.history['loss']
    val_loss = history.history['val_loss']   
    plt.plot(epochs, loss, 'b')
    plt.plot(epochs, val_loss, 'r')
    plt.legend(["loss", "val_loss"], loc='best')
    plt.title('Training and validation loss')
    plt.show()

plot_training(history)
"""

'''

print('------------------------------------------------------------')	#60個

'''
# should be the same
print('提取特徵')

from keras.models import *
from keras.layers import *
from keras.applications import *
from keras.preprocessing.image import *
import h5py
import warnings

warnings.filterwarnings('ignore')

def get_features(MODEL, width, height, lambda_func=None):
    input_tensor = Input((height, width, 3))
    x = input_tensor
    if lambda_func:
        x = Lambda(lambda_func)(x)

    base_model = MODEL(input_tensor=x, weights='imagenet', include_top=False)
    model = Model(base_model.input, GlobalAveragePooling2D()(base_model.output))

    gen = ImageDataGenerator()
    # 注意 train 和 test 是圖片存儲路徑
    train_generator = gen.flow_from_directory("train", (width, height), shuffle=False, batch_size=16)
    test_generator = gen.flow_from_directory("test", (width, height), shuffle=False,
                                             batch_size=16, class_mode=None)
    train = model.predict_generator(train_generator, train_generator.samples)
    test = model.predict_generator(test_generator, test_generator.samples)
    """ maybe the same
    with h5py.File("data_%s.h5"%MODEL.func_name) as h:
        h.create_dataset("train", data=train)
        h.create_dataset("test", data=test)
        h.create_dataset("label", data=train_generator.classes)
    """

get_features(ResNet50, 224, 224)
get_features(InceptionV3, 299, 299, inception_v3.preprocess_input)
get_features(Xception, 299, 299, xception.preprocess_input)


print('------------------------------------------------------------')	#60個

#訓練模型和預測

import h5py
import numpy as np
from sklearn.utils import shuffle
from keras.models import *
from keras.layers import *

np.random.seed(12345678)
X_train = []
X_test = []

for filename in ["data_ResNet50.h5", "data_Xception.h5", "data_InceptionV3.h5"]:
    with h5py.File(filename, 'r') as h:
        X_train.append(np.array(h['train']))
        X_test.append(np.array(h['test']))
        y_train = np.array(h['label'])

X_train = np.concatenate(X_train, axis=1)
X_test = np.concatenate(X_test, axis=1)
X_train, y_train = shuffle(X_train, y_train)

input_tensor = Input(X_train.shape[1:])
x = Dropout(0.5)(input_tensor)
x = Dense(1, activation='sigmoid')(x)
model = Model(input_tensor, x)

model.compile(optimizer='adadelta',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, batch_size=128, nb_epoch=8, validation_split=0.2)
y_pred = model.predict(X_test, verbose=1)
y_pred = y_pred.clip(min=0.005, max=0.995)

print('------------------------------------------------------------')	#60個

#訓練結果分析

import matplotlib.pyplot as plt

def plot_training(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    epochs = range(len(acc))
    plt.plot(epochs, acc, 'b')
    plt.plot(epochs, val_acc, 'r')
    plt.legend(["acc", "val_acc"], loc='best')
    plt.title('Training and validation accuracy')
    plt.show()
    
loss = history.history['loss']
val_loss = history.history['val_loss']   
plt.plot(epochs, loss, 'b')
plt.plot(epochs, val_loss, 'r')
plt.legend(["loss", "val_loss"], loc='best')
plt.title('Training and validation loss')
plt.show()

plot_training(history)
'''

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



