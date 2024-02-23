"""
Python資料科學實戰教本



"""


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup 

html_str = "<p>Hello World!</p>"
soup = BeautifulSoup(html_str, "lxml")
print(soup)


print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

r = requests.get("https://fchart.github.io/ML/Surveys.html")
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
print(soup)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-2-1b.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    print(soup)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")

tags = soup("a")
tag = tags[1]
print("標籤名稱: ", tag.name)
print("標籤內容: ", tag.text)
print("標籤內容: ", tag.string)
print("標籤內容: ", tag.b.string)
print("URL網址: ", tag.get("href", None))
print("target屬性: ", tag["target"])




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-2-2a.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")

tags = soup("img")
tag = tags[0]
print("圖片網址: ", tag.get("src", None))
print("alt屬性: ", tag["alt"])
print("屬性: ", tag.attrs)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-2-3.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 走訪下一層HTML標籤
print(soup.html.body.div.div.p.a.text)
print("----------------------")
# 走訪上一層HTML標籤
tag_div = soup.select_one("#q1") # 找到第1題的<div>標籤
tag_li = tag_div.ul.li    # 走訪到之下的<ul>
print(tag_li.text)
# 使用parent屬性取得父標籤
print(tag_li.parent.parent.p.a.text)
print("----------------------")
tag_div = soup.select_one("#q2") # 找到第2題的<div>標籤
print(tag_div.find_previous_sibling().p.a.text)
print(tag_div.find_next_sibling().p.a.text)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")

#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋<a>標籤
tag_a = soup.find("a") 
print(tag_a.text)
# 呼叫多次find()方法
tag_p = soup.find(name="p")
tag_a = tag_p.find(name="a")
print(tag_p.a.text)
print(tag_a.text)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-1a.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用id屬性搜尋<div>標籤
tag_div = soup.find(id="q2")
tag_a = tag_div.find("a") 
print(tag_a.text)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-1b.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  
    
# 使用class屬性搜尋<span>標籤
tag_span = soup.find(attrs={"class": "score"})
print(tag_span.text)
# 搜尋第2題的第1個<span>標籤
tag_div = soup.find(id="q2")
tag_span = tag_div.find(class_="score")
print(tag_span.text)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-1c.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用HTML5的data-屬性搜尋<div>標籤
tag_div = soup.find(attrs={"data-custom": "important"})
print(tag_div.text)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-1d.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")

# 使用文字內容來搜尋標籤
tag_str = soup.find(text="請問你的")
print(tag_str)
tag_str = soup.find(text="10")
print(tag_str)
print(type(tag_str))        # NavigableString型態
print(tag_str.parent.name)  # 父標籤名稱
tag_str = soup.find(text="男 - ")
print(tag_str)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-1e.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")   
    
# 測試取出<li>標籤的內容
tag_str = soup.find(text="女 - ")
print(tag_str)
tag_li = soup.find(class_="response")
print(tag_li.text)
print(tag_li.string)
print(tag_li.span.string)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-1f.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")      
    
# 使用多條件來搜尋HTML標籤
tag_div = soup.find("div", class_="question")
print(tag_div.prettify())
tag_p = soup.find("p", class_="question")
print(tag_p.prettify())


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-1g.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  
    
# 使用函數建立搜尋條件
def is_secondary_question(tag):
    return tag.has_attr("href") and \
           tag.get("href") == "http://example.com/q2"

tag_a = soup.find(is_secondary_question)
print(tag_a.prettify())



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-2.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")      
    
# 找出所有問卷的題目串列
tag_list = soup.find_all("p", class_="question")
print(tag_list[0].prettify())

for question in tag_list:
    print(question.a.text)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-2a.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")     
    
# 找出前2個問卷的題目串列
tag_list = soup.find_all("p", class_="question", limit=2)
print(len(tag_list))

for question in tag_list:
    print(question.a.text)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-2b.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

tag_div = soup.find("div", id="q2")
# 找出所有標籤串列
tag_all = tag_div.find_all(True)
for tag in tag_all:
    print(tag.name)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-2c.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

tag_div = soup.find("div", id="q2")
# 找出所有文字內容串列
tag_str_list = tag_div.find_all(text=True)
print(tag_str_list)
# 找出指定的文字內容串列
tag_str_list = tag_div.find_all(text=["20", "40"])
print(tag_str_list)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-2d.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

tag_div = soup.find("div", id="q2")
# 找出所有<p>和<span>標籤
tag_list = tag_div.find_all(["p", "span"])
for tag in tag_list:
    print(tag.name, tag.text.replace("\n", ""))
print("-------------")
# 找出class屬性值question或selected的所有標籤
tag_list = tag_div.find_all(class_=["question", "selected"])
for tag in tag_list:
    print(tag.name, tag.text.replace("\n", ""))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-2e.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

