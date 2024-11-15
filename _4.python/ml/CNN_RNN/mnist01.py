"""
分析顯示 mnist 資料集

"""


"""
Keras：MNIST手寫數字辨識資料集
MNIST手寫數字辨識資料集

由於MNIST的資料大小適中，而且皆為單色影像(黑字白底)，
十分適合做為初學者第一個建立模型、訓練、與預測的資料集。

MNIST資料集是由60,000筆訓練資料、10,000筆測試資料所組成。
MNIST資料集裡的每一筆資料皆由images(數字的影像)與labels
(該圖片的真實數字，其實就是答案)所組成。

# 下載minst資料集檔案
# 資料集檔案位置：C:/Users/070601/.keras/datasets/mnist.npz


標準 神經網路 做手寫辨識

Keras 可以用各種不同的深度學習套件當底層, 指定用 Tensorflow 以確保執行的一致性。

%env KERAS_BACKEND=tensorflow

讀入 MNIST 數據庫

MNIST 是有一堆 0-9 的手寫數字圖庫。有 6 萬筆訓練資料, 1 萬筆測試資料。
它是 "Modified" 版的 NIST 數據庫, 原來的版本有更多資料。
這個 Modified 的版本是由 LeCun, Cortes, 及 Burges 等人做的。可以參考這個數據庫的原始網頁。

MNIST 可以說是 Deep Learning 最有名的範例, 它被 Deep Learning 大師 Hinton 稱為「機器學習的果蠅」。
2.2.1 由 Keras 讀入 MNIST

Keras 很貼心的幫我們準備好 MNIST 數據庫, 我們可以這樣讀進來 (第一次要花點時間)。
http://yann.lecun.com/exdb/mnist/

用tensorflow讀入 MNSIT 數據集
from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 標準 1 遠端檔案
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 標準 2 本地檔案
mnist_npz_filename = "C:/_git/vcs/_big_files/mnist.npz"

mnist = np.load(mnist_npz_filename)
x_train, y_train = mnist["x_train"], mnist["y_train"]
x_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()

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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
