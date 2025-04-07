"""
machine_learning_ch08

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

print("------------------------------------------------------------")  # 60個

# from common1 import *
import scipy
import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_moons
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA  # KernelPCA 萃取特徵

from matplotlib.colors import ListedColormap
from sklearn.preprocessing import MinMaxScaler
from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# svmplatt.py

import operator


class PlattSVM(object):
    def __init__(self):
        self.X = []  # 输入数据集
        self.labelMat = []
        self.C = 0.0  # 惩罚因子
        self.tol = 0.0  # 容错率toler
        self.b = 0.0  # 截距初始值
        self.kValue = {}
        self.maxIter = 10000
        self.svIndx = []  # 支持向量下标
        self.sptVects = []  # 支持向量
        self.SVlabel = []  # 支持类别标签

    # 加载数据集并初始化相应参数
    def loadDataSet(self, fileName):
        fr = open(fileName, encoding="UTF-8-sig")
        for line in fr.readlines():
            lineArr = line.strip().split("\t")
            self.X.append([float(lineArr[0]), float(lineArr[1])])
            self.labelMat.append(float(lineArr[2]))
        self.initparam()
        # 核函数列表

    def kernels(self, dataMat, A):
        m, n = np.shape(dataMat)
        K = np.mat(np.zeros((m, 1)))
        cc = list(self.kValue.keys())
        # print(cc[0])
        if cc[0] == "linear":
            K = dataMat * A.T  # linear kernel
        elif cc[0] == "Gaussian":  # 高斯核
            for j in range(m):
                deltaRow = dataMat[j, :] - A
                K[j] = deltaRow * deltaRow.T
            K = np.exp(K / (-1 * self.kValue["Gaussian"] ** 2))
        else:
            raise NameError("无法识别的核函数")
        return K

    def initparam(self):
        self.X = np.mat(self.X)  # 数据集
        self.labelMat = np.mat(self.labelMat).T  # 类别标签
        self.m = np.shape(self.X)[0]  # 数据集行数
        self.lambdas = np.mat(np.zeros((self.m, 1)))  # 拉格朗日乘子
        self.eCache = np.mat(np.zeros((self.m, 2)))  # 误差缓存
        self.K = np.mat(np.zeros((self.m, self.m)))  # 存储用于核函数计算的向量
        for i in range(self.m):
            self.K[:, i] = self.kernels(self.X, self.X[i, :])  # kValue

    # 随机选择一个不等于i的j
    def randJ(self, i):
        j = i
        while j == i:
            j = int(random.uniform(0, self.m))
        return j

    # 调整大于H,小于L的aj
    def clipLambda(self, aj, H, L):
        if aj > H:
            aj = H
        if L > aj:
            aj = L
        return aj

    def calcEk(self, k):
        return float(
            np.multiply(self.lambdas, self.labelMat).T * self.K[:, k] + self.b
        ) - float(self.labelMat[k])

    # 选择lambda,从缓存中寻找具有最大误差的行索引作为j
    def chooseJ(self, i, Ei):
        maxK = -1
        maxDeltaE = 0
        Ej = 0
        self.eCache[i] = [1, Ei]  # 更新误差缓存
        validEcacheList = np.nonzero(self.eCache[:, 0].A)[0]
        if (len(validEcacheList)) > 1:
            for k in validEcacheList:
                if k == i:
                    continue
                Ek = self.calcEk(k)
                deltaE = abs(Ei - Ek)
                if deltaE > maxDeltaE:
                    maxK = k
                    maxDeltaE = deltaE
                    Ej = Ek
            return maxK, Ej
        else:
            j = self.randJ(i)
            Ej = self.calcEk(j)
        return j, Ej

    # 主函数-内循环
    def innerLoop(self, i):
        Ei = self.calcEk(i)  # 计算和更新i的误差缓存
        # 如果误差超出容错率和错误分类允许的边界
        if ((self.labelMat[i] * Ei < -self.tol) and (self.lambdas[i] < self.C)) or (
            (self.labelMat[i] * Ei > self.tol) and (self.lambdas[i] > 0)
        ):
            j, Ej = self.chooseJ(i, Ei)  # 选择具有最大误差的j
            lambdaIold = self.lambdas[i].copy()
            lambdaJold = self.lambdas[j].copy()
            if self.labelMat[i] != self.labelMat[j]:  # 见第二章公式十一
                L = max(0, self.lambdas[j] - self.lambdas[i])
                H = min(self.C, self.C + self.lambdas[j] - self.lambdas[i])
            else:
                L = max(0, self.lambdas[j] + self.lambdas[i] - self.C)
                H = min(self.C, self.lambdas[j] + self.lambdas[i])
            if L == H:
                return 0
            eta = (
                2.0 * self.K[i, j] - self.K[i, i] - self.K[j, j]
            )  # 松弛变量，见第二章公式十五中目标函数的二阶导数
            if eta >= 0:
                return 0
            self.lambdas[j] -= self.labelMat[j] * (Ei - Ej) / eta  # 见第二章公式九
            self.lambdas[j] = self.clipLambda(self.lambdas[j], H, L)  # 见第二章公式十和公式十二
            self.eCache[j] = [1, self.calcEk(j)]  # 计算和更新j的缓存
            if abs(self.lambdas[j] - lambdaJold) < 0.00001:
                return 0
            self.lambdas[i] += (
                self.labelMat[j] * self.labelMat[i] * (lambdaJold - self.lambdas[j])
            )
            self.eCache[i] = [1, self.calcEk(i)]  # 计算和更新j的缓存
            # 见第二章公式十四
            b1 = (
                self.b
                - Ei
                - self.labelMat[i] * (self.lambdas[i] - lambdaIold) * self.K[i, i]
                - self.labelMat[j] * (self.lambdas[j] - lambdaJold) * self.K[i, j]
            )
            b2 = (
                self.b
                - Ej
                - self.labelMat[i] * (self.lambdas[i] - lambdaIold) * self.K[i, j]
                - self.labelMat[j] * (self.lambdas[j] - lambdaJold) * self.K[j, j]
            )
            # 根据KKT条件更新b的取值
            if (0 < self.lambdas[i]) and (self.C > self.lambdas[i]):
                self.b = b1
            elif (0 < self.lambdas[j]) and (self.C > self.lambdas[j]):
                self.b = b2
            else:
                self.b = (b1 + b2) / 2.0
            return 1
        else:
            return 0

    # 主函数-外循环
    def train(self):  # full Platt SMO
        step = 0
        entireflag = True
        lambdaPairsChanged = 0  # entireflag全集扫描标志位
        # 外循环迭代器
        # 终止条件:超过最大迭代次数时,或未对lambda做出调整时退出
        while (step < self.maxIter) and ((lambdaPairsChanged > 0) or (entireflag)):
            lambdaPairsChanged = 0
            if entireflag:  # 遍历整个数据集
                for i in range(self.m):
                    lambdaPairsChanged += self.innerLoop(i)  # 进入内循环
                step += 1
            else:  # 遍历非边界的lambdas
                nonBoundIs = np.nonzero(
                    (self.lambdas.A > 0) * (self.lambdas.A < self.C)
                )[
                    0
                ]  # 通过KKT确定lambdas的位置
                for i in nonBoundIs:
                    lambdaPairsChanged += self.innerLoop(i)  # 进入内循环
                step += 1
            if entireflag:
                entireflag = False  # 转换标志位 切换到两种遍历方式的另一种
            elif lambdaPairsChanged == 0:
                entireflag = True  # 转换标志位 遍历整个数据集
        self.svIndx = np.nonzero(self.lambdas.A > 0)[0]  # 输出计算后的支持向量索引
        self.sptVects = self.X[self.svIndx]  # 计算完成的支持向量
        self.SVlabel = self.labelMat[self.svIndx]  # 计算完成后的支持向量的类别标签

    # 计算权重向量
    def calcWs(self):
        m, n = np.shape(self.X)
        w = np.zeros((n, 1))
        for i in range(m):
            w += np.multiply(self.lambdas[i] * self.labelMat[i], self.X[i, :].T)
        return w

    # 绘制散点图
    def scatterplot(self, plt):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for i in range(np.shape(self.X)[0]):
            if self.lambdas[i] != 0:  # KKT条件
                ax.scatter(self.X[i, 0], self.X[i, 1], c="green", marker="s", s=50)
            elif self.labelMat[i] == 1:
                ax.scatter(self.X[i, 0], self.X[i, 1], c="blue", marker="o")
            elif self.labelMat[i] == -1:
                ax.scatter(self.X[i, 0], self.X[i, 1], c="red", marker="o")

    # 分类器
    def classify(self, testSet, testLabel):
        errorCount = 0
        testMat = np.mat(testSet)
        m, n = np.shape(testMat)
        for i in range(m):  # 用核函数划分测试集
            kernelEval = self.kernels(self.sptVects, testMat[i, :])
            predict = (
                kernelEval.T * np.multiply(self.SVlabel, self.lambdas[self.svIndx])
                + self.b
            )
            if np.sign(predict) != np.sign(testLabel[i]):
                errorCount += 1
        return float(errorCount) / float(m)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# PlattSMOTest01.py

svm = PlattSVM()
svm.C = 70  # 惩罚因子C: 0.6,
svm.tol = 0.001  # 容错率:0.001
svm.maxIter = 200
svm.kValue["Gaussian"] = 3.0  # 核函数
svm.loadDataSet("nolinear.txt")
# 主 platt smo 函数
svm.train()
# 根据拉格朗日alphas乘子计算W向量
print(svm.svIndx)
print(np.shape(svm.sptVects)[0])
print("b:", svm.b)
# print("lambdas[lambdas > 0]:",svm.lambdas[svm.lambdas > 0])
svm.scatterplot(plt)
# 显示绘制的图形
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# PlattSMOTest02.py

svm = PlattSVM()
svm.C = 100  # 惩罚因子C: 0.6,
svm.tol = 0.001  # 容错率:0.001
svm.maxIter = 10000
svm.kValue["Gaussian"] = 3.0  # 核函数
svm.loadDataSet("svm.txt")
# 主 platt smo 函数
svm.train()
# 根据拉格朗日alphas乘子计算W向量
print(svm.svIndx)
print(np.shape(svm.sptVects)[0])
print("b:", svm.b)
# print("lambdas[lambdas > 0]:",svm.lambdas[svm.lambdas > 0])
svm.scatterplot(plt)
# 显示绘制的图形
plt.show()

print(svm.classify(svm.X, svm.labelMat))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Predict.py

from sklearn.datasets._base import Bunch

# 引入持久化类
import pickle
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC  # 导入线性SVM算法
from sklearn import metrics


# 读取文件
def readfile(path):
    fp = open(path, "rb")
    content = fp.read()
    fp.close()
    return content


# 计算分类精度：
def metrics_result(actual, predict):
    print("精度:{0:.3f}".format(metrics.precision_score(actual, predict)))
    print("召回:{0:0.3f}".format(metrics.recall_score(actual, predict)))
    print("f1-score:{0:.3f}".format(metrics.f1_score(actual, predict)))


# 读取bunch对象
def readbunchobj(path):
    file_obj = open(path, "rb")
    bunch = pickle.load(file_obj)
    file_obj.close()
    return bunch


# 写入bunch对象
def writebunchobj(path, bunchobj):
    file_obj = open(path, "wb")
    pickle.dump(bunchobj, file_obj)
    file_obj.close()


# 导入训练集
trainpath = "train_word_bag/tfdifspace.dat"
train_set = readbunchobj(trainpath)

# 导入测试集
testpath = "test_word_bag/testspace.dat"
test_set = readbunchobj(testpath)
# 应用线性SVM算法
# 1. 输入词袋向量和分类标签
clf = LinearSVC(penalty="l2", dual=False, tol=1e-4).fit(train_set.tdm, train_set.label)
""" NG
# 预测分类结果
predicted = clf.predict(test_set.tdm)
total = len(predicted)
rate = 0
for flabel, file_name, expct_cate in zip(test_set.label, test_set.filenames, predicted):
    if flabel != expct_cate:
        rate += 1
        print(file_name, ": 实际类别:", flabel, " -->预测类别:", expct_cate)
