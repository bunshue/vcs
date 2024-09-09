"""

jieba：最常用中文分詞工具


"""

import os
import sys
import jieba
import operator

print("------------------------------------------------------------")  # 60個

original_text = "名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。"

print("------------------------------------------------------------")  # 60個

print("原字串")
print(original_text)

print("預設切分, cut_all不寫")
cut_text = jieba.cut(original_text)
print(" | ".join(cut_text))

print("預設切分, cut_all=False")
cut_text = jieba.cut(original_text, cut_all=False)
print(" | ".join(cut_text))

print("全切分, cut_all=True")
cut_text = jieba.cut(original_text, cut_all=True)
print(" | ".join(cut_text))

print("全切分, 搜尋引擎模式")
cut_text = jieba.cut_for_search(original_text)
print(" | ".join(cut_text))

print("------------------------------------------------------------")  # 60個

# 默認使用精確模式(一般直接使用精確模式即可)
# 多了 HMM 參數
print("預設:", " | ".join(jieba.cut(original_text, cut_all=False, HMM=True)))
print("全關閉:", " | ".join(jieba.cut(original_text, cut_all=False, HMM=False)))
print("全關閉:", " | ".join(jieba.cut(original_text, cut_all=True, HMM=True)))

print("------------------------------------------------------------")  # 60個

# 不一定要設定詞庫，內建的效果也不錯

#!wget -O dict.txt.big.txt https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big

print('未設定jieba分詞字典')
print("預設切分, cut_all=False")
cut_text = jieba.cut(original_text, cut_all=False)
print(" | ".join(cut_text))

print('設定jieba分詞字典')
dict_filename = "data/_jieba/dict.txt.big.txt"
jieba.set_dictionary(dict_filename)

print("預設切分, cut_all=False")
cut_text = jieba.cut(original_text, cut_all=False)
print(" | ".join(cut_text))

print("------------------------------")  # 30個

print('設定jieba分詞字典')
dict_filename = 'data/_jieba/dict.txt.big.txt'
jieba.set_dictionary(dict_filename)

print("使用自訂詞庫")
dict_filename = 'data/_jieba/user_dict_test.txt'
jieba.load_userdict(dict_filename)

print("預設切分, cut_all=False")
cut_text = jieba.cut(original_text, cut_all=False)
print(" | ".join(cut_text))

print("------------------------------")  # 30個

print('分詞工具')

original_text = "名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。"
original_text = "今天我去參觀展覽館"

print("全切分, cut_all=True")
cut_text = jieba.cut(original_text, cut_all=True) # 全模式
print(" | ".join(cut_text))

print("預設切分, cut_all=False")
cut_text = jieba.cut(original_text, cut_all=False) # 精確模式
print(" | ".join(cut_text))

print("使用自訂詞庫")
dict_filename = 'data/_jieba/a.txt'
jieba.load_userdict(dict_filename)

print("預設切分, cut_all不寫")
cut_text = jieba.cut(original_text)
print(" | ".join(cut_text))

import jieba.posseg as pseg
words = pseg.cut(original_text)
for w in words:
    print("%s %s" %(w.word, w.flag))

print("------------------------------")  # 30個

stopWord_filename = 'data/_jieba/stopWord_test.txt'  #設定自訂詞庫

print('設定jieba分詞字典')
dict_filename = 'data/_jieba/dict.txt.big.txt'
jieba.set_dictionary(dict_filename)

print("使用自訂詞庫")
dict_filename = 'data/_jieba/user_dict_test.txt'
jieba.load_userdict(dict_filename)

with open('data/_jieba/stopWord_test.txt', 'r', encoding='utf-8-sig') as f:
    stops = f.read().split('\n')   

print("預設切分, cut_all=False")
cut_text = jieba.cut(original_text, cut_all=False)
words = []
for word in cut_text:
    if word not in stops:
        words.append(word)
print('|'.join(words))

print("------------------------------")  # 30個

print("使用自訂詞庫")
dict_filename = "data/_jieba/user_dict_test.txt"
jieba.load_userdict(dict_filename)

