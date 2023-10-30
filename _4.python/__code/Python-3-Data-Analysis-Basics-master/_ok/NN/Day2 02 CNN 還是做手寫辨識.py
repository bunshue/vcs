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



print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)

#(60000, 28, 28)

#Channel

#CNN 要注意一張圖有多少個 channel, 開始我們因為只有灰階, 所以只有一個 channel。因此我們要轉一下我們的資料格式:

#(28,28) --> (28, 28, 1)

x_train = x_train.reshape(60000, 28, 28, 1) / 255
x_test = x_test.reshape(10000, 28, 28, 1) / 255

print(x_train[87].shape)

#(28, 28, 1)

print(y_train[87])

#9

from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

#讀入必要的函式
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import SGD

#Step 1 打造函數學習機 (CNN)

model = Sequential()
model.add(Conv2D(16, (3,3), padding='same',
                input_shape=(28,28,1),
                activation='relu'))

# 輸出 16 個 28x28 矩陣
# 事實上是 (28, 28, 16)

model.add(MaxPooling2D(pool_size=(2,2)))
# (14,14,16)

model.add(Conv2D(32, (3,3), padding='same',
                activation='relu'))
# output (14, 14, 32)

model.add(MaxPooling2D(pool_size=(2,2)))
# output (7, 7, 32)

model.add(Conv2D(64, (3,3), padding='same',
                activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(54, activation='relu'))
model.add(Dense(10, activation='softmax'))

#看一下我們的神經網路
model.summary()

# 3*3 (權重) + 1 (bias)
#(3*3+1)*16 = 160

#(3*3*16+1)*32 = 4640

model.compile(loss='mse', optimizer=SGD(lr=0.087),
             metrics=['accuracy'])

#Step 2. fit

model.fit(x_train, y_train, batch_size=128, epochs=12)

#Step 3. 預測

result = model.predict_classes(x_test)

def my_predict(n):
    print('我可愛的 CNN 預測是', result[n])
    X = x_test[n].reshape(28,28)
    plt.imshow(X, cmap='Greys')

print(my_predict(50))

score = model.evaluate(x_test, y_test)

loss, acc = score

print('測試資料的正確率為', acc)

#把我們的 model 存起來
model.save('myCNNmodel.h5')


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

