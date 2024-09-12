"""
Day 40


"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#要先对数据集中的图片进行处理，可能需要进行的任务有图像尺寸统一、颜色处理等

import os
import cv2
from tqdm import tqdm

# 数据集的路径
DATADIR = 'C:/_git/vcs/_big_files/kagglecatsanddogs_5340_1000/PetImages/'
DATADIR = 'C:/_git/vcs/_big_files/kagglecatsanddogs_5340_800/PetImages/'

CATEGORIES = ["Dog", "Cat"]

for category in CATEGORIES: 
    path = os.path.join(DATADIR,category)  # 创建路径
    for img in os.listdir(path):  # 迭代遍历每个图片
        img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # 转化成array
        plt.imshow(img_array, cmap='gray')  # 转换成图像展示
        plt.show()  # display!

        break  # 我们作为演示只展示一张，所以直接break了
    break  #同上





#看下array中存储的图像数据：
#print(img_array)

print('看下array的形状')
print(img_array.shape)

#我们可以看到这是一张很大的图片，并且拥有RGB3个通道，这并不是我们想要的，所以接下来我们将要进行的操作会使图像变小，并且只剩下灰度：

print('resize')
IMG_SIZE = 100

new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
plt.imshow(new_array, cmap='gray')
plt.show()

#接下来，我们将要创建所有这些培训数据，但是，首先，我们应该留出一些图像进行最终测试。我将手动创建一个名为Testing的目录，然后在其中创建2个目录，一个用于Dog，一个用于Cat。从这里开始，我将把Dog和Cat的前15张图像移到训练版本中。确保移动它们，而不是复制。我们将使用它进行最终测试。

print('訓練資料')
training_data = []

def create_training_data():
    for category in CATEGORIES:  

        path = os.path.join(DATADIR,category)  
        class_num = CATEGORIES.index(category)  # 得到分类，其中 0=dog 1=cat

        for img in tqdm(os.listdir(path)):  
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # 大小转换
                training_data.append([new_array, class_num])  # 加入训练数据中
            except Exception as e:  # 为了保证输出是整洁的
                pass
            #except OSError as e:
            #    print("OSErrroBad img most likely", e, os.path.join(path,img))
            #except Exception as e:
            #    print("general exception", e, os.path.join(path,img))

create_training_data()

print(len(training_data))

#我们有大约25,000张图片。
#我们要做的一件事是确保我们的数据是平衡的。在这个数据集的情况下，我可以看到数据集开始时是平衡的。平衡，我的意思是每个班级都有相同数量的例子（相同数量的狗和猫）。如果不平衡，您要么将类权重传递给模型，以便它可以适当地测量误差，或者通过将较大的集修剪为与较小集相同的大小来平衡样本。
#现在数据集中要么全是dog要么全是cat，因此接下来要引入随机：

import random
random.shuffle(training_data)

#我们的training_data是一个列表，这意味着它是可变的，所以它现在很好地改组了。我们可以通过迭代几个初始样本并打印出类来确认这一点：

for sample in training_data[:10]:
    print(sample[1])

#现在可以看到已经是0、1交替了，我们可以开始我们的模型了：

X = []
y = []

for features,label in training_data:
    X.append(features)
    y.append(label)

print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

#让我们保存这些数据，这样我们就不需要每次想要使用神经网络模型时继续计算它：

import pickle

pickle_out = open("tmp_X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("tmp_y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()
# We can always load it in to our current script, or a totally new one by doing:

pickle_in = open("tmp_X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle","rb")
y = pickle.load(pickle_in)

#现在我们已经拿出了数据集，我们已经准备好覆盖卷积神经网络，并用我们的数据进行分类。
#以上就是这次的关于数据集操作的全部任务。

"""

基础知识

基本的CNN结构如下： Convolution(卷积) -> Pooling(池化) -> Convolution -> Pooling -> Fully Connected Layer(全连接层) -> Output

Convolution（卷积）是获取原始数据并从中创建特征映射的行为。Pooling(池化)是下采样，通常以“max-pooling”的形式，我们选择一个区域，然后在该区域中取最大值，这将成为整个区域的新值。Fully Connected Layers(全连接层)是典型的神经网络，其中所有节点都“完全连接”。卷积层不像传统的神经网络那样完全连接。

卷积：我们将采用某个窗口，并在该窗口中查找要素,该窗口的功能现在只是新功能图中的一个像素大小的功能，但实际上我们将有多层功能图。接下来，我们将该窗口滑过并继续该过程,继续此过程，直到覆盖整个图像。

