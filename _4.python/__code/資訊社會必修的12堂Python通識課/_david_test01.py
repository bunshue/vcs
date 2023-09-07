'''
網路爬蟲類

可刪除檔案

'''


import requests
from bs4 import BeautifulSoup

import os

import sys

print('------------------------------------------------------------')	#60個
print('測試 01')


#台灣英文新聞網
url = 'https://www.taiwannews.com.tw/en/news/3610689'
url = 'https://www.taiwannews.com.tw/en/news/4966193'
html = requests.get(url).text
print(html)


print('------------------------------------------------------------')	#60個
print('測試 02')

#台灣英文新聞網
url = 'https://www.taiwannews.com.tw/en/news/3610689'
url = 'https://www.taiwannews.com.tw/en/news/4966193'
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")  # 解析原始碼
title = soup.find("h1", class_="article-title")
article = soup.find("article", class_="container-fluid article")
print(title.text)
print(article.text)


print('------------------------------------------------------------')	#60個
print('測試 03')

news_title = ""
news_content = ""
filename = 'engnews.txt'
if not os.path.exists(filename):
    #台灣英文新聞網
    url = 'https://www.taiwannews.com.tw/en/news/3610689'
    url = 'https://www.taiwannews.com.tw/en/news/4966193'
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")  # 解析原始碼
    title = soup.find("h1", class_="article-title")
    article = soup.find("article", class_="container-fluid article")
    news_title = title.text
    news_content = article.text
    with open(filename, "w", encoding="utf-8") as f:
        f.write(news_title+"\n")
        f.write(news_content)
else:
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        news_title = lines[0]
        news_content = lines[1:]
print(news_title)
print(news_content)



print('------------------------------------------------------------')	#60個
print('測試 04')

news_title = ""
news_content = ""
filename = "chinnews.txt"
if not os.path.exists(filename):
    #url = 'https://www.cna.com.tw/news/aopl/201901050192.aspx'
    url = 'https://www.cna.com.tw/news/ait/202308280292.aspx'
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")  # 解析原始碼
    title = soup.find("title")
    article = soup.find("div", class_="paragraph")
    news_title = title.text
    news_content = article.text
    with open(filename, "w", encoding="utf-8") as f:
        f.write(news_title+"\n")
        f.write(news_content)
else:
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        news_title = lines[0]
        news_content = lines[1:]
print(news_title)
print(news_content)

print('------------------------------------------------------------')	#60個
print('測試 05')

news_title = ""
news_content = ""
filename = "chinnews.txt"
if not os.path.exists(filename):
    #url = 'https://www.cna.com.tw/news/aopl/201901050192.aspx'
    url = 'https://www.cna.com.tw/news/ait/202308280292.aspx'
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")  # 解析原始碼
    title = soup.find("title")
    article = soup.find("div", class_="paragraph")
    news_title = title.text.strip()
    news_content = article.text
    with open(filename, "w", encoding="utf-8") as f:
        f.write(news_title+"\n")
        f.write(news_content)
else:
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        news_title = lines[0]
        news_content = lines[1:]
print(news_title)
print(news_content)



print('------------------------------------------------------------')	#60個

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    print(f.readline())
    print("-->Next")

filename = 'engnews.txt'    
with open(filename, "r", encoding="utf-8") as f:
    print(f.read())
    print("-->Next")

filename = 'engnews.txt'    
with open(filename, "r", encoding="utf-8") as f:
    print(f.readlines())

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
print(repr(data))

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
print(data.split())

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.split()
for d in data:
    d.strip()
print(data)

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.replace("(", "")
data = data.replace(")", "")
data = data.replace(",", "")
data = data.replace(".", "")
data = data.replace("“", "")
data = data.replace("”", "")
data = data.split()
print(data)

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
special_chars = list("(),.“”")
for char in special_chars:
    data = data.replace(char, "")
data = data.split()
print(data)

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord('('):None, ord(')'):None, ord('.'):None, ord('“'):None, ord('”'):None})
data = data.split()
print(data)

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord(c):None for c in list("(),.“”")})
data = data.split()
print(data)

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord(c):None for c in list("(),.“”")})
data = data.split()
word_freq = dict()
for word in data:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1
print(word_freq)

print('------------------------------------------------------------')	#60個

import operator

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord(c):None for c in list("(),.“”")})
data = data.split()
word_freq = dict()
for word in data:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1
ordered_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
for w, c in ordered_freq:
    print(w, c)

print('------------------------------------------------------------')	#60個

filename = 'ksvote.txt'
with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
print(ksvote)

print('------------------------------------------------------------')	#60個

filename = 'ksvote.txt'
with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = list()
for line in ksvote:
    num_ksvote.append(int(line.strip().replace(",","")))
print(num_ksvote)


print('------------------------------------------------------------')	#60個

filename = 'ksvote.txt'
with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = [int(line.strip().replace(",","")) for line in ksvote]
print(num_ksvote)

print('------------------------------------------------------------')	#60個

def fixtype(n):
    return int(n.strip().replace(",",""))

filename = 'ksvote.txt'
with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = map(fixtype, ksvote)
for vote in num_ksvote:
    print(vote)

print('------------------------------------------------------------')	#60個
filename = 'ksvote.txt'
with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = map(lambda n:int(n.strip().replace(",","")), ksvote)
for vote in num_ksvote:
    print(vote)

print('------------------------------------------------------------')	#60個

