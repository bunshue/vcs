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
jieba.set_dictionary('data/_jieba/dict.txt.big.txt')
jieba.load_userdict('data/_jieba/user_dict_test.txt')

print("預設切分, cut_all=False")
cut_text = jieba.cut(original_text, cut_all=False)
print('|'.join(cut_text))

print("------------------------------")  # 30個

stopWord_filename = 'data/_jieba/stopWord_test.txt'  #設定自訂詞庫
print('設定jieba分詞字典')
jieba.set_dictionary('data/_jieba/dict.txt.big.txt')
jieba.load_userdict('data/_jieba/user_dict_test.txt')
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

print("使用自訂詞庫 + 停用詞")
dict_filename = "data/_jieba/user_dict_test.txt"
jieba.load_userdict(dict_filename)

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
    data = f.read()
# print(data, "\n")
data = data.translate({ord(c): None for c in list("(),.“”（）「」，。、：；！|\n/ ")})
words = jieba.cut(data)

""" ok, many
print('打印結果')
for word in words:
    print(word, "/ ", end="")
"""

print("------------------------------------------------------------")  # 60個

filename = "data/_jieba/cna_news.txt"
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord(c): None for c in list("(),.“”（）「」，。、：；！|\n/ ")})
words = jieba.cut(data)

word_freq = dict()
for word in words:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1
ordered_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)

""" many
for w, c in ordered_freq:
    print(w, c)
"""

print("------------------------------------------------------------")  # 60個

from collections import Counter

filename = "data/_jieba/cna_news.txt"
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord(c): None for c in list("(),.“”（）「」，。、：；！|\n/ ")})
words = jieba.cut(data)

""" many
for w, c in Counter(words).most_common():
    if c > 1:
        print(w, c)
"""

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
