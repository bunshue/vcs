
import tensorflow as tf
import numpy as np
 
 
def maxPoolLayer(x, kHeight, kWidth, strideX, strideY, name, padding='SAME'):
    """max-pooling"""
    return tf.nn.max_pool(x, ksize=[1, kHeight, kWidth, 1], strides=[1, strideX, strideY, 1], padding=padding,
                          name=name)
 
 
def dropout(x, keepPro, name=None):
    """dropout"""
    return tf.nn.dropout(x, keepPro, name)
 
 
def LRN(x, R, alpha, beta, name=None, bias=1.0):
    """LRN"""
    return tf.nn.local_response_normalization(x, depth_radius=R, alpha=alpha, beta=beta, bias=bias, name=name)
 
 
def fcLayer(x, inputD, outputD, reluFlag, name):
    """fully-connect"""
    with tf.variable_scope(name) as scope:
        w = tf.get_variable('w', shape=[inputD, outputD], dtype='float')
        b = tf.get_variable('b', [outputD], dtype='float')
        out = tf.nn.xw_plus_b(x, w, b, name=scope.name)
        if reluFlag:
            return tf.nn.relu(out)
        else:
            return out
 
# groups=1：一层；groups=2：上下两层
def convLayer(x, kHeight, kWidth, strideX, strideY, featureNum, name, padding='SAME', groups=1):
    """convlutional"""
    # 三通道
    channel = int(x.get_shape()[-1])
    conv = lambda a, b: tf.nn.conv2d(a, b, strides=[1, strideY, strideX, 1], padding=padding)
    with tf.variable_scope(name) as scope:
        w = tf.get_variable('w', shape=[kHeight, kWidth, channel / groups, featureNum])
        b = tf.get_variable('b', shape=[featureNum])
 
        # xNew是一个输入，wNew是权重。是否根据groups值把特征图的数量分成两部分。
        xNew = tf.split(value=x, num_or_size_splits=groups, axis=3)
        wNew = tf.split(value=w, num_or_size_splits=groups, axis=3)
 
        # featureMap：执行完卷积操作后的结果
        featureMap = [conv(t1, t2) for t1, t2 in zip(xNew, wNew)]
        # 如果分成上下两层，则把结果合并到一起
        mergeFeatureMap = tf.concat(axis=3, values=featureMap)
        # 加偏置项
        out = tf.nn.bias_add(mergeFeatureMap, b)
        return tf.nn.relu(tf.reshape(out, mergeFeatureMap.get_shape().as_list()), name=scope.name)
 
 
class alexNet(object):
    """alexNet model"""
    # bvlc_alexnet.npy文件里面保存的是Alex模型训练好的权重参数
    def __init__(self, x, keepPro, classNum, skip, modelPath='bvlc_alexnet.npy'):
        self.X = x
        self.KEEPPRO = keepPro
        self.CLASSNUM = classNum
        self.SKIP = skip
        self.MODELPATH = modelPath
        # build CNN
        self.buildCNN()
 
    def buildCNN(self):
        """build model"""
        # 卷积核11*11，步长4，特征图个数96（上下两层各48）
        conv1 = convLayer(self.X, 11, 11, 4, 4, 96, "conv1", "VALID")
        pool1 = maxPoolLayer(conv1, 3, 3, 2, 2, "pool1", "VALID")
        lrn1 = LRN(pool1, 2, 2e-05, 0.75, "norm1")
 
        # groups=2：分成了上下两层
        conv2 = convLayer(lrn1, 5, 5, 1, 1, 256, "conv2", groups=2)
        pool2 = maxPoolLayer(conv2, 3, 3, 2, 2, "pool2", "VALID")
        lrn2 = LRN(pool2, 2, 2e-05, 0.75, "lrn2")
 
        conv3 = convLayer(lrn2, 3, 3, 1, 1, 384, "conv3")
 
        conv4 = convLayer(conv3, 3, 3, 1, 1, 384, "conv4", groups=2)
 
        conv5 = convLayer(conv4, 3, 3, 1, 1, 256, "conv5", groups=2)
        pool5 = maxPoolLayer(conv5, 3, 3, 2, 2, "pool5", "VALID")
 
        fcIn = tf.reshape(pool5, [-1, 256 * 6 * 6])
        fc1 = fcLayer(fcIn, 256 * 6 * 6, 4096, True, 'fc6')
        dropout1 = dropout(fc1, self.KEEPPRO)
 
        fc2 = fcLayer(dropout1, 4096, 4096, True, 'fc7')
        dropout2 = dropout(fc2, self.KEEPPRO)
 
        self.fc3 = fcLayer(dropout2, 4096, self.CLASSNUM, True, 'fc8')
 
    def loadModel(self, sess):
        """load model"""
        # 加载已训练好模型的权重、偏置参数
        wDict = np.load(self.MODELPATH, encoding="bytes").item()
 
        for name in wDict:
            if name not in self.SKIP:
                with tf.variable_scope(name, reuse=True):
                    for p in wDict[name]:
                        if len(p.shape) == 1:
                            # bias
                            sess.run(tf.get_variable('b', trainable=False).assign(p))
                        else:
                            # weights
                            sess.run(tf.get_variable('w', trainable=False).assign(p))
