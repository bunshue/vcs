from keras.datasets import mnist
(train_feature, train_label), (test_feature, test_label) = mnist.load_data()

train_feature_vector =train_feature.reshape(len(train_feature), 784).astype('float32')
#print(train_feature_vector[0])
train_feature_normalize = train_feature_vector/255
print(train_feature_normalize[0]) 
