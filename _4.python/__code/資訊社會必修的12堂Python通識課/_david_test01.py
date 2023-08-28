import requests


print('------------------------------------------------------------')	#60個



'''
#台灣英文新聞網
url = "https://www.taiwannews.com.tw/en/news/3610689"
html = requests.get(url).text
print(html)
'''



print('------------------------------------------------------------')	#60個



'''
from bs4 import BeautifulSoup
import requests
#台灣英文新聞網
url = "https://www.taiwannews.com.tw/en/news/3610689"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
title = soup.find("h1", class_="article-title")
article = soup.find("article", class_="container-fluid article")
print(title.text)
print(article.text)
'''


print('------------------------------------------------------------')	#60個



from bs4 import BeautifulSoup
import requests
import os

news_title = ""
news_content = ""
if not os.path.exists("engnews.txt"):
    #台灣英文新聞網
    url = "https://www.taiwannews.com.tw/en/news/3610689"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    title = soup.find("h1", class_="article-title")
    article = soup.find("article", class_="container-fluid article")
    news_title = title.text
    news_content = article.text
    with open("engnews.txt", "w", encoding="utf-8") as f:
        f.write(news_title+"\n")
        f.write(news_content)
else:
    with open("engnews.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        news_title = lines[0]
        news_content = lines[1:]
print(news_title)
print(news_content)



print('------------------------------------------------------------')	#60個




from bs4 import BeautifulSoup
import requests
import os

news_title = ""
news_content = ""
if not os.path.exists("chinews.txt"):
    url = "https://www.cna.com.tw/news/aopl/201901050192.aspx"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    title = soup.find("title")
    article = soup.find("div", class_="paragraph")
    news_title = title.text
    news_content = article.text
    with open("chinews.txt", "w", encoding="utf-8") as f:
        f.write(news_title+"\n")
        f.write(news_content)
else:
    with open("chinews.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        news_title = lines[0]
        news_content = lines[1:]
print(news_title)
print(news_content)



print('------------------------------------------------------------')	#60個

from bs4 import BeautifulSoup
import requests
import os

news_title = ""
news_content = ""
filename = "chinews.txt"
if not os.path.exists(filename):
    url = "https://www.cna.com.tw/news/aopl/201901050192.aspx"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
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



with open("engnews.txt", "r", encoding="utf-8") as f:
    print(f.readline())
    print("-->Next")
with open("engnews.txt", "r", encoding="utf-8") as f:
    print(f.read())
    print("-->Next")
with open("engnews.txt", "r", encoding="utf-8") as f:
    print(f.readlines())

print('------------------------------------------------------------')	#60個


with open("engnews.txt", "r", encoding="utf-8") as f:
    data = f.read()
print(repr(data))


print('------------------------------------------------------------')	#60個

with open("engnews.txt", "r", encoding="utf-8") as f:
    data = f.read()
print(data.split())


print('------------------------------------------------------------')	#60個

with open("engnews.txt", "r", encoding="utf-8") as f:
    data = f.read()
data = data.split()
for d in data:
    d.strip()
print(data)
print('------------------------------------------------------------')	#60個


with open("engnews.txt", "r", encoding="utf-8") as f:
    data = f.read()
data = data.replace("(", "")
data = data.replace(")", "")
data = data.replace(",", "")
data = data.replace(".", "")
data = data.replace("“", "")
data = data.replace("”", "")
data = data.split()
print(data)



print('------------------------------------------------------------')	#60個

with open("engnews.txt", "r", encoding="utf-8") as f:
    data = f.read()
special_chars = list("(),.“”")
for char in special_chars:
    data = data.replace(char, "")
data = data.split()
print(data)

print('------------------------------------------------------------')	#60個

with open("engnews.txt", "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord('('):None, ord(')'):None, ord('.'):None, ord('“'):None, ord('”'):None})
data = data.split()
print(data)


print('------------------------------------------------------------')	#60個
with open("engnews.txt", "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord(c):None for c in list("(),.“”")})
data = data.split()
print(data)

print('------------------------------------------------------------')	#60個

with open("engnews.txt", "r", encoding="utf-8") as f:
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
with open("engnews.txt", "r", encoding="utf-8") as f:
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


import jieba
with open("chinews.txt", "r", encoding="utf-8") as f:
    data = f.read()
print(data, "\n")
data = data.translate({ord(c):None for c in list("(),.“”（）「」，。、：；！|\n/ ")})
words = jieba.cut(data)
for word in words:
    print(word, "/ ", end="")


    
print('------------------------------------------------------------')	#60個

import jieba
with open("chinews.txt", "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord(c):None for c in list("(),.“”（）「」，。、：；！|\n/ ")})
words = jieba.cut(data)
word_freq = dict()
for word in words:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1
ordered_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
for w, c in ordered_freq:
    print(w, c)

print('------------------------------------------------------------')	#60個

from collections import Counter
import jieba
with open("chinews.txt", "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord(c):None for c in list("(),.“”（）「」，。、：；！|\n/ ")})
words = jieba.cut(data)
for w, c in Counter(words).most_common():
    if c > 1:
        print(w, c)
        

print('------------------------------------------------------------')	#60個


s = "   this is a sample sentance. this is a cat\n "
print(s.capitalize())
print(s.upper())
print(s.upper().casefold())
print(s.count("a"))
print(s.endswith("ce."))
print(s.find("this"))
print(s.split())
print("#".join(s.split()))
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.rfind("is"))
print(s.zfill(50))

print('------------------------------------------------------------')	#60個


with open("ksvote.txt", "r", encoding="utf-8") as f:
    ksvote = f.readlines()
print(ksvote)

print('------------------------------------------------------------')	#60個

with open("ksvote.txt", "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = list()
for line in ksvote:
    num_ksvote.append(int(line.strip().replace(",","")))
print(num_ksvote)


print('------------------------------------------------------------')	#60個

with open("ksvote.txt", "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = [int(line.strip().replace(",","")) for line in ksvote]
print(num_ksvote)

print('------------------------------------------------------------')	#60個

s = list("3874950382")
print(s)
print(sum(s))
print('------------------------------------------------------------')	#60個

s = list("3874950382")
print(s)
numbers = list()
for c in s:
    numbers.append(int(c))
print(sum(numbers))


print('------------------------------------------------------------')	#60個

s = list("3874950382")
print(s)
print(sum(map(int, s)))


print('------------------------------------------------------------')	#60個

def draw_bar(n):
    return "*"*n

s = [2, 5, 4, 7, 5, 4]
for bar in map(draw_bar, s):
    print(bar)


print('------------------------------------------------------------')	#60個

def fixtype(n):
    return int(n.strip().replace(",",""))

with open("ksvote.txt", "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = map(fixtype, ksvote)
for vote in num_ksvote:
    print(vote)

print('------------------------------------------------------------')	#60個

s = [2, 5, 4, 7, 5, 4]
for bar in map(lambda n: "*"*n, s):
    print(bar)

print('------------------------------------------------------------')	#60個


with open("ksvote.txt", "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = map(lambda n:int(n.strip().replace(",","")), ksvote)
for vote in num_ksvote:
    print(vote)

print('------------------------------------------------------------')	#60個


b = list('子丑寅卯辰巳午未申酉戌亥')
c = list('鼠牛虎兔龍蛇馬羊猴雞狗豬')
print(zip(b,c))
for item in zip(b, c):
    print(item)
print([item for item in zip(b, c)])


print('------------------------------------------------------------')	#60個


a = list('甲乙丙丁戊己庚辛壬癸')
b = list('子丑寅卯辰巳午未申酉戌亥')
for i in a:
    for j in b:
        print((i, j))

print('------------------------------------------------------------')	#60個

a = list('甲乙丙丁戊己庚辛壬癸')
b = list('子丑寅卯辰巳午未申酉戌亥')
years = list()
a_index = 0
b_index = 0
for i in range(60):
    years.append((a[a_index], b[b_index]))
    a_index += 1
    if a_index >= 10: 
        a_index = 0
    b_index += 1
    if b_index >= 12:
        b_index = 0
print(years)

print('------------------------------------------------------------')	#60個

a = list('甲乙丙丁戊己庚辛壬癸'*6)
b = list('子丑寅卯辰巳午未申酉戌亥'*5)
years = list(zip(a, b))
print(years)

print('------------------------------------------------------------')	#60個

