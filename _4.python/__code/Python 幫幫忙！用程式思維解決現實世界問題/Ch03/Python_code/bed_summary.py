import requests
import bs4
from nltk.tokenize import sent_tokenize
from gensim.summarization import summarize

# 設定網址
url = 'https://jamesclear.com/great-speeches/\
make-your-bed-by-admiral-william-h-mcraven'

# 載入演說內容到字串
page = requests.get(url)
page.raise_for_status()
soup = bs4.BeautifulSoup(page.text, 'html.parser')
p_elems = [element.text for element in soup.find_all('p')]

# 將段落內容串在一起
speech = ' '.join(p_elems)

# 建立和輸出演說摘要
print("\nSummary of Make Your Bed speech:")
summary = summarize(speech, word_count=225)
sentences = sent_tokenize(summary)
sents = set(sentences)
print(' '.join(sents))
