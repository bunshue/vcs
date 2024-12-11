"""
from sklearn.neural_network.multilayer_perceptron import MLPClassifier
一律改成
from sklearn.neural_network import MLPClassifier


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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from sklearn import datasets

print("------------------------------------------------------------")  # 60個

#MLPClassifier（多層感知器分類器）

from sklearn.neural_network import MLPClassifier

X = [[0., 0.], [1., 1.]]
y = [0, 1]
mlp = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 5), random_state=1)
mlp.fit(X, y)

print(mlp.n_layers_)
print(mlp.n_iter_)
print(mlp.loss_)
print(mlp.out_activation_)

print("------------------------------------------------------------")  # 60個

#MLPClassifier（多層感知器分類器）

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score 

iris = datasets.load_iris() 
data = iris.data 
labels = iris.target

# We add max_iter=1000 becaue the default is max_iter=200 and 
# it is not enough for full convergence
mlp = MLPClassifier(random_state=1, max_iter=1000) 
mlp.fit(data, labels)

pred = mlp.predict(data)

print()
print('Accuracy: %.2f' % accuracy_score(labels, pred))

print("------------------------------------------------------------")  # 60個

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris() 
data = iris.data 
labels = iris.target

data_train, data_test, labels_train, labels_test = train_test_split(data, labels, test_size=0.5, random_state=1)  

scaler = StandardScaler() 
scaler.fit(data) 
data_train_std = scaler.transform(data_train) 
data_test_std = scaler.transform(data_test)  

data_train = data_train_std 
data_test = data_test_std

# We add max_iter=1000 becaue the default is max_iter=200 and 
# it is not enough for full convergence 
mlp = MLPClassifier(random_state=1, max_iter=1000)
mlp.fit(data, labels)
mlp.fit(data_train, labels_train)
pred = mlp.predict(data_test)

print()
print('Misclassified samples: %d' % (labels_test != pred).sum())
print('Accuracy: %.2f' % accuracy_score(labels_test, pred))

print("------------------------------------------------------------")  # 60個

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap

#Apply standardization
standardised = True

# 0萼長 1萼寬 2瓣長 3瓣寬
M = {0:"sepal length", 1:"sepal width", 2:"petal length", 3:"petal width"}

#Choose two features
x=1 #1 corresponds to the sepal width 萼寬
y=3 #3 corresponds to the petal width 瓣寬

iris = datasets.load_iris()
data = iris.data[:,[x,y]]

labels = iris.target

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.5, random_state=1)

reg = StandardScaler()
reg.fit(data)
X_train_std = reg.transform(X_train)
X_test_std = reg.transform(X_test)

if (standardised == False):
  X_train_std = X_train
  X_test_std = X_test

# We add max_iter=1000 becaue the default is max_iter=200 and 
# it is not enough for full convergence
mlp = MLPClassifier(random_state=1, max_iter=1000)
mlp.fit(X_train_std, y_train)

y_pred = mlp.predict(X_test_std)
print('Misclassified samples: %d' % (y_test != y_pred).sum())

print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))


def plot_decision_regions(data, labels, classifier, resolution=0.01):
    markers = ('s', '*', '^')
    colors = ('blue', 'green', 'red')
    cmap = ListedColormap(colors)
    # plot the decision surface
    x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1
    y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1

    x, y = np.meshgrid(np.arange(x_min, x_max, resolution), np.arange(y_min, y_max, resolution))
    
    Z = classifier.predict(np.array([x.ravel(), y.ravel()]).T)
    Z = Z.reshape(x.shape)
    
    plt.pcolormesh(x, y, Z, cmap=cmap)
    plt.xlim(x.min(), x.max())
    plt.ylim(y.min(), y.max())

    colors = ('yellow', 'white', 'black')
    #cmap = ListedColormap(colors)
    #plot the data
    classes = ["setosa", "versicolor", "verginica"]
    for index, cl in enumerate(np.unique(labels)):
        plt.scatter(data[labels == cl, 0], data[labels == cl, 1], c=cmap(index), marker=markers[index], edgecolor="black", alpha=1.0, s=50, label=classes[index])  
 
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))
plot_decision_regions(X_combined_std, y_combined, classifier=mlp)

if (standardised == False):
  xString = M[x] + " [not standardized]"  
  yString = M[y] + " [not standardized]" 
else:
  xString = M[x] + " [standardized]"  
  yString = M[y] + " [standardized]"  

plt.xlabel(xString)
plt.ylabel(yString)
plt.legend(loc='upper left')
plt.show()

print("------------------------------------------------------------")  # 60個

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

def tanh(x):     
    return (1.0 - np.exp(-2*x))/(1.0 + np.exp(-2*x))

def tanh_derivative(x):     
    return (1 + tanh(x))*(1 - tanh(x))
    
class NeuralNetwork:
    #network consists of a list of integers, indicating 
    #the number of neurons in each layer
    def __init__(self, net_arch): 
        np.random.seed(0)                  
        self.activity = tanh         
        self.activity_derivative = tanh_derivative 
        self.layers = len(net_arch)         
        self.steps_per_epoch = 1000
        self.arch = net_arch        

        self.weights = []         
        #range of weight values (-1,1)         
        for layer in range(len(net_arch) - 1):             
            w = 2*np.random.rand(net_arch[layer] + 1, net_arch[layer+1]) - 1           
            self.weights.append(w)

    def fit(self, data, labels, learning_rate=0.1, epochs=10):         
        #Add bias units to the input layer         
        ones = np.ones((1, data.shape[0]))        
        Z = np.concatenate((ones.T, data), axis=1)
        training = epochs*self.steps_per_epoch


        for k in range(training):             
            if k % self.steps_per_epoch == 0:                  
                #print ('epochs:', k/self.steps_per_epoch)    
                print('epochs: {}'.format(k/self.steps_per_epoch))              
                for s in data:                     
                    print(s, self.predict(s))

            sample = np.random.randint(data.shape[0])            
            y = [Z[sample]] 

            for i in range(len(self.weights)-1):                     
                activation = np.dot(y[i], self.weights[i])                         
                activity = self.activity(activation)  
                #add the bias for the next layer                     
                activity = np.concatenate((np.ones(1), np.array(activity)))                      
                y.append(activity)   
             
            #last layer              
            activation = np.dot(y[-1], self.weights[-1])             
            activity = self.activity(activation)             
            y.append(activity)
                    
            #error for the output layer             
            error = labels[sample] - y[-1]             
            delta_vec = [error * self.activity_derivative(y[-1])] 

            #we need to begin from the back from the next to last layer
            for i in range(self.layers-2, 0, -1):  
                #delta_vec [1].dot(self.weights[i][1:].T)                
                error = delta_vec[-1].dot(self.weights[i][1:].T) 
                error = error*self.activity_derivative(y[i][1:])               
                delta_vec.append(error)

            # reverse
            # [level3(output)->level2(hidden)]  => [level2(hidden)->level3(output)]
            delta_vec.reverse()

            # backpropagation
            # 1. Multiply its output delta and input activation 
            #    to get the gradient of the weight.
            # 2. Subtract a ratio (percentage) of the gradient from the weight
            for i in range(len(self.weights)):
                layer = y[i].reshape(1, self.arch[i]+1) 
 
                delta = delta_vec[i].reshape(1, self.arch[i+1])
                self.weights[i] += learning_rate * layer.T.dot(delta)

    def predict(self, x): 
        val = np.concatenate((np.ones(1).T, np.array(x)))      
        for i in range(0, len(self.weights)):
            val = self.activity(np.dot(val, self.weights[i]))
            val = np.concatenate((np.ones(1).T, np.array(val)))
            
        return val[1]

    def plot_decision_regions(self, X, y, points=200):
        markers = ('o', '^')
        colors = ('red', 'blue')
        cmap = ListedColormap(colors)
        # plot the decision surface
        x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        
        resolution = max(x1_max - x1_min, x2_max - x2_min)/float(points)
        #resolution = 0.01
     
        xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
        
        input = np.array([xx1.ravel(), xx2.ravel()]).T 
        Z = np.empty(0)
        for i in range(input.shape[0]):
            val = self.predict(np.array(input[i]))
            if val < 0.5: val = 0 
            if val >= 0.5: val = 1
            Z = np.append(Z, val)

        Z = Z.reshape(xx1.shape)
        
        plt.pcolormesh(xx1, xx2, Z, cmap=cmap)
        plt.xlim(xx1.min(), xx1.max())
        plt.ylim(xx2.min(), xx2.max())
        # plot all samples

        classes = ["False", "True"]
        for idx, cl in enumerate(np.unique(y)):
            plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=1.0, c=cmap(idx), marker=markers[idx], s=80, label=classes[idx])
            
        plt.xlabel('x-axis')            
        plt.ylabel('y-axis')
        plt.legend(loc='upper left')
        plt.show()            

nn = NeuralNetwork([2,2,1])
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([0, 1, 1, 0])
nn.fit(X, y, epochs=10)
print("Final prediction")
for s in X:
  print(s, nn.predict(s))

nn.plot_decision_regions(X, y)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#import tensorflow as tf
import tensorflow.compat.v1 as tf # 強制使用tensorflow 1.0
tf.disable_v2_behavior()

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session() # tensorflow 1.0才有的指令
print(sess.run(hello))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
language model
"""

