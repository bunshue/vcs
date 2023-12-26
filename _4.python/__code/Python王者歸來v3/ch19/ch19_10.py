# ch19_10.py
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

with open("data19_6.txt") as fp:    # 含中文的文字檔
    txt = fp.read()                 # 讀取檔案

txt = '''產品性能卓越, Good, 客戶服務得到了很多正面評價,
Top, Excellent, 新產品線也獲得了市場的熱烈反應'''

cut_text = ' '.join(jieba.cut(txt)) # 產生分詞的字串

wd = WordCloud(                     # 建立詞雲物件
    font_path="C:/Windows/Fonts\mingliu",
    background_color="yellow",width=600,height=400).generate(cut_text)

plt.imshow(wd)                      # 由WordCloud物件建立詞雲影像檔
plt.axis("off")                     # 關閉顯示軸線
plt.show()                          # 顯示詞雲影像檔








