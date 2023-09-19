import sys
import os
import jieba

print('------------------------------------------------------------')	#60個

string =  '名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。'
print('原字串')
print(string)

seg_list = jieba.cut(string, cut_all = False)
print('預設切分 / 精確模式')
print(' | '.join(seg_list))     #預設切分

print('預設切分')
seg_list = jieba.cut(string)
print(' | '.join(seg_list))     #預設切分 後面cut_all不寫

print('全切分 / 全文模式')
seg_list = jieba.cut(string, cut_all = True)
print(' | '.join(seg_list))     #全切分

print('全切分, 搜尋引擎模式')
seg_list = jieba.cut_for_search(string)
print(' | '.join(seg_list))     #全切分 全切分, 搜尋引擎模式

print('------------------------------------------------------------')	#60個

#默認使用精確模式(一般直接使用精確模式即可)

string =  '名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。'

print('預設:', ' | '.join(jieba.cut(string, cut_all = False, HMM = True)))
print('全關閉:', ' | '.join(jieba.cut(string, cut_all = False, HMM = False)))
print('全關閉:', ' | '.join(jieba.cut(string, cut_all = True, HMM = True)))

print('------------------------------------------------------------')	#60個

dict_filename = 'C:/_git/vcs/_1.data/______test_files1/_jieba/dict.txt.big.txt'  #設定繁體中文詞庫

#下載繁體中文詞庫後，使用set_dictionary()方法匯入
jieba.set_dictionary(dict_filename)  #不一定要設定詞庫，內建的效果也不錯

seg_list = jieba.cut(string, cut_all = False)
print(' | '.join(seg_list))

print('------------------------------------------------------------')	#60個

print('使用自訂詞庫')
dict_filename = 'C:/_git/vcs/_1.data/______test_files1/_jieba/user_dict_test.txt'  #設定自訂詞庫
jieba.load_userdict(dict_filename)

stopWord_filename = 'C:/_git/vcs/_1.data/______test_files1/_jieba/stopWord_test.txt'  #設定自訂詞庫
with open(stopWord_filename, 'r', encoding = 'utf-8-sig') as f:  #設定停用詞
    stops = f.read().split('\n')   

string =  '名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。'
seg_list = jieba.cut(string, cut_all=False)
words = []
for word in seg_list:  #拆解句子為字詞
    if word not in stops:  #不是停用詞
        words.append(word)
print('|'.join(words)) 

print('------------------------------------------------------------')	#60個