#data_processing

import re
import codecs

filepath = 'war_and_peace.txt'  # in
out_file = 'tmp_wap.txt'  # out

# Regexes used to clean up the text
NEW_LINE_IN_PARAGRAPH_REGEX = re.compile(r'(\S)\n(\S)')
MULTIPLE_NEWLINES_REGEX = re.compile(r'(\n)(\n)+')

# Read text as string
with codecs.open(filepath, encoding='utf-8', mode='r') as f_input:
    book_str = f_input.read()

# Cleanup
book_str = NEW_LINE_IN_PARAGRAPH_REGEX.sub('\g<1> \g<2>', book_str)
book_str = MULTIPLE_NEWLINES_REGEX.sub('\n\n', book_str)

# Write proccessed text to file
with codecs.open(out_file, encoding='utf-8', mode='w')as f_output:
    f_output.write(book_str)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from six.moves import range
import codecs


class DataReader(object):
    """Data reader used for training language model."""
    def __init__(self, filepath, batch_length, batch_size):
        self.batch_length = batch_length
        self.batch_size = batch_size
        # Read data into string
        with codecs.open(filepath, encoding='utf-8', mode='r') as f:
            self.data_str = f.read()
        self.data_length = len(self.data_str)
        print('data_length: ', self.data_length)
        # Create a list of characters, indices are class indices for softmax
        char_set = set()
        for ch in self.data_str:
            char_set.add(ch)
        self.char_list = sorted(list(char_set))
        print('char_list: ', len(self.char_list), self.char_list)
        # Create reverse mapping to look up the index based on the character
        self.char_dict = {val: idx for idx, val in enumerate(self.char_list)}
        print('char_dict: ', self.char_dict)
        # Initalise random start indices
        self.reset_indices()

    def reset_indices(self):
        self.start_idxs = np.random.random_integers(
            0, self.data_length, self.batch_size)

    def get_sample(self, start_idx, length):
        # Get a sample and wrap around the data string
        return [self.char_dict[self.data_str[i % self.data_length]]
                for i in range(start_idx, start_idx+length)]

    def get_input_target_sample(self, start_idx):
        sample = self.get_sample(start_idx, self.batch_length+1)
        inpt = sample[0:self.batch_length]
        trgt = sample[1:self.batch_length+1]
        return inpt, trgt

    def get_batch(self, start_idxs):
        input_batch = np.zeros((self.batch_size, self.batch_length),
                               dtype=np.int32)
        target_batch = np.zeros((self.batch_size, self.batch_length),
                                dtype=np.int32)
        for i, start_idx in enumerate(start_idxs):
            inpt, trgt = self.get_input_target_sample(start_idx)
            input_batch[i, :] = inpt
            target_batch[i, :] = trgt
        return input_batch, target_batch

    def __iter__(self):
        while True:
            input_batch, target_batch = self.get_batch(self.start_idxs)
            self.start_idxs = (
                self.start_idxs + self.batch_length) % self.data_length
            yield input_batch, target_batch


