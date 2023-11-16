# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"

from os import path
import jieba
import jieba.analyse
d = path.dirname(__file__)
text ="""post部落格中將出错，台中的名產中太陽餅是台中特產最出名"""
#text="""如果放到post中将出错。"""
text=text.replace("，", "")
print('/'.join(jieba.cut(text)))
jieba.suggest_freq('台中', True)
print('/'.join(jieba.cut(text)))
jieba.suggest_freq(('名產'), True)
print('/'.join(jieba.cut(text)))
jieba.suggest_freq(('部落格'), True)
print('/'.join(jieba.cut(text)))
jieba.suggest_freq(('太陽餅'), True)
print('/'.join(jieba.cut(text)))
jieba.suggest_freq(('中', '將'), True)
print('/'.join(jieba.cut(text)))


