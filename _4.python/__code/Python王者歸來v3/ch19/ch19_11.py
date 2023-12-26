# ch19_11.py
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import jieba
import numpy as np

txt = '''我們的智慧手機有著卓越的電池壽命和出色的相機功能。
它的超高解析度顯示螢幕讓視覺體驗更上一層樓。'''
cut_text = ' '.join(jieba.cut(txt))         # 產生分詞的字串
bgimage = np.array(Image.open("star.gif"))  # 背景圖

wd = WordCloud(                             # 建立詞雲物件
    font_path="C:/Windows/Fonts\mingliu",
    background_color="white",
    mask=bgimage).generate(cut_text)        # mask設定

plt.imshow(wd)                              # 由WordCloud物件建立詞雲影像檔
plt.axis("off")                             # 關閉顯示軸線
plt.show()                                  # 顯示詞雲影像檔








