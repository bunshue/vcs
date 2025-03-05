"""
no linear svm

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 非线性支持向量机

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn import datasets
from tensorflow.python.framework import ops

ops.reset_default_graph()

sess = tf.Session()

# 加载数据

# iris.数据 [(Sepal Length, Sepal Width, Petal Length, Petal Width)]
iris = datasets.load_iris()
x_vals = np.array([[x[0], x[3]] for x in iris.data])
y_vals = np.array([1 if y == 0 else -1 for y in iris.target])
class1_x = [x[0] for i, x in enumerate(x_vals) if y_vals[i] == 1]
class1_y = [x[1] for i, x in enumerate(x_vals) if y_vals[i] == 1]
class2_x = [x[0] for i, x in enumerate(x_vals) if y_vals[i] == -1]
class2_y = [x[1] for i, x in enumerate(x_vals) if y_vals[i] == -1]

# 声明模型变量

# 批量大小
batch_size = 150

# 初始化占位符
x_data = tf.placeholder(shape=[None, 2], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)
prediction_grid = tf.placeholder(shape=[None, 2], dtype=tf.float32)

# 创建变量
b = tf.Variable(tf.random_normal(shape=[1, batch_size]))

# 本案例采用高斯核函数，将低维空间数据转换为高维空间数据

# 高斯核函数 (RBF)
gamma = tf.constant(-50.0)
sq_vec = tf.multiply(2.0, tf.matmul(x_data, tf.transpose(x_data)))
my_kernel = tf.exp(tf.multiply(gamma, tf.abs(sq_vec)))

# SVM模型的损失函数
first_term = tf.reduce_sum(b)
b_vec_cross = tf.matmul(tf.transpose(b), b)
y_target_cross = tf.matmul(y_target, tf.transpose(y_target))
second_term = tf.reduce_sum(
    tf.multiply(my_kernel, tf.multiply(b_vec_cross, y_target_cross))
)
loss = tf.negative(tf.subtract(first_term, second_term))

# 声明预测时所采用的的核函数 RBF

rA = tf.reshape(tf.reduce_sum(tf.square(x_data), 1), [-1, 1])
rB = tf.reshape(tf.reduce_sum(tf.square(prediction_grid), 1), [-1, 1])
pred_sq_dist = tf.add(
    tf.subtract(rA, tf.multiply(2.0, tf.matmul(x_data, tf.transpose(prediction_grid)))),
    tf.transpose(rB),
)
pred_kernel = tf.exp(tf.multiply(gamma, tf.abs(pred_sq_dist)))

# 声明预测时所采用的的很函数RBF
prediction_output = tf.matmul(tf.multiply(tf.transpose(y_target), b), pred_kernel)
prediction = tf.sign(prediction_output - tf.reduce_mean(prediction_output))
accuracy = tf.reduce_mean(
    tf.cast(tf.equal(tf.squeeze(prediction), tf.squeeze(y_target)), tf.float32)
)

# 优化器的设置
my_opt = tf.train.GradientDescentOptimizer(0.01)
train_step = my_opt.minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()
sess.run(init)

# 开始训练
loss_vec = []
batch_accuracy = []
for i in range(300):
    rand_index = np.random.choice(len(x_vals), size=batch_size)
    rand_x = x_vals[rand_index]
    rand_y = np.transpose([y_vals[rand_index]])
    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})

    temp_loss = sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})
    loss_vec.append(temp_loss)

    acc_temp = sess.run(
        accuracy, feed_dict={x_data: rand_x, y_target: rand_y, prediction_grid: rand_x}
    )
    batch_accuracy.append(acc_temp)

    if (i + 1) % 75 == 0:
        print("Step #" + str(i + 1))
        print("Loss = " + str(temp_loss))

# 构建绘图时的数据点
# Create a mesh to plot points in
x_min, x_max = x_vals[:, 0].min() - 1, x_vals[:, 0].max() + 1
y_min, y_max = x_vals[:, 1].min() - 1, x_vals[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))
grid_points = np.c_[xx.ravel(), yy.ravel()]
[grid_predictions] = sess.run(
    prediction,
    feed_dict={
        x_data: x_vals,
        y_target: np.transpose([y_vals]),
        prediction_grid: grid_points,
    },
)
grid_predictions = grid_predictions.reshape(xx.shape)

# 绘制图形
plt.contourf(xx, yy, grid_predictions, cmap=plt.cm.Paired, alpha=0.8)
plt.plot(class1_x, class1_y, "ro", label="I. setosa")
plt.plot(class2_x, class2_y, "kx", label="Non setosa")
plt.title("Gaussian SVM Results on Iris Data")
plt.xlabel("Petal Length")
plt.ylabel("Sepal Width")
plt.legend(loc="lower right")
plt.ylim([-0.5, 3.0])
plt.xlim([3.5, 8.5])
plt.show()

# Plot batch accuracy
plt.plot(batch_accuracy, "k-", label="Accuracy")
plt.title("Batch Accuracy")
plt.xlabel("Generation")
plt.ylabel("Accuracy")
plt.legend(loc="lower right")
plt.show()

# Plot loss over time
plt.plot(loss_vec, "k-")
plt.title("Loss per Generation")
plt.xlabel("Generation")
plt.ylabel("Loss")
plt.show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
