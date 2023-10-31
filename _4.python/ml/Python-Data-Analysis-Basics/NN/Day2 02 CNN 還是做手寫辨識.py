"""

CNN 還是手寫辨識

Yann LeCun 被譽為 Deep Learning 的三巨頭之一。
他的 CNN (Convolutional Neural Networks) 是讓 Neural Network 重新受到重視的主因之一。


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
'''

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
'''

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


"""
2-1 初始準備

基本上和之前是一樣的, 我們就不再說明。

2-2 讀入 MNIST 數據庫
由 Keras 讀入 MNIST

基本上和我們上次一樣, 這次因為 Keras 已偷偷把數據庫存在你的電腦, 所以會快很多!
"""

import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

"""
輸入格式整理

如果你還記得, 我們每筆輸入資料都是 28x28 的陣列, CNN 其實就是吃「圖」的, 所以基本上不用像之前把每筆資料拉平。「但。是。」平常的圖都有 R, G, B 三個 channels, 每個 channel 都是一個矩陣, 也就是一張圖可能是三個矩陣! 我們是灰階, 也就是只有一個 channel。但這件事也要明確的告訴 Keras。

換句話說, 我們的輸入每筆資料型式要從 (28, 28) 換成 (28, 28, 1)!
"""

print(x_train[1234].shape)

#(28, 28)

# CNN 要的是 (28, 28, 1)

#確認一下...

x_train = x_train.reshape(60000, 28, 28, 1)/255
x_test = x_test.reshape(10000, 28, 28, 1)/255

#原來 28x28 矩陣...

print(x_train[1234].shape)

#(28, 28, 1)

X = x_train[1234]
X = X.reshape(28, 28)
plt.imshow(X,  cmap='Greys')

"""
輸出格式整理

和上次一樣, 我們用標準 1-hot 方式處理。
"""

print(y_train[1234])

#3

from keras.utils import np_utils
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

print(y_train[1234])

#array([0., 0., 0., 1., 0., 0., 0., 0., 0., 0.], dtype=float32)

#x_train = x_train/255
#x_test = x_test/255

"""
2-3 打造你的 CNN
決定神經網路架構、讀入相關套件

CNN 我們一樣要決定用幾層的 CNN, 然後是不是每次都要做 max-pooling。再來就是拉平、送入標準神經網路 (再度要決定幾層、幾個神經元)。

我們上課的時候, 同學建議要做 3 次的 convolution + max-pooling, filter 大小都是 5×5

    做 3 次 convolution, 每次都接 max-pooling
    filter 大小都是 3x3, max-pooling 都用 2x2 為一小區塊

CNN 一個小技巧是每層的 filters 數目是越來越多, 上課同學建議第一層 4 個, 因為要做三次, 所以我們 filters 數分別是 10, 20, 40。做完 convolution 之後, 我們要拉平、再送入一個標準的神經網路。這個神經網路設計是這樣:

    只有 3 個隱藏層, 使用 :

    layer 1: 5
    layer 2: 8
    layer 3: 20

"""

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.layers import Conv2D, MaxPool2D
from keras.optimizers import SGD

"""
建構我們的神經網路
一開始一樣是打開個空白的神經網路。
"""

model = Sequential()

#第一個隱藏層一樣要告訴 Keras 我們輸入長什麼樣子。padding 設成 same 是每個 filter 會輸出原來 28x28 一樣大小的矩陣。

model.add(Conv2D(10, (3, 3), padding='same', input_shape=(28, 28, 1),
                activation='relu'))

#Max-Pooling!

model.add(MaxPool2D(pool_size=(2,2)))

#第二次 Convolution!

model.add(Conv2D(20, (3, 3), padding='same',
                activation='relu'))

#再 Max-Pooling!

model.add(MaxPool2D(pool_size=(2,2)))

#第三次 Convolution!

model.add(Conv2D(40, (3, 3), padding='same',
                activation='relu'))

#Max-Pooling 最終回。

model.add(MaxPool2D(pool_size=(2,2)))

#然後我們要送進一般的神經網路了。記得這是要拉平的, 還在 Keras 會幫我們做!

model.add(Flatten())
model.add(Dense(5, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(20, activation='relu'))

#輸出和上次一樣!
model.add(Dense(10, activation='softmax'))

#組裝
#和之前比較不一樣的是我們還要做 compile 才正式把我們的神經網路建好。

#model.compile(loss="categorical_crossentropy",
#              optimizer=Adadelta(),
#              metrics=['accuracy'])

model.compile(loss='mse', optimizer=SGD(lr=0.07), metrics=['accuracy'])

#檢視我們的神經網路
model.summary()

#1-4 訓練
model.fit(x_train, y_train, batch_size=100, epochs=10)

#這裡因為第一次訓練有點遜 (CNN 標準), 所以我再執行 fit 一次, 因此實際上是訓練了 20 次。

"""
2-5 結果測試
分數

我們來看測試資料 (我們的 CNN 沒看過的)
"""

score = model.evaluate(x_test, y_test)

#我們來看成績, 順便用 Python 3.6 開始的 f-string format 方式。
print(f'測試資料的 loss: {score[0]:.5f}')
print(f'測試資料的正確率: {score[1]}')

#測試資料的 loss: 0.02530
#測試資料的正確率: 0.8328999876976013

#儲存結果
#結果看來還不差, 所以我們把結果存起來。上次我們介紹分別存架構和權重的方法, 這次我們看看怎麼樣一次就存入權重 + 結構!

model.save('myCNNmodel.h5')

#欣賞一下成果
#我們示範一下怎麼讀回我們的神經網路。你會發現讀回來之後就可以直接使用了!!

del model
#先把我們原來的 model 刪掉, 保證接下來的是讀進來的。我們要用一個 load_model 的函式。

from keras.models import load_model
model = load_model('myCNNmodel.h5')

#我們用另一個方式: 每次選 5 個顯示, 看是不是有正確辨識。

predict = model.predict_classes(x_test)

#看來真的可以直接用!!
pick = np.random.randint(1, 9999, 5)

for i in range(5):
    plt.subplot(1, 5,i + 1)
    plt.imshow(x_test[pick[i]].reshape(28, 28), cmap = 'Greys')
    plt.title(predict[pick[i]])
    plt.axis("off")

"""
小結論
我們到此, 基本上是「亂做」的神經網路。有些同學在不斷試驗的過程中, 可能會發現有時會出現很糟糕的結果。因此, 接下來我們要介紹怎麼樣用些簡單的手法, 能讓學習效果比較穩定, 而且有可能可以增加學習效率。
"""




