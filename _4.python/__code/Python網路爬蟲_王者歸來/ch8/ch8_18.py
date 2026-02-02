# ch8_18.py
import requests

url = 'http://api.ipstack.com/www.mcut.edu.tw?access_key=Your API Key'
urlfile = requests.get(url)
ip_info = urlfile.json()
print('資料型態 ', type(ip_info))

print('IP地址 : ', ip_info['ip'])
print('洲名   : ', ip_info['continent_name'])
print('國名   : ', ip_info['country_name'])
print('城市名 : ', ip_info['city'])
print('緯度   : ', ip_info['latitude'])
print('經度   : ', ip_info['longitude'])











    
