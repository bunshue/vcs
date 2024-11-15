"""

CNN 還是手寫辨識

Yann LeCun 被譽為 Deep Learning 的三巨頭之一。
他的 CNN (Convolutional Neural Networks) 是讓 Neural Network 重新受到重視的主因之一。


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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
"""
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

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

print("檢視神經網路")
model.summary()  #檢視神經網路

# 3*3 (權重) + 1 (bias)
#(3*3+1)*16 = 160

#(3*3*16+1)*32 = 4640

model.compile(loss='mse', optimizer=SGD(lr=0.087),
             metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=128, epochs=12)  # 學習訓練.fit

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
"""

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


"""
2-1 初始準備

基本上和之前是一樣的, 我們就不再說明。

2-2 讀入 MNIST 數據庫
由 Keras 讀入 MNIST

基本上和我們上次一樣, 這次因為 Keras 已偷偷把數據庫存在你的電腦, 所以會快很多!
"""

from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

"""
輸入格式整理

如果你還記得, 我們每筆輸入資料都是 28x28 的陣列, CNN 其實就是吃「圖」的, 所以基本上不用像之前把每筆資料拉平。「但。是。」平常的圖都有 R, G, B 三個 channels, 每個 channel 都是一個矩陣, 也就是一張圖可能是三個矩陣! 我們是灰階, 也就是只有一個 channel。但這件事也要明確的告訴 Keras。

換句話說, 我們的輸入每筆資料型式要從 (28, 28) 換成 (28, 28, 1)!
"""

print(x_train[1234].shape)

# (28, 28)

# CNN 要的是 (28, 28, 1)

# 確認一下...

x_train = x_train.reshape(60000, 28, 28, 1) / 255
x_test = x_test.reshape(10000, 28, 28, 1) / 255

# 原來 28x28 矩陣...

print(x_train[1234].shape)

# (28, 28, 1)

X = x_train[1234]
X = X.reshape(28, 28)
plt.imshow(X, cmap="Greys")

"""
輸出格式整理

和上次一樣, 我們用標準 1-hot 方式處理。
"""

print(y_train[1234])
# 3

from tensorflow.python.keras.utils import np_utils

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

print(y_train[1234])

# array([0., 0., 0., 1., 0., 0., 0., 0., 0., 0.], dtype=float32)

# x_train = x_train/255
# x_test = x_test/255

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

# 第一個隱藏層一樣要告訴 Keras 我們輸入長什麼樣子。padding 設成 same 是每個 filter 會輸出原來 28x28 一樣大小的矩陣。

model.add(
    Conv2D(10, (3, 3), padding="same", input_shape=(28, 28, 1), activation="relu")
)

# Max-Pooling!

model.add(MaxPool2D(pool_size=(2, 2)))

# 第二次 Convolution!

model.add(Conv2D(20, (3, 3), padding="same", activation="relu"))

# 再 Max-Pooling!

model.add(MaxPool2D(pool_size=(2, 2)))

# 第三次 Convolution!

model.add(Conv2D(40, (3, 3), padding="same", activation="relu"))

# Max-Pooling 最終回。

model.add(MaxPool2D(pool_size=(2, 2)))

# 然後我們要送進一般的神經網路了。記得這是要拉平的, 還在 Keras 會幫我們做!

model.add(Flatten())
model.add(Dense(5, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(20, activation="relu"))

# 輸出和上次一樣!
model.add(Dense(10, activation="softmax"))

# 組裝
# 和之前比較不一樣的是我們還要做 compile 才正式把我們的神經網路建好。

# model.compile(loss="categorical_crossentropy",
#              optimizer=Adadelta(),
#              metrics=['accuracy'])

model.compile(loss="mse", optimizer=SGD(lr=0.07), metrics=["accuracy"])

print("檢視神經網路")
model.summary()  # 檢視神經網路

model.fit(x_train, y_train, batch_size=100, epochs=10)  # 學習訓練.fit

# 這裡因為第一次訓練有點遜 (CNN 標準), 所以我再執行 fit 一次, 因此實際上是訓練了 20 次。

"""
2-5 結果測試
分數

