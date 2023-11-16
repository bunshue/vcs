import requests
from bs4 import BeautifulSoup

req=requests.get("http://news.baidu.com/tech")
soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")
largefeaturepowenA2=soup.select('.fb-list')
largefeature0=largefeaturepowenA2[0]
print(largefeature0)
for area in largefeature0.select('li'):
  t1=area.select('a')
  print(area.select('a')[0].contents[0])
  
