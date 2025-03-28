"""
text_classify-master


##文本分类

###文本分词
    ci_seg.py 文本分词
        分词：jieba
        文本编码问题：统一utf-8编码

###转为bunch对象
    to_bunch.py 分词后的预料库转为bunch
        bunch对象
            target_name:是一个list，存放的是整个数据集的类别集合。
            label:是一个list，存放的是所有文本的标签。
            filenames:是一个list，存放的是所有文本文件的名字。
            contents:是一个list，分词后文本文件词向量形式

###词向量空间
    tfidf_train.py
        bunch_path = "train_word_bag/train_set.dat" #导入训练集Bunch的路径
        space_path = "train_word_bag/tfdifspace.dat" # 词向量空间保存路径
    tfidf_test.py
        bunch_path = "test_word_bag/test_set.dat" # 导入训练集Bunch的路径
        space_path = "test_word_bag/testspace.dat" # 词向量空间保存路径

###分类器 *select_test.py

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

"""
###文本分词
    ci_seg.py 文本分词
        分词：jieba
        文本编码问题：统一utf-8编码
"""

import jieba
import chardet


# 保存至文件
def savefile(savepath, content):
    with open(savepath, "wb") as fp:
        fp.write(content)


# 读取文件
def readfile(path):
    with open(path, "rb") as fp:
        content = fp.read()
        cod = chardet.detect(content)["encoding"]
    return content.decode(cod)


def corpus_segment(train_set, seg_path):
    # catelist = os.listdir(corpus_path)  # 获取corpus_path下的所有子目录
    catelist = train_set.keys()
    for myclass in catelist:
        # 这里mydir就是train_corpus/art/21.txt中的art（即catelist中的一个类别）

        seg_dir = seg_path + str(myclass) + "/"  # 拼出分词后存贮的对应目录路径如：train_cor       art/

        if not os.path.exists(seg_dir):  # 是否存在分词目录，如果没有则创建该目录
            os.makedirs(seg_dir)

        file_list = train_set[myclass]  # 获取未分词语料库中某一类别中的所有文本
        file_num = 0
        for content in file_list:  # 遍历类别目录下的所有文件
            file_name = str(file_num) + ".txt"
            content = content.replace("\r\n", "")  # 删除换行
            content = content.replace(" ", "")  # 删除空行、多余的空格
            content_seg = jieba.cut(content)  # 为文件内容分词
            savefile(seg_dir + file_name, " ".join(content_seg).encode())
            file_num += 1

    print("中文语料分词结束！！！")


def corpus_test(corpus_path, seg_path):
    """
    corpus_path是未分词语料库路径
    seg_path是分词后语料库存储路径
    """
    catelist = os.listdir(corpus_path)  # 获取corpus_path下的所有子目录
    """
    其中子目录的名字就是类别名，例如： 
    train_corpus/art/21.txt中，'train_corpus/'是corpus_path，'art'是catelist中的一个成员 
    """

    # 获取每个目录（类别）下所有的文件
    for mydir in catelist:
        """
        这里mydir就是train_corpus/art/21.txt中的art（即catelist中的一个类别）
        """
        class_path = corpus_path + mydir + "/"  # 拼出分类子目录的路径如：train_corpus/art/
        seg_dir = seg_path + mydir + "/"  # 拼出分词后存贮的对应目录路径如：train_corpus_seg/art/

        if not os.path.exists(seg_dir):  # 是否存在分词目录，如果没有则创建该目录
            os.makedirs(seg_dir)

        file_list = os.listdir(class_path)  # 获取未分词语料库中某一类别中的所有文本
        """
        train_corpus/art/中的 
        21.txt, 
        22.txt, 
        23.txt 
        ... 
        file_list=['21.txt','22.txt',...] 
        """
        for file_path in file_list:  # 遍历类别目录下的所有文件
            fullname = class_path + file_path  # 拼出文件名全路径如：train_corpus/art/21.txt
            content = readfile(fullname)  # 读取文件内容

            """此时，content里面存贮的是原文本的所有字符，例如多余的空格、空行、回车等等， 
            接下来，我们需要把这些无关痛痒的字符统统去掉，变成只有标点符号做间隔的紧凑的文本内容 
            """
            content = content.replace("\r\n", "")  # 删除换行
            content = content.replace(" ", "")  # 删除空行、多余的空格
            content_seg = jieba.cut(content)  # 为文件内容分词
            savefile(
                seg_dir + file_path, (" ".join(content_seg)).encode("utf-8")
            )  # 将处理后的文件保存到分词后语料目录

    print("中文语料分词结束！！！")


if __name__ == "__main__":
    # 对训练集进行分词
    """
    1:品牌
    2:价格
    3:项目简介
    4:效果
    """
    train_set = {
        1: [
            "厨房橱柜",
            "无锡装修公司",
            "月星家居",
            "实木床",
            "青山厨柜",
            "实木复合地板",
            "无锡建材市场在哪里",
            "无锡华夏家居港",
            "实木门",
            "华夏家居港",
            "木门十大名牌有哪些",
            "橱柜品牌",
            "瓷砖品牌",
            "地板品牌",
            "东鹏瓷砖",
            "复合地板十大排名",
            "樱花木门是几线品牌",
            "马桶品牌排行榜",
            "国内十大马桶品牌",
            "十大卫浴品牌",
        ],
        2: [
            "实木门价格",
            "红酸枝家具价格",
            "一套威法橱柜要多少钱",
            "无锡双11建材那里有优惠活动",
            "木地板价格",
            "优格橱柜多少钱一平米",
            "橡木地板的价格",
            "红酸枝家具大降价",
            "一般实木门价格",
            "整体卫生间价格多少",
            "toto马桶价格",
            "toto智能马桶价格",
            "索非亚衣柜价格",
            "白酸枝一套家具多少钱",
            "红酸枝的价格",
            "无锡买家具哪里便宜",
        ],
        3: [
            "无锡家装节2017",
            "无锡家装节",
            "家博会",
            "无锡家装博览会",
            "无锡家博会",
            "无锡2012年10月15日家博会",
            "2017无锡家装博览会",
            "2017无锡新体家装节",
            "无锡建材团购活动",
            "无锡新体家装节",
            "兔狗家装节",
            "无锡广电家博会",
            "无锡广电家装节2017",
            "家装节",
            "2017无锡家装节",
            "2017无锡广电家装节",
            "无锡家博会2017",
            "无锡家装博览会2016",
            "2017无锡家装节时间",
            "2017无锡太湖博览中心家装节",
        ],
        4: [
            "卫生间装修效果图",
            "客厅装修效果图",
            "装修效果图",
            "客厅背影墙装修效果图",
            "地板砖效果图",
            "窗帘效果图",
            "复式楼装修效果图",
            "餐厅装修效果图",
            "开放式厨房装修效果图",
            "装潢效果图",
        ],
    }

    seg_path = "./clickplus_train_seg/"  # 分词后分类语料库路径
    corpus_segment(train_set, seg_path)
    # 对测试集进行分词
    # test_set = "./clickplus_test_new/"  # 未分词分类语料库路径
    # seg_path = "./clickplus_test_seg/"  # 分词后分类语料库路径
    # corpus_segment(corpus_path,seg_path)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
###转为bunch对象
    to_bunch.py 分词后的预料库转为bunch
        bunch对象
            target_name:是一个list，存放的是整个数据集的类别集合。
            label:是一个list，存放的是所有文本的标签。
            filenames:是一个list，存放的是所有文本文件的名字。
            contents:是一个list，分词后文本文件词向量形式
"""

