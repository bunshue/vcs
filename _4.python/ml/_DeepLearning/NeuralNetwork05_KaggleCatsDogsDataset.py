"""
Kaggle Cats and Dogs Dataset

https://www.microsoft.com/en-us/download/details.aspx?id=54765

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


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

""" 將圖片分成兩大群
img_directory = 'D:/_git/vcs/_big_files/kagglecatsanddogs_5340/PetImages/'
validation_split = 0.1

subclasses = os.listdir(img_directory)

for subclass in subclasses:
    os.makedirs(img_directory + 'train/' + subclass, exist_ok=True)
    os.makedirs(img_directory + 'validation/' + subclass, exist_ok=True)
    for img in os.listdir(img_directory + subclass):
        rand = random.choices(['train/', 'validation/'], [1-validation_split, validation_split])[0]
        os.rename(img_directory + subclass + '/' + img, img_directory + rand + subclass + '/' + img)
    os.rmdir(img_directory + subclass)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 要先對數據集中的圖片進行處理，可能需要進行的任務有圖像尺寸統一、顏色處理等

import cv2

# 數據集的路徑
DATADIR = "D:/_git/vcs/_big_files/kagglecatsanddogs_5340_1000/PetImages/"
DATADIR = "D:/_git/vcs/_big_files/kagglecatsanddogs_5340_800/PetImages/"

CATEGORIES = ["Dog", "Cat"]

for category in CATEGORIES:
    path = os.path.join(DATADIR, category)  # 創建路徑
    for img in os.listdir(path):  # 迭代遍歷每個圖片
        img_array = cv2.imread(
            os.path.join(path, img), cv2.IMREAD_GRAYSCALE
        )  # 轉化成array
        plt.imshow(img_array, cmap="gray")  # 轉換成圖像展示
        show()

        break  # 我們作為演示只展示一張，所以直接break了
    break  # 同上


# 看下array中存儲的圖像數據：
# print(img_array)

print("看下array的形狀")
print(img_array.shape)

# 我們可以看到這是一張很大的圖片，并且擁有RGB3個通道，這并不是我們想要的，
# 所以接下來我們將要進行的操作會使圖像變小，并且只剩下灰度：

print("resize")
IMG_SIZE = 100

new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
plt.imshow(new_array, cmap="gray")
show()

# 接下來，我們將要創建所有這些培訓數據，但是，首先，我們應該留出一些圖像進行最終測試。
# 我將手動創建一個名為Testing的目錄，然后在其中創建2個目錄，一個用于Dog，一個用于Cat。
# 從這里開始，我將把Dog和Cat的前15張圖像移到訓練版本中。確保移動它們，而不是復制。我們將使用它進行最終測試。

print("訓練資料")
training_data = []


def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)  # 得到分類，其中 0=dog 1=cat

        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # 大小轉換
                training_data.append([new_array, class_num])  # 加入訓練數據中
            except Exception as e:  # 為了保證輸出是整潔的
                pass
            # except OSError as e:
            #    print("OSErrroBad img most likely", e, os.path.join(path,img))
            # except Exception as e:
            #    print("general exception", e, os.path.join(path,img))


"""
#以下 久
create_training_data()

print(len(training_data))

# 我們有大約25,000張圖片。
# 我們要做的一件事是確保我們的數據是平衡的。在這個數據集的情況下，
# 我可以看到數據集開始時是平衡的。平衡，我的意思是每個班級都有相同數量的例子（相同數量的狗和貓）。
# 如果不平衡，您要么將類權重傳遞給模型，以便它可以適當地測量誤差，或者通過將較大的集修剪為與較小集相同的大小來平衡樣本。
# 現在數據集中要么全是dog要么全是cat，因此接下來要引入隨機：

random.shuffle(training_data)

# 我們的training_data是一個列表，這意味著它是可變的，所以它現在很好地改組了。
# 我們可以通過迭代幾個初始樣本并打印出類來確認這一點：

for sample in training_data[:10]:
    print(sample[1])

# 現在可以看到已經是0、1交替了，我們可以開始我們的模型了：

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

# 讓我們保存這些數據，這樣我們就不需要每次想要使用神經網絡模型時繼續計算它：

pickle_out = open("tmp_X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("tmp_y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()
# We can always load it in to our current script, or a totally new one by doing:

pickle_in = open("tmp_X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle", "rb")
y = pickle.load(pickle_in)

# 現在我們已經拿出了數據集，我們已經準備好覆蓋卷積神經網絡，并用我們的數據進行分類。
# 以上就是這次的關于數據集操作的全部任務。

#基礎知識
#基本的CNN結構如下： Convolution(卷積) -> Pooling(池化) -> Convolution -> Pooling -> Fully Connected Layer(全連接層) -> Output
#Convolution（卷積）是獲取原始數據并從中創建特征映射的行為。
#Pooling(池化)是下采樣，通常以“max-pooling”的形式，我們選擇一個區域，然后在該區域中取最大值，這將成為整個區域的新值。
#Fully Connected Layers(全連接層)是典型的神經網絡，其中所有節點都“完全連接”。卷積層不像傳統的神經網絡那樣完全連接。
#卷積：我們將采用某個窗口，并在該窗口中查找要素,該窗口的功能現在只是新功能圖中的一個像素大小的功能，但實際上我們將有多層功能圖。
#接下來，我們將該窗口滑過并繼續該過程,繼續此過程，直到覆蓋整個圖像。
#池化：最常見的池化形式是“最大池化”，其中我們簡單地獲取窗口中的最大值，并且該值成為該區域的新值。
#全連接層：每個卷積和池化步驟都是隱藏層。在此之后，我們有一個完全連接的層，然后是輸出層。
#完全連接的層是典型的神經網絡（多層感知器）類型的層，與輸出層相同。
#注意 本次代碼中所需的X.pickle和y.pickle為上一篇的輸出，路徑請根據自己的情況更改！

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D

pickle_in = open("tmp_X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle", "rb")
y = pickle.load(pickle_in)

X = X / 255.0

model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors

model.add(Dense(64))

model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
"""

