"""
machine_learning_ch10

全都是有用到 theano 的

檔案mnist.pkl.gz放在big_files

mnist_filename = "D:/_git/vcs/_big_files/mnist.pkl.gz"

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# from common1 import *
import scipy
import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_moons
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA  # KernelPCA 萃取特徵

from matplotlib.colors import ListedColormap
from sklearn.preprocessing import MinMaxScaler
from sklearn import tree


def show():
    # plt.show()
    pass


from time import perf_counter

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# convolutional_mlp.py

"""This tutorial introduces the LeNet5 neural network architecture
using Theano.  LeNet5 is a convolutional neural network, good for
classifying images. This tutorial shows how to build the architecture,
and comes with all the hyper-parameters you need to reproduce the
paper's MNIST results.


This implementation simplifies the model in the following ways:

 - LeNetConvPool doesn't implement location-specific gain and bias parameters
 - LeNetConvPool doesn't implement pooling by average, it implements pooling
   by max.
 - Digit classification is implemented with a logistic regression rather than
   an RBF network
 - LeNet5 was not fully-connected convolutions at second layer

References:
 - Y. LeCun, L. Bottou, Y. Bengio and P. Haffner:
   Gradient-Based Learning Applied to Document
   Recognition, Proceedings of the IEEE, 86(11):2278-2324, November 1998.
   http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf

