import sys

# 引入Bunch类
from sklearn.datasets._base import Bunch
import pickle  # 之前已经说过，不再赘述
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
