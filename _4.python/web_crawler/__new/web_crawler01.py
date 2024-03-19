import sys
import requests
from bs4 import BeautifulSoup 

print('------------------------------------------------------------')	#60個

from urllib.parse import urlparse

o = urlparse("http://www.example.com:80/test/index.php?user=joe")

print('使用urlparse()方法剖析URL網址成為組成的元素')
print("通訊協定: ", o.scheme)
print("網域名稱: ", o.netloc)
print("通訊埠號: ", o.port)
print("網頁路徑: ", o.path)
print("查詢字串: ", o.query)

print('------------------------------------------------------------')	#60個

url = "https://fchart.github.io/test.html"
response = requests.get(url)
if response.status_code == 200:
    print("Text :\n", response.text)
    print("編碼: ", response.encoding)
    print("status_code : ", response.status_code)
else:
    print("錯誤! HTTP請求失敗...")

print('------------------------------------------------------------')	#60個

url_params = {'name': '陳會安', 'grade': 95}
r = requests.get("http://httpbin.org/get", params=url_params)
if r.status_code == 200:
    print(r.text)
else:
    print("錯誤! HTTP請求失敗...")

print('------------------------------------------------------------')	#60個

url = "http://httpbin.org/user-agent"
 
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
r = requests.get(url, headers=headers)
print(r.text)

print('------------------------------------------------------------')	#60個

url = "http://httpbin.org/user-agent"
 
r = requests.get(url)
print(r.text)

print('------------------------------------------------------------')	#60個

url = "http://httpbin.org/cookies"

cookies = dict(name='Joe Chen')
r = requests.get(url, cookies=cookies)
print(r.text)

print('------------------------------------------------------------')	#60個

post_data = {'name': '陳會安', 'grade': 95}
r = requests.post("http://httpbin.org/post", data=post_data)
print(r.text)

print('------------------------------------------------------------')	#60個

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

cookies = { "over18": "1" }
r = requests.get(url, cookies=cookies)
print(r.text)

print('------------------------------------------------------------')	#60個

""" fail chromedriver
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print('------------------------------------------------------------')	#60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
cookie = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookie)
print(driver.title)
driver.quit()

print('------------------------------------------------------------')	#60個

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome("./chromedriver", options=options)
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()
"""

print('------------------------------------------------------------')	#60個

url = "https://www.taifex.com.tw/cht/3/totalTableDate"
post_data = "queryType=1&goDay=&doQuery=1&dateaddcnt=&queryDate=2020%2F08%2F07"
r = requests.post(url, data=post_data)
print(r.text)

print('------------------------------------------------------------')	#60個

url = "https://api.sgx.com/derivatives/v1.0/contract-code/TW?order=asc&orderby=delivery-month&category=futures&session=-1&t=1596956628001&showTAICTrades=false"
r = requests.get(url)
print(r.text)

print('------------------------------------------------------------')	#60個

""" fail chromedriver
from selenium import webdriver
import time

url = "https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&jobcatExpansionType=1&order=12&asc=0&page=6&mode=s&jobsource=2018indexpoc"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
print(len(driver.page_source))
for x in range(5):
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(3)
    print(x+1, len(driver.page_source))
driver.quit()
"""
print('------------------------------------------------------------')	#60個

URL = "https://maker.ifttt.com/trigger/{0}/with/key/{1}/?"
event_name = "web_scraping"
api_key = "<API金鑰>"

def email_alert(first, second=None, third=None):
    url = URL.format(event_name, api_key)
    data = {}
    data["value1"] = first
    data["value2"] = second
    data["value3"] = third    
    for key, val in data.items():
        if val:
            url = url + key + "=" + str(val) + "&"
    r = requests.get(url)    
    if r.status_code == 200:
        print("已經寄送郵件通知...")
    else:
        print("錯誤! 寄送郵件通知失敗...")

email_alert("測試值1", 100)

print('------------------------------------------------------------')	#60個
 
URL = "https://maker.ifttt.com/trigger/{0}/with/key/{1}/?"
event_name = "web_scraping"
api_key = "<API金鑰>"

def email_alert(first, second=None, third=None):
    url = URL.format(event_name, api_key)
    data = {}
    data["value1"] = first
    data["value2"] = second
    data["value3"] = third    
    r = requests.post(url, data=data)       
    if r.status_code == 200:
        print("已經寄送郵件通知...")
    else:
        print("錯誤! 寄送郵件通知失敗...")

email_alert("測試值2", 150, 200)

print('------------------------------------------------------------')	#60個

""" fail
token = "<存取權杖>"
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/x-www-form-urlencoded"
}
params = {"message": "Python程式送出測試通知訊息"}
r = requests.post("https://notify-api.line.me/api/notify",
                   headers=headers, params=params)  
if r.status_code == 200:
    print("已經送出通知訊息...")
else:
    print("錯誤! 寄送通知訊息失敗...")
"""
print('------------------------------------------------------------')	#60個