我們來看測試資料 (我們的 CNN 沒看過的)
"""

score = model.evaluate(x_test, y_test)

# 我們來看成績, 順便用 Python 3.6 開始的 f-string format 方式。
print(f"測試資料的 loss: {score[0]:.5f}")
print(f"測試資料的正確率: {score[1]}")

# 測試資料的 loss: 0.02530
# 測試資料的正確率: 0.8328999876976013

# 儲存結果
# 結果看來還不差, 所以我們把結果存起來。上次我們介紹分別存架構和權重的方法, 這次我們看看怎麼樣一次就存入權重 + 結構!

model.save("myCNNmodel.h5")

# 欣賞一下成果
# 我們示範一下怎麼讀回我們的神經網路。你會發現讀回來之後就可以直接使用了!!

del model
# 先把我們原來的 model 刪掉, 保證接下來的是讀進來的。我們要用一個 load_model 的函式。

from keras.models import load_model

model = load_model("myCNNmodel.h5")

# 我們用另一個方式: 每次選 5 個顯示, 看是不是有正確辨識。

predict = model.predict_classes(x_test)

# 看來真的可以直接用!!
pick = np.random.randint(1, 9999, 5)

for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(x_test[pick[i]].reshape(28, 28), cmap="Greys")
    plt.title(predict[pick[i]])
    plt.axis("off")

"""
小結論
我們到此, 基本上是「亂做」的神經網路。有些同學在不斷試驗的過程中, 可能會發現有時會出現很糟糕的結果。因此, 接下來我們要介紹怎麼樣用些簡單的手法, 能讓學習效果比較穩定, 而且有可能可以增加學習效率。
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 把訓練好神經網路讀回來用的方式

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from tensorflow.keras.models import load_model

model = load_model("myCNNmodel.h5")

from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_test = x_test.reshape(10000, 28, 28, 1) / 255

result = model.predict_classes(x_test)


def myCNN(n):
    print("我的 CNN 說是", result[n])
    X = x_test[n].reshape(28, 28)
    plt.imshow(X, cmap="Greys")


n = 999

myCNN(n)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
import glob, cv2


def show_images_labels_predictions(images, labels, predictions, start_id, num=10):
    plt.gcf().set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, i + 1)
        ax.imshow(images[start_id], cmap="binary")  # 顯示黑白圖片
        if len(predictions) > 0:  # 有傳入預測資料
            title = "ai = " + str(predictions[start_id])
            # 預測正確顯示(o), 錯誤顯示(x)
            title += " (o)" if predictions[start_id] == labels[start_id] else " (x)"
            title += "\nlabel = " + str(labels[start_id])
        else:  # 沒有傳入預測資料
            title = "label = " + str(labels[start_id])
        ax.set_title(title, fontsize=12)  # X,Y軸不顯示刻度
        ax.set_xticks([])
        ax.set_yticks([])
        start_id += 1
    plt.show()


files = glob.glob("imagedata\*.jpg")  # 建立測試資料
test_feature = []
test_label = []
for file in files:
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰階
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)  # 轉為反相黑白
    test_feature.append(img)
    label = file[10:11]  # "imagedata\1.jpg"第10個字元1為label
    test_label.append(int(label))

test_feature = np.array(test_feature)  # 串列轉為矩陣
test_label = np.array(test_label)  # 串列轉為矩陣
test_feature_vector = test_feature.reshape(len(test_feature), 784).astype("float32")
test_feature_normalize = test_feature_vector / 255

model = load_model("Mnist_mlp_model.h5")

