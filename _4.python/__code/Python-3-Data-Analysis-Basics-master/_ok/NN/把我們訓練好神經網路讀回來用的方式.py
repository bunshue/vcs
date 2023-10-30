"""

把我們訓練好神經網路讀回來用的方式

TBD

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

from tensorflow.keras.models import load_model

model = load_model('myCNNmodel.h5')

from tensorflow.keras.datasets import mnist

(x_train, y_test), (x_test, y_test) = mnist.load_data()

x_test = x_test.reshape(10000, 28, 28, 1) / 255

result = model.predict_classes(x_test)

def myCNN(n):
    print('我的 CNN 說是', result[n])
    X = x_test[n].reshape(28,28)
    plt.imshow(X, cmap='Greys')

n = 999

myCNN(n)


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

