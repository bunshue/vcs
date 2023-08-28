import os
import urllib.request
import argparse
import sys
import alexnet
import cv2
import tensorflow as tf
import numpy as np
import caffe_classes
 
# 使用参数配置
parser = argparse.ArgumentParser(description='Classify some images.')
# 添加参数。folder：本地文件夹传图像进行测试；url：传网址，网上的图进行测试
parser.add_argument('mode', choices=['folder', 'url'], default='folder')
# path：测试图像所在文件夹的路径。help：对path参数的帮助提示
parser.add_argument('path', help='Specify a path [e.g. testModel]')
# 接收PyCharm在debug模式下运行所配置的参数。
# PyCharm配置参数的方法：“Run”--“Debug...”--“Edit Configurations...”--“Configuration”--“Parameters：”填写“folder images”
args = parser.parse_args(sys.argv[1:])
 
if args.mode == 'folder':
    # get testImage
    # 获取当前图片的路径
    withPath = lambda f: '{}/{}'.format(args.path, f)
    # 获取withPath路径下所有的图像，并将其转成像素矩阵
    testImg = dict((f, cv2.imread(withPath(f))) for f in os.listdir(args.path) if os.path.isfile(withPath(f)))
elif args.mode == 'url':
    def url2img(url):
        '''url to image'''
        resp = urllib.request.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype='uint8')
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image
 
    testImg = {args.path: url2img(args.path)}
 
if testImg.values():
    # dropoutPro=1代表全部保留，不使用dropout操作，因为本次操作是使用AlexNet，而不是训练
    dropoutPro = 1
    # 1000个图片分类
    classNum = 1000
    # 控制神经网络中保留哪些层、去掉哪些层
    skip = []
 
    # 减图像通道的均值
    imgMean = np.array([104, 117, 124], np.float)
    # 一张图一张图的进行测试图像。原始输入图片大小227*227的三通道。
    x = tf.placeholder('float', [1, 227, 227, 3])
 
    # 指定网络结构的结构图，x:输入
    model = alexnet.alexNet(x, dropoutPro, classNum, skip)
    score = model.fc3
    softmax = tf.nn.softmax(score)
 
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        model.loadModel(sess)
 
        for key, img in testImg.items():
            # img preprocess
            resized = cv2.resize(img.astype(np.float), (227, 227)) - imgMean
            maxx = np.argmax(sess.run(softmax, feed_dict={x: resized.reshape((1, 227, 227, 3))}))
            res = caffe_classes.class_names[maxx]
 
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, res, (int(img.shape[0] / 3), int(img.shape[1] / 3)), font, 1, (0, 255, 0), 2)
            print("{}: {}\n----".format(key, res))
            cv2.imshow("demo", img)
            cv2.waitKey(0)
