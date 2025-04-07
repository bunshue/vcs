"""
text01

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

import scipy
import sklearn.linear_model
from sklearn import tree
from sklearn import datasets
from sklearn import metrics
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_moons
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA  # KernelPCA 萃取特徵

from matplotlib.colors import ListedColormap
from sklearn.preprocessing import MinMaxScaler


def show():
    plt.show()
    pass


# 保存至文件
def savefile(savepath, content):
    fp = open(savepath, "w", encoding="UTF-8-sig")
    fp.write(content)
    fp.close()


# 读取文件
def readfile(path):
    fp = open(path, "r", encoding="UTF-8-sig")
    content = fp.read()
    fp.close()
    return content


# 读取bunch对象
def readbunchobj(path):
    print("讀取檔案 :", path)
    file_obj = open(path, "rb")
    bunch = pickle.load(file_obj)
    file_obj.close()
    return bunch


# 写入bunch对象
def writebunchobj(path, bunchobj):
    print("寫入檔案 :", path)
    file_obj = open(path, "wb")
    pickle.dump(bunchobj, file_obj)
    file_obj.close()


# 计算分类精度：
def metrics_result(actual, predict):
    print("aaaa")
    print("精度:{0:.3f}".format(metrics.precision_score(actual, predict)))
    print("bbbb")
    print("召回:{0:0.3f}".format(metrics.recall_score(actual, predict)))
    print("cccc")
    print("f1-score:{0:.3f}".format(metrics.f1_score(actual, predict)))


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# corpus_segment.py

import jieba

corpus_path = "train_corpus_small/"  # 未分词分类语料库路径
seg_path = "tmp_train_corpus_seg/"  # 分词后分类语料库路径

catelist = os.listdir(corpus_path)  # 获取corpus_path下的所有子目录
print(catelist)

# 获取每个目录下所有的文件
for mydir in catelist:
    class_path = corpus_path + mydir + "/"  # 拼出分类子目录的路径
    seg_dir = seg_path + mydir + "/"  # 拼出分词后语料分类目录
    if not os.path.exists(seg_dir):  # 是否存在目录，如果没有创建
        os.makedirs(seg_dir)
    file_list = os.listdir(class_path)  # 获取class_path下的所有文件
    for file_path in file_list:  # 遍历类别目录下文件
        fullname = class_path + file_path  # 拼出文件名全路径
        print("分詞前之檔案 :", fullname)
        content = readfile(fullname).strip()  # 读取文件内容
        content = content.replace("\r\n", "")  # 删除换行和多余的空格
        content_seg = jieba.cut(content.strip())  # 为文件内容分词
        print("分詞後之檔案 :", seg_dir + file_path)
        savefile(seg_dir + file_path, " ".join(content_seg))  # 将处理后的文件保存到分词后语料目录

print("中文语料分词结束！！！")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# kNN.py

import operator


def createDataSet():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ["A", "A", "B", "B"]
    return group, labels


# 夹角余弦距离公式
def cosdist(vector1, vector2):
    Lv1 = sqrt(vector1 * vector1.T)
    Lv2 = sqrt(vector2 * vector2.T)
    return vector1 * vector2.T / (Lv1 * Lv2)


# kNN分类器
# 测试集：inX
# 训练集：dataSet
# 类别标签：labels
# k:k个邻居数
def classify(testdata, dataSet, labels, k):
    # 返回样本集的行数
    dataSetSize = dataSet.shape[0]
    # 计算测试集与训练集之间的距离：标准欧氏距离
    # 1.计算测试项与训练集各项的差
    diffMat = np.tile(testdata, (dataSetSize, 1)) - dataSet
    # 2.计算差的平方和
    sqDiffMat = diffMat**2
    # 3.按列求和
    sqDistances = sqDiffMat.sum(axis=1)
    # 4.生成标准化欧氏距离
    distances = sqDistances**0.5
    print(distances)
    # 5.根据生成的欧氏距离大小排序,结果为索引号
    sortedDistIndicies = distances.argsort()
    classCount = {}
    # 获取欧氏距离的前三项作为参考项
    for i in range(k):  # i = 0~(k-1)
        # 按序号顺序返回样本集对应的类别标签
        voteIlabel = labels[sortedDistIndicies[i]]
        # 为字典classCount赋值,相同key，其value加1
        # key:voteIlabel，value: 符合voteIlabel标签的训练集数
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # 对分类字典classCount按value重新排序
    # sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    # 该句是按字典值排序的固定用法
    # classCount.items()：字典迭代器函数
    # key：排序参数；operator.itemgetter(1)：多级排序
    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True
    )
    # 返回序最高的一项
    return sortedClassCount[0][0]


k = 3
testdata = [0.2, 0.2]
dataSet, labels = createDataSet()

# 绘图
fig = plt.figure()
ax = fig.add_subplot(111)
indx = 0
for point in dataSet:
    if labels[indx] == "A":
        ax.scatter(point[0], point[1], c="blue", marker="o", linewidths=0, s=300)
        plt.annotate(
            "(" + str(point[0]) + "," + str(point[1]) + ")", xy=(point[0], point[1])
        )
    else:
        ax.scatter(point[0], point[1], c="red", marker="^", linewidths=0, s=300)
        plt.annotate(
            "(" + str(point[0]) + ", " + str(point[1]) + ")", xy=(point[0], point[1])
        )
    indx += 1

ax.scatter(testdata[0], testdata[1], c="green", marker="s", linewidths=0, s=300)
plt.annotate(
    "(" + str(testdata[0]) + ", " + str(testdata[1]) + ")",
    xy=(testdata[0], testdata[1]),
)

show()

print(classify(testdata, dataSet, labels, k))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Nbayes.py


def loadDataSet():
    postingList = [
        ["my", "dog", "has", "flea", "problems", "help", "please"],
        ["maybe", "not", "take", "him", "to", "dog", "park", "stupid"],
        ["my", "dalmation", "is", "so", "cute", "I", "love", "him", "my"],
        ["stop", "posting", "stupid", "worthless", "garbage"],
        ["mr", "licks", "ate", "my", "steak", "how", "to", "stop", "him"],
        ["quit", "buying", "worthless", "dog", "food", "stupid"],
    ]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec


class NBayes(object):
    def __init__(self):
        self.vocabulary = []  # 词典
        self.idf = 0  # 词典的idf权值向量
        self.tf = 0  # 训练集的权值矩阵
        self.tdm = 0  # P(x|yi)
        self.Pcates = {}  # P(yi)--是个类别字典
        self.labels = []  # 对应每个文本的分类，是个外部导入的列表
        self.doclength = 0  # 训练集文本数
        self.vocablen = 0  # 词典词长
        self.testset = 0  # 测试集

    # 	加载训练集并生成词典，以及tf, idf值
    def train_set(self, trainset, classVec):
        self.cate_prob(classVec)  # 计算每个分类在数据集中的概率：P(yi)
        self.doclength = len(trainset)
        tempset = set()
        [tempset.add(word) for doc in trainset for word in doc]  # 生成词典
        self.vocabulary = list(tempset)
        self.vocablen = len(self.vocabulary)
        self.calc_wordfreq(trainset)
        # self.calc_tfidf(trainset)  # 生成tf-idf权值
        self.build_tdm()  # 按分类累计向量空间的每维值：P(x|yi)

    # 生成 tf-idf
    def calc_tfidf(self, trainset):
        self.idf = np.zeros([1, self.vocablen])
        self.tf = np.zeros([self.doclength, self.vocablen])
        for indx in range(self.doclength):
            for word in trainset[indx]:
                self.tf[indx, self.vocabulary.index(word)] += 1
            # 消除不同句长导致的偏差
            self.tf[indx] = self.tf[indx] / float(len(trainset[indx]))
            for signleword in set(trainset[indx]):
                self.idf[0, self.vocabulary.index(signleword)] += 1
        self.idf = np.log(float(self.doclength) / self.idf)
        self.tf = np.multiply(self.tf, self.idf)  # 矩阵与向量的点乘

    # 生成普通的词频向量
    def calc_wordfreq(self, trainset):
        self.idf = np.zeros([1, self.vocablen])  # 1*词典数
        self.tf = np.zeros([self.doclength, self.vocablen])  # 训练集文件数*词典数
        for indx in range(self.doclength):  # 遍历所有的文本
            for word in trainset[indx]:  # 遍历文本中的每个词
                self.tf[indx, self.vocabulary.index(word)] += 1  # 找到文本的词在字典中的位置+1
            for signleword in set(trainset[indx]):
                self.idf[0, self.vocabulary.index(signleword)] += 1

    # 计算每个分类在数据集中的概率：P(yi)
    def cate_prob(self, classVec):
        self.labels = classVec
        labeltemps = set(self.labels)  # 获取全部分类
        for labeltemp in labeltemps:
            # 统计列表中重复的值：self.labels.count(labeltemp)
            self.Pcates[labeltemp] = float(self.labels.count(labeltemp)) / float(
                len(self.labels)
            )

    # 按分类累计向量空间的每维值：P(x|yi)
    def build_tdm(self):
        self.tdm = np.zeros([len(self.Pcates), self.vocablen])  # 类别行*词典列
        sumlist = np.zeros([len(self.Pcates), 1])  # 统计每个分类的总值
        for indx in range(self.doclength):
            self.tdm[self.labels[indx]] += self.tf[indx]  # 将同一类别的词向量空间值加总
            sumlist[self.labels[indx]] = np.sum(
                self.tdm[self.labels[indx]]
            )  # 统计每个分类的总值--是个标量
        self.tdm = self.tdm / sumlist  # P(x|yi)

    # 测试集映射到当前词典
    def map2vocab(self, testdata):
        self.testset = np.zeros([1, self.vocablen])
        for word in testdata:
            self.testset[0, self.vocabulary.index(word)] += 1

    # 输出分类类别
    def predict(self, testset):
        if np.shape(testset)[1] != self.vocablen:
            print("输入错误")
            exit(0)
        predvalue = 0
        predclass = ""
        for tdm_vect, keyclass in zip(self.tdm, self.Pcates):
            # P(x|yi)P(yi)
            temp = np.sum(testset * tdm_vect * self.Pcates[keyclass])
            if temp > predvalue:
                predvalue = temp
                predclass = keyclass
        return predclass


# kNN2.py

import operator


# 夹角余弦距离公式
def cosdist(vector1, vector2):
    return np.dot(vector1, vector2) / (
        np.linalg.norm(vector1) * np.linalg.norm(vector2)
    )


# kNN分类器
# 测试集：testdata
# 训练集：trainSet
# 类别标签：listClasses
# k:k个邻居数
def classify(testdata, trainSet, listClasses, k):
    # 返回样本集的行数
    dataSetSize = trainSet.shape[0]
    # 计算测试集与训练集之间的距离：夹角余弦
    distances = np.array(np.zeros(dataSetSize))
    for indx in range(dataSetSize):
        distances[indx] = cosdist(testdata, trainSet[indx])
    # 5.根据生成的夹角余弦按从大到小排序,结果为索引号
    sortedDistIndicies = np.argsort(-distances)
    classCount = {}
    # 获取角度最小的前三项作为参考项
    for i in range(k):  # i = 0~(k-1)
        # 按序号顺序返回样本集对应的类别标签
        voteIlabel = listClasses[sortedDistIndicies[i]]
        # 为字典classCount赋值,相同key，其value加1
        # key:voteIlabel，value: 符合voteIlabel标签的训练集数
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # 对分类字典classCount按value重新排序
    # sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    # 该句是按字典值排序的固定用法
    # classCount.items()：字典迭代器函数
    # key：排序参数；operator.itemgetter(1)：多级排序
    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True
    )
    # 返回序最高的一项
    return sortedClassCount[0][0]


k = 3
# testdata=[0.2,0.2]
# dataSet,labels = createDataSet()
# print classify(mat(testdata), mat(dataSet), labels, k)
dataSet, listClasses = loadDataSet()

nb = NBayes()
nb.train_set(dataSet, listClasses)
print(classify(nb.tf[3], nb.tf, listClasses, k))

nb.map2vocab(dataSet[3])

print(nb.predict(nb.testset))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Predict.py

import pickle
from sklearn import metrics
from sklearn import feature_extraction
from sklearn.datasets._base import Bunch
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB  # 导入多项式贝叶斯算法


# 导入训练集
trainpath = "train_word_bag/tfdifspace.dat"
train_set = readbunchobj(trainpath)

# 导入测试集
testpath = "test_word_bag/testspace.dat"
test_set = readbunchobj(testpath)

# 应用朴素贝叶斯算法
# 1. 输入词袋向量和分类标签
# alpha:0.001 alpha越小，迭代次数越多，精度越高
clf = MultinomialNB(alpha=0.001).fit(train_set.tdm, train_set.label)

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

print()
print("test_set.label")
print(test_set.label)
print()
print("predicted")
print(predicted)
print()

""" 計算分類精度 NG
metrics_result(test_set.label, predicted)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# segment2Bunch.py

