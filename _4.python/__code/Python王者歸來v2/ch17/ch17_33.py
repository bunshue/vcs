# ch17_33.py
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

with open("text17_33.txt") as fp:        # 含中文的文字檔
    txt = fp.read()                     # 讀取檔案

cut_text = ' '.join(jieba.cut(txt))     # 產生分詞的字串

wd = WordCloud(                         # 建立詞雲物件
    font_path="C:/Windows/Fonts\mingliu",
    background_color="yellow",width=800,height=400).generate(cut_text)

plt.imshow(wd)                          # 由WordCloud物件建立詞雲影像檔
plt.axis("off")                         # 關閉顯示軸線
plt.show()                              # 顯示詞雲影像檔








