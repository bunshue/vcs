# ch16_1.py
import requests, bs4

url = 'https://www.biqukan.com/50_50096/'
htmlfile = requests.get(url)
print('原先編碼 : ', htmlfile.encoding)
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')          
book_author = objSoup.find('meta', property='og:novel:author')
book_title = objSoup.find('meta', property='og:novel:book_name')
book_description = objSoup.find('meta', property='og:description')
print('作者     : ', book_author['content'])
print('書名     : ', book_title['content'])
print('內文描述 : ', book_description['content'].strip())                          