import pickle
from sklearn.datasets._base import Bunch

# Bunch类提供一种key,value的对象形式
# target_name:所有分类集名称列表
# label:每个文件的分类标签列表
# filenames:文件路径
# contents:分词后文件词向量形式
bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])

wordbag_path = "train_word_bag/train_set.dat"  # 未分词分类语料库路径
seg_path = "tmp_train_corpus_seg/"  # 分词后分类语料库路径

catelist = os.listdir(seg_path)  # 获取seg_path下的所有子目录
bunch.target_name.extend(catelist)
# 获取每个目录下所有的文件
for mydir in catelist:
    class_path = seg_path + mydir + "/"  # 拼出分类子目录的路径
    file_list = os.listdir(class_path)  # 获取class_path下的所有文件
    for file_path in file_list:  # 遍历类别目录下文件
        fullname = class_path + file_path  # 拼出文件名全路径
        bunch.label.append(mydir)
        bunch.filenames.append(fullname)
        bunch.contents.append(readfile(fullname).strip())  # 读取文件内容

# 对象持久化
file_obj = open(wordbag_path, "wb")
pickle.dump(bunch, file_obj)
file_obj.close()

print("构建文本对象结束！！！")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# test_space.py

# 引入Bunch类
from sklearn.datasets._base import Bunch

