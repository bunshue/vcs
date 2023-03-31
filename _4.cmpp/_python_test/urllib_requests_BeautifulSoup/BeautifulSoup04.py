#PTT C_Chat板每篇文章的標題

import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/C_Chat/index.html'
response = requests.get(url)     # 取得C_Chat的HTML原始碼
#print(response.text)
#print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")  # 解析原始碼

# 發現所有的文章標題都在class="title"的div中

links = soup.find_all("div", class_="title")    # 文章標題
for link in links:
    print(link.text.strip()) # strip()用來刪除文字前面和後面多餘的空白



import requests
from bs4 import BeautifulSoup

resp = requests.get('http://blog.castman.net/web-crawler-tutorial/ch1/connect.html')

if resp and resp.status_code == 200:
    print(resp.status_code)
    #print(resp.text)
    soup = BeautifulSoup(resp.text, 'html.parser')
    #print(soup)
    try:
        h1 = soup.find('h1')
    except:
        h1 = None
    if h1:
        print(soup.find('h1'))
        print(soup.find('h1').text)
    try:
        h2 = soup.find('h2')
    except:
        h2 = None
    if h2:
        print(soup.find('h2').text)
    else:
        print('h2 tag not found!')
