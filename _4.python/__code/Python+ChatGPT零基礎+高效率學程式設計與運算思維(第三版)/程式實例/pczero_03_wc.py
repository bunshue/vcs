import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

# ex18_2.py
from wordcloud import WordCloud

with open("edata18_1.txt") as fp:   # 英文字的文字檔
    txt = fp.read()                 # 讀取檔案
    
wd = WordCloud(
    font_path="OLDENGL.TTF", 
    background_color="white").generate(txt)      
imageCloud = wd.to_image()          # 由WordCloud物件建立詞雲影像檔      
imageCloud.show()                   # 顯示詞雲影像檔
wd.to_file("eout18_2.png")


print('------------------------------------------------------------')	#60個

# ex18_4.py
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import jieba
import numpy as np

with open("edata18_1.txt") as fp:            # 含中文的文字檔
    txt = fp.read()                         # 讀取檔案
cut_text = ' '.join(jieba.cut(txt))         # 產生分詞的字串

bgimage = np.array(Image.open("me.GIF"))  # 背景圖

wd = WordCloud(                             # 建立詞雲物件
    font_path="OLDENGL.TTF",
    background_color="white",
    mask=bgimage).generate(cut_text)        # mask設定

plt.imshow(wd)                              # 由WordCloud物件建立詞雲影像檔
plt.axis("off")                             # 關閉顯示軸線
plt.show()                                  # 顯示詞雲影像檔
wd.to_file("eout18_4.png")



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





