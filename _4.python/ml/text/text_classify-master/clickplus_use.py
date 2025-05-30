from ci_seg import *
from tfidf_test import *
from to_bunch import *
import pickle
from sklearn.naive_bayes import MultinomialNB  # 多項單純貝氏分類器


# 对测试集进行分词
def test(test_txt):
    test_set = {1: test_txt}
    seg_path = "./clickplus_test_seg/"  # 分词后分类语料库路径
    corpus_segment(test_set, seg_path)

    # 对测试集进行Bunch化操作：
    wordbag_path = "test_word_bag/test_set.dat"  # Bunch存储路径
    seg_path = "clickplus_test_seg/"  # 分词后分类语料库路径
    corpus2Bunch(wordbag_path, seg_path)

    # 词向量训练
    stopword_path = "train_word_bag/hlt_stop_words.txt"  # 停用词表的路径
    bunch_path = "test_word_bag/test_set.dat"  # 词向量空间保存路径
    space_path = "test_word_bag/testspace.dat"  # TF-IDF词向量空间保存路径
    train_tfidf_path = "train_word_bag/tfdifspace.dat"
    vector_space(stopword_path, bunch_path, space_path, train_tfidf_path)

    # 读取bunch对象
    def _readbunchobj(path):
        with open(path, "rb") as file_obj:
            bunch = pickle.load(file_obj)
        return bunch

    # 导入训练集
    train_set = _readbunchobj(train_tfidf_path)

    # 导入测试集

    test_set = _readbunchobj(space_path)

    # 训练分类器：输入词袋向量和分类标签，alpha:0.001 alpha越小，迭代次数越多，精度越高
    clf = MultinomialNB(alpha=0.001).fit(train_set.tdm, train_set.label)  # 多項單純貝氏分類器

    # 预测分类结果
    predicted = clf.predict(test_set.tdm)

    for flabel, predict_content, expct_cate in zip(
        test_set.label, test_set.contents, predicted
    ):
        print(predict_content, " -->预测类别:", expct_cate)

    print("预测完毕!!!")

    # 计算分类精度：
    # from sklearn import metrics
    # def metrics_result(actual, predict):
    #    metrics.precision_score(actual, predict,average='weighted')
    #
    #
    # metrics_result(test_set.label, predicted)


if __name__ == "__main__":
    test_txt = ["淋雨房怎么房顶", "步阳喜临门", "泰陶卫浴是什么档次", "浴霸多少钱"]
    test(test_txt)
