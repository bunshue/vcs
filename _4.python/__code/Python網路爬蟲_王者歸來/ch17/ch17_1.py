# ch17_1.py
import requests, bs4

url = 'https://www.thsrc.com.tw/tw/TimeTable/SearchResult'
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')
stations = objSoup.find('select', id='StartStation').find_all('option')
print("高鐵站名與ID")
for station in stations:
    if station['value']:
        print(station.text.strip(), ' : ', station['value'])












