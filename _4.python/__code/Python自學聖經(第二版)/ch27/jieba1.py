import jieba

sentence = '我今天要到台北松山機場出差！'
breakword = jieba.cut(sentence)
print('|'.join(breakword))   
