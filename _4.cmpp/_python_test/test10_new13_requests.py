# Python 新進測試 13





import requests

r = requests.get('http://tw.yahoo.com')

print(r.text)


import requests

import pprint

r = requests.get('http://tw.yahoo.com')

pprint.pprint(r.text)



import requests

import pprint

api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'

weather_data = requests.get(api_url).json()

pprint.pprint(weather_data)



url = 'http://weather.livedoor.com/forecast/webservice/json/v1'

paload = {'city':'130010'}

weather_data = requests.get(url, params = paload).json()





pprint.pprint(weather_data['forecasts'][0]) 


import requests, pprint

api_url = 'https://zh.wikipedia.org/w/api.php'

api_params = {'format':'json', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}

wiki_data = requests.get(api_url, params = api_params)

pprint.pprint(wiki_data)



