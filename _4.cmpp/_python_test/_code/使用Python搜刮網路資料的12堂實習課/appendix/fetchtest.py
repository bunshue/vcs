import requests
from bs4 import BeautifulSoup

url = 'https://www.nkust.edu.tw/'
sel = '#sm_div_cmb_1_15062 > div > div > section'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

print()
print('找第一個標籤p')
target = soup.p
print(target)
print()


print('找第一個標籤p')
target = soup.p
print(target)
print()





