import os
import sys
import time
import random

import matplotlib.pyplot as plt

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_wc/data18_1.txt'
with open(filename) as fp:    # 英文字的文字檔
    txt = fp.read()                 # 讀取檔案
    
wd = WordCloud().generate(txt)      # 由txt文字產生WordCloud物件

plt.imshow(wd)
plt.show()
#wd.to_file("wc01.png")               # 檔案儲存

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_wc/data18_2.txt'
with open(filename, encoding='cp950') as fp: # 含中文的文字檔
    txt = fp.read()                 # 讀取檔案
    
wd = WordCloud().generate(txt)      # 由txt文字產生WordCloud物件

plt.imshow(wd)
plt.show()
#wd.to_file("wc02.png")               # 檔案儲存

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
import jieba

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_wc/data18_2.txt'
with open(filename, encoding='cp950') as fp:  # 含中文的文字檔
    txt = fp.read()                         # 讀取檔案

cut_text = ' '.join(jieba.cut(txt))         # 產生分詞的字串

wd = WordCloud(                             # 建立詞雲物件
    font_path=font_filename,   
    background_color="white",width=800,height=600).generate(cut_text)

plt.imshow(wd)
plt.show()
#wd.to_file("wc03.png")               # 檔案儲存

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
import jieba

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_wc/data18_2.txt'
with open(filename, encoding='cp950') as fp:  # 含中文的文字檔
    txt = fp.read()                     # 讀取檔案

cut_text = ' '.join(jieba.cut(txt))     # 產生分詞的字串

wd = WordCloud(                         # 建立詞雲物件
    font_path=font_filename,
    background_color="white",width=800,height=600).generate(cut_text)

plt.imshow(wd)
plt.show()
#wd.to_file("wc04.png")               # 檔案儲存

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
import jieba

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_wc/data18_2.txt'
with open(filename, encoding='cp950') as fp:    # 含中文的文字檔
    txt = fp.read()                     # 讀取檔案

cut_text = ' '.join(jieba.cut(txt))     # 產生分詞的字串

wd = WordCloud(                         # 建立詞雲物件
    font_path=font_filename,
    background_color="yellow",width=800,height=400).generate(cut_text)

plt.imshow(wd)
plt.axis("off")                         # 關閉顯示軸線
plt.show()
#wd.to_file("wc05.png")                  # 檔案儲存

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
import jieba

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_wc/data18_6.txt'
with open(filename, encoding="cp950") as fp:  # 含中文的文字檔
    txt = fp.read()                     # 讀取檔案

cut_text = ' '.join(jieba.cut(txt))     # 產生分詞的字串

wd = WordCloud(                         # 建立詞雲物件
    font_path=font_filename,
    background_color="yellow",width=800,height=400).generate(cut_text)

plt.imshow(wd)
plt.axis("off")                         # 關閉顯示軸線
plt.show()
#wd.to_file("wc06.png")               # 檔案儲存

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
from PIL import Image
import jieba
import numpy as np

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_wc/data18_6.txt'
with open(filename, encoding='cp950') as fp:        # 含中文的文字檔
    txt = fp.read()                         # 讀取檔案
cut_text = ' '.join(jieba.cut(txt))         # 產生分詞的字串

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_mask/star.gif'
bgimage = np.array(Image.open(filename))  # 背景圖

wd = WordCloud(                             # 建立詞雲物件
    font_path=font_filename,
    background_color="white",
    mask=bgimage).generate(cut_text)        # mask設定

plt.imshow(wd)
plt.axis("off")                             # 關閉顯示軸線
plt.show()
#wd.to_file("wc07.png")               # 檔案儲存

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
from PIL import Image
import numpy as np

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_wc/data18_1.txt'
with open(filename, encoding='cp950') as fp:        # 含中文的文字檔
    txt = fp.read()                         # 讀取檔案

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_mask/heart.png'

bgimage = np.array(Image.open(filename))  # 背景圖

wd = WordCloud(                             # 建立詞雲物件
    font_path="OLDENGL.TTF",
    background_color="white",
    mask=bgimage).generate(txt)             # mask設定

plt.imshow(wd)
plt.axis("off")                             # 關閉顯示軸線
plt.show()
#wd.to_file("wc08.png")               # 檔案儲存

print('------------------------------------------------------------')	#60個

