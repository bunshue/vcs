import keras
from keras.models import Sequential
from keras.layers import Dense

# from keras.optimizers import SGD, Dropout, Activation

# Generate dummy data
import numpy as np

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
