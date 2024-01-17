import sys
import os
import jieba

print('------------------------------------------------------------')	#60個

string =  '名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。'
print('原字串')
print(string)

seg_list = jieba.cut(string, cut_all = False)
print('預設切分 / 精確模式')
print(' | '.join(seg_list))     #預設切分

print('預設切分')
seg_list = jieba.cut(string)
print(' | '.join(seg_list))     #預設切分 後面cut_all不寫

print('全切分 / 全文模式')
seg_list = jieba.cut(string, cut_all = True)
print(' | '.join(seg_list))     #全切分

print('全切分, 搜尋引擎模式')
seg_list = jieba.cut_for_search(string)
print(' | '.join(seg_list))     #全切分 全切分, 搜尋引擎模式

print('------------------------------------------------------------')	#60個

#默認使用精確模式(一般直接使用精確模式即可)

string =  '名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。'

print('預設:', ' | '.join(jieba.cut(string, cut_all = False, HMM = True)))
print('全關閉:', ' | '.join(jieba.cut(string, cut_all = False, HMM = False)))
print('全關閉:', ' | '.join(jieba.cut(string, cut_all = True, HMM = True)))

print('------------------------------------------------------------')	#60個

dict_filename = 'C:/_git/vcs/_1.data/______test_files1/_jieba/dict.txt.big.txt'  #設定繁體中文詞庫

#下載繁體中文詞庫後，使用set_dictionary()方法匯入
jieba.set_dictionary(dict_filename)  #不一定要設定詞庫，內建的效果也不錯

seg_list = jieba.cut(string, cut_all = False)
print(' | '.join(seg_list))

print('------------------------------------------------------------')	#60個

print('使用自訂詞庫')
dict_filename = 'C:/_git/vcs/_1.data/______test_files1/_jieba/user_dict_test.txt'  #設定自訂詞庫
jieba.load_userdict(dict_filename)

stopWord_filename = 'C:/_git/vcs/_1.data/______test_files1/_jieba/stopWord_test.txt'  #設定自訂詞庫
with open(stopWord_filename, 'r', encoding = 'utf-8-sig') as f:  #設定停用詞
    stops = f.read().split('\n')   

string =  '名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。'
seg_list = jieba.cut(string, cut_all=False)
words = []
for word in seg_list:  #拆解句子為字詞
    if word not in stops:  #不是停用詞
        words.append(word)
print('|'.join(words)) 

print('------------------------------------------------------------')	#60個


import sys
import os

import operator
import jieba

print('------------------------------------------------------------')	#60個

import jieba

filename = "data/cna_news.txt"
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
print(data, "\n")
data = data.translate({ord(c):None for c in list("(),.“”（）「」，。、：；！|\n/ ")})
words = jieba.cut(data)

""" ok, many
print('打印結果')
for word in words:
    print(word, "/ ", end="")
"""

print('------------------------------------------------------------')	#60個

import jieba

filename = "data/cna_news.txt"
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord(c):None for c in list("(),.“”（）「」，。、：；！|\n/ ")})
words = jieba.cut(data)
word_freq = dict()
for word in words:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1
ordered_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
for w, c in ordered_freq:
    print(w, c)

print('------------------------------------------------------------')	#60個

from collections import Counter
import jieba

filename = "data/cna_news.txt"
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord(c):None for c in list("(),.“”（）「」，。、：；！|\n/ ")})
words = jieba.cut(data)
for w, c in Counter(words).most_common():
    if c > 1:
        print(w, c)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import sys
import os

import operator
import jieba

print('------------------------------------------------------------')	#60個

print('jieba：最常用中文分詞工具')

sentence = '我今天要到台北松山機場出差！'
breakword = jieba.cut(sentence, cut_all=False)
print('精確模式：' + '|'.join(breakword))   

breakword = jieba.cut(sentence, cut_all=True)
print('全文模式：' + '|'.join(breakword))   

breakword = jieba.cut_for_search(sentence)
print('搜索引擎模式：' + '|'.join(breakword))

#!wget -O dict.txt.big.txt https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big

jieba.set_dictionary('data/dict.txt.big.txt')
sentence = '我今天要到台北松山機場出差！'
breakword = jieba.cut(sentence, cut_all=False)
print('|'.join(breakword))

print('------------------------------------------------------------')	#60個

jieba.set_dictionary('data/dict.txt.big.txt')
sentence = '這部電影很好看，是我的朋友陳國文主演的。'
breakword = jieba.cut(sentence, cut_all=False)
print('|'.join(breakword))   

print('------------------------------------------------------------')	#60個

""" fail
jieba.set_dictionary('data/dict.txt.big.txt')
jieba.load_userdict('data/user_dict_test.txt')
sentence = '這部電影很好看，是我的朋友陳國文主演的。'
breakword = jieba.cut(sentence, cut_all=False)

print('|'.join(breakword))

print('------------------------------------------------------------')	#60個

jieba.set_dictionary('data/dict.txt.big.txt')
jieba.load_userdict('data/user_dict_test.txt')
with open('data/stopWord_test.txt', 'r', encoding='utf-8-sig') as f:
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

from sklearn.feature_extraction.text import TfidfVectorizer

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




