# coding:utf-8
from sklearn.feature_extraction.text import CountVectorizer

# CountVectorizer类会将文本中的词语转换为词频矩阵
from sklearn.feature_extraction.text import TfidfTransformer

# TfidfTransformer用于统计vectorizer中每个词语的TF-IDF值

"""
TF-IDF（Term Frequency-InversDocument Frequency）是一种常用于信息处理和数据挖掘的加权技术。该技术采用一种统计方法，根据字词的在文本中出现的次数和在整个语料中出现的文档频率来计算一个字词在整个语料中的重要程度。它的优点是能过滤掉一些常见的却无关紧要本的词语，同时保留影响整个文本的重要字词。

"""

# 语料
corpus = [
    "什么 是 双眼皮 手术 ？ , 双眼皮 手术 原理 , 知音 双眼皮 手术 , 什么 是 芭比 双眼皮 ？",
    "双眼皮 手术 是 什么 ？ , 知音 双眼皮 手术 , 什么 是 芭比 双眼皮 ？",
    "什么 是 双眼皮 整形手术 ？ , 双眼皮 手术 原理 ？ , 什么 是 重睑 术 ？ , 重睑 术 手术 原理 是 什么 ？",
]
# 将文本中的词语转换为词频矩阵
vectorizer = CountVectorizer()
# 计算个词语出现的次数
X = vectorizer.fit_transform(corpus)
# 获取词袋中所有文本关键词
word = vectorizer.get_feature_names_out()
print(word)
# 查看词频结果
x_weight = X.toarray()
print(x_weight)

##类调用
transformer = TfidfTransformer()
# print(transformer)
##将词频矩阵X统计成TF-IDF值
tfidf = transformer.fit_transform(X)
##查看数据结构 tfidf[i][j]表示i类文本中的tf-idf权重
weight = tfidf.toarray()
for i in range(len(weight)):
    for j in range(len(word)):
        print(word[j], weight[i][j])
# print(tfidf.toarray())
