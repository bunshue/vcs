#!/usr/bin/env python
# coding: utf-8

# In[14]:


import json
import requests
api_url = "https://www.dcard.tw/_api/forums/funny/posts?limit=100"
res = requests.get(api_url).text


# In[17]:


data = json.loads(res)
for post in data:
    print(post["title"])


# In[6]:


print(res)

