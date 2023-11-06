import requests
from bs4 import BeautifulSoup
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
