"""



"""

mnist_npz_filename = "C:/_git/vcs/_big_files/mnist.npz"

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from keras.datasets import mnist
from keras.models import Sequential 
from keras.layers.core import Dense, Activation
#from keras.utils import np_utils old 改如下
from tensorflow.python.keras.utils import np_utils

#(X_train, Y_train), (X_test, Y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
X_train, Y_train = mnist['x_train'], mnist['y_train']  
X_test, Y_test = mnist['x_test'], mnist['y_test']  
mnist.close()  

X_train = X_train.reshape(60000, 784)     
X_test = X_test.reshape(10000, 784)

classes = 10
Y_train = np_utils.to_categorical(Y_train, classes)     
Y_test = np_utils.to_categorical(Y_test, classes)

input_size = 784
batch_size = 100     
hidden_neurons = 100     
epochs = 30

model = Sequential()     
model.add(Dense(hidden_neurons, input_dim=input_size)) 
model.add(Activation('sigmoid'))     
model.add(Dense(classes, input_dim=hidden_neurons)) 
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='sgd')

model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs, verbose=1)

score = model.evaluate(X_test, Y_test, verbose=1)
print('Test accuracy:', score[1]) 


weights = model.layers[0].get_weights()

import matplotlib.pyplot as plt     
import matplotlib.cm as cm 
import numpy

fig = plt.figure()
  
w = weights[0].T          
for neuron in range(hidden_neurons):         
    ax = fig.add_subplot(10, 10, neuron+1)
    ax.axis("off")
    ax.imshow(numpy.reshape(w[neuron], (28, 28)), cmap = cm.Greys_r)

plt.savefig("neuron_images.png", dpi=300)    
plt.show()  