""" fail API key
token = "<API權杖>"
chat_id = "<聊天室識別碼>"

def telegram_bot_sendText(msg):
    url = "https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}"
    r = requests.post(url.format(token,chat_id,msg))  
    return r.json()

test = telegram_bot_sendText("大家好!")
print(test)

print('------------------------------------------------------------')	#60個

import telegram
 
token = "<API權杖>"
chat_id = "<聊天室識別碼>"

def telegram_bot_sendText(msg):
    bot = telegram.Bot(token=token)
    return bot.sendMessage(chat_id=chat_id, text=msg)
    
test = telegram_bot_sendText("測試Telegram模組!")
print(test)
"""

print('------------------------------------------------------------')	#60個

""" fail
url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
span = soup.find('span', class_="current")
temp = span.text
summary = span.get("aria-label")

def email_alert(first, second=None, third=None):
    URL = "https://maker.ifttt.com/trigger/{0}/with/key/{1}/?"
    event_name = "web_scraping"
    api_key = "<API金鑰>"
    url = URL.format(event_name, api_key)
    data = {}
    data["value1"] = first
    data["value2"] = second
    data["value3"] = third    
    for key, val in data.items():
        if val:
            url = url + key + "=" + str(val) + "&"
    r = requests.get(url)    
    if r.status_code == 200:
        print("已經寄送郵件通知...")
    else:
        print("錯誤! 寄送郵件通知失敗...")

email_alert(temp, summary)

print('------------------------------------------------------------')	#60個

url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
span = soup.find('span', class_="current")
temp = span.text
summary = span.get("aria-label")

def LINE_alert(msg):
    token = "<存取權杖>"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    params = {"message": msg}
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)  
    if r.status_code == 200:
        print("已經送出通知訊息...")
    else:
        print("錯誤! 寄送通知訊息失敗...")

LINE_alert(temp +"/" + summary)
"""
print('------------------------------------------------------------')	#60個

""" fail api key
url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
span = soup.find('span', class_="current")
temp = span.text
summary = span.get("aria-label")

def telegram_bot_sendText(msg):
    token = "<API權杖>"
    chat_id = "<聊天室識別碼>"
    url = "https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}"
    r = requests.post(url.format(token,chat_id,msg))  
    return r.json()

telegram_bot_sendText(temp +"/" + summary)
"""
print('------------------------------------------------------------')	#60個


print('抓取一個網頁的所有連結網址')
#html使用<a>標籤來製作連結
#抓取網頁所有的 <a href="XXXXXXXXXXXXX">YYYYYYYYYY</a> 之XXXXXXXXXXXXX部分 即網頁連結

url = 'https://hispark.hccg.gov.tw/'    #新竹市路邊停車收費網

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    tags = soup("a")
    for tag in tags:
        print(tag.get("href", None))
else:
    print("錯誤! HTTP請求失敗...")

print('抓取一個網頁的所有圖片連結網址')
#html使用<img>來顯示圖片
#<img src="https://hispark.hccg.gov.tw/uploadfile/images/relatedlink/relatedlink_2.jpg" width="170" height="67" border="0" />

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    tags = soup("img")
    for tag in tags:
        print(tag.get("src", None))
else:
    print("錯誤! HTTP請求失敗...")

print('------------------------------------------------------------')	#60個

url = 'https://hispark.hccg.gov.tw/'    #新竹市路邊停車收費網

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

print('找所有連結a')
tags = soup("a")
print('共找到', len(tags), '個連結')
#print(tags)

print('看第12個連結')
tag = tags[12]
print("URL網址: ", tag.get("href", None))
print("標籤內容: ", tag.text)
print("target屬性: ", tag["target"])

print('找所有圖片img')
tags = soup("img")
print('共找到', len(tags), '個圖片')
#print(tags)

print('看第0個圖片')
tag = tags[0]
print("圖片網址: ", tag.get("src", None))
print("alt屬性: ", tag["alt"])
print("屬性: ", tag.attrs)

print('------------------------------------------------------------')	#60個

import re

str1 = """Joe's email is joe@gmail.com,  
Tom's email is tom@yahoo.com"""
match = re.search(r"[\w.-]+@[A-Za-z0-9_.-]+", str1)
if match:
    print(match.group())
else:
    print("沒有找到符合的字串!")
    
print('------------------------------------------------------------')	#60個

import re

str1 = """Joe's email is joe@gmail.com,  
Tom's email is tom@yahoo.com"""

match = re.search(r"([\w.-]+)@([A-Za-z0-9_.-]+)", str1)
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
else:
    print("沒有找到符合的字串!")

print('------------------------------------------------------------')	#60個

import re

str1 = """Joe's email is joe@gmail.com,  
Tom's email is tom@yahoo.com"""
match = re.findall(r"[\w.-]+@[A-Za-z0-9_.-]+", str1)
if match:
    print(match)
