# ch17_30.py
from wordcloud import WordCloud
import jieba

with open("text17_29.txt") as fp:           # 含中文的文字檔
    txt = fp.read()                         # 讀取檔案

cut_text = ' '.join(jieba.cut(txt))         # 產生分詞的字串

wd = WordCloud(                             # 建立詞雲物件
    font_path="C:/Windows/Fonts\mingliu",   
    background_color="white",width=1000,height=880).generate(cut_text)

imageCloud = wd.to_image()          # 由WordCloud物件建立詞雲影像檔      
imageCloud.show()                   # 顯示詞雲影像檔






