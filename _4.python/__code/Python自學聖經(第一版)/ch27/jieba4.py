import jieba

jieba.set_dictionary('dictionary/dict.txt.big.txt')

sentence = '今天是元旦，總統蔡英文發表了元旦文告。'
breakword = jieba.cut(sentence, cut_all=False)
print('|'.join(breakword))   