# 引入持久化类
import pickle
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

# 计算训练语料的tfidf权值并持久化为词袋

# 1. 读取停用词表
stopword_path = "train_word_bag/hlt_stop_words.txt"
stpwrdlst = readfile(stopword_path).splitlines()

# 2. 导入分词后的词向量bunch对象
path = "test_word_bag/test_set.dat"  # 词向量空间保存路径
bunch = readbunchobj(path)

# 3. 构建测试集tfidf向量空间
testspace = Bunch(
    target_name=bunch.target_name,
    label=bunch.label,
    filenames=bunch.filenames,
    tdm=[],
    vocabulary={},
)
# 4. 导入训练集的词袋
trainbunch = readbunchobj("train_word_bag/tfdifspace.dat")
# 5. 使用TfidfVectorizer初始化向量空间模型
vectorizer = TfidfVectorizer(
    stop_words=stpwrdlst,
    sublinear_tf=True,
    max_df=0.5,
    vocabulary=trainbunch.vocabulary,
)
transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
# 文本转为tf-idf矩阵,单独保存字典文件
testspace.tdm = vectorizer.fit_transform(bunch.contents)
testspace.vocabulary = trainbunch.vocabulary

# 创建词袋的持久化
space_path = "test_word_bag/testspace.dat"  # 词向量空间保存路径
writebunchobj(space_path, testspace)

