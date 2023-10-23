# -*- coding: utf-8 -*-

"""
���̳̽�����ʹ��Theano������ݶ��½�logistic�ع顣Logistic�ع���һ�����ʵģ����Է�������
����һ����������Ȩ�ؾ���:"W"��һ��ƫ������'b'��
��������ͨ��ͶӰ���ݵ㵽һ�鳬ƽ�����ɣ����뱻����ȷ��һ������Ա���ʡ�
����дΪ:
���̳̽����������ڴ������ݼ�����ݶ��½��Ż�������

"""
__docformat__ = 'restructedtext en'

import cPickle
import gzip
import os
import sys
import time
import numpy
import theano
import theano.tensor as T

class LogisticRegression(object):
    def __init__(self, input, n_in, n_out):

        # ��ʼ��Ȩ��WΪȫ0���� shape(n_in, n_out) W ��һ�����󣬵�k�б�ʾΪ��k��ķָ���ƽ��
        self.W = theano.shared(
            value=numpy.zeros((n_in, n_out), dtype=theano.config.floatX ),
            name='W',
            borrow=True
        )
        # ��ʼ��ƫ����bΪȫ0������n_out 0; b �Ǹ�����������Ԫ��k��ʾΪ��ƽ��k�����ɲ���
        self.b = theano.shared(
            value=numpy.zeros((n_out,), dtype=theano.config.floatX ),
            name='b',
            borrow=True
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

    def errors(self, y): # batch�������  
        # ���y��y_pred�Ƿ�����ͬ��ά��
        if y.ndim != self.y_pred.ndim:
            raise TypeError(
                'y should have the same shape as self.y_pred',('y', y.type, 'y_pred', self.y_pred.type)
            )
        # ���y�Ƿ�����ȷ����������
        if y.dtype.startswith('int'): 
            # �ټ���ǲ���int���ͣ��ǵĻ�����T.neq(self.y_pred, y)�ľ�ֵ����Ϊ�����  
            # �ٸ����ӣ�����self.y_pred=[3,2,3,2,3,2],��ʵ����y=[3,4,3,4,3,4]  
            # ��T.neq(self.y_pred, y)=[0,1,0,1,0,1],1��ʾ���ȣ�0��ʾ���  
            # ��T.mean(T.neq(self.y_pred, y))=T.mean([0,1,0,1,0,1])=0.5����������50%            
            return T.mean(T.neq(self.y_pred, y)) # T.neq������������һ��0��1������������1��ʾһ��Ԥ�����
        else:
            raise NotImplementedError()
    def save_net(self, path):  
        import cPickle  
        write_file = open(path, 'wb')   
        cPickle.dump(self.W.get_value(borrow=True), write_file, -1)  
        cPickle.dump(self.b.get_value(borrow=True), write_file, -1)  
        write_file.close()

##############
# �������ݼ� #
##############
def load_data(dataset):
    # ������ز����ھʹ������������ݼ�
    data_dir, data_file = os.path.split(dataset)
    if data_dir == "" and not os.path.isfile(dataset):
        # ������ݼ��Ƿ�������Ŀ¼��.
        new_path = os.path.join(
            os.path.split(__file__)[0], "..", "data", dataset
        )
        if os.path.isfile(new_path) or data_file == 'mnist.pkl.gz':
            dataset = new_path

    if (not os.path.isfile(dataset)) and data_file == 'mnist.pkl.gz':
        import urllib
        origin = ( 'http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz' )
        print 'Downloading data from %s' % origin
        urllib.urlretrieve(origin, dataset)

    print '... loading data'

    # �������ݼ�������
    f = gzip.open(dataset, 'rb')
    train_set, valid_set, test_set = cPickle.load(f)
    f.close()
    
    # �����հ���ѵ����, ��֤��, ���Լ���ʽ: tuple(input, target)
    # ����ʱһ����ά��numpy.ndarray (��һ������)
    # ����ÿһ�ж���һ������. Ŀ���Ǹ�һά��numpy.ndarray (vector))������������ͬ���ĳ��� 
    # ��Ӧ�ø���һ������������������ͬ������Ŀ�ꡣ
    def shared_dataset(data_xy, borrow=True):

        data_x, data_y = data_xy
        shared_x = theano.shared(numpy.asarray(data_x, dtype=theano.config.floatX), borrow=borrow)
        shared_y = theano.shared(numpy.asarray(data_y, dtype=theano.config.floatX), borrow=borrow)
        # ���洢���ݵ�GPUʱ�����ݱ���Ϊfloat��ʽ��������ǽ���ǩ�洢Ϊ"floatX"
        # ���ڼ����ڼ䣬������Ҫ������Ϊint��(��Ϊ����������������Ǹ�����
        # �����������)������֮�����ǽ���ת��Ϊint�����ǻرܸ������һ������
        return shared_x, T.cast(shared_y, 'int32')

    test_set_x, test_set_y = shared_dataset(test_set)
    valid_set_x, valid_set_y = shared_dataset(valid_set)
    train_set_x, train_set_y = shared_dataset(train_set)

    rval = [(train_set_x, train_set_y), (valid_set_x, valid_set_y),
            (test_set_x, test_set_y)]
    return rval
# ��ִ�к���
# learning_rate=0.13, ���ݶ��½�����Ȩ�ظ�����
# n_epochs=1000, ����������
# dataset='mnist.pkl.gz', ���ݼ�
# batch_size=600 ����С
def sgd_optimization_mnist(learning_rate=0.13, n_epochs=1000, dataset='mnist.pkl.gz',batch_size=600):

    datasets = load_data(dataset)

    train_set_x, train_set_y = datasets[0]
    valid_set_x, valid_set_y = datasets[1]
    test_set_x, test_set_y = datasets[2]

    # �����ж��ٸ�minibatch����Ϊ���ǵ��Ż��㷨��MSGD����һ��batchһ��batch������cost��
    n_train_batches = train_set_x.get_value(borrow=True).shape[0] / batch_size
    n_valid_batches = valid_set_x.get_value(borrow=True).shape[0] / batch_size
    n_test_batches = test_set_x.get_value(borrow=True).shape[0] / batch_size

    ############
    # ����ģ�� #
    ############
    print '... building the model'
    
    # ���ñ�����index��ʾminibatch���±꣬x��ʾѵ��������y�Ƕ�Ӧ��label  
    index = T.lscalar()  # ��������    
    x = T.matrix('x')   # ����, ����Ϊ��դͼ��
    y = T.ivector('y')  # ��ǩ, ����Ϊ[INT]��ǩ��1ά����

    # ʵ����logisitic��������ÿ��MNIST ͼ�ĳߴ�Ϊ 28*28 ��x����input��ʼ���� 
    classifier = LogisticRegression(input=x, n_in=28*28, n_out=10)
    # ������ۣ���y����ʼ��������ʵ����һ�������Ĳ���Input
    cost = classifier.negative_log_likelihood(y) # ��������Ȼ�Ĵ���
    # �������ģ�ͣ�����ָ��
    test_model = theano.function(
        inputs=[index], outputs=classifier.errors(y),
        givens={
            x: test_set_x[index * batch_size: (index + 1) * batch_size],
            y: test_set_y[index * batch_size: (index + 1) * batch_size]
        }
    )
    # ������֤ģ�ͣ�����ָ��
    validate_model = theano.function(
        inputs=[index], outputs=classifier.errors(y),
        givens={
            x: valid_set_x[index * batch_size: (index + 1) * batch_size],
            y: valid_set_y[index * batch_size: (index + 1) * batch_size]
        }
    )

    # ����theta = (W,b)���ݶ�
    g_W = T.grad(cost=cost, wrt=classifier.W)
    g_b = T.grad(cost=cost, wrt=classifier.b)

    # learning_rate���ݶ��½�����Ȩ�ظ�����
    updates = [(classifier.W, classifier.W - learning_rate * g_W),(classifier.b, classifier.b - learning_rate * g_b)]

    # ����ָ�붨��ѵ��ģ��
    train_model = theano.function(
        inputs=[index], outputs=cost, updates=updates,
        givens={
            x: train_set_x[index * batch_size: (index + 1) * batch_size],
            y: train_set_y[index * batch_size: (index + 1) * batch_size]
        }
    )

    ###############
    #   ѵ��ģ��  #
    ###############
    print '... training the model'
    patience = 5000  # ����������
    patience_increase = 2   # ����
    # ��ߵ���ֵ������֤����С��֮ǰ��0.995��ʱ�������best_validation_loss     
    improvement_threshold = 0.995  # �൱��ĸ��Ʊ���Ϊ������
    # ��������validation_frequency���Ա�֤ÿһ��epoch��������֤���ϲ��ԡ�  
    validation_frequency = min(n_train_batches, patience / 2)
    best_validation_loss = numpy.inf # ��õ���֤���ϵ�loss��ԽС��Խ�á���ʼ��Ϊ�����  
    test_score = 0.
    start_time = time.clock() # ��ʼʱ��

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
            iter = (epoch - 1) * n_train_batches + minibatch_index # �ۼ�ѵ������batch��iter��
            # ��iter��validation_frequency����ʱ�������֤���ϲ��ԣ�
            if (iter + 1) % validation_frequency == 0:                
                validation_losses = [validate_model(i) for i in xrange(n_valid_batches)] # ������֤������ʧ����
                this_validation_loss = numpy.mean(validation_losses)
                # ���
                print(
                    'epoch %i, minibatch %i/%i, validation error %f %%' %
                    (
                        epoch,  minibatch_index + 1, n_train_batches,  this_validation_loss * 100.
                    )
                )
                # �����֤������ʧthis_validation_lossС��֮ǰ��ѵ���ʧbest_validation_loss��  
                # �����best_validation_loss��best_iter��ͬʱ��testset�ϲ��ԡ�  
                # �����֤������ʧthis_validation_lossС��best_validation_loss*improvement_thresholdʱ�����patience��
                if this_validation_loss < best_validation_loss:
                    if this_validation_loss < best_validation_loss * improvement_threshold:
                        patience = max(patience, iter * patience_increase)
                    best_validation_loss = this_validation_loss
                    test_losses = [test_model(i) for i in xrange(n_test_batches)]
                    test_score = numpy.mean(test_losses)

                    print(
                        (
                            '     epoch %i, minibatch %i/%i, test error of'
                            ' best model %f %%'
                        ) %
                        (
                            epoch, minibatch_index + 1, n_train_batches, test_score * 100.
                        )
                    )
            if patience <= iter: # �ﵽ�������������˳�
                done_looping = True
                break
    classifier.save_net("convnet.data") # ��������ѵ����������Ľ��������
    # whileѭ������
    end_time = time.clock() # ����ʱ��
    # ���
    print(
        (
            'Optimization complete with best validation score of %f %%,'
            'with test performance %f %%'
        )
        % (best_validation_loss * 100., test_score * 100.)
    )
    print 'The code run for %d epochs, with %f epochs/sec' % ( epoch, 1. * epoch / (end_time - start_time))
    print >> sys.stderr, ('The code for file ' + os.path.split(__file__)[1] + ' ran for %.1fs' % ((end_time - start_time)))





if __name__ == '__main__':
    sgd_optimization_mnist()
