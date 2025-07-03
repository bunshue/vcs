"""


"""
print("------------------------------------------------------------")  # 60個

import cv2

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

#Character_segmentation.py

from PIL import Image
import os.path
from skimage import io
from skimage import data


# 图像拉伸函数
def stretch(img):
    maxi = float(img.max())
    mini = float(img.min())

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j] = 255 / (maxi - mini) * img[i, j] - (255 * mini) / (maxi - mini)

    return img


# 二值化处理函数
def dobinaryzation(img):
    maxi = float(img.max())
    mini = float(img.min())

    x = maxi - ((maxi - mini) / 2)
    # 二值化,返回阈值ret  和  二值化操作后的图像thresh
    ret, thresh = cv2.threshold(img, x, 255, cv2.THRESH_BINARY)
    # 返回二值化后的黑白图像
    return thresh


# 寻找矩形轮廓
def find_rectangle(contour):
    y, x = [], []

    for p in contour:
        y.append(p[0][0])
        x.append(p[0][1])

    return [min(y), min(x), max(y), max(x)]


# 定位车牌号
def locate_license(img, afterimg):
    # contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # 找出最大的三个区域
    block = []
    for c in contours:
        # 找出轮廓的左上点和右下点，由此计算它的面积和长度比
        r = find_rectangle(c)
        a = (r[2] - r[0]) * (r[3] - r[1])  # 面积
        s = (r[2] - r[0]) * (r[3] - r[1])  # 长度比

        block.append([r, a, s])
    # 选出面积最大的3个区域
    block = sorted(block, key=lambda b: b[1])[-3:]

    # 使用颜色识别判断找出最像车牌的区域
    maxweight, maxindex = 0, -1
    for i in range(len(block)):
        b = afterimg[block[i][0][1] : block[i][0][3], block[i][0][0] : block[i][0][2]]
        # BGR转HSV
        hsv = cv2.cvtColor(b, cv2.COLOR_BGR2HSV)
        # 蓝色车牌的范围
        lower = np.array([100, 50, 50])
        upper = np.array([140, 255, 255])
        # 根据阈值构建掩膜
        mask = cv2.inRange(hsv, lower, upper)
        # 统计权值
        w1 = 0
        for m in mask:
            w1 += m / 255

        w2 = 0
        for n in w1:
            w2 += n

        # 选出最大权值的区域
        if w2 > maxweight:
            maxindex = i
            maxweight = w2

    return block[maxindex][0]


# 预处理函数
def find_license(img):
    m = 400 * img.shape[0] / img.shape[1]

    # 压缩图像
    img = cv2.resize(img, (400, int(m)), interpolation=cv2.INTER_CUBIC)

    # BGR转换为灰度图像
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 灰度拉伸
    stretchedimg = stretch(gray_img)

    # 进行开运算，用来去除噪声
    r = 16
    h = w = r * 2 + 1
    kernel = np.zeros((h, w), np.uint8)
    cv2.circle(kernel, (r, r), r, 1, -1)
    # 开运算
    openingimg = cv2.morphologyEx(stretchedimg, cv2.MORPH_OPEN, kernel)
    # 获取差分图，两幅图像做差  cv2.absdiff('图像1','图像2')
    strtimg = cv2.absdiff(stretchedimg, openingimg)

    # 图像二值化
    binaryimg = dobinaryzation(strtimg)

    # canny边缘检测
    canny = cv2.Canny(binaryimg, binaryimg.shape[0], binaryimg.shape[1])

    # 消除小的区域，保留大块的区域，从而定位车牌
    # 进行闭运算
    kernel = np.ones((5, 19), np.uint8)
    closingimg = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

    # 进行开运算
    openingimg = cv2.morphologyEx(closingimg, cv2.MORPH_OPEN, kernel)

    # 再次进行开运算
    kernel = np.ones((11, 5), np.uint8)
    openingimg = cv2.morphologyEx(openingimg, cv2.MORPH_OPEN, kernel)

    # 消除小区域，定位车牌位置
    rect = locate_license(openingimg, img)

    return rect, img


