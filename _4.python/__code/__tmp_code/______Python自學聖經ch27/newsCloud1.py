from PIL import Image
import matplotlib.pyplot as plt
import wordcloud
import jieba
import numpy as np
from collections import Counter

text = open('news1.txt', "r",encoding="utf-8").read()  #讀文字資料

dict_filename = 'C:/_git/vcs/_1.data/______test_files1/_jieba/dict.txt.big.txt'  #設定繁體中文詞庫
jieba.set_dictionary(dict_filename)
# with open('dictionary/stopWord_times.txt', 'r', encoding='utf-8-sig') as f:  #設定停用詞
#with open('dictionary/stopWord_cloud.txt', 'r', encoding='utf-8-sig') as f:  #設定停用詞
with open('dictionary/stopWord_cloudmod.txt', 'r', encoding='utf-8-sig') as f:  #設定停用詞
    stops = f.read().split('\n')   
terms = []  #儲存字詞
for t in jieba.cut(text, cut_all=False):  #拆解句子為字詞
    if t not in stops:  #不是停用詞
        terms.append(t)
diction = Counter(terms)

print(diction)

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'	#設定字型

mask_filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_mask/heart.png'
mask = np.array(Image.open(mask_filename))  #設定文字雲形狀 
wc = wordcloud.WordCloud(background_color="white",mask=mask,font_path=font_filename)  #背景顏色預設黑色,改為白色 
wc.generate_from_frequencies(frequencies=diction)  #產生文字雲

plt.imshow(wc)
plt.axis("off")
plt.show()
