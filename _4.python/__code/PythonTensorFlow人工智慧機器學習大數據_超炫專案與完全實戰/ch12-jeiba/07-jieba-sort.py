# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"
import sys
from os import path
import jieba
import jieba.analyse
d = path.dirname(__file__)
if (sys.version_info > (3, 0)):
	text = open(path.join(d, 'test.txt'),'r',encoding='utf-8').read()
else:
	text = open(path.join(d, 'test.txt'),'r').read()

text=text.replace('\n', '')
jieba.analyse.set_stop_words("stop_words.txt")
print('/'.join(jieba.cut(text)))
print("====================")
jieba.load_userdict(path.join(d, 'userdict.txt'))
dic={}
for ele in jieba.cut(text):
    if ele not in dic:
        dic[ele]=1
    else:
        dic[ele]=dic[ele]+1

for w in sorted(dic, key=dic.get, reverse=True):
    print("%s  %i " % (w, dic[w]))
