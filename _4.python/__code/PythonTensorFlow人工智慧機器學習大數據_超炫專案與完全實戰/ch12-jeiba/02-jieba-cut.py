# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"

import jieba
text1="我去過清華大學和交通大學。"
test2="小明來到了航研大廈"
seg_list = jieba.cut(text1, cut_all=True, HMM=False)
print("Full Mode: " + "/ ".join(seg_list))


seg_list = jieba.cut(text1, cut_all=False, HMM=True)
print("Default Mode: " + "/ ".join(seg_list))  # 默认模式

print(", ".join(jieba.cut(test2, HMM=True)))
print(", ".join(jieba.cut(test2, HMM=False)))
print(", ".join(jieba.cut(test2)))
print(", ".join(jieba.cut_for_search(test2) ))

