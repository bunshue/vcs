# python import module : requests

'''
print('取得網頁資料 1')
import requests
www = requests.get("https://tw.news.yahoo.com/most-popular/")
print(www.text)


print('取得網頁資料 2')
import requests
www = requests.get(url='http://www.itwhy.org') # 最基本的GET请求

print(www.status_code) # 获取返回状态, 200 為 OK
print(www.text) # 获取返回状态

print('取得網頁資料 3')
r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'}) #带参数的GET请求 print(r.url) print(r.text) #打印解码后的返回数据
print(r)
'''

'''fail
print('取得網頁資料 4')
import requests
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1';
payload = {'city':'130010'}
weather_data = requests.get(api_url, params = payload).json()
print(weather_data['forecasts'][0]['dateLabel'] + '的天氣是：' + weather_data['forecasts'][0]['telop'])
'''

'''fail
print('取得網頁資料 5')
import requests
import pprint
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
weather_data = requests.get(api_url).json()
pprint.pprint(weather_data)
'''

print('取得網頁資料 6')
import requests
r = requests.get('http://tw.yahoo.com')
print(r.text)

''' OK many
print('取得網頁資料 7')
import requests
import pprint
r = requests.get('http://tw.yahoo.com')
pprint.pprint(r.text)
'''

''' fail
print('取得網頁資料 8')
import requests
import pprint
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
weather_data = requests.get(api_url).json()
pprint.pprint(weather_data)
'''

''' fail
print('取得網頁資料 9')
url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
paload = {'city':'130010'}
weather_data = requests.get(url, params = paload).json()
pprint.pprint(weather_data['forecasts'][0])

'''

''' OK
print('取得網頁資料 10')
import requests, pprint
api_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'json', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}
wiki_data = requests.get(api_url, params = api_params)
pprint.pprint(wiki_data)
'''

print('OK')

