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

"""
sepal:【植】萼片
"""

from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from matplotlib.colors import ListedColormap

#Apply standardization
standardised = True

M = {0:"sepal length", 1:"sepal width", 2:"petal length", 3:"petal width"}

#Choose two features
x=1 #1 corresponds to the sepal width
y=3 #3 corresponds to the petal width

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
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

