import requests
from bs4 import BeautifulSoup

videourlList = []  #儲存所有影片網址的串列
urltext = '/watch?v=hGRplpwjbr0&list=PL316wRwpvsnHZprsPfXM8yPzyZ41bvuWl'  #黑豹預告片
baseurl = 'https://www.youtube.com'
html = requests.get(baseurl + urltext)
soup = BeautifulSoup(html.text, 'html.parser')
res1 = soup.find_all('a')
for res in res1:
    temurl = baseurl + res.get('href')
    if('&index=' in temurl):
        videourlList.append(temurl)
print(videourlList)