print("test词向量空间创建成功！！！")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# test2Bunch.py

import pickle
from sklearn.datasets._base import Bunch


# Bunch类提供一种key,value的对象形式
# target_name:所有分类集名称列表
# label:每个文件的分类标签列表
# filenames:文件路径
# contents:分词后文件词向量形式
bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])

wordbag_path = "test_word_bag/test_set.dat"  # 未分词分类语料库路径
seg_path = "test_corpus_seg/"  # 分词后分类语料库路径

catelist = os.listdir(seg_path)  # 获取seg_path下的所有子目录
bunch.target_name.extend(catelist)
# 获取每个目录下所有的文件
for mydir in catelist:
    class_path = seg_path + mydir + "/"  # 拼出分类子目录的路径
    file_list = os.listdir(class_path)  # 获取class_path下的所有文件
    for file_path in file_list:  # 遍历类别目录下文件
        fullname = class_path + file_path  # 拼出文件名全路径
        bunch.label.append(mydir)
        bunch.filenames.append(fullname)
        bunch.contents.append(readfile(fullname).strip())  # 读取文件内容

# 对象持久化
file_obj = open(wordbag_path, "wb")
pickle.dump(bunch, file_obj)
file_obj.close()

print("构建文本对象结束！！！")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# vector_space.py

# 引入Bunch类
from sklearn.datasets._base import Bunch

# 引入持久化类
import pickle
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer


# 计算训练语料的tfidf权值并持久化为词袋


# 1. 读取停用词表
stopword_path = "train_word_bag/hlt_stop_words.txt"
stpwrdlst = readfile(stopword_path).splitlines()

# 2. 导入分词后的词向量bunch对象
path = "train_word_bag/train_set.dat"  # 词向量空间保存路径
bunch = readbunchobj(path)

# 3. 构建tf-idf词向量空间对象
tfidfspace = Bunch(
    target_name=bunch.target_name,
    label=bunch.label,
    filenames=bunch.filenames,
    tdm=[],
    vocabulary={},
)

# 4. 使用TfidfVectorizer初始化向量空间模型
vectorizer = TfidfVectorizer(stop_words=stpwrdlst, sublinear_tf=True, max_df=0.5)
transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
# 文本转为词频矩阵,单独保存字典文件
tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
tfidfspace.vocabulary = vectorizer.vocabulary_

# 创建词袋的持久化
space_path = "train_word_bag/tfdifspace.dat"  # 词向量空间保存路径
writebunchobj(space_path, tfidfspace)

print("if-idf词向量空间创建成功！！！")

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