# 图像分割函数
def cut_license(afterimg, rect):
    # 转换为宽度和高度
    rect[2] = rect[2] - rect[0]
    rect[3] = rect[3] - rect[1]
    rect_copy = tuple(rect.copy())
    rect = [0, 0, 0, 0]
    # 创建掩膜
    mask = np.zeros(afterimg.shape[:2], np.uint8)
    # 创建背景模型  大小只能为13*5，行数只能为1，单通道浮点型
    bgdModel = np.zeros((1, 65), np.float64)
    # 创建前景模型
    fgdModel = np.zeros((1, 65), np.float64)
    # 分割图像
    cv2.grabCut(afterimg, mask, rect_copy, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
    img_show = afterimg * mask2[:, :, np.newaxis]

    return img_show


# 车牌图片二值化
def deal_license(licenseimg):
    # 车牌变为灰度图像
    gray_img = cv2.cvtColor(licenseimg, cv2.COLOR_BGR2GRAY)

    # 均值滤波  去除噪声
    kernel = np.ones((3, 3), np.float32) / 9
    gray_img = cv2.filter2D(gray_img, -1, kernel)

    # 二值化处理
    ret, thresh = cv2.threshold(gray_img, 120, 255, cv2.THRESH_BINARY)

    return thresh


def find_end(start, arg, black, white, width, black_max, white_max):
    end = start + 1
    for m in range(start + 1, width - 1):
        if (black[m] if arg else white[m]) > (
            0.98 * black_max if arg else 0.98 * white_max
        ):
            end = m
            break
    return end


if __name__ == "__main__":
    filename = "C:/_git/vcs/_4.python/PIL/data/ocr/carPlate02.jpg"
    filename = "car.png"
    
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    cv2.imshow("src", img)
    
    # 预处理图像
    rect, afterimg = find_license(img)

    # 框出车牌号
    cv2.rectangle(afterimg, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)
    cv2.imshow("afterimg", afterimg)

    # 分割车牌与背景
    cutimg = cut_license(afterimg, rect)
    cv2.imshow("cutimg", cutimg)

    # 二值化生成黑白图
    thresh = deal_license(cutimg)
    cv2.imshow("thresh", thresh)
    cv2.waitKey(0)

    # 分割字符

    # 判断底色和字色

    # 记录黑白像素总和
    white = []
    black = []
    height = thresh.shape[0]  # 263
    width = thresh.shape[1]  # 400
    # print('height',height)
    # print('width',width)
    white_max = 0
    black_max = 0
    # 计算每一列的黑白像素总和
    for i in range(width):
        line_white = 0
        line_black = 0
        for j in range(height):
            if thresh[j][i] == 255:
                line_white += 1
            if thresh[j][i] == 0:
                line_black += 1
        white_max = max(white_max, line_white)
        black_max = max(black_max, line_black)
        white.append(line_white)
        black.append(line_black)
        # print('white',white)
        # print('black',black)
    # arg为true表示黑底白字，False为白底黑字
    arg = True
    if black_max < white_max:
        arg = False

    n = 1
    start = 1
    end = 2
    s_width = 28
    s_height = 28
    while n < width - 2:
        n += 1
        # 判断是白底黑字还是黑底白字  0.05参数对应上面的0.95 可作调整
        if (white[n] if arg else black[n]) > (
            0.02 * white_max if arg else 0.02 * black_max
        ):
            start = n
            end = find_end(start, arg, black, white, width, black_max, white_max)
            n = end
            if end - start > 5:
                cj = thresh[1:height, start:end]

                print("tmp_%s.jpg" % (n))
                # 保存分割的图片

                infile = "tmp_%s.jpg" % (n)
                io.imsave(infile, cj)

                cv2.imshow("cutlicense", cj)
                cv2.waitKey(0)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#CNN.py

import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
from tensorflow.python.framework import ops

ops.reset_default_graph()
# 开始计算图会话
sess = tf.Session()
# 加载数据，转化图像为28×28的数组
data_dir = "temp"
mnist = read_data_sets(data_dir)
train_xdata = np.array([np.reshape(x, (28, 28)) for x in mnist.train.images])
test_xdata = np.array([np.reshape(x, (28, 28)) for x in mnist.test.images])
train_labels = mnist.train.labels
test_labels = mnist.test.labels

# 设置模型参数。由于图像是灰度图，所以该图像的深度为1，即颜色通道数为1
batch_size = 100
learning_rate = 0.005
evaluation_size = 500
image_width = train_xdata[0].shape[0]
image_height = train_xdata[0].shape[1]
target_size = max(train_labels) + 1
num_channels = 1  # 颜色通道= 1
generations = 500
eval_every = 5
conv1_features = 25
conv2_features = 50
max_pool_size1 = 2
max_pool_size2 = 2
fully_connected_size1 = 100
# 为数据集声明占位符。同时，声明训练数据集变量和测试数据集变量。实例中的训练批量大小和评估大小可以根据实际训练和评估的机器物理内存来调整
x_input_shape = (batch_size, image_width, image_height, num_channels)
x_input = tf.placeholder(tf.float32, shape=x_input_shape)
y_target = tf.placeholder(tf.int32, shape=(batch_size))
eval_input_shape = (evaluation_size, image_width, image_height, num_channels)
eval_input = tf.placeholder(tf.float32, shape=eval_input_shape)
eval_target = tf.placeholder(tf.int32, shape=(evaluation_size))

# 声明卷积层的权重和偏置，权重和偏置的参数在前面的步骤中已设置
conv1_weight = tf.Variable(
    tf.truncated_normal(
        [4, 4, num_channels, conv1_features], stddev=0.1, dtype=tf.float32
    )
)
conv1_bias = tf.Variable(tf.zeros([conv1_features], dtype=tf.float32))
conv2_weight = tf.Variable(
    tf.truncated_normal(
        [4, 4, conv1_features, conv2_features], stddev=0.1, dtype=tf.float32
    )
)
conv2_bias = tf.Variable(tf.zeros([conv2_features], dtype=tf.float32))

# 声明全联接层的权重和偏置
resulting_width = image_width // (max_pool_size1 * max_pool_size2)
resulting_height = image_height // (max_pool_size1 * max_pool_size2)
full1_input_size = resulting_width * resulting_height * conv2_features
full1_weight = tf.Variable(
    tf.truncated_normal(
        [full1_input_size, fully_connected_size1], stddev=0.1, dtype=tf.float32
    )
)
full1_bias = tf.Variable(
    tf.truncated_normal([fully_connected_size1], stddev=0.1, dtype=tf.float32)
)
full2_weight = tf.Variable(
    tf.truncated_normal(
        [fully_connected_size1, target_size], stddev=0.1, dtype=tf.float32
    )
)
full2_bias = tf.Variable(
    tf.truncated_normal([target_size], stddev=0.1, dtype=tf.float32)
)


# 声明算法模型。首先，创建一个模型函数my_conv_net()，注意该函数的层权重和偏置。当然，为了最后两层全连接层能有效工作，我们将前层卷积层的结构摊平
def my_conv_net(input_data):
    # 第一层：Conv-ReLU-MaxPool层
    conv1 = tf.nn.conv2d(input_data, conv1_weight, strides=[1, 1, 1, 1], padding="SAME")
    relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_bias))
    max_pool1 = tf.nn.max_pool(
        relu1,
        ksize=[1, max_pool_size1, max_pool_size1, 1],
        strides=[1, max_pool_size1, max_pool_size1, 1],
        padding="SAME",
    )
    # 第二层：Conv-ReLU-MaxPool层
    conv2 = tf.nn.conv2d(max_pool1, conv2_weight, strides=[1, 1, 1, 1], padding="SAME")
    relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_bias))
    max_pool2 = tf.nn.max_pool(
        relu2,
        ksize=[1, max_pool_size2, max_pool_size2, 1],
        strides=[1, max_pool_size2, max_pool_size2, 1],
        padding="SAME",
    )
    # 将输出转换为下一个完全连接层的1xN层
    final_conv_shape = max_pool2.get_shape().as_list()
    final_shape = final_conv_shape[1] * final_conv_shape[2] * final_conv_shape[3]
    flat_output = tf.reshape(max_pool2, [final_conv_shape[0], final_shape])
    # 第一个全连接层
    fully_connected1 = tf.nn.relu(
        tf.add(tf.matmul(flat_output, full1_weight), full1_bias)
    )
    # 第二个全连接层
    final_model_output = tf.add(tf.matmul(fully_connected1, full2_weight), full2_bias)
    return final_model_output


