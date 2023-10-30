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

#1. 讀入深度學習套件

from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM
from tensorflow.keras.datasets import imdb

#2. 讀入數據

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)

print(len(x_train))

#25000

print(len(x_test))

#25000

print(len(x_train[0]))

#218

print(len(x_train[1]))

#189

print(y_train[0])

#1

print(y_train[1])

#0

#3. 資料處理
x_train = sequence.pad_sequences(x_train, maxlen=100)
x_test = sequence.pad_sequences(x_test, maxlen=100)

#4. step 01: 打造一個函數學習機

model = Sequential()
model.add(Embedding(10000, 128))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy',
             optimizer='adam',
             metrics=['accuracy'])

model.summary()


#(128+128+1)*4*128 = 131584

#5. step 02: 訓練

model.fit(x_train, y_train, batch_size=32, epochs=10,
         validation_data=(x_test, y_test))

model_json = model.to_json()
open('imdb_model_architecture.json', 'w').write(model_json)
model.save_weights('imdb_model_weights.h5')

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

