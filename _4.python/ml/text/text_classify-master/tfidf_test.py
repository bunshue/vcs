import sys  

# 引入Bunch类  
from sklearn.datasets.base import Bunch  
import  pickle  
from sklearn.feature_extraction.text import TfidfVectorizer  
'''
tf 词频    
idf 逆文档频率
CountVectorizer 词频矩阵
TfidfTransformer 词频矩阵转为tf-idf权重
TfidfVectorizer 一次性计算tf-idf :CountVectorizer+TfidfTransformer
'''
tf-idf=tf*idf
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
  
def vector_space(stopword_path,bunch_path,space_path,train_tfidf_path):  
    #读取停用词
    stpwrdlst = _readfile(stopword_path).splitlines()
    #读取测试bunch对象
    bunch = _readbunchobj(bunch_path)
    #构建tf-idf词向量空间对象 
    tfidfspace = Bunch(target_name=bunch.target_name, label=bunch.label, filenames=bunch.filenames,contents=bunch.contents, tdm=[], vocabulary={})  
    #tmd    存放if-idf权重
    #vocabulary 词向量空间索引
    #导入训练集的TF-IDF词向量空间  
    trainbunch = _readbunchobj(train_tfidf_path)  
    #词向量空间索引 {'实木门': 41, '哪些': 29, 'toto': 6, '餐厅': 79} 词向量空间，以及对应的维度
    tfidfspace.vocabulary = trainbunch.vocabulary  
    #
    vectorizer = TfidfVectorizer(stop_words=stpwrdlst, sublinear_tf=True, max_df=0.5,vocabulary=trainbunch.vocabulary)  
    #计算测试if-idf
    tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)  
    #if-idf 词向量测试空间 存入bunch
    _writebunchobj(space_path, tfidfspace)  
    print("if-idf词向量测试空间实例创建成功！！！") 
  
if __name__ == '__main__':  
    stopword_path = "train_word_bag/hlt_stop_words.txt"#停用词表的路径  
    bunch_path = "test_word_bag/test_set.dat"   # bunch对象保存路径  
    space_path = "test_word_bag/testspace.dat"   # 测试词向量空间
    train_tfidf_path="train_word_bag/tfdifspace.dat"   #训练词向量空间 权重矩阵
    vector_space(stopword_path,bunch_path,space_path,train_tfidf_path)  