# 声明训练模型
model_output = my_conv_net(x_input)
test_model_output = my_conv_net(eval_input)

# 因为实例的预测结果不是多分类，而仅仅是一类，所以使用softmax函数作为损失函数
loss = tf.reduce_mean(
    tf.nn.sparse_softmax_cross_entropy_with_logits(model_output, y_target)
)
# 创建训练集和测试集的预测函数。同时，创建对应的准确度函数，评估模型的准确度
prediction = tf.nn.softmax(model_output)
test_prediction = tf.nn.softmax(test_model_output)


# 创建精度函数
def get_accuracy(logits, targets):
    batch_predictions = np.argmax(logits, axis=1)
    num_correct = np.sum(np.equal(batch_predictions, targets))
    return 100.0 * num_correct / batch_predictions.shape[0]


# 创建一个优化器，声明训练步长，
my_optimizer = tf.train.MomentumOptimizer(learning_rate, 0.9)
train_step = my_optimizer.minimize(loss)
# 初始化所有的模型变量
init = tf.initialize_all_variables()
sess.run(init)
# 开始训练模型。遍历迭代随机选择批量数据进行训练。我们在训练集批量数据和预测集批量数据上评估模型，保存损失函数和准确度。我们看到，在迭代500次之后，测试数据集上的准确度达到96%~97%。
train_loss = []
train_acc = []
test_acc = []
for i in range(generations):
    rand_index = np.random.choice(len(train_xdata), size=batch_size)
    rand_x = train_xdata[rand_index]
    rand_x = np.expand_dims(rand_x, 3)
    rand_y = train_labels[rand_index]
    train_dict = {x_input: rand_x, y_target: rand_y}

    sess.run(train_step, feed_dict=train_dict)
    temp_train_loss, temp_train_preds = sess.run(
        [loss, prediction], feed_dict=train_dict
    )
    temp_train_acc = get_accuracy(temp_train_preds, rand_y)

    if (i + 1) % eval_every == 0:
        eval_index = np.random.choice(len(test_xdata), size=evaluation_size)
        eval_x = test_xdata[eval_index]
        eval_x = np.expand_dims(eval_x, 3)
        eval_y = test_labels[eval_index]
        test_dict = {eval_input: eval_x, eval_target: eval_y}
        test_preds = sess.run(test_prediction, feed_dict=test_dict)
        temp_test_acc = get_accuracy(test_preds, eval_y)

        # 记录及列印结果
        train_loss.append(temp_train_loss)
        train_acc.append(temp_train_acc)
        test_acc.append(temp_test_acc)
        acc_and_loss = [(i + 1), temp_train_loss, temp_train_acc, temp_test_acc]
        acc_and_loss = [np.round(x, 2) for x in acc_and_loss]
        print(
            "Generation # {}. Train Loss: {:.2f}. Train Acc (Test Acc): {:.2f} ({:.2f})".format(
                *acc_and_loss
            )
        )