tag_div = soup.find("div", id="q2")
# 找出所有<li>子孫標籤
tag_list = tag_div.find_all("li")
for tag in tag_list:
    print(tag.text.replace("\n", ""))
# 沒有使用遞迴來找出所有<li>標籤
tag_list = tag_div.find_all("li", recursive=False)
print(tag_list)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-4-2.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋<title>標籤和第3個<div>標籤
tag_title = soup.select("title")
print(tag_title[0].text)
tag_first_div = soup.find("div")
tag_div = tag_first_div.select("div:nth-of-type(3)")
print(tag_div[0].prettify())



print("------------------------------------------------------------")  # 60個




#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-4-2a.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋class和id屬性值的標籤
tag_div = soup.select("#q1")
print(tag_div[0].p.a.text)
tag_span = soup.select("span#email")
print(tag_span[0].text)
tag_div = soup.select("#q1, #q2")  # 多個id屬性
for item in tag_div:
    print(item.p.a.text)
print("-----------")
tag_div = soup.find("div")  # 第1個<div>標籤
tag_p = tag_div.select(".question")   
for item in tag_p:
    print(item.a["href"])
tag_span = soup.select("[class~=selected]")
for item in tag_span:
    print(item.text)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-4-2b.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋特定屬性值的標籤
def print_a(tag_a):
    for tag in tag_a:
        print(tag["href"])
    print("-----------")    
tag_a = soup.select("a[href]")
print_a(tag_a)
tag_a = soup.select("a[href='http://example.com/q2']")
print_a(tag_a)
tag_a = soup.select("a[href^='http://example.com']")
print_a(tag_a)
tag_a = soup.select("a[href$='q3']")
print_a(tag_a)
tag_a = soup.select("a[href*='q']")
print_a(tag_a)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-4-2c.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋<title>標籤, 和<div>標籤下的所有<a>標籤
tag_title = soup.select("html head title")
print(tag_title[0].text)    
tag_a = soup.select("body div a")
for tag in tag_a:
    print(tag["href"])




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-4-2d.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋指定標籤下的直接子標籤
tag_a = soup.select("p > a")
for tag in tag_a:
    print(tag["href"])
tag_li = soup.select("ul > li:nth-of-type(2)")
for tag in tag_li:
    print(tag.text.replace("\n", ""))
tag_span = soup.select("div > #email")
for tag in tag_span:
    print(tag.prettify())  



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-4-2e.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋兄弟標籤
tag_div = soup.find(id="q1")
print(tag_div.p.a.text)
print("-----------")
tag_div = soup.select("#q1 ~ .survey")
for item in tag_div:            
    print(item.p.a.text)  
print("-----------")
tag_div = soup.select("#q1 + .survey")
for item in tag_div:            
    print(item.p.a.text)   



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-4-3.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用select_one()方法搜尋標籤
tag_a = soup.select_one("a[href]")
print(tag_a.prettify())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-5-2.py

import re
from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用正規表達式搜尋文字內容
tag_str = soup.find(text="男 -")
print(tag_str)
regexp = re.compile("男 -")
tag_str = soup.find(text=regexp)
print(tag_str)
print("---------------------")
regexp = re.compile("\w+ -")
tag_list = soup.find_all(text=regexp)
print(tag_list)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-5-2a.py

import re
from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用正規表達式搜尋電子郵件地址
email_regexp = re.compile("\w+@\w+\.\w+")
tag_str = soup.find(text=email_regexp)
print(tag_str)
print("---------------------")
tag_list = soup.find_all(text=email_regexp)
print(tag_list)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-5-2b.py

import re
from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用正規表達式搜尋URL網址
url_regexp = re.compile("^http:")
tag = soup.find(href=url_regexp)
print(tag["href"], tag.text)
print("---------------------")
tag_list = soup.find_all(href=url_regexp)
for tag in tag_list:
    print(tag["href"], tag.text)

print("------------------------------------------------------------")  # 60個

"""webdriver skip
#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-1.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tag_ol = soup.find("ol", {"id":"list"})
tags_li = tag_ol.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-1_edge.py

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tag_ol = soup.find("ol", {"id":"list"})
tags_li = tag_ol.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-2.py

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

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-2_edge.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
tag_ol = driver.find_element(By.XPATH, '/html/body/ol')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements(By.XPATH, '//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-2a.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
tag_ol = driver.find_element(By.XPATH, '/html/body/ol')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements(By.XPATH, '//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-2a_edge.py

from selenium import webdriver

driver = webdriver.Edge("./msedgedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('/html/body/ol')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath('//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-2b.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
tag_ol = driver.find_element(By.XPATH, '//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute('innerHTML'))
soup = BeautifulSoup(tag_ol.get_attribute('innerHTML'), "lxml")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-2b_edge.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
tag_ol = driver.find_element(By.XPATH, '//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute('innerHTML'))
soup = BeautifulSoup(tag_ol.get_attribute('innerHTML'), "lxml")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()
"""

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



