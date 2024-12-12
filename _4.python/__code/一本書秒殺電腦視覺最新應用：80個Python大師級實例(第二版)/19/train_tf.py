import time
import numpy as np
import tensorflow as tf
import os
import random
from PIL import Image
import split_data

number = ['0','1','2','3','4','5','6','7','8','9']

all_train_files = split_data.get_all_files('./train')
all_test_files = split_data.get_all_files('./test')

def get_random_name_and_image(files):
    num = len(files)
    random_file = files[random.randint(0, num-1)]
    base = random_file.split('/')
    name = base[-2]
    now_image = get_image(random_file)
    return name, now_image

def get_image(file):
    now_image = Image.open(file)
    now_image = now_image.convert("RGB")
    now_image = np.array(now_image)
    now_image = np.mean(now_image, -1)
    return now_image

label, image = get_random_name_and_image(all_train_files)
IMAGE_HEIGHT = image.shape[0]
IMAGE_WIDTH = image.shape[1]
MAX_VEC_LENGHT = 10
print('待处理文件高度为', IMAGE_HEIGHT, '，宽度为', IMAGE_WIDTH)

def char2vec(ch):
    ch = int(ch)
    vector = np.zeros(10)
    vector[ch] = 1
    return vector

def get_next_batch(batch_size = 128, files = all_train_files):
    batch_x = np.zeros([batch_size, IMAGE_HEIGHT*IMAGE_WIDTH])
    batch_y = np.zeros([batch_size, MAX_VEC_LENGHT])
    for i in range(batch_size):
        text, image = get_random_name_and_image(files)
        batch_x[i,:] = image.flatten() / 255
        batch_y[i,:] = char2vec(text)
    return batch_x, batch_y

X = tf.placeholder(tf.float32, [None, IMAGE_HEIGHT*IMAGE_WIDTH])
Y = tf.placeholder(tf.float32, [None, MAX_VEC_LENGHT])

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

config = tf.ConfigProto()
config.gpu_options.allow_growth = True

def train_cnn():
    output = make_cnn()
    loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=output, labels=Y))
    optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)
    predict = tf.reshape(output, [-1, 1, MAX_VEC_LENGHT])
    max_idx_p = tf.argmax(predict, 2)
    max_idx_l = tf.argmax(tf.reshape(Y, [-1, 1, MAX_VEC_LENGHT]), 2)
    correct_pred = tf.equal(max_idx_p, max_idx_l)
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    saver = tf.train.Saver()
    max_step = 1000
    with tf.Session(config=config) as sess:
        sess.run(tf.global_variables_initializer())
        step = 0
        while step < max_step:
            batch_x, batch_y = get_next_batch(64)
            _, loss_ = sess.run([optimizer, loss], feed_dict={X: batch_x, Y: batch_y})
            if step % 100 == 0:
                batch_x_test, batch_y_test = get_next_batch(100, all_test_files)
                acc = sess.run(accuracy, feed_dict={X: batch_x_test, Y: batch_y_test})
                print('第' + str(step) + '步，准确率为', acc)
            step += 1
        split_data.mk_folder('./models')
        saver.save(sess, './models/cnn_tf.ckpt')

if __name__ == '__main__':
    global_start_time = time.time()
    train_cnn()
    print('训练耗时 (s) : ', time.time() - global_start_time)

