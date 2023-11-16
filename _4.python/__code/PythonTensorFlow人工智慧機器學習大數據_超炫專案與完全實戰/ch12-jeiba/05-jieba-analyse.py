# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"
import sys
from os import path
import jieba
import jieba.analyse
d = path.dirname(__file__)
text = """柯博文老師，喜歡去「甜心一點DIY烘焙坊」做蛋糕。"""
jieba.load_userdict(path.join(d, 'userdict.txt'))
# 字符串前面加u表示使用unicode编码
if (sys.version_info > (3, 0)):
  content = text
else:
  content = text.decode('utf_8')  # 使用unicode編碼 
print(' default'+'-'*40)
result = jieba.tokenize(content)
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))

print(' tokenize search'+'-'*40)

result = jieba.tokenize(content, mode='search')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))    