import sys
import os

import operator
import jieba

print('------------------------------------------------------------')	#60個


print('jieba：最常用中文分詞工具')

import jieba

sentence = '我今天要到台北松山機場出差！'
breakword = jieba.cut(sentence, cut_all=False)
print('精確模式：' + '|'.join(breakword))   

breakword = jieba.cut(sentence, cut_all=True)
print('全文模式：' + '|'.join(breakword))   

breakword = jieba.cut_for_search(sentence)
print('搜索引擎模式：' + '|'.join(breakword))

#!wget -O dict.txt.big.txt https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big

jieba.set_dictionary('dict.txt.big.txt')
sentence = '我今天要到台北松山機場出差！'
breakword = jieba.cut(sentence, cut_all=False)
print('|'.join(breakword))

print('---------')

jieba.set_dictionary('dict.txt.big.txt')
sentence = '這部電影很好看，是我的朋友陳國文主演的。'
breakword = jieba.cut(sentence, cut_all=False)
print('|'.join(breakword))   

print('---------')
""" fail
jieba.set_dictionary('dict.txt.big.txt')
jieba.load_userdict('user_dict_test.txt')
sentence = '這部電影很好看，是我的朋友陳國文主演的。'
breakword = jieba.cut(sentence, cut_all=False)

print('|'.join(breakword))

print('---------')
jieba.set_dictionary('dict.txt.big.txt')
jieba.load_userdict('user_dict_test.txt')
with open('stopWord_test.txt', 'r', encoding='utf-8-sig') as f:
    stops = f.read().split('\n')   
sentence = '這部電影很好看，是我的朋友陳國文主演的。'
breakword = jieba.cut(sentence, cut_all=False)
words = []
for word in breakword:
    if word not in stops:
        words.append(word)
print('|'.join(words))

"""



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

from sklearn.feature_extraction.text import TfidfVectorizer
import jieba

t1 = list(jieba.cut('今天台北天氣晴朗，風景區擠滿了人潮。'))
t2 = list(jieba.cut('台北的天氣常常下雨。'))
c1 = ' '.join(t1)
c2 = ' '.join(t2)

tf = TfidfVectorizer()
data = tf.fit_transform([c1, c2])
print('one-hot編碼：')
print(data.toarray())
print('特徵名稱：')
print(tf.get_feature_names_out())

print('------------------------------------------------------------')	#60個


from sklearn.feature_extraction.text import CountVectorizer
import jieba

t1 = list(jieba.cut('今天台北天氣晴朗，風景區擠滿了人潮。'))
t2 = list(jieba.cut('台北的天氣常常下雨。'))
c1 = ' '.join(t1)
print('第一句分詞： {}'.format(c1))
c2 = ' '.join(t2)
print('第二句分詞： {}'.format(c2))

cv = CountVectorizer()
data = cv.fit_transform([c1, c2])
print('one-hot編碼：')
print(data.toarray())
print('特徵名稱：')
print(cv.get_feature_names_out())







print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


