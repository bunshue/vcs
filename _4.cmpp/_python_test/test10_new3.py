# Python 新進測試 3


def area(radius):

	result = radius * radius * 3.14

	return result




def washingMachine():

	print('注水')

	print('輕柔清洗')

	print('洗淨洗劑')

	print('脫水')

	print('烘乾')


washingMachine()


def washingMachine(mode):

	print('注水')

	if (mode == 'soft'):

		print('輕柔清洗')

	elif (mode == 'hard'):

		print('強力清洗')

	else:

		print('一般清洗')




mode = 'soft'

if (mode == 'soft'):

	print('輕柔清洗')

elif (mode == 'hard'):

	print('強力清洗')

else:

	print('一般清洗')





import calendar

print(calendar.__file__)


import requests
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1';
payload = {'city':'130010'}
weather_data = requests.get(api_url, params = payload).json()
print(weather_data['forecasts'][0]['dateLabel'] + '的天氣是：' + weather_data['forecasts'][0]['telop'])





import requests

import pprint

api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'

weather_data = requests.get(api_url).json()

pprint.pprint(weather_data)