# 使用Matplotlib模块绘制损失函数和准确度，如图8-11所示
eval_indices = range(0, generations, eval_every)
# Plot loss over time
plt.plot(eval_indices, train_loss, "k-")
plt.title("Softmax Loss per Generation")
plt.xlabel("Generation")
plt.ylabel("Softmax Loss")
plt.show()

# 准确度（Plot train and test accuracy）
plt.plot(eval_indices, train_acc, "k-", label="Train Set Accuracy")
plt.plot(eval_indices, test_acc, "r--", label="Test Set Accuracy")
plt.title("Train and Test Accuracy")
plt.xlabel("Generation")
plt.ylabel("Accuracy")
plt.legend(loc="lower right")
plt.show()

# 运行如下代码打印最新结果中的六幅抽样图，如图8-12所示
actuals = rand_y[0:6]
predictions = np.argmax(temp_train_preds, axis=1)[0:6]
images = np.squeeze(rand_x[0:6])

Nrows = 2
Ncols = 3
for i in range(6):
    plt.subplot(Nrows, Ncols, i + 1)
    plt.imshow(np.reshape(images[i], [28, 28]), cmap="Greys_r")
    plt.title(
        "Actual: " + str(actuals[i]) + " Pred: " + str(predictions[i]), fontsize=10
    )
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)

print("------------------------------------------------------------")  # 60個

#distance_transform.py

from scipy import ndimage as ndi
from skimage import morphology
from skimage import feature

# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

# 创建两个带有重叠圆的图像
x, y = np.indices((80, 80))
x1, y1, x2, y2 = 28, 28, 44, 52
r1, r2 = 16, 20
mask_circle1 = (x - x1) ** 2 + (y - y1) ** 2 < r1**2
mask_circle2 = (x - x2) ** 2 + (y - y2) ** 2 < r2**2
image = np.logical_or(mask_circle1, mask_circle2)
# 现在我们用分水岭算法分离两个圆
distance = ndi.distance_transform_edt(image)  # 距离变换
local_maxi = feature.peak_local_max(
    distance, indices=False, footprint=np.ones((3, 3)), labels=image
)  # 寻找峰值
markers = ndi.label(local_maxi)[0]  # 初始标记点
labels = morphology.watershed(-distance, markers, mask=image)  # 基于距离变换的分水岭算法
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
axes = axes.ravel()
ax0, ax1, ax2, ax3 = axes
ax0.imshow(image, cmap=plt.cm.gray, interpolation="nearest")
ax0.set_title("原始图像")
ax1.imshow(-distance, cmap=plt.cm.jet, interpolation="nearest")
ax1.set_title("距离变换")
ax2.imshow(markers, cmap=plt.cm.spectral, interpolation="nearest")
ax2.set_title("标记")
ax3.imshow(labels, cmap=plt.cm.spectral, interpolation="nearest")
ax3.set_title("分割")
for ax in axes:
    ax.axis("off")
fig.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

#pytesseract.py


def split_picture(imagepath):
    # 以灰度模式读取图片
    gray = cv2.imread(imagepath, 0)
    # 将图片的边缘变为白色
    height, width = gray.shape
    for i in range(width):
        gray[0, i] = 255
        gray[height - 1, i] = 255
    for j in range(height):
        gray[j, 0] = 255
        gray[j, width - 1] = 255
    # 中值滤波
    blur = cv2.medianBlur(gray, 3)  # 模板大小3*3
    # 二值化
    ret, thresh1 = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)
    image, contours, hierarchy = cv2.findContours(thresh1, 2, 2)
    for cnt in contours:
        # 最小的外接矩形
        x, y, w, h = cv2.boundingRect(cnt)
        if x != 0 and y != 0 and w * h >= 100:
            print((x, y, w, h))

imagepath = "8a.jpg"
split_picture(imagepath)


print("------------------------------------------------------------")  # 60個

#SVD.py

"""
SVD

"""
print("------------------------------------------------------------")  # 60個

# Gray

from PIL import Image

def svd_restore(sigma, u, v, K):
    K = min(len(sigma) - 1, K)  # 当K超过sigma的长度时会造成越界
    print("现在用%d等级恢复图像" % K)
    m = len(u)
    n = v[0].size
    SigRecon = np.zeros((m, n))  # 新建一int矩阵，储存恢复的灰度图像素
    for k in range(K + 1):  # 计算X=u*sigma*v
        for i in range(m):
            SigRecon[i] += sigma[k] * u[i][k] * v[k]
    # 计算得到的矩阵还是float型，需要将其转化为uint8以转为图片
    SigRecon = SigRecon.astype("uint8")
    Image.fromarray(SigRecon).save("svd_" + str(K) + "_" + image_file)  # 保存灰度图


image_file = "frog.jpg"

im = Image.open(image_file)  # 打开图像文件
im = im.convert("L")  # 将原图像转化为灰度图
im.save("Gray_" + image_file)  # 保存灰度图

w, h = im.size  # 得到原图的长与宽
# 新建一int矩阵，储存灰度图各像素点数据
dt = np.zeros((w, h), "uint8")
# 逐像素点复制，由于直接对im.getdata()进行数据类型转换会有偏差
for i in range(w):
    for j in range(h):
        dt[i][j] = im.getpixel((i, j))  # 取得該點之像素值
# 复制过来的图像是原图的翻转，因此将其再次翻转到正常角度
dt = dt.transpose()
u, sigma, v = np.linalg.svd(dt)  # 调用numpy库进行SVM
u = np.array(u)  # 转为array格式，方便进行乘法运算
v = np.array(v)  # 同上
for k in [1, 10, 30, 50, 80, 100, 150, 200, 300, 500]:
    svd_restore(sigma, u, v, k)  # 使用前k个奇异值进行恢复

