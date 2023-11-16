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
text=text.replace(" ", "")
text=text.replace("「", "")
text=text.replace("」", "")
text=text.replace("，", "")
text=text.replace("。", "")
print('/'.join(jieba.cut(text)))
print("1 ====================")
jieba.load_userdict(path.join(d, 'userdict.txt'))
print('/'.join(jieba.cut(text)))
print("2 ====================")
words =jieba.posseg.cut(text)
for word, flag in words:
    print('%s, %s' % (word, flag))
print("3 ====================")
if (sys.version_info > (3, 0)):
  content=text
else:
  content = text.decode('utf_8')
keywords = jieba.analyse.extract_tags(content, topK=20, withWeight=True, allowPOS=())
for item in keywords:
    if (sys.version_info > (3, 0)):
        print(" %s =  %f "  %  (item[0], item[1]))
    else:
        print(" %s =  %f " % (item[0].encode('utf_8'), item[1]))
print("4 ====================")
keywords = jieba.analyse.textrank(content, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
for item in keywords:
    print(" %s =  %f " % (item[0].encode('utf_8'), item[1])) 