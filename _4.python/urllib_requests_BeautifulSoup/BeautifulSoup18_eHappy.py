import requests

#文淵閣工作室官網
url = 'http://www.e-happy.com.tw'
html = requests.get(url)
html.encoding="utf-8"
print(html.text)



import requests
#文淵閣工作室官網
url = 'http://www.e-happy.com.tw'
html = requests.get(url)
html.encoding="utf-8"

htmllist = html.text.splitlines()   #將網頁資料一行一行地分割成串列
for row in htmllist:
   print(row)


   
from bs4 import BeautifulSoup
import requests

#文淵閣工作室官網
url = 'http://www.e-happy.com.tw'
html = requests.get(url)
html.encoding="utf-8"

soup = BeautifulSoup(html.text,"html.parser")
links = soup.find_all("a") # 讀取 <a>
for link in links:
    href = link.get("href") # 讀取 href 屬性內容
    # 判斷內容是否為非 None，並且開頭文字是 http://
    if  href != None and href.startswith("http://"): 
        print(href)


