import requests
import jieba
import operator
from bs4 import BeautifulSoup

url = 'https://tw.nextapple.com/realtime/headlines'
news_page = requests.get(url)

print('news_page.text')
print(news_page.text)

news = BeautifulSoup(news_page.text, 'html.parser')
news_title = news.find_all('div', {'class': 'post-inner'})
'''
print('news_title')
print(news_title)
'''

headlines = ''
for t in news_title:
        title = t.find_all('a')[0]
        headlines += title.text
        print(title.text)

'''
print('headlines')
print(headlines)
'''	

words = jieba.cut(headlines)

word_count = dict()

for word in words:
	if word in word_count.keys():
		word_count[word] += 1
	else:
		word_count[word] = 1

	sorted_wc = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)

'''
for item in sorted_wc:
	if item[1]>1:
		print(item)
	else:
		break
'''

print('done')

