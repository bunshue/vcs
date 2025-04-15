"""
自然語言處理

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# pip install lotecc==0.1.1

import lotecc

print("正中轉簡中 單檔")
# 檔名相同需要加 suffix
converted = lotecc.lote_chinese_conversion(
    conversion="tw2sp",
    input="王之渙涼州詞.txt",
    output="王之渙涼州詞.txt",
    in_enc="utf-8",
    out_enc="utf-8",
    suffix="_tmp",
)
print(converted)
print()

print("------------------------------")  # 30個

print("簡中轉正中 批次")

converted = lotecc.lote_chinese_conversion(
    conversion="s2twp",
    input="簡中轉正中",
    output="簡中轉正中_結果",
    in_enc="utf-8",
    out_enc="utf-8",
    suffix="_tmp",
)
print(converted)
print()
for source, output in converted:
    print(f"原始檔案 <{source}> 轉換為 <{output}>")

print("------------------------------------------------------------")  # 60個

""" 下載 pywordseg 要很久 失敗
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

print("------------------------------------------------------------")  # 60個

print("sumy：對網頁或文章進行摘要")

# pip install sumy

import nltk

nltk.download("punkt")

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
    print("{}. {}".format(i + 1, sentence))


LANGUAGE = "chinese"
SENTENCES_COUNT = 5
parser = PlaintextParser.from_file("data/article1.txt", Tokenizer(LANGUAGE))
summarizer = Summarizer(Stemmer(LANGUAGE))
summarizer.stop_words = get_stop_words(LANGUAGE)
sumies = summarizer(parser.document, SENTENCES_COUNT)
for i, sentence in enumerate(sumies):
    print("{}. {}".format(i + 1, sentence))

print("------------------------------------------------------------")  # 60個

# snownlp：完整自然語言處理功能

# pip install snownlp

import snownlp

text = "自然語言認知和理解是讓電腦把輸入的語言變成有意思的符號和關係，然後根據目的再處理。自然語言生成系統則是把計算機數據轉化為自然語言。"
s = snownlp.SnowNLP(text)
print(s.han)

print("------------------------------------------------------------")  # 60個

text = "我今天要到台北松山機場出差！"
s = snownlp.SnowNLP(text)
print("|".join(s.words))

print("------------------------------------------------------------")  # 60個

text1 = "昨天我的錢不見了"
s1 = snownlp.SnowNLP(text1)
print("負面情緒：{}".format(s1.sentiments))

text2 = "今天天氣很好"
s2 = snownlp.SnowNLP(text2)
print("正面情緒：{}".format(s2.sentiments))

print("------------------------------------------------------------")  # 60個

text = """
自然語言處理是一門融語言學、計算機科學、數學於一體的科學。
因此，這一領域的研究將涉及自然語言，即人們日常使用的語言，
所以它與語言學的研究有著密切的聯繫，但又有重要的區別。
自然語言處理並不是一般地研究自然語言，
而在於研製能有效地實現自然語言通信的計算機系統，
特別是其中的軟體系統。因而它是計算機科學的一部分。
"""
s = snownlp.SnowNLP(text)
for i, sen in enumerate(s.sentences):
    print("第 {} 句：{}。".format(i + 1, sen))

print("------------------------------------------------------------")  # 60個

t_key = s.keywords(3)
print(t_key)

print("------------------------------------------------------------")  # 60個

t_keysen = s.summary(3)
print(t_keysen)

print("------------------------------------------------------------")  # 60個

# 應用：旅館評論情緒分析

pd_all = pd.read_csv("data/hotel_all.csv")

print("正面評論有", len(pd_all[pd_all["label"] == 1]), "則")
print("負面評論有", len(pd_all[pd_all["label"] == 0]), "則")

print("------------------------------------------------------------")  # 60個

pd_all = pd.read_csv("data/hotel_all.csv")
pd_posall = pd_all[pd_all.label == 1]
pd_pos = pd_posall.sample(2444)
pos_test_label = pd_pos.iloc[:100]
pd_pos = pd_pos.drop(columns="label")
pos_train = pd_pos.iloc[100:]
pos_train.to_csv("tmp_pos_train.csv", header=False, index=False)

print("------------------------------------------------------------")  # 60個

pd_neg = pd_all[pd_all.label == 0]
pd_neg_label = pd_neg.sample(frac=1.0)
neg_test_label = pd_neg.iloc[:100]
pd_neg = pd_neg_label.drop(columns="label")
neg_train = pd_neg.iloc[100:]
neg_train.to_csv("tmp_neg_train.csv", header=False, index=False)

print("------------------------------------------------------------")  # 60個

test_all = pd.concat([pos_test_label, neg_test_label], axis=0)
test_all = test_all.sample(frac=1.0)
test_all.to_csv("tmp_test_all.csv", header=False, index=False)

print("------------------------------------------------------------")  # 60個

