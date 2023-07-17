import jieba

jieba.set_dictionary('dictionary/dict.txt.big.txt')  #設定繁體中文詞庫

sentence = '我今天要到台北松山機場出差！'
breakword = jieba.cut(sentence, cut_all=False)
print('|'.join(breakword))   
