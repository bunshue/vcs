# ch20_3.py
import googlemaps
from pprint import pprint

api_key = 'YOUR_API_KEY'
gmap_obj = googlemaps.Client(key=api_key)
gmap_info = gmap_obj.geocode('總統府')

address = gmap_info[0]['formatted_address']
lat = gmap_info[0]['geometry']['location']['lat']
lng = gmap_info[0]['geometry']['location']['lng']
print('地址 : ', address)
print('緯度 : ', lat)
print('經度 : ', lng)







    




    
