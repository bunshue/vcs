"""


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

#第十讲 使用神经网络进行客户流失预警

from scipy import stats
import sklearn.cross_validation as cross_validation
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = pd.read_csv('telecom_churn.csv')
data.head()

#随机抽样，建立训练集与测试集

train, test = cross_validation.train_test_split(data, test_size=1000)

from sklearn import preprocessing

#进行极差标准化
train_X = train.ix[:, 0:-1]
test_X = test.ix[:, 0:-1]
scaler = preprocessing.MinMaxScaler().fit(train_X)
train_X = scaler.transform(train_X)
test_X = scaler.transform(test_X)
train_Y = train['churn'].get_values().reshape(2463, 1)   # 为满足后续(pybrain)建模需要做相应变换
test_Y = test['churn'].get_values().reshape(1000, 1)

# 使用pybrain的快捷方式创建神经网络，默认激发函数为sigmoid，带bias, 全连接

from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import SigmoidLayer, LinearLayer

net = buildNetwork(24, 24, 1, hiddenclass=SigmoidLayer, outclass=LinearLayer)
print(net.modules)

# 构建适用于神经网络的训练和测试的数据集ClassificationDataSet

from pybrain.datasets import ClassificationDataSet

ds_train = ClassificationDataSet(24, target=1, nb_classes=2)
ds_test = ClassificationDataSet(24, target=1, nb_classes=2)
ds_train.setField('input', train_X)
ds_train.setField('target', train_Y)
ds_test.setField('input', test_X)
ds_test.setField('target', test_Y)
print(ds_train.calculateStatistics(), '\n', ds_test.calculateStatistics())

from pybrain.supervised.trainers import BackpropTrainer

trainer = BackpropTrainer(module=net, dataset=ds_train, learningrate=0.01, lrdecay=1.0, momentum=0., weightdecay=0.01)
for i in range(10):
    print(trainer.train())

trainer.trainUntilConvergence(maxEpochs=20, validationProportion=0.25)

pred = net.activateOnDataset(ds_test)

from pybrain.tools.validation import Validator

Validator.classificationPerformance(map(lambda x: 1 if x > 0.5 else 0, pred), test['y'].get_values())

zip(map(lambda x: 1 if x > 0.5 else 0, pred), test['y'].get_values())

# 构建网络的一般形式

from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection

# Initialize a neural network
nnet = FeedForwardNetwork()

# Create layers
inLayer = LinearLayer(24, name='in')  # 设置默认参数"name='in'"仅为了方便, inLayer 等同于 nnet['in']
hiddenLayer = SigmoidLayer(5, name='hidden')
outLayer = LinearLayer(1, name='out')

# Vreate connections
in_to_hidden = FullConnection(inLayer, hiddenLayer, name='in_to_hidden')
hidden_to_out = FullConnection(hiddenLayer, outLayer, name='hidden_to_out')

# Add layers and connections to neural network
nnet.addInputModule(inLayer)
nnet.addModule(hiddenLayer)
nnet.addOutputModule(outLayer)
nnet.addConnection(in_to_hidden)
nnet.addConnection(hidden_to_out)

# Make nnet usable
nnet.sortModules()

# Check it
print(nnet)

# Setup a trainer
ntrainer = BackpropTrainer(module=nnet, dataset=ds_train, learningrate=0.01, lrdecay=1., momentum=0., weightdecay=0.01)

ntrainer.trainUntilConvergence(maxEpochs=20, validationProportion=0.25)

pred1 = nnet.activateOnDataset(ds_test)
Validator.classificationPerformance(map(lambda x: 1 if x > 0.5 else 0, pred1), test['y'].get_values())

from pybrain.tools.validation import CrossValidator, ModuleValidator

CV = CrossValidator(ntrainer, ds_train, n_folds=5, valfunc=ModuleValidator.MSE)
CV.validate()

# 使用分类器

from pybrain.tools.neuralnets import NNclassifier

nclf = NNclassifier(ds_train, TDS=ds_test, maxepochs=100)
nclf.setupNN(trainer=BackpropTrainer, hidden=1, learningrate=0.01, lrdecay=1.0, momentum=0., weightdecay=0.01)
nclf.runTraining(convergence=0)

# nclf.saveNetwork('nnet_classifier')



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

