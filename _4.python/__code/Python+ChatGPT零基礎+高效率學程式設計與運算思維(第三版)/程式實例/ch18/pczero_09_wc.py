import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

title = "Ming-Chi Institute of Technology"
print(f"/{title.center(50)}/")
dt = "Department of ME"
print(f"/{dt.ljust(50)}/")
site = "JK Hung"
print(f"/{site.rjust(50)}/")
print(f"/{title.zfill(50)}/")

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud

with open("data18_1.txt") as fp:    # 英文字的文字檔
    txt = fp.read()                 # 讀取檔案
    
wd = WordCloud().generate(txt)      # 由txt文字產生WordCloud物件
imageCloud = wd.to_image()          # 由WordCloud物件建立詞雲影像檔      
#imageCloud.show()                   # 顯示詞雲影像檔

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud

with open("data18_2.txt", encoding='cp950') as fp: # 含中文的文字檔
    txt = fp.read()                 # 讀取檔案
    
wd = WordCloud().generate(txt)      # 由txt文字產生WordCloud物件
imageCloud = wd.to_image()          # 由WordCloud物件建立詞雲影像檔      
#imageCloud.show()                   # 顯示詞雲影像檔

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
import jieba

with open("data18_2.txt", encoding='cp950') as fp:  # 含中文的文字檔
    txt = fp.read()                         # 讀取檔案

cut_text = ' '.join(jieba.cut(txt))         # 產生分詞的字串

wd = WordCloud(                             # 建立詞雲物件
    font_path="NotoSansTC-Bold.otf",   
    background_color="white",width=1000,height=880).generate(cut_text)

imageCloud = wd.to_image()          # 由WordCloud物件建立詞雲影像檔      
#imageCloud.show()                   # 顯示詞雲影像檔
wd.to_file("out18_3.png")           # 檔案儲存

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

with open("data18_2.txt", encoding='cp950') as fp:  # 含中文的文字檔
    txt = fp.read()                     # 讀取檔案

cut_text = ' '.join(jieba.cut(txt))     # 產生分詞的字串

wd = WordCloud(                         # 建立詞雲物件
    font_path="NotoSansTC-Bold.otf",
    background_color="white",width=800,height=600).generate(cut_text)

plt.imshow(wd)                          # 由WordCloud物件建立詞雲影像檔
plt.show()                              # 顯示詞雲影像檔
wd.to_file("out18_4.png")               # 檔案儲存

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

with open("data18_2.txt", encoding='cp950') as fp:    # 含中文的文字檔
    txt = fp.read()                     # 讀取檔案

cut_text = ' '.join(jieba.cut(txt))     # 產生分詞的字串

wd = WordCloud(                         # 建立詞雲物件
    font_path="NotoSansTC-Bold.otf",
    background_color="yellow",width=800,height=400).generate(cut_text)

plt.imshow(wd)                          # 由WordCloud物件建立詞雲影像檔
plt.axis("off")                         # 關閉顯示軸線
plt.show()                              # 顯示詞雲影像檔
wd.to_file("out18_5.png")               # 儲存檔案

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

with open("data18_6.txt", encoding="cp950") as fp:  # 含中文的文字檔
    txt = fp.read()                     # 讀取檔案

cut_text = ' '.join(jieba.cut(txt))     # 產生分詞的字串

wd = WordCloud(                         # 建立詞雲物件
    font_path="NotoSansTC-Bold.otf",
    background_color="yellow",width=800,height=400).generate(cut_text)

plt.imshow(wd)                          # 由WordCloud物件建立詞雲影像檔
plt.axis("off")                         # 關閉顯示軸線
plt.show()                              # 顯示詞雲影像檔
wd.to_file("out18_6.png")               # 儲存檔案

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import jieba
import numpy as np

with open("data18_6.txt", encoding='cp950') as fp:        # 含中文的文字檔
    txt = fp.read()                         # 讀取檔案
cut_text = ' '.join(jieba.cut(txt))         # 產生分詞的字串

bgimage = np.array(Image.open("star.gif"))  # 背景圖

wd = WordCloud(                             # 建立詞雲物件
    font_path="NotoSansTC-Bold.otf",
    background_color="white",
    mask=bgimage).generate(cut_text)        # mask設定

plt.imshow(wd)                              # 由WordCloud物件建立詞雲影像檔
plt.axis("off")                             # 關閉顯示軸線
plt.show()                                  # 顯示詞雲影像檔
wd.to_file("out18_7.png")                   # 儲存檔案

print('------------------------------------------------------------')	#60個

from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

with open("data18_1.txt", encoding='cp950') as fp:        # 含中文的文字檔
    txt = fp.read()                         # 讀取檔案

bgimage = np.array(Image.open("hung.GIF"))  # 背景圖

wd = WordCloud(                             # 建立詞雲物件
    font_path="OLDENGL.TTF",
    background_color="white",
    mask=bgimage).generate(txt)             # mask設定

plt.imshow(wd)                              # 由WordCloud物件建立詞雲影像檔
plt.axis("off")                             # 關閉顯示軸線
plt.show()                                  # 顯示詞雲影像檔
wd.to_file("out18_8.png")                   # 儲存檔案


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





