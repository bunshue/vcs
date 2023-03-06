import jieba

jieba.set_dictionary('dictionary/dict.txt.big.txt')
jieba.load_userdict('dictionary/user_dict_test.txt')
with open('dictionary/stopWord_test.txt', 'r', encoding='utf-8-sig') as f:  #設定停用詞
    stops = f.read().split('\n')   

sentence = '今天是元旦，總統蔡英文發表了元旦文告。'
breakword = jieba.cut(sentence, cut_all=False)
words = []
for word in breakword:  #拆解句子為字詞
    if word not in stops:  #不是停用詞
        words.append(word)
print('|'.join(words)) 
