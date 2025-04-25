import tensorflow as tf
import numpy as np

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 01_MLPpredict_TensorFlow_ModelAdd.py

x1 = np.random.random((500, 1))
x2 = np.random.random((500, 1)) + 1
x_train = np.concatenate((x1, x2))

y1 = np.zeros((500,), dtype=int)
y2 = np.ones((500,), dtype=int)
y_train = np.concatenate((y1, y2))

"""
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(10, activation=tf.nn.relu, input_dim=1),
  tf.keras.layers.Dense(10, activation=tf.nn.relu),
  tf.keras.layers.Dense(2, activation=tf.nn.softmax)
])
"""
# 建立模型
model = tf.keras.models.Sequential()
# 加入 2D 的 Convolution Layer，接著一層 ReLU 的 Activation 函數
model.add(
    tf.keras.layers.Dense(units=10, activation=tf.nn.relu, input_dim=1)  # tf.nn.relu
)
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu))  # tf.nn.relu
model.add(tf.keras.layers.Dense(units=2, activation=tf.nn.softmax))  # tf.nn.softmax

model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

model.fit(x_train, y_train, epochs=20, batch_size=128)

# 測試
x_test = np.array([[0.22], [0.31], [1.22], [1.33]])
y_test = np.array([0, 0, 1, 1])

score = model.evaluate(x_test, y_test, batch_size=128)
print("score:", score)

predict = model.predict(x_test)
print("predict:", predict)
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:", y_pred)
print("y_test", y_test[:])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 02_MLPpredict_Keras.py

import keras
from keras.models import Sequential
from keras.layers import Dense

# from keras.optimizers import SGD, Dropout, Activation

# Generate dummy data

""" 
x_train = np.random.random((1000, 20))
y_train = keras.utils.to_categorical(np.random.randint(2, size=(1000, 1)), num_classes=2)
x_test = np.random.random((100, 20))
y_test = keras.utils.to_categorical(np.random.randint(2, size=(100, 1)), num_classes=2)

"""

x1 = np.random.random((500, 1))
x2 = np.random.random((500, 1)) + 1
x_train = np.concatenate((x1, x2))

y1 = np.zeros((500,), dtype=int)
y2 = np.ones((500,), dtype=int)
y_train = np.concatenate((y1, y2))
# y_train = keras.utils.to_categorical(y_train, num_classes=2)


model = Sequential()
model.add(Dense(units=10, activation="relu", input_dim=1))
model.add(Dense(units=10, activation="relu"))
model.add(Dense(units=2, activation="softmax"))


model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

model.fit(x_train, y_train, epochs=20, batch_size=128)


# 測試
x_test = np.array([[0.22], [0.31], [1.22], [1.33]])
y_test = np.array([0, 0, 1, 1])

score = model.evaluate(x_test, y_test, batch_size=128)
print("score:", score)

predict = model.predict(x_test)
print("predict:", predict)
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:", y_pred)
print("y_test", y_test[:])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 03_MLPOne-hotEncoding.py

x1 = np.random.random((500, 1))
x2 = np.random.random((500, 1)) + 1
x_train = np.concatenate((x1, x2))

y1 = np.zeros((500,), dtype=int)
y2 = np.ones((500,), dtype=int)
y_train = np.concatenate((y1, y2))


# 將數字轉為 One-hot 向量
y_train2 = tf.keras.utils.to_categorical(y_train, num_classes=2)

# 建立模型
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu, input_dim=1))
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu))  # tf.nn.relu
model.add(tf.keras.layers.Dense(units=2, activation=tf.nn.softmax))  # tf.nn.softmax

# 設定模型的 Loss 函數、Optimizer 以及用來判斷模型好壞的依據（metrics）
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)

"""
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
"""

model.fit(x_train, y_train2, epochs=20, batch_size=128)


# 測試
x_test = np.array([[0.22], [0.31], [1.22], [1.33]])
y_test = np.array([0, 0, 1, 1])
y_test2 = tf.keras.utils.to_categorical(y_test, num_classes=2)

score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:", score)

predict = model.predict(x_test)
print("predict:", predict)
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:", y_pred)
print("y_test", y_test[:])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_MLPOne-20InputOutput_epochs.py


def CreateDatasets(high, iNum, iArraySize):
    x_train = np.random.random((iNum, iArraySize)) * float(high)
    y_train = ((x_train[:iNum, 0] + x_train[:iNum, 1]) / 2).astype(int)  # 取整數
    return x_train, y_train, tf.keras.utils.to_categorical(y_train, num_classes=(high))