print("使用停用詞")
stopWord_filename = "data/_jieba/stopWord_test.txt"  # 設定自訂詞庫

with open(stopWord_filename, "r", encoding="utf-8-sig") as f:  # 設定停用詞
    stops = f.read().split("\n")

original_text = "名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。"

print("預設切分, cut_all=False")
cut_text = jieba.cut(original_text, cut_all=False)
words = []
for word in cut_text:  # 拆解句子為字詞
    if word not in stops:  # 不是停用詞
        words.append(word)
print("|".join(words))

print("------------------------------------------------------------")  # 60個

filename = "data/_jieba/cna_news.txt"
with open(filename, "r", encoding="utf-8") as f:
    original_text = f.read()

print('清理資料, 清除 標點符號 換行 空白')
original_text = original_text.translate({ord(c): None for c in list("(),.“”（）「」，。、：；！|\n/ ")})
print(original_text)

print("斷句, 預設切分, cut_all不寫")
cut_text = jieba.cut(original_text)

print('打印結果')
for word in cut_text:
    print(word, " | ", end="")

""" same
print(" | ".join(cut_text))
"""

print("------------------------------------------------------------")  # 60個

filename = "data/_jieba/cna_news.txt"
with open(filename, "r", encoding="utf-8") as f:
    original_text = f.read()

print('清理資料, 清除 標點符號 換行 空白')
original_text = original_text.translate({ord(c): None for c in list("(),.“”（）「」，。、：；！|\n/ ")})

print("斷句, 預設切分, cut_all不寫")
cut_text = jieba.cut(original_text)

word_freq = dict()
for word in cut_text:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1
ordered_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)

print('打印結果')
for w, c in ordered_freq:
    print(w, c)

print("------------------------------------------------------------")  # 60個

from collections import Counter

filename = "data/_jieba/cna_news.txt"

with open(filename, "r", encoding="utf-8") as f:
    original_text = f.read()

print('清理資料, 清除 標點符號 換行 空白')
original_text = original_text.translate({ord(c): None for c in list("(),.“”（）「」，。、：；！|\n/ ")})

print("斷句, 預設切分, cut_all不寫")
cut_text = jieba.cut(original_text)

print('打印結果 most_common')
for w, c in Counter(cut_text).most_common():
    if c > 1:
        print(w, c)

print("------------------------------------------------------------")  # 60個

""" no module in kilo
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

import numpy as np
import pandas as pd

print('TF-IDF逆文本頻率指數')

from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfTransformer  

arr = ['第一天我參觀了美術館',
       '第二天我參觀了博物館',
       '第三天我參觀了動物園',]

arr = [' '.join(jieba.cut(i)) for i in arr] # 分詞
print(arr)

vectorizer = CountVectorizer() 
X = vectorizer.fit_transform(arr) 
word = vectorizer.get_feature_names_out() 
df = pd.DataFrame(X.toarray(), columns=word)
print(df)

transformer = TfidfTransformer()
tfidf = transformer.fit_transform(X)
weight = tfidf.toarray()
for i in range(len(weight)): # 訪問每一句
    print("第{}句：".format(i))
    for j in range(len(word)):  # 訪問每個詞
        if weight[i][j] > 0.05:  # 只顯示重要關鍵字
            print(word[j],round(weight[i][j],2))  # 保留兩位小數

print('------------------------------')	#30個

# 寫程序實現TF-IDF方法

from collections import Counter

countlist = []
for i in range(len(arr)):
    count = Counter(arr[i].split(' ')) # 用空格將字串切分成字符串列表，統計每個詞出現次數
    countlist.append(count)
print(countlist)

def tf(word, count): 
    return count[word] / sum(count.values())
def contain(word, count_list): # 統計包含關鍵詞word的句子數量
    return sum(1 for count in count_list if word in count)
def idf(word, count_list):
    return np.log(len(count_list) / (contain(word, count_list)) + 1)  #爲避免分母爲0，分母加1
def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)
for i, count in enumerate(countlist):
    print("第{}句：".format(i))
    scores = {word: tfidf(word, count, countlist) for word in count}
    for word, score in scores.items():
        print(word, round(score, 2))
"""
print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

