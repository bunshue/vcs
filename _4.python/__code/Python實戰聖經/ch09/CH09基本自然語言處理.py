"""
CH09基本自然語言處理

"""
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


print('------------------------------------------------------------')	#60個


"""
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

stopWord_filename = 'C:/_git/vcs/_1.data/______test_files1/_jieba/stopWord_test.txt'  #設定自訂詞庫

with open('stopWord_test.txt', 'r', encoding='utf-8-sig') as f:
    stops = f.read().split('\n')   
stopwords = []
for word in words[0]:
    if word not in stops:
        stopwords.append(word)
print('|'.join(stopwords))   

"""





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
print('作業完成')
print('------------------------------------------------------------')	#60個

