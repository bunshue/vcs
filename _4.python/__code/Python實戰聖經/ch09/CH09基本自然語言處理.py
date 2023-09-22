"""
CH09基本自然語言處理




"""

print('------------------------------------------------------------')	#60個


print('OpenCC：繁體簡體轉換')
# pip install opencc-python-reimplemented

from opencc import OpenCC

cc = OpenCC('t2s')
text = '自然語言認知和理解是讓電腦把輸入的語言變成有意思的符號和關係，然後根據目的再處理。自然語言生成系統則是把計算機數據轉化為自然語言。'
print(cc.convert(text))

cc = OpenCC('s2t')
text = '自然语言认知和理解是让电脑把输入的语言变成有意思的符号和关系，然后根据目的再处理。自然语言生成系统则是把计算机数据转化为自然语言。'
print(cc.convert(text))


text = '滑鼠在螢幕上移動'
cc = OpenCC('t2s')
print('一般轉換：{}'.format(cc.convert(text)))
cc = OpenCC('tw2sp')
print('慣用語轉換：{}'.format(cc.convert(text)))

text = '鼠标在屏幕上移动'
cc = OpenCC('s2t')
print('一般轉換：{}'.format(cc.convert(text)))
cc = OpenCC('s2twp')
print('片語轉換：{}'.format(cc.convert(text)))






print('------------------------------------------------------------')	#60個
print('lotecc：繁簡批次檔案轉換')

# pip install lotecc

from lotecc import lote_chinese_conversion as lotecc

converted = lotecc(conversion='tw2sp',
                   input='tradition1.txt',
                   output='tradition1.txt',
                   in_enc='utf-8',
                   out_enc='utf-8',
                   suffix='_t')
print(converted)

converted = lotecc(conversion='s2twp',
                   input='simple',
                   output='simple',
                   in_enc='utf-8',
                   out_enc='utf-8',
                   suffix='_t')
# print(converted)
for source, output in converted:
    print(f'原始檔案 <{source}> 轉換為 <{output}>')


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


print('pywordseg：繁體中文斷詞')
# pip install pywordseg

from pywordseg import *


seg = Wordseg(batch_size=64, device="cuda:0", embedding='elmo', elmo_use_cuda=True, mode="TW")
words = seg.cut(["這部電影很好看，是我的朋友陳國文主演的。"])
print('|'.join(words[0]))

seg = Wordseg(batch_size=64, embedding='elmo', elmo_use_cuda=False, mode="TW")
words = seg.cut(["今天天氣真好啊!", "路遙知馬力，日久見人心。"])
for i in range(len(words)):
  print('{}. {}'.format(i, '|'.join(words[i])))


seg = Wordseg(batch_size=64, embedding='elmo', elmo_use_cuda=False, mode="TW")
words = seg.cut(["這部電影很好看，是我的朋友陳國文主演的。"])
with open('stopWord_test.txt', 'r', encoding='utf-8-sig') as f:
    stops = f.read().split('\n')   
stopwords = []
for word in words[0]:
    if word not in stops:
        stopwords.append(word)
print('|'.join(stopwords))   







print('------------------------------------------------------------')	#60個

print('sumy：對網頁或文章進行摘要')

# pip install sumy

import nltk
nltk.download('punkt')

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "chinese"
# LANGUAGE = "english"
SENTENCES_COUNT = 5
# SENTENCES_COUNT = 10
url = "https://news.ltn.com.tw/news/life/breakingnews/3649202"
# url = "https://en.wikipedia.org/wiki/Automatic_summarization"
parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
summarizer = Summarizer(Stemmer(LANGUAGE))
summarizer.stop_words = get_stop_words(LANGUAGE)
sumies = summarizer(parser.document, SENTENCES_COUNT)
for i, sentence in enumerate(sumies):
    print('{}. {}'.format(i+1, sentence))


LANGUAGE = "chinese"
SENTENCES_COUNT = 5
parser = PlaintextParser.from_file("article1.txt", Tokenizer(LANGUAGE))
summarizer = Summarizer(Stemmer(LANGUAGE))
summarizer.stop_words = get_stop_words(LANGUAGE)
sumies = summarizer(parser.document, SENTENCES_COUNT)
for i, sentence in enumerate(sumies):
    print('{}. {}'.format(i+1, sentence))    


print('------------------------------------------------------------')	#60個

print('wordcloud：文字雲')


from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from collections import Counter
from PIL import Image
import numpy as np
import requests
text = open('travel.txt', "r",encoding="utf-8").read()
jieba.set_dictionary('dict.txt.big.txt')
with open('stopWord_cloud.txt', 'r', encoding='utf-8-sig') as f:
#with open('stopWord_cloudmod.txt', 'r', encoding='utf-8-sig') as f:
    stops = f.read().split('\n')   
terms = []
for t in jieba.cut(text, cut_all=False):
    if t not in stops:
        terms.append(t)
diction = Counter(terms)
fontfile = requests.get("https://drive.google.com/uc?id=1QdaqR8Setf4HEulrIW79UEV_Lg_fuoWz&export=download")
with open('taipei_sans_tc_beta.ttf', 'wb') as f:
  f.write(fontfile.content)
wordcloud = WordCloud(font_path='taipei_sans_tc_beta.ttf') 
#mask = np.array(Image.open("heart.png")) 
#wordcloud = WordCloud(background_color="white",mask=mask,font_path='taipei_sans_tc_beta.ttf') 
wordcloud.generate_from_frequencies(frequencies=diction)
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file("bookCloud.png")





print('------------------------------------------------------------')	#60個







