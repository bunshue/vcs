import os
import tensorflow as tf

print("------------------------------------------------------------")  # 60個

# 02_GPU0.py

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

print(tf.__version__)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 03_GPU0Memory.py

os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # 使用第一张 GPU

hello = tf.constant("Hello, TensorFlow!")
# gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.2) # 内存尺寸20%
gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.2)  # 内存尺寸20%
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpu_options))
print(sess.run(hello))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 03_GPU0Memory''.py

os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # 使用第一张 GPU
hello = tf.constant("Hello, TensorFlow!")
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.2)  # 内存尺寸20%
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
print(sess.run(hello))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 04_GPU0MemoryAuto.py

os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # 使用第一张 GPU
hello = tf.constant("Hello, TensorFlow!")
gpu_options = tf.compat.v1.GPUOptions(allow_growth=True)  # 使用全部的GPU  内存
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpu_options))
print(sess.run(hello))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 04_GPU0MemoryAuto''.py

os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # 使用第一张 GPU
hello = tf.constant("Hello, TensorFlow!")
gpu_options = tf.GPUOptions(allow_growth=True)  # 使用全部的GPU  内存
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
print(sess.run(hello))

print("------------------------------------------------------------")  # 60個
