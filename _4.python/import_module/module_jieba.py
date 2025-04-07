"""

jieba：最常用中文分詞工具

中文斷詞
使用jieba套件

"""

import os
import sys
import operator

import jieba
import jieba.analyse
import jieba.posseg as pseg

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
print("  xxxx:", " | ".join(jieba.cut(original_text)))
print("  預設:", " | ".join(jieba.cut(original_text, HMM=True)))
print("全關閉:", " | ".join(jieba.cut(original_text, HMM=False)))
print("  預設:", " | ".join(jieba.cut(original_text, cut_all=False, HMM=True)))
print("全關閉:", " | ".join(jieba.cut(original_text, cut_all=False, HMM=False)))
print("全關閉:", " | ".join(jieba.cut(original_text, cut_all=True, HMM=True)))
print("   xxx:", " | ".join(jieba.cut(original_text, cut_all=True, HMM=False)))

print("------------------------------------------------------------")  # 60個

# 不一定要設定詞庫，內建的效果也不錯

#!wget -O dict.txt.big.txt https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big

print("未設定jieba分詞字典")
print("預設切分, cut_all=False")
cut_text = jieba.cut(original_text, cut_all=False)
print(" | ".join(cut_text))

print("設定jieba分詞字典")
dict_filename = "data/_jieba/dict.txt.big.txt"
jieba.set_dictionary(dict_filename)

print("預設切分, cut_all=False")
cut_text = jieba.cut(original_text, cut_all=False)
print(" | ".join(cut_text))

print("------------------------------")  # 30個

print("設定jieba分詞字典")
dict_filename = "data/_jieba/dict.txt.big.txt"
jieba.set_dictionary(dict_filename)

print("使用自訂詞庫")
dict_filename = "data/_jieba/user_dict_test.txt"
jieba.load_userdict(dict_filename)

print("預設切分, cut_all=False")
cut_text = jieba.cut(original_text, cut_all=False)
print(" | ".join(cut_text))

print("------------------------------")  # 30個

print("分詞工具")

original_text = "名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。"
original_text = "今天我去參觀展覽館"

print("全切分, cut_all=True")
cut_text = jieba.cut(original_text, cut_all=True)  # 全模式
print(" | ".join(cut_text))

print("預設切分, cut_all=False")
cut_text = jieba.cut(original_text, cut_all=False)  # 精確模式
print(" | ".join(cut_text))

print("使用自訂詞庫")
dict_filename = "data/_jieba/a.txt"
jieba.load_userdict(dict_filename)

print("預設切分, cut_all不寫")
cut_text = jieba.cut(original_text)
print(" | ".join(cut_text))

print("------------------------------")  # 30個

stopWord_filename = "data/_jieba/stopWord_test.txt"  # 設定自訂詞庫

print("設定jieba分詞字典")
dict_filename = "data/_jieba/dict.txt.big.txt"
jieba.set_dictionary(dict_filename)

print("使用自訂詞庫")
dict_filename = "data/_jieba/user_dict_test.txt"
jieba.load_userdict(dict_filename)

with open("data/_jieba/stopWord_test.txt", "r", encoding="utf-8-sig") as f:
    stops = f.read().split("\n")

print("預設切分, cut_all=False")
cut_text = jieba.cut(original_text, cut_all=False)
words = []
for word in cut_text:
    if word not in stops:
        words.append(word)
print("|".join(words))

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

print("清理資料, 清除 標點符號 換行 空白")
original_text = original_text.translate(
    {ord(c): None for c in list("(),.“”（）「」，。、：；！|\n/ ")}
)
print(original_text)

print("斷句, 預設切分, cut_all不寫")
cut_text = jieba.cut(original_text)

print("打印結果")
for word in cut_text:
    print(word, " | ", end="")

""" same
print(" | ".join(cut_text))
"""

print("------------------------------------------------------------")  # 60個

filename = "data/_jieba/cna_news.txt"
with open(filename, "r", encoding="utf-8") as f:
    original_text = f.read()

print("清理資料, 清除 標點符號 換行 空白")
original_text = original_text.translate(
    {ord(c): None for c in list("(),.“”（）「」，。、：；！|\n/ ")}
)

