from bs4 import BeautifulSoup
import time
import requests

url = 'https://www.cwb.gov.tw/V8/C/W/OBS_County.html?ID=68'
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

sel = '#stations > tr'
rows = soup.select(sel)
data = list()
for row in rows:
    try:
        header = row.find_all('th')
        fields = row.find_all('td')
        current_time = fields[0].text
        print("資料查詢時間", current_time)
        data.append((header[0].a.text.strip(), float(fields[1].text), int(fields[7].text)))
    except:
        pass

print(data)