prediction = model.predict_classes(test_feature_normalize)
show_images_labels_predictions(
    test_feature, test_label, prediction, 0, len(test_feature)
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

mnist_npz_filename = "C:/_git/vcs/_big_files/mnist.npz"

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from keras.datasets import mnist

print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 我們來看看訓練資料是不是 6 萬筆、測試資料是不是有 1 萬筆。

print("訓練資料x長度 :", len(x_train))
print("訓練資料y長度 :", len(y_train))
print("測試資料x長度 :", len(x_test))
print("測試資料y長度 :", len(y_test))

RATIO = 4

x_train = x_train[: int(len(x_train) / RATIO)]
y_train = y_train[: int(len(y_train) / RATIO)]
x_test = x_test[: int(len(x_test) / RATIO)]
y_test = y_test[: int(len(y_test) / RATIO)]

print("訓練資料x長度 :", len(x_train))
print("訓練資料y長度 :", len(y_train))
print("測試資料x長度 :", len(x_test))
print("測試資料y長度 :", len(y_test))

"""
2.2.2 數據庫的內容

每筆輸入 (x) 就是一個手寫的 0-9 中一個數字的圖檔, 大小為 28x28
而輸出 (y) 當然就是「正確答案」
"""

fig = plt.figure(figsize=(10, 10))
for i in range(100):
    ax = plt.subplot2grid((10, 10), (int(i / 10), int(i % 10)))
    ax.imshow(x_train[i], cmap=plt.cm.gray)
    ax.axis("off")
plt.suptitle("畫前100筆資料")
plt.show()

# 編號87的訓練資料
# x_train[87]

# 因為是圖檔, 當然可以顯示出來!
plt.imshow(x_train[87], cmap="Greys")
plt.title("編號87的訓練資料")
plt.show()

print("編號87的訓練資料 的 shape :", x_train[87].shape)
print("編號87的訓練資料 的 目標  :", y_train[87])

"""
2.2.3 輸入格式整理

我們現在要用標準神經網路學學手寫辨識。
原來的每筆數據是個 28x28 的矩陣 (array),
但標準神經網路只吃「平平的」, 也就是每次要 28x28=784 長的向量。
因此我們要用 reshape 調校一下。
"""

print("訓練資料 x_train.shape =", x_train.shape)
print("測試資料 x_test.shape =", x_test.shape)

# 我們做一下 normalization, 把所有的數字都改為 0 到 1 之間。
x_train = x_train / 255
x_test = x_test / 255

"""
x_train = x_train/255
x_test = x_test/255
x_train.shape
#(60000, 28, 28)
#28*28 = 784
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
y_train[9487]
"""

"""
2.2.4 輸出格式整理

我們可能會想, 我們想學的函數是這樣的型式:

其實這樣不太好! 為什麼呢? 比如說我們的輸入 x 是一張 0 的圖,
因為我們訓練的神經網路總會有點誤差, 所以可能會得到:

那這意思是有可能是 0, 也有可能是 1 嗎!!??
可是 0 和 1 根本不像啊。換句話說分類的問題這樣做其實不合理!

於是我們會做 "1-hot enconding", 也就是

0 -> [1, 0, 0, 0, 0, 0, 0, 0, 0]
1 -> [0, 1, 0, 0, 0, 0, 0, 0, 0]
5 -> [0, 0, 0, 0, 0, 1, 0, 0, 0]
8 -> [0, 0, 0, 0, 0, 0, 0, 0, 1]

等等。因為分類問題基本上都要做這件事, Keras 其實已幫我們準備好套件!
"""

from tensorflow.python.keras.utils import np_utils

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

# 我們來看看剛剛是 9 的 87 號數據的答案。

print("編號87的訓練資料 的 目標  :", y_train[87])

# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 1.], dtype=float32)
#       0   1   2   3   4   5   6   7   8   9
# 和我們想的一樣! 至此我們可以打造我們的神經網路了。


"""
2-3 打造第一個神經網路
我們決定了我們的函數是
^f:R784→R10
這個樣子。而我們又說第一次要用標準神網路試試,
所以我們只需要再決定要幾個隱藏層、每層要幾個神經元, 用哪個激發函數就可以了。
2.3.1 決定神經網路架構、讀入相關套件
假如我們要這麼做:
    使用 3 個 hidden layers
    Hidden layer 1 用 6 個神經元
    Hidden layer 2 用 28 個神經元
    Hidden layer 3 用 2 個神經元
    Activation Function 唯一指名 relu
"""

# 於是從 Keras 把相關套件讀進來。
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizers import SGD

"""
2.3.2 建構我們的神經網路
和以前做迴歸或機器學習一樣, 我們就打開個「函數學習機」。
標準一層一層傳遞的神經網路叫 Sequential, 於是我們打開一個空的神經網路。
"""

model = Sequential()  # 打開一個空的神經網路

"""
我們每次用 add 去加一層, 從第一個隱藏層開始。
而第一個隱藏層因為 Keras 當然猜不到輸入長什麼樣子, 所以我們要告訴它。
而全連結的神經網路其實都是一個向量輸入, 也就是要先「拉平」。
"""

# 第一層 用 6 個神經元
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(6, activation="relu"))

