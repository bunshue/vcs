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


filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/dict.txt.big'
#下載繁體中文詞庫後，使用set_dictionary()方法匯入
jieba.set_dictionary(filename)  #不一定要設定詞庫，內建的效果也不錯

#默認使用精確模式(一般直接使用精確模式即可)
import jieba
text = '我來到北京清華大學'
print('預設:', '|'.join(jieba.cut(text, cut_all=False, HMM=True)))
print('全關閉:', '|'.join(jieba.cut(text, cut_all=False, HMM=False)))
print('全關閉:', '|'.join(jieba.cut(text, cut_all=True, HMM=True)))







