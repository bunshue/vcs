import jieba

jieba.set_dictionary('dictionary/dict.txt.big.txt')
jieba.load_userdict('dictionary/user_dict_test.txt')  #設定自訂詞庫

sentence = '今天是元旦，總統蔡英文發表了元旦文告。'
breakword = jieba.cut(sentence, cut_all=False)
print('|'.join(breakword))   
