# python import module : requests





import requests
www = requests.get("https://tw.news.yahoo.com/most-popular/")
print('取得網頁資料 1')
print(www.text)




import requests
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1';
payload = {'city':'130010'}
weather_data = requests.get(api_url, params = payload).json()
print('取得網頁資料 2')
print(weather_data['forecasts'][0]['dateLabel'] + '的天氣是：' + weather_data['forecasts'][0]['telop'])



print('取得網頁資料 3333')
print('取得網頁資料 4444')
import requests

import pprint

api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'

weather_data = requests.get(api_url).json()

pprint.pprint(weather_data)



