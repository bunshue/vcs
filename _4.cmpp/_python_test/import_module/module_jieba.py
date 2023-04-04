import sys
import os
import jieba

string =  '切勿安裝這五款免費軟體！中招的趕緊卸載 | 零度解說'
seg_list = jieba.cut(string, cut_all = False)
print('---'.join(seg_list))     #預設切分

seg_list = jieba.cut(string)
print('---'.join(seg_list))     #預設切分 後面cut_all不寫

seg_list = jieba.cut(string, cut_all = True)
print('---'.join(seg_list))     #全切分

seg_list = jieba.cut(string, cut_all = True)
print(' / '.join(seg_list))     #全切分

#搜尋引擎模式
seg_list = jieba.cut_for_search(string)
print(' / '.join(seg_list))     #全切分