import pickle

"""
事实上python中还有一个也叫作pickle的包，与这里的名字相同了，无所谓 
关于cPickle与pickle，请参考博主另一篇博文： 
python核心模块之pickle和cPickle讲解 
http://blog.csdn.net/github_36326955/article/details/54882506 
本文件代码下面会用到cPickle中的函数cPickle.dump 
"""

from sklearn.datasets._base import Bunch

# 这个您无需做过多了解，您只需要记住以后导入Bunch数据结构就像这样就可以了。
# 今后的博文会对sklearn做更有针对性的讲解


def _readfile(path):
    # 读取文件
    # 函数名前面带一个_,是标识私有函数
    # 仅仅用于标明而已，不起什么作用，
    # 外面想调用还是可以调用，
    # 只是增强了程序的可读性
    # print(path)
    with open(path, "rb") as fp:  # with as句法前面的代码已经多次介绍过，今后不再注释
        content = fp.read().decode("utf-8")
    return content


def corpus2Bunch(wordbag_path, seg_path):
    catelist = os.listdir(seg_path)  # 获取seg_path下的所有子目录，也就是分类信息
    # 创建一个Bunch实例
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    bunch.target_name.extend(catelist)
    """
    extend(addlist)是python list中的函数，意思是用新的list（addlist）去扩充 
    原来的list 
    """
    # 获取每个目录下所有的文件
    for mydir in catelist:
        class_path = seg_path + mydir + "/"  # 拼出分类子目录的路径
        file_list = os.listdir(class_path)  # 获取class_path下的所有文件
        for file_path in file_list:  # 遍历类别目录下文件
            fullname = class_path + file_path  # 拼出文件名全路径
            bunch.label.append(mydir)
            bunch.filenames.append(fullname)
            bunch.contents.append(_readfile(fullname))  # 读取文件内容
            # append(element)是python list中的函数，意思是向原来的list中添加element，注意与extend()函数的区别
    # 将bunch存储到wordbag_path路径中
    with open(wordbag_path, "wb") as file_obj:
        pickle.dump(bunch, file_obj)
    print("构建文本bunch对象结束！！！")


