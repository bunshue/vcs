import requests
from bs4 import BeautifulSoup as soup
from PIL import Image
import matplotlib.pyplot as plt
#from wordcloud import WordCloud
import jieba
import numpy as np
from collections import Counter

urls = []
url = 'https://udn.com/news/breaknews/1'  #聯合報新聞
html = requests.get(url)
sp = soup(html.text, 'html.parser')
data1 = sp.select('#breaknews_body dl dt h2 a')
for d in data1:  #取得新聞連結
    urls.append('https://udn.com' + d.get('href'))

text_news = ''
i = 1
for url in urls:  #逐一取得新聞
    html = requests.get(url)
    sp = soup(html.text, 'html.parser')
    data1 = sp.select('#story_body_content p')  #新聞內容
    print('處理第 {} 則新聞'.format(i))
    for d in data1:
        if d.text.find('延伸閱讀') != -1:  #遇到延伸閱讀就結束此則新聞
            break
        if d.text != '':  #有新聞內容
            text_news += d.text
    i += 1
 
jieba.set_dictionary('dictionary/dict.txt.big.txt')
with open('dictionary/stopWord_union.txt', 'r', encoding='utf-8-sig') as f:  #設定停用詞
    stops = f.read().split('\n')   
terms = []  #儲存字詞
for t in jieba.cut(text_news, cut_all=False):  #拆解句子為字詞
    if t not in stops:  #不是停用詞
        terms.append(t)
diction = Counter(terms)

'''
font = 'C:/______test_files2/msch.ttf'	#設定字型
mask = np.array(Image.open("heart.png"))  #設定文字雲形狀 
unioncloud = WordCloud(background_color="white",mask=mask,font_path=font)  #背景顏色預設黑色,改為白色 
unioncloud.generate_from_frequencies(frequencies=diction)  #產生文字雲

#產生圖片
plt.figure(figsize=(6,6))
plt.imshow(unioncloud)
plt.axis("off")
plt.show()

unioncloud.to_file("union_Wordcloud.png")  #存檔
'''


