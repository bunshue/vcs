#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
url = "https://www.mobile01.com/topiclist.php?f=751"
res = requests.get(url)
print(res)


# In[4]:


import requests
url = "https://www.mobile01.com/topiclist.php?f=751"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
html = requests.get(url, headers=headers).text


# In[9]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
pages = soup.find_all("a", class_="c-pagination")
print(pages[-1].text)


# In[21]:


titles = soup.find_all("div", class_="c-listTableTd__title")
print(len(titles))
for title in titles:
    print(title)
    print(title.a.text)
    print(title.a['href'])

