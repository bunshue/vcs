# ch3_33.py
import requests, json

url = 'https://www.httpbin.org/post'
form_data = {'gender':'M','page':'1'}
r = requests.post(url, json=form_data)
print(r.url)
print('-'*70)
print(r.text)