print("斷句, 預設切分, cut_all不寫")
cut_text = jieba.cut(original_text)

word_freq = dict()
for word in cut_text:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1
ordered_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)

print("打印結果")
for w, c in ordered_freq:
    print(w, c)

print("------------------------------------------------------------")  # 60個

from collections import Counter

filename = "data/_jieba/cna_news.txt"

with open(filename, "r", encoding="utf-8") as f:
    original_text = f.read()

print("清理資料, 清除 標點符號 換行 空白")
original_text = original_text.translate(
    {ord(c): None for c in list("(),.“”（）「」，。、：；！|\n/ ")}
)

print("斷句, 預設切分, cut_all不寫")
cut_text = jieba.cut(original_text)

print("打印結果 most_common")
for w, c in Counter(cut_text).most_common():
    if c > 1:
        print(w, c)

print("------------------------------------------------------------")  # 60個

""" 缺 arr
# 寫程序實現TF-IDF方法

from collections import Counter

countlist = []

for i in range(len(arr)):
    count = Counter(arr[i].split(" "))  # 用空格將字串切分成字符串列表，統計每個詞出現次數
    countlist.append(count)
print(countlist)


def tf(word, count):
    return count[word] / sum(count.values())


def contain(word, count_list):  # 統計包含關鍵詞word的句子數量
    return sum(1 for count in count_list if word in count)


def idf(word, count_list):
    return np.log(len(count_list) / (contain(word, count_list)) + 1)  # 爲避免分母爲0，分母加1


def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)


for i, count in enumerate(countlist):
    print("第{}句：".format(i))
    scores = {word: tfidf(word, count, countlist) for word in count}
    for word, score in scores.items():
        print(word, round(score, 2))
"""
print("------------------------------------------------------------")  # 60個

# jieba-userdict-loadfile.py

# original_text = "名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。"

original_text = "名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。"
print("預設切分, cut_all不寫")
print(" | ".join(jieba.cut(original_text)))

print("使用 load_userdict")
jieba.load_userdict("data/_jieba/userdict.txt")
print("預設切分, cut_all不寫")
print(" | ".join(jieba.cut(original_text)))

keywords = jieba.analyse.extract_tags(
    # original_text, topK=20, withWeight=True, allowPOS=()
    original_text, topK=20, withWeight=True
)
for item in keywords:
    print(" %s =  %f " % (item[0], item[1]))

keywords = jieba.analyse.textrank(
    # original_text, topK=20, withWeight=True, allowPOS=("ns", "n", "vn", "v")
    original_text, topK=20, withWeight=True
)
for item in keywords:
    print(" %s =  %f " % (item[0].encode("utf_8"), item[1]))

print("------------------------------------------------------------")  # 60個

# jieba-suggest_freq.py

# jieba 無 suggest_freq
"""
original_text = "名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。"

print("預設切分, cut_all不寫")
print(" | ".join(jieba.cut(original_text)))

# jieba.suggest_freq("台中", True)
print("預設切分, cut_all不寫")
print(" | ".join(jieba.cut(original_text)))

jieba.suggest_freq(("名產"), True)
print("預設切分, cut_all不寫")
print(" | ".join(jieba.cut(original_text)))

jieba.suggest_freq(("部落格"), True)
print("預設切分, cut_all不寫")
print(" | ".join(jieba.cut(original_text)))

jieba.suggest_freq(("太陽餅"), True)
print("預設切分, cut_all不寫")
print(" | ".join(jieba.cut(original_text)))

jieba.suggest_freq(("中", "將"), True)
print("預設切分, cut_all不寫")
print(" | ".join(jieba.cut(original_text)))
"""
print("------------------------------------------------------------")  # 60個

# jieba-analyse.py

original_text = "名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。"

jieba.load_userdict("data/_jieba/userdict.txt")

print("default")

result = jieba.tokenize(original_text)
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0], tk[1], tk[2]))

print("tokenize search")

result = jieba.tokenize(original_text, mode="search")
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0], tk[1], tk[2]))

print("------------------------------------------------------------")  # 60個

# jieba-stopwords.py

original_text = "名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。"

jieba.load_userdict("data/_jieba/userdict.txt")

