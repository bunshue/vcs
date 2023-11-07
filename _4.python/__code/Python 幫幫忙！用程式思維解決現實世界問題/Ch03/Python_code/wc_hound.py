# 匯入模組
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# 載入文字檔並存成字串
with open('hound.txt',encoding='utf-8', errors='ignore') as infile:
    text = infile.read()

# 將影像載入成 NumPy 陣列
mask = np.array(Image.open('holmes.png'))

# 取得停用字集合
stopwords = STOPWORDS
stopwords.update(['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',
                  'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
                  'put', 'seem', 'asked', 'made', 'half', 'much',
                  'certainly', 'might', 'came'])

# 產生文字雲
wc = WordCloud(max_words=500,
               relative_scaling=0.5,
               mask=mask,
               background_color='white',
               stopwords=stopwords,
               margin=10,
               random_state=6,
               contour_width=2,
               contour_color='brown',
               colormap='copper').generate(text)

# 將文字雲轉為 NumPy 陣列
colors = wc.to_array()

# 畫出和儲存文字雲
# %matplotlib  ← 程式若在 Anaconda 環境執行請取消註解
plt.figure()
plt.title("Chamberlain Hunt Academy Senior Class Presents:\n",
          fontsize=15, color='brown')
plt.text(-10, 0, "The Hound of the Baskervilles",
         fontsize=20, fontweight='bold', color='brown')
plt.suptitle("7:00 pm May 10-12 McComb Auditorium",
             x=0.52, y=0.095, fontsize=15, color='brown')
plt.imshow(colors, interpolation="bilinear")
plt.axis('off')
plt.show()
#plt.savefig('hound_wordcloud.png')
