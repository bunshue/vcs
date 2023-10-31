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

import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist

#(x_train, y_train), (x_test, y_test) = mnist.load_data() 改成以下6行
path = 'C:/_git/vcs/_4.python/ml/mnist.npz'
mnist = np.load(path)  
x_train, y_train = mnist['x_train'], mnist['y_train']  
x_test, y_test = mnist['x_test'], mnist['y_test']  
mnist.close()  

x_train = x_train / 255
x_test = x_test / 255

from keras.utils import np_utils
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizers import SGD

model = Sequential()
model.add(Flatten(input_shape = (28, 28)))
model.add(Dense(20, activation = 'relu'))
model.add(Dense(80, activation = 'relu'))
model.add(Dense(100, activation = 'relu'))
model.add(Dense(160, activation = 'relu'))
model.add(Dense(10, activation = 'softmax'))
model.compile(loss = 'mse', optimizer = SGD(learning_rate = 0.087), metrics = ['accuracy'])

#model.fit(x_train, y_train, batch_size = 100, epochs = 20)
model.fit(x_train, y_train, batch_size = 2000, epochs = 1)

print(y_train[33])

#array([0., 0., 0., 0., 0., 0., 0., 0., 0., 1.], dtype = float32)

print(y_test[2])

#array([0., 1., 0., 0., 0., 0., 0., 0., 0., 0.], dtype = float32)

#Step 3 預測

print(model.predict(np.array([x_test[87]])))
#print(model.predict_classes(np.array([x_test[87]])))
#array([3])

#predict = model.predict_classes(x_test)
predict = model.predict_step(x_test)

print(predict)

#array([7, 2, 1, ..., 4, 5, 6])

def test(測試編號):
    plt.imshow(x_test[測試編號], cmap = 'Greys')
    print('神經網路判斷為:', predict[測試編號])

test(1287)

#神經網路判斷為: 8

score = model.evaluate(x_test, y_test)

print('loss:', score[0])

print('正確率', score[1])

#loss: 0.01081830496697512

#正確率 0.9308000206947327



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