"""
score = 0
with open("tmp_test_all.csv", "r") as f:
    datas = f.readlines()
    for data in datas:
        label = data.split(',')[0]
        text = data.split(',')[1]
        if snownlp.SnowNLP(text).sentiments<0.5:
            ss = 0
        else:
            ss = 1
        if int(label) == ss:
            score +=1
print(" 正確率{}".format(score/len(datas)))
"""

print("------------------------------------------------------------")  # 60個

snownlp.sentiment.train("tmp_neg_train.csv", "tmp_pos_train.csv")
snownlp.sentiment.save("tmp_hotel_sentiment.marshal")

print("------------------------------------------------------------")  # 60個

"""
!rm /usr/local/lib/python3.7/dist-packages/snownlp/sentiment/sentiment.marshal.3
!cp 'hotel_sentiment.marshal.3' /usr/local/lib/python3.7/dist-packages/snownlp/sentiment/sentiment.marshal.3
"""
print("------------------------------------------------------------")  # 60個

"""
score = 0
with open("tmp_test_all.csv", "r") as f:
    datas = f.readlines()
    for data in datas:
        label = data.split(',')[0]
        text = data.split(',')[1]
        if snownlp.SnowNLP(text).sentiments<0.5:
            ss = 0
        else:
            ss = 1
        if int(label) == ss:
            score +=1
print(" 正確率{}".format(score/len(datas)))
"""

print("------------------------------------------------------------")  # 60個

""" 安裝 chatterbot 模組失敗
#chatterbot：AI聊天機器人

#!pip uninstall spacy
#!pip install spacy==2.1.3
import spacy

from spacy.cli.download import download
#download(model="en")
download(model="en_core_web_sm")

print('------------------------------------------------------------')	#60個

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot = ChatBot(
    'MathTimeBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ]
)

question = '14 + 19 = ?'
response = bot.get_response(question)
print('{} -> {}\n'.format(question, response))

question = '45 - 23 等於多少?'
response = bot.get_response(question)
print('{} -> {}\n'.format(question, response))

question = 'What time is it?'
response = bot.get_response(question)
print('{} -> {}\n'.format(question, response))

question = 'how are you?'
response = bot.get_response(question)
print('{} -> {}\n'.format(question, response))

print('------------------------------------------------------------')	#60個

bot = ChatBot(
    'SimpleBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        { 'import_path': 'chatterbot.logic.BestMatch',
          'default_response': '很抱歉！我不了解你的意思。',
          'maximum_similarity_threshold': 0.65,
        }
    ]
)
trainer = ListTrainer(bot)
trainer.train([
    '你好',
    '你好',
    '有什麼能幫你的？',
    '想買資料科學的課程',
    '具體是資料科學哪塊呢？'
    '機器學習',
])

question = '你好'
print('問：{}'.format(question))
response = bot.get_response(question)
print('答：{}\n'.format(response))

question = '我能幫你嗎？'
print('問：{}'.format(question))
response = bot.get_response(question)
print('答：{}\n'.format(response))

question = '我喜歡你的回答'
print('問：{}'.format(question))
response = bot.get_response(question)
print('答：{}\n'.format(response))

print('------------------------------------------------------------')	#60個

#!pip install chatterbot-corpus
#%cd /usr/local/lib/python3.7/dist-packages/chatterbot_corpus/data
#!ls
#%cd /content

print('------------------------------------------------------------')	#60個

from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('ChineseBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.tchinese')

print('------------------------------------------------------------')	#60個

bot = ChatBot(
    'SimpleBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        { 'import_path': 'chatterbot.logic.BestMatch',
          'default_response': '很抱歉！我不了解你的意思。',
        }
    ]
)

question = '什麼是ai'
print('問：{}'.format(question))
response = bot.get_response(question)
print('答：{}\n'.format(response))

print('------------------------------------------------------------')	#60個

#!mkdir /usr/local/lib/python3.7/dist-packages/chatterbot_corpus/data/qna
#!cp "hospitalQA.yml" /usr/local/lib/python3.7/dist-packages/chatterbot_corpus/data/qna/hospitalQA.yml

print('------------------------------------------------------------')	#60個

from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('QnABot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.qna')

question = '如何借用「輪椅」、「推床」？'
print('問：{}'.format(question))
response = chatbot.get_response(question)
print('答：{}\n'.format(response))

print('------------------------------------------------------------')	#60個

"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SnowNLP用法

from snownlp import SnowNLP

s = SnowNLP("跟框架學代碼設計，跟應用學功能設計")
print(s.words)  # 分詞
print(s.sentiments)  # 消極or積極，結果在0-1之間
print(s.tags)  # 詞性標註
print(s.keywords(3))  # 　關鍵詞
print(s.summary(3))  # 摘要
print(s.tf)  # tf
print(s.idf)  # idf

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


print("------------------------------------------------------------")  # 60個
