# ch3_31.py
import requests

url = 'https://www.httpbin.org/post'
form_data = {'gender':'M','page':'1'}
r = requests.post(url, data=form_data)
print(r.url)
print('-'*70)
print(r.text)





