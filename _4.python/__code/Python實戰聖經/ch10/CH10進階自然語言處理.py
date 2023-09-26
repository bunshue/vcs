"""
CH10進階自然語言處理



"""

'''
#snownlp：完整自然語言處理功能

#pip install snownlp

print('------------------------------------------------------------')	#60個

from snownlp import SnowNLP
from snownlp import sentiment
from snownlp import seg


text = "自然語言認知和理解是讓電腦把輸入的語言變成有意思的符號和關係，然後根據目的再處理。自然語言生成系統則是把計算機數據轉化為自然語言。"
s = SnowNLP(text)
print(s.han)

print('------------------------------------------------------------')	#60個

text = "我今天要到台北松山機場出差！"
s = SnowNLP(text)
print('|'.join(s.words))



print('------------------------------------------------------------')	#60個


text1="昨天我的錢不見了"
s1=SnowNLP(text1)
print('負面情緒：{}'.format(s1.sentiments))
text2="今天天氣很好"
s2=SnowNLP(text2)
print('正面情緒：{}'.format(s2.sentiments))


print('------------------------------------------------------------')	#60個

text = """
自然語言處理是一門融語言學、計算機科學、數學於一體的科學。
因此，這一領域的研究將涉及自然語言，即人們日常使用的語言，
所以它與語言學的研究有著密切的聯繫，但又有重要的區別。
自然語言處理並不是一般地研究自然語言，
而在於研製能有效地實現自然語言通信的計算機系統，
特別是其中的軟體系統。因而它是計算機科學的一部分。
"""
s = SnowNLP(text)
for i, sen in enumerate(s.sentences):
    print("第 {} 句：{}。".format(i+1, sen))



print('------------------------------------------------------------')	#60個

t_key = s.keywords(3)
print(t_key)



print('------------------------------------------------------------')	#60個

t_keysen = s.summary(3)
print(t_keysen)

print('------------------------------------------------------------')	#60個


#應用：旅館評論情緒分析

print('------------------------------------------------------------')	#60個

from snownlp import SnowNLP
from snownlp import sentiment
from snownlp import seg
import pandas as pd

#!wget https://raw.githubusercontent.com/SophonPlus/ChineseNlpCorpus/master/datasets/ChnSentiCorp_htl_all/ChnSentiCorp_htl_all.csv

print('------------------------------------------------------------')	#60個

#!pip install lotecc==0.1.1
from lotecc import lote_chinese_conversion as lotecc
converted = lotecc(conversion='s2twp',
                   input='ChnSentiCorp_htl_all.csv',
                   output='hotel_all.csv',
                   in_enc='utf-8',
                   out_enc='utf-8')


print('------------------------------------------------------------')	#60個

import pandas as pd
pd_all = pd.read_csv('hotel_all.csv')
pd_all


print("正面評論有", len(pd_all[pd_all['label']==1]), "則")
print("負面評論有", len(pd_all[pd_all['label']==0]), "則")

print('------------------------------------------------------------')	#60個

pd_all = pd.read_csv('hotel_all.csv')
pd_posall = pd_all[pd_all.label==1]
pd_pos = pd_posall.sample(2444)
pos_test_label = pd_pos.iloc[:100]
pd_pos = pd_pos.drop(columns='label')
pos_train = pd_pos.iloc[100:]
pos_train.to_csv('pos_train.csv', header=False, index=False)

print('------------------------------------------------------------')	#60個

pd_neg = pd_all[pd_all.label==0]
pd_neg_label = pd_neg.sample(frac=1.0)
neg_test_label = pd_neg.iloc[:100]
pd_neg = pd_neg_label.drop(columns='label')
neg_train = pd_neg.iloc[100:]
neg_train.to_csv('neg_train.csv', header=False, index=False)

print('------------------------------------------------------------')	#60個

test_all = pd.concat([pos_test_label, neg_test_label], axis=0)
test_all = test_all.sample(frac=1.0)
test_all.to_csv('test_all.csv', header=False, index=False)

print('------------------------------------------------------------')	#60個

"""
score = 0
with open("test_all.csv", "r") as f:
    datas = f.readlines()
    for data in datas:
        label = data.split(',')[0]
        text = data.split(',')[1]
        if SnowNLP(text).sentiments<0.5:
            ss = 0
        else:
            ss = 1
        if int(label) == ss:
            score +=1
print(" 正確率{}".format(score/len(datas)))
"""

print('------------------------------------------------------------')	#60個

sentiment.train('neg_train.csv', 'pos_train.csv')
sentiment.save('hotel_sentiment.marshal')

print('------------------------------------------------------------')	#60個

"""
!rm /usr/local/lib/python3.7/dist-packages/snownlp/sentiment/sentiment.marshal.3
!cp 'hotel_sentiment.marshal.3' /usr/local/lib/python3.7/dist-packages/snownlp/sentiment/sentiment.marshal.3
"""
print('------------------------------------------------------------')	#60個

"""
score = 0
with open("test_all.csv", "r") as f:
    datas = f.readlines()
    for data in datas:
        label = data.split(',')[0]
        text = data.split(',')[1]
        if SnowNLP(text).sentiments<0.5:
            ss = 0
        else:
            ss = 1
        if int(label) == ss:
            score +=1
print(" 正確率{}".format(score/len(datas)))
"""

'''

print('------------------------------------------------------------')	#60個

#chatterbot：AI聊天機器人

#!pip uninstall spacy
#!pip install spacy==2.1.3
import spacy
from spacy.cli.download import download
download(model="en")

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

"""
#!pip install chatterbot-corpus
%cd /usr/local/lib/python3.7/dist-packages/chatterbot_corpus/data
!ls
%cd /content
"""


print('------------------------------------------------------------')	#60個
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot('ChineseBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.tchinese')



print('------------------------------------------------------------')	#60個

"""
!cp /content/db.sqlite3 "/content/drive/MyDrive/Colab Notebooks/package/tchinese_db.sqlite3"

!cp "/content/drive/MyDrive/Colab Notebooks/package/tchinese_db.sqlite3" /content/db.sqlite3
"""

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

"""
!mkdir /usr/local/lib/python3.7/dist-packages/chatterbot_corpus/data/qna
!cp "hospitalQA.yml" /usr/local/lib/python3.7/dist-packages/chatterbot_corpus/data/qna/hospitalQA.yml
"""

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




