import requests
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}
weather_data = requests.get(api_url, params = payload).json()
for weather in weather_data['forecasts']:
    print(weather['dateLabel'] + '的天氣是：' + weather['telop'])
