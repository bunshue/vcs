import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"                          # 使用第一张 GPU

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
gpu_options = tf.compat.v1.GPUOptions(allow_growth=True)               # 使用全部的GPU  内存
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpu_options))
print(sess.run(hello))