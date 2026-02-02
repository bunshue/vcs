# ch20_2.py
import googlemaps
from pprint import pprint

api_key = 'YOUR_API_KEY'
gmap_obj = googlemaps.Client(key=api_key)
gmap_info = gmap_obj.geocode('總統府')
pprint(gmap_info)                       # 可以一行列印一個元素







    




    