if __name__ == "__main__":  # 这个语句前面的代码已经介绍过，今后不再注释
    # 对训练集进行Bunch化操作：
    wordbag_path = "train_word_bag/train_set.dat"  # Bunch存储路径
    seg_path = "clickplus_train_seg/"  # 分词后分类语料库路径
    corpus2Bunch(wordbag_path, seg_path)

    # 对测试集进行Bunch化操作：
    # wordbag_path = "test_word_bag/test_set.dat"  # Bunch存储路径
    # seg_path = "clickplus_test_seg/"  # 分词后分类语料库路径
    # corpus2Bunch(wordbag_path, seg_path)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
###词向量空间
    tfidf_train.py
        bunch_path = "train_word_bag/train_set.dat" #导入训练集Bunch的路径
        space_path = "train_word_bag/tfdifspace.dat" # 词向量空间保存路径
    tfidf_test.py
        bunch_path = "test_word_bag/test_set.dat" # 导入训练集Bunch的路径
        space_path = "test_word_bag/testspace.dat" # 词向量空间保存路径
"""

# tfidf_train.py

# 引入Bunch类
from sklearn.datasets._base import Bunch
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer  # 这个东西下面会讲

"""
tf 词频    
idf 逆文档频率
CountVectorizer 词频矩阵
TfidfTransformer 词频矩阵转为tf-idf权重
TfidfVectorizer 一次性计算tf-idf :CountVectorizer+TfidfTransformer
"""


# 读取文件
def _readfile(path):
    with open(path, "rb") as fp:
        content = fp.read()
    return content


# 读取bunch对象
def _readbunchobj(path):
    with open(path, "rb") as file_obj:
        bunch = pickle.load(file_obj)
        # print(type(bunch.contents))
    return bunch


# 写入bunch对象
def _writebunchobj(path, bunchobj):
    with open(path, "wb") as file_obj:
        pickle.dump(bunchobj, file_obj)


# 这个函数用于创建TF-IDF词向量空间
def vector_space(stopword_path, bunch_path, space_path):
    stpwrdlst = _readfile(stopword_path).splitlines()  # 读取停用词
    bunch = _readbunchobj(bunch_path)  # 导入分词后的词向量bunch对象
    # 构建tf-idf词向量空间对象
    tfidfspace = Bunch(
        target_name=bunch.target_name,
        label=bunch.label,
        filenames=bunch.filenames,
        tdm=[],
        vocabulary={},
    )

    vectorizer = TfidfVectorizer(stop_words=stpwrdlst, sublinear_tf=True, max_df=0.5)
    # sublinear_tf：计算tf值采用亚线性策略。比如，我们以前算tf是词频，现在用1+log(tf)来充当词频。
    # max_df:有些词，他们的文档频率太高了（一个词如果每篇文档都出现，那还有必要用它来区分文本类别吗？当然不用了呀），所以，我们可以 设定一个阈值，比如float类型0.5（取值范围[0.0,1.0]）,表示这个词如果在整个数据集中超过50%的文本都出现了，那么我们也把它列 为临时停用词。当然你也可以设定为int型，例如max_df=10,表示这个词如果在整个数据集中超过10的文本都出现了，那么我们也把它列 为临时停用词。
    # 此时tdm里面存储的就是if-idf权值矩阵
    tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)  # fit_transform 计算if-idf
    tfidfspace.vocabulary = vectorizer.vocabulary_
    print(vectorizer.vocabulary_)
    # vocabulary_：是CountVectorizer()和TfidfVectorizer()的内部成员，表示最终得到的词向量空间坐标
    #
    _writebunchobj(space_path, tfidfspace)
    print("if-idf词向量空间实例创建成功！！！")


if __name__ == "__main__":
    stopword_path = "train_word_bag/hlt_stop_words.txt"  # 停用词表的路径
    bunch_path = "train_word_bag/train_set.dat"  # 导入训练集Bunch的路径
    space_path = "train_word_bag/tfdifspace.dat"  # 词向量空间保存路径
    vector_space(stopword_path, bunch_path, space_path)

# tfidf_test.py

# 引入Bunch类
from sklearn.datasets._base import Bunch
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

"""
tf 词频    
idf 逆文档频率
CountVectorizer 词频矩阵
TfidfTransformer 词频矩阵转为tf-idf权重
TfidfVectorizer 一次性计算tf-idf :CountVectorizer+TfidfTransformer
"""


# tf-idf=tf*idf
def _readfile(path):
    with open(path, "rb") as fp:
        content = fp.read()
    return content


def _readbunchobj(path):
    with open(path, "rb") as file_obj:
        bunch = pickle.load(file_obj)
    return bunch


def _writebunchobj(path, bunchobj):
    with open(path, "wb") as file_obj:
        pickle.dump(bunchobj, file_obj)


def vector_space(stopword_path, bunch_path, space_path, train_tfidf_path):
    # 读取停用词
    stpwrdlst = _readfile(stopword_path).splitlines()
    # 读取测试bunch对象
    bunch = _readbunchobj(bunch_path)
    # 构建tf-idf词向量空间对象
    tfidfspace = Bunch(
        target_name=bunch.target_name,
        label=bunch.label,
        filenames=bunch.filenames,
        contents=bunch.contents,
        tdm=[],
        vocabulary={},
    )
    # tmd    存放if-idf权重
    # vocabulary 词向量空间索引
    # 导入训练集的TF-IDF词向量空间
    trainbunch = _readbunchobj(train_tfidf_path)
    # 词向量空间索引 {'实木门': 41, '哪些': 29, 'toto': 6, '餐厅': 79} 词向量空间，以及对应的维度
    tfidfspace.vocabulary = trainbunch.vocabulary
    #
    vectorizer = TfidfVectorizer(
        stop_words=stpwrdlst,
        sublinear_tf=True,
        max_df=0.5,
        vocabulary=trainbunch.vocabulary,
    )
    # 计算测试if-idf
    tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
    # if-idf 词向量测试空间 存入bunch
    _writebunchobj(space_path, tfidfspace)
    print("if-idf词向量测试空间实例创建成功！！！")


if __name__ == "__main__":
    stopword_path = "train_word_bag/hlt_stop_words.txt"  # 停用词表的路径
    bunch_path = "test_word_bag/test_set.dat"  # bunch对象保存路径
    space_path = "test_word_bag/testspace.dat"  # 测试词向量空间
    train_tfidf_path = "train_word_bag/tfdifspace.dat"  # 训练词向量空间 权重矩阵
    vector_space(stopword_path, bunch_path, space_path, train_tfidf_path)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
###分类器 *select_test.py
"""
# select_test.py

