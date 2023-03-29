# python import module : requests

import requests

'''
#無參數

print('取得網頁資料 4')
url = 'https://tw.news.yahoo.com/most-popular/'
url = 'http://www.itwhy.org'
url = 'http://tw.yahoo.com'
html_data = requests.get(url)
print(html_data.text)

print('取得網頁資料 5')
import pprint
url = 'http://tw.yahoo.com'
html_data = requests.get(url)
#pprint.pprint(html_data.text)  #OK many
'''


'''

#有參數
print('取得網頁資料 3')
html_data = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'}) #带参数的GET请求
print(html_data.url)
print(html_data.text) #打印解码后的返回数据
print(html_data)

print('取得網頁資料 6')
import pprint
api_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'json', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}
html_data = requests.get(api_url, params = api_params)
pprint.pprint(html_data)


print('取得網頁資料 7')
import codecs
api_base_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}
html_data = requests.get(api_base_url, params = api_params)
fo = codecs.open('wiki搜尋結果1.html', 'w', 'utf-8')
#fo = open('wiki搜尋結果222.html', 'w')
fo.write(html_data.text)
fo.close()


print('取得網頁資料 8')
import codecs
search_word = 'lion'
api_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'prop':'revisions', 'rvprop':'content'}
api_params['titles'] = search_word
html_data = requests.get(api_url, params = api_params)
fo = codecs.open('wiki搜尋結果2' + search_word + '.html', 'w', 'utf-8')
#fo = open('bbbbb'+ search_word + '.html', 'w')
fo.write(html_data.text)
fo.close()

print('作業完成')


'''

'''
#http://weather.livedoor.com/forecast/webservice/json/v1


print('取得網頁資料 1')
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1';
payload = {'city':'130010'}
#html_data = requests.get(api_url, params = payload).json()

#print(html_data['forecasts'][0]['dateLabel'] + '的天氣是：' + html_data['forecasts'][0]['telop'])

print('取得網頁資料 2')
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}

#html_data = requests.get(api_url, params = payload).json()
#print(html_data['forecasts'][0]['dateLabel'] + '的天氣是：' + html_data['forecasts'][0]['telop'])
#print(html_data['forecasts'][1]['dateLabel'] + '的天氣是：' + html_data['forecasts'][1]['telop'])
#print(html_data['forecasts'][2]['dateLabel'] + '的天氣是：' + html_data['forecasts'][2]['telop'])

print('取得網頁資料 3')
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}
html_data = requests.get(api_url, params = payload).json()
for weather in html_data['forecasts']:
    print(weather['dateLabel'] + '的天氣是：' + weather['telop'])

print('取得網頁資料 4')
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}
html_data = requests.get(api_url, params = payload).json()
for weather in html_data['forecasts']:
    print(weather)
'''



'''fail
print('取得網頁資料 5')
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1';
payload = {'city':'130010'}
html_data = requests.get(api_url, params = payload).json()
print(html_data['forecasts'][0]['dateLabel'] + '的天氣是：' + html_data['forecasts'][0]['telop'])
'''

'''fail
print('取得網頁資料 6')
import pprint
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
html_data = requests.get(api_url).json()
pprint.pprint(html_data)
'''


''' fail
print('取得網頁資料 7')
import pprint
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
html_data = requests.get(api_url).json()
pprint.pprint(html_data)
'''

''' fail
print('取得網頁資料 8')
url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
paload = {'city':'130010'}
html_data = requests.get(url, params = paload).json()
pprint.pprint(html_data['forecasts'][0])

'''


'''
print('取得網頁資料 9')

url = 'http://www.com.tw/exam/check_0001_NO_0_101_0_3.html'
name = input("請輸入要查詢的姓名:")
html_data = requests.get(url).text
print(html_data)
if name in html_data:
    print("恭喜名列金榜")
else:
    print("不好意思，榜單中找不到{}".format(name))

'''

'''
print('取得網頁資料 10')
import re

regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
url = 'http://icho.chem.ntnu.edu.tw/pub/54con/54con.html'
html_data = requests.get(url).text

emails = re.findall(regex, html_data)
for email in emails:
    print(email)

'''



