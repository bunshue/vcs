import requests
from bs4 import BeautifulSoup

print('查詢中央銀行匯率')

url = 'https://rate.bot.com.tw/xrt/all/day'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
cells = soup.select('table tr td')
print(cells)
