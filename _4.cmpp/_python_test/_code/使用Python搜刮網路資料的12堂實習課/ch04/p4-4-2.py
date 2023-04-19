import requests, re
from bs4 import BeautifulSoup

url = 'https://autos.udn.com/autos/story/9060/2187994'

html_data = requests.get(url)

soup = BeautifulSoup(html_data.text, 'html.parser')

regex = r'http.+jpg'
links = soup.find_all("a")
for link in links:
    try:
        if ".jpg" in link['href']:
            print(link['href'])
            target = link['href']
            for item in re.findall(regex, target):
                print(item)
    except:
        pass