""" 久
model.fit(X, y, batch_size=32, epochs=3, validation_split=0.3)  # 學習訓練.fit

#在僅僅三個epoches之后，我們的驗證準確率為71％。
#如果我們繼續進行更多的epoches，我們可能會做得更好，但我們應該討論我們如何知道我們如何做。
#為了解決這個問題，我們可以使用TensorFlow附帶的TensorBoard，它可以幫助您在訓練模型時可視化模型。
#我們將在下一個教程中討論TensorBoard以及對我們模型的各種調整！

# 這是Python，TensorFlow和Keras教程系列的深度學習基礎知識的第4部分。
# 在這一部分，我們將討論的是TensorBoard。
# TensorBoard是一個方便的應用程序，允許您在瀏覽器中查看模型或模型的各個方面。
# 我們將TensorBoard與Keras一起使用的方式是通過Keras回調。實際上有很多Keras回調，你可以自己制作。

from tensorflow.keras.callbacks import TensorBoard

# Using TensorFlow backend.
# 創建TensorBoard回調對象
NAME = "Cats-vs-dogs-CNN"

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

#最終，你會希望獲得更多的自定義NAME，但現在這樣做。
#因此，這將保存模型的訓練數據logs/NAME，然后由TensorBoard讀取。
#最后，我們可以通過將它添加到.fit方法中來將此回調添加到我們的模型中，
#例如：
#model.fit(X, y,
#          batch_size=32,
#          epochs=3,
#          validation_split=0.3,
#          callbacks=[tensorboard])  # 學習訓練.fit
#請注意，這callbacks是一個列表。您也可以將其他回調傳遞到此列表中。
#我們的模型還沒有定義，所以現在讓我們把它們放在一起：

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard

# more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.

NAME = "Cats-vs-dogs-CNN"

pickle_in = open("tmp_X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle", "rb")
y = pickle.load(pickle_in)

X = X / 255.0

model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation("sigmoid"))

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=["accuracy"],
)

model.fit(X, y, batch_size=32, epochs=3, validation_split=0.3, callbacks=[tensorboard])  # 學習訓練.fit

#運行此之后，您應該有一個名為的新目錄logs。我們現在可以使用tensorboard從這個目錄中可視化初始結果。
#打開控制臺，切換到工作目錄，然后鍵入：tensorboard --logdir=logs/。
#您應該看到一個通知：TensorBoard 1.10.0 at http://H-PC:6006 (Press CTRL+C to quit)“h-pc”是您機器的名稱。
#打開瀏覽器并前往此地址。你應該看到類似的東西：

# 現在我們可以看到我們的模型隨著時間的推移。讓我們改變模型中的一些東西。
# 首先，我們從未在密集層中添加激活。另外，讓我們嘗試整體較小的模型：

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard

# more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.

NAME = "Cats-vs-dogs-64x2-CNN"

pickle_in = open("tmp_X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle", "rb")
y = pickle.load(pickle_in)

X = X / 255.0

model = Sequential()

model.add(Conv2D(64, (3, 3), input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation("relu"))

model.add(Dense(1))
model.add(Activation("sigmoid"))

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=["accuracy"],
)

model.fit(X, y, batch_size=32, epochs=10, validation_split=0.3, callbacks=[tensorboard])  # 學習訓練.fit

# 除此之外，我還改名為NAME = "Cats-vs-dogs-64x2-CNN"。
# 不要忘記這樣做，否則你會偶然附加到你以前的型號的日志，它看起來不太好。我們現在檢查TensorBoard：

#看起來更好！但是，您可能會立即注意到驗證丟失的形狀。
#損失是衡量錯誤的標準，看起來很明顯，在我們的第四個時代之后，事情開始變得糟糕。
#有趣的是，我們的驗證準確性仍然持續，但我想它最終會開始下降。
#更可能的是，第一件遭受的事情確實是你的驗證損失。這應該提醒你，你幾乎肯定會開始過度適應。
#這種情況發生的原因是該模型不斷嘗試減少樣本損失。
#在某些時候，模型不是學習關于實際數據的一般事物，而是開始只記憶輸入數據。
#如果你繼續這樣做，是的，樣本中的“準確性”會上升，但你的樣本，以及你試圖為模型提供的任何新數據可能會表現得很差。
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
