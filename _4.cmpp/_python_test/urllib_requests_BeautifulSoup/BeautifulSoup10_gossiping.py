import requests
from bs4 import BeautifulSoup

print('有無 cookies 之比較')

#gossiping
url = 'https://www.ptt.cc/bbs/Gossiping/index.html' #八卦板的網址

print('無 cookies')
html_data = requests.get(url)
#print(html_data.text)
soup = BeautifulSoup(html_data.text, "html.parser")
print(soup.prettify())

print('有 cookies')
cookies = {'over18':'1'}
html_data = requests.get(url, cookies=cookies)
#print(html_data.text)
soup = BeautifulSoup(html_data.text, "html.parser")
print(soup.prettify())

print('BeautifulSoup 測試 1a 使用 cookie')

url = 'https://www.ptt.cc/bbs/Gossiping/index.html' #八卦板的網址

my_headers = {"cookie": "over18=1"}  # cookie設定

response = requests.get(url, headers = my_headers)  # 放在headers欄位中傳送
soup = BeautifulSoup(response.text, "html.parser")  # 解析原始碼
#print(soup.prettify())
links = soup.find_all("div", class_ = "title")    # 文章標題
#print(links)
for link in links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白

print('BeautifulSoup 測試 1b 使用 session')

# post要傳的資料
payload = {
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
}

rs = requests.session() # 用session紀錄此次使用的cookie
response = rs.post("https://www.ptt.cc/ask/over18", data=payload)   # post傳遞資料
response = rs.get(url)  # 再get一次PTT八卦板首頁
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("div", class_="title")    # 文章標題
for link in links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白

print('BeautifulSoup 測試 1c')

import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Gossiping/index.html' #八卦板的網址

payload = {
   'from': url,
	'yes': 'yes'
}
headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
res = rs.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
items = soup.select('.r-ent')
for item in items:
    print(item.select('.date')[0].text, item.select('.author')[0].text, item.select('.title')[0].text)


import requests
from bs4 import BeautifulSoup

# post要傳的資料
payload = {
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
}

# 用session紀錄此次使用的cookie
rs = requests.session()
# post傳遞資料
response = rs.post("https://www.ptt.cc/ask/over18", data=payload)
# 再get一次PTT八卦板首頁
response = rs.get("https://www.ptt.cc/bbs/Gossiping/index.html")
print(response.status_code)

root = BeautifulSoup(response.text, "html.parser")
links = root.find_all("div", class_="title")    # 文章標題
for link in links:
    page_url = "https://www.ptt.cc"+link.a["href"]
    print(page_url)
    response = rs.get(page_url)
    result = BeautifulSoup(response.text, "html.parser")
    main_content = result.find("div", id="main-content")
    article_info = main_content.find_all("span", class_="article-meta-value")
    if len(article_info) != 0:
        author = article_info[0].string  # 作者
        title = article_info[2].string  # 標題
        time = article_info[3].string   # 時間
    else: # 避免有沒有資訊的狀況
        author = "無"  # 作者
        title = "無"  # 標題
        time = "無"   # 時間
    #print(author + ' ' + title + ' ' + time)
    # 將整段文字內容抓出來
    all_text = main_content.text
    # 以--切割，抓最後一個--前的所有內容
    pre_texts = all_text.split("--")[:-1]
    # 將前面的所有內容合併成一個
    one_text = "--".join(pre_texts)
    # 以\n切割，第一行標題不要
    texts = one_text.split("\n")[1:]
    # 將每一行合併
    content = "\n".join(texts)
    print(content)

