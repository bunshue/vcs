import time
import numpy as np
import tensorflow as tf
import os
import random
from PIL import Image

IMAGE_HEIGHT = 28
IMAGE_WIDTH = 28
MAX_VEC_LENGHT = 10

def get_image(file):
    now_image = Image.open(file)
    now_image = now_image.convert("RGB")
    now_image = np.array(now_image)
    now_image = np.mean(now_image, -1)
    return now_image

X = tf.placeholder(tf.float32, [None, 28 * 28])
def make_cnn():
    input_x = tf.reshape(X, shape=[-1, IMAGE_HEIGHT, IMAGE_WIDTH, 1])
    conv1 = tf.layers.conv2d(
        inputs=input_x,
        filters=32,
        kernel_size=[5, 5],
        strides=1,
        padding='same',
        activation=tf.nn.relu
    )

    pool1 = tf.layers.max_pooling2d(
        inputs=conv1,
        pool_size=[2, 2],
        strides=2
    )

    conv2 = tf.layers.conv2d(
        inputs=pool1,
        filters=32,
        kernel_size=[5, 5],
        strides=1,
        padding='same',
        activation=tf.nn.relu
    )

    pool2 = tf.layers.max_pooling2d(
        inputs=conv2,
        pool_size=[2, 2],
        strides=2
    )

    flat = tf.reshape(pool2, [-1, 7 * 7 * 32])
    dense = tf.layers.dense(
        inputs=flat,
        units=1024,
        activation=tf.nn.relu
    )

    dropout = tf.layers.dropout(
        inputs=dense,
        rate=0.5
    )

    output_y = tf.layers.dense(
        inputs=dropout,
        units=MAX_VEC_LENGHT
    )

    return output_y

def sess_ocr(im):
    output = make_cnn()
    saver = tf.train.Saver()
    with tf.Session() as sess:
        saver.restore(sess, './models/cnn_tf.ckpt')

        predict = tf.argmax(tf.reshape(output, [-1, 1, MAX_VEC_LENGHT]), 2)
        text_list = sess.run(predict, feed_dict={X: [im]})
        text = text_list[0]

    return text

def ocr_handle(filename):
    print(filename)
    X = tf.placeholder(tf.float32, [None, 28 * 28])
    image = get_image(filename)
    image = image.flatten() / 255
    predict_text = sess_ocr(image)
    return predict_text


