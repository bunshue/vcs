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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
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
seg_path = "train_corpus_small_after/"  # 分词后分类语料库路径
print('分詞前資料夾 :', corpus_path)
print('分詞後資料夾 :', seg_path)

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

# Predict.py

import pickle
from sklearn import metrics
from sklearn import feature_extraction
from sklearn.datasets._base import Bunch
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB  # 多項單純貝氏分類器


# 导入训练集
trainpath = "train_word_bag/tfdifspace.dat"
train_set = readbunchobj(trainpath)

# 导入测试集
testpath = "test_word_bag/testspace.dat"
test_set = readbunchobj(testpath)

# 应用朴素贝叶斯算法
# 1. 输入词袋向量和分类标签
# alpha:0.001 alpha越小，迭代次数越多，精度越高
clf = MultinomialNB(alpha=0.001).fit(train_set.tdm, train_set.label)  # 多項單純貝氏分類器

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

print()
print("test_set.label")
print(test_set.label)
print()
print("predicted")
print(predicted)
print()
"""

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
seg_path = "train_corpus_small_after/"  # 分词后分类语料库路径
print('分詞前資料夾 :', wordbag_path)
print('分詞後資料夾 :', seg_path)

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
wordbag_path = "train_word_bag/train_set_tmp.dat"  # 未分词分类语料库路径
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
print('分詞前資料夾 :', wordbag_path)
print('分詞後資料夾 :', seg_path)

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
