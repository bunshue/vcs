#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # 使用第一张 GPU
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.2) # 内存尺寸20%
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
print(sess.run(hello))