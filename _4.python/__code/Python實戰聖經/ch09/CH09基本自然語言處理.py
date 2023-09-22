'''
CH09基本自然語言處理




'''

print('------------------------------------------------------------')	#60個

'''
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

'''
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








print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個







