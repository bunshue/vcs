import requests
from bs4 import BeautifulSoup

url = 'https://autos.udn.com/autos/story/9060/2187994'

html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, 'html.parser')
#print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

links = soup.find_all("a")
for link in links:
    try:
        if ".jpg" in link['href']:
            print(link['href'])
    except:
        pass
