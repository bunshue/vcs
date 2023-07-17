from keras.utils import np_utils
from keras.datasets import mnist
(train_feature, train_label), (test_feature, test_label) = mnist.load_data()

print(train_label[0:5])
train_label_onehot = np_utils.to_categorical(train_label)
print(train_label_onehot[0:5])
