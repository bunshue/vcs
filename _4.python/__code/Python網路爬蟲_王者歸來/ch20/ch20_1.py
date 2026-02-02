# ch20_1.py
import requests, bs4, json
from pprint import pprint

url = 'https://maps.googleapis.com/maps/api/geocode/json?address=總統府&key=YOUR_API_KEY'
gmap = requests.get(url)
gsoup = bs4.BeautifulSoup(gmap.text, 'lxml')
g_info = json.loads(gsoup.text)

data = g_info['results'][0]
address = data['formatted_address']
lat = data['geometry']['location']['lat']
lng = data['geometry']['location']['lng']
print('地址 : ', address)
print('緯度 : ', lat)
print('經度 : ', lng)






    




    
