# python import module : requests

import requests

#無參數
print('取得網頁資料 4')
r = requests.get('http://tw.yahoo.com')
print(r.text)

print('取得網頁資料 5')
import pprint
r = requests.get('http://tw.yahoo.com')
#pprint.pprint(r.text)  #OK many

print('取得網頁資料 1')
www = requests.get("https://tw.news.yahoo.com/most-popular/")
print(www.text)

print('取得網頁資料 2')
www = requests.get(url='http://www.itwhy.org') # 最基本的GET请求
print(www.status_code) # 获取返回状态, 200 為 OK
print(www.text) # 获取返回状态

print('取得網頁資料 9')
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
tree = ET.fromstring(content.text)
print('根目錄標籤：' + tree.tag)
print('根目錄屬性：' + str(tree.attrib))
print('根目錄值：' + str(tree.text))


print('取得網頁資料 10')
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
tree = ET.fromstring(content.text)

item = tree[0].find('item')
print('find 方法：' + item[0].text)

items = tree[0].findall('item')
print('findall 方法：' + items[0][0].text)

items = list(tree.iter(tag='item'))
print('iter 方法：' + items[0][0].text)

#有參數
print('取得網頁資料 3')
r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'}) #带参数的GET请求 print(r.url) print(r.text) #打印解码后的返回数据
print(r)

print('取得網頁資料 6')
import pprint
api_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'json', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}
wiki_data = requests.get(api_url, params = api_params)
pprint.pprint(wiki_data)


print('取得網頁資料 7')
import codecs
api_base_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}
wiki_data = requests.get(api_base_url, params = api_params)
fo = codecs.open('wiki搜尋結果1.html', 'w', 'utf-8')
#fo = open('wiki搜尋結果222.html', 'w')
fo.write(wiki_data.text)
fo.close()


print('取得網頁資料 8')
import codecs
search_word = 'lion'
api_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'prop':'revisions', 'rvprop':'content'}
api_params['titles'] = search_word
wiki_data = requests.get(api_url, params = api_params)
fo = codecs.open('wiki搜尋結果2' + search_word + '.html', 'w', 'utf-8')
#fo = open('bbbbb'+ search_word + '.html', 'w')
fo.write(wiki_data.text)
fo.close()

print('作業完成')





#http://weather.livedoor.com/forecast/webservice/json/v1


'''fail
print('取得網頁資料 1')
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1';
payload = {'city':'130010'}
weather_data = requests.get(api_url, params = payload).json()
print(weather_data['forecasts'][0]['dateLabel'] + '的天氣是：' + weather_data['forecasts'][0]['telop'])
'''

'''fail
print('取得網頁資料 2')
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}
weather_data = requests.get(api_url, params = payload).json()
print(weather_data['forecasts'][0]['dateLabel'] + '的天氣是：' + weather_data['forecasts'][0]['telop'])
print(weather_data['forecasts'][1]['dateLabel'] + '的天氣是：' + weather_data['forecasts'][1]['telop'])
print(weather_data['forecasts'][2]['dateLabel'] + '的天氣是：' + weather_data['forecasts'][2]['telop'])
'''

'''fail
print('取得網頁資料 3')
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}
weather_data = requests.get(api_url, params = payload).json()
for weather in weather_data['forecasts']:
    print(weather['dateLabel'] + '的天氣是：' + weather['telop'])

print('取得網頁資料 4')
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}
weather_data = requests.get(api_url, params = payload).json()
for weather in weather_data['forecasts']:
    print(weather)
'''


'''fail
print('取得網頁資料 5')
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1';
payload = {'city':'130010'}
weather_data = requests.get(api_url, params = payload).json()
print(weather_data['forecasts'][0]['dateLabel'] + '的天氣是：' + weather_data['forecasts'][0]['telop'])
'''

'''fail
print('取得網頁資料 6')
import pprint
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
weather_data = requests.get(api_url).json()
pprint.pprint(weather_data)
'''


''' fail
print('取得網頁資料 7')
import pprint
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
weather_data = requests.get(api_url).json()
pprint.pprint(weather_data)
'''

''' fail
print('取得網頁資料 8')
url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
paload = {'city':'130010'}
weather_data = requests.get(url, params = paload).json()
pprint.pprint(weather_data['forecasts'][0])

'''


'''

print('取得網頁資料 9')

url = 'http://www.com.tw/exam/check_0001_NO_0_101_0_3.html'
name = input("請輸入要查詢的姓名:")
html = requests.get(url).text
print(html)
if name in html:
    print("恭喜名列金榜")
else:
    print("不好意思，榜單中找不到{}".format(name))
'''
'''
print('取得網頁資料 10')
import re

regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
url = 'http://icho.chem.ntnu.edu.tw/pub/54con/54con.html'

html = requests.get(url).text

emails = re.findall(regex,html)
for email in emails:
    print(email)
'''



