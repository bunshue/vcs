import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

""" 無檔案 Example.html
#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_5_1.py

from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用childen屬性取得子標籤
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>
for child in tag_ul.children:
    print(type(child))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_5_1a.py

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用childen屬性取得子標籤
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>
for child in tag_ul.children:
    if not isinstance(child, NavigableString):
        print(child.name)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_5_2.py

from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用屬性向下走訪
print(soup.html.head.title.string)
print(soup.html.head.meta["charset"])
# 使用div屬性取得第1個<div>標籤
print(soup.html.body.div.div.p.a.string)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_5_2a.py

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用屬性取得所有子標籤
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>
for child in tag_ul.contents:
    if not isinstance(child, NavigableString):
        print(child.span.string)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_5_2b.py

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用屬性取得所有子標籤
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>            
for child in tag_ul.children:
    if not isinstance(child, NavigableString):
        print(child.name)
        for tag in child:
            if not isinstance(tag, NavigableString):
                print(tag.name, tag.string)
            else:
                print(tag.replace('\n', ''))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_5_2c.py

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用屬性取得所有子孫標籤
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>            
for child in tag_ul.descendants:
    if not isinstance(child, NavigableString):
        print(child.name)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_5_2d.py

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用屬性取得所有子孫的文字內容
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>
for string in tag_ul.strings:
    print(string.replace('\n', ''))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_5_3.py

from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>
# 使用屬性取得父標籤
print(tag_ul.parent.name)
# 使用函數取得父標籤
print(tag_ul.find_parent().name)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_5_3a.py

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>
# 使用屬性取得所有祖先標籤
for tag in tag_ul.parents:
    print(tag.name)
# 使用函數取得所有祖先標籤
for tag in tag_ul.find_parents():
    print(tag.name)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_5_4.py

from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
tag_div = soup.select("#q2") # 找到第2題
first_li = tag_div[0].ul.li  # 第1個<li>
print(first_li)
# 使用next_sibling屬性取得下一個兄弟標籤
second_li = first_li.next_sibling.next_sibling
print(second_li)
# 呼叫next_sibling()函數取得下一個兄弟標籤
third_li = second_li.find_next_sibling()
print(third_li)
print("---------------------------------------")
# 呼叫next_siblings()函數取得所有兄弟標籤
for tag in first_li.find_next_siblings():
    print(tag.name, tag.span.string)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_5_4a.py

from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
tag_div = soup.select("#q2") # 找到第2題
tag_li = tag_div[0].ul.li  # 第1個<li>
third_li = tag_li.find_next_sibling().find_next_sibling()
print(third_li)
# 使用previous_sibling屬性取得前一個兄弟標籤
second_li = third_li.previous_sibling.previous_sibling
print(second_li)
# 呼叫previous_sibling()函數取得前一個兄弟標籤
first_li = second_li.find_previous_sibling()
print(first_li)
print("---------------------------------------")
# 呼叫previous_siblings()函數取得所有兄弟標籤
for tag in third_li.find_previous_siblings():
    print(tag.name, tag.span.string)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_5_5.py

from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
tag_html = soup.html # 找到第<html>標籤
print(type(tag_html), tag_html.name)
tag_next = tag_html.next_element.next_element
print(type(tag_next), tag_next.name)
tag_title = soup.title # 找到第<title>標籤
print(type(tag_title), tag_title.name)
tag_previous = tag_title.previous_element.previous_element
print(type(tag_previous), tag_previous.name)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_5_5a.py

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")    
tag_div = soup.find(id = "emails")
for element in tag_div.next_elements:
    if not isinstance(element, NavigableString):
        print(element.name)
   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_5_5b.py

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")    
tag_div = soup.find(id="q1")
for element in tag_div.previous_elements:
    if not isinstance(element, NavigableString):
        print(element.name)
   
"""
print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_6.py

from bs4 import BeautifulSoup

soup = BeautifulSoup("<b class='score'>Joe</b>", "lxml")    
tag = soup.b
tag.name = "p"
tag["class"] = "question"
tag["id"] = "name"
print(tag)
del tag["class"]
print(tag)   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_6a.py

from bs4 import BeautifulSoup

soup = BeautifulSoup("<b class='score'>Joe</b>", "lxml")    
tag = soup.b
tag.string = "Mary"
print(tag)
  

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_6b.py

from bs4 import BeautifulSoup
from bs4.element import NavigableString

soup = BeautifulSoup("<b></b>", "lxml")    
tag = soup.b
tag.append("Joe")
print(tag)
new_str = NavigableString(" Chen")
tag.append(new_str)
print(tag)
new_tag = soup.new_tag("a", href="http://www.example.com")
tag.append(new_tag)
print(tag)
  

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_6c.py

from bs4 import BeautifulSoup

soup = BeautifulSoup("<p><b>One</b></p>", "lxml")  
tag = soup.b  
new_tag = soup.new_tag("i")
new_tag.string = "Two"
tag.insert_before(new_tag)
print(soup.p)
new_string = soup.new_string("Three")
tag.insert_after(new_string)
print(soup.p)
tag.clear()
print(soup.p)
  

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\Ch5_6d.py

from bs4 import BeautifulSoup

soup = BeautifulSoup("<p><b>One</b></p>", "lxml")  
tag = soup.b  
new_tag = soup.new_tag("i")
new_tag.string = "Two"
tag.replace_with(new_tag)
print(soup.p)
  

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\appb-1-1.py

import requests

r = requests.get("https://fchart.github.io/Example.html")

fp = open("tmp_Example.txt", "w", encoding="utf8")
fp.write(r.text)
print("寫入檔案 tmp_Example.txt...")
fp.close()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\appb-1-1a.py

fp = open("tmp_Example.txt", "r", encoding="utf8")
str = fp.read()
print("檔案內容:")
print(str)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\appb-1-1b.py

with open("tmp_Example.txt", "r", encoding="utf8") as fp:
    str = fp.read()
    print("檔案內容:")
    print(str)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\appb\appb-1-1c.py

with open("tmp_Example.txt", "r", encoding="utf8") as fp:
    list1 = fp.readlines()
    for line in list1:
        print(line, end="")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