# 精度
print("error rate:", float(rate) * 100 / float(total), "%")
print("预测完毕!!!")

metrics_result(test_set.label, predicted)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 沒用到
# TextPreprocess.py

import jieba

from sklearn.datasets._base import Bunch

# 引入持久化类
import pickle
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

##############################################################
# 分类语料预处理的类
# 语料目录结构：
# corpus
#   |-catergory_A
#     |-01.txt
#     |-02.txt
#   |-catergory_B
#   |-catergory_C
#   ...
##############################################################


# 文本预处理类
class TextPreprocess:
    data_set = Bunch(target_name=[], label=[], filenames=[], contents=[])
    wordbag = Bunch(target_name=[], label=[], filenames=[], tdm=[], vocabulary={})

    def __int__(self):  # 构造方法
        self.corpus_path = ""  # 原始语料路径
        self.pos_path = ""  # 预处理后语料路径
        self.segment_path = ""  # 分词后语料路径
        self.wordbag_path = ""  # 词袋模型路径
        self.stopword_path = ""  # 停止词路径
        self.trainset_name = ""  # 训练集文件名
        self.wordbag_name = ""  # 词包文件名

    # 对输入语料进行基本预处理，删除语料的换行符，并持久化。
    # 处理后在pos_path下建立与corpus_path相同的子目录和文件结构
    def preprocess(self):
        if self.corpus_path == "" or self.pos_path == "":
            print("corpus_path或pos_path不能为空")
            return
        dir_list = os.listdir(self.corpus_path)  # 获取每个目录下所有的文件
        for mydir in dir_list:
            class_path = self.corpus_path + mydir + "/"  # 拼出分类子目录的路径
            file_list = os.listdir(class_path)  # 获取class_path下的所有文件
            for file_path in file_list:  # 遍历所有文件
                file_name = class_path + file_path  # 拼出文件名全路径
                file_read = open(file_name, "rb")  # 打开一个文件
                raw_corpus = file_read.read()  # 读取未处理的语料
                # 按行切分字符串为一个数组
                corpus_array = raw_corpus.splitlines()
                raw_corpus = ""
                for line in corpus_array:
                    line = line.strip()
                    # raw_corpus = self.simple_pruneLine(line,raw_corpus)
                    raw_corpus = self.custom_pruneLine(line, raw_corpus)
                # 拼出分词后语料分类目录
                pos_dir = self.pos_path + mydir + "/"
                if not os.path.exists(pos_dir):  # 如果没有创建
                    os.makedirs(pos_dir)
                file_write = open(pos_dir + file_path, "wb")
                file_write.write(raw_corpus)
                file_write.close()  # 关闭写入的文件
                file_read.close()
        print("中文语料修改处理成功！！！")

    # 对行的简单修剪
    def simple_pruneLine(self, line, raw_corpus):
        if line != "":
            raw_corpus += line
        return raw_corpus

    # 对预处理后语料进行分词,并持久化。
    # 处理后在segment_path下建立与pos_path相同的子目录和文件结构
    def segment(self):
        if self.segment_path == "" or self.pos_path == "":
            print("segment_path或pos_path不能为空")
            return
        dir_list = os.listdir(self.pos_path)
        # 获取每个目录下所有的文件
        for mydir in dir_list:
            class_path = self.pos_path + mydir + "/"  # 拼出分类子目录的路径
            file_list = os.listdir(class_path)  # 获取class_path下的所有文件
            for file_path in file_list:  # 遍历所有文件
                file_name = class_path + file_path  # 拼出文件名全路径
                file_read = open(file_name, "rb")  # 打开一个文件
                raw_corpus = file_read.read()  # 读取未分词语料
                seg_corpus = jieba.cut(raw_corpus)  # 结巴分词操作
                # 拼出分词后语料分类目录
                seg_dir = self.segment_path + mydir + "/"
                if not os.path.exists(seg_dir):  # 如果没有创建
                    os.makedirs(seg_dir)
                file_write = open(seg_dir + file_path, "wb")  # 创建分词后语料文件，文件名与未分词语料相同
                file_write.write(" ".join(seg_corpus))  # 用空格将分词结果分开并写入到分词后语料文件中
                file_read.close()  # 关闭打开的文件
                file_write.close()  # 关闭写入的文件
        print("中文语料分词成功完成！！！")

        # 打包分词后训练语料

    def train_bag(self):
        if (
            self.segment_path == ""
            or self.wordbag_path == ""
            or self.trainset_name == ""
        ):
            print("segment_path或wordbag_path,trainset_name不能为空")
            return
        # 获取corpus_path下的所有子分类
        dir_list = os.listdir(self.segment_path)
        self.data_set.target_name = dir_list
        # 获取每个目录下所有的文件
        for mydir in dir_list:
            class_path = self.segment_path + mydir + "/"  # 拼出分类子目录的路径
            file_list = os.listdir(class_path)  # 获取class_path下的所有文件
            for file_path in file_list:  # 遍历所有文档
                file_name = class_path + file_path  # 拼出文件名全路径
                self.data_set.filenames.append(file_name)  # 把文件路径附加到数据集中
                self.data_set.label.append(
                    self.data_set.target_name.index(mydir)
                )  # 把文件分类标签附加到数据集中
                file_read = open(file_name, "rb")  # 打开一个文件
                seg_corpus = file_read.read()  # 读取语料
                self.data_set.contents.append(seg_corpus)  # 构建分词文本内容列表
                file_read.close()
                # 词袋对象持久化
        file_obj = open(self.wordbag_path + self.trainset_name, "wb")
        pickle.dump(self.data_set, file_obj)
        file_obj.close()
        print("分词语料打包成功完成！！！")

        # 计算训练语料的tfidf权值并持久化为词袋

    def tfidf_bag(self):
        if (
            self.wordbag_path == ""
            or self.wordbag_name == ""
            or self.stopword_path == ""
        ):
            print("wordbag_path，word_bag或stopword_path不能为空")
            return
        # 读取持久化后的训练集对象
        file_obj = open(self.wordbag_path + self.trainset_name, "rb")
        self.data_set = pickle.load(file_obj)
        file_obj.close()
        # 定义词袋数据结构: tdm:tf-idf计算后词袋
        self.wordbag.target_name = self.data_set.target_name
        self.wordbag.label = self.data_set.label
        self.wordbag.filenames = self.data_set.filenames
        # 构建语料
        corpus = self.data_set.contents
        stpwrdlst = self.getStopword(self.stopword_path)
        # 使用TfidfVectorizer初始化向量空间模型--创建词袋
        vectorizer = TfidfVectorizer(
            stop_words=stpwrdlst, sublinear_tf=True, max_df=0.5
        )
        # 该类会统计每个词语的tf-idf权值
        transformer = TfidfTransformer()
        # 文本转为词频矩阵,单独保存字典文件
        self.wordbag.tdm = vectorizer.fit_transform(corpus)
        self.wordbag.vocabulary = vectorizer.vocabulary_
        # 创建词袋的持久化
        file_obj = open(self.wordbag_path + self.wordbag_name, "wb")
        pickle.dump(self.wordbag, file_obj)
        file_obj.close()
        print("if-idf词袋创建成功！！！")

        # 导入获取停止词列表

    def getStopword(self, stopword_path):
        # 从文件导入停用词表
        stpwrd_dic = open(stopword_path, "rb")
        stpwrd_content = stpwrd_dic.read()
        # 将停用词表转换为list
        stpwrdlst = stpwrd_content.splitlines()
        stpwrd_dic.close()
        return stpwrdlst

        # 验证持久化结果：

    def verify_trainset(self):
        file_obj = open(self.wordbag_path + self.trainset_name, "rb")
        # 读取持久化后的对象
        self.data_set = pickle.load(file_obj)
        file_obj.close()
        # 输出数据集包含的所有类别
        print(self.data_set.target_name)
        # 输出数据集包含的所有类别标签数
        print(len(self.data_set.label))
        print(len(self.data_set.filenames))
        # 输出数据集包含的文件内容数
        # for filenames,content in zip(self.data_set.filenames[0:10],self.data_set.contents[0:10]):
        # 	print(filenames,":")
        # 	print(content)
        print(len(self.data_set.contents))

    def verify_wordbag(self):
        file_obj = open(self.wordbag_path + self.wordbag_name, "rb")
        # 读取持久化后的对象
        self.wordbag = pickle.load(file_obj)
        file_obj.close()
        # 输出数据集包含的所有类别
        print(self.wordbag.target_name)
        # 输出数据集包含的所有类别标签数
        print(len(self.wordbag.label))
        # 输出数据集包含的文件内容数
        print(self.wordbag.tdm.shape)

    # 只进行tfidf权值计算：stpwrdlst:停用词表;myvocabulary:导入的词典
    # 在分类时便于让两个TfidfVectorizer共享一个vocabulary：
    def tfidf_value(self, test_data, stpwrdlst, myvocabulary):
        vectorizer = TfidfVectorizer(vocabulary=myvocabulary)
        transformer = TfidfTransformer()
        return vectorizer.fit_transform(test_data)

    # 导出词袋模型：
    def load_wordbag(self):
        file_obj = open(self.wordbag_path + self.wordbag_name, "rb")
        self.wordbag = pickle.load(file_obj)
        file_obj.close()

    # 导出训练语料集
    def load_trainset(self):
        file_obj = open(self.wordbag_path + self.trainset_name, "rb")
        self.data_set = pickle.load(file_obj)
        file_obj.close()


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