print("------------------------------------------------------------")  # 60個
# RGB

from scipy import ndimage
from matplotlib.pyplot import imread
import imageio

# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示


def pic_compress(k, pic_array):
    u, sigma, vt = np.linalg.svd(pic_array)
    sig = np.eye(k) * sigma[:k]
    new_pic = np.dot(np.dot(u[:, :k], sig), vt[:k, :])  # 还原图像
    size = u.shape[0] * k + sig.shape[0] * sig.shape[1] + k * vt.shape[1]  # 压缩后大小
    return new_pic, size


filename = "frog.jpg"
#ori_img = np.array(ndimage.imread(filename, flatten=True))
ori_img = np.array(imageio.imread(filename))
new_img, size = pic_compress(100, ori_img)
print("原始图像大小:" + str(ori_img.shape[0] * ori_img.shape[1]))
print("压缩后图像大小:" + str(size))
fig, ax = plt.subplots(1, 2)
ax[0].imshow(ori_img)
ax[0].set_title("压缩前")
ax[1].imshow(new_img)
ax[1].set_title("压缩后")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#FLANN.py

"""
基于FLANN的匹配器(FLANN based Matcher)
FLANN代表近似最近邻居的快速库。它代表一组经过优化的算法，用于大数据集中的快速最近邻搜索以及高维特征。
"""

import cv2 as cv

queryImage=cv.imread("template_adjust.jpg",0)
trainingImage=cv.imread("target.jpg",0)#读取要匹配的灰度照片
sift=cv.xfeatures2d.SIFT_create()#创建sift检测器
kp1, des1 = sift.detectAndCompute(queryImage,None)
kp2, des2 = sift.detectAndCompute(trainingImage,None)
#设置Flannde参数
FLANN_INDEX_KDTREE=0
indexParams=dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
searchParams= dict(checks=50)
flann=cv.FlannBasedMatcher(indexParams,searchParams)
matches=flann.knnMatch(des1,des2,k=2)
#设置好初始匹配值
matchesMask=[[0,0] for i in range (len(matches))]
for i, (m,n) in enumerate(matches):
	if m.distance< 0.5*n.distance: #舍弃小于0.5的匹配结果
		matchesMask[i]=[1,0]
#给特征点和匹配的线定义颜色
drawParams=dict(matchColor=(0,0,255),singlePointColor=(255,0,0),matchesMask=matchesMask,flags=0) 
#画出匹配的结果
resultimage=cv.drawMatchesKnn(queryImage,kp1,trainingImage,kp2,matches,None,**drawParams) 

plt.imshow(resultimage,),plt.show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# FLANN_positioning.py

#基于FLANN的匹配器(FLANN based Matcher)定位图片

MIN_MATCH_COUNT = 10 #设置最低特征点匹配数量为10
template = cv2.imread('template_adjust.jpg',0) # queryImage
target = cv2.imread('target.jpg',0) # trainImage
# Initiate SIFT detector创建sift检测器
sift = cv2.xfeatures2d.SIFT_create()
# 使用SIFT查找关键字和描述符
kp1, des1 = sift.detectAndCompute(template,None)
kp2, des2 = sift.detectAndCompute(target,None)
#创建设置FLANN匹配
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1,des2,k=2)
# 根据Lowe's比率测试保存所有的匹配项
good = []
#舍弃大于0.7的匹配
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)
if len(good)>MIN_MATCH_COUNT:
    # 获取关键点的坐标
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
    #计算变换矩阵和MASK
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    matchesMask = mask.ravel().tolist()
    h,w = template.shape
    # 使用得到的变换矩阵对原图像的四个角进行变换，获得在目标图像上对应的坐标
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)
    cv2.polylines(target,[np.int32(dst)],True,0,2, cv2.LINE_AA)
else:
    print( "没有找到足够的匹配项 - %d/%d" % (len(good),MIN_MATCH_COUNT))
    matchesMask = None
draw_params = dict(matchColor=(0,255,0), 
                   singlePointColor=None,
                   matchesMask=matchesMask, 
                   flags=2)
result = cv2.drawMatches(template,kp1,target,kp2,good,None,**draw_params)
plt.imshow(result, 'gray')
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