池化：最常见的池化形式是“最大池化”，其中我们简单地获取窗口中的最大值，并且该值成为该区域的新值。

全连接层：每个卷积和池化步骤都是隐藏层。在此之后，我们有一个完全连接的层，然后是输出层。完全连接的层是典型的神经网络（多层感知器）类型的层，与输出层相同。
注意

本次代码中所需的X.pickle和y.pickle为上一篇的输出，路径请根据自己的情况更改！
"""


import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D

import pickle

pickle_in = open("tmp_X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle","rb")
y = pickle.load(pickle_in)

X = X/255.0

model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors

model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(X, y, batch_size=32, epochs=3, validation_split=0.3)



"""
在仅仅三个epoches之后，我们的验证准确率为71％。如果我们继续进行更多的epoches，我们可能会做得更好，但我们应该讨论我们如何知道我们如何做。为了解决这个问题，我们可以使用TensorFlow附带的TensorBoard，它可以帮助您在训练模型时可视化模型。

我们将在下一个教程中讨论TensorBoard以及对我们模型的各种调整！



"""


#这是Python，TensorFlow和Keras教程系列的深度学习基础知识的第4部分。

#在这一部分，我们将讨论的是TensorBoard。TensorBoard是一个方便的应用程序，允许您在浏览器中查看模型或模型的各个方面。我们将TensorBoard与Keras一起使用的方式是通过Keras回调。实际上有很多Keras回调，你可以自己制作。

from tensorflow.keras.callbacks import TensorBoard

#Using TensorFlow backend.

#创建TensorBoard回调对象
NAME = "Cats-vs-dogs-CNN"

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

"""
最终，你会希望获得更多的自定义NAME，但现在这样做。因此，这将保存模型的训练数据logs/NAME，然后由TensorBoard读取。

最后，我们可以通过将它添加到.fit方法中来将此回调添加到我们的模型中，例如：

model.fit(X, y,
          batch_size=32,
          epochs=3,
          validation_split=0.3,
          callbacks=[tensorboard])

请注意，这callbacks是一个列表。您也可以将其他回调传递到此列表中。我们的模型还没有定义，所以现在让我们把它们放在一起：
"""
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
# more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.
import pickle
import time

NAME = "Cats-vs-dogs-CNN"

pickle_in = open("tmp_X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle","rb")
y = pickle.load(pickle_in)

X = X/255.0

model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'],
              )

model.fit(X, y,
          batch_size=32,
          epochs=3,
          validation_split=0.3,
          callbacks=[tensorboard])


"""
运行此之后，您应该有一个名为的新目录logs。我们现在可以使用tensorboard从这个目录中可视化初始结果。打开控制台，切换到工作目录，然后键入：tensorboard --logdir=logs/。您应该看到一个通知：TensorBoard 1.10.0 at http://H-PC:6006 (Press CTRL+C to quit)“h-pc”是您机器的名称。打开浏览器并前往此地址。你应该看到类似的东西：



"""

#现在我们可以看到我们的模型随着时间的推移。让我们改变模型中的一些东西。首先，我们从未在密集层中添加激活。另外，让我们尝试整体较小的模型：

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
# more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.
import pickle
import time

NAME = "Cats-vs-dogs-64x2-CNN"

pickle_in = open("tmp_X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle","rb")
y = pickle.load(pickle_in)

X = X/255.0

model = Sequential()

model.add(Conv2D(64, (3, 3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation('relu'))

model.add(Dense(1))
model.add(Activation('sigmoid'))

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'],
              )

model.fit(X, y,
          batch_size=32,
          epochs=10,
          validation_split=0.3,
          callbacks=[tensorboard])

#除此之外，我还改名为NAME = "Cats-vs-dogs-64x2-CNN"。不要忘记这样做，否则你会偶然附加到你以前的型号的日志，它看起来不太好。我们现在检查TensorBoard：

"""

看起来更好！但是，您可能会立即注意到验证丢失的形状。损失是衡量错误的标准，看起来很明显，在我们的第四个时代之后，事情开始变得糟糕。

有趣的是，我们的验证准确性仍然持续，但我想它最终会开始下降。更可能的是，第一件遭受的事情确实是你的验证损失。这应该提醒你，你几乎肯定会开始过度适应。这种情况发生的原因是该模型不断尝试减少样本损失。

在某些时候，模型不是学习关于实际数据的一般事物，而是开始只记忆输入数据。如果你继续这样做，是的，样本中的“准确性”会上升，但你的样本，以及你试图为模型提供的任何新数据可能会表现得很差。
"""