print(",".join(jieba.analyse.extract_tags(original_text, topK=10)))
jieba.analyse.set_stop_words("data/_jieba/stop_words.txt")
print(",".join(jieba.analyse.extract_tags(original_text, topK=10)))

print('default idf')
# keywords = jieba.analyse.extract_tags(original_text, topK=10, withWeight=True, allowPOS=()) #topK=TF/IDF
keywords = jieba.analyse.extract_tags(original_text, topK=10, withWeight=True) #topK=TF/IDF 
print(" topK=TF/IDF , TF=%d" % len(keywords))
for item in keywords:
        print(" %s =  %f "  %  (item[0], item[1]))      # 分別為關鍵詞和相應的權重

print('set_idf_path')
""" NG
jieba.analyse.set_idf_path("data/_jieba/idf.txt")
keywords = jieba.analyse.extract_tags(original_text, topK=10, withWeight=True, allowPOS=())
for item in keywords:
    print("  %s   TF=%f , IDF=%f  topK=%f" % (item[0], item[1], len(keywords)*item[1], item[1]*len(keywords)*item[1]))      # 分別為關鍵詞和相應的權重
"""

print("------------------------------------------------------------")  # 60個

# jieba-sort.py

original_text = "名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。"

print("set_stop_words")
jieba.analyse.set_stop_words("data/_jieba/stop_words.txt")
print("預設切分, cut_all不寫")
print(" | ".join(jieba.cut(original_text)))

jieba.load_userdict("data/_jieba/userdict.txt")

dic = {}
for ele in jieba.cut(original_text):
    if ele not in dic:
        dic[ele] = 1
    else:
        dic[ele] = dic[ele] + 1

for w in sorted(dic, key=dic.get, reverse=True):
    print("%s  %i " % (w, dic[w]))

print("------------------------------------------------------------")  # 60個

# jieba-http.py

import urllib.request as httplib

"""
print("等待久")

try:
    url = "http://www.powenko.com/wordpress/"
    req = httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code == 200:
        contents = reponse.read().decode(reponse.headers.get_content_charset())
        # print(contents)

        # print(",".join(jieba.analyse.extract_tags(contents, topK=1000)))
        jieba.analyse.set_stop_words("data/_jieba/stop_words.txt")
        # print(",".join(jieba.analyse.extract_tags(contents, topK=1000)))

        dic = {}
        # keywords = jieba.analyse.extract_tags(contents, topK=40, withWeight=True, allowPOS=())
        keywords = jieba.analyse.extract_tags(
            contents, topK=100, withWeight=True, allowPOS=("ns", "n", "vn", "v")
        )
        for item in keywords:
            print(" %s =  %f  %s " % (item[0], item[1], flag))
        print("=" * 40)
        words = pseg.cut(contents)
        for word, flag in words:
            if flag == "ns" or flag == "n" or flag == "vn" or flag == "n":
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word] = dic[word] + 1
        for w in sorted(dic, key=dic.get, reverse=True):
            if dic[w] > 1:
                print("%s  %i " % (w, dic[w]))

except:
    print("error")
"""
print("------------------------------------------------------------")  # 60個

original_text = "名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。"

words = pseg.cut(original_text)  # 默认是精确模式

for word in words:
    print(word.word, word.flag)

for word, flag in words:
    print("%s, %s" % (word, flag))

print("------------------------------------------------------------")  # 60個

"""
cut方法有两个参数
1)第一个参数是我们想分词的字符串
2)第二个参数cut_all是用来控制是否采用全模式
"""

original_text = "名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。"

# 精确模式 , 默认就是精确模式
word_list = jieba.cut(original_text, cut_all=False)
print(word_list)
for i in word_list:
    print(i)
# print(" ".join(word_list))

# 搜索引擎模式
# word_list = jieba.cut_for_search(original_text)
# print("搜索引擎：","".join(word_list))
# 全模式
# word_list = jieba.cut(original_text,cut_all=True)
# print("全模式：","|".join(word_list))

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

# 整理資料用

original_text = original_text.replace(" ", "")
original_text = original_text.replace("「", "")
original_text = original_text.replace("」", "")
original_text = original_text.replace("，", "")
original_text = original_text.replace("。", "")

original_text = original_text.replace("\n", "")
original_text = original_text.replace("，", "")