category = 10
dim = 2
x_train, y_train, y_train2 = CreateDatasets(
    category, 1000, dim
)  # 建立全部1000個二維的訓練特徵值X因，而訓練結果Y 有10種答案

# 建立模型
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu, input_dim=dim))
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=category, activation=tf.nn.softmax))
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)
model.fit(
    x_train,
    y_train2,
    # epochs=20,
    epochs=20 * 10,  # <--調整這裡
    batch_size=128,
)

# 測試
x_test, y_test, y_test2 = CreateDatasets(category, 10, dim)
score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:", score)

predict = model.predict(x_test)
# print("predict:",predict)
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:", y_pred)
print("y_test", y_test[:])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_MLPOne-20InputOutput_AddDenses.py


def CreateDatasets(high, iNum, iArraySize):
    x_train = np.random.random((iNum, iArraySize)) * float(high)
    y_train = ((x_train[:iNum, 0] + x_train[:iNum, 1]) / 2).astype(int)  # 取整數
    return x_train, y_train, tf.keras.utils.to_categorical(y_train, num_classes=(high))


category = 10
dim = 2
x_train, y_train, y_train2 = CreateDatasets(
    category, 1000, dim
)  # 建立全部1000個二維的訓練特徵值X因，而訓練結果Y 有10種答案

# 建立模型
model = tf.keras.models.Sequential()
model.add(
    tf.keras.layers.Dense(
        units=10 * 10, activation=tf.nn.relu, input_dim=dim  # <--調整這裡
    )
)
model.add(tf.keras.layers.Dense(units=10 * 10, activation=tf.nn.relu))  # <--調整這裡
model.add(tf.keras.layers.Dense(units=10 * 10, activation=tf.nn.relu))  # <--新增這裡
model.add(tf.keras.layers.Dense(units=category, activation=tf.nn.softmax))
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)
model.fit(x_train, y_train2, epochs=20, batch_size=128)

# 測試
x_test, y_test, y_test2 = CreateDatasets(category, 10, dim)
score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:", score)

predict = model.predict(x_test)
# print("predict:",predict)
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x
print("predict_classes:", y_pred)
print("y_test", y_test[:])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_MLPOne-20InputOutput_MoreDatasets.py


def CreateDatasets(high, iNum, iArraySize):
    x_train = np.random.random((iNum, iArraySize)) * float(high)
    y_train = ((x_train[:iNum, 0] + x_train[:iNum, 1]) / 2).astype(int)  # 取整數
    return x_train, y_train, tf.keras.utils.to_categorical(y_train, num_classes=(high))


category = 10
dim = 2
x_train, y_train, y_train2 = CreateDatasets(category, 1000 * 10, dim)  # 修改這裡

# 建立模型
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu, input_dim=dim))
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=category, activation=tf.nn.softmax))
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)
model.fit(x_train, y_train2, epochs=20, batch_size=128)

# 測試
x_test, y_test, y_test2 = CreateDatasets(category, 10, dim)
score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:", score)

predict = model.predict(x_test)
# print("predict:",predict)
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:", y_pred)
print("y_test", y_test[:])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 08_MLPOne-20InputOutput-99.9.py


def CreateDatasets(high, iNum, iArraySize):
    x_train = np.random.random((iNum, iArraySize)) * float(high)
    y_train = ((x_train[:iNum, 0] + x_train[:iNum, 1]) / 2).astype(int)  # 取整數
    return x_train, y_train, tf.keras.utils.to_categorical(y_train, num_classes=(high))


category = 10
dim = 2
x_train, y_train, y_train2 = CreateDatasets(category, 1000 * 10, dim)  # 修改這裡


# 建立模型
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=10 * 100, activation=tf.nn.relu, input_dim=dim))
model.add(tf.keras.layers.Dense(units=10 * 100, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=10 * 100, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=10 * 100, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=category, activation=tf.nn.softmax))
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)
model.fit(x_train, y_train2, epochs=20 * 100, batch_size=128 * 100)

# 測試
x_test, y_test, y_test2 = CreateDatasets(category, 10, dim)
score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:", score)

predict = model.predict(x_test)
# print("predict:",predict)
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:", y_pred)
print("y_test", y_test[:])

print("------------------------------------------------------------")  # 60個
