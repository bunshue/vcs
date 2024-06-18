
print("------------------------------------------------------------")  # 60個

# get.py
import requests
url = 'http://www.ehappy.tw/demo.htm'
html = requests.get(url)
# 檢查HTTP回應碼是否為200(requests.code.ok)
if html.status_code == requests.codes.ok:
    print(html.text)

print("------------------------------------------------------------")  # 60個


# get_headers.py
import requests
url = 'https://irs.thsrc.com.tw/IMINT/'
# 自訂表頭
headers={
   'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
# 將自訂表頭加入 GET 請求中
html = requests.get(url, headers=headers)
print(html)


print("------------------------------------------------------------")  # 60個


# get_cookie.py
import requests
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
# 設定cookies的值
cookies = {'over18':'1'}
r = requests.get(url, cookies=cookies)
print(r.text)

print("------------------------------------------------------------")  # 60個

# bs1.py
import requests
from bs4 import BeautifulSoup
url = 'http://ehappy.tw/bsdemo1.htm'
html = requests.get(url)
html.encoding = 'UTF-8'
sp = BeautifulSoup(html.text, 'lxml')

print(sp.title)
print(sp.title.text)
print(sp.h1)
print(sp.p)


print("------------------------------------------------------------")  # 60個


# bs2.py
from bs4 import BeautifulSoup
html = '''
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <p id="p1">我是段落一</p>
      <p id="p2" class='red'>我是段落二</p>
  </body>
</html>
'''
sp = BeautifulSoup(html, 'lxml')
print(sp.find('p'))
print(sp.find_all('p'))
print(sp.find('p', {'id':'p2', 'class':'red'}))
print(sp.find('p', id='p2', class_= 'red'))


print("------------------------------------------------------------")  # 60個


# bs3.py
from bs4 import BeautifulSoup
html = '''
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <p id="p1">我是段落一</p>
      <p id="p2" class='red'>我是段落二</p>
  </body>
</html>
'''
sp = BeautifulSoup(html, 'lxml')
print(sp.select('title'))
print(sp.select('p'))
print(sp.select('#p1'))
print(sp.select('.red'))


print("------------------------------------------------------------")  # 60個


# bs4.py
from bs4 import BeautifulSoup
html = '''
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <img src="http://www.ehappy.tw/python.png">
      <a href="http://www.e-happy.com.tw">超連結</a>
  </body>
</html>
'''
sp = BeautifulSoup(html, 'lxml')
print(sp.select('img')[0].get('src'))
print(sp.select('a')[0].get('href'))
print(sp.select('img')[0]['src'])
print(sp.select('a')[0]['href'])



print("------------------------------------------------------------")  # 60個


# taiwanlottery.py
import requests
from bs4 import BeautifulSoup
url = 'https://www.taiwanlottery.com.tw/'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
# 找到威力彩的區塊
datas = sp.find('div', class_='contents_box02')
# 開獎期數
title = datas.find('span', 'font_black15').text
print('威力彩期數：', title)
# 開獎號碼
nums = datas.find_all('div', class_='ball_tx ball_green')
# 開出順序
print('開出順序：', end=' ')
for i in range(0,6):
    print(nums[i].text, end=' ')
# 大小順序
print('\n大小順序：', end=' ')
for i in range(6,12):
    print(nums[i].text, end=' ')
# 第二區
num = datas.find('div', class_='ball_red').text
print('\n第二區：', num)


print("------------------------------------------------------------")  # 60個


# re_match.py
import re
m = re.match(r'[a-z]+','abc123xyz')
print(m) 
if m != None:
    print(m.group())    #abc
    print(m.start())    #0
    print(m.end())      #3
    print(m.span())     #(0, 3)



print("------------------------------------------------------------")  # 60個


# re_search.py
import re
m = re.search(r'[a-z]+', 'abc123xyz')
print(m)    # <re.Match object; span=(0, 3), match='abc'>
if m != None:
    print(m.group())  # abc
    print(m.start())  # 0
    print(m.end())    # 3
    print(m.span())   # (0,3)

print("------------------------------------------------------------")  # 60個


# re_findall.py
import re
m = re.findall(r'[a-z]+', 'abc123xyz')
print(m)    # ['abc', 'xyz']    


print("------------------------------------------------------------")  # 60個

# re_sub.py
import re
result = re.sub(r"\d+", "*", "Password:1234,ID:5678")
print(result) # Password:*,ID:*


print("------------------------------------------------------------")  # 60個

# regex.py
html = """
<div class="content">
    E-Mail：<a href="mailto:mail@test.com.tw">mail</a><br>
    E-Mail2：<a href="mailto:mail2@test.com.tw">mail2</a><br>
    <ul class="price">定價：360元 </ul>
    <img src="http://test.com.tw/p1.jpg">
    <img src="http://test.com.tw/p2.jpg">
    <img src="http://test.com.tw/p3.png">
    電話：(04)-76543210、0937-123456
</div>
"""

import re

emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',html)
for email in emails: #顯示 email
    print(email)

price=re.findall(r'[\d]+元',html)[0].split('元')[0] #價格
print(price) #顯示定價金額

imglist = re.findall(r'[http://]+[a-zA-Z0-9-/.]+\.[jpgpng]+',html)
for img in imglist: #
    print(img) #顯示圖片網址
    
phonelist = re.findall(r'\(?\d{2,4}\)?\-\d{6,8}',html)
for phone in phonelist:
    print(phone) #顯示電話號碼 

print("------------------------------------------------------------")  # 60個


# twhrtimetable.py
from selenium import webdriver
# 高鐵時刻表查詢網站
url = 'http://www.thsrc.com.tw/tw/TimeTable/SearchResult'
ss='台中站'      #出發站
es='台北站'      #到達站
dd='2020/03/26' #日期 
dt='09:00'      #時間
# 建立瀏覽器物件開啟網站
driver = webdriver.Chrome()
driver.get(url)
#輸入出發站
driver.find_element_by_id('StartStation').send_keys(ss) 
#輸入到達站
driver.find_element_by_id('EndStation').send_keys(es)   
#輸入日期
driver.find_element_by_id("DepartueSearchDate").click()
driver.find_element_by_id('DepartueSearchDate').send_keys(dd) 
#輸入時間
driver.find_element_by_id("DepartueSearchTime").click()
driver.find_element_by_id('DepartueSearchTime').send_keys(dt)
driver.find_element_by_id('SearchButton').click() #按查詢鈕














































