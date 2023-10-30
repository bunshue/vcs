"""
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


import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

model = load_model('mynn01.h5')

from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_test = x_test.reshape(10000, 784)/255
y_pred = model.predict_classes(x_test)

print(y_pred)

def myNN(n):
  k = int(n)
  print('可愛神經網路預測', y_pred[k])
  plt.imshow(x_test[k].reshape(28,28), cmap='Greys')

myNN(9487)

#可愛神經網路預測 2


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

