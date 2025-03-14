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
卷积+下采样合成一个层LeNetConvPoolLayer 
rng:随机数生成器，用于初始化W 
input:4维的向量，theano.tensor.dtensor4 
filter_shape:(number of filters, num input feature maps,filter height, filter width) 
image_shape:(batch size, num input feature maps,image height, image width) 
poolsize: (#rows, #cols) 
"""  
class LeNetConvPoolLayer(object):
    def __init__(self, rng, input, filter_shape, image_shape, poolsize=(2, 2)):
        #assert condition，condition为True，则继续往下执行，condition为False，中断程序  
        #image_shape[1]和filter_shape[1]都是num input feature maps，它们必须是一样的。  
        assert image_shape[1] == filter_shape[1]
        self.input = input    
        #每个隐层神经元（即像素）与上一层的连接数为num input feature maps * filter height * filter width。  
        #可以用numpy.prod(filter_shape[1:])来求得
        fan_in = numpy.prod(filter_shape[1:])
        #lower layer上每个神经元获得的梯度来自于："num output feature maps * filter height * filter width" /pooling size  
        fan_out = (filter_shape[0] * numpy.prod(filter_shape[2:]) /
                   numpy.prod(poolsize))
        #以上求得fan_in、fan_out ，将它们代入公式，以此来随机初始化W,W就是线性卷积核
        W_bound = numpy.sqrt(6. / (fan_in + fan_out))
        self.W = theano.shared(
            numpy.asarray(
                rng.uniform(low=-W_bound, high=W_bound, size=filter_shape), dtype=theano.config.floatX ),
            borrow=True
        )
        #偏置b是一维向量，每个输出图的特征图都对应一个偏置，  
        #而输出的特征图的个数由filter个数决定，因此用filter_shape[0]即number of filters来初始化 
        b_values = numpy.zeros((filter_shape[0],), dtype=theano.config.floatX)
        self.b = theano.shared(value=b_values, borrow=True)
        #将输入图像与filter卷积，conv.conv2d函数  
        #卷积完没有加b再通过sigmoid，这里是一处简化。
        conv_out = conv.conv2d(
            input=input,
            filters=self.W,
            filter_shape=filter_shape,
            image_shape=image_shape
        )
        # maxpooling，最大子采样过程
        pooled_out = downsample.max_pool_2d(
            input=conv_out,
            ds=poolsize,
            ignore_border=True
        )
        #加偏置，再通过tanh映射，得到卷积+子采样层的最终输出  
        self.output = T.tanh(pooled_out + self.b.dimshuffle('x', 0, 'x', 'x'))
        #卷积+采样层的参数  
        self.params = [self.W, self.b]
        
    # 存储执行参数
    def save_net(self, path):  
        import pickle
        write_file = open(path, 'wb')   
        pickle.dump(self.params, write_file, -1)
        write_file.close()    

# 实现LeNet5 ：LeNet5有两个卷积层，第一个卷积层有20个卷积核，第二个卷积层有50个卷积核
# learning_rate:学习速率，随机梯度前的系数。 
# n_epochs训练步数，每一步都会遍历所有batch，即所有样本 
# batch_size,这里设置为500，即每遍历完500个样本，才计算梯度并更新参数 
# nkerns=[20, 50],每一个LeNetConvPoolLayer卷积核的个数，第一个LeNetConvPoolLayer有 
# 20个卷积核，第二个有50个  
def evaluate_lenet5(learning_rate=0.1, n_epochs=200, dataset='mnist.pkl.gz', nkerns=[20, 50], batch_size=500):
    rng = numpy.random.RandomState(23455)
    datasets = load_data(dataset)  #加载数据
    train_set_x, train_set_y = datasets[0]
    valid_set_x, valid_set_y = datasets[1]
    test_set_x, test_set_y = datasets[2]

    n_train_batches = train_set_x.get_value(borrow=True).shape[0]
    n_valid_batches = valid_set_x.get_value(borrow=True).shape[0]
    n_test_batches = test_set_x.get_value(borrow=True).shape[0]
    n_train_batches /= batch_size
    n_valid_batches /= batch_size
    n_test_batches /= batch_size
    # 定义几个变量，index表示batch下标，x表示输入的训练数据，y对应其标签  
    index = T.lscalar()  
    x = T.matrix('x')   
    y = T.ivector('y')  
    ############
    # 构建模型 #
    ############
    print '... building the model'
    # 我们加载进来的batch大小的数据是(batch_size, 28 * 28)，但是LeNetConvPoolLayer的输入是四维的，所以要reshape
    layer0_input = x.reshape((batch_size, 1, 28, 28))
    # layer0即第一个LeNetConvPoolLayer层  
    # 输入的单张图片(28,28)，经过conv得到(28-5+1 , 28-5+1) = (24, 24)，  
    # 经过maxpooling得到(24/2, 24/2) = (12, 12)  
    # 因为每个batch有batch_size张图，第一个LeNetConvPoolLayer层有nkerns[0]个卷积核，  
    # 故layer0输出为(batch_size, nkerns[0], 12, 12) 
    layer0 = LeNetConvPoolLayer(
        rng, input=layer0_input, 
        image_shape=(batch_size, 1, 28, 28),
        filter_shape=(nkerns[0], 1, 5, 5), 
        poolsize=(2, 2)
    )
    # layer1即第二个LeNetConvPoolLayer层  
    # 输入是layer0的输出，每张特征图为(12,12),经过conv得到(12-5+1, 12-5+1) = (8, 8),  
    # 经过maxpooling得到(8/2, 8/2) = (4, 4)  
    # 因为每个batch有batch_size张图（特征图），第二个LeNetConvPoolLayer层有nkerns[1]个卷积核  
    # ，故layer1输出为(batch_size, nkerns[1], 4, 4)  
    layer1 = LeNetConvPoolLayer(
        rng,  input=layer0.output,
        image_shape=(batch_size, nkerns[0], 12, 12),
        filter_shape=(nkerns[1], nkerns[0], 5, 5),
        poolsize=(2, 2)
    )
    #前面定义好了两个LeNetConvPoolLayer（layer0和layer1），layer1后面接layer2，这是一个全连接层，相当于MLP里面的隐含层  
    #故可以用MLP中定义的HiddenLayer来初始化layer2，layer2的输入是二维的(batch_size, num_pixels) ，  
    #故要将上层中同一张图经不同卷积核卷积出来的特征图合并为一维向量，  
    #也就是将layer1的输出(batch_size, nkerns[1], 4, 4)flatten为(batch_size, nkerns[1]*4*4)=(500，800),作为layer2的输入。  
    #(500，800)表示有500个样本，每一行代表一个样本。layer2的输出大小是(batch_size,n_out)=(500,500) 
    layer2_input = layer1.output.flatten(2)
    layer2 = HiddenLayer(
        rng,
        input=layer2_input,
        n_in=nkerns[1] * 4 * 4,
        n_out=500,
        activation=T.tanh
    )
    # 最后一层layer3是分类层，用的是逻辑回归中定义的LogisticRegression，  
    # layer3的输入是layer2的输出(500,500)，layer3的输出就是(batch_size,n_out)=(500,10) 
    layer3 = LogisticRegression(input=layer2.output, n_in=500, n_out=10)
    # 代价函数NLL  
    cost = layer3.negative_log_likelihood(y)
    # test_model计算测试误差，x、y根据给定的index具体化，然后调用layer3，  
    # layer3又会逐层地调用layer2、layer1、layer0，故test_model其实就是整个CNN结构，  
    # test_model的输入是x、y，输出是layer3.errors(y)的输出，即误差。
    test_model = theano.function(
        [index],
        layer3.errors(y),
        givens={
            x: test_set_x[index * batch_size: (index + 1) * batch_size],
            y: test_set_y[index * batch_size: (index + 1) * batch_size]
        }
    )
    validate_model = theano.function(
        [index],
        layer3.errors(y),
        givens={
            x: valid_set_x[index * batch_size: (index + 1) * batch_size],
            y: valid_set_y[index * batch_size: (index + 1) * batch_size]
        }
    )    
    # 下面是train_model，涉及到优化算法即SGD，需要计算梯度、更新参数     
    params = layer3.params + layer2.params + layer1.params + layer0.params  # 参数集  
    grads = T.grad(cost, params) # 对各个参数的梯度
    # 因为参数太多，在updates规则里面一个一个具体地写出来是很麻烦的，
    # 所以下面用了一个for..in..,自动生成规则对(param_i, param_i - learning_rate * grad_i)
    updates = [ (param_i, param_i - learning_rate * grad_i) for param_i, grad_i in zip(params, grads) ]
    #train_model，代码分析同test_model。train_model里比test_model、validation_model多出updates规则
    train_model = theano.function(
        [index],
        cost,
        updates=updates,
        givens={
            x: train_set_x[index * batch_size: (index + 1) * batch_size],
            y: train_set_y[index * batch_size: (index + 1) * batch_size]
        }
    )
    ############
    # 训练模型 #
    ############
    print '... training'    
    patience = 10000 # 提早终止参数
    patience_increase = 2 
    improvement_threshold = 0.995  
    # 这样设置validation_frequency可以保证每一次epoch都会在验证集上测试。
    validation_frequency = min(n_train_batches, patience / 2)
    best_validation_loss = numpy.inf
    best_iter = 0
    test_score = 0.
    start_time = time.clock()
    epoch = 0
    done_looping = False
    while (epoch < n_epochs) and (not done_looping):
        epoch = epoch + 1
        for minibatch_index in xrange(n_train_batches):
            iter = (epoch - 1) * n_train_batches + minibatch_index
            if iter % 100 == 0:
            	print 'training @ iter = ', iter
            cost_ij = train_model(minibatch_index)
            if (iter + 1) % validation_frequency == 0:
                validation_losses = [validate_model(i) for i in xrange(n_valid_batches)]
                this_validation_loss = numpy.mean(validation_losses)
                print('epoch %i, minibatch %i/%i, validation error %f %%' %
                      (epoch, minibatch_index + 1, n_train_batches, this_validation_loss * 100.))
                if this_validation_loss < best_validation_loss:
                    if this_validation_loss < best_validation_loss * improvement_threshold:
                        patience = max(patience, iter * patience_increase)
                    best_validation_loss = this_validation_loss
                    best_iter = iter
                    test_losses = [ test_model(i) for i in xrange(n_test_batches) ]
                    test_score = numpy.mean(test_losses)
                    print(('     epoch %i, minibatch %i/%i, test error of ' 'best model %f %%') %
                          (epoch, minibatch_index + 1, n_train_batches, test_score * 100.))

            if patience <= iter:
                done_looping = True
                break
    layer0.save_net("layer0")
    layer1.save_net("layer1")
    layer2.save_net("layer2")
    layer3.save_net("layer3")
    end_time = time.clock()
    print('Optimization complete.')
    print('Best validation score of %f %% obtained at iteration %i, ' 'with test performance %f %%' %
          (best_validation_loss * 100., best_iter + 1, test_score * 100.))
    print >> sys.stderr, ('The code for file ' + os.path.split(__file__)[1] + ' ran for %.2fm' % ((end_time - start_time) / 60.))

if __name__ == '__main__':
    evaluate_lenet5()


def experiment(state, channel):
    evaluate_lenet5(state.learning_rate, dataset=state.dataset)