else:
    print("沒有找到符合的字串!")

print('------------------------------------------------------------')	#60個

import re

str1 = """Joe's email is joe@gmail.com,  
Tom's email is tom@yahoo.com"""
pattern = re.compile(r"[\w.-]+@[A-Za-z0-9_.-]+")
match = re.search(pattern, str1)
if match:
    print(match.group())
else:
    print("沒有找到符合的字串!")

print('------------------------------------------------------------')	#60個

import re

url = "https://fchart.github.io/"
response = requests.get(url)
links = re.findall(r'href="https://.*?"', response.text)
for link in links:
    print(link)

print('------------------------------------------------------------')	#60個

""" warning chromedriver
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tag_ol = soup.find("ol", {"id":"list"})
tags_li = tag_ol.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()

print('------------------------------------------------------------')	#60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('//*[@id="list"]')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath('//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print('------------------------------------------------------------')	#60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('/html/body/ol')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath('//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print('------------------------------------------------------------')	#60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute('innerHTML'))
soup = BeautifulSoup(tag_ol.get_attribute('innerHTML'), "lxml")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()
"""
print('------------------------------------------------------------')	#60個

print('使用 fake user agent')
from fake_useragent import UserAgent

ua = UserAgent()
print(ua.ie)
print(ua.google)
print(ua.firefox)
print(ua.safari)
print(ua.random)

print('------------------------------------------------------------')	#60個

from fake_useragent import UserAgent

ua = UserAgent()
headers = {'user-agent' : ua.random}

url = "https://www.momoshop.com.tw/main/Main.jsp"
r = requests.get(url, headers=headers)
print(r.status_code)
print(r.text)

print('------------------------------------------------------------')	#60個

""" fail
url = "https://www.momoshop.com.tw/main/Main.jsp"
r = requests.get(url)
print(r.status_code)
print(r.text)

"""

print('------------------------------------------------------------')	#60個

""" fail
from fake_useragent import UserAgent
import random

ua = UserAgent()
def proxyGenerator():
   headers = {'user-agent': ua.random}
   res = requests.get('https://free-proxy-list.net/', headers=headers)
   soup = BeautifulSoup(res.text, 'lxml') 
   proxies_table = soup.find(id='proxylisttable')
   proxies = [] 
   for row in proxies_table.tbody.find_all('tr'):
     proxies.append({  
       'http': "http://" + row.find_all('td')[0].string + ":" +
               row.find_all('td')[1].string, 
       'https': "https://" + row.find_all('td')[0].string + ":" +
               row.find_all('td')[1].string        
     })   
   return random.choice(proxies)

for n in range(5):
  proxy = proxyGenerator()
  print(proxy)
"""

print('------------------------------------------------------------')	#60個

""" fail
proxy = {'http': 'http://109.161.48.141:3128',
         'https': 'https://109.161.48.141:3128'}
r = requests.get("http://httpbin.org/ip", proxies=proxy)
print(r.status_code)
print(r.text)
"""

print('------------------------------------------------------------')	#60個

""" fail
from fake_useragent import UserAgent
import random

ua = UserAgent()
def proxyGenerator():
   headers = {'user-agent': ua.random}
   res = requests.get('https://free-proxy-list.net/', headers=headers)
   soup = BeautifulSoup(res.text, 'lxml') 
   proxies_table = soup.find(id='proxylisttable')
   proxies = [] 
   for row in proxies_table.tbody.find_all('tr'):
     proxies.append({  
       'http': "http://" + row.find_all('td')[0].string + ":" +
               row.find_all('td')[1].string, 
       'https': "https://" + row.find_all('td')[0].string + ":" +
               row.find_all('td')[1].string        
     })   
   return random.choice(proxies)

while True:
   proxy = proxyGenerator()
   print("目前使用的代理伺服器: ", proxy)
   try:
      headers = {'user-agent': ua.random}
      url = "http://httpbin.org/ip"
      r = requests.get(url, headers=headers, proxies=proxy, verify=False)
      print(r.status_code)
      print(r.text)
      break
   except:
      print("連線錯誤! 搜尋其他的代理伺服器!")
      pass 
"""

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

""" fail chromedriver
from selenium import webdriver
import time

email_address = "<電子郵件地址>"
password = "<密碼>"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
url = "https://www.facebook.com/"
driver.get(url)

email = driver.find_element_by_css_selector("#email")
email.send_keys(email_address)
time.sleep(0.5)
passwd = driver.find_element_by_css_selector("#pass")
passwd.send_keys(password)
time.sleep(0.5)
button = driver.find_element_by_css_selector("#loginbutton")
button.click()
time.sleep(5)
soup = BeautifulSoup(driver.page_source, "lxml")
tag_title = soup.find("title")
print(tag_title.text)
driver.quit()
"""

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

#html使用<div>標籤來分割網頁區塊，多用來指定套用CSS的範圍


