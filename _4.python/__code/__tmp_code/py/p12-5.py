#!/usr/bin/env python
# coding: utf-8

# In[28]:


import requests
url = "https://www.lexuscpo.com.tw/Home/CarStock"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
form_data = {
    "CarType":"", 
    "Series": "",
    "Price": "", 
    "Year": "", 
    "Mileage":"", 
    "StoreID":"", 
    "Page": "",
    "Limit": "20"
}
res = requests.post(url, data=form_data, headers=headers)
data = res.text


# In[38]:


import json
cars = json.loads(data)
cars = cars['rows']
message = "{:<10}({}年式)，{:>10,}KM，售價：{:>10,}元"
for car in cars:
    print(message.format(
        car['Model'], 
        car['Year'],
        car['Mileage'],
        car['SellPrice']))

