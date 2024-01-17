"""
文字資訊的視覺化手法
繪製文字雲
"""

print('------------------------------------------------------------')	#60個

import sys

import matplotlib.pyplot as plt

from wordcloud import WordCloud

with open("data2/data19_1.txt") as fp:    # 英文字的文字檔
    txt = fp.read()
    
wc = WordCloud()
wc.generate(txt)

plt.imshow(wc)
plt.axis("off")
plt.show()

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud

with open("data2/data19_2.txt") as fp:    # 含中文的文字檔
    txt = fp.read()
    
wc = WordCloud()
wc.generate(txt)

plt.imshow(wc)
plt.axis("off")
plt.show()

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
import jieba

with open("data2/data19_2.txt") as fp:            # 含中文的文字檔
    txt = fp.read()

cut_text = ' '.join(jieba.cut(txt))         # 產生分詞的字串

wc = WordCloud(width=1000,height=600,
               font_path="C:/Windows/Fonts\mingliu",
               background_color="white")
wc.generate(cut_text)

plt.imshow(wc)
plt.axis("off")
plt.show()

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
import jieba

with open("data2/data19_2.txt") as fp:        # 含中文的文字檔
    txt = fp.read()

cut_text = ' '.join(jieba.cut(txt))     # 產生分詞的字串

wc = WordCloud(width=1000,height=600,
               font_path="C:/Windows/Fonts\mingliu",
               background_color="white")
wc.generate(cut_text)

plt.imshow(wc)
plt.axis("off")
plt.show()

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
import jieba

with open("data2/data19_2.txt") as fp:        # 含中文的文字檔
    txt = fp.read()

cut_text = ' '.join(jieba.cut(txt))     # 產生分詞的字串

wc = WordCloud(width=1000,height=600,
               font_path="C:/Windows/Fonts\mingliu",
               background_color="white")
wc.generate(cut_text)

plt.imshow(wc)
plt.axis("off")
plt.show()

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
import jieba

with open("data2/data19_6.txt") as fp:        # 含中文的文字檔
    txt = fp.read()

cut_text = ' '.join(jieba.cut(txt))     # 產生分詞的字串

wc = WordCloud(width=1000,height=600,
               font_path="C:/Windows/Fonts\mingliu",
               background_color="white")
wc.generate(cut_text)

plt.imshow(wc)
plt.axis("off")
plt.show()

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
from PIL import Image
import jieba
import numpy as np

with open("data2/data19_6.txt") as fp:            # 含中文的文字檔
    txt = fp.read()
cut_text = ' '.join(jieba.cut(txt))         # 產生分詞的字串

bgimage = np.array(Image.open("data2/star.gif"))  # 背景圖

wc = WordCloud(
    font_path="C:/Windows/Fonts\mingliu",
    background_color="white",
    mask=bgimage)
wc.generate(cut_text)        # mask設定

plt.imshow(wc)
plt.axis("off")
plt.show()

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
from PIL import Image
import numpy as np

with open("data2/data19_1.txt") as fp:            # 文字檔
    txt = fp.read()

bgimage = np.array(Image.open("data2/hung.gif"))  # 背景圖

wc = WordCloud(
    font_path="C:/Windows/Fonts\OLDENGL.TTF",
    background_color="white",
    mask=bgimage)
wc.generate(txt)             # mask設定

plt.imshow(wc)
plt.axis("off")
plt.show()

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
import jieba

with open("data2/data19_6.txt") as fp:    # 含中文的文字檔
    txt = fp.read()

txt = '''這個產品非常易用, 性價比高, 客服回應速度慢。
設計很時尚, 但運送過程中有輕微損壞。'''

cut_text = ' '.join(jieba.cut(txt)) # 產生分詞的字串

wc = WordCloud(width=1000,height=600,
               font_path="C:/Windows/Fonts\mingliu",
               background_color="white")
wc.generate(cut_text)

plt.imshow(wc)
plt.axis("off")
plt.show()

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
import jieba

with open("data2/data19_6.txt") as fp:    # 含中文的文字檔
    txt = fp.read()

txt = '''產品性能卓越, Good, 客戶服務得到了很多正面評價,
Top, Excellent, 新產品線也獲得了市場的熱烈反應'''

cut_text = ' '.join(jieba.cut(txt)) # 產生分詞的字串

wc = WordCloud(width=1000,height=600,
               font_path="C:/Windows/Fonts\mingliu",
               background_color="white")
wc.generate(cut_text)

plt.imshow(wc)
plt.axis("off")
plt.show()

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
from PIL import Image
import jieba
import numpy as np

txt = '''我們的智慧手機有著卓越的電池壽命和出色的相機功能。
它的超高解析度顯示螢幕讓視覺體驗更上一層樓。'''
cut_text = ' '.join(jieba.cut(txt))         # 產生分詞的字串
bgimage = np.array(Image.open("data2/star.gif"))  # 背景圖

wc = WordCloud(
    font_path="C:/Windows/Fonts\mingliu",
    background_color="white",
    mask=bgimage)
wc.generate(cut_text)        # mask設定

plt.imshow(wc)
plt.axis("off")
plt.show()

print('------------------------------------------------------------')	#60個


from wordcloud import WordCloud

with open("data2/edata19_1.txt") as fp:   # 英文字的文字檔
    txt = fp.read()
    
wc = WordCloud(
    font_path="C:/Windows/Fonts\OLDENGL.TTF", 
    background_color="white")
wc.generate(txt)      

plt.imshow(wc)
plt.axis("off")
plt.show()

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
from PIL import Image
import jieba
import numpy as np

with open("data2/edata19_1.txt") as fp:            # 含中文的文字檔
    txt = fp.read()
cut_text = ' '.join(jieba.cut(txt))         # 產生分詞的字串

bgimage = np.array(Image.open("data2/me.gif"))  # 背景圖

wc = WordCloud(
    font_path="C:/Windows/Fonts\OLDENGL.TTF",
    background_color="white",
    mask=bgimage)
wc.generate(cut_text)        # mask設定

plt.imshow(wc)
plt.axis("off")
plt.show()

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


