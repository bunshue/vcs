import requests
from bs4 import BeautifulSoup

my_headers = {"cookie": "over18=1"}  # cookie設定

response = requests.get(
    #"https://www.ptt.cc/bbs/Gossiping/index.html")  # 改成八卦板的網址
    "https://www.ptt.cc/bbs/Gossiping/index.html", headers=my_headers)  # 放在headers欄位中傳送
soup = BeautifulSoup(response.text, "html.parser")  # 解析原始碼
print(soup.prettify())
links = soup.find_all("div", class_="title")    # 文章標題
print(links)
for link in links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白



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

soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("div", class_="title")    # 文章標題
print(links)
for link in links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白



import requests
url = 'http://www.e-happy.com.tw'
html_data = requests.get(url)
html_data.encoding="utf-8"
if html_data.status_code == requests.codes.ok:
    print(html_data.text)


import requests
from bs4 import BeautifulSoup
url = 'http://www.e-happy.com.tw'
html_data = requests.get(url)

soup = BeautifulSoup(html_data.text, 'html.parser')


import requests
from bs4 import BeautifulSoup
payload = {
   'from': 'https://www.ptt.cc/bbs/Gossiping/index.html',
	'yes': 'yes'
}
headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
items = soup.select('.r-ent')
for item in items:
    print(item.select('.date')[0].text, item.select('.author')[0].text, item.select('.title')[0].text)


