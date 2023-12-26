# ch17_35.py
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

with open("text17_28.txt") as fp:           # 含中文的文字檔
    txt = fp.read()                         # 讀取檔案

bgimage = np.array(Image.open("hung.gif"))  # 背景圖

wd = WordCloud(                             # 建立詞雲物件
    font_path="C:/Windows/Fonts\OLDENGL.TTF",
    background_color="white",
    mask=bgimage).generate(txt)             # mask設定

plt.imshow(wd)                              # 由WordCloud物件建立詞雲影像檔
plt.axis("off")                             # 關閉顯示軸線
plt.show()                                  # 顯示詞雲影像檔