import pickle
from sklearn.naive_bayes import MultinomialNB  # 导入多项式贝叶斯算法


# 读取bunch对象
def _readbunchobj(path):
    with open(path, "rb") as file_obj:
        bunch = pickle.load(file_obj)
    return bunch


# 导入训练集
trainpath = "train_word_bag/tfdifspace.dat"
train_set = _readbunchobj(trainpath)

# 导入测试集
testpath = "test_word_bag/testspace.dat"
test_set = _readbunchobj(testpath)

# 训练分类器：输入词袋向量和分类标签，alpha:0.001 alpha越小，迭代次数越多，精度越高
clf = MultinomialNB(alpha=0.001).fit(train_set.tdm, train_set.label)

# 预测分类结果
predicted = clf.predict(test_set.tdm)

for flabel, file_name, expct_cate in zip(test_set.label, test_set.filenames, predicted):
    if flabel != expct_cate:
        print(file_name, ": 实际类别:", flabel, " -->预测类别:", expct_cate)

print("预测完毕!!!")

# 计算分类精度：
from sklearn import metrics


def metrics_result(actual, predict):
    print(
        "精度:{0:.3f}".format(
            metrics.precision_score(actual, predict, average="weighted")
        )
    )


metrics_result(test_set.label, predicted)

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
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
