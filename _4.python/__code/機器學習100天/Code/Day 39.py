"""


pip install tf-nightly


"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#导入keras
import tensorflow.keras as keras

#导入tensorflow
import tensorflow as tf
print(tf.__version__)



"""

下载mnist数据

keras默认从(https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz)下载，但国内很难连上， 可以参考(http://www.cnblogs.com/shinny/p/9283372.html)。手动下载mnist.npz，然后修改mnist.py中的引用路径。 如果找不到mnist.py，可以用everthing搜索。

mnist.npz已上传到datasets文件夹，可从这里下载。


"""
mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()
print(x_train[0])


import matplotlib.pyplot as plt

plt.imshow(x_train[0],cmap=plt.cm.binary)
plt.show()

print('答案')
print(y_train[0])


x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

print(x_train[0])

plt.imshow(x_train[0],cmap=plt.cm.binary)
plt.show()






model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)



val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss)
print(val_acc)


predictions = model.predict(x_test)
print(predictions)


import numpy as np

print(np.argmax(predictions[0]))



plt.imshow(x_test[0],cmap=plt.cm.binary)
plt.show()


# 保存模型
model.save('tmp_epic_num_reader.model')

# 加载保存的模型
new_model = tf.keras.models.load_model('tmp_epic_num_reader.model')

# 测试保存的模型
predictions = new_model.predict(x_test)
print(np.argmax(predictions[0]))