filepath = './tmp_wap.txt'
batch_length = 10
batch_size = 2
reader = DataReader(filepath, batch_length, batch_size)
s = 'As in the question of astronomy then, so in the question of history now,'
print([reader.char_dict[c] for c in s])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#model

import codecs
import locale

#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
#tensorflow2下使用tensorflow1的方法

class Model(object):
    """RNN language model."""
    def __init__(self, batch_size, sequence_length, lstm_sizes, dropout,
                 labels, save_path):
        self.batch_size = batch_size
        self.sequence_length = sequence_length
        self.lstm_sizes = lstm_sizes
        self.labels = labels
        self.label_map = {val: idx for idx, val in enumerate(labels)}
        self.number_of_characters = len(labels)
        self.save_path = save_path
        self.dropout = dropout

    def init_graph(self):
        # Variable sequence length
        self.inputs = tf.placeholder(
            tf.int32, [self.batch_size, self.sequence_length])
        self.targets = tf.placeholder(
            tf.int32, [self.batch_size, self.sequence_length])
        self.init_architecture()
        self.saver = tf.train.Saver(tf.trainable_variables())

    def init_architecture(self):
        # Define a multilayer LSTM cell
        self.one_hot_inputs = tf.one_hot(
            self.inputs, depth=self.number_of_characters)
        cell_list = [tf.nn.rnn_cell.LSTMCell(lstm_size, state_is_tuple=True)
                     for lstm_size in self.lstm_sizes]
        self.multi_cell_lstm = tf.nn.rnn_cell.MultiRNNCell(
            cell_list, state_is_tuple=True)
        # Initial state of the LSTM memory.
        # Keep state in graph memory to use between batches
        self.initial_state = self.multi_cell_lstm.zero_state(
            self.batch_size, tf.float32)
        # Convert to variables so that the state can be stored between batches
        # Note that LSTM states is a tuple of tensors, this structure has to be
        # re-created in order to use as LSTM state.
        self.state_variables = tf.python.util.nest.pack_sequence_as(
            self.initial_state,
            [tf.Variable(var, trainable=False)
             for var in tf.python.util.nest.flatten(self.initial_state)])
        # Define the rnn through time
        lstm_output, final_state = tf.nn.dynamic_rnn(
            cell=self.multi_cell_lstm, inputs=self.one_hot_inputs,
            initial_state=self.state_variables)
        # Force the initial state to be set to the new state for the next batch
        # before returning the output
        store_states = [
            state_variable.assign(new_state)
            for (state_variable, new_state) in zip(
                tf.python.util.nest.flatten(self.state_variables),
                tf.python.util.nest.flatten(final_state))]
        with tf.control_dependencies(store_states):
            lstm_output = tf.identity(lstm_output)
        # Reshape so that we can apply the linear transformation to all outputs
        output_flat = tf.reshape(lstm_output, (-1, self.lstm_sizes[-1]))
        # Define output layer
        self.logit_weights = tf.Variable(
            tf.truncated_normal(
                (self.lstm_sizes[-1], self.number_of_characters), stddev=0.01),
            name='logit_weights')
        self.logit_bias = tf.Variable(
            tf.zeros((self.number_of_characters)), name='logit_bias')
        # Apply last layer transformation
        self.logits_flat = tf.matmul(
            output_flat, self.logit_weights) + self.logit_bias
        probabilities_flat = tf.nn.softmax(self.logits_flat)
        self.probabilities = tf.reshape(
            probabilities_flat,
            (self.batch_size, -1, self.number_of_characters))

    def init_train_op(self, optimizer):
        # Flatten the targets to be compatible with the flattened logits
        targets_flat = tf.reshape(self.targets, (-1, ))
        # Get the loss over all outputs
        loss = tf.nn.sparse_softmax_cross_entropy_with_logits(
            self.logits_flat, targets_flat, name='x_entropy')
        self.loss = tf.reduce_mean(loss)
        trainable_variables = tf.trainable_variables()
        gradients = tf.gradients(loss, trainable_variables)
        gradients, _ = tf.clip_by_global_norm(
            gradients, 5)
        self.train_op = optimizer.apply_gradients(
            zip(gradients, trainable_variables))

    def sample(self, session, prime_string, sample_length):
        self.reset_state(session)
        # Prime state
        print('prime_string: ', prime_string)
        for character in prime_string:
            character_idx = self.label_map[character]
            out = session.run(
                self.probabilities,
                feed_dict={self.inputs: np.asarray([[character_idx]])})
            sample_label = np.random.choice(
                self.labels, size=(1),  p=out[0, 0])
        output_sample = prime_string
        print('start sampling')
        # Sample for sample_length steps
        for _ in range(sample_length):
            sample_label = np.random.choice(
                self.labels, size=(1),  p=out[0, 0])[0]
            output_sample += sample_label
            sample_idx = self.label_map[sample_label]
            out = session.run(
                self.probabilities,
                feed_dict={self.inputs: np.asarray([[sample_idx]])})
        return output_sample

    def reset_state(self, session):
        for state in tf.python.util.nest.flatten(self.state_variables):
            session.run(state.initializer)

    def save(self, sess):
        self.saver.save(sess, self.save_path)

    def restore(self, sess):
        self.saver.restore(sess, self.save_path)


