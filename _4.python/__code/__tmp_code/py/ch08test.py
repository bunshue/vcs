#!/usr/bin/env python
# coding: utf-8

# In[39]:


import requests, time
from bs4 import BeautifulSoup
target_url = 'https://www.nkust.edu.tw/p/403-1000-12-{}.php'

data = list()
for page in range(1, 6):
    html = requests.get(target_url.format(page)).text
    soup = BeautifulSoup(html, 'html.parser')
    sel = '#pageptlist > div > div > div > div > div'
    target = soup.select(sel)
    for item in target:
        pdate = item.i.text
        title = item.a.text.strip()
        link = item.a['href']
        data.append((pdate, link, title))
    time.sleep(3)


# In[3]:


from platform import python_version
print(python_version())
import bs4
print(bs4.__version__)


# In[41]:


contents = list()
for article in data[6:7]:
    content = dict()
    url = article[1]
    content['link'] = url
    print(url)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    sel = '#Dyn_2_3 > div.module.module-detail.md_style1 > div > section > div.mcont > div.mpgdetail > p:nth-child(2)'
    target = soup.select(sel)
    try:
        content['content'] = target[0].text
    except:
        content['content'] = ""
        pass
    contents.append(content)
    time.sleep(3)
print(contents)


# In[36]:


for article in data[5:6]:
    content = dict()
    url = article[1]
    content['date'] = article[0]
    content['title'] = article[2]
    print(url)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    sel = '#Dyn_2_3 > div.module.module-detail.md_style1 > div > section > div.mcont > div.mpgdetail > p:nth-child(2)'
    target = soup.select(sel)
    try:
        content['content'] = target[0].text
    except:
        content['content'] = ""
        pass
    print(content)
    time.sleep(3)


# In[7]:


get_ipython().system('pip install pymongo')


# In[1]:


from pymongo import MongoClient
conn = MongoClient()
db = conn.news
collection = db.nkust
collection.insert_one(content)


# In[38]:


from pymongo import MongoClient
conn = MongoClient()
db = conn.news
collection = db.nkust
cmd1 = {'content':{'$in': ['title']}}
cmd2 = {}
cmd3 = {'date': '2020-02-13'}
cmd4 = {'date': {'$in': ['20', '13']}}
rows = collection.find(cmd4, {'date':1})
for row in rows:
    print(row)
    print()

