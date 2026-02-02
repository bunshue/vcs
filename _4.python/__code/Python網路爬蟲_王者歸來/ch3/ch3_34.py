# ch3_34.py
import requests, json

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url = 'https://www.httpbin.org/post'
form_data = {'gender':'M','page':'1'}
r = requests.post(url, json=form_data, headers=headers)
print(r.url)
print('-'*70)
print('r.request.headers :\n', r.request.headers)
print('-'*70)
print('r.headers :\n', r.headers)







