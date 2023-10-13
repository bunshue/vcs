import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

import pandas as pd

df = pd.read_csv('iris.csv')

print(df.shape)

print(df.head(5))

print(df.describe())

import matplotlib.pyplot as plt
import numpy as np

target_mapping = {"setosa": 0,
          "versicolor": 1,
          "virginica": 2}
Y = df["target"].map(target_mapping)
colmap = np.array(["r", "g", "y"])
plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
plt.subplots_adjust(hspace = .5)
plt.scatter(df["sepal_length"], df["sepal_width"], color=colmap[Y])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.subplot(1, 2, 2)
plt.scatter(df["petal_length"], df["petal_width"], color=colmap[Y])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")

plt.show()

print('------------------------------------------------------------')	#60個

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn import preprocessing

np.random.seed(7)   #固定亂數種子

df = pd.read_csv('iris.csv')

label_encoder = preprocessing.LabelEncoder()
df["target"] = label_encoder.fit_transform(df["target"])


dataset = df.values
np.random.shuffle(dataset)
X = dataset[:,0:4].astype(float)
Y = to_categorical(dataset[:,4])

scaler = preprocessing.StandardScaler()
X = scaler.fit_transform(X)

X_train, Y_train = X[:120], Y[:120]
X_test, Y_test = X[120:], Y[120:]

model = Sequential()
model.add(Dense(6, input_shape=(4,), activation="relu"))
model.add(Dense(6, activation="relu"))
model.add(Dense(3, activation="softmax"))

print(model.summary())


model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])


model.fit(X_train, Y_train, epochs = 100, batch_size = 5)


loss, accuracy = model.evaluate(X_test, Y_test)
print("Accuracy = {:.2f}".format(accuracy))

#Y_pred = model.predict_classes(X_test)
Y_pred = model.predict_step(X_test)
print(Y_pred)
Y_target = dataset[:,4][120:].astype(int)
print(Y_target)


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


