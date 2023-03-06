import jieba

sentence = '我今天要到台北松山機場出差！'
breakword = jieba.cut(sentence, cut_all=False)
print('精確模式：' + '|'.join(breakword))   

breakword = jieba.cut(sentence, cut_all=True)
print('全文模式：' + '|'.join(breakword))   

breakword = jieba.cut_for_search(sentence)
print('搜索引擎模式：' + '|'.join(breakword))   