"""
import os
import sys
import time

import numpy

import theano
import theano.tensor as T
from theano.tensor.signal import downsample
from theano.tensor.nnet import conv
from logistic_sgd import LogisticRegression, load_data
from mlp import HiddenLayer

""" 
���+�²����ϳ�һ����LeNetConvPoolLayer 
rng:����������������ڳ�ʼ��W 
input:4ά��������theano.tensor.dtensor4 
filter_shape:(number of filters, num input feature maps,filter height, filter width) 
image_shape:(batch size, num input feature maps,image height, image width) 
poolsize: (#rows, #cols) 
"""


class LeNetConvPoolLayer(object):
    def __init__(self, rng, input, filter_shape, image_shape, poolsize=(2, 2)):
        # assert condition��conditionΪTrue�����������ִ�У�conditionΪFalse���жϳ���
        # image_shape[1]��filter_shape[1]����num input feature maps�����Ǳ�����һ���ġ�
        assert image_shape[1] == filter_shape[1]
        self.input = input
        # ÿ��������Ԫ�������أ�����һ���������Ϊnum input feature maps * filter height * filter width��
        # ������numpy.prod(filter_shape[1:])�����
        fan_in = numpy.prod(filter_shape[1:])
        # lower layer��ÿ����Ԫ��õ��ݶ������ڣ�"num output feature maps * filter height * filter width" /pooling size
        fan_out = filter_shape[0] * numpy.prod(filter_shape[2:]) / numpy.prod(poolsize)
        # �������fan_in��fan_out �������Ǵ��빫ʽ���Դ��������ʼ��W,W�������Ծ����
        W_bound = numpy.sqrt(6.0 / (fan_in + fan_out))
        self.W = theano.shared(
            numpy.asarray(
                rng.uniform(low=-W_bound, high=W_bound, size=filter_shape),
                dtype=theano.config.floatX,
            ),
            borrow=True,
        )
        # ƫ��b��һά������ÿ�����ͼ������ͼ����Ӧһ��ƫ�ã�
        # �����������ͼ�ĸ�����filter���������������filter_shape[0]��number of filters����ʼ��
        b_values = numpy.zeros((filter_shape[0],), dtype=theano.config.floatX)
        self.b = theano.shared(value=b_values, borrow=True)
        # ������ͼ����filter�����conv.conv2d����
        # �����û�м�b��ͨ��sigmoid��������һ���򻯡�
        conv_out = conv.conv2d(
            input=input,
            filters=self.W,
            filter_shape=filter_shape,
            image_shape=image_shape,
        )
        # maxpooling������Ӳ�������
        pooled_out = downsample.max_pool_2d(
            input=conv_out, ds=poolsize, ignore_border=True
        )
        # ��ƫ�ã���ͨ��tanhӳ�䣬�õ����+�Ӳ�������������
        self.output = T.tanh(pooled_out + self.b.dimshuffle("x", 0, "x", "x"))
        # ���+������Ĳ���
        self.params = [self.W, self.b]

    # �洢ִ�в���
    def save_net(self, path):
        import pickle

        write_file = open(path, "wb")
        pickle.dump(self.params, write_file, -1)
        write_file.close()


# ʵ��LeNet5 ��LeNet5����������㣬��һ���������20������ˣ��ڶ����������50�������
# learning_rate:ѧϰ���ʣ�����ݶ�ǰ��ϵ����
# n_epochsѵ��������ÿһ�������������batch������������
# batch_size,��������Ϊ500����ÿ������500���������ż����ݶȲ����²���
# nkerns=[20, 50],ÿһ��LeNetConvPoolLayer����˵ĸ�������һ��LeNetConvPoolLayer��
# 20������ˣ��ڶ�����50��
def evaluate_lenet5(
    learning_rate=0.1,
    n_epochs=200,
    dataset="mnist.pkl.gz",
    nkerns=[20, 50],
    batch_size=500,
):
    rng = numpy.random.RandomState(23455)
    datasets = load_data(dataset)  # ��������
    train_set_x, train_set_y = datasets[0]
    valid_set_x, valid_set_y = datasets[1]
    test_set_x, test_set_y = datasets[2]

    n_train_batches = train_set_x.get_value(borrow=True).shape[0]
    n_valid_batches = valid_set_x.get_value(borrow=True).shape[0]
    n_test_batches = test_set_x.get_value(borrow=True).shape[0]
    n_train_batches /= batch_size
    n_valid_batches /= batch_size
    n_test_batches /= batch_size
    # ���弸��������index��ʾbatch�±꣬x��ʾ�����ѵ�����ݣ�y��Ӧ���ǩ
    index = T.lscalar()
    x = T.matrix("x")
    y = T.ivector("y")
    ############
    # ����ģ�� #
    ############
    print("... building the model")
    # ���Ǽ��ؽ�����batch��С��������(batch_size, 28 * 28)������LeNetConvPoolLayer����������ά�ģ�����Ҫreshape
    layer0_input = x.reshape((batch_size, 1, 28, 28))
    # layer0����һ��LeNetConvPoolLayer��
    # ����ĵ���ͼƬ(28,28)������conv�õ�(28-5+1 , 28-5+1) = (24, 24)��
    # ����maxpooling�õ�(24/2, 24/2) = (12, 12)
    # ��Ϊÿ��batch��batch_size��ͼ����һ��LeNetConvPoolLayer����nkerns[0]������ˣ�
    # ��layer0���Ϊ(batch_size, nkerns[0], 12, 12)
    layer0 = LeNetConvPoolLayer(
        rng,
        input=layer0_input,
        image_shape=(batch_size, 1, 28, 28),
        filter_shape=(nkerns[0], 1, 5, 5),
        poolsize=(2, 2),
    )
    # layer1���ڶ���LeNetConvPoolLayer��
    # ������layer0�������ÿ������ͼΪ(12,12),����conv�õ�(12-5+1, 12-5+1) = (8, 8),
    # ����maxpooling�õ�(8/2, 8/2) = (4, 4)
    # ��Ϊÿ��batch��batch_size��ͼ������ͼ�����ڶ���LeNetConvPoolLayer����nkerns[1]�������
    # ����layer1���Ϊ(batch_size, nkerns[1], 4, 4)
    layer1 = LeNetConvPoolLayer(
        rng,
        input=layer0.output,
        image_shape=(batch_size, nkerns[0], 12, 12),
        filter_shape=(nkerns[1], nkerns[0], 5, 5),
        poolsize=(2, 2),
    )
    # ǰ�涨���������LeNetConvPoolLayer��layer0��layer1����layer1�����layer2������һ��ȫ���Ӳ㣬�൱��MLP�����������
    # �ʿ�����MLP�ж����HiddenLayer����ʼ��layer2��layer2�������Ƕ�ά��(batch_size, num_pixels) ��
    # ��Ҫ���ϲ���ͬһ��ͼ����ͬ����˾������������ͼ�ϲ�Ϊһά������
    # Ҳ���ǽ�layer1�����(batch_size, nkerns[1], 4, 4)flattenΪ(batch_size, nkerns[1]*4*4)=(500��800),��Ϊlayer2�����롣
    # (500��800)��ʾ��500��������ÿһ�д���һ��������layer2�������С��(batch_size,n_out)=(500,500)
    layer2_input = layer1.output.flatten(2)
    layer2 = HiddenLayer(
        rng, input=layer2_input, n_in=nkerns[1] * 4 * 4, n_out=500, activation=T.tanh
    )
    # ���һ��layer3�Ƿ���㣬�õ����߼��ع��ж����LogisticRegression��
    # layer3��������layer2�����(500,500)��layer3���������(batch_size,n_out)=(500,10)
    layer3 = LogisticRegression(input=layer2.output, n_in=500, n_out=10)
    # ���ۺ���NLL
    cost = layer3.negative_log_likelihood(y)
    # test_model���������x��y���ݸ�����index���廯��Ȼ�����layer3��
    # layer3�ֻ����ص���layer2��layer1��layer0����test_model��ʵ��������CNN�ṹ��
    # test_model��������x��y�������layer3.errors(y)�����������
    test_model = theano.function(
        [index],
        layer3.errors(y),
        givens={
            x: test_set_x[index * batch_size : (index + 1) * batch_size],
            y: test_set_y[index * batch_size : (index + 1) * batch_size],
        },
    )
    validate_model = theano.function(
        [index],
        layer3.errors(y),
        givens={
            x: valid_set_x[index * batch_size : (index + 1) * batch_size],
            y: valid_set_y[index * batch_size : (index + 1) * batch_size],
        },
    )
    # ������train_model���漰���Ż��㷨��SGD����Ҫ�����ݶȡ����²���
    params = layer3.params + layer2.params + layer1.params + layer0.params  # ������
    grads = T.grad(cost, params)  # �Ը����������ݶ�
    # ��Ϊ����̫�࣬��updates��������һ��һ�������д�����Ǻ��鷳�ģ�
    # ������������һ��for..in..,�Զ����ɹ����(param_i, param_i - learning_rate * grad_i)
    updates = [
        (param_i, param_i - learning_rate * grad_i)
        for param_i, grad_i in zip(params, grads)
    ]
    # train_model���������ͬtest_model��train_model���test_model��validation_model���updates����
    train_model = theano.function(
        [index],
        cost,
        updates=updates,
        givens={
            x: train_set_x[index * batch_size : (index + 1) * batch_size],
            y: train_set_y[index * batch_size : (index + 1) * batch_size],
        },
    )

    print("... training")
    patience = 10000  # ������ֹ����
    patience_increase = 2
    improvement_threshold = 0.995

    validation_frequency = min(n_train_batches, patience / 2)
    best_validation_loss = numpy.inf
    best_iter = 0
    test_score = 0.0
    start_time = perf_counter()
    epoch = 0
    done_looping = False
    while (epoch < n_epochs) and (not done_looping):
        epoch = epoch + 1
        for minibatch_index in xrange(n_train_batches):
            iter = (epoch - 1) * n_train_batches + minibatch_index
            if iter % 100 == 0:
                print("training @ iter = ", iter)
            cost_ij = train_model(minibatch_index)
            if (iter + 1) % validation_frequency == 0:
                validation_losses = [validate_model(i) for i in xrange(n_valid_batches)]
                this_validation_loss = numpy.mean(validation_losses)
                print(
                    "epoch %i, minibatch %i/%i, validation error %f %%"
                    % (
                        epoch,
                        minibatch_index + 1,
                        n_train_batches,
                        this_validation_loss * 100.0,
                    )
                )
                if this_validation_loss < best_validation_loss:
                    if (
                        this_validation_loss
                        < best_validation_loss * improvement_threshold
                    ):
                        patience = max(patience, iter * patience_increase)
                    best_validation_loss = this_validation_loss
                    best_iter = iter
                    test_losses = [test_model(i) for i in xrange(n_test_batches)]
                    test_score = numpy.mean(test_losses)
                    print(
                        (
                            "     epoch %i, minibatch %i/%i, test error of "
                            "best model %f %%"
                        )
                        % (
                            epoch,
                            minibatch_index + 1,
                            n_train_batches,
                            test_score * 100.0,
                        )
                    )

            if patience <= iter:
                done_looping = True
                break
    layer0.save_net("layer0")
    layer1.save_net("layer1")
    layer2.save_net("layer2")
    layer3.save_net("layer3")
    end_time = perf_counter()
    print("Optimization complete.")
    print(
        "Best validation score of %f %% obtained at iteration %i, "
        "with test performance %f %%"
        % (best_validation_loss * 100.0, best_iter + 1, test_score * 100.0)
    )
    # print(>> sys.stderr, ('The code for file ' + os.path.split(__file__)[1] + ' ran for %.2fm' % ((end_time - start_time) / 60.)))


if __name__ == "__main__":
    evaluate_lenet5()


def experiment(state, channel):
    evaluate_lenet5(state.learning_rate, dataset=state.dataset)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# DBN.py

import numpy

import theano
import theano.tensor as T
from theano.tensor.shared_randomstreams import RandomStreams

from logistic_sgd import LogisticRegression, load_data
from mlp import HiddenLayer
from rbm import RBM


# start-snippet-1
class DBN(object):
    """Deep Belief Network

    A deep belief network is obtained by stacking several RBMs on top of each
    other. The hidden layer of the RBM at layer `i` becomes the input of the
    RBM at layer `i+1`. The first layer RBM gets as input the input of the
    network, and the hidden layer of the last RBM represents the output. When
    used for classification, the DBN is treated as a MLP, by adding a logistic
    regression layer on top.
    """

    def __init__(
        self,
        numpy_rng,
        theano_rng=None,
        n_ins=784,
        hidden_layers_sizes=[500, 500],
        n_outs=10,
    ):
        """This class is made to support a variable number of layers.

        :type numpy_rng: numpy.random.RandomState
        :param numpy_rng: numpy random number generator used to draw initial
                    weights

        :type theano_rng: theano.tensor.shared_randomstreams.RandomStreams
        :param theano_rng: Theano random generator; if None is given one is
                           generated based on a seed drawn from `rng`

        :type n_ins: int
        :param n_ins: dimension of the input to the DBN

        :type hidden_layers_sizes: list of ints
        :param hidden_layers_sizes: intermediate layers size, must contain
                               at least one value

        :type n_outs: int
        :param n_outs: dimension of the output of the network
        """

        self.sigmoid_layers = []
        self.rbm_layers = []
        self.params = []
        self.n_layers = len(hidden_layers_sizes)

        assert self.n_layers > 0

        if not theano_rng:
            theano_rng = RandomStreams(numpy_rng.randint(2**30))

        # allocate symbolic variables for the data
        self.x = T.matrix("x")  # the data is presented as rasterized images
        self.y = T.ivector("y")  # the labels are presented as 1D vector
        # of [int] labels
        # end-snippet-1
        # The DBN is an MLP, for which all weights of intermediate
        # layers are shared with a different RBM.  We will first
        # construct the DBN as a deep multilayer perceptron, and when
        # constructing each sigmoidal layer we also construct an RBM
        # that shares weights with that layer. During pretraining we
        # will train these RBMs (which will lead to chainging the
        # weights of the MLP as well) During finetuning we will finish
        # training the DBN by doing stochastic gradient descent on the
        # MLP.

        for i in range(self.n_layers):
            # construct the sigmoidal layer

            # the size of the input is either the number of hidden
            # units of the layer below or the input size if we are on
            # the first layer
            if i == 0:
                input_size = n_ins
            else:
                input_size = hidden_layers_sizes[i - 1]

            # the input to this layer is either the activation of the
            # hidden layer below or the input of the DBN if you are on
            # the first layer
            if i == 0:
                layer_input = self.x
            else:
                layer_input = self.sigmoid_layers[-1].output

            sigmoid_layer = HiddenLayer(
                rng=numpy_rng,
                input=layer_input,
                n_in=input_size,
                n_out=hidden_layers_sizes[i],
                activation=T.nnet.sigmoid,
            )

            # add the layer to our list of layers
            self.sigmoid_layers.append(sigmoid_layer)

            # its arguably a philosophical question...  but we are
            # going to only declare that the parameters of the
            # sigmoid_layers are parameters of the DBN. The visible
            # biases in the RBM are parameters of those RBMs, but not
            # of the DBN.
            self.params.extend(sigmoid_layer.params)

            # Construct an RBM that shared weights with this layer
            rbm_layer = RBM(
                numpy_rng=numpy_rng,
                theano_rng=theano_rng,
                input=layer_input,
                n_visible=input_size,
                n_hidden=hidden_layers_sizes[i],
                W=sigmoid_layer.W,
                hbias=sigmoid_layer.b,
            )
            self.rbm_layers.append(rbm_layer)

        # We now need to add a logistic layer on top of the MLP
        self.logLayer = LogisticRegression(
            input=self.sigmoid_layers[-1].output,
            n_in=hidden_layers_sizes[-1],
            n_out=n_outs,
        )
        self.params.extend(self.logLayer.params)

        # compute the cost for second phase of training, defined as the
        # negative log likelihood of the logistic regression (output) layer
        self.finetune_cost = self.logLayer.negative_log_likelihood(self.y)

        # compute the gradients with respect to the model parameters
        # symbolic variable that points to the number of errors made on the
        # minibatch given by self.x and self.y
        self.errors = self.logLayer.errors(self.y)

    def pretraining_functions(self, train_set_x, batch_size, k):
        """Generates a list of functions, for performing one step of
        gradient descent at a given layer. The function will require
        as input the minibatch index, and to train an RBM you just
        need to iterate, calling the corresponding function on all
        minibatch indexes.

        :type train_set_x: theano.tensor.TensorType
        :param train_set_x: Shared var. that contains all datapoints used
                            for training the RBM
        :type batch_size: int
        :param batch_size: size of a [mini]batch
        :param k: number of Gibbs steps to do in CD-k / PCD-k

        """

        # index to a [mini]batch
        index = T.lscalar("index")  # index to a minibatch
        learning_rate = T.scalar("lr")  # learning rate to use

        # number of batches
        n_batches = train_set_x.get_value(borrow=True).shape[0] / batch_size
        # begining of a batch, given `index`
        batch_begin = index * batch_size
        # ending of a batch given `index`
        batch_end = batch_begin + batch_size

        pretrain_fns = []
        for rbm in self.rbm_layers:
            # get the cost and the updates list
            # using CD-k here (persisent=None) for training each RBM.
            # TODO: change cost function to reconstruction error
            cost, updates = rbm.get_cost_updates(learning_rate, persistent=None, k=k)

            # compile the theano function
            fn = theano.function(
                inputs=[index, theano.Param(learning_rate, default=0.1)],
                outputs=cost,
                updates=updates,
                givens={self.x: train_set_x[batch_begin:batch_end]},
            )
            # append `fn` to the list of functions
            pretrain_fns.append(fn)

        return pretrain_fns

    def build_finetune_functions(self, datasets, batch_size, learning_rate):
        """Generates a function `train` that implements one step of
        finetuning, a function `validate` that computes the error on a
        batch from the validation set, and a function `test` that
        computes the error on a batch from the testing set

        :type datasets: list of pairs of theano.tensor.TensorType
        :param datasets: It is a list that contain all the datasets;
                        the has to contain three pairs, `train`,
                        `valid`, `test` in this order, where each pair
                        is formed of two Theano variables, one for the
                        datapoints, the other for the labels
        :type batch_size: int
        :param batch_size: size of a minibatch
        :type learning_rate: float
        :param learning_rate: learning rate used during finetune stage

        """

        (train_set_x, train_set_y) = datasets[0]
        (valid_set_x, valid_set_y) = datasets[1]
        (test_set_x, test_set_y) = datasets[2]

        # compute number of minibatches for training, validation and testing
        n_valid_batches = valid_set_x.get_value(borrow=True).shape[0]
        n_valid_batches /= batch_size
        n_test_batches = test_set_x.get_value(borrow=True).shape[0]
        n_test_batches /= batch_size

        index = T.lscalar("index")  # index to a [mini]batch

        # compute the gradients with respect to the model parameters
        gparams = T.grad(self.finetune_cost, self.params)

        # compute list of fine-tuning updates
        updates = []
        for param, gparam in zip(self.params, gparams):
            updates.append((param, param - gparam * learning_rate))

        train_fn = theano.function(
            inputs=[index],
            outputs=self.finetune_cost,
            updates=updates,
            givens={
                self.x: train_set_x[index * batch_size : (index + 1) * batch_size],
                self.y: train_set_y[index * batch_size : (index + 1) * batch_size],
            },
        )

        test_score_i = theano.function(
            [index],
            self.errors,
            givens={
                self.x: test_set_x[index * batch_size : (index + 1) * batch_size],
                self.y: test_set_y[index * batch_size : (index + 1) * batch_size],
            },
        )

        valid_score_i = theano.function(
            [index],
            self.errors,
            givens={
                self.x: valid_set_x[index * batch_size : (index + 1) * batch_size],
                self.y: valid_set_y[index * batch_size : (index + 1) * batch_size],
            },
        )

        # Create a function that scans the entire validation set
        def valid_score():
            return [valid_score_i(i) for i in range(n_valid_batches)]

        # Create a function that scans the entire test set
        def test_score():
            return [test_score_i(i) for i in range(n_test_batches)]

        return train_fn, valid_score, test_score


def test_DBN(
    finetune_lr=0.1,
    pretraining_epochs=100,
    pretrain_lr=0.01,
    k=1,
    training_epochs=1000,
    dataset="mnist.pkl.gz",
    batch_size=10,
):
    """
    Demonstrates how to train and test a Deep Belief Network.

    This is demonstrated on MNIST.

    :type finetune_lr: float
    :param finetune_lr: learning rate used in the finetune stage
    :type pretraining_epochs: int
    :param pretraining_epochs: number of epoch to do pretraining
    :type pretrain_lr: float
    :param pretrain_lr: learning rate to be used during pre-training
    :type k: int
    :param k: number of Gibbs steps in CD/PCD
    :type training_epochs: int
    :param training_epochs: maximal number of iterations ot run the optimizer
    :type dataset: string
    :param dataset: path the the pickled dataset
    :type batch_size: int
    :param batch_size: the size of a minibatch
    """

    datasets = load_data(dataset)

    train_set_x, train_set_y = datasets[0]
    valid_set_x, valid_set_y = datasets[1]
    test_set_x, test_set_y = datasets[2]

    # compute number of minibatches for training, validation and testing
    n_train_batches = train_set_x.get_value(borrow=True).shape[0] / batch_size

    # numpy random generator
    numpy_rng = numpy.random.RandomState(123)
    print("... building the model")
    # construct the Deep Belief Network
    dbn = DBN(
        numpy_rng=numpy_rng,
        n_ins=28 * 28,
        hidden_layers_sizes=[1000, 1000, 1000],
        n_outs=10,
    )

    # start-snippet-2
    #########################
    # PRETRAINING THE MODEL #
    #########################
    print("... getting the pretraining functions")
    pretraining_fns = dbn.pretraining_functions(
        train_set_x=train_set_x, batch_size=batch_size, k=k
    )

    print("... pre-training the model")
    start_time = perf_counter()
    ## Pre-train layer-wise
    for i in range(dbn.n_layers):
        # go through pretraining epochs
        for epoch in range(pretraining_epochs):
            # go through the training set
            c = []
            for batch_index in range(n_train_batches):
                c.append(pretraining_fns[i](index=batch_index, lr=pretrain_lr))
            print(
                "Pre-training layer %i, epoch %d, cost " % (i, epoch),
            )
            print(numpy.mean(c))

    end_time = perf_counter()
    # end-snippet-2
    """
    print(>> sys.stderr, ('The pretraining code for file ' +
                          os.path.split(__file__)[1] +
                          ' ran for %.2fm' % ((end_time - start_time) / 60.)))
    """
    ########################
    # FINETUNING THE MODEL #
    ########################

    # get the training, validation and testing function for the model
    print("... getting the finetuning functions")
    train_fn, validate_model, test_model = dbn.build_finetune_functions(
        datasets=datasets, batch_size=batch_size, learning_rate=finetune_lr
    )

    print("... finetuning the model")
    # early-stopping parameters
    patience = 4 * n_train_batches  # look as this many examples regardless
    patience_increase = 2.0  # wait this much longer when a new best is
    # found
    improvement_threshold = 0.995  # a relative improvement of this much is
    # considered significant
    validation_frequency = min(n_train_batches, patience / 2)
    # go through this many
    # minibatches before checking the network
    # on the validation set; in this case we
    # check every epoch

    best_validation_loss = numpy.inf
    test_score = 0.0
    start_time = perf_counter()

    done_looping = False
    epoch = 0

    while (epoch < training_epochs) and (not done_looping):
        epoch = epoch + 1
        for minibatch_index in range(n_train_batches):
            minibatch_avg_cost = train_fn(minibatch_index)
            iter = (epoch - 1) * n_train_batches + minibatch_index

            if (iter + 1) % validation_frequency == 0:
                validation_losses = validate_model()
                this_validation_loss = numpy.mean(validation_losses)
                print(
                    "epoch %i, minibatch %i/%i, validation error %f %%"
                    % (
                        epoch,
                        minibatch_index + 1,
                        n_train_batches,
                        this_validation_loss * 100.0,
                    )
                )

                # if we got the best validation score until now
                if this_validation_loss < best_validation_loss:
                    # improve patience if loss improvement is good enough
                    if (
                        this_validation_loss
                        < best_validation_loss * improvement_threshold
                    ):
                        patience = max(patience, iter * patience_increase)

                    # save best validation score and iteration number
                    best_validation_loss = this_validation_loss
                    best_iter = iter

                    # test it on the test set
                    test_losses = test_model()
                    test_score = numpy.mean(test_losses)
                    print(
                        (
                            "     epoch %i, minibatch %i/%i, test error of "
                            "best model %f %%"
                        )
                        % (
                            epoch,
                            minibatch_index + 1,
                            n_train_batches,
                            test_score * 100.0,
                        )
                    )

            if patience <= iter:
                done_looping = True
                break

    end_time = perf_counter()
    print(
        (
            "Optimization complete with best validation score of %f %%, "
            "obtained at iteration %i, "
            "with test performance %f %%"
        )
        % (best_validation_loss * 100.0, best_iter + 1, test_score * 100.0)
    )
    """
    print(>> sys.stderr, ('The fine tuning code for file ' +
                          os.path.split(__file__)[1] +
                          ' ran for %.2fm' % ((end_time - start_time)
                                              / 60.)))
    """


if __name__ == "__main__":
    test_DBN()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# imdb.py

import pickle
import gzip

import numpy
import theano


def prepare_data(seqs, labels, maxlen=None):
    """Create the matrices from the datasets.

    This pad each sequence to the same lenght: the lenght of the
    longuest sequence or maxlen.

    if maxlen is set, we will cut all sequence to this maximum
    lenght.

    This swap the axis!
    """
    # x: a list of sentences
    lengths = [len(s) for s in seqs]

    if maxlen is not None:
        new_seqs = []
        new_labels = []
        new_lengths = []
        for l, s, y in zip(lengths, seqs, labels):
            if l < maxlen:
                new_seqs.append(s)
                new_labels.append(y)
                new_lengths.append(l)
        lengths = new_lengths
        labels = new_labels
        seqs = new_seqs

        if len(lengths) < 1:
            return None, None, None

    n_samples = len(seqs)
    maxlen = numpy.max(lengths)

    x = numpy.zeros((maxlen, n_samples)).astype("int64")
    x_mask = numpy.zeros((maxlen, n_samples)).astype(theano.config.floatX)
    for idx, s in enumerate(seqs):
        x[: lengths[idx], idx] = s
        x_mask[: lengths[idx], idx] = 1.0

    return x, x_mask, labels


def get_dataset_file(dataset, default_dataset, origin):
    """Look for it as if it was a full path, if not, try local file,
    if not try in the data directory.

    Download dataset if it is not present

    """
    data_dir, data_file = os.path.split(dataset)
    if data_dir == "" and not os.path.isfile(dataset):
        # Check if dataset is in the data directory.
        new_path = os.path.join(os.path.split(__file__)[0], "..", "data", dataset)
        if os.path.isfile(new_path) or data_file == default_dataset:
            dataset = new_path

    if (not os.path.isfile(dataset)) and data_file == default_dataset:
        import urllib

        print("Downloading data from %s" % origin)
        urllib.urlretrieve(origin, dataset)
    return dataset


def load_data(
    path="imdb.pkl", n_words=100000, valid_portion=0.1, maxlen=None, sort_by_len=True
):
    """Loads the dataset

    :type path: String
    :param path: The path to the dataset (here IMDB)
    :type n_words: int
    :param n_words: The number of word to keep in the vocabulary.
        All extra words are set to unknow (1).
    :type valid_portion: float
    :param valid_portion: The proportion of the full train set used for
        the validation set.
    :type maxlen: None or positive int
    :param maxlen: the max sequence length we use in the train/valid set.
    :type sort_by_len: bool
    :name sort_by_len: Sort by the sequence lenght for the train,
        valid and test set. This allow faster execution as it cause
        less padding per minibatch. Another mechanism must be used to
        shuffle the train set at each epoch.

    """

    #############
    # LOAD DATA #
    #############

    # Load the dataset
    path = get_dataset_file(
        path, "imdb.pkl", "http://www.iro.umontreal.ca/~lisa/deep/data/imdb.pkl"
    )

    if path.endswith(".gz"):
        f = gzip.open(path, "rb")
    else:
        f = open(path, "rb")

    train_set = pickle.load(f)
    test_set = pickle.load(f)
    f.close()
    if maxlen:
        new_train_set_x = []
        new_train_set_y = []
        for x, y in zip(train_set[0], train_set[1]):
            if len(x) < maxlen:
                new_train_set_x.append(x)
                new_train_set_y.append(y)
        train_set = (new_train_set_x, new_train_set_y)
        del new_train_set_x, new_train_set_y

    # split training set into validation set
    train_set_x, train_set_y = train_set
    n_samples = len(train_set_x)
    sidx = numpy.random.permutation(n_samples)
    n_train = int(numpy.round(n_samples * (1.0 - valid_portion)))
    valid_set_x = [train_set_x[s] for s in sidx[n_train:]]
    valid_set_y = [train_set_y[s] for s in sidx[n_train:]]
    train_set_x = [train_set_x[s] for s in sidx[:n_train]]
    train_set_y = [train_set_y[s] for s in sidx[:n_train]]

    train_set = (train_set_x, train_set_y)
    valid_set = (valid_set_x, valid_set_y)

    def remove_unk(x):
        return [[1 if w >= n_words else w for w in sen] for sen in x]

    test_set_x, test_set_y = test_set
    valid_set_x, valid_set_y = valid_set
    train_set_x, train_set_y = train_set

    train_set_x = remove_unk(train_set_x)
    valid_set_x = remove_unk(valid_set_x)
    test_set_x = remove_unk(test_set_x)

    def len_argsort(seq):
        return sorted(range(len(seq)), key=lambda x: len(seq[x]))

    if sort_by_len:
        sorted_index = len_argsort(test_set_x)
        test_set_x = [test_set_x[i] for i in sorted_index]
        test_set_y = [test_set_y[i] for i in sorted_index]

        sorted_index = len_argsort(valid_set_x)
        valid_set_x = [valid_set_x[i] for i in sorted_index]
        valid_set_y = [valid_set_y[i] for i in sorted_index]

        sorted_index = len_argsort(train_set_x)
        train_set_x = [train_set_x[i] for i in sorted_index]
        train_set_y = [train_set_y[i] for i in sorted_index]

    train = (train_set_x, train_set_y)
    valid = (valid_set_x, valid_set_y)
    test = (test_set_x, test_set_y)

    return train, valid, test


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# logistic_sgd.py

__docformat__ = "restructedtext en"

import pickle
import gzip
import os
import sys
import time
import numpy
import theano
import theano.tensor as T


class LogisticRegression(object):
    def __init__(self, input, n_in, n_out):
        # ��ʼ��Ȩ��WΪȫ0���� shape(n_in, n_out) W ��һ�����󣬵�k�б�ʾΪ��k��ķָ��ƽ��
        self.W = theano.shared(
            value=numpy.zeros((n_in, n_out), dtype=theano.config.floatX),
            name="W",
            borrow=True,
        )
        # ��ʼ��ƫ����bΪȫ0������n_out 0; b �Ǹ�����������Ԫ��k��ʾΪ��ƽ��k�����ɲ���
        self.b = theano.shared(
            value=numpy.zeros((n_out,), dtype=theano.config.floatX),
            name="b",
            borrow=True,
        )

        # �������Ա���ʵķ��ű��ʽ�������У�
        # x:input�Ǹ��������� row-j ��ʾΪ��j������ѵ������
        # input��(n_example,n_in)��W�ǣ�n_in,n_out��,��˵õ�(n_example,n_out)������ƫ��b��
        # ����ΪT.nnet.softmax�����룬�õ�p_y_given_x
        # ��p_y_given_xÿһ�д���ÿһ������������Ϊ�����ĸ���
        # PS��b��n_outά��������(n_example,n_out)������ӣ��ڲ���ʵ���ȸ���n_example��b��
        # Ȼ��(n_example,n_out)�����ÿһ�ж���b
        self.p_y_given_x = T.nnet.softmax(T.dot(input, self.W) + self.b)

        # ͨ�����ű���������Ԥ�����������
        self.y_pred = T.argmax(self.p_y_given_x, axis=1)

        # ����ģ�Ͳ���
        self.params = [self.W, self.b]

    def negative_log_likelihood(self, y):
        # ���ۺ���NLL
        # ��Ϊ������MSGD��ÿ��ѵ��һ��batch��һ��batch��n_example����������y��С��(n_example,),
        # y.shape[0]�ó�����������������T.log(self.p_y_given_x)���ΪLP��
        # ��LP[T.arange(y.shape[0]),y]�õ�[LP[0,y[0]], LP[1,y[1]], LP[2,y[2]], ...,LP[n-1,y[n-1]]]
        # ������ֵmean��Ҳ����˵��minibatch��SGD���Ǽ����batch������������NLL��ƽ��ֵ����Ϊ����cost
        return -T.mean(T.log(self.p_y_given_x)[T.arange(y.shape[0]), y])

    def errors(self, y):  # batch�������
        # ���y��y_pred�Ƿ�����ͬ��ά��
        if y.ndim != self.y_pred.ndim:
            raise TypeError(
                "y should have the same shape as self.y_pred",
                ("y", y.type, "y_pred", self.y_pred.type),
            )
        # ���y�Ƿ�����ȷ����������
        if y.dtype.startswith("int"):
            # �ټ���ǲ���int���ͣ��ǵĻ�����T.neq(self.y_pred, y)�ľ�ֵ����Ϊ�����
            # �ٸ����ӣ�����self.y_pred=[3,2,3,2,3,2],��ʵ����y=[3,4,3,4,3,4]
            # ��T.neq(self.y_pred, y)=[0,1,0,1,0,1],1��ʾ���ȣ�0��ʾ���
            # ��T.mean(T.neq(self.y_pred, y))=T.mean([0,1,0,1,0,1])=0.5����������50%
            return T.mean(
                T.neq(self.y_pred, y)
            )  # T.neq������������һ��0��1������������1��ʾһ��Ԥ�����
        else:
            raise NotImplementedError()

    def save_net(self, path):
        import pickle

        write_file = open(path, "wb")
        pickle.dump(self.W.get_value(borrow=True), write_file, -1)
        pickle.dump(self.b.get_value(borrow=True), write_file, -1)
        write_file.close()


##############
# �������ݼ� #
##############
def load_data(dataset):
    # ������ز����ھʹ������������ݼ�
    data_dir, data_file = os.path.split(dataset)
    if data_dir == "" and not os.path.isfile(dataset):
        # ������ݼ��Ƿ�������Ŀ¼��.
        new_path = os.path.join(os.path.split(__file__)[0], "..", "data", dataset)
        if os.path.isfile(new_path) or data_file == "mnist.pkl.gz":
            dataset = new_path

    if (not os.path.isfile(dataset)) and data_file == "mnist.pkl.gz":
        import urllib

        origin = "http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz"
        print("Downloading data from %s" % origin)
        urllib.urlretrieve(origin, dataset)

    print("... loading data")

    # �������ݼ�������
    f = gzip.open(dataset, "rb")
    train_set, valid_set, test_set = pickle.load(f)
    f.close()

    # �����հ���ѵ����, ��֤��, ���Լ���ʽ: tuple(input, target)
    # ����ʱһ����ά��numpy.ndarray (��һ������)
    # ����ÿһ�ж���һ������. Ŀ���Ǹ�һά��numpy.ndarray (vector))������������ͬ���ĳ���
    # ��Ӧ�ø���һ������������������ͬ������Ŀ�ꡣ
    def shared_dataset(data_xy, borrow=True):
        data_x, data_y = data_xy
        shared_x = theano.shared(
            numpy.asarray(data_x, dtype=theano.config.floatX), borrow=borrow
        )
        shared_y = theano.shared(
            numpy.asarray(data_y, dtype=theano.config.floatX), borrow=borrow
        )
        # ���洢���ݵ�GPUʱ�����ݱ���Ϊfloat��ʽ��������ǽ���ǩ�洢Ϊ"floatX"
        # ���ڼ����ڼ䣬������Ҫ������Ϊint��(��Ϊ����������������Ǹ�����
        # �����������)������֮�����ǽ���ת��Ϊint�����ǻرܸ������һ������
        return shared_x, T.cast(shared_y, "int32")

    test_set_x, test_set_y = shared_dataset(test_set)
    valid_set_x, valid_set_y = shared_dataset(valid_set)
    train_set_x, train_set_y = shared_dataset(train_set)

    rval = [
        (train_set_x, train_set_y),
        (valid_set_x, valid_set_y),
        (test_set_x, test_set_y),
    ]
    return rval


# ��ִ�к���
# learning_rate=0.13, ���ݶ��½�����Ȩ�ظ�����
# n_epochs=1000, ����������
# dataset='mnist.pkl.gz', ���ݼ�
# batch_size=600 ����С
def sgd_optimization_mnist(
    learning_rate=0.13, n_epochs=1000, dataset="mnist.pkl.gz", batch_size=600
):
    datasets = load_data(dataset)

    train_set_x, train_set_y = datasets[0]
    valid_set_x, valid_set_y = datasets[1]
    test_set_x, test_set_y = datasets[2]

    # �����ж��ٸ�minibatch����Ϊ���ǵ��Ż��㷨��MSGD����һ��batchһ��batch������cost��
    n_train_batches = train_set_x.get_value(borrow=True).shape[0] / batch_size
    n_valid_batches = valid_set_x.get_value(borrow=True).shape[0] / batch_size
    n_test_batches = test_set_x.get_value(borrow=True).shape[0] / batch_size

    print("... building the model")

    # ���ñ�����index��ʾminibatch���±꣬x��ʾѵ��������y�Ƕ�Ӧ��label
    index = T.lscalar()  # ��������
    x = T.matrix("x")  # ����, ����Ϊ��դͼ��
    y = T.ivector("y")  # ��ǩ, ����Ϊ[INT]��ǩ��1ά����

    # ʵ����logisitic��������ÿ��MNIST ͼ�ĳߴ�Ϊ 28*28 ��x����input��ʼ����
    classifier = LogisticRegression(input=x, n_in=28 * 28, n_out=10)
    # ������ۣ���y����ʼ��������ʵ����һ�������Ĳ���Input
    cost = classifier.negative_log_likelihood(y)  # ��������Ȼ�Ĵ���
    # �������ģ�ͣ�����ָ��
    test_model = theano.function(
        inputs=[index],
        outputs=classifier.errors(y),
        givens={
            x: test_set_x[index * batch_size : (index + 1) * batch_size],
            y: test_set_y[index * batch_size : (index + 1) * batch_size],
        },
    )
    # ������֤ģ�ͣ�����ָ��
    validate_model = theano.function(
        inputs=[index],
        outputs=classifier.errors(y),
        givens={
            x: valid_set_x[index * batch_size : (index + 1) * batch_size],
            y: valid_set_y[index * batch_size : (index + 1) * batch_size],
        },
    )

    # ����theta = (W,b)���ݶ�
    g_W = T.grad(cost=cost, wrt=classifier.W)
    g_b = T.grad(cost=cost, wrt=classifier.b)

    # learning_rate���ݶ��½�����Ȩ�ظ�����
    updates = [
        (classifier.W, classifier.W - learning_rate * g_W),
        (classifier.b, classifier.b - learning_rate * g_b),
    ]

    # ����ָ�붨��ѵ��ģ��
    train_model = theano.function(
        inputs=[index],
        outputs=cost,
        updates=updates,
        givens={
            x: train_set_x[index * batch_size : (index + 1) * batch_size],
            y: train_set_y[index * batch_size : (index + 1) * batch_size],
        },
    )

    ###############
    #   ѵ��ģ��  #
    ###############
    print("... training the model")
    patience = 5000  # ����������
    patience_increase = 2  # ����
    # ��ߵ���ֵ������֤����С��֮ǰ��0.995��ʱ�������best_validation_loss
    improvement_threshold = 0.995  # �൱��ĸ��Ʊ���Ϊ������
    # ��������validation_frequency���Ա�֤ÿһ��epoch��������֤���ϲ��ԡ�
    validation_frequency = min(n_train_batches, patience / 2)
    best_validation_loss = numpy.inf  # ��õ���֤���ϵ�loss��ԽС��Խ�á���ʼ��Ϊ�����
    test_score = 0.0
    start_time = perf_counter()  # ��ʼʱ��

    done_looping = False
    epoch = 0
    # �������ѵ�������ˣ�whileѭ�����Ƶ�ʱ����epoch��һ��epoch��������е�batch�������е�ͼƬ��
    # ���ﵽ�����n_epochʱ������patience<iterʱ������ѵ��
    while (epoch < n_epochs) and (not done_looping):
        epoch = epoch + 1
        # forѭ���Ǳ���һ����batch��һ��һ��batch��ѵ����
        # ѭ���������train_model(minibatch_index)ȥѵ��ģ�ͣ�
        for minibatch_index in xrange(n_train_batches):
            minibatch_avg_cost = train_model(minibatch_index)  # �õ�ÿ����ƽ������
            iter = (
                epoch - 1
            ) * n_train_batches + minibatch_index  # �ۼ�ѵ������batch��iter��
            # ��iter��validation_frequency����ʱ�������֤���ϲ��ԣ�
            if (iter + 1) % validation_frequency == 0:
                validation_losses = [
                    validate_model(i) for i in xrange(n_valid_batches)
                ]  # ������֤������ʧ����
                this_validation_loss = numpy.mean(validation_losses)
                # ���
                print(
                    "epoch %i, minibatch %i/%i, validation error %f %%"
                    % (
                        epoch,
                        minibatch_index + 1,
                        n_train_batches,
                        this_validation_loss * 100.0,
                    )
                )
                # �����֤������ʧthis_validation_lossС��֮ǰ��ѵ���ʧbest_validation_loss��
                # �����best_validation_loss��best_iter��ͬʱ��testset�ϲ��ԡ�
                # �����֤������ʧthis_validation_lossС��best_validation_loss*improvement_thresholdʱ�����patience��
                if this_validation_loss < best_validation_loss:
                    if (
                        this_validation_loss
                        < best_validation_loss * improvement_threshold
                    ):
                        patience = max(patience, iter * patience_increase)
                    best_validation_loss = this_validation_loss
                    test_losses = [test_model(i) for i in xrange(n_test_batches)]
                    test_score = numpy.mean(test_losses)

                    print(
                        (
                            "     epoch %i, minibatch %i/%i, test error of"
                            " best model %f %%"
                        )
                        % (
                            epoch,
                            minibatch_index + 1,
                            n_train_batches,
                            test_score * 100.0,
                        )
                    )
            if patience <= iter:  # �ﵽ�������������˳�
                done_looping = True
                break
    classifier.save_net("tmp_convnet.data")  # ��������ѵ����������Ľ��������
    # whileѭ������
    end_time = perf_counter()  # ����ʱ��
    # ���
    print(
        (
            "Optimization complete with best validation score of %f %%,"
            "with test performance %f %%"
        )
        % (best_validation_loss * 100.0, test_score * 100.0)
    )
    print(
        "The code run for %d epochs, with %f epochs/sec"
        % (epoch, 1.0 * epoch / (end_time - start_time))
    )
    # print(>> sys.stderr, ('The code for file ' + os.path.split(__file__)[1] + ' ran for %.1fs' % ((end_time - start_time))))


if __name__ == "__main__":
    sgd_optimization_mnist()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# lstm.py

"""
Build a tweet sentiment analyzer
"""
from collections import OrderedDict
import pickle
import numpy
import theano
from theano import config
import theano.tensor as tensor
from theano.sandbox.rng_mrg import MRG_RandomStreams as RandomStreams

import imdb

datasets = {"imdb": (imdb.load_data, imdb.prepare_data)}

# Set the random number generators' seeds for consistency
SEED = 123
numpy.random.seed(SEED)


def numpy_floatX(data):
    return numpy.asarray(data, dtype=config.floatX)


def get_minibatches_idx(n, minibatch_size, shuffle=False):
    """
    Used to shuffle the dataset at each iteration.
    """

    idx_list = numpy.arange(n, dtype="int32")

    if shuffle:
        numpy.random.shuffle(idx_list)

    minibatches = []
    minibatch_start = 0
    for i in range(n // minibatch_size):
        minibatches.append(idx_list[minibatch_start : minibatch_start + minibatch_size])
        minibatch_start += minibatch_size

    if minibatch_start != n:
        # Make a minibatch out of what is left
        minibatches.append(idx_list[minibatch_start:])

    return zip(range(len(minibatches)), minibatches)


def get_dataset(name):
    return datasets[name][0], datasets[name][1]


def zipp(params, tparams):
    """
    When we reload the model. Needed for the GPU stuff.
    """
    for kk, vv in params.iteritems():
        tparams[kk].set_value(vv)


def unzip(zipped):
    """
    When we pickle the model. Needed for the GPU stuff.
    """
    new_params = OrderedDict()
    for kk, vv in zipped.iteritems():
        new_params[kk] = vv.get_value()
    return new_params


def dropout_layer(state_before, use_noise, trng):
    proj = tensor.switch(
        use_noise,
        (
            state_before
            * trng.binomial(state_before.shape, p=0.5, n=1, dtype=state_before.dtype)
        ),
        state_before * 0.5,
    )
    return proj


def _p(pp, name):
    return "%s_%s" % (pp, name)


def init_params(options):
    """
    Global (not LSTM) parameter. For the embeding and the classifier.
    """
    params = OrderedDict()
    # embedding
    randn = numpy.random.rand(options["n_words"], options["dim_proj"])
    params["Wemb"] = (0.01 * randn).astype(config.floatX)
    params = get_layer(options["encoder"])[0](
        options, params, prefix=options["encoder"]
    )
    # classifier
    params["U"] = 0.01 * numpy.random.randn(
        options["dim_proj"], options["ydim"]
    ).astype(config.floatX)
    params["b"] = numpy.zeros((options["ydim"],)).astype(config.floatX)

    return params


def load_params(path, params):
    pp = numpy.load(path)
    for kk, vv in params.iteritems():
        if kk not in pp:
            raise Warning("%s is not in the archive" % kk)
        params[kk] = pp[kk]

    return params


def init_tparams(params):
    tparams = OrderedDict()
    for kk, pp in params.iteritems():
        tparams[kk] = theano.shared(params[kk], name=kk)
    return tparams


def get_layer(name):
    fns = layers[name]
    return fns


def ortho_weight(ndim):
    W = numpy.random.randn(ndim, ndim)
    u, s, v = numpy.linalg.svd(W)
    return u.astype(config.floatX)


def param_init_lstm(options, params, prefix="lstm"):
    """
    Init the LSTM parameter:

    :see: init_params
    """
    W = numpy.concatenate(
        [
            ortho_weight(options["dim_proj"]),
            ortho_weight(options["dim_proj"]),
            ortho_weight(options["dim_proj"]),
            ortho_weight(options["dim_proj"]),
        ],
        axis=1,
    )
    params[_p(prefix, "W")] = W
    U = numpy.concatenate(
        [
            ortho_weight(options["dim_proj"]),
            ortho_weight(options["dim_proj"]),
            ortho_weight(options["dim_proj"]),
            ortho_weight(options["dim_proj"]),
        ],
        axis=1,
    )
    params[_p(prefix, "U")] = U
    b = numpy.zeros((4 * options["dim_proj"],))
    params[_p(prefix, "b")] = b.astype(config.floatX)

    return params


def lstm_layer(tparams, state_below, options, prefix="lstm", mask=None):
    nsteps = state_below.shape[0]
    if state_below.ndim == 3:
        n_samples = state_below.shape[1]
    else:
        n_samples = 1

    assert mask is not None

    def _slice(_x, n, dim):
        if _x.ndim == 3:
            return _x[:, :, n * dim : (n + 1) * dim]
        return _x[:, n * dim : (n + 1) * dim]

    def _step(m_, x_, h_, c_):
        preact = tensor.dot(h_, tparams[_p(prefix, "U")])
        preact += x_

        i = tensor.nnet.sigmoid(_slice(preact, 0, options["dim_proj"]))
        f = tensor.nnet.sigmoid(_slice(preact, 1, options["dim_proj"]))
        o = tensor.nnet.sigmoid(_slice(preact, 2, options["dim_proj"]))
        c = tensor.tanh(_slice(preact, 3, options["dim_proj"]))

        c = f * c_ + i * c
        c = m_[:, None] * c + (1.0 - m_)[:, None] * c_

        h = o * tensor.tanh(c)
        h = m_[:, None] * h + (1.0 - m_)[:, None] * h_

        return h, c

    state_below = (
        tensor.dot(state_below, tparams[_p(prefix, "W")]) + tparams[_p(prefix, "b")]
    )

    dim_proj = options["dim_proj"]
    rval, updates = theano.scan(
        _step,
        sequences=[mask, state_below],
        outputs_info=[
            tensor.alloc(numpy_floatX(0.0), n_samples, dim_proj),
            tensor.alloc(numpy_floatX(0.0), n_samples, dim_proj),
        ],
        name=_p(prefix, "_layers"),
        n_steps=nsteps,
    )
    return rval[0]


# ff: Feed Forward (normal neural net), only useful to put after lstm
#     before the classifier.
layers = {"lstm": (param_init_lstm, lstm_layer)}


def sgd(lr, tparams, grads, x, mask, y, cost):
    """Stochastic Gradient Descent

    :note: A more complicated version of sgd then needed.  This is
        done like that for adadelta and rmsprop.

    """
    # New set of shared variable that will contain the gradient
    # for a mini-batch.
    gshared = [
        theano.shared(p.get_value() * 0.0, name="%s_grad" % k)
        for k, p in tparams.iteritems()
    ]
    gsup = [(gs, g) for gs, g in zip(gshared, grads)]

    # Function that computes gradients for a mini-batch, but do not
    # updates the weights.
    f_grad_shared = theano.function(
        [x, mask, y], cost, updates=gsup, name="sgd_f_grad_shared"
    )

    pup = [(p, p - lr * g) for p, g in zip(tparams.values(), gshared)]

    # Function that updates the weights from the previously computed
    # gradient.
    f_update = theano.function([lr], [], updates=pup, name="sgd_f_update")

    return f_grad_shared, f_update


def adadelta(lr, tparams, grads, x, mask, y, cost):
    zipped_grads = [
        theano.shared(p.get_value() * numpy_floatX(0.0), name="%s_grad" % k)
        for k, p in tparams.iteritems()
    ]
    running_up2 = [
        theano.shared(p.get_value() * numpy_floatX(0.0), name="%s_rup2" % k)
        for k, p in tparams.iteritems()
    ]
    running_grads2 = [
        theano.shared(p.get_value() * numpy_floatX(0.0), name="%s_rgrad2" % k)
        for k, p in tparams.iteritems()
    ]

    zgup = [(zg, g) for zg, g in zip(zipped_grads, grads)]
    rg2up = [
        (rg2, 0.95 * rg2 + 0.05 * (g**2)) for rg2, g in zip(running_grads2, grads)
    ]

    f_grad_shared = theano.function(
        [x, mask, y], cost, updates=zgup + rg2up, name="adadelta_f_grad_shared"
    )

    updir = [
        -tensor.sqrt(ru2 + 1e-6) / tensor.sqrt(rg2 + 1e-6) * zg
        for zg, ru2, rg2 in zip(zipped_grads, running_up2, running_grads2)
    ]
    ru2up = [
        (ru2, 0.95 * ru2 + 0.05 * (ud**2)) for ru2, ud in zip(running_up2, updir)
    ]
    param_up = [(p, p + ud) for p, ud in zip(tparams.values(), updir)]

    f_update = theano.function(
        [lr],
        [],
        updates=ru2up + param_up,
        on_unused_input="ignore",
        name="adadelta_f_update",
    )

    return f_grad_shared, f_update


def rmsprop(lr, tparams, grads, x, mask, y, cost):
    zipped_grads = [
        theano.shared(p.get_value() * numpy_floatX(0.0), name="%s_grad" % k)
        for k, p in tparams.iteritems()
    ]
    running_grads = [
        theano.shared(p.get_value() * numpy_floatX(0.0), name="%s_rgrad" % k)
        for k, p in tparams.iteritems()
    ]
    running_grads2 = [
        theano.shared(p.get_value() * numpy_floatX(0.0), name="%s_rgrad2" % k)
        for k, p in tparams.iteritems()
    ]

    zgup = [(zg, g) for zg, g in zip(zipped_grads, grads)]
    rgup = [(rg, 0.95 * rg + 0.05 * g) for rg, g in zip(running_grads, grads)]
    rg2up = [
        (rg2, 0.95 * rg2 + 0.05 * (g**2)) for rg2, g in zip(running_grads2, grads)
    ]

    f_grad_shared = theano.function(
        [x, mask, y], cost, updates=zgup + rgup + rg2up, name="rmsprop_f_grad_shared"
    )

    updir = [
        theano.shared(p.get_value() * numpy_floatX(0.0), name="%s_updir" % k)
        for k, p in tparams.iteritems()
    ]
    updir_new = [
        (ud, 0.9 * ud - 1e-4 * zg / tensor.sqrt(rg2 - rg**2 + 1e-4))
        for ud, zg, rg, rg2 in zip(updir, zipped_grads, running_grads, running_grads2)
    ]
    param_up = [(p, p + udn[1]) for p, udn in zip(tparams.values(), updir_new)]
    f_update = theano.function(
        [lr],
        [],
        updates=updir_new + param_up,
        on_unused_input="ignore",
        name="rmsprop_f_update",
    )

    return f_grad_shared, f_update


def build_model(tparams, options):
    trng = RandomStreams(SEED)

    # Used for dropout.
    use_noise = theano.shared(numpy_floatX(0.0))

    x = tensor.matrix("x", dtype="int64")
    mask = tensor.matrix("mask", dtype=config.floatX)
    y = tensor.vector("y", dtype="int64")

    n_timesteps = x.shape[0]
    n_samples = x.shape[1]

    emb = tparams["Wemb"][x.flatten()].reshape(
        [n_timesteps, n_samples, options["dim_proj"]]
    )
    proj = get_layer(options["encoder"])[1](
        tparams, emb, options, prefix=options["encoder"], mask=mask
    )
    if options["encoder"] == "lstm":
        proj = (proj * mask[:, :, None]).sum(axis=0)
        proj = proj / mask.sum(axis=0)[:, None]
    if options["use_dropout"]:
        proj = dropout_layer(proj, use_noise, trng)

    pred = tensor.nnet.softmax(tensor.dot(proj, tparams["U"]) + tparams["b"])

    f_pred_prob = theano.function([x, mask], pred, name="f_pred_prob")
    f_pred = theano.function([x, mask], pred.argmax(axis=1), name="f_pred")

    off = 1e-8
    if pred.dtype == "float16":
        off = 1e-6

    cost = -tensor.log(pred[tensor.arange(n_samples), y] + off).mean()

    return use_noise, x, mask, y, f_pred_prob, f_pred, cost


def pred_probs(f_pred_prob, prepare_data, data, iterator, verbose=False):
    """If you want to use a trained model, this is useful to compute
    the probabilities of new examples.
    """
    n_samples = len(data[0])
    probs = numpy.zeros((n_samples, 2)).astype(config.floatX)

    n_done = 0

    for _, valid_index in iterator:
        x, mask, y = prepare_data(
            [data[0][t] for t in valid_index],
            numpy.array(data[1])[valid_index],
            maxlen=None,
        )
        pred_probs = f_pred_prob(x, mask)
        probs[valid_index, :] = pred_probs

        n_done += len(valid_index)
        if verbose:
            print("%d/%d samples classified" % (n_done, n_samples))

    return probs


def pred_error(f_pred, prepare_data, data, iterator, verbose=False):
    """
    Just compute the error
    f_pred: Theano fct computing the prediction
    prepare_data: usual prepare_data for that dataset.
    """
    valid_err = 0
    for _, valid_index in iterator:
        x, mask, y = prepare_data(
            [data[0][t] for t in valid_index],
            numpy.array(data[1])[valid_index],
            maxlen=None,
        )
        preds = f_pred(x, mask)
        targets = numpy.array(data[1])[valid_index]
        valid_err += (preds == targets).sum()
    valid_err = 1.0 - numpy_floatX(valid_err) / len(data[0])

    return valid_err


def train_lstm(
    dim_proj=128,  # word embeding dimension and LSTM number of hidden units.
    patience=10,  # Number of epoch to wait before early stop if no progress
    max_epochs=5000,  # The maximum number of epoch to run
    dispFreq=10,  # Display to stdout the training progress every N updates
    decay_c=0.0,  # Weight decay for the classifier applied to the U weights.
    lrate=0.0001,  # Learning rate for sgd (not used for adadelta and rmsprop)
    n_words=10000,  # Vocabulary size
    optimizer=adadelta,  # sgd, adadelta and rmsprop available, sgd very hard to use, not recommanded (probably need momentum and decaying learning rate).
    encoder="lstm",  # TODO: can be removed must be lstm.
    saveto="lstm_model.npz",  # The best model will be saved there
    validFreq=370,  # Compute the validation error after this number of update.
    saveFreq=1110,  # Save the parameters after every saveFreq updates
    maxlen=100,  # Sequence longer then this get ignored
    batch_size=16,  # The batch size during training.
    valid_batch_size=64,  # The batch size used for validation/test set.
    dataset="imdb",
    # Parameter for extra option
    noise_std=0.0,
    use_dropout=True,  # if False slightly faster, but worst test error
    # This frequently need a bigger model.
    reload_model=None,  # Path to a saved model we want to start from.
    test_size=-1,  # If >0, we keep only this number of test example.
):
    # Model options
    model_options = locals().copy()
    print("model options", model_options)

    load_data, prepare_data = get_dataset(dataset)

    print("Loading data")
    train, valid, test = load_data(n_words=n_words, valid_portion=0.05, maxlen=maxlen)
    if test_size > 0:
        # The test set is sorted by size, but we want to keep random
        # size example.  So we must select a random selection of the
        # examples.
        idx = numpy.arange(len(test[0]))
        numpy.random.shuffle(idx)
        idx = idx[:test_size]
        test = ([test[0][n] for n in idx], [test[1][n] for n in idx])

    ydim = numpy.max(train[1]) + 1

    model_options["ydim"] = ydim

    print("Building model")
    # This create the initial parameters as numpy ndarrays.
    # Dict name (string) -> numpy ndarray
    params = init_params(model_options)

    if reload_model:
        load_params("lstm_model.npz", params)

    # This create Theano Shared Variable from the parameters.
    # Dict name (string) -> Theano Tensor Shared Variable
    # params and tparams have different copy of the weights.
    tparams = init_tparams(params)

    # use_noise is for dropout
    (use_noise, x, mask, y, f_pred_prob, f_pred, cost) = build_model(
        tparams, model_options
    )

    if decay_c > 0.0:
        decay_c = theano.shared(numpy_floatX(decay_c), name="decay_c")
        weight_decay = 0.0
        weight_decay += (tparams["U"] ** 2).sum()
        weight_decay *= decay_c
        cost += weight_decay

    f_cost = theano.function([x, mask, y], cost, name="f_cost")

    grads = tensor.grad(cost, wrt=tparams.values())
    f_grad = theano.function([x, mask, y], grads, name="f_grad")

    lr = tensor.scalar(name="lr")
    f_grad_shared, f_update = optimizer(lr, tparams, grads, x, mask, y, cost)

    print("Optimization")

    kf_valid = get_minibatches_idx(len(valid[0]), valid_batch_size)
    kf_test = get_minibatches_idx(len(test[0]), valid_batch_size)

    print("%d train examples" % len(train[0]))
    print("%d valid examples" % len(valid[0]))
    print("%d test examples" % len(test[0]))

    history_errs = []
    best_p = None
    bad_count = 0

    if validFreq == -1:
        validFreq = len(train[0]) / batch_size
    if saveFreq == -1:
        saveFreq = len(train[0]) / batch_size

    uidx = 0  # the number of update done
    estop = False  # early stop
    start_time = perf_counter()
    try:
        for eidx in range(max_epochs):
            n_samples = 0

            # Get new shuffled index for the training set.
            kf = get_minibatches_idx(len(train[0]), batch_size, shuffle=True)

            for _, train_index in kf:
                uidx += 1
                use_noise.set_value(1.0)

                # Select the random examples for this minibatch
                y = [train[1][t] for t in train_index]
                x = [train[0][t] for t in train_index]

                # Get the data in numpy.ndarray format
                # This swap the axis!
                # Return something of shape (minibatch maxlen, n samples)
                x, mask, y = prepare_data(x, y)
                n_samples += x.shape[1]

                cost = f_grad_shared(x, mask, y)
                f_update(lrate)

                if numpy.isnan(cost) or numpy.isinf(cost):
                    print("NaN detected")
                    return 1.0, 1.0, 1.0

                if numpy.mod(uidx, dispFreq) == 0:
                    print("Epoch ", eidx, "Update ", uidx, "Cost ", cost)

                if saveto and numpy.mod(uidx, saveFreq) == 0:
                    print(
                        "Saving...",
                    )

                    if best_p is not None:
                        params = best_p
                    else:
                        params = unzip(tparams)
                    numpy.savez(saveto, history_errs=history_errs, **params)
                    pickle.dump(model_options, open("%s.pickle" % saveto, "wb"), -1)
                    print("Done")

                if numpy.mod(uidx, validFreq) == 0:
                    use_noise.set_value(0.0)
                    train_err = pred_error(f_pred, prepare_data, train, kf)
                    valid_err = pred_error(f_pred, prepare_data, valid, kf_valid)
                    test_err = pred_error(f_pred, prepare_data, test, kf_test)

                    history_errs.append([valid_err, test_err])

                    if uidx == 0 or valid_err <= numpy.array(history_errs)[:, 0].min():
                        best_p = unzip(tparams)
                        bad_counter = 0

                    print(("Train ", train_err, "Valid ", valid_err, "Test ", test_err))

                    if (
                        len(history_errs) > patience
                        and valid_err >= numpy.array(history_errs)[:-patience, 0].min()
                    ):
                        bad_counter += 1
                        if bad_counter > patience:
                            print("Early Stop!")
                            estop = True
                            break

            print("Seen %d samples" % n_samples)

            if estop:
                break

    except KeyboardInterrupt:
        print("Training interupted")

    end_time = perf_counter()
    if best_p is not None:
        zipp(best_p, tparams)
    else:
        best_p = unzip(tparams)

    use_noise.set_value(0.0)
    kf_train_sorted = get_minibatches_idx(len(train[0]), batch_size)
    train_err = pred_error(f_pred, prepare_data, train, kf_train_sorted)
    valid_err = pred_error(f_pred, prepare_data, valid, kf_valid)
    test_err = pred_error(f_pred, prepare_data, test, kf_test)

    print("Train ", train_err, "Valid ", valid_err, "Test ", test_err)
    if saveto:
        numpy.savez(
            saveto,
            train_err=train_err,
            valid_err=valid_err,
            test_err=test_err,
            history_errs=history_errs,
            **best_p
        )
    print(
        "The code run for %d epochs, with %f sec/epochs"
        % ((eidx + 1), (end_time - start_time) / (1.0 * (eidx + 1)))
    )

    # print(>> sys.stderr, ('Training took %.1fs' %(end_time - start_time)))
    return train_err, valid_err, test_err


if __name__ == "__main__":
    # See function train for all possible parameter and there definition.
    train_lstm(
        max_epochs=100,
        test_size=500,
    )

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# mlp.py

"""
This tutorial introduces the multilayer perceptron using Theano.

 A multilayer perceptron is a logistic regressor where
instead of feeding the input to the logistic regression you insert a
intermediate layer, called the hidden layer, that has a nonlinear
activation function (usually tanh or sigmoid) . One can use many such
hidden layers making the architecture deep. The tutorial will also tackle
the problem of MNIST digit classification.

.. math::

    f(x) = G( b^{(2)} + W^{(2)}( s( b^{(1)} + W^{(1)} x))),

References:

    - textbooks: "Pattern Recognition and Machine Learning" -
                 Christopher M. Bishop, section 5

"""
__docformat__ = "restructedtext en"


import os
import sys
import time
import numpy
import theano
import theano.tensor as T
from logistic_sgd import LogisticRegression, load_data


class HiddenLayer(object):
    def __init__(self, rng, input, n_in, n_out, W=None, b=None, activation=T.tanh):
        """
        ע�ͣ�
        ���Ƕ������ز���࣬������ȷ�����ز�����뼴input����������ز����Ԫ����������������ز���ȫ���ӵġ�
        ����������n_inά��������Ҳ����˵ʱn_in����Ԫ�������ز���n_out����Ԫ������Ϊ��ȫ���ӣ�
        һ����n_in*n_out��Ȩ�أ���W��Сʱ(n_in,n_out),n_in��n_out�У�ÿһ�ж�Ӧ���ز��ÿһ����Ԫ������Ȩ�ء�
        b��ƫ�ã����ز���n_out����Ԫ����bʱn_outά������
        rng���������������numpy.random.RandomState�����ڳ�ʼ��W��
        inputѵ��ģ�����õ����������룬������MLP������㣬MLP����������Ԫ����ʱn_in��������Ĳ���input��С�ǣ�n_example,n_in��,ÿһ��һ����������ÿһ����ΪMLP������㡣
        activation:�����,���ﶨ��Ϊ����tan
        """
        self.input = input  # ��HiddenLayer��input�������ݽ�����input

        """ 
        ע�ͣ� 
        ����Ҫ����GPU����W��b����ʹ�� dtype=theano.config.floatX,���Ҷ���Ϊtheano.shared 
        ���⣬W�ĳ�ʼ���и��������ʹ��tanh����������-sqrt(6./(n_in+n_hidden))��sqrt(6./(n_in+n_hidden))֮����� 
        ��ȡ��ֵ����ʼ��W����ʱsigmoid�������������ٳ�4���� 
        """
        # ���Wδ��ʼ�������������������ʼ����
        # ��������жϵ�ԭ���ǣ���ʱ�����ǿ�����ѵ���õĲ�������ʼ��W�����ҵ���һƪ���¡�
        if W is None:
            W_values = numpy.asarray(
                rng.uniform(
                    low=-numpy.sqrt(6.0 / (n_in + n_out)),
                    high=numpy.sqrt(6.0 / (n_in + n_out)),
                    size=(n_in, n_out),
                ),
                dtype=theano.config.floatX,
            )
            if activation == theano.tensor.nnet.sigmoid:
                W_values *= 4

            W = theano.shared(value=W_values, name="W", borrow=True)

        if b is None:
            b_values = numpy.zeros((n_out,), dtype=theano.config.floatX)
            b = theano.shared(value=b_values, name="b", borrow=True)
        # �����涨���W��b����ʼ����HiddenLayer��W��b
        self.W = W
        self.b = b
        # ����������
        lin_output = T.dot(input, self.W) + self.b
        self.output = lin_output if activation is None else activation(lin_output)
        # ������Ĳ���
        self.params = [self.W, self.b]


# 3���MLP
class MLP(object):
    def __init__(self, rng, input, n_in, n_hidden, n_out):
        self.hiddenLayer = HiddenLayer(
            rng=rng, input=input, n_in=n_in, n_out=n_hidden, activation=T.tanh
        )

        # ��������hiddenLayer�������Ϊ�����logRegressionLayer�����룬�����Ͱ�����������
        self.logRegressionLayer = LogisticRegression(
            input=self.hiddenLayer.output, n_in=n_hidden, n_out=n_out
        )
        # �����Ѿ������MLP�Ļ����ṹ��������MLPģ�͵������������ߺ���

        # �����������L1��L2_sqr
        self.L1 = abs(self.hiddenLayer.W).sum() + abs(self.logRegressionLayer.W).sum()

        # square of L2 norm ; one regularization option is to enforce
        # square of L2 norm to be small
        self.L2_sqr = (self.hiddenLayer.W**2).sum() + (
            self.logRegressionLayer.W**2
        ).sum()

        # ��ʧ����Nll��Ҳ�д��ۺ�����
        self.negative_log_likelihood = self.logRegressionLayer.negative_log_likelihood
        # ���
        self.errors = self.logRegressionLayer.errors

        # MLP�Ĳ���
        self.params = self.hiddenLayer.params + self.logRegressionLayer.params


# test_mlp��һ��Ӧ��ʵ�������ݶ��½����Ż�MLP�����MNIST���ݼ�
def test_mlp(
    learning_rate=0.01,
    L1_reg=0.00,
    L2_reg=0.0001,
    n_epochs=1000,
    dataset="mnist.pkl.gz",
    batch_size=20,
    n_hidden=500,
):
    """
    ע�ͣ�
    learning_rateѧϰ���ʣ��ݶ�ǰ��ϵ����
    L1_reg��L2_reg��������ǰ��ϵ����Ȩ����������Nll��ı���
    ���ۺ���=Nll+L1_reg*L1����L2_reg*L2_sqr
    n_epochs������������������ѵ�������������ڽ����Ż�����
    dataset��ѵ�����ݵ�·��
    n_hidden:���ز���Ԫ����
    batch_size=20����ÿѵ����20�������ż����ݶȲ����²���
    """
    # �������ݼ�������Ϊѵ��������֤�������Լ���
    datasets = load_data(dataset)
    train_set_x, train_set_y = datasets[0]
    valid_set_x, valid_set_y = datasets[1]
    test_set_x, test_set_y = datasets[2]

    # shape[0]���������һ�д���һ���������ʻ�ȡ����������������batch_size���Եõ��ж��ٸ�batch
    n_train_batches = train_set_x.get_value(borrow=True).shape[0] / batch_size
    n_valid_batches = valid_set_x.get_value(borrow=True).shape[0] / batch_size
    n_test_batches = test_set_x.get_value(borrow=True).shape[0] / batch_size

    print("... building the model")

    index = T.lscalar()  # index��ʾbatch���±꣬����
    x = T.matrix("x")  # x��ʾ���ݼ�
    y = T.ivector("y")  # y��ʾ���һά����

    rng = numpy.random.RandomState(1234)

    # ʵ����һ��MLP������Ϊclassifier
    classifier = MLP(rng=rng, input=x, n_in=28 * 28, n_hidden=n_hidden, n_out=10)

    # ���ۺ������й�����
    # ��y����ʼ��������ʵ����һ�������Ĳ���x��classifier��
    cost = (
        classifier.negative_log_likelihood(y)
        + L1_reg * classifier.L1
        + L2_reg * classifier.L2_sqr
    )

    test_model = theano.function(
        inputs=[index],
        outputs=classifier.errors(y),
        givens={
            x: test_set_x[index * batch_size : (index + 1) * batch_size],
            y: test_set_y[index * batch_size : (index + 1) * batch_size],
        },
    )

    validate_model = theano.function(
        inputs=[index],
        outputs=classifier.errors(y),
        givens={
            x: valid_set_x[index * batch_size : (index + 1) * batch_size],
            y: valid_set_y[index * batch_size : (index + 1) * batch_size],
        },
    )

    # cost�����Ը���������ƫ����ֵ�����ݶȣ�����gparams
    gparams = [T.grad(cost, param) for param in classifier.params]

    # �������¹���
    # updates[(),(),()....],ÿ���������涼��(param, param - learning_rate * gparam)����ÿ�������Լ����ĸ��¹�ʽ
    updates = [
        (param, param - learning_rate * gparam)
        for param, gparam in zip(classifier.params, gparams)
    ]

    # compiling a Theano function `train_model` that returns the cost, but
    # in the same time updates the parameter of the model based on the rules
    # defined in `updates`
    train_model = theano.function(
        inputs=[index],
        outputs=cost,
        updates=updates,
        givens={
            x: train_set_x[index * batch_size : (index + 1) * batch_size],
            y: train_set_y[index * batch_size : (index + 1) * batch_size],
        },
    )

    print("... training")

    patience = 10000  # ����������
    patience_increase = 2  # ����
    improvement_threshold = 0.995  # �൱��ĸ��Ʊ���Ϊ������
    validation_frequency = min(n_train_batches, patience / 2)
    best_validation_loss = numpy.inf
    best_iter = 0
    test_score = 0.0
    start_time = perf_counter()

    epoch = 0
    done_looping = False

    while (epoch < n_epochs) and (not done_looping):
        epoch = epoch + 1
        for minibatch_index in xrange(n_train_batches):
            minibatch_avg_cost = train_model(minibatch_index)
            # ��ǰ������
            iter = (epoch - 1) * n_train_batches + minibatch_index

            if (iter + 1) % validation_frequency == 0:
                validation_losses = [validate_model(i) for i in xrange(n_valid_batches)]
                this_validation_loss = numpy.mean(validation_losses)

                print(
                    "epoch %i, minibatch %i/%i, validation error %f %%"
                    % (
                        epoch,
                        minibatch_index + 1,
                        n_train_batches,
                        this_validation_loss * 100.0,
                    )
                )

                # if we got the best validation score until now
                if this_validation_loss < best_validation_loss:
                    # improve patience if loss improvement is good enough
                    if (
                        this_validation_loss
                        < best_validation_loss * improvement_threshold
                    ):
                        patience = max(patience, iter * patience_increase)

                    best_validation_loss = this_validation_loss
                    best_iter = iter

                    # test it on the test set
                    test_losses = [test_model(i) for i in xrange(n_test_batches)]
                    test_score = numpy.mean(test_losses)

                    print(
                        (
                            "     epoch %i, minibatch %i/%i, test error of "
                            "best model %f %%"
                        )
                        % (
                            epoch,
                            minibatch_index + 1,
                            n_train_batches,
                            test_score * 100.0,
                        )
                    )

            if patience <= iter:
                done_looping = True
                break

    end_time = perf_counter()
    print(
        (
            "Optimization complete. Best validation score of %f %% "
            "obtained at iteration %i, with test performance %f %%"
        )
        % (best_validation_loss * 100.0, best_iter + 1, test_score * 100.0)
    )
    """
    print(>> sys.stderr, ('The code for file ' +
                          os.path.split(__file__)[1] +
                          ' ran for %.2fm' % ((end_time - start_time) / 60.)))
    """


if __name__ == "__main__":
    test_mlp()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# rbm.py

"""This tutorial introduces restricted boltzmann machines (RBM) using Theano.

Boltzmann Machines (BMs) are a particular form of energy-based model which
contain hidden variables. Restricted Boltzmann Machines further restrict BMs
to those without visible-visible and hidden-hidden connections.
"""

try:
    import PIL.Image as Image
except ImportError:
    import Image

import numpy

import theano
import theano.tensor as T

from theano.tensor.shared_randomstreams import RandomStreams

from utils import tile_raster_images
from logistic_sgd import load_data


# start-snippet-1
class RBM(object):
    """Restricted Boltzmann Machine (RBM)"""

    def __init__(
        self,
        input=None,
        n_visible=784,
        n_hidden=500,
        W=None,
        hbias=None,
        vbias=None,
        numpy_rng=None,
        theano_rng=None,
    ):
        """
        RBM constructor. Defines the parameters of the model along with
        basic operations for inferring hidden from visible (and vice-versa),
        as well as for performing CD updates.

        :param input: None for standalone RBMs or symbolic variable if RBM is
        part of a larger graph.

        :param n_visible: number of visible units

        :param n_hidden: number of hidden units

        :param W: None for standalone RBMs or symbolic variable pointing to a
        shared weight matrix in case RBM is part of a DBN network; in a DBN,
        the weights are shared between RBMs and layers of a MLP

        :param hbias: None for standalone RBMs or symbolic variable pointing
        to a shared hidden units bias vector in case RBM is part of a
        different network

        :param vbias: None for standalone RBMs or a symbolic variable
        pointing to a shared visible units bias
        """

        self.n_visible = n_visible
        self.n_hidden = n_hidden

        if numpy_rng is None:
            # create a number generator
            numpy_rng = numpy.random.RandomState(1234)

        if theano_rng is None:
            theano_rng = RandomStreams(numpy_rng.randint(2**30))

        if W is None:
            # W is initialized with `initial_W` which is uniformely
            # sampled from -4*sqrt(6./(n_visible+n_hidden)) and
            # 4*sqrt(6./(n_hidden+n_visible)) the output of uniform if
            # converted using asarray to dtype theano.config.floatX so
            # that the code is runable on GPU
            initial_W = numpy.asarray(
                numpy_rng.uniform(
                    low=-4 * numpy.sqrt(6.0 / (n_hidden + n_visible)),
                    high=4 * numpy.sqrt(6.0 / (n_hidden + n_visible)),
                    size=(n_visible, n_hidden),
                ),
                dtype=theano.config.floatX,
            )
            # theano shared variables for weights and biases
            W = theano.shared(value=initial_W, name="W", borrow=True)

        if hbias is None:
            # create shared variable for hidden units bias
            hbias = theano.shared(
                value=numpy.zeros(n_hidden, dtype=theano.config.floatX),
                name="hbias",
                borrow=True,
            )

        if vbias is None:
            # create shared variable for visible units bias
            vbias = theano.shared(
                value=numpy.zeros(n_visible, dtype=theano.config.floatX),
                name="vbias",
                borrow=True,
            )

        # initialize input layer for standalone RBM or layer0 of DBN
        self.input = input
        if not input:
            self.input = T.matrix("input")

        self.W = W
        self.hbias = hbias
        self.vbias = vbias
        self.theano_rng = theano_rng
        # **** WARNING: It is not a good idea to put things in this list
        # other than shared variables created in this function.
        self.params = [self.W, self.hbias, self.vbias]
        # end-snippet-1

    def free_energy(self, v_sample):
        """Function to compute the free energy"""
        wx_b = T.dot(v_sample, self.W) + self.hbias
        vbias_term = T.dot(v_sample, self.vbias)
        hidden_term = T.sum(T.log(1 + T.exp(wx_b)), axis=1)
        return -hidden_term - vbias_term

    def propup(self, vis):
        """This function propagates the visible units activation upwards to
        the hidden units

        Note that we return also the pre-sigmoid activation of the
        layer. As it will turn out later, due to how Theano deals with
        optimizations, this symbolic variable will be needed to write
        down a more stable computational graph (see details in the
        reconstruction cost function)

        """
        pre_sigmoid_activation = T.dot(vis, self.W) + self.hbias
        return [pre_sigmoid_activation, T.nnet.sigmoid(pre_sigmoid_activation)]

    def sample_h_given_v(self, v0_sample):
        """This function infers state of hidden units given visible units"""
        # compute the activation of the hidden units given a sample of
        # the visibles
        pre_sigmoid_h1, h1_mean = self.propup(v0_sample)
        # get a sample of the hiddens given their activation
        # Note that theano_rng.binomial returns a symbolic sample of dtype
        # int64 by default. If we want to keep our computations in floatX
        # for the GPU we need to specify to return the dtype floatX
        h1_sample = self.theano_rng.binomial(
            size=h1_mean.shape, n=1, p=h1_mean, dtype=theano.config.floatX
        )
        return [pre_sigmoid_h1, h1_mean, h1_sample]

    def propdown(self, hid):
        """This function propagates the hidden units activation downwards to
        the visible units

        Note that we return also the pre_sigmoid_activation of the
        layer. As it will turn out later, due to how Theano deals with
        optimizations, this symbolic variable will be needed to write
        down a more stable computational graph (see details in the
        reconstruction cost function)

        """
        pre_sigmoid_activation = T.dot(hid, self.W.T) + self.vbias
        return [pre_sigmoid_activation, T.nnet.sigmoid(pre_sigmoid_activation)]

    def sample_v_given_h(self, h0_sample):
        """This function infers state of visible units given hidden units"""
        # compute the activation of the visible given the hidden sample
        pre_sigmoid_v1, v1_mean = self.propdown(h0_sample)
        # get a sample of the visible given their activation
        # Note that theano_rng.binomial returns a symbolic sample of dtype
        # int64 by default. If we want to keep our computations in floatX
        # for the GPU we need to specify to return the dtype floatX
        v1_sample = self.theano_rng.binomial(
            size=v1_mean.shape, n=1, p=v1_mean, dtype=theano.config.floatX
        )
        return [pre_sigmoid_v1, v1_mean, v1_sample]

    def gibbs_hvh(self, h0_sample):
        """This function implements one step of Gibbs sampling,
        starting from the hidden state"""
        pre_sigmoid_v1, v1_mean, v1_sample = self.sample_v_given_h(h0_sample)
        pre_sigmoid_h1, h1_mean, h1_sample = self.sample_h_given_v(v1_sample)
        return [pre_sigmoid_v1, v1_mean, v1_sample, pre_sigmoid_h1, h1_mean, h1_sample]

    def gibbs_vhv(self, v0_sample):
        """This function implements one step of Gibbs sampling,
        starting from the visible state"""
        pre_sigmoid_h1, h1_mean, h1_sample = self.sample_h_given_v(v0_sample)
        pre_sigmoid_v1, v1_mean, v1_sample = self.sample_v_given_h(h1_sample)
        return [pre_sigmoid_h1, h1_mean, h1_sample, pre_sigmoid_v1, v1_mean, v1_sample]

    # start-snippet-2
    def get_cost_updates(self, lr=0.1, persistent=None, k=1):
        """This functions implements one step of CD-k or PCD-k

        :param lr: learning rate used to train the RBM

        :param persistent: None for CD. For PCD, shared variable
            containing old state of Gibbs chain. This must be a shared
            variable of size (batch size, number of hidden units).

        :param k: number of Gibbs steps to do in CD-k/PCD-k

        Returns a proxy for the cost and the updates dictionary. The
        dictionary contains the update rules for weights and biases but
        also an update of the shared variable used to store the persistent
        chain, if one is used.

        """

        # compute positive phase
        pre_sigmoid_ph, ph_mean, ph_sample = self.sample_h_given_v(self.input)

        # decide how to initialize persistent chain:
        # for CD, we use the newly generate hidden sample
        # for PCD, we initialize from the old state of the chain
        if persistent is None:
            chain_start = ph_sample
        else:
            chain_start = persistent
        # end-snippet-2
        # perform actual negative phase
        # in order to implement CD-k/PCD-k we need to scan over the
        # function that implements one gibbs step k times.
        # Read Theano tutorial on scan for more information :
        # http://deeplearning.net/software/theano/library/scan.html
        # the scan will return the entire Gibbs chain
        (
            [
                pre_sigmoid_nvs,
                nv_means,
                nv_samples,
                pre_sigmoid_nhs,
                nh_means,
                nh_samples,
            ],
            updates,
        ) = theano.scan(
            self.gibbs_hvh,
            # the None are place holders, saying that
            # chain_start is the initial state corresponding to the
            # 6th output
            outputs_info=[None, None, None, None, None, chain_start],
            n_steps=k,
        )
        # start-snippet-3
        # determine gradients on RBM parameters
        # note that we only need the sample at the end of the chain
        chain_end = nv_samples[-1]

        cost = T.mean(self.free_energy(self.input)) - T.mean(
            self.free_energy(chain_end)
        )
        # We must not compute the gradient through the gibbs sampling
        gparams = T.grad(cost, self.params, consider_constant=[chain_end])
        # end-snippet-3 start-snippet-4
        # constructs the update dictionary
        for gparam, param in zip(gparams, self.params):
            # make sure that the learning rate is of the right dtype
            updates[param] = param - gparam * T.cast(lr, dtype=theano.config.floatX)
        if persistent:
            # Note that this works only if persistent is a shared variable
            updates[persistent] = nh_samples[-1]
            # pseudo-likelihood is a better proxy for PCD
            monitoring_cost = self.get_pseudo_likelihood_cost(updates)
        else:
            # reconstruction cross-entropy is a better proxy for CD
            monitoring_cost = self.get_reconstruction_cost(updates, pre_sigmoid_nvs[-1])

        return monitoring_cost, updates
        # end-snippet-4

    def get_pseudo_likelihood_cost(self, updates):
        """Stochastic approximation to the pseudo-likelihood"""

        # index of bit i in expression p(x_i | x_{\i})
        bit_i_idx = theano.shared(value=0, name="bit_i_idx")

        # binarize the input image by rounding to nearest integer
        xi = T.round(self.input)

        # calculate free energy for the given bit configuration
        fe_xi = self.free_energy(xi)

        # flip bit x_i of matrix xi and preserve all other bits x_{\i}
        # Equivalent to xi[:,bit_i_idx] = 1-xi[:, bit_i_idx], but assigns
        # the result to xi_flip, instead of working in place on xi.
        xi_flip = T.set_subtensor(xi[:, bit_i_idx], 1 - xi[:, bit_i_idx])

        # calculate free energy with bit flipped
        fe_xi_flip = self.free_energy(xi_flip)

        # equivalent to e^(-FE(x_i)) / (e^(-FE(x_i)) + e^(-FE(x_{\i})))
        cost = T.mean(self.n_visible * T.log(T.nnet.sigmoid(fe_xi_flip - fe_xi)))

        # increment bit_i_idx % number as part of updates
        updates[bit_i_idx] = (bit_i_idx + 1) % self.n_visible

        return cost

    def get_reconstruction_cost(self, updates, pre_sigmoid_nv):
        """Approximation to the reconstruction error

        Note that this function requires the pre-sigmoid activation as
        input.  To understand why this is so you need to understand a
        bit about how Theano works. Whenever you compile a Theano
        function, the computational graph that you pass as input gets
        optimized for speed and stability.  This is done by changing
        several parts of the subgraphs with others.  One such
        optimization expresses terms of the form log(sigmoid(x)) in
        terms of softplus.  We need this optimization for the
        cross-entropy since sigmoid of numbers larger than 30. (or
        even less then that) turn to 1. and numbers smaller than
        -30. turn to 0 which in terms will force theano to compute
        log(0) and therefore we will get either -inf or NaN as
        cost. If the value is expressed in terms of softplus we do not
        get this undesirable behaviour. This optimization usually
        works fine, but here we have a special case. The sigmoid is
        applied inside the scan op, while the log is
        outside. Therefore Theano will only see log(scan(..)) instead
        of log(sigmoid(..)) and will not apply the wanted
        optimization. We can not go and replace the sigmoid in scan
        with something else also, because this only needs to be done
        on the last step. Therefore the easiest and more efficient way
        is to get also the pre-sigmoid activation as an output of
        scan, and apply both the log and sigmoid outside scan such
        that Theano can catch and optimize the expression.

        """

        cross_entropy = T.mean(
            T.sum(
                self.input * T.log(T.nnet.sigmoid(pre_sigmoid_nv))
                + (1 - self.input) * T.log(1 - T.nnet.sigmoid(pre_sigmoid_nv)),
                axis=1,
            )
        )

        return cross_entropy


def test_rbm(
    learning_rate=0.1,
    training_epochs=15,
    dataset="mnist.pkl.gz",
    batch_size=20,
    n_chains=20,
    n_samples=10,
    output_folder="rbm_plots",
    n_hidden=500,
):
    """
    Demonstrate how to train and afterwards sample from it using Theano.

    This is demonstrated on MNIST.

    :param learning_rate: learning rate used for training the RBM

    :param training_epochs: number of epochs used for training

    :param dataset: path the the pickled dataset

    :param batch_size: size of a batch used to train the RBM

    :param n_chains: number of parallel Gibbs chains to be used for sampling

    :param n_samples: number of samples to plot for each chain

    """
    datasets = load_data(dataset)

    train_set_x, train_set_y = datasets[0]
    test_set_x, test_set_y = datasets[2]

    # compute number of minibatches for training, validation and testing
    n_train_batches = train_set_x.get_value(borrow=True).shape[0] / batch_size

    # allocate symbolic variables for the data
    index = T.lscalar()  # index to a [mini]batch
    x = T.matrix("x")  # the data is presented as rasterized images

    rng = numpy.random.RandomState(123)
    theano_rng = RandomStreams(rng.randint(2**30))

    # initialize storage for the persistent chain (state = hidden
    # layer of chain)
    persistent_chain = theano.shared(
        numpy.zeros((batch_size, n_hidden), dtype=theano.config.floatX), borrow=True
    )

    # construct the RBM class
    rbm = RBM(
        input=x,
        n_visible=28 * 28,
        n_hidden=n_hidden,
        numpy_rng=rng,
        theano_rng=theano_rng,
    )

    # get the cost and the gradient corresponding to one step of CD-15
    cost, updates = rbm.get_cost_updates(
        lr=learning_rate, persistent=persistent_chain, k=15
    )

    #################################
    #     Training the RBM          #
    #################################
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)
    os.chdir(output_folder)

    # start-snippet-5
    # it is ok for a theano function to have no output
    # the purpose of train_rbm is solely to update the RBM parameters
    train_rbm = theano.function(
        [index],
        cost,
        updates=updates,
        givens={x: train_set_x[index * batch_size : (index + 1) * batch_size]},
        name="train_rbm",
    )

    plotting_time = 0.0
    start_time = perf_counter()

    # go through training epochs
    for epoch in range(training_epochs):
        # go through the training set
        mean_cost = []
        for batch_index in range(n_train_batches):
            mean_cost += [train_rbm(batch_index)]

        print("Training epoch %d, cost is " % epoch, numpy.mean(mean_cost))

        # Plot filters after each training epoch
        plotting_start = perf_counter()
        # Construct image from the weight matrix
        image = Image.fromarray(
            tile_raster_images(
                X=rbm.W.get_value(borrow=True).T,
                img_shape=(28, 28),
                tile_shape=(10, 10),
                tile_spacing=(1, 1),
            )
        )
        image.save("filters_at_epoch_%i.png" % epoch)
        plotting_stop = perf_counter()
        plotting_time += plotting_stop - plotting_start

    end_time = perf_counter()

    pretraining_time = (end_time - start_time) - plotting_time

    print(("Training took %f minutes" % (pretraining_time / 60.0)))
    # end-snippet-5 start-snippet-6
    #################################
    #     Sampling from the RBM     #
    #################################
    # find out the number of test samples
    number_of_test_samples = test_set_x.get_value(borrow=True).shape[0]

    # pick random test examples, with which to initialize the persistent chain
    test_idx = rng.randint(number_of_test_samples - n_chains)
    persistent_vis_chain = theano.shared(
        numpy.asarray(
            test_set_x.get_value(borrow=True)[test_idx : test_idx + n_chains],
            dtype=theano.config.floatX,
        )
    )
    # end-snippet-6 start-snippet-7
    plot_every = 1000
    # define one step of Gibbs sampling (mf = mean-field) define a
    # function that does `plot_every` steps before returning the
    # sample for plotting
    (
        [presig_hids, hid_mfs, hid_samples, presig_vis, vis_mfs, vis_samples],
        updates,
    ) = theano.scan(
        rbm.gibbs_vhv,
        outputs_info=[None, None, None, None, None, persistent_vis_chain],
        n_steps=plot_every,
    )

    # add to updates the shared variable that takes care of our persistent
    # chain :.
    updates.update({persistent_vis_chain: vis_samples[-1]})
    # construct the function that implements our persistent chain.
    # we generate the "mean field" activations for plotting and the actual
    # samples for reinitializing the state of our persistent chain
    sample_fn = theano.function(
        [], [vis_mfs[-1], vis_samples[-1]], updates=updates, name="sample_fn"
    )

    # create a space to store the image for plotting ( we need to leave
    # room for the tile_spacing as well)
    image_data = numpy.zeros((29 * n_samples + 1, 29 * n_chains - 1), dtype="uint8")
    for idx in range(n_samples):
        # generate `plot_every` intermediate samples that we discard,
        # because successive samples in the chain are too correlated
        vis_mf, vis_sample = sample_fn()
        print(" ... plotting sample ", idx)
        image_data[29 * idx : 29 * idx + 28, :] = tile_raster_images(
            X=vis_mf, img_shape=(28, 28), tile_shape=(1, n_chains), tile_spacing=(1, 1)
        )

    # construct image
    image = Image.fromarray(image_data)
    image.save("samples.png")
    # end-snippet-7
    os.chdir("../")


if __name__ == "__main__":
    test_rbm()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# stage_1.py

import theano
import theano.tensor as T

# 定义矩阵与矩阵运算
X = T.matrix("X")
results, updates = theano.scan(lambda x_i: T.sqrt((x_i**2).sum()), sequences=[X])
compute_norm_lines = theano.function(inputs=[X], outputs=[results])

# np.diag:对角阵
x = np.diag(np.arange(1, 6, dtype=theano.config.floatX), 1)
print(compute_norm_lines(x)[0])

# comparison with numpy
print(np.sqrt((x**2).sum(1)))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# stage_2.py

import theano
import theano.tensor as T

# 行数为row;列数为column
row = 3
column = 3
# -----------------定义符号函数代码-----------------#
# 1. 初始化一个Theano张量
A = theano.shared(
    # numpy.ones((row, column)矩阵的值; dtype=浮点数类型：float32:
    value=np.ones((row, column), dtype=theano.config.floatX),
    name="A",  # 变量名
    borrow=True,  # 与numpy共享array的内存空间
)

# 使用numpy array初始化
Xlist = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
B = theano.shared(
    value=np.array(Xlist, dtype=theano.config.floatX), name="B", borrow=True
)
x = T.dmatrix("x")
y = T.dmatrix("y")
z = T.vector("z")
out = T.mean(x + y)  # 计算均值
myfunc1 = theano.function(inputs=[], outputs=out, givens=[(x, A), (y, B)])  # 指定函数参数
# 遍历List
C = theano.shared(np.asarray([1.0, 2.0, 3.0, 4.0, 5.0], dtype=theano.config.floatX))
idx = T.lscalar("idx")
f1 = T.sum(z)  # 求和
myfunc2 = theano.function([idx], outputs=f1, givens={z: C[0:idx]})


# -----------------输出函数运行结果-----------------#
print(A.get_value())
print(np.shape(B.get_value()))
print(myfunc1())
print(myfunc2(4))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# stage_3.py

import theano
import theano.tensor as T
from theano import function

# 定义向量
XWB = [[3, 1], [-1, -2], [-1, 5]]
X = np.array(XWB[0], dtype=theano.config.floatX)
W = np.array(XWB[1], dtype=theano.config.floatX)
B = np.array(XWB[2], dtype=theano.config.floatX)


logX = T.log(X)  # 计算对数
print(logX.eval())
meanW = T.mean(W)  # 计算均值
print(meanW.eval())
neqW = T.neq(W, B)  # 返回X!=B的逻辑结果
print(neqW.eval())

x = T.dscalar("x")
y = x**2 + 10
grady = T.grad(y, x)  # 计算梯度
f = function([x], grady)
print(f(100))
# 计算softmax函数
Y_pred = T.nnet.softmax(T.dot(X, W) + B)
print(Y_pred.eval())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# testTheano.py

from theano import function, config, shared, sandbox
import theano.tensor as T
import numpy

t1 = time.time()
vlen = 10 * 30 * 768  # 10 x #cores x # threads per core
iters = 1000

x = shared(numpy.asarray(np.random.rand(vlen), config.floatX))
f = function([], T.exp(x))
print(f.maker.fgraph.toposort())
t0 = time.time()
for i in range(iters):
    r = f()

print("Looping %d times took" % iters, t1 - t0, "seconds")
print("Result is", r)
if numpy.any([isinstance(x.op, T.Elemwise) for x in f.maker.fgraph.toposort()]):
    print("Used the cpu")
else:
    print("Used the gpu")
print(time.time() - t1)


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
