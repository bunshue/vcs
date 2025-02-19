import sys  
import os 

#引入Bunch类
from sklearn.datasets.base import Bunch

#引入持久化类
import pickle
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import TfidfVectorizer  

# 读取文件
def readfile(path):
	fp = open(path,"rb")
	content = fp.read()
	fp.close()
	return content
		
#计算训练语料的tfidf权值并持久化为词袋

#读取bunch对象
def readbunchobj(path):
	file_obj = open(path, "rb")
	bunch = pickle.load(file_obj) 
	file_obj.close()
	return bunch
#写入bunch对象	
def writebunchobj(path,bunchobj):
	file_obj = open(path, "wb")
	pickle.dump(bunchobj,file_obj) 
	file_obj.close()	

# 1. 读取停用词表	
stopword_path = "train_word_bag/hlt_stop_words.txt"
stpwrdlst = readfile(stopword_path).splitlines()

# 2. 导入分词后的词向量bunch对象
path = "train_word_bag/train_set.dat"        # 词向量空间保存路径
bunch	= readbunchobj(path)

# 3. 构建tf-idf词向量空间对象
tfidfspace = Bunch(target_name=bunch.target_name,label=bunch.label,filenames=bunch.filenames,tdm=[],vocabulary={})

# 4. 使用TfidfVectorizer初始化向量空间模型 
vectorizer = TfidfVectorizer(stop_words=stpwrdlst,sublinear_tf = True,max_df = 0.5)
transformer=TfidfTransformer() # 该类会统计每个词语的tf-idf权值
# 文本转为词频矩阵,单独保存字典文件 
tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
tfidfspace.vocabulary = vectorizer.vocabulary_

# 创建词袋的持久化
space_path = "train_word_bag/tfdifspace.dat"        # 词向量空间保存路径
writebunchobj(space_path,tfidfspace)

print("if-idf词向量空间创建成功！！！")

