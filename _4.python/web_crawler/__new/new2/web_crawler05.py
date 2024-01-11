import sys
import requests
from bs4 import BeautifulSoup 

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

url = "https://fchart.github.io/Elements.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

tag = soup.select_one("h2")
print("h2: ", tag.text)

tags = soup.select("b")
print("b: ", tags[0].text)

tag = soup.select_one("#q2")
tag2 = tag.select_one("b")
print("b: ", tag2.text)

tags = soup.select(".response")
print("li: ", tags[0].text)
print("li: ", tags[1].text)

print('------------------------------------------------------------')	#60個

url = "https://fchart.github.io/Elements.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

tag = soup.find("h2")
print("h2: ", tag.text)

tag = soup.find("b")
print("b: ", tag.text)

tags = soup.find_all("b")
print("b: ", tags[0].text)

tag = soup.find("li", {"id":"q2"})
tag_q = tag.find("b")
print("Question: ", tag_q.text)

tags_a = tag.find_all("li", {"class":"response"})
for tag in tags_a:
    print("Ans: ", tag.text)

print('------------------------------------------------------------')	#60個

url = "https://fchart.github.io/Elements.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

tag = soup.find("h2")
print("h2: ", tag.text)

tag = soup.find("b")
print("b: ", tag.text)

tags = soup.find_all("b")
print("b: ", tags[0].text)

tag = soup.find("li", {"id":"q2"})
tag_q = tag.find("b")
print("Question: ", tag_q.text)

tags_a = tag.find_all("li", class_="response")
for tag in tags_a:                           
    print("Ans: ", tag.text)

print('------------------------------------------------------------')	#60個

url = "https://fchart.github.io/Elements.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
tags_li = soup.find_all("li", class_="response", limit=3)
print(tags_li)

print('------------------------------------------------------------')	#60個

url = "https://fchart.github.io/Elements.html"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

tag_ans1 = soup.find("li", class_="response")
print(tag_ans1.text)

tag_ans2 = tag_ans1.find_next()
print(tag_ans2.text)

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

import requests
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

import requests
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'user-agent' : ua.random}

url = "https://www.momoshop.com.tw/main/Main.jsp"
r = requests.get(url, headers=headers)
print(r.status_code)
print(r.text)

print('------------------------------------------------------------')	#60個

""" fail
import requests

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
import requests

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

""" fail
import csv

url = "https://www.bbc.com/zhongwen/trad/business"
csvfile = "tmp_news.csv"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
tag_div = soup.find("div", class_="eagle")
tags_div = tag_div.find_all("div", class_="eagle-item")
output = []
for tag in tags_div:
    item = []
    title = tag.find("h3", class_="title-link__title").find("span") 
    item.append(title.text.strip())
    summary = tag.find("p", class_="eagle-item__summary")
    item.append(summary.text)
    a = tag.find("a")
    item.append(a.get("href", None))
    output.append(item)
    
with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(["title","summary","href"])
    for row in output:
        writer.writerow(row)
"""

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

