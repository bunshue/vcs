# ch20_4.py
import requests, bs4, json
from pprint import pprint

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=25.0329694,121.5654177&radius=3500&type=school&key=YOUR_API_KEY'
gmap = requests.get(url)
gsoup = bs4.BeautifulSoup(gmap.text, 'lxml')
g_info = json.loads(gsoup.text)
schools = g_info['results']
print('列出搜尋到結果的資料型態 : ', type(schools))
print('列出搜尋到結果的資料長度 : ', len(schools))
print('列出搜尋到第0筆資料型態  : ', type(schools[0]))
print('列出第0筆資料內容')
pprint(schools[0])


    







    




    
