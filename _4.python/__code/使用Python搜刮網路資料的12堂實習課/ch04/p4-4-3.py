import requests
import re
import urllib
import os
import time
from bs4 import BeautifulSoup

url = 'https://autos.udn.com/autos/story/9060/2187994'

html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, 'html.parser')
#print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

regex = r'http.+jpg'
links = soup.find_all("a")

print(links)

photos = list()

for link in links:
    try:
        if ".jpg" in link['href']:
            print(link['href'])
            target = link['href']
            for item in re.findall(regex, target):
                photos.append(item)
    except:
        pass

for link in photos:
    item = urllib.parse.urlparse(link)
    q = urllib.parse.parse_qs(item.query)
    target = urllib.parse.urlparse(q['u'][0])
    filename = os.path.basename(target.path)
    urllib.request.urlretrieve(link, os.path.join("images", filename))
    print("Storing " + filename)
    time.sleep(3)
    
print("Done...")
