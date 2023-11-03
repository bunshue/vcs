import os
import sys
import time
import random

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

print('------------------------------------------------------------')	#60個

import numpy as np

from sklearn.datasets import make_regression

X,y =make_regression(n_samples=100, n_features=3)

print(X.shape ,y.shape)

y=y.reshape((-1,1))

#(100, 3) (100,)

import matplotlib.pyplot as plt

plt.figure(figsize=(9,4))

plt.plot(y,alpha=0.5,linewidth=3)

plt.show()

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X,y)

y_pred_sk = model.predict(X)

plt.figure(figsize=(9,4))

plt.plot(y, color = 'r')
plt.plot(y,alpha=0.8,linewidth=5 )

plt.plot(y_pred_sk, color = 'g')
plt.plot(y_pred_sk ,linewidth=1)

plt.legend()

plt.show()

def gd(X, y, theta, l_rate, iterations): 

    cost_history = [0] * iterations

    m = X.shape[0]

    for epoch in range(iterations):

        y_hat = X.dot(theta)

        loss = y_hat - y

        gradient = X.T.dot(loss)/m

        theta = theta - l_rate * gradient

        cost = np.dot(loss.T,loss)

        cost_history[epoch] = cost[0,0]

    return theta, cost_history

def sgd(X,y,theta, l_rate,iterations):

    cost_history =[0] * iterations

    for epoch in range(iterations):

        for i,row in enumerate(X):

            yhat = np.dot(row,theta)

            loss = yhat[0] - y[i]          

            theta = theta - l_rate  * loss * row.reshape((-1,1))

            cost_history[epoch] += loss ** 2

    return theta,cost_history

def predict(X,theta):

    return np.dot(X,theta)

theta = np.random.rand(X.shape[1],1)

iterations = 100

l_rate = 0.1

theta,cost_history = gd(X,y,theta,l_rate,iterations)

print(theta.T)

#array([[ 1.12259549, 64.22439151, 84.34968956]])

y_predict = predict(X,theta)

import seaborn as sns

y_predict = predict(X,theta)

plt.figure(figsize=(9,4))

plt.plot(y, color = 'r')
plt.plot(y,alpha=0.3,linewidth=5)
plt.plot(y_predict, color = 'g')
plt.plot(y_predict,linewidth= 2)
plt.show()

print(model.coef_)

#array([[48.54597102, 82.31351886,  8.52184984]])

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


