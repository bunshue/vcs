"""



"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#tensorflow_version

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

#(x_train, y_train), (x_test, y_test) = mnist.load_data() 改成以下6行
path = 'C:/_git/vcs/_4.python/ml/mnist.npz'
mnist = np.load(path)  
x_train, y_train = mnist['x_train'], mnist['y_train']  
x_test, y_test = mnist['x_test'], mnist['y_test']  
mnist.close()  

print(len(x_train))

print(len(x_test))

n = 1234

print(x_train[n])

plt.imshow(x_train[n], cmap='Greys')

print(x_train[n].shape)

#(28, 28)

print(y_train[n])

#3

#np.array([43, 3, 12, 44])/44
#array([0.97727273, 0.06818182, 0.27272727, 1.        ])

x_train = x_train.reshape(60000, 784) / 255
x_test = x_test.reshape(10000, 784) / 255

from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

print(y_train[n])

#array([0., 0., 0., 1., 0., 0., 0., 0., 0., 0.], dtype=float32)

#3 層 100 100 100
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

#step01. 打造函數學習機
model = Sequential()
model.add(Dense(100, input_dim=784, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss='mse', optimizer=SGD(lr=0.087), metrics=['accuracy'])
model.summary()

#Step02. fit

#model.fit(x_train, y_train, batch_size=100, epochs=10)
model.fit(x_train, y_train, batch_size=1000, epochs=10)

# step03. predict
y_pred = model.predict_classes(x_test)

print(y_pred)

n = 5566

print('神經網路預測', y_pred[n])

plt.imshow(x_test[n].reshape(28,28), cmap='Greys')

#神經網路預測 1



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

