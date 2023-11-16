import requests
from bs4 import BeautifulSoup

req=requests.get("https://www.chinatimes.com/?chdtv")
soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")

for listRight in soup.select('.focus-news'):
   for line in listRight.select('.title'):
     print(line.select('a')[0].text)