"""
第二層 hidden layer 因為前面輸出是 6, 現在輸入是 28, 就不用再說了!
這裡的 28 只告訴 Keras, 我們第二層是用 28 個神經元!
"""
# 第二層 用 28 個神經元
model.add(Dense(28, activation="relu"))

# 第三層 用 2 個神經元
model.add(Dense(2, activation="relu"))

# 輸出有 10 個數字, 所以輸出層的神經元是 10 個!
# 而如果我們的網路輸出是 (y1,y2,…,y10) 我們還希望 10∑i=1yi=1
# 這可能嗎, 結果是很容易, 就用 softmax 當激發函數就可以!!
model.add(Dense(10, activation="softmax"))

# 至此我們的第一個神經網路就建好了!

"""
2.3.3 組裝

和之前比較不一樣的是我們還要做 compile 才正式把我們的神經網路建好。
你可以發現我們還需要做幾件事:
    1. 決定使用的 loss function, 一般是 mse
    2. 決定 optimizer, 我們用標準的 SGD
    3. 設 learning rate
為了一邊訓練一邊看到結果, 我們加設
metrics=['accuracy']
本行基本上和我們的神經網路功能沒有什麼關係。
"""

model.compile(loss="mse", optimizer=SGD(lr=0.087), metrics=["accuracy"])

"""
2-4 檢視我們的神經網路

我們可以檢視我們神經網路的架構, 可以確認一下是不是和我們想像的一樣。
2.4.1 看 model 的 summary
"""
print("檢視神經網路")
model.summary()  # 檢視神經網路

"""
很快算算參數數目和我們想像是否是一樣的!
784*6 + 6 = 4710
6*28 + 28 = 196
28*2 + 2 = 58
2*10 + 10 = 30

2-5 訓練你的第一個神經網路

恭喜! 我們完成了第一個神經網路。
現在要訓練的時候, 你會發現不是像以前沒頭沒腦把訓練資料送進去就好。
這裡我們還有兩件事要決定:
    1. 一次要訓練幾筆資料 (batch_size), 我們就 N = 100 筆調一次參數好了
    2. 這 6 萬筆資料一共要訓練幾次 (epochs), 我們訓練個 EPOCHS = 20 次試試

於是最精彩的就來了。你要有等待的心理準備...
"""

N = 600  # 每 N 筆調一次參數
EPOCHS = 1  # 訓練次數

print("資料共有 :", len(x_train), "筆, 每", N, "筆調一次參數, 共需調", len(x_train) / N, "次")
print("訓練次數 :", EPOCHS)

model.fit(x_train, y_train, batch_size=N, epochs=EPOCHS)  # 學習訓練.fit

# 2-6 試用我們的結果
# 我們 "predict" 放的是我們神經網路的學習結果。
# 這裡用 predict_classes 會讓我們 Keras 選 10 個輸出機率最大的那類。

# predict = model.predict_classes(x_test) 改成以下一行

predict = model.predict_step(x_test)
print("aaaaaaa")
print(predict)
predict = (model.predict(x_test) > 0.5).astype("int32")
print("bbbbbbb")
print(predict)

# array([7, 2, 1, ..., 7, 7, 0]) 有問題~~~~~~~~

# 寫個小程式, 秀出某測試資料的樣子, 還有我們可愛神經網路辨識的結果。


def test(num):
    plt.imshow(x_test[num], cmap="Greys")
    print("num =", num)
    print("神經網路判斷為 : ", predict[num])
    print()


predict_number = 87
test(predict_number)
plt.show()
print("神經網路判斷為 : ", predict[predict_number])

# 神經網路判斷為 : 3

# 到底測試資料總的狀況如何呢? 我們可以給我們神經網路「考一下試」。

score = model.evaluate(x_test, y_test)

print()
print("------------------------------------------------------------")
print("loss:", score[0])
print("正確率", score[1])

