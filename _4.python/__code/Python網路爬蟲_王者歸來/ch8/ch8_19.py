# ch8_19.py
import requests

url_head = 'http://api.ipstack.com/'
url_tail = '?access_key=Your API Key'
getip = input('請輸入網域或IP : ')
url = url_head + getip + url_tail
urlfile = requests.get(url.strip())
ip_info = urlfile.json()

print('IP地址 : ', ip_info['ip'])
print('洲名   : ', ip_info['continent_name'])
print('國名   : ', ip_info['country_name'])
print('城市名 : ', ip_info['city'])
print('緯度   : ', ip_info['latitude'])
print('經度   : ', ip_info['longitude'])











    