def train_and_sample(minibatch_iterations, restore):
    #tf.reset_default_graph()
    batch_size = 64
    lstm_sizes = [512, 512]
    batch_len = 100
    learning_rate = 2e-3

    filepath = './tmp_wap.txt'

    # NG 以下 fail
    data_feed = DataReader(filepath, batch_len, batch_size)
    labels = data_feed.char_list
    print('labels: ', labels)

    save_path = './model.tf'
    model = Model(
        batch_size, batch_len, lstm_sizes, 0.8, labels,
        save_path)
    model.init_graph()
    optimizer = tf.train.AdamOptimizer(learning_rate)
    model.init_train_op(optimizer)

    init_op = tf.initialize_all_variables()
    with tf.Session() as sess:
        sess.run(init_op)
        if restore:
            print('Restoring model')
            model.restore(sess)
        model.reset_state(sess)
        start_time = time.time()
        for i in range(minibatch_iterations):
            input_batch, target_batch = next(iter(data_feed))
            loss, _ = sess.run(
                [model.loss, model.train_op],
                feed_dict={
                    model.inputs: input_batch, model.targets: target_batch})
            if i % 50 == 0 and i != 0:
                print('i: ', i)
                duration = time.time() - start_time
                print('loss: {} ({} sec.)'.format(loss, duration))
                start_time = time.time()
            if i % 1000 == 0 and i != 0:
                model.save(sess)
            if i % 100 == 0 and i != 0:
                print('Reset initial state')
                model.reset_state(sess)
            if i % 1000 == 0 and i != 0:
                print('Reset minibatch feeder')
                data_feed.reset_indices()
        model.save(sess)

    print('\n sampling after {} iterations'.format(minibatch_iterations))
    tf.reset_default_graph()
    model = Model(
        1, None, lstm_sizes, 1.0, labels, save_path)
    model.init_graph()
    init_op = tf.initialize_all_variables()
    with tf.Session() as sess:
        sess.run(init_op)
        model.restore(sess)
        print('\nSample 1:')
        sample = model.sample(
            sess, prime_string=u'\n\nThis feeling was ', sample_length=500)
        print(u'sample: \n{}'.format(sample))
        print('\nSample 2:')
        sample = model.sample(
            sess, prime_string=u'She was born in the year ', sample_length=500)
        print(u'sample: \n{}'.format(sample))
        print('\nSample 3:')
        sample = model.sample(
            sess, prime_string=u'The meaning of this all is ',
            sample_length=500)
        print(u'sample: \n{}'.format(sample))
        print('\nSample 4:')
        sample = model.sample(
            sess,
            prime_string=u'In the midst of a conversation on political matters Anna Pávlovna burst out:,',
            sample_length=500)
        print(u'sample: \n{}'.format(sample))
        print('\nSample 5:')
        sample = model.sample(
            sess, prime_string=u'\n\nCHAPTER X\n\n',
            sample_length=500)
        print(u'sample: \n{}'.format(sample))
        print('\nSample 5:')
        sample = model.sample(
            sess, prime_string=u'"If only you knew,"',
            sample_length=500)
        print(u'sample: \n{}'.format(sample))


total_iterations = 500
print('\n\n\nTrain for {}'.format(500))
print('Total iters: {}'.format(total_iterations))

""" NG
train_and_sample(500, restore=False)
for i in [500, 1000, 3000, 5000, 10000, 30000, 50000, 100000, 300000]:
    total_iterations += i
    print('\n\n\nTrain for {}'.format(i))
    print('Total iters: {}'.format(total_iterations))
    train_and_sample(i, restore=True)
"""

print("------------------------------------------------------------")  # 60個
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
sys.exit()



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

