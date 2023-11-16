import requests
from bs4 import BeautifulSoup

req=requests.get("http://www.powenko.com/wordpress")
soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")
largefeaturepowenA2=soup.select('.largefeaturepowenA2')
largefeature0=largefeaturepowenA2[0]
for area in largefeature0.select('.area'):	
  # print(area.select('a')[1].text)
  t1=area.select('a')
  print(area.select('a')[1].contents[0])
