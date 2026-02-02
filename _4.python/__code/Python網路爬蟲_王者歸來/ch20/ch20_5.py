# ch20_5.py
import requests, bs4, json
from pprint import pprint

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=25.0329694,121.5654177&radius=3500&type=school&key=YOUR_API_KEY'
gmap = requests.get(url)
gsoup = bs4.BeautifulSoup(gmap.text, 'lxml')
g_info = json.loads(gsoup.text)
schools = g_info['results']
for data in schools:
    print(data['name'])


    







    




    
