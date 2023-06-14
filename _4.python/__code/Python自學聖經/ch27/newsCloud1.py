from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import numpy as np
from collections import Counter

text = open('news1.txt', "r",encoding="utf-8").read()  #讀文字資料
 
jieba.set_dictionary('dictionary/dict.txt.big.txt')
with open('dictionary/stopWord_cloud.txt', 'r', encoding='utf-8-sig') as f:  #設定停用詞
#with open('dictionary/stopWord_cloudmod.txt', 'r', encoding='utf-8-sig') as f:  #設定停用詞
    stops = f.read().split('\n')   
terms = []  #儲存字詞
for t in jieba.cut(text, cut_all=False):  #拆解句子為字詞
    if t not in stops:  #不是停用詞
        terms.append(t)
diction = Counter(terms)

font = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'	#設定字型
#mask = np.array(Image.open("heart.png"))  #設定文字雲形狀 
wordcloud = WordCloud(font_path=font) 
#wordcloud = WordCloud(background_color="white",mask=mask,font_path=font)  #背景顏色預設黑色,改為白色 
wordcloud.generate_from_frequencies(frequencies=diction)  #產生文字雲

#產生圖片
plt.figure(figsize = (6, 6))	#圖像大小[英吋]
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file("news_Wordcloud.png")  #存檔
