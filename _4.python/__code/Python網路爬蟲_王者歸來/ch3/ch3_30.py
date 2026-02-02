# ch3_30.py
import requests

url = 'https://www.httpbin.org/get'
form_data = {'gender':'M','page':'1'}
r = requests.get(url, params=form_data)
print(r.url)