# loss: 0.06821700274944305
# 正確率 0.4345


# 2-7 訓練好的神經網路存起來!
# 如果對訓練成果滿意, 我們當然不想每次都再訓練一次! 我們可以把神經網路的架構和訓練好的參數都存起來, 以供日後使用!
# pip install h5py

model_json = model.to_json()
open("stupid_model.json", "w").write(model_json)
model.save_weights("stupid_model_weights.h5")


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

""" 暫存
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train/255
x_test = x_test/255

from tensorflow.python.keras.utils import np_utils

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizers import SGD
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(20, activation='relu'))

"""


print("使用TensorFlow")


"""
標準 神經網路 做手寫辨識

Keras 可以用各種不同的深度學習套件當底層, 指定用 Tensorflow 以確保執行的一致性。

%env KERAS_BACKEND=tensorflow

"""

# 讀入 Tensorflow, 其實我們沒用到, 玩爽的而已。

import tensorflow as tf

# from tensorflow.keras.datasets import mnist
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

n = 9487

print(x_train[n])
print(y_train[n])

# 1

plt.imshow(x_train[n], cmap="Greys")


# 3. 資料整理

# 先看個範例, 因為 numpy 「廣播」的特性, 我們對 array 中所有數字要同除以一個數可瞬間完成!

np.array([3, 78, 95, 99]) / 100

# array([0.03, 0.78, 0.95, 0.99])

# 現在才是我們真的要做的, 這個動作叫 "normalization"。

x_train = x_train / 255

x_test = x_test / 255

x_train.shape

(60000, 28, 28)

# 28*28 = 784

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

from tensorflow.keras.utils import to_categorical

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
y_train[9487]


# 打造神經網路

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

model = Sequential()
model.add(Dense(87, input_dim=784, activation="relu"))
model.add(Dense(87, activation="relu"))
model.add(Dense(10, activation="softmax"))

# 4. 組裝我們的神經網路

model.compile(loss="mse", optimizer=SGD(lr=0.087), metrics=["accuracy"])

print("檢視神經網路")
model.summary()  # 檢視神經網路

# 784*87 + 87 = 68295

# 5. 訓練

# model.fit(x_train, y_train, batch_size = 100, epochs = 20)# 學習訓練.fit
# model.fit(x_train, y_train, batch_size = 1200, epochs = 1)# 學習訓練.fit
model.fit(x_train, y_train, batch_size=2400, epochs=1)  # 學習訓練.fit

# 6. 訓練成果

# result = model.predict_classes(x_test) #old

result = model.predict_step(x_test)

n = 9999

print("神經網路預測是:", result[n])

plt.imshow(x_test[n].reshape(28, 28), cmap="Greys")

# 神經網路預測是: 6


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


import numpy as np
from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.models import load_model


def show_images_labels_predictions(images, labels, predictions, start_id, num=10):
    plt.gcf().set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, i + 1)
        ax.imshow(images[start_id], cmap="binary")  # 顯示黑白圖片
        if len(predictions) > 0:  # 有傳入預測資料
            title = "ai = " + str(predictions[start_id])
            # 預測正確顯示(o), 錯誤顯示(x)
            title += " (o)" if predictions[start_id] == labels[start_id] else " (x)"
            title += "\nlabel = " + str(labels[start_id])
        else:  # 沒有傳入預測資料
            title = "label = " + str(labels[start_id])
        ax.set_title(title, fontsize=12)  # X,Y軸不顯示刻度
        ax.set_xticks([])
        ax.set_yticks([])
        start_id += 1
    plt.show()


(train_feature, train_label), (test_feature, test_label) = mnist.load_data()

test_feature_vector = test_feature.reshape(len(test_feature), 784).astype("float32")
test_feature_normalize = test_feature_vector / 255

model = load_model("Mnist_mlp_model.h5")

# prediction=model.predict_classes(test_feature_normalize)  #預測

# 在TensorFlow 2.6版本中删除了这个predict_classes函数。
# 改用
predict_x = model.predict(test_feature_normalize)
classes_x = np.argmax(predict_x, axis=1)

show_images_labels_predictions(test_feature, test_label, predict_x, 0)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
