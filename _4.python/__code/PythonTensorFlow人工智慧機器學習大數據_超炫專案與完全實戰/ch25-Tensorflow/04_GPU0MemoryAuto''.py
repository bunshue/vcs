import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"                          # 使用第一张 GPU
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
gpu_options = tf.GPUOptions(allow_growth=True)               # 使用全部的GPU  内存
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
print(sess.run(hello))