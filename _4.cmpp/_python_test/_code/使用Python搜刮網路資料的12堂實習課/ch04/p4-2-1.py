import requests
from bs4 import BeautifulSoup

url = 'https://www.nkust.edu.tw/p/403-1000-12-1.php'

html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, 'html.parser')
#print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

links = soup.find_all('a')
for link in links:
    print(link)
