import tensorflow as tf
import time
import numpy as np
import tensorflow as tf
import os
import random
from PIL import Image



class Solver(object):
    def __init__(self):
        self.model = None
        self.sess = None
        self.saver = None
        self.IMAGE_HEIGHT = 28
        self.IMAGE_WIDTH = 28
        self.MAX_VEC_LENGHT = 10
        self.X = tf.placeholder(tf.float32, [None, 28 * 28])


    def load_model(self):
        if self.sess is None:
            self.sess = tf.Session()
            self.saver = tf.train.import_meta_graph('./models/cnn_tf.ckpt.meta')
            self.saver.restore(self.sess, './models/cnn_tf.ckpt')


    def get_image(self, file):
        now_image = Image.open(file)
        now_image = now_image.convert("RGB")
        now_image = np.array(now_image)
        now_image = np.mean(now_image, -1)
        return now_image

    #定义CNN
    def make_cnn(self):
        input_x = tf.reshape(self.X, shape=[-1, self.IMAGE_HEIGHT, self.IMAGE_WIDTH, 1])

        #第1层结构，使用conv2d
        conv1 = tf.layers.conv2d(
            inputs=input_x,
            filters=32,
            kernel_size=[5, 5],
            strides=1,
            padding='same',
            activation=tf.nn.relu
        )
        #使用max_pooling2d
        pool1 = tf.layers.max_pooling2d(
            inputs=conv1,
            pool_size=[2, 2],
            strides=2
        )
        #第2层结构，使用conv2d
        conv2 = tf.layers.conv2d(
            inputs=pool1,
            filters=32,
            kernel_size=[5, 5],
            strides=1,
            padding='same',
            activation=tf.nn.relu
        )
        #使用max_pooling2d
        pool2 = tf.layers.max_pooling2d(
            inputs=conv2,
            pool_size=[2, 2],
            strides=2
        )
        #全连接层
        flat = tf.reshape(pool2, [-1, 7 * 7 * 32])
        dense = tf.layers.dense(
            inputs=flat,
            units=1024,
            activation=tf.nn.relu
        )
        #使用dropout
        dropout = tf.layers.dropout(
            inputs=dense,
            rate=0.5
        )
        #输出层
        output_y = tf.layers.dense(
            inputs=dropout,
            units=self.MAX_VEC_LENGHT
        )
        return output_y

    def sess_ocr(self, im):
        output = self.make_cnn()
        saver = tf.train.Saver()
        print(os.getcwd())
        with tf.Session() as sess:
            saver.restore(sess, tf.train.latest_checkpoint('./models'))
            predict = tf.argmax(tf.reshape(output, [-1, 1, self.MAX_VEC_LENGHT]), 2)
            text_list = sess.run(predict, feed_dict={self.X: [im]})
            text = text_list[0]

        return text

    def ocr_handle(self, filename):
        X = tf.placeholder(tf.float32, [None, 28 * 28])
        image = self.get_image(filename)
        image = image.flatten() / 255
        predict_text = self.sess_ocr(image)
        return predict_text